"""Validates NVD's whole modified feed, one record at a time.

The feed moves about every two hours and is too large for git. `just
fetch-nvd-feed` downloads it into tmp/nvd-feed/ and checks it against its own .meta
file, and `just test-nvd-feed` runs these tests with NVD_FEED=1, as the nvd-feed job
of main.yaml does. Without that variable they skip, so `just test` stays quick; with
it, a missing feed fails them.

Because the feed is live, these tests fail when NVD starts writing a new status, tag
or key, which is what they are for. So a red job may be NVD's change and not the
pull request's. On 2026-11-03 all 15,762 records validated unchanged.
"""

import json
import os
from collections import Counter
from functools import cache
from pathlib import Path

import jsonschema
import pytest
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

from tests import nvd_rules
from tests.test_data import errors, pointer

ROOT = Path(__file__).parent.parent
FEED = (
    Path(os.environ.get("NVD_FEED_DIR", ROOT / "tmp" / "nvd-feed"))
    / "nvdcve-2.0-modified.json"
)
UPSTREAM = ROOT / "upstream"
BASE = "https://csrc.nist.gov/schema/nvd/api/2.0/"

pytestmark = pytest.mark.skipif(
    os.environ.get("NVD_FEED") != "1",
    reason="the whole feed is tested by `just test-nvd-feed`",
)

# Where the real data breaks NVD's own JSON schemas, as (validator, path with * for
# each index): why, and the count in the modified feed of 2026-11-03. The schema
# here admits each, and tests/test_upstream.py lists the first two as departures. A
# kind not listed fails the test below; the counts move with the feed.
KNOWN_BREACHES_OF_NVDS_SCHEMA = {
    ("format", "published"): ("no UTC offset", 15762),
    ("format", "lastModified"): ("no UTC offset", 15762),
    ("format", "vendorComments/*/lastModified"): ("no UTC offset", 1),
    ("format", "affected/*/affectedData/*/repo"): (
        "git://git@gitlab.com:gitlab-org/gitlab.git is no RFC 3986 address",
        2,
    ),
    # NVD's CVSS 4.0 file says multipleOf 0.1. A jsonschema validator computes that
    # in binary floating point, where 7.1 is no multiple of 0.1, so its score bands
    # fail for 2,110 scores that are right. tests/nvd_rules.py checks the step in
    # decimal, and finds nothing.
    ("anyOf", "metrics/cvssMetricV40/*/cvssData"): ("float arithmetic, not data", 2110),
}


@cache
def feed():
    if not FEED.is_file():
        pytest.fail(f"{FEED} is missing; run `just fetch-nvd-feed`")
    return json.loads(FEED.read_text(encoding="utf-8"))


def records():
    return [item["cve"] for item in feed()["vulnerabilities"]]


def _nvds_own_validator():
    """A validator of NVD's own cve_item, with formats checked, over the copies
    under upstream/. The SSVC schema's structure is enough to validate with, and
    the decision tree's outside schema stands empty."""
    registry = Registry()
    held = {
        "ssvc-v2.0.3.json": "ssvc-v2.0.3.structure.json",
        "cve_affected_1.0.json": "cve_affected_1.0.json",
        "external/cvss-v2.0.json": "external/cvss-v2.0.json",
        "external/cvss-v3.0.json": "external/cvss-v3.0.json",
        "external/cvss-v3.1.json": "external/cvss-v3.1.json",
        "external/cvss-v4.0.json": "external/cvss-v4.0.json",
    }
    for address, name in held.items():
        document = json.loads((UPSTREAM / name).read_text(encoding="utf-8"))
        registry = registry.with_resource(
            BASE + address,
            Resource.from_contents(document, default_specification=DRAFT7),
        )
    registry = registry.with_resource(
        "https://democert.org/ssvc/SSVC_Provision_v2.03.schema.json",
        Resource.from_contents({}, default_specification=DRAFT7),
    )
    main = json.loads(
        (UPSTREAM / "cve_api_json_2.0.schema").read_text(encoding="utf-8")
    )
    schema = {
        "$schema": main["$schema"],
        "$ref": "#/definitions/cve_item",
        "definitions": main["definitions"],
    }
    cls = jsonschema.validators.validator_for(schema)
    return cls(schema, registry=registry, format_checker=cls.FORMAT_CHECKER)


def test_the_response_validates():
    """The response around the records, with its records left out for memory's
    sake, passes as the top class."""
    data = {**feed(), "vulnerabilities": feed()["vulnerabilities"][:1]}
    assert not errors(data, "NvdCveResponse")
    assert data["format"] == "NVD_CVE"
    assert data["totalResults"] == len(records())


def test_every_record_validates():
    """Every record passes unchanged; the first 20 failures are shown."""
    failures = []
    for record in records():
        for error in errors(record, "NvdCve"):
            failures.append(f"{record['id']} {pointer(error)}: {error.message[:160]}")
    assert not failures, failures[:20]


def test_every_record_keeps_the_rules_beyond_the_validator():
    found = [
        (record["id"], problem)
        for record in records()
        for problem in nvd_rules.cve_problems(record)
    ]
    assert not found, found[:20]


def test_each_status_of_the_list_is_in_use():
    """The enum comes from the data, so a value the feed no longer holds is worth a
    look. Rarely used statuses can drop out of a two-hour window of changes, so only
    the common three must be there."""
    statuses = Counter(record.get("vulnStatus") for record in records())
    assert {"Analyzed", "Awaiting Analysis", "Modified"} <= set(statuses), statuses


def test_the_breaches_of_nvds_own_schema_are_the_known_kinds():
    """The real data breaks NVD's own schemas in the known ways and no other, so a
    new way that the schema here happens to admit is noticed."""
    validator = _nvds_own_validator()
    found = Counter()
    for record in records():
        for error in validator.iter_errors(record):
            path = "/".join(
                "*" if isinstance(part, int) else str(part)
                for part in error.absolute_path
            )
            found[(error.validator, path)] += 1
    unknown = set(found) - set(KNOWN_BREACHES_OF_NVDS_SCHEMA)
    assert not unknown, sorted(unknown)[:20]
