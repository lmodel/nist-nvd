---
type: Reference
id: https://w3id.org/lmodel/nist-nvd/knowledge/references/first-cvss-schemas
title: FIRST's CVSS schemas
description: The CVSS JSON schemas of the Forum of Incident Response and Security Teams (FIRST), versions 2.0, 3.0, 3.1 and 4.0, of which NIST publishes copies under `external/`. Each carries FIRST's copyright notice and BSD-style licence inside the file.
genre: reference
resource: upstream/external
relatedTo:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/cvss-module
sources:
  - id: notice
    resource: NOTICE
    title: The Forum of Incident Response and Security Teams
  - id: feed
    resource: tests/test_nvd_feed.py
    title: KNOWN_BREACHES_OF_NVDS_SCHEMA
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# FIRST's CVSS schemas

`upstream/external/` holds NIST's copies of FIRST's CVSS schemas, each unchanged and each carrying FIRST's copyright notice and BSD-style licence inside the file.[^notice]

NVD's copy of CVSS 4.0 says `multipleOf: 0.1`. A JSON Schema validator computes that in binary floating point, where 7.1 is no multiple of 0.1, so NVD's own schema refuses 2,110 scores of the modified feed of 2026-11-03 that are right. `tests/nvd_rules.py` checks the step in decimal.[^feed]

[^notice]: NOTICE, The Forum of Incident Response and Security Teams
[^feed]: tests/test_nvd_feed.py, KNOWN_BREACHES_OF_NVDS_SCHEMA
