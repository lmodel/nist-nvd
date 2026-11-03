"""Checks the fetch of NVD's modified feed against stubbed downloads.

scripts/fetch_nvd_feed.py downloads the feed and keeps it only when it matches the
size and SHA-256 that the feed's own .meta file gives. These tests replace its
opener with a stub, so they run offline. They show that a matching download is
kept, that a wrong, oversized or cut-off one is deleted, that a feed that moved
between the two requests gets a second try, and that the script refuses an address
or a redirect off nvd.nist.gov.
"""

import gzip
import hashlib
import http.client
import importlib.util
import io
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "fetch_nvd_feed.py"
GOOD = b'{"format": "NVD_CVE", "vulnerabilities": []}\n'


@pytest.fixture
def fetch():
    spec = importlib.util.spec_from_file_location("fetch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _meta(data: bytes) -> bytes:
    packed = gzip.compress(data)
    return (
        "lastModifiedDate:2026-11-03T14:00:07-05:00\r\n"
        f"size:{len(data)}\r\nzipSize:1\r\ngzSize:{len(packed)}\r\n"
        f"sha256:{hashlib.sha256(data).hexdigest().upper()}\r\n"
    ).encode()


class _Answer(io.BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False


def _serve(fetch, monkeypatch, answers):
    """Answer each request from a list per address, the last answer repeating."""
    asked = []

    def opener(req, timeout):
        asked.append(req.full_url)
        queue = answers[req.full_url.rsplit(".", 1)[1]]
        body = queue.pop(0) if len(queue) > 1 else queue[0]
        if isinstance(body, Exception):
            raise body
        return _Answer(body)

    monkeypatch.setattr(fetch, "_open", opener)
    return asked


def test_a_matching_download_lands(fetch, monkeypatch, tmp_path):
    _serve(fetch, monkeypatch, {"meta": [_meta(GOOD)], "gz": [gzip.compress(GOOD)]})
    code, line = fetch.fetch(tmp_path)
    assert code == 0, line
    assert (tmp_path / fetch.NAME).read_bytes() == GOOD
    assert [p.name for p in tmp_path.iterdir()] == [fetch.NAME]


def test_a_matching_copy_is_kept_without_a_download(fetch, monkeypatch, tmp_path):
    (tmp_path / fetch.NAME).write_bytes(GOOD)
    asked = _serve(fetch, monkeypatch, {"meta": [_meta(GOOD)], "gz": [b"never read"]})
    code, line = fetch.fetch(tmp_path)
    assert code == 0 and "present" in line
    assert not [u for u in asked if u.endswith(".gz")]


@pytest.mark.parametrize(
    "served",
    [GOOD.replace(b"[]", b"{}"), GOOD + b" " * 10],
    ids=["wrong", "oversized"],
)
def test_a_wrong_or_oversized_download_is_deleted(fetch, monkeypatch, tmp_path, served):
    _serve(fetch, monkeypatch, {"meta": [_meta(GOOD)], "gz": [gzip.compress(served)]})
    code, line = fetch.fetch(tmp_path)
    assert code == 1
    assert "does not match its .meta file, twice" in line
    assert list(tmp_path.iterdir()) == []


def test_a_feed_that_moved_between_requests_gets_a_second_try(fetch, monkeypatch, tmp_path):
    newer = GOOD + b"\n"
    asked = _serve(
        fetch,
        monkeypatch,
        {"meta": [_meta(GOOD), _meta(newer)], "gz": [gzip.compress(newer)]},
    )
    code, line = fetch.fetch(tmp_path)
    assert code == 0, line
    assert (tmp_path / fetch.NAME).read_bytes() == newer
    assert len([u for u in asked if u.endswith(".meta")]) == 2


def test_a_corrupt_gzip_gets_a_second_try_and_then_fails(fetch, monkeypatch, tmp_path):
    _serve(fetch, monkeypatch, {"meta": [_meta(GOOD)], "gz": [b"not gzip at all"]})
    code, _ = fetch.fetch(tmp_path)
    assert code == 1
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize(
    "error",
    [
        OSError("refused"),
        TimeoutError("timed out"),
        http.client.IncompleteRead(b"", 10),
        ValueError("a redirect leads off the host"),
    ],
    ids=lambda e: type(e).__name__,
)
def test_a_failed_request_could_not_run(fetch, monkeypatch, tmp_path, error):
    """A network failure exits 2 and says so: it says nothing about NVD's data."""
    _serve(fetch, monkeypatch, {"meta": [_meta(GOOD)], "gz": [error]})
    code, line = fetch.fetch(tmp_path)
    assert code == 2
    assert line.startswith("the fetch could not run")
    assert list(tmp_path.iterdir()) == []


def test_a_meta_of_the_wrong_shape_could_not_run(fetch, monkeypatch, tmp_path):
    _serve(fetch, monkeypatch, {"meta": [b"<html>a page</html>"], "gz": [b""]})
    code, _ = fetch.fetch(tmp_path)
    assert code == 2


@pytest.mark.parametrize(
    "meta",
    [
        "size:1\ngzSize:1\nsha256:abc\n",
        f"size:{10**12}\ngzSize:1\nsha256:{'0' * 64}\n",
        f"size:1\ngzSize:{10**12}\nsha256:{'0' * 64}\n",
        f"size:0\ngzSize:1\nsha256:{'0' * 64}\n",
    ],
    ids=["short-hash", "huge-size", "huge-gzip", "no-size"],
)
def test_a_meta_that_asks_too_much_is_refused(fetch, meta):
    with pytest.raises(ValueError):
        fetch.parse_meta(meta)


def test_a_meta_larger_than_the_cap_is_refused(fetch, monkeypatch):
    monkeypatch.setattr(fetch, "_open", lambda req, timeout: _Answer(b"x" * 5000))
    with pytest.raises(ValueError, match="larger than"):
        fetch.read_meta()


@pytest.mark.parametrize(
    "url",
    [
        "http://nvd.nist.gov/feeds/x",
        "https://example.org/feeds/x",
        "https://nvd.nist.gov.example.org/x",
    ],
)
def test_an_address_off_the_host_is_refused(fetch, url):
    with pytest.raises(ValueError):
        fetch._check_address(url)
    handler = fetch._PinnedHostRedirect()
    with pytest.raises(ValueError):
        handler.redirect_request(None, None, 302, "Found", {}, url)


def test_a_redirect_on_the_host_is_followed(fetch):
    handler = fetch._PinnedHostRedirect()
    req = urllib.request.Request("https://nvd.nist.gov/a")
    new = handler.redirect_request(req, None, 302, "Found", {}, "https://nvd.nist.gov/b")
    assert new.full_url == "https://nvd.nist.gov/b"


def test_the_real_meta_form_parses(fetch):
    parsed = fetch.parse_meta(_meta(GOOD).decode())
    assert parsed["size"] == len(GOOD)
    assert parsed["sha256"] == hashlib.sha256(GOOD).hexdigest()
