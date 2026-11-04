---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/upstream-copies
title: Copies of NIST's JSON schemas
description: "`upstream/`, the JSON schemas of the NVD API 2.0 as NIST publishes them, each pinned by SHA-256 in the watch. All are copied unchanged but the SSVC schema, of which only the structure is held."
genre: reference
resource: upstream
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
sources:
  - id: upstream-readme
    resource: upstream/README.md
    title: the whole file
  - id: notice
    resource: NOTICE
    title: NIST's SSVC schema
  - id: watch
    resource: scripts/check_upstream_release.py
    title: PINNED_SHA256
  - resource: upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Copies of NIST's JSON schemas

`upstream/` holds NIST's four response schemas, `cve_affected_1.0.json` and NIST's copies of FIRST's CVSS schemas under `external/`, each unchanged.[^upstream-readme]

`ssvc-v2.0.3.structure.json` is NIST's SSVC file with every description, title and example removed. NIST's file states no licence, and its subject is the CERT Coordination Center's work, whose repository places its material under other terms, so this project copies none of those words.[^notice]

`scripts/check_upstream_release.py` pins each file's SHA-256, and `tests/test_upstream.py` checks the copies and the schema headers against those pins.[^watch]

[^upstream-readme]: upstream/README.md, the whole file
[^notice]: NOTICE, NIST's SSVC schema
[^watch]: scripts/check_upstream_release.py, PINNED_SHA256
