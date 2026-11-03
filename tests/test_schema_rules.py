"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
import re
from pathlib import Path

import yaml
from linkml_runtime import SchemaView

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned by
# the sidecar, and the adapt copies other lmodel repositories release. Each released
# neighbour is the schema asset of the newest release that carries one, downloaded
# and checked against the release's .sha256 and its build-provenance attestation on
# 2026-11-03, and pinned here by that checksum.
SCHEMA_DIR = ROOT / "src" / "nist_nvd" / "schema"
COPY = ROOT / ".lokf" / "nist-nvd.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = {
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/cve and lmodel/kev-catalog have no release yet, so these are the adapt
    # copies on their feat/first-release branches, at the commits their NOTICE
    # entries here name. Replace them with the release assets of cve v0.1.0 and
    # kev-catalog v0.1.0, and move these two checksums.
    "cve.yaml": "464e2c4b21e6a6eb6ed12010f06261b8096c2f657166a6824dcd231ac3f86145",
    "kev-catalog.yaml": "98385b9764afa2168d1462b22a49ab2631c68ce6c055e3f87e4036727c16059b",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# The classes `just lokf-adapt` re-roots on Concept, which the README lists for the
# plugins' Known LOKF types setting.
ROOTS = {"NvdCve"}

# What the copy renames because LOKF defines the name, keeping the IRI the source
# gives it, and the identifier it drops for LOKF's `id`. The prefix is cve for the
# reason project.justfile gives.
RENAMED = {
    "timestamp": "cve_timestamp",
    "created": "cve_created",
    "source": "cve_source",
    "type": "cve_type",
    "status": "cve_status",
    "version": "cve_version",
    "references": "cve_references",
    "description": "cve_description",
    "tags": "cve_tags",
    "url": "cve_url",
    "name": "cve_name",
    "at": "cve_at",
    "title": "cve_title",
}
DROPPED = {"id"}

# A key the copy shares with LOKF under another IRI, because it is an attribute of a
# class under no root, which adapt leaves as it is. SSVC's `id` names the vulnerability
# a decision is about, on an object inside a record. In a concept, LOKF's flat context
# would project it as that object's @id.
ATTRIBUTES_SHARED_WITH_LOKF = {"id"}

# The CVSS module is lmodel/cve's, so its classes, enums and keys are shared with
# lmodel/cve's copy on purpose, under the same IRIs. A host takes one of the two
# copies' CVSS classes: both hold them, so a host importing both gets the same
# definition twice. gen-python and gen-jsonld-context stop on that (linkml 1.12.1),
# as the same import of stix and attack would.
CVSS_CLASSES = {"CvssSeverityBandsMixin", "CvssV20", "CvssV30", "CvssV31", "CvssV40"}

# Keys the copy shares with a neighbour, each under another IRI there. LinkML keeps
# one namespace, and the JSON-LD context gives each key one IRI across a composite,
# so in a host that imports both copies one of them projects under the other's IRI.
# These are NVD's and FIRST's own keys, which must stay as they are for a real
# response to validate; lokf issue #169 asks `lokf adapt` for a --beside option that
# would rename them in the copy. A new overlap fails this test. The cve copy's list
# is long because NVD republishes CVE's records under its own IRIs, and because
# `--prefix cve` gives NVD's renamed keys the names cve's copy gives its own.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS} | {
    "cve.yaml": {
        "affected",
        "baseSeverity",
        "changes",
        "collectionURL",
        "configurations",
        "cpeMatch",
        "cpes",
        "criteria",
        "cveId",
        "cve_at",
        "cve_description",
        "cve_name",
        "cve_references",
        "cve_source",
        "cve_status",
        "cve_tags",
        "cve_title",
        "cve_type",
        "cve_url",
        "cve_version",
        "defaultStatus",
        "descriptions",
        "format",
        "lang",
        "lessThan",
        "lessThanOrEqual",
        "matchCriteriaId",
        "metrics",
        "modules",
        "negate",
        "nodes",
        "operator",
        "packageName",
        "packageURL",
        "platforms",
        "product",
        "programFiles",
        "programRoutines",
        "repo",
        "value",
        "vendor",
        "versionEndExcluding",
        "versionEndIncluding",
        "versionStartExcluding",
        "versionStartIncluding",
        "versionType",
        "versions",
        "vulnerable",
    },
    "in-toto.yaml": {"value"},
    "kev-catalog.yaml": {"product", "vulnerabilities"},
    "oscal.yaml": {"published", "value"},
    "slsa.yaml": {"value"},
    "spdx.yaml": {"comment", "scope", "value", "vectorString"},
    "stix.yaml": {
        "comment",
        "cpe",
        "descriptions",
        "lang",
        "modules",
        "options",
        "product",
        "published",
        "value",
        "vendor",
    },
    "uco.yaml": {"action", "comment", "descriptions", "format", "options", "value"},
}

