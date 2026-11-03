"""Holds the schema to NIST's JSON schemas, and its headers to the watch's pins.

The walk starts from each class's `upstream_definition` annotation, which names
the object of a file under upstream/ that the class renders. It fails when a
definition, a property, an enum value or a required member has no element here,
or has a different cardinality, a different pattern or another bound, and when a
class has a key the file does not name. Each place where the schema departs from
NIST's file is listed in DEPARTURES with its reason, and a listed departure that
no longer applies fails too.
"""

import hashlib
import importlib.util
import json
import re
from functools import cache
from pathlib import Path

import pytest
from linkml_runtime import SchemaView

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "nist_nvd" / "schema"
UPSTREAM = ROOT / "upstream"
BASE = "https://csrc.nist.gov/schema/nvd/api/2.0/"
SSVC = "ssvc-v2.0.3.json"

spec = importlib.util.spec_from_file_location(
    "watch_pins", ROOT / "scripts" / "check_upstream_release.py"
)
WATCH = importlib.util.module_from_spec(spec)
spec.loader.exec_module(WATCH)

VIEW = SchemaView(str(SCHEMA_DIR / "nist_nvd.yaml"))

# The edition of each file, as its title names it, and the module that renders
# it. A file with no edition in its title is rendered inside nvd_cve.
MODULES = {
    "nist_nvd.yaml": ("cve_api_json_2.0.schema", "2.2.4"),
    "nvd_cve.yaml": ("cve_api_json_2.0.schema", "2.2.4"),
    "nvd_cpe.yaml": ("cpe_api_json_2.0.schema", "2.0"),
    "nvd_cpematch.yaml": ("cpematch_api_json_2.0.schema", "2.0"),
    "nvd_history.yaml": ("cve_history_api_json_2.0.schema", "2.0.1"),
}

# The classes that render no object of NIST's files: the fields four responses
# share, the decision tree of an outside schema, and the object form of a change's
# value, of which NIST's file says nothing more.
UNANCHORED = {"NvdResponseMixin", "NvdSsvcDecisionTree", "NvdChangeObject"}

# The module of lmodel/cve renders these, and tests/test_cve_import.py walks them.
EXTERNAL = {
    f"{BASE}external/cvss-v2.0.json": "CvssV20",
    f"{BASE}external/cvss-v3.0.json": "CvssV30",
    f"{BASE}external/cvss-v3.1.json": "CvssV31",
    f"{BASE}external/cvss-v4.0.json": "CvssV40",
}

# Definitions that hold a plain value, so no class renders them; the properties
# that refer to them are walked through the reference.
SCALAR_DEFINITIONS = {
    "cve_api_json_2.0.schema": {"cve_id", "def_subscore"},
    "cve_affected_1.0.json": {"uriType", "cpe22and23", "version", "status"},
}

# A string in NIST's file that the schema closes with an enum, because the real
# data fixes the list. Each enum's comment says which data.
DATA_ENUMS = {
    ("cve_api_json_2.0.schema#/definitions/cve_item", "vulnStatus"): "NvdVulnStatus",
    ("cve_api_json_2.0.schema#/definitions/reference", "tags"): "NvdReferenceTag",
    ("cve_api_json_2.0.schema#/definitions/weakness", "type"): "NvdSourceType",
    ("cve_api_json_2.0.schema#/definitions/cvss-v2", "baseSeverity"): "NvdCvssV2Severity",
    ("cpematch_api_json_2.0.schema#/definitions/def_match_data", "status"): "NvdMatchStringStatus",
}

# A string in NIST's file that the schema pins to the one value the API's answers
# carry, on each response class.
DATA_PINNED = {
    ("cve_api_json_2.0.schema#", "format"): "NVD_CVE",
    ("cpe_api_json_2.0.schema#", "format"): "NVD_CPE",
    ("cpematch_api_json_2.0.schema#", "format"): "NVD_CPEMatchString",
    ("cve_history_api_json_2.0.schema#", "format"): "NVD_CVEHistory",
}

# Keys a class names beyond NIST's file, where that file leaves its keys open. Each
# is the only key the data holds there, and the class's comment says why it is named.
DATA_KEYS = {
    f"{SSVC}#/properties/options/items": {"exploitation", "automatable", "technicalImpact"},
}

