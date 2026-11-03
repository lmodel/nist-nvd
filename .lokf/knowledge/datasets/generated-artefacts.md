---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/generated-artefacts
title: Generated artefacts
description: "What the generators write from the schema, and which is never edited by hand: `project/`, `src/nist_nvd/datamodel/` and `docs/schema/nist_nvd.yaml`, under the settings in `.linkml/generators.yaml`."
genre: reference
resource: project
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: config-public
    resource: config.public.mk
    title: LINKML_GENERATORS_CONFIG_YAML
  - id: generators
    resource: .linkml/generators.yaml
    title: the jsonschema settings
  - resource: project
  - resource: src/nist_nvd/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Generated artefacts

`just gen-project` writes `project/` and the Python models in `src/nist_nvd/datamodel/`, and `just gen-doc` writes `docs/schema/nist_nvd.yaml` and the pages under `docs/elements/`, which git ignores. None of these is edited by hand.[^contributing]

`config.public.mk` points the justfile at `.linkml/generators.yaml`.[^config-public] Under `jsonschema`, that file names `NvdCveResponse` as the top class and turns off `include_null`, so an optional key is absent or holds a value, as in NVD's own schemas. `tests/test_generated_json_schema.py` validates the extract against the committed `project/jsonschema/nist_nvd.schema.json`.[^generators]

[^contributing]: CONTRIBUTING.md, Before opening a pull request
[^config-public]: config.public.mk, LINKML_GENERATORS_CONFIG_YAML
[^generators]: .linkml/generators.yaml, the jsonschema settings
