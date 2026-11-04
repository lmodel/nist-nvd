---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nvd-extract
title: Extract of real NVD responses
description: "`tests/data/nvd/`, real answers of the NVD API read on 2026-11-03 and unchanged: one record for each case worth showing, and samples of the product, match-string and change-history responses."
genre: reference
resource: tests/data/nvd
isPartOf:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/example-data
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-api
sources:
  - id: extract-readme
    resource: tests/data/nvd/README.md
    title: the whole file
  - id: test_data.py
    resource: tests/test_data.py
    title: EXTRACT_CASES
  - resource: tests/data/nvd
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Extract of real NVD responses

Each file under `tests/data/nvd/` is one answer of the NVD API, read on 2026-11-03 and unchanged. Each `cve-` file is the smallest record that shows one case: each `vulnStatus`, each CVSS version, SSVC, the CISA fields, vendor comments, each evaluator field, each CVE tag, a nested configuration, a version range and others.[^extract-readme]

`tests/test_data.py` validates each against the class of its kind, and fails if a case goes missing. `tests/test_generated_json_schema.py` validates each against the committed JSON Schema too.[^test_data.py]

[^extract-readme]: tests/data/nvd/README.md, the whole file
[^test_data.py]: tests/test_data.py, EXTRACT_CASES
