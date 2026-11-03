---
type: Reference
id: https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-api
title: The NVD API and data feeds
description: NVD's vulnerability, product and match-string APIs at `services.nvd.nist.gov/rest/json/`, and the modified feed at `nvd.nist.gov/feeds/json/cve/2.0/`, whose `.meta` file gives its size and SHA-256. NVD's `nvd.nist.gov` web pages refuse an automated client.
genre: reference
relatedTo:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
source:
  - https://services.nvd.nist.gov/rest/json/cves/2.0
sources:
  - id: extract-readme
    resource: tests/data/nvd/README.md
    title: the whole file
  - id: fetch
    resource: scripts/fetch_nvd_feed.py
    title: the docstring
  - id: notice
    resource: NOTICE
    title: the opening
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# The NVD API and data feeds

The extract comes from `services.nvd.nist.gov/rest/json/`, by the requests its README names.[^extract-readme] The feed test reads `https://nvd.nist.gov/feeds/json/cve/2.0/nvdcve-2.0-modified.json.gz`, and checks it against the size and the SHA-256 that its `.meta` file gives.[^fetch]

NVD's terms of use, at `https://nvd.nist.gov/developers/terms-of-use`, refused a plain client with 403 on 2026-11-03. This project cites them by address and date, and read them that day in the copy at `https://scancode-licensedb.aboutcode.org/nist-nvd-api-tou.html`. They ask a service that uses or accesses the API for a notice, which NOTICE and the README carry.[^notice]

[^extract-readme]: tests/data/nvd/README.md, the whole file
[^fetch]: scripts/fetch_nvd_feed.py, the docstring
[^notice]: NOTICE, the opening