# Where the schema departs from NIST's file, as (object, key, aspect): reason. The
# counts are of the modified feed of 2026-11-03, 15,762 records, which
# tests/test_nvd_feed.py reads anew each run.
_NO_OFFSET = (
    "NIST's format date-time is RFC 3339, which needs a UTC offset, and NVD writes "
    "none, so all 15,762 records break it in published and in lastModified. The "
    "nvd_timestamp type admits both forms."
)
DEPARTURES = {
    ("cve_api_json_2.0.schema#/definitions/cve_item", "published", "format"): _NO_OFFSET,
    ("cve_api_json_2.0.schema#/definitions/cve_item", "lastModified", "format"): _NO_OFFSET,
    ("cve_api_json_2.0.schema#/definitions/vendorComment", "lastModified", "format"): _NO_OFFSET,
    ("cve_api_json_2.0.schema#", "timestamp", "format"): _NO_OFFSET,
    ("cpe_api_json_2.0.schema#", "timestamp", "format"): _NO_OFFSET,
    ("cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe", "created", "format"): _NO_OFFSET,
    ("cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe", "lastModified", "format"): _NO_OFFSET,
    ("cpematch_api_json_2.0.schema#", "timestamp", "format"): _NO_OFFSET,
    ("cpematch_api_json_2.0.schema#/definitions/def_match_data", "created", "format"): _NO_OFFSET,
    ("cpematch_api_json_2.0.schema#/definitions/def_match_data", "lastModified", "format"): _NO_OFFSET,
    ("cpematch_api_json_2.0.schema#/definitions/def_match_data", "cpeLastModified", "format"): _NO_OFFSET,
    ("cve_history_api_json_2.0.schema#", "timestamp", "format"): _NO_OFFSET,
    ("cve_history_api_json_2.0.schema#/definitions/changeItem", "created", "format"): _NO_OFFSET,
    (f"{SSVC}#", "timestamp", "format"): _NO_OFFSET,
    ("cve_affected_1.0.json#", "repo", "format"): (
        "NIST's format uri is RFC 3986. Two records write "
        "git://git@gitlab.com:gitlab-org/gitlab.git, which it refuses, so this slot "
        "is a string with NIST's lengths."
    ),
    ("cve_affected_1.0.json#", "cpes", "length"): (
        "LinkML gives a slot one pattern, and NIST's CPE pattern takes it, so the "
        "lengths of 1 to 2048 go unstated."
    ),
    (f"{SSVC}#", "$schema", "key"): (
        "A slot of this name breaks the generated Python, and no record of the feed "
        "holds the key, so a decision that carries it fails validation."
    ),
    (f"{SSVC}#", "decisionTree", "ref"): (
        "NIST's file refers to a schema at democert.org, whose $id names another "
        "edition. It is not rendered: no record of the feed holds a decision tree, "
        "and this slot takes any value."
    ),
    (f"{SSVC}#/properties/options/items", ".*", "pattern-key"): (
        "The keys are open, so the class states them with extra_slots, which the "
        "JSON Schema checks and the Python models do not."
    ),
    ("cve_history_api_json_2.0.schema#/definitions/detail", "oldValue", "union"): (
        "NIST's union of string, array and object is an any_of here. NIST says nothing "
        "of an array's items, and the generators need a type for them, so the array "
        "form takes strings."
    ),
    ("cve_history_api_json_2.0.schema#/definitions/detail", "newValue", "union"): (
        "NIST's union of string, array and object is an any_of here. NIST says nothing "
        "of an array's items, and the generators need a type for them, so the array "
        "form takes strings."
    ),
}

# NIST's objects that do not forbid other keys. The classes are closed, so that a
# key NVD adds fails validation and the feed test reports it.
OPEN_UPSTREAM_OBJECTS = {
    "cve_api_json_2.0.schema#/definitions/cve_item",
    "cve_api_json_2.0.schema#/definitions/cve_item/properties/cveTags/items",
    "cve_api_json_2.0.schema#/definitions/cve_item/properties/metrics",
    "cve_api_json_2.0.schema#/definitions/reference",
    "cve_api_json_2.0.schema#/definitions/config",
    "cve_api_json_2.0.schema#/definitions/node",
    "cve_api_json_2.0.schema#/definitions/cpe_match",
    "cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe/properties/deprecatedBy/items",
    "cve_history_api_json_2.0.schema#",
    "cve_affected_1.0.json#",
    f"{SSVC}#/properties/options/items",
}

# The same object under another path of the same file: NIST repeats the shape of
# deprecatedBy under deprecates, and one class renders both.
SAME_AS = {
    "cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe/properties/deprecates/items": (
        "cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe/properties/deprecatedBy/items"
    )
}

_LENGTH = re.compile(r"^\^\[\\s\\S\]\{(\d+),(\d+)\}\$$")
USED_DEPARTURES = set()


