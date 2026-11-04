"""Data tests: the examples and the committed extract against the schema.

Each valid example and each response of the extract under tests/data/nvd/ is
validated against the JSON Schema the validator generates from the schema, with
formats checked as linkml-validate checks them. Each counter-example must fail
at the place its first line names, and nowhere else. tests/nvd_rules.py checks
over the same data what the generated JSON Schema cannot state.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml.validator.loaders import JsonLoader
from linkml_runtime import SchemaView
from linkml_runtime.loaders import yaml_loader

import nist_nvd.datamodel.nist_nvd as dataclasses_module
import nist_nvd.datamodel.nist_nvd_pydantic as pydantic_module
from tests import nvd_rules

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_nvd" / "schema" / "nist_nvd.yaml"
DATA = Path(__file__).parent / "data"
VALID = sorted((DATA / "valid").glob("*.yaml")) + sorted(
    (DATA / "problem" / "valid").glob("*.yaml")
)
INVALID = sorted((DATA / "invalid").glob("*.yaml"))
EXTRACT = sorted((DATA / "nvd").glob("*.json"))
KINDS = {
    "NVD_CVE": "NvdCveResponse",
    "NVD_CPE": "NvdCpeResponse",
    "NVD_CPEMatchString": "NvdCpeMatchResponse",
    "NVD_CVEHistory": "NvdHistoryResponse",
}

# What each case of the extract is there to show, by the CVE identifier in its
# file name. tests/data/nvd/README.md says how they were chosen.
EXTRACT_CASES = {
    "vulnStatus=Rejected": "CVE-2025-0998",
    "vulnStatus=Deferred": "CVE-2026-118170",
    "vulnStatus=Awaiting Analysis": "CVE-2026-117350",
    "vulnStatus=Analyzed": "CVE-2026-113948",
    "vulnStatus=Modified": "CVE-1999-0106",
    "vulnStatus=Received": "CVE-2026-38601",
    "vulnStatus=Undergoing Analysis": "CVE-2026-112513",
    "metrics=cvssMetricV2": "CVE-1999-0106",
    "metrics=cvssMetricV30": "CVE-2026-77172",
    "metrics=cvssMetricV31": "CVE-2026-118435",
    "metrics=cvssMetricV40": "CVE-2026-101034",
    "metrics=ssvcV203": "CVE-2026-58857",
    "key=cisaExploitAdd": "CVE-2023-29357",
    "key=vendorComments": "CVE-1999-0523",
    "key=evaluatorComment": "CVE-1999-0453",
    "key=evaluatorSolution": "CVE-1999-0646",
    "key=evaluatorImpact": "CVE-1999-0658",
}


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def class_of_file(path):
    return path.stem.split("-")[0]


@cache
def definitions():
    """The class definitions of the JSON Schema that linkml-validate generates.
    Generating it once keeps the run short; test_validator_agrees checks that
    linkml-validate gives the same answers."""
    generator = JsonSchemaGenerator(
        str(SCHEMA),
        mergeimports=True,
        top_class="NvdCveResponse",
        include_range_class_descendants=True,
    )
    return json.loads(generator.serialize())["$defs"]


@cache
def _validator(class_name):
    schema = {
        "$schema": "https://json-schema.org/draft/2019-09/schema",
        "$ref": f"#/$defs/{class_name}",
        "$defs": definitions(),
    }
    cls = jsonschema.validators.validator_for(schema)
    return cls(schema, format_checker=cls.FORMAT_CHECKER)


def errors(instance, class_name):
    return list(_validator(class_name).iter_errors(instance))


def pointer(error):
    """Where an error is, as a JSON pointer. A missing or an undeclared key is
    named after the object that lacks or holds it, so a counter-example that
    drops one required key cannot pass by dropping another."""
    parts = [str(part) for part in error.absolute_path]
    if error.validator == "required":
        parts.append(error.message.split("'")[1])
    elif error.validator == "additionalProperties":
        declared = error.schema.get("properties") or {}
        parts += sorted(key for key in error.instance if key not in declared)
    return "/" + "/".join(parts)


def response_problems(data):
    """The rules beyond the validator over one whole response."""
    for item in data.get("vulnerabilities") or []:
        yield from nvd_rules.cve_problems(item["cve"], item["cve"]["id"])


def test_each_folder_holds_data():
    """A test parametrized over an empty folder passes without checking
    anything, so each folder the tests read must hold files, and each file must
    name a class of the schema."""
    assert VALID and INVALID and EXTRACT
    classes = set(definitions())
    named = {class_of_file(path) for path in VALID + INVALID}
    assert named <= classes, sorted(named - classes)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_validate(path):
    found = errors(load(path), class_of_file(path))
    assert not found, [f"{pointer(e)}: {e.message}" for e in found]


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.stem)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails at the place its first line names, as
    `# Fails at: <JSON pointer>`, and nowhere else, so a file that starts failing
    for another reason fails this test."""
    first = path.read_text(encoding="utf-8").splitlines()[0]
    assert first.startswith("# Fails at: "), f"{path.name}: the first line names where"
    where = first.removeprefix("# Fails at: ").strip()
    found = errors(load(path), class_of_file(path))
    assert {pointer(e) for e in found} == {where}, [
        f"{pointer(e)}: {e.message}" for e in found
    ]


