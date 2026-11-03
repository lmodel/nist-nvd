---
type: Playbook
id: https://w3id.org/lmodel/nist-nvd/knowledge/playbooks/validate-an-nvd-response
title: Validate an NVD response
description: How to validate a file against the schema with `linkml-validate`, naming the kind of response with `-C NvdCveResponse`, `NvdCpeResponse`, `NvdCpeMatchResponse` or `NvdHistoryResponse`.
genre: how-to
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:45:03Z"
status: draft
---

# Validate an NVD response

NVD has four kinds of response and no document that holds them, so name the kind:[^index.md]

```bash
linkml-validate -s src/nist_nvd/schema/nist_nvd.yaml -C NvdCveResponse response.json
```

Use `NvdCpeResponse` for the product API, `NvdCpeMatchResponse` for the match-string API and `NvdHistoryResponse` for the change-history API.[^index.md]

`linkml-validate` reads a `.json` file through a LinkML loader that drops every empty list. So it reports `references` as missing on each rejected record, whose `references` NVD writes as an empty list. The same response validates as a `.yaml` file, and against `project/jsonschema/nist_nvd.schema.json`.[^index.md]

`tests/test_nvd_feed.py` validates a feed one record at a time, as the class `NvdCve`.[^index.md]

[^index.md]: docs/index.md, Validating data
