"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py reads NIST's JSON schemas and compares each
with its pinned hash. These tests replace its one network call, `_get`, or its
opener, so they run offline. They show what the report says and how the script
exits in each case it knows: nothing moved, a changed file, a file gone, a copy
that differs, and a check that could not run, which is not called a change.
"""

import hashlib
import http.client
import importlib.util
import io
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
UPSTREAM = ROOT / "upstream"
SSVC = "ssvc-v2.0.3.json"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _unchanged(watch, monkeypatch):
    """Answer each file with bytes that hash to its pin. The copies are those
    bytes; the SSVC file's bytes are not held here, so its hash comes through a
    stubbed _sha256 and its body is its structure."""
    bodies = {}
    for name, pin in watch.PINNED_SHA256.items():
        held = watch.STRUCTURE_ONLY.get(name, name)
        bodies[name] = (UPSTREAM / held).read_bytes()
    real = watch._sha256
    pins = {real(body): watch.PINNED_SHA256[n] for n, body in bodies.items()}
    monkeypatch.setattr(watch, "_sha256", lambda data: pins.get(real(data), real(data)))
    monkeypatch.setattr(watch, "_get", lambda url: bodies[url[len(watch.BASE) :]])
    return bodies


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_moved(watch, monkeypatch, tmp_path):
    _unchanged(watch, monkeypatch)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "**" not in text
    assert text.count("answers with its pinned hash") == len(watch.PINNED_SHA256)


def test_a_changed_file_is_a_finding_that_quotes_the_title(
    watch, monkeypatch, tmp_path
):
    bodies = _unchanged(watch, monkeypatch)
    name = "cve_api_json_2.0.schema"
    bodies[name] = json.dumps({"title": "JSON Schema for NVD version 9.9.9"}).encode()
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**NIST changed `{name}`.**" in text
    assert "`JSON Schema for NVD version 9.9.9`" in text


def test_server_text_stays_on_one_line_in_a_code_span(watch, monkeypatch, tmp_path):
    """A title that tries to close the span or start a paragraph cannot, so the
    issue the workflow opens from the report mentions no one."""
    bodies = _unchanged(watch, monkeypatch)
    name = "cve_api_json_2.0.schema"
    bodies[name] = json.dumps({"title": "x`\n\n@someone hello"}).encode()
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "`x' @someone hello`" in text


def test_a_file_that_is_gone_is_a_finding(watch, monkeypatch, tmp_path):
    _unchanged(watch, monkeypatch)
    real = watch._get

    def gone(url):
        if url.endswith("cve_affected_1.0.json"):
            raise urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b""))
        return real(url)

    monkeypatch.setattr(watch, "_get", gone)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**NIST no longer serves `cve_affected_1.0.json`:** it answers 404." in text


@pytest.mark.parametrize(
    "error",
    [
        urllib.error.URLError("timed out"),
        urllib.error.HTTPError("u", 503, "Unavailable", {}, io.BytesIO(b"")),
        urllib.error.HTTPError("u", 403, "Forbidden", {}, io.BytesIO(b"")),
        http.client.IncompleteRead(b"", 10),
        TimeoutError("timed out"),
        ValueError("too large"),
    ],
    ids=lambda e: type(e).__name__ + str(getattr(e, "code", "")),
)
def test_a_failed_request_could_not_run_and_is_not_drift(
    watch, monkeypatch, tmp_path, error
):
    """A network failure says the check could not run, names nothing as changed,
    still checks the other files, and exits 2, not 1."""
    _unchanged(watch, monkeypatch)
    real = watch._get

    def fails(url):
        if url.endswith("cpe_api_json_2.0.schema"):
            raise error
        return real(url)

    monkeypatch.setattr(watch, "_get", fails)
    code, text = _run(watch, tmp_path)
    assert code == 2
    assert "The check of `cpe_api_json_2.0.schema` could not run" in text
    assert "This says nothing about the file." in text
    assert "NIST changed" not in text
    assert "`cve_api_json_2.0.schema` answers with its pinned hash." in text


@pytest.mark.parametrize("body", [b"[1, 2]", b"<html>not json</html>", b"\xff\xfe"])
def test_an_answer_of_the_wrong_shape_could_not_run(watch, monkeypatch, tmp_path, body):
    bodies = _unchanged(watch, monkeypatch)
    bodies["cpe_api_json_2.0.schema"] = body
    code, text = _run(watch, tmp_path)
    assert code == 2, text
    assert "could not run" in text


def test_drift_outranks_a_failed_request(watch, monkeypatch, tmp_path):
    bodies = _unchanged(watch, monkeypatch)
    bodies["cve_api_json_2.0.schema"] = b'{"title": "new"}'
    real = watch._get

    def fails(url):
        if url.endswith("cpe_api_json_2.0.schema"):
            raise urllib.error.URLError("refused")
        return real(url)

    monkeypatch.setattr(watch, "_get", fails)
    code, _ = _run(watch, tmp_path)
    assert code == 1


def test_a_copy_that_differs_is_a_finding(watch, monkeypatch, tmp_path):
    _unchanged(watch, monkeypatch)
    copy = tmp_path / "copy"
    copy.mkdir()
    monkeypatch.setattr(watch, "COPY", copy)
    (copy / "ssvc-v2.0.3.structure.json").write_bytes(
        (UPSTREAM / "ssvc-v2.0.3.structure.json").read_bytes()
    )
    (copy / "cve_api_json_2.0.schema").write_text("{}", encoding="utf-8")
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "`cve_api_json_2.0.schema` differs from its pin" in text
    assert "`cpe_api_json_2.0.schema` is missing" in text


def test_a_structure_that_is_not_the_files_is_a_finding(watch, monkeypatch, tmp_path):
    bodies = _unchanged(watch, monkeypatch)
    pin = watch.PINNED_SHA256[SSVC]
    document = json.loads(bodies[SSVC])
    document["properties"]["added"] = {"type": "string"}
    changed = json.dumps(document).encode()
    bodies[SSVC] = changed
    real = watch._sha256
    monkeypatch.setattr(
        watch, "_sha256", lambda data: pin if data == changed else real(data)
    )
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "`upstream/ssvc-v2.0.3.structure.json` is not the structure" in text


def test_structure_drops_prose_and_keeps_a_property_named_like_prose(watch):
    document = {
        "title": "drop",
        "description": "drop",
        "properties": {"title": {"type": "string", "description": "drop"}},
        "definitions": {"description": {"examples": ["drop"], "type": "string"}},
    }
    assert watch.structure(document) == {
        "properties": {"title": {"type": "string"}},
        "definitions": {"description": {"type": "string"}},
    }


def test_get_refuses_an_answer_larger_than_the_cap(watch, monkeypatch):
    class Big(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return False

    big = Big(b"x" * (watch.MAX_BYTES + 10))
    monkeypatch.setattr(watch, "_open", lambda req, timeout: big)
    with pytest.raises(ValueError, match="larger than"):
        watch._get(watch.BASE + "cve_api_json_2.0.schema")


@pytest.mark.parametrize(
    "target",
    [
        "http://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema",
        "https://example.org/cve_api_json_2.0.schema",
        "https://csrc.nist.gov.example.org/x",
    ],
)
def test_a_redirect_off_the_host_is_refused(watch, target):
    handler = watch._ExpectedHostRedirect()
    with pytest.raises(ValueError, match="leads off"):
        handler.redirect_request(None, None, 302, "Found", {}, target)


def test_a_redirect_on_the_host_is_followed(watch):
    import urllib.request

    handler = watch._ExpectedHostRedirect()
    req = urllib.request.Request(watch.BASE + "x")
    new = handler.redirect_request(req, None, 302, "Found", {}, watch.BASE + "y")
    assert new.full_url == watch.BASE + "y"


def test_the_pins_cover_every_copy():
    """Every file under upstream/ other than the README is pinned, by name or
    as the structure of a pinned file, so nothing unpinned sits there."""
    spec = importlib.util.spec_from_file_location("watch_pins", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    held = {
        str(p.relative_to(UPSTREAM)) for p in UPSTREAM.rglob("*") if p.is_file()
    } - {"README.md"}
    expected = {module.STRUCTURE_ONLY.get(name, name) for name in module.PINNED_SHA256}
    assert held == expected
    assert all(len(pin) == 64 for pin in module.PINNED_SHA256.values())
    assert hashlib.sha256(b"").hexdigest() not in module.PINNED_SHA256.values()
