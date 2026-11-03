#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Fetch NVD's modified feed into tmp/ and check it against its own .meta file.

The feed changes about every two hours, so it cannot be pinned by a hash here.
NVD publishes a .meta file beside it that gives the size and the SHA-256 of the
uncompressed JSON, and the size of the gzip file. This script:

- reads the .meta file, which is a few short lines;
- keeps a copy already in the destination when its .meta matches;
- otherwise downloads the gzip file to a temporary name beside its place,
  stopping one byte past the size the .meta gives, unpacks it, stopping one byte
  past the size the .meta gives, and moves it into place only when the size and
  the SHA-256 match;
- deletes a download that does not match. The feed may have moved between the two
  requests, so a mismatch reads the .meta again and tries once more.

It refuses an address, or a redirect to one, that is not https on nvd.nist.gov. It
writes nothing outside the destination, which is tmp/nvd-feed/ unless --dest names
another folder. It exits 0 when the feed is in place, 1 when a download does not
match its .meta twice, and 2 when a check could not run, such as a refused or
cut-off request, which says nothing about NVD's data. Usage::

    python scripts/fetch_nvd_feed.py [--dest DIR]
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import http.client
import os
import re
import sys
import urllib.parse
import urllib.request
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "tmp" / "nvd-feed"
BASE = "https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-modified"
NAME = "nvdcve-2.0-modified.json"
HOST = "nvd.nist.gov"
USER_AGENT = "lmodel-nist-nvd-fetch"
CHUNK = 1 << 20

# The most the script reads of a .meta file, and of the feed, whatever a .meta says:
# about 25 times the size of the modified feed in 2026, which is 105 MB unpacked.
MAX_META_BYTES = 4096
MAX_FEED_BYTES = 2_500_000_000

# What a failed request can raise: OSError covers a refused or failed request and a
# timeout, HTTPException a read cut off, and ValueError a redirect off the host, a
# .meta of the wrong shape or an answer too large.
COULD_NOT_RUN = (OSError, http.client.HTTPException, ValueError, LookupError, TypeError)


def _check_address(url: str) -> None:
    """Refuse an address that is not https on NVD's host."""
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError(f"{url} is not an https address on {HOST}")


class _PinnedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on NVD's host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _check_address(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener without the default redirect handler, which follows a redirect to any
# address.
_open = urllib.request.build_opener(_PinnedHostRedirect).open


def _request(url: str):
    _check_address(url)
    return _open(
        urllib.request.Request(url, headers={"User-Agent": USER_AGENT}), timeout=120
    )


def parse_meta(text: str) -> dict:
    """The size, gzip size and SHA-256 that a .meta file gives."""
    fields = dict(line.split(":", 1) for line in text.splitlines() if ":" in line)
    size, gz_size = int(fields["size"]), int(fields["gzSize"])
    digest = fields["sha256"].strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ValueError("the .meta file's sha256 is not 64 hexadecimal digits")
    if not (0 < gz_size <= MAX_FEED_BYTES and 0 < size <= MAX_FEED_BYTES):
        raise ValueError("the .meta file gives a size this script will not read")
    return {"size": size, "gz_size": gz_size, "sha256": digest}


def read_meta() -> dict:
    with _request(f"{BASE}.meta") as resp:
        body = resp.read(MAX_META_BYTES + 1)
    if len(body) > MAX_META_BYTES:
        raise ValueError(f"the .meta file is larger than {MAX_META_BYTES} bytes")
    return parse_meta(body.decode("ascii"))


def _matches(path: Path, meta: dict) -> bool:
    if not path.is_file() or path.stat().st_size != meta["size"]:
        return False
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK):
            digest.update(chunk)
    return digest.hexdigest() == meta["sha256"]


def _download(part: Path, meta: dict) -> None:
    """Download the gzip file and unpack it into a file, stopping one byte past
    each size the .meta gives, so that an oversized answer fails the check
    without filling the disk."""
    # A file left at the temporary name, even a link, is replaced, not written through.
    part.unlink(missing_ok=True)
    packed = part.with_name(part.name + ".gz")
    packed.unlink(missing_ok=True)
    try:
        with _request(f"{BASE}.json.gz") as resp, packed.open("wb") as out:
            left = meta["gz_size"] + 1
            while left > 0 and (chunk := resp.read(min(CHUNK, left))):
                out.write(chunk)
                left -= len(chunk)
        with gzip.open(packed, "rb") as source, part.open("wb") as out:
            left = meta["size"] + 1
            while left > 0 and (chunk := source.read(min(CHUNK, left))):
                out.write(chunk)
                left -= len(chunk)
    finally:
        packed.unlink(missing_ok=True)


def fetch(dest: Path) -> tuple[int, str]:
    """Put the feed in place, and return an exit code and a line to print."""
    target = dest / NAME
    part = dest / f"{NAME}.part"
    try:
        dest.mkdir(parents=True, exist_ok=True)
        for _ in range(2):
            meta = read_meta()
            if _matches(target, meta):
                return 0, f"{NAME}: present and matching its .meta file"
            try:
                _download(part, meta)
            # A cut-off or corrupt gzip stream, which a moved feed can also cause.
            except (EOFError, gzip.BadGzipFile, zlib.error):
                part.unlink(missing_ok=True)
                continue
            if _matches(part, meta):
                os.replace(part, target)
                return (
                    0,
                    f"{NAME}: downloaded, {meta['size']} bytes matching its .meta file",
                )
            part.unlink(missing_ok=True)
    except COULD_NOT_RUN as err:
        part.unlink(missing_ok=True)
        return 2, f"the fetch could not run: {err}"
    return 1, f"{NAME}: the download does not match its .meta file, twice"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEST,
        help="The folder to fill (default: %(default)s)",
    )
    args = parser.parse_args(argv)
    code, line = fetch(args.dest)
    print(line, file=sys.stderr if code else sys.stdout)
    return code


if __name__ == "__main__":
    sys.exit(main())
