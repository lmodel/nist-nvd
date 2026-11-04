---
type: Explanation
id: https://w3id.org/lmodel/nist-nvd/knowledge/explanations/what-each-checker-checks
title: What each checker checks
description: "What the validator, the Python rules and the generated Python models each check: `linkml-validate` covers NIST's keys, value lists, patterns and bounds and the version rule, `tests/nvd_rules.py` covers uniqueness and the CVSS 4.0 score step, and the generated models check less."
genre: reference
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
relatedTo:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/example-data
sources:
  - id: index.md
    resource: docs/index.md
    title: Validating data
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# What each checker checks

`linkml-validate` checks each key, value list, pattern, cardinality and bound of NIST's files, and refuses a key they do not name. It checks that a `NvdAffectedVersion` is a single version or a range, as NIST's `oneOf` has it, and each CVSS score against the CVSS module.[^index.md]

The generated JSON Schema leaves out two of NIST's statements, so `tests/nvd_rules.py` checks them over the examples and the feed: that a list NIST marks unique has no repeats, and that a CVSS 4.0 score is a multiple of 0.1.[^index.md]

The generated Python models check less. The dataclasses refuse an empty list for a required key, as a rejected record's `references` has, and neither model checks a pattern from a type or applies a rule. The dataclasses turn a change's list value into a string, and the Pydantic model refuses a change's list or object value and any SSVC decision point beyond the three the data holds.[^index.md]

[^index.md]: docs/index.md, Validating data
