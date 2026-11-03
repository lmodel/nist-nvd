"""Checks the vendored copy of lmodel/cve's CVSS module against NVD's CVSS files.

src/nist_nvd/schema/cve/ holds lmodel/cve's `cve_cvss` module, copied unchanged,
which the vulnerability module imports for its score objects. NVD's copies of
FIRST's CVSS schemas have the same property names and required lists as the CVE
Program's, and differ in how they state score bands and in whether they close
the object. So these tests walk NVD's copies under upstream/external/ and fail on
a key or an enum value that NVD has and the module lacks.
"""

import hashlib
import json
from pathlib import Path

import pytest
from linkml_runtime import SchemaView

ROOT = Path(__file__).parent.parent
COPY = ROOT / "src" / "nist_nvd" / "schema" / "cve"
EXTERNAL = ROOT / "upstream" / "external"

# The commit of lmodel/cve that the copy equals, and the git object hash of the
# module there, under src/cve/schema/. lmodel/cve has no release yet, so this is
# the head of its feat/first-release branch when the file was last read. Move both
# with the copy, from lmodel/cve v0.1.0 once it is released.
CVE_COMMIT = "c66cd5d72932b77173526dc65bb7497814af6548"
PINNED_BLOBS = {"cve_cvss.yaml": "54829e1452fba5ddd6e7a9f30c5de7077b7e3c0f"}

CLASSES = {
    "cvss-v2.0.json": "CvssV20",
    "cvss-v3.0.json": "CvssV30",
    "cvss-v3.1.json": "CvssV31",
    "cvss-v4.0.json": "CvssV40",
}

# The keys of NVD's CVSS 4.0 file that it declares only under `allOf`, with its
# score bands, and the module declares as properties.
ALLOF_KEYS = {
    "baseScore",
    "baseSeverity",
    "threatScore",
    "threatSeverity",
    "environmentalScore",
    "environmentalSeverity",
}

# Where NVD's CVSS files and the module differ, each because the CVE Program's copy
# differs from NVD's, which is FIRST's. Neither is forked: the module stays as it is
# released, and these lists fail when the difference moves. The validator reads the
# module, so tests/test_nvd_feed.py fails on the first record that needs what it
# refuses. The counts are of the modified feed first read on 2026-11-03, 15,762
# records, and agree with the same feed read later that day and with 17,669 other
# records from the known-exploited list and eight pages across all NVD's years.
#
# NVD's CVSS 4.0 rules name these four keys and NVD leaves its object open, so a score
# could carry them. The CVE Program's copy names them too but closes its object. None
# of the 4,590 CVSS 4.0 metrics holds one.
KNOWN_MISSING_KEYS = {
    "threatScore",
    "threatSeverity",
    "environmentalScore",
    "environmentalSeverity",
}
# FIRST's value for no modified impact on connected systems is NEGLIGIBLE, as NVD's
# copy has it. The CVE Program's copy writes NONE. All 13,770 values of these three
# keys in those 4,590 metrics are NOT_DEFINED, so neither spelling occurs.
KNOWN_MISSING_VALUES = {
    "modifiedSubConfidentialityImpact": ["NEGLIGIBLE"],
    "modifiedSubIntegrityImpact": ["NEGLIGIBLE"],
    "modifiedSubAvailabilityImpact": ["NEGLIGIBLE"],
}
# NVD's CVSS 3.x files state no bands between a score and its severity, and the
# module's do, through CvssSeverityBandsMixin. So the module is stricter here than
# NVD's own schema. All 14,431 CVSS 3.x metrics keep the bands.
NO_BANDS_IN_NVDS_FILE = {"cvss-v3.0.json", "cvss-v3.1.json"}


def _blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _nvd(name):
    return json.loads((EXTERNAL / name).read_text(encoding="utf-8"))


def _enum_of(document, prop):
    """The enum values a property of NVD's file allows, or None."""
    target = prop
    if "$ref" in target:
        target = document["definitions"][target["$ref"].rsplit("/", 1)[1]]
    if "enum" in target:
        return set(target["enum"])
    if "const" in target:
        return {target["const"]}
    return None


VIEW = SchemaView(str(COPY / "cve_cvss.yaml"))


def test_the_module_is_the_pinned_file():
    assert {name: _blob_sha(COPY / name) for name in PINNED_BLOBS} == PINNED_BLOBS


def test_the_copy_holds_only_the_pinned_module():
    assert sorted(p.name for p in COPY.iterdir()) == sorted(PINNED_BLOBS)


def test_the_module_keeps_the_contract():
    """The classes and identity the shared contract names, importing only the
    LinkML types."""
    schema = VIEW.schema
    assert schema.id == "https://w3id.org/lmodel/cve/cve_cvss"
    assert list(schema.imports) == ["linkml:types"]
    assert set(CLASSES.values()) <= set(VIEW.all_classes())


@pytest.mark.parametrize("name", sorted(NO_BANDS_IN_NVDS_FILE), ids=str)
def test_the_module_states_bands_that_nvds_3_x_files_do_not(name):
    document = _nvd(name)
    assert "allOf" not in document and "anyOf" not in document
    assert "CvssSeverityBandsMixin" in VIEW.get_class(CLASSES[name]).mixins


def test_nvds_4_0_file_states_its_own_bands():
    assert "allOf" in _nvd("cvss-v4.0.json")


@pytest.mark.parametrize("name", sorted(CLASSES), ids=str)
def test_every_key_of_nvd_is_in_the_module(name):
    document = _nvd(name)
    keys = set(document["properties"])
    if name == "cvss-v4.0.json":
        keys |= ALLOF_KEYS
    held = {slot.name for slot in VIEW.class_induced_slots(CLASSES[name])}
    expected = KNOWN_MISSING_KEYS if name == "cvss-v4.0.json" else set()
    assert keys - held == expected, sorted(keys - held)


@pytest.mark.parametrize("name", sorted(CLASSES), ids=str)
def test_every_required_key_of_nvd_is_required_in_the_module(name):
    document = _nvd(name)
    for key in document["required"]:
        slot = VIEW.induced_slot(key, CLASSES[name])
        assert slot.required, key


@pytest.mark.parametrize("name", sorted(CLASSES), ids=str)
def test_every_enum_value_of_nvd_is_in_the_module(name):
    document = _nvd(name)
    missing = {}
    for key, prop in document["properties"].items():
        values = _enum_of(document, prop)
        if values is None:
            continue
        slot = VIEW.induced_slot(key, CLASSES[name])
        enum = VIEW.get_enum(slot.range) if slot.range else None
        if enum is not None:
            held = set(enum.permissible_values)
        elif slot.equals_string is not None:
            held = {slot.equals_string}
        else:
            held = set()
        if values - held:
            missing[key] = sorted(values - held)
    assert missing == (KNOWN_MISSING_VALUES if name == "cvss-v4.0.json" else {}), (
        missing
    )
