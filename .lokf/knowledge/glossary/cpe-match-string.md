---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-nvd/knowledge/glossary/cpe-match-string
title: CPE match string
description: A Common Platform Enumeration (CPE) pattern, with an optional version range, that a vulnerability's configurations use and the match-string API lists with the CPE names it matches. `matchCriteriaId` is its UUID.
genre: reference
definedBy:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: nvd_core.yaml
    resource: src/nist_nvd/schema/nvd_core.yaml
    title: criteria
  - id: nvd_cpematch.yaml
    resource: src/nist_nvd/schema/nvd_cpematch.yaml
    title: NvdMatchString
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# CPE match string

A Common Platform Enumeration (CPE) match string is a pattern, with an optional version range, in the `criteria` key.[^nvd_core.yaml] A vulnerability's configurations use one in each `NvdCpeMatch`, with a flag saying whether what it matches has the vulnerability. The match-string API lists each as a `NvdMatchString`, with the CPE names it matches.[^nvd_cpematch.yaml]

`matchCriteriaId` identifies a match string in the match-string response. It does not identify a use of one in a configuration, where the same string can recur with a different flag.[^nvd_cpematch.yaml]

[^nvd_core.yaml]: src/nist_nvd/schema/nvd_core.yaml, criteria
[^nvd_cpematch.yaml]: src/nist_nvd/schema/nvd_cpematch.yaml, NvdMatchString
