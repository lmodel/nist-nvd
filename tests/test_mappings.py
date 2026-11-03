"""Every mapping names a term that exists, by a CURIE whose prefix the schema binds.

The schema is the one home for this project's mappings. A target outside lmodel is
in tests/vocabulary-terms.txt, which lists what was read at each source. A target in
lmodel is in the neighbour's copy under tests/neighbours/, so NVD's crosswalk to CVE
and KEV fails when either renames a key. A mapping names no element here.
"""

import re
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.utils.formatutils import underscore

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "nist_nvd" / "schema"
SCHEMA = SCHEMA_DIR / "nist_nvd.yaml"
TERMS = Path(__file__).parent / "vocabulary-terms.txt"
NEIGHBOURS = Path(__file__).parent / "neighbours"
MAPPING_KINDS = (
    "exact_mappings",
    "close_mappings",
    "broad_mappings",
    "narrow_mappings",
    "related_mappings",
)

# Each lmodel prefix, and the neighbour copy that holds its terms.
LMODEL = {"cve": "cve.yaml", "kev_catalog": "kev-catalog.yaml", "stix": "stix.yaml"}

# The crosswalk: the mappings the data was checked for, so that none goes quietly.
# NVD's CISA fields equal the catalog's for all 1,766 entries of the catalog of
# 2026-11-03, read through the API with hasKev, and each of those entries' CVE
# identifiers is the id of one record, and the reverse.
CROSSWALK = {
    "id": ("exact_mappings", {"cve:cveId", "kev_catalog:cveID"}),
    "cisaExploitAdd": ("exact_mappings", {"kev_catalog:dateAdded"}),
    "cisaActionDue": ("exact_mappings", {"kev_catalog:dueDate"}),
    "cisaRequiredAction": ("exact_mappings", {"kev_catalog:requiredAction"}),
    "cisaVulnerabilityName": ("exact_mappings", {"kev_catalog:vulnerabilityName"}),
    "published": ("related_mappings", {"cve:datePublished"}),
    "lastModified": ("related_mappings", {"cve:dateUpdated"}),
    "descriptions": ("close_mappings", {"cve:descriptions"}),
    "references": ("close_mappings", {"cve:references"}),
    "weaknesses": ("close_mappings", {"cve:problemTypes"}),
    "configurations": ("close_mappings", {"cve:cpeApplicability"}),
    "affected": ("close_mappings", {"cve:affected"}),
}


def _files():
    """Each NVD module's plain YAML, so an attribute's mapping is read too."""
    return [p for p in sorted(SCHEMA_DIR.glob("*.yaml"))]


def mappings():
    """Each mapping of each element of NVD's modules, with the element it is on."""
    found = []

    def walk(node, name):
        if isinstance(node, dict):
            for kind in MAPPING_KINDS:
                for curie in node.get(kind) or []:
                    found.append((name, kind, str(curie)))
            for key, value in node.items():
                if key in ("slots", "classes", "attributes", "enums", "slot_usage", "types"):
                    if isinstance(value, dict):
                        for sub, definition in value.items():
                            walk(definition, sub)

    for path in _files():
        walk(yaml.safe_load(path.read_text(encoding="utf-8")), path.stem)
    return found


VIEW = SchemaView(str(SCHEMA))
MAPPINGS = mappings()
READ_TERMS = {
    line.strip()
    for line in TERMS.read_text(encoding="utf-8").splitlines()
    if line.strip() and not line.startswith("#")
}


def _bindings():
    """The prefixes the umbrella's closure binds, as each module states them."""
    bound = {}
    for path in _files():
        bound.update(yaml.safe_load(path.read_text(encoding="utf-8")).get("prefixes") or {})
    return bound


BOUND = _bindings()


def _names_in(path):
    """What a neighbour's copy calls its elements: classes, enums, slots and
    attributes, in their own names and in the IRI each slot pins, and whatever adapt
    dropped for LOKF's id, which the copy's notes name."""
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    names = set(doc.get("classes") or {}) | set(doc.get("enums") or {})
    for name, slot in (doc.get("slots") or {}).items():
        names.add(name)
        if slot and slot.get("slot_uri"):
            names.add(str(slot["slot_uri"]).rpartition(":")[2])
        names |= set((slot or {}).get("aliases") or [])
    for cls in (doc.get("classes") or {}).values():
        for name, attr in ((cls or {}).get("attributes") or {}).items():
            names.add(name)
            if attr and attr.get("slot_uri"):
                names.add(str(attr["slot_uri"]).rpartition(":")[2])
    for note in doc.get("notes") or []:
        match = re.search(r"dropped for LOKF's: ([^;.]+)", note)
        if match:
            names |= {n.strip() for n in match[1].split(",")}
    return names