@cache
def document(name):
    path = UPSTREAM / WATCH.STRUCTURE_ONLY.get(name, name)
    return json.loads(path.read_text(encoding="utf-8"))


def resolve(anchor):
    """The object an anchor of the form file#/json/pointer names."""
    name, _, path = anchor.partition("#")
    node = document(name)
    for part in filter(None, path.split("/")):
        node = node[part]
    return node


def anchors():
    """Each class that renders an object of NIST's files, by that object."""
    found = {}
    for name, cls in VIEW.all_classes().items():
        annotation = (cls.annotations or {}).get("upstream_definition")
        if annotation is not None:
            found[annotation.value] = name
    return found


ANCHORS = anchors()


def _deref(anchor, prop):
    """A property with its local or outside reference followed. Returns the plain
    schema and, for an object, where it lives: an anchor, or an outside address."""
    name = anchor.partition("#")[0]
    ref = prop.get("$ref")
    if ref is None:
        return prop, None
    if ref.startswith("#"):
        target = f"{name}{ref}"
        return resolve(target), target
    if ref in EXTERNAL:
        return {}, ref
    if ref.startswith(BASE):
        target = ref.removeprefix(BASE) + "#"
        return resolve(target), target
    return {}, ref


def _departs(anchor, key, aspect):
    entry = (anchor, key, aspect)
    if entry in DEPARTURES:
        USED_DEPARTURES.add(entry)
        return True
    return False


def _pattern_of(slot):
    """The slot's pattern, or its type's, with the quotes as NIST writes them."""
    pattern = slot.pattern
    if pattern is None and slot.range in VIEW.all_types():
        pattern = VIEW.get_type(slot.range).pattern
    if pattern is None:
        return None
    return pattern.replace("\\x27", "'").replace("\\x22", '"')


def _check_scalar(anchor, key, schema, slot, problems):
    """A plain value's type, format, pattern, lengths, bounds and enum."""
    where = f"{anchor} {key}"
    if "enum" in schema:
        values = set(schema["enum"])
        enum = VIEW.get_enum(slot.range)
        if enum is None or set(enum.permissible_values) != values:
            problems.append(f"{where}: the enum is not {sorted(values)}")
        return
    if (anchor, key) in DATA_ENUMS:
        if slot.range != DATA_ENUMS[(anchor, key)]:
            problems.append(f"{where}: range is {slot.range}")
        return
    if (anchor, key) in DATA_PINNED:
        if slot.equals_string != DATA_PINNED[(anchor, key)]:
            problems.append(f"{where}: pins {slot.equals_string}")
        return
    kinds = schema.get("type")
    if kinds == "boolean" and slot.range != "boolean":
        problems.append(f"{where}: range is {slot.range}, not boolean")
    if kinds == "integer" and slot.range != "integer":
        problems.append(f"{where}: range is {slot.range}, not integer")
    if kinds == "number" and slot.range != "float":
        problems.append(f"{where}: range is {slot.range}, not float")
    for bound, metaslot in (("minimum", "minimum_value"), ("maximum", "maximum_value")):
        if bound in schema and getattr(slot, metaslot) != schema[bound]:
            problems.append(f"{where}: {metaslot} is not {schema[bound]}")
    fmt = schema.get("format")
    expected = {"date-time": "nvd_timestamp", "date": "date", "uri": "uri", "uuid": "nvd_uuid"}
    pattern = _pattern_of(slot)
    if fmt == "date-time" and slot.range == "nvd_timestamp":
        if not _departs(anchor, key, "format"):
            problems.append(f"{where}: an unlisted departure from format date-time")
    elif fmt == "uri" and slot.range != "uri":
        if not _departs(anchor, key, "format"):
            problems.append(f"{where}: range is {slot.range}, not uri")
    elif fmt and slot.range != expected[fmt]:
        problems.append(f"{where}: range is {slot.range}, not {expected[fmt]}")
    elif kinds == "string" and not fmt and "$ref" not in schema:
        if slot.range not in ("string", "NvdCve", "nvd_cve_identifier"):
            problems.append(f"{where}: range is {slot.range}, not string")
    if "pattern" in schema and pattern != schema["pattern"]:
        problems.append(f"{where}: the pattern is not NIST's")
    if "minLength" in schema or "maxLength" in schema:
        match = _LENGTH.match(pattern or "")
        if "pattern" in schema:
            if not _departs(anchor, key, "length"):
                problems.append(f"{where}: an unlisted departure from the lengths")
        elif match is None:
            problems.append(f"{where}: no pattern states the lengths")
        else:
            low, high = int(match[1]), int(match[2])
            if low != schema.get("minLength", 0) or high != schema["maxLength"]:
                problems.append(f"{where}: lengths {low} to {high}")


