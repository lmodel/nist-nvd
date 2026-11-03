"""The JSON Schema that gen-project writes accepts what the tests accept.

The other tests build their JSON Schema as linkml-validate does. gen-project builds
project/jsonschema/nist_nvd.schema.json from the settings in .linkml/generators.yaml
instead, so a setting there could make the generated file reject what the tests
accept. These tests build the file from those settings, and check the committed file
itself, each under the draft it declares and with its formats checked. NVD has four
kinds of response, so the file's top is the vulnerability response, and the other
three are validated through the file's `$defs`.
"""

import copy
import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_nvd" / "schema" / "nist_nvd.yaml"
CONFIG = ROOT / ".linkml" / "generators.yaml"
GENERATED = ROOT / "project" / "jsonschema" / "nist_nvd.schema.json"
EXTRACT = sorted((ROOT / "tests" / "data" / "nvd").glob("*.json"))
KINDS = {
    "NVD_CVE": "NvdCveResponse",
    "NVD_CPE": "NvdCpeResponse",
    "NVD_CPEMatchString": "NvdCpeMatchResponse",
    "NVD_CVEHistory": "NvdHistoryResponse",
}


@cache
def from_settings():
    """The JSON Schema as gen-project writes it, from its own settings."""
    settings = yaml.safe_load(CONFIG.read_text())["generator_args"]["jsonschema"]
    return json.dumps(json.loads(JsonSchemaGenerator(str(SCHEMA), **settings).serialize()))


def schemas():
    return [
        ("the generator's settings", json.loads(from_settings())),
        (str(GENERATED.relative_to(ROOT)), json.loads(GENERATED.read_text())),
    ]


def errors(schema, data, kind):
    """Validate against the class of a kind, under the draft the file declares."""
    if kind != "NvdCveResponse":
        schema = {
            "$schema": schema["$schema"],
            "$ref": f"#/$defs/{kind}",
            "$defs": schema["$defs"],
        }
    cls = jsonschema.validators.validator_for(schema)
    return [
        e.message[:200]
        for e in cls(schema, format_checker=cls.FORMAT_CHECKER).iter_errors(data)
    ]


def test_there_are_responses_to_read():
    assert EXTRACT
    assert {json.loads(p.read_text())["format"] for p in EXTRACT} == set(KINDS)


def test_the_committed_file_declares_a_draft_and_the_top_class():
    for label, schema in schemas():
        assert "$schema" in schema, label
        assert schema["title"] == "nist_nvd", label
        assert set(schema["required"]) >= {"vulnerabilities", "format", "timestamp"}, label


@pytest.mark.parametrize("path", EXTRACT, ids=lambda p: p.stem)
def test_real_responses_validate_against_the_generated_schema(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for label, schema in schemas():
        assert not errors(schema, data, KINDS[data["format"]]), label


def test_a_broken_response_fails_against_the_generated_schema():
    """A record of a response that breaks its class fails the whole response, so the
    test above is not passing for want of a check."""
    path = next(p for p in EXTRACT if p.name.startswith("cve-"))
    broken = copy.deepcopy(json.loads(path.read_text(encoding="utf-8")))
    broken["vulnerabilities"][0]["cve"]["vulnStatus"] = "AWAITING_ENRICHMENT"
    for label, schema in schemas():
        assert errors(schema, broken, "NvdCveResponse"), label


def test_an_optional_key_may_not_be_null():
    """NVD's schemas say a key is absent or holds a value. The settings keep that,
    where the generator's default would add null."""
    path = next(p for p in EXTRACT if p.name.startswith("cve-"))
    data = copy.deepcopy(json.loads(path.read_text(encoding="utf-8")))
    data["vulnerabilities"][0]["cve"]["vulnStatus"] = None
    for label, schema in schemas():
        assert errors(schema, data, "NvdCveResponse"), label