def test_there_are_mappings():
    assert len(MAPPINGS) > 60


def test_the_umbrella_binds_the_family_prefixes():
    """The prefixes the contract between the three repositories names."""
    assert BOUND["cve"] == "https://w3id.org/lmodel/cve/"
    assert BOUND["nist_nvd"] == "https://w3id.org/lmodel/nist-nvd/"
    assert BOUND["kev_catalog"] == "https://w3id.org/lmodel/kev-catalog/"
    # LOKF binds spdx: to SPDX 2, so the schema must not bind it to SPDX 3.
    assert "spdx" not in BOUND
    assert BOUND["spdx3"] == "https://spdx.org/rdf/3.0.1/terms/"


@pytest.mark.parametrize("mapping", MAPPINGS, ids=lambda m: f"{m[0]}-{m[2]}")
def test_mapping_prefix_is_bound_in_its_module(mapping):
    element, kind, curie = mapping
    prefix = curie.partition(":")[0]
    assert prefix in BOUND, f"{element} {kind} {curie}: no module binds {prefix}"


@pytest.mark.parametrize(
    "path",
    [p for p in _files()],
    ids=lambda p: p.stem,
)
def test_each_module_binds_the_prefixes_it_uses(path):
    """A module lints and generates alone, so its own header binds what it maps to:
    gen-python drops the namespace of a prefix bound only in an import."""
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    used = set()

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in MAPPING_KINDS:
                    used.update(str(c).partition(":")[0] for c in value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(doc)
    assert used <= set(doc.get("prefixes") or {}), sorted(used - set(doc["prefixes"]))


@pytest.mark.parametrize("mapping", MAPPINGS, ids=lambda m: f"{m[0]}-{m[2]}")
def test_mapping_names_a_term_that_exists(mapping):
    element, kind, curie = mapping
    prefix, _, local = curie.partition(":")
    if prefix in LMODEL:
        path = NEIGHBOURS / LMODEL[prefix]
        names = _names_in(path)
        assert local in names or underscore(local) in names or f"{prefix}_{local}" in names, (
            f"{element} {kind} {curie} is not in {path.name}"
        )
    else:
        assert BOUND[prefix] + local in READ_TERMS, (
            f"{element} {kind} {curie} is not in tests/vocabulary-terms.txt"
        )


@pytest.mark.parametrize("element", sorted(CROSSWALK))
def test_the_crosswalk_keeps_its_kinds(element):
    kind, targets = CROSSWALK[element]
    found = {m[2] for m in MAPPINGS if m[0] == element and m[1] == kind}
    assert targets <= found, sorted(targets - found)


def test_nvds_timestamps_are_never_exact_to_cves():
    """NVD's published and lastModified are NVD's own times, so they are never called
    equal to the CVE record's."""
    for element in ("published", "lastModified"):
        kinds = {m[1] for m in MAPPINGS if m[0] == element and m[2].startswith("cve:")}
        assert kinds == {"related_mappings"}, element


def test_nvds_reference_tags_are_not_mapped_to_cves():
    """NVD's reference tags are its own vocabulary, not the CVE Program's. The slot
    and the enum map to nothing, and no value has a meaning, so nothing calls them
    equal."""
    assert not [m for m in MAPPINGS if m[0] in ("tags", "NvdReferenceTag")]
    enum = VIEW.get_enum("NvdReferenceTag")
    assert not any(pv.meaning for pv in enum.permissible_values.values())
    assert not enum.enum_uri


def test_no_old_mapping_file_comes_back():
    """The schema is the one home for mappings. The hand-kept SSSOM file rested on
    language-model matches that no source confirmed."""
    assert not list((ROOT / "src").rglob("*.sssom.tsv"))


def test_the_readme_names_each_target_prefix():
    """The README's Mappings section names what the schema crosses to, by each
    prefix the mappings use, and says the old file is gone."""
    section = (ROOT / "README.md").read_text(encoding="utf-8").split("## Mappings")[1]
    section = section.split("\n## ")[0]
    for prefix in {m[2].partition(":")[0] for m in MAPPINGS} - {"dcterms", "schema"}:
        assert f"{prefix}:" in section, prefix
    assert "Dublin Core" in section and "schema.org" in section
    assert "SSSOM" in section


def test_every_listed_term_is_used():
    """A term read at its source and no longer mapped leaves the list."""
    used = {BOUND[m[2].partition(":")[0]] + m[2].partition(":")[2] for m in MAPPINGS}
    assert READ_TERMS <= used, sorted(READ_TERMS - used)