def _check_property(anchor, key, prop, cname, problems):
    where = f"{anchor} {key}"
    if isinstance(prop.get("type"), list) and "object" in prop["type"]:
        if not _departs(anchor, key, "union"):
            problems.append(f"{where}: an unlisted union")
        return
    plain, target = _deref(anchor, prop)
    if target is not None and target not in ANCHORS and target not in EXTERNAL:
        if ref_is_outside := str(target).startswith("http"):
            if ref_is_outside and _departs(anchor, key, "ref"):
                return
            problems.append(f"{where}: an unlisted outside reference {target}")
            return
    slot = VIEW.induced_slot(key, cname)
    is_list = plain.get("type") == "array"
    if bool(slot.multivalued) != is_list:
        problems.append(f"{where}: multivalued is {slot.multivalued}, not {is_list}")
    minimum = plain.get("minItems", 0)
    if is_list and (slot.minimum_cardinality or 0) != minimum:
        problems.append(f"{where}: minimum_cardinality is not {minimum}")
    if is_list and bool(slot.list_elements_unique) != bool(plain.get("uniqueItems")):
        problems.append(f"{where}: list_elements_unique is not {plain.get('uniqueItems')}")
    items = plain.get("items", {}) if is_list else plain
    inner_anchor = anchor if target is None else target
    plain_item, item_target = _deref(inner_anchor, items) if is_list else (items, target)
    if is_list and "properties" in plain_item and item_target is None:
        item_target = f"{anchor}/properties/{key}/items"
    if not is_list and "properties" in plain_item and item_target is None:
        item_target = f"{anchor}/properties/{key}"
    item_target = SAME_AS.get(item_target, item_target)
    if item_target in EXTERNAL:
        if slot.range != EXTERNAL[item_target]:
            problems.append(f"{where}: range is {slot.range}, not {EXTERNAL[item_target]}")
    elif item_target in ANCHORS:
        if slot.range != ANCHORS[item_target]:
            problems.append(f"{where}: range is {slot.range}, not {ANCHORS[item_target]}")
    elif "properties" in plain_item:
        problems.append(f"{where}: no class renders {item_target}")
    else:
        _check_scalar(anchor, key, plain_item, slot, problems)


def walk():
    """Every problem of every anchored object, as a line each."""
    problems = []
    for anchor, cname in sorted(ANCHORS.items()):
        schema = resolve(anchor)
        declared = schema.get("properties", {})
        held = {slot.name for slot in VIEW.class_induced_slots(cname)}
        for key, prop in declared.items():
            if key not in held:
                if not _departs(anchor, key, "key") and not _departs(anchor, key, "ref"):
                    problems.append(f"{anchor} {key}: no slot on {cname}")
                continue
            _check_property(anchor, key, prop, cname, problems)
        for key in schema.get("patternProperties", {}):
            if not _departs(anchor, key, "pattern-key"):
                problems.append(f"{anchor} {key}: an unlisted pattern of keys")
        for key in held - set(declared) - DATA_KEYS.get(anchor, set()):
            problems.append(f"{anchor} {key}: {cname} has a key NIST's file does not name")
        required = set(schema.get("required", []))
        branches = [set(b.get("required", [])) for b in schema.get("oneOf", [])]
        # What every branch of a oneOf requires is required; the rest is a rule.
        required |= set.intersection(*branches) if branches else set()
        for key in declared:
            if key not in held:
                continue
            slot = VIEW.induced_slot(key, cname)
            is_required = bool(slot.required or slot.identifier)
            if is_required != (key in required):
                problems.append(f"{anchor} {key}: required is {is_required}")
        for key in required - set(declared):
            problems.append(f"{anchor} {key}: required but not declared")
    return problems


PROBLEMS = walk()


# tests/test_cve_import.py walks the four CVSS files.
_RENDERED_FILES = sorted(n for n in WATCH.PINNED_SHA256 if not n.startswith("external/"))


def _objects_in(name, node, path, found):
    """Every object in a file that has properties, by its anchor."""
    if isinstance(node, dict):
        if "properties" in node and isinstance(node["properties"], dict):
            found.add(f"{name}#{path}")
        for key, value in node.items():
            child = f"{path}/{key}"
            if key in ("properties", "definitions"):
                for sub, schema in value.items():
                    _objects_in(name, schema, f"{child}/{sub}", found)
            elif key == "items":
                _objects_in(name, value, child, found)
    return found


def test_the_walk_finds_nothing():
    assert not PROBLEMS, "\n".join(PROBLEMS)


