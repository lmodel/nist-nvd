---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/adapt-copy
title: The adapt copy
description: "`.lokf/schema/nist-nvd.yaml`, the copy `just lokf-adapt` writes from the schema with `--root NvdCve --prefix cve`, so it can sit beside LOKF's schema. It is the bundle's domain schema, and a release attaches it as `schema-<tag>-nist-nvd.yaml`."
genre: reference
resource: .lokf/schema/nist-nvd.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: project.justfile
    resource: project.justfile
    title: the knowledge bundle section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: RENAMED, SHARED_WITH_NEIGHBOURS and the lokf 0.9.0 test
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:22:40Z"
status: draft
---

# The adapt copy

`just lokf-adapt` runs `lokf adapt` with `--root NvdCve --prefix cve` and writes `.lokf/schema/nist-nvd.yaml`. `just lokf-adapt-check` fails when the copy is stale. `.lokf/justfile` names it as the bundle's domain schema.[^project.justfile]

The one root is `NvdCve`, because adapt replaces the schema's identifier slot, `id`, with LOKF's own and refuses a class that lists it without descending from `Concept`. The copy renames thirteen keys that LOKF also defines, such as `references` to `cve_references`, and keeps each key's IRI. The prefix is `cve` so that the CVSS module's `version` gets the name lmodel/cve's own copy gives it, and the prefix applies to NVD's keys too.[^project.justfile]

`tests/test_schema_rules.py` lists every name the copy shares with LOKF or a neighbour's copy, and fails on a new one. It also records a limit of lokf 0.9.0: the copy gives the CVSS module's attributes this schema's namespace, where the source gives them `cve:`.[^test_schema_rules.py]

[^project.justfile]: project.justfile, the knowledge bundle section
[^test_schema_rules.py]: tests/test_schema_rules.py, RENAMED, SHARED_WITH_NEIGHBOURS and the lokf 0.9.0 test
