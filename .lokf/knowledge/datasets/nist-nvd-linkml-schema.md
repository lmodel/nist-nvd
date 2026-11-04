---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
title: NVD LinkML schema
description: "The LinkML schema of the NVD API 2.0's JSON responses, under `src/nist_nvd/schema/`: the umbrella `nist_nvd` over the modules `nvd_core`, `nvd_cve`, `nvd_cpe`, `nvd_cpematch` and `nvd_history`, and the vendored `cve_cvss`. It keeps NVD's keys, so a real response validates unchanged."
genre: reference
resource: src/nist_nvd/schema
hasPart:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/cvss-module
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/worked-record-cve-2023-29357
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
sources:
  - id: nist_nvd.yaml
    resource: src/nist_nvd/schema/nist_nvd.yaml
    title: the header and its comments
  - id: about.md
    resource: docs/about.md
    title: the module table and Names
  - id: linkmllint
    resource: .linkmllint.yaml
    title: the comment
  - resource: src/nist_nvd/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# NVD LinkML schema

`src/nist_nvd/schema/nist_nvd.yaml` is the umbrella, with the identifier `https://w3id.org/lmodel/nist-nvd`, and it holds only imports. Its version is 2.2.4, the edition of NVD's vulnerability schema as its title names it.[^nist_nvd.yaml]

The modules follow NVD's responses:[^about.md]

| Module | Renders | Edition |
| --- | --- | --- |
| `nvd_cve` | the vulnerability response, which NVD's data feeds share | 2.2.4 |
| `nvd_cpe` | the product response | 2.0 |
| `nvd_cpematch` | the match-string response | 2.0 |
| `nvd_history` | the change-history response | 2.0.1 |
| `nvd_core` | the fields of a page and the keys several responses share | none of its own |

NVD has four kinds of response and no document that holds them. So each response module marks its own response class as a tree root, and the generators write `NvdCveResponse` as the top class. A reader names the kind when validating, with `linkml-validate -C`.[^nist_nvd.yaml]

Classes and enums carry the `Nvd` prefix. Slots and permissible values keep NVD's spelling, such as `vulnStatus` and `Awaiting Analysis`.[^about.md] `.linkmllint.yaml` relaxes the naming rule for that reason, and says so in its comment.[^linkmllint]

[^nist_nvd.yaml]: src/nist_nvd/schema/nist_nvd.yaml, the header and its comments
[^about.md]: docs/about.md, the module table and Names
[^linkmllint]: .linkmllint.yaml, the comment