def test_every_departure_listed_still_applies():
    assert set(DEPARTURES) == USED_DEPARTURES, sorted(set(DEPARTURES) ^ USED_DEPARTURES)


@pytest.mark.parametrize("name", _RENDERED_FILES)
def test_every_object_of_nists_files_has_a_class(name):
    """Every object with properties, anywhere in a file, is an anchor or the same
    shape as one, and every definition with no properties is a known plain value."""
    found = _objects_in(name, document(name), "", set())
    unclaimed = {a for a in found if a not in ANCHORS and a not in SAME_AS}
    assert not unclaimed, sorted(unclaimed)
    plain = {
        key
        for key, schema in document(name).get("definitions", {}).items()
        if "properties" not in schema
    }
    assert plain == SCALAR_DEFINITIONS.get(name, set())


def test_every_scalar_definition_is_used():
    """A plain value's definition is used by a property the walk reads, or NIST
    has added a definition that nothing renders."""
    for name, keys in SCALAR_DEFINITIONS.items():
        text = json.dumps(document(name))
        for key in keys:
            assert f"#/definitions/{key}" in text, key


def test_every_nvd_class_is_anchored_or_known():
    for name, cls in VIEW.all_classes().items():
        if name.startswith("Nvd"):
            annotated = "upstream_definition" in (cls.annotations or {})
            assert annotated != (name in UNANCHORED), name


def test_each_named_definition_is_an_alias():
    """A class that renders a named definition of NIST's file gives that name as an
    alias, the one second name the upstream has."""
    for anchor, name in ANCHORS.items():
        match = re.search(r"#/definitions/([^/]+)$", anchor)
        if match:
            assert list(VIEW.get_class(name).aliases) == [match[1]], name


def test_every_anchor_resolves():
    for anchor in ANCHORS:
        assert isinstance(resolve(anchor), dict), anchor


def test_the_open_objects_are_the_ones_listed():
    """The classes are closed. This list names where NIST's file is not, so a
    change to it is noticed."""
    found = {f"{SSVC}#/properties/options/items"}
    for name in _RENDERED_FILES:
        for anchor in _objects_in(name, document(name), "", set()):
            if resolve(anchor).get("additionalProperties") is not False:
                found.add(anchor)
    assert found - set(SAME_AS) == OPEN_UPSTREAM_OBJECTS, sorted(
        (found - set(SAME_AS)) ^ OPEN_UPSTREAM_OBJECTS
    )


@pytest.mark.parametrize("module", sorted(MODULES))
def test_each_header_names_its_edition(module):
    """The header's version, source and hash name the file, and the file's title
    names that version."""
    header = SchemaView(str(SCHEMA_DIR / module)).schema
    name, edition = MODULES[module]
    assert header.version == edition
    assert header.source == BASE + name
    assert header.license == "Apache-2.0"
    assert header.annotations["upstream_sha256"].value == WATCH.PINNED_SHA256[name]
    assert f"version {edition}" in document(name)["title"]


def test_the_copies_are_the_pinned_files():
    for name, pin in WATCH.PINNED_SHA256.items():
        if name in WATCH.STRUCTURE_ONLY:
            continue
        assert hashlib.sha256((UPSTREAM / name).read_bytes()).hexdigest() == pin, name


def test_the_structure_holds_no_prose():
    """NOTICE says why the SSVC file's descriptions, titles and examples are not
    held here. Only property names may read like them."""
    def prose(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in ("description", "title", "examples"):
                    yield key
                if key in ("properties", "patternProperties", "definitions"):
                    for sub in value.values():
                        yield from prose(sub)
                else:
                    yield from prose(value)
        elif isinstance(node, list):
            for item in node:
                yield from prose(item)

    assert not list(prose(document(SSVC)))


def test_the_watch_pins_what_the_references_name():
    """Every file of NIST's that a pinned file refers to is pinned, so the watch
    sees it move. The one outside reference is the departure above."""
    outside = set()
    for name in WATCH.PINNED_SHA256:
        for ref in re.findall(r'"\$ref": "([^"#][^"]*)"', json.dumps(document(name))):
            if ref.startswith(BASE):
                assert ref.removeprefix(BASE) in WATCH.PINNED_SHA256, ref
            else:
                outside.add(ref)
    assert outside == {"https://democert.org/ssvc/SSVC_Provision_v2.03.schema.json"}


def test_the_enums_of_the_data_are_each_said_to_come_from_the_data():
    for enum in set(DATA_ENUMS.values()):
        comments = " ".join(VIEW.get_enum(enum).comments)
        assert "NVD's schema" in comments and "data" in comments, enum
