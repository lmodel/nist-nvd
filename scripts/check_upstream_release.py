#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check NIST's NVD API 2.0 JSON schemas against the editions the schema renders.

NIST publishes the JSON schemas at https://csrc.nist.gov/schema/nvd/api/2.0/
with no release or git object, under addresses that stay the same when a file
changes. So this script compares each file's SHA-256 with its pin below.
upstream/ holds a copy of each file, unchanged, except NIST's SSVC schema, of
which it holds only the structure, for the reason NOTICE gives.

The script prints a Markdown report, and exits:

- 0 when every file answers with its pinned hash;
- 1 when a file differs from its pin or is gone, or its copy here differs;
- 2 when nothing differs but a check could not run, such as a refused, failed
  or cut-off request, an answer larger than the script reads, or an answer
  that is not a JSON object. That says nothing about NIST's files, so the
  report says the check could not run and does not call it a change.

Text a server chose, such as a schema's title or an error message, is quoted
as code on one line in the report, so the issue the workflow opens from it
cannot mention anyone. A redirect is followed only to an https address on
csrc.nist.gov. The script sends no token. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "upstream"
BASE = "https://csrc.nist.gov/schema/nvd/api/2.0/"
USER_AGENT = "lmodel-nist-nvd-watch"

# The one host a redirect may lead to.
HOST = "csrc.nist.gov"

# The most the script reads of one answer. The largest file is about 15 kB.
MAX_BYTES = 5_000_000

# Each file's path under BASE, and its SHA-256 as read on 2026-11-03.
# tests/test_upstream.py holds the copies under upstream/ and the schema
# modules' headers to these pins. Move them together when the schema moves.
PINNED_SHA256 = {
    "cve_api_json_2.0.schema": "2b9c4e8ab7e6e42aa17ea787f58167beff47c119c6f291405f86ac19c6149e01",
    "cpe_api_json_2.0.schema": "102ae482c48e8edfdd56ebae4e9d487675bf6499c4ee5479732a6b1b9e81df36",
    "cpematch_api_json_2.0.schema": "3e0bbadfe51a7f73f9fb4417889a9f5fe37ed47de1e3cd125db97b3b130e15c0",
    "cve_history_api_json_2.0.schema": "6c037873ddf8c8fe9a54d26c3438dd8d77cf0a8b3e375c04e171d6dc7b71b415",
    "ssvc-v2.0.3.json": "9d38b0ba856929d63b02025057ee0ba0a7844fe41fd5f176798d4aea4f2bedb9",
    "cve_affected_1.0.json": "6ad105e90486f4b82a949aef1af369b1ef1ce6720918d31cc158e11a26ff68ff",
    "external/cvss-v2.0.json": "1b2f6a71ad5e2fab32a7807dde521a4dd867eb7dad974e9c4e8fb7625cd6f0a2",
    "external/cvss-v3.0.json": "70e3032a93c7369da4d51042392aea420655850ee24d9812f53d8c09f5f31f03",
    "external/cvss-v3.1.json": "ba6499cc006baa2f8f13f074011ebfd16a1829207cf37773c33173ab66e46cbb",
    "external/cvss-v4.0.json": "b29e075556a8ec27303bb80f82acce253e1431c79d6a429bf5825e0335c92ce9",
}

# The file upstream/ holds only the structure of, and that structure's name.
STRUCTURE_ONLY = {"ssvc-v2.0.3.json": "ssvc-v2.0.3.structure.json"}

# What an answer's failure can raise: OSError covers a refused or failed
# request and a timeout, HTTPException a read cut off, ValueError an answer
# too large, bad JSON or a redirect off the host, and LookupError and
# TypeError an answer whose shape is not the one expected.
COULD_NOT_RUN = (
    OSError,
    http.client.HTTPException,
    ValueError,
    LookupError,
    TypeError,
)


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on HOST."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname != HOST:
            raise ValueError(f"a redirect leads off {HOST}, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> bytes:
    """The body of an answer, refused when it is larger than MAX_BYTES."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _code(text: object) -> str:
    """Text a server chose as a code span on one line, so it cannot mention a
    person or add a link in the issue. A blank line would end the span, so
    every run of spaces and line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def structure(document):
    """A JSON schema without its prose: every description, title and example
    goes, and the keys, types and requirements stay. A key of a `properties`
    map is a property's name, even when it reads `title`, so it stays."""
    if isinstance(document, list):
        return [structure(item) for item in document]
    if not isinstance(document, dict):
        return document
    return {
        key: {name: structure(sub) for name, sub in value.items()}
        if key in ("properties", "patternProperties", "definitions")
        and isinstance(value, dict)
        else structure(value)
        for key, value in document.items()
        if key not in ("description", "title", "examples")
    }


def check_file(name: str, pin: str) -> tuple[list[str], bool]:
    """A line for one published file, and whether it differs from its pin. A
    failed request raises, and main() reports that the check could not run."""
    try:
        body = _get(BASE + name)
    except urllib.error.HTTPError as err:
        if err.code not in (404, 410):
            raise
        return [f"- **NIST no longer serves `{name}`:** it answers {err.code}."], True
    found = _sha256(body)
    if found != pin:
        document = json.loads(body)
        if not isinstance(document, dict):
            raise TypeError(f"the answer from {name} is not a JSON object")
        return [
            f"- **NIST changed `{name}`.** Its SHA-256 is now {_code(found)}, not the "
            f"pinned `{pin[:16]}`; its title reads {_code(document.get('title'))}. "
            "Compare the file with `upstream/`, then move the copy, this script's pin "
            "and the schema's header together."
        ], True
    lines = [f"- `{name}` answers with its pinned hash."]
    if name in STRUCTURE_ONLY:
        held = json.loads((COPY / STRUCTURE_ONLY[name]).read_text(encoding="utf-8"))
        if structure(json.loads(body)) != held:
            return [
                f"- **`upstream/{STRUCTURE_ONLY[name]}` is not the structure of `{name}`.**"
            ], True
    return lines, False


def check_copies() -> tuple[list[str], bool]:
    """Report a copy under upstream/ that differs from its pin."""
    differing = []
    for name, pin in sorted(PINNED_SHA256.items()):
        if name in STRUCTURE_ONLY:
            continue
        path = COPY / name
        if not path.is_file():
            differing.append(f"  - `{name}` is missing from `upstream/`")
        elif _sha256(path.read_bytes()) != pin:
            differing.append(f"  - `{name}` differs from its pin")
    if not differing:
        return ["- Every copy under `upstream/` matches its pin."], False
    return [f"- **{len(differing)} problem(s) with the copies:**", *differing], True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, drift = check_copies()
    could_not_run = False
    # A check that cannot reach NIST becomes a line of the report rather than
    # a traceback, so the other files are still checked and the issue says
    # what failed.
    for name, pin in sorted(PINNED_SHA256.items()):
        try:
            found, differs = check_file(name, pin)
        except COULD_NOT_RUN as err:
            could_not_run = True
            found, differs = (
                [f"- **The check of `{name}` could not run: {_code(err)}.** This says "
                 "nothing about the file."],
                False,
            )
        lines += found
        drift = drift or differs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    if drift:
        return 1
    return 2 if could_not_run else 0


if __name__ == "__main__":
    sys.exit(main())
