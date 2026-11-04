---
type: Playbook
id: https://w3id.org/lmodel/nist-nvd/knowledge/playbooks/regenerate-and-test
title: Regenerate and test
description: "How to change the schema: edit `src/nist_nvd/schema/`, run `just lint`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just test`, and commit the output."
genre: how-to
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/generated-artefacts
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/adapt-copy
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: justfile
    resource: justfile
    title: the lint recipe
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Regenerate and test

1. Edit a module under `src/nist_nvd/schema/`, but not `cve/`.[^contributing]
2. Run `just lint`. A warning fails it as an error does.[^justfile]
3. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit what they write.[^contributing]
4. Run `just test`, which generates the schema, runs `pytest` and runs the examples.[^contributing]
5. Run `just test-nvd-feed` to validate the live modified feed.[^contributing]

[^contributing]: CONTRIBUTING.md, Before opening a pull request
[^justfile]: justfile, the lint recipe
