---
type: Explanation
id: https://w3id.org/lmodel/nist-nvd/knowledge/explanations/crosswalk-and-mappings
title: The crosswalk to CVE and KEV, and other mappings
description: "How the schema maps to lmodel/cve, lmodel/kev-catalog and public vocabularies, and which mappings rest on data: the `id` and the four CISA fields are exact, NVD's timestamps only related. The hand-kept SSSOM file is gone, and the schema is the one home for mappings."
genre: reference
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/neighbour-copies
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: readme
    resource: README.md
    title: Mappings
  - id: test_mappings.py
    resource: tests/test_mappings.py
    title: CROSSWALK and its tests
  - id: nvd_cve.yaml
    resource: src/nist_nvd/schema/nvd_cve.yaml
    title: the published attribute
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# The crosswalk to CVE and KEV, and other mappings

NVD republishes CVE and KEV, and the schema says so with mappings, which point from NVD to the two others.[^readme]

- `id` is in `exact_mappings` to `cve:cveId` and `kev_catalog:cveID`.
- `cisaExploitAdd`, `cisaActionDue`, `cisaRequiredAction` and `cisaVulnerabilityName` are in `exact_mappings` to `kev_catalog:dateAdded`, `dueDate`, `requiredAction` and `vulnerabilityName`. Each equals the catalog's value for all 1,766 entries of the catalog of 2026-11-03, read through the API.[^test_mappings.py]
- `published` and `lastModified` are only in `related_mappings` to `cve:datePublished` and `cve:dateUpdated`, because they are NVD's own times. For CVE-2021-44228 the CVE record says 2021-12-10T00:00:00.000Z and NVD says 2021-12-10T10:15:09.143.[^nvd_cve.yaml]
- A reference's `tags` map to nothing. They are NVD's own vocabulary, not the CVE Program's.[^test_mappings.py]

`tests/test_mappings.py` holds each mapping to a prefix the schema binds, and to a term read at its source or in a neighbour's copy.[^test_mappings.py]

An SSSOM file once kept beside the schema is gone. Its rows named elements that no longer exist and rested on language-model matches that no source confirmed.[^readme]

[^readme]: README.md, Mappings
[^test_mappings.py]: tests/test_mappings.py, CROSSWALK and its tests
[^nvd_cve.yaml]: src/nist_nvd/schema/nvd_cve.yaml, the published attribute
