---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-nvd/knowledge/glossary/ssvc
title: SSVC
description: Stakeholder-Specific Vulnerability Categorization, a decision through a tree of questions. NVD's `ssvcV203` metric records the answers chosen, as one-key objects such as `exploitation`, `automatable` and `technicalImpact`, with the role of whoever decided.
genre: reference
definedBy:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: nvd_cve.yaml
    resource: src/nist_nvd/schema/nvd_cve.yaml
    title: NvdSsvcData and NvdSsvcOption
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# SSVC

Stakeholder-Specific Vulnerability Categorization (SSVC) reaches a decision through a tree of questions. NVD's `ssvcV203` metric records the answers chosen, with the role of whoever decided.[^nvd_cve.yaml]

NIST's file allows any key in an answer, with a string or a list of strings as its value, and the class `NvdSsvcOption` states that with `extra_slots`. The real data holds one key per object, and only `exploitation`, `automatable` and `technicalImpact`, each with a string. They are named because LinkML's Pydantic generator ignores `extra_slots`.[^nvd_cve.yaml]

[^nvd_cve.yaml]: src/nist_nvd/schema/nvd_cve.yaml, NvdSsvcData and NvdSsvcOption