# One pair of keys differs only by case: CVSS 4.0's Automatable and SSVC's
# automatable. Both are real keys, so neither is renamed, and on a case-insensitive
# filesystem the two share one page of the generated docs. No other pair may.
CASE_PAIRS = {"automatable"}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _expander(doc):
    """A function that expands a CURIE by the prefixes a schema file binds."""
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    return expand


def _names(path):
    """Each kind of element a schema file declares, and every slot and attribute
    name with the IRIs it expands to."""
    doc = _load(path)
    expand = _expander(doc)
    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_pinned_files():
    """Each neighbour copy is byte for byte the file pinned above, and no copy sits
    there unpinned."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == set(NEIGHBOURS)
    for name, sha256 in NEIGHBOURS.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot name
    the two share carries LOKF's IRI, but for the attribute listed above."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    differing = {
        name
        for name in slots.keys() & their_slots.keys()
        if slots[name] - their_slots[name]
    }
    assert differing == ATTRIBUTES_SHARED_WITH_LOKF | {"id"}


def test_names_apart_from_neighbours():
    """A class, enum, type or subset name is the copy's alone, but for the CVSS
    module's in lmodel/cve's copy, and the only keys it shares under another IRI with
    a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            shared = elements[kind] & their_elements[kind]
            if name == "cve.yaml":
                shared = {n for n in shared if not n.startswith("Cvss")}
            assert not shared, (name, kind, sorted(shared))
        differing = {
            key
            for key in slots.keys() & their_slots.keys()
            if slots[key] != their_slots[key]
        }
        if name == "cve.yaml":
            differing -= _module_attributes()
        assert differing == SHARED_WITH_NEIGHBOURS[name], (name, sorted(differing))


def _module_attributes():
    """The attributes of the vendored CVSS module, by name."""
    module = _load(SCHEMA_DIR / "cve" / "cve_cvss.yaml")
    return {
        attr
        for cls in module["classes"].values()
        for attr in (cls.get("attributes") or {})
    }


def test_lokf_0_9_0_leaves_the_modules_attributes_in_this_namespace():
    """lokf 0.9.0 pins the IRI of a class, slot and enum of a module whose default
    prefix differs, and not of an attribute, so the copy gives the CVSS module's
    attributes this schema's namespace, where the source gives them cve:. lokf's main
    branch pins them too. This fails when a newer lokf does, and then this test and
    the exclusion in test_names_apart_from_neighbours go."""
    copy = _load(COPY)
    assert copy["default_prefix"] == "nist_nvd"
    for cls in ("CvssV20", "CvssV40"):
        assert not [
            name
            for name, attr in copy["classes"][cls]["attributes"].items()
            if (attr or {}).get("slot_uri")
        ], cls
    assert copy["classes"]["CvssV31"]["class_uri"] == "cve:CvssV31"
    assert copy["slots"]["vectorString"]["slot_uri"] == "cve:vectorString"


def test_the_copy_holds_lmodel_cves_cvss_classes():
    """The module is vendored unchanged and `--prefix cve` keeps the key cve's own
    copy renames, so both copies give each CVSS class the same keys."""
    ours = _load(COPY)["classes"]
    theirs = _load(NEIGHBOUR_DIR / "cve.yaml")["classes"]
    for name in CVSS_CLASSES:
        assert set(ours[name].get("slots") or []) == set(theirs[name].get("slots") or []), name
        assert set(ours[name].get("attributes") or {}) == set(
            theirs[name].get("attributes") or {}
        ), name


