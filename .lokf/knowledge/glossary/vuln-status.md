---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-nvd/knowledge/glossary/vuln-status
title: vulnStatus
description: "A record's place in NVD's own analysis. NIST's schema says only that it is a string; the schema's enum holds the seven values of the real data: Analyzed, Deferred, Awaiting Analysis, Modified, Received, Undergoing Analysis and Rejected."
genre: reference
definedBy:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: nvd_cve.yaml
    resource: src/nist_nvd/schema/nvd_cve.yaml
    title: NvdVulnStatus
  - id: about.md
    resource: docs/about.md
    title: Names
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# vulnStatus

`vulnStatus` says where a vulnerability stands in NVD's own analysis. NIST's schema says only that it is a string. The enum `NvdVulnStatus` holds the seven values of the 33,378 records read on 2026-11-03. A new value fails validation, and the feed test reports it.[^nvd_cve.yaml]

NVD's page that defines the values refuses an automated client, so each value's description says only what its name and the data show.[^about.md]

[^nvd_cve.yaml]: src/nist_nvd/schema/nvd_cve.yaml, NvdVulnStatus
[^about.md]: docs/about.md, Names