def test_every_class_has_an_example():
    """Every class an NVD response holds has a valid example, apart from the mixin
    and the decision tree, which stands for any value."""
    view = SchemaView(str(SCHEMA))
    open_classes = {"NvdSsvcDecisionTree", "NvdResponseMixin"}
    wanted = {
        name
        for name, cls in view.all_classes().items()
        if name.startswith("Nvd") and name not in open_classes
    }
    assert wanted <= {class_of_file(path) for path in VALID}


def test_validator_agrees():
    """linkml-validate, which docs/index.md tells a user to run, accepts a valid
    example and rejects a counter-example at the same place, for each response."""
    for kind in (
        "NvdCveResponse",
        "NvdCpeResponse",
        "NvdCpeMatchResponse",
        "NvdHistoryResponse",
    ):
        good = next(p for p in VALID if class_of_file(p) == kind)
        assert not validate(load(good), str(SCHEMA), kind).results, good.name
    bad = DATA / "invalid" / "NvdCve-unknown-status.yaml"
    report = validate(load(bad), str(SCHEMA), "NvdCve")
    assert any(r.message.endswith(" in /vulnStatus") for r in report.results), [
        r.message for r in report.results
    ]


def test_the_validator_checks_a_real_timestamp_as_nvd_writes_it():
    """linkml-validate checks formats. A real timestamp has no UTC offset, so a
    `datetime` range would refuse every record, and this one must not."""
    assert not validate(
        load(DATA / "valid" / "NvdCve-smallest.yaml"), str(SCHEMA), "NvdCve"
    ).results


def test_linkml_validates_a_rejected_record_but_its_json_loader_drops_the_list():
    """A rejected record's `references` is an empty list, which NIST's schema and this
    one accept. linkml-validate reads a .json file through a loader that drops every
    empty list, and then reports the required key as missing. docs/index.md says so.
    This fails once a LinkML release changes it, and that sentence goes then."""
    path = DATA / "nvd" / "cve-CVE-2025-0998.json"
    raw = json.loads(path.read_text(encoding="utf-8"))
    assert raw["vulnerabilities"][0]["cve"]["references"] == []
    assert not validate(raw, str(SCHEMA), "NvdCveResponse").results
    loaded = next(iter(JsonLoader(str(path)).iter_instances()))
    assert "references" not in loaded["vulnerabilities"][0]["cve"]
    report = validate(loaded, str(SCHEMA), "NvdCveResponse")
    assert [r.message for r in report.results] == [
        "'references' is a required property in /vulnerabilities/0/cve"
    ]