def test_the_copy_renames_what_lokf_defines_and_keeps_the_iris():
    """Each name the copy takes from LOKF's way is renamed with its source IRI, the
    identifier gives way to LOKF's `id`, and nothing else is renamed."""
    source = {}
    expand = {}
    for path in SCHEMA_DIR.glob("*.yaml"):
        doc = _load(path)
        source.update(doc.get("slots") or {})
        for key in doc.get("slots") or {}:
            expand[key] = _expander(doc)
    for path in (SCHEMA_DIR / "cve").glob("*.yaml"):
        doc = _load(path)
        source.update(doc.get("slots") or {})
        for key in doc.get("slots") or {}:
            expand[key] = _expander(doc)
    copy = _load(COPY)
    expand_copy = _expander(copy)
    for old, new in RENAMED.items():
        assert new in copy["slots"] and old not in copy["slots"], old
        assert expand_copy(copy["slots"][new]["slot_uri"]) == expand[old](
            source[old]["slot_uri"]
        ), old
    assert set(copy["slots"]) == (set(source) - set(RENAMED) - DROPPED) | set(RENAMED.values())


def test_copy_roots_the_concept_class():
    """The copy re-roots the one class on Concept, and imports nothing but the LinkML
    types and LOKF."""
    doc = _load(COPY)
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_the_readme_names_the_known_lokf_types():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    block = readme.split("```text\n", 1)[1].split("```", 1)[0]
    assert {name.strip() for name in block.split(",")} == ROOTS


def test_the_readme_and_notice_carry_nvds_notice():
    """NVD's terms ask a product that uses its data to say so, and to say that NVD
    does not endorse it."""
    wanted = "This product uses data from the NVD API but is not endorsed or certified by the NVD."
    assert wanted in (ROOT / "README.md").read_text(encoding="utf-8")
    assert wanted in " ".join((ROOT / "NOTICE").read_text(encoding="utf-8").split())


def test_the_copy_keeps_the_enum_values():
    """YAML reads some plain words as other types, so this holds the copy's values to
    NVD's spelling after adapt has rewritten the file."""
    enums = _load(COPY)["enums"]
    assert set(enums["NvdVulnStatus"]["permissible_values"]) == {
        "Analyzed",
        "Deferred",
        "Awaiting Analysis",
        "Modified",
        "Received",
        "Undergoing Analysis",
        "Rejected",
    }
    assert set(enums["NvdOperator"]["permissible_values"]) == {"AND", "OR"}


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full address
    that no prefix covers makes every `lokf convert --schema` over the copy warn that
    it has no namespace."""
    doc = _load(COPY)
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


def test_each_module_stands_alone_with_no_cycle():
    """A module's imports load, none imports the umbrella, and the core imports only
    the LinkML types, as the module is meant to be taken alone."""
    order = {
        "nvd_core": {"linkml:types"},
        "nvd_cve": {"linkml:types", "./nvd_core", "./cve/cve_cvss"},
        "nvd_cpe": {"linkml:types", "./nvd_core"},
        "nvd_cpematch": {"linkml:types", "./nvd_core"},
        "nvd_history": {"linkml:types", "./nvd_core", "./nvd_cve"},
    }
    for module, imports in order.items():
        doc = _load(SCHEMA_DIR / f"{module}.yaml")
        assert set(doc["imports"]) == imports, module
        assert doc["id"] == f"https://w3id.org/lmodel/nist-nvd/{module}"
        assert doc["name"] == module
        assert SchemaView(str(SCHEMA_DIR / f"{module}.yaml")).all_classes()


def test_no_two_names_differ_only_by_case():
    """gen-doc writes a page per element, and two names that differ only by case share
    one page on a case-insensitive filesystem. No slot is called `index` either, whose
    page would overwrite the docs' index, and none is a Python keyword."""
    import keyword

    view = SchemaView(str(SCHEMA_DIR / "nist_nvd.yaml"))
    names = (
        list(view.all_classes(imports=True))
        + list(view.all_slots(imports=True))
        + list(view.all_enums(imports=True))
        + list(view.all_types(imports=True))
    )
    folded = {}
    for name in set(names):
        folded.setdefault(str(name).lower(), set()).add(str(name))
    pairs = {key for key, spelled in folded.items() if len(spelled) > 1}
    assert pairs == CASE_PAIRS
    assert "index" not in folded
    assert not [name for name in names if keyword.iskeyword(str(name))]
    assert not [n for n in names if re.search(r"[^A-Za-z0-9_]", str(n))]
