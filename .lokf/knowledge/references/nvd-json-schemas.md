---
type: Reference
id: https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
title: NIST's NVD API JSON schemas
description: "The JSON schemas NIST publishes at `https://csrc.nist.gov/schema/nvd/api/2.0/`: the vulnerability schema at edition 2.2.4, products and match strings at 2.0, change history at 2.0.1. NIST changes them in place, so they are pinned by SHA-256."
genre: reference
source:
  - https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema
sources:
  - id: upstream-readme
    resource: upstream/README.md
    title: the table
  - id: notice
    resource: NOTICE
    title: The National Vulnerability Database
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# NIST's NVD API JSON schemas

NIST publishes one JSON schema per response of the NVD API 2.0, with two more files they reference and its copies of FIRST's CVSS schemas. The editions are in each file's title: *version 2.2.4* for vulnerabilities, 2.0 for products and for match strings, and 2.0.1 for change history.[^upstream-readme]

The files have no release and no git object, so this project pins each by SHA-256. NIST's works are not subject to copyright in the United States, and may be elsewhere. NOTICE carries the statement NIST asks a distribution to carry.[^notice]

[^upstream-readme]: upstream/README.md, the table
[^notice]: NOTICE, The National Vulnerability Database
