---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/neighbour-copies
title: Neighbours' adapt copies
description: "`tests/neighbours/`, the adapt copies of other lmodel schemas, each pinned by SHA-256 in `tests/test_schema_rules.py`: slsa, github-actions, in-toto, oscal, spdx, stix, uco, cve and kev-catalog."
genre: reference
resource: tests/neighbours
relatedTo:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/adapt-copy
sources:
  - id: rules
    resource: tests/test_schema_rules.py
    title: NEIGHBOURS and SHARED_WITH_NEIGHBOURS
  - id: mappings
    resource: tests/test_mappings.py
    title: LMODEL
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-04T21:51:12Z"
status: draft
---

# Neighbours' adapt copies

`tests/neighbours/` holds the adapt copies of lmodel/slsa, github-actions, in-toto, oscal, spdx, stix, uco, cve and kev-catalog, each the schema asset of its newest release that carries one, and checked against its `.sha256` and attestation.[^rules]

`tests/test_schema_rules.py` pins each by SHA-256, and fails on a key shared under another IRI that it does not list. `tests/test_mappings.py` checks each mapping into lmodel/cve, lmodel/kev-catalog and lmodel/stix against the copy of that neighbour.[^mappings]

[^rules]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
[^mappings]: tests/test_mappings.py, LMODEL