@pytest.mark.parametrize("path", EXTRACT, ids=lambda p: p.stem)
def test_extract_validates(path):
    """Every response of the extract, unchanged, passes as its own kind."""
    data = json.loads(path.read_text(encoding="utf-8"))
    found = errors(data, KINDS[data["format"]])
    assert not found, [f"{pointer(e)}: {e.message}" for e in found]
    assert not list(response_problems(data))


def test_the_extract_covers_every_kind_and_case():
    kinds = set()
    by_id = {}
    for path in EXTRACT:
        data = json.loads(path.read_text(encoding="utf-8"))
        kinds.add(data["format"])
        for item in data.get("vulnerabilities") or []:
            by_id[item["cve"]["id"]] = item["cve"]
    assert kinds == set(KINDS)
    for case, cve_id in EXTRACT_CASES.items():
        key, _, value = case.partition("=")
        cve = by_id[cve_id]
        if key == "vulnStatus":
            assert cve["vulnStatus"] == value, case
        elif key == "metrics":
            assert value in cve["metrics"], case
        else:
            assert value in cve, case
    configurations = [
        c for cve in by_id.values() for c in cve.get("configurations", [])
    ]
    assert any(
        c.get("operator") == "AND" and len(c["nodes"]) > 1 for c in configurations
    )


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.stem)
def test_valid_examples_keep_the_rules_beyond_the_validator(path):
    data = load(path)
    kind = class_of_file(path)
    found = []
    if kind == "NvdCve":
        found = list(nvd_rules.cve_problems(data))
    elif kind == "NvdAffectedProduct":
        found = list(nvd_rules.product_problems(data))
    elif kind == "NvdSsvcData":
        found = list(nvd_rules.ssvc_problems(data))
    elif kind.endswith("Response"):
        found = list(response_problems(data))
    assert not found


def test_each_rule_finds_its_breach():
    """Each rule beyond the validator reports a breach of it."""
    product = {
        "cpes": ["a", "a"],
        "versions": [{"changes": [{"at": "1"}, {"at": "1"}]}],
    }
    assert [p[1] for p in nvd_rules.product_problems(product)] == [
        "/cpes",
        "/versions/0/changes",
    ]
    twice = {"programRoutines": [{"name": "f"}, {"name": "f"}]}
    assert [p[1] for p in nvd_rules.product_problems(twice)] == ["/programRoutines"]
    assert list(nvd_rules.ssvc_problems({"options": [{"a": "b"}, {"a": "b"}]}))
    assert [p[1] for p in nvd_rules.cvss_v40_problems({"baseScore": 7.15})] == [
        "/baseScore"
    ]
    assert not list(nvd_rules.cvss_v40_problems({"baseScore": 7.1}))
    cve = {
        "affected": [{"affectedData": [{"modules": ["m", "m"]}]}],
        "metrics": {
            "ssvcV203": [{"ssvcData": {"options": [{"a": "b"}, {"a": "b"}]}}],
            "cvssMetricV40": [{"cvssData": {"baseScore": 7.15}}],
        },
    }
    assert {p[0] for p in nvd_rules.cve_problems(cve)} == {"unique-items", "score-step"}


def test_the_generated_models_load_real_responses():
    """Both generated models build from a real response of each kind, keys
    unchanged. A required list may be empty in NVD's data, as the references of a
    rejected record are, and the dataclasses refuse that, so they load only the
    others; tests/data/README.md says the same of the examples."""
    loaded = 0
    for path in EXTRACT:
        data = json.loads(path.read_text(encoding="utf-8"))
        name = KINDS[data["format"]]
        getattr(pydantic_module, name)(**data)
        records = [item["cve"] for item in data.get("vulnerabilities") or []]
        if any(not record["references"] for record in records):
            continue
        yaml_loader.loads(
            yaml.safe_dump(data), target_class=getattr(dataclasses_module, name)
        )
        loaded += 1
    assert loaded
