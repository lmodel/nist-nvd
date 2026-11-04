---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/example-data
title: Example data
description: "The examples the tests hold the schema to, under `tests/data/`: valid examples, counter-examples that each name the JSON pointer they fail at, a folder for valid data LinkML's example runner cannot take, and a committed extract of real NVD responses."
genre: reference
resource: tests/data
hasPart:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nvd-extract
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: data-readme
    resource: tests/data/README.md
    title: the whole file
  - id: test_data.py
    resource: tests/test_data.py
    title: test_counter_examples_fail_where_they_say
  - id: nvd_rules.py
    resource: tests/nvd_rules.py
    title: the module's docstring
  - resource: tests/data
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Example data

`tests/data/` holds the examples, and `tests/data/README.md` says what each folder is for:[^data-readme]

- `valid/` holds data that conforms, named `ClassName-anything.yaml`. These are this project's own, not real records.
- `invalid/` holds counter-examples. The first line of each, `# Fails at: <pointer>`, names where the validator must report it, and `tests/test_data.py` fails one that fails anywhere else.[^test_data.py]
- `problem/valid/` holds valid data that LinkML 1.12.1's example runner cannot take.
- `nvd/` holds real answers of the API, each unchanged.

`tests/nvd_rules.py` checks two of NIST's statements that the generated JSON Schema does not: that a list NIST marks unique has no repeats, and that a CVSS 4.0 score is a multiple of 0.1.[^nvd_rules.py]

[^data-readme]: tests/data/README.md, the whole file
[^test_data.py]: tests/test_data.py, test_counter_examples_fail_where_they_say
[^nvd_rules.py]: tests/nvd_rules.py, the module's docstring
