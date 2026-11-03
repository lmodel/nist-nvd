---
type: Policy
id: https://w3id.org/lmodel/nist-nvd/knowledge/policies/license-and-attribution
title: License and attribution
description: The code is under Apache-2.0 and the bundle under CC BY 4.0. NOTICE carries NVD's notice that it does not endorse or certify this product, NIST's statement on its works, FIRST's position on the CVSS schemas, and why the SSVC file's descriptions are not copied.
genre: reference
resource: NOTICE
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-api
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/first-cvss-schemas
sources:
  - id: readme
    resource: README.md
    title: License
  - id: notice
    resource: NOTICE
    title: the whole file
  - resource: LICENSE
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# License and attribution

The code is under the Apache License 2.0, and the bundle under CC BY 4.0.[^readme]

`NOTICE` carries:[^notice]

- NVD's notice: this product uses the NVD API but is not endorsed or certified by the NVD. The README carries it too.
- NIST's statement on its data and works, which it asks a distribution to carry.
- Why NIST's SSVC file is held only as its structure.
- FIRST's copyright notice and licence, which stay inside each CVSS file.
- lmodel/cve's module, the copier template's MIT licence and the sidecar's and website's origin.

[^readme]: README.md, License
[^notice]: NOTICE, the whole file
