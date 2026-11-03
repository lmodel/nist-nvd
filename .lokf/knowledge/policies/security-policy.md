---
type: Policy
id: https://w3id.org/lmodel/nist-nvd/knowledge/policies/security-policy
title: Security policy
description: "`SECURITY.md`: report by GitHub's private vulnerability reporting, only the latest release gets fixes, what each workflow may do, what the watch and the feed fetch read, and what is not covered, such as NVD's data and a flaw in a product NVD lists."
genre: reference
resource: SECURITY.md
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/main
sources:
  - id: security
    resource: SECURITY.md
    title: the whole file
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Security policy

`SECURITY.md` says to report by GitHub's private vulnerability reporting, not a public issue. Only the latest release receives fixes. A vulnerability in a product NVD lists is not one in this repository.[^security]

It lists what executes here and what holds each surface. `scripts/check_upstream_release.py` runs only in the weekly watch, is given no token, reads at most 5 MB of an answer, follows a redirect only over https to `csrc.nist.gov`, and quotes server text as code on one line. `scripts/fetch_nvd_feed.py` keeps the feed only when it matches the feed's own `.meta` file, and follows a redirect only over https to `nvd.nist.gov`.[^security]

Two settings are not yet in force, it says: required reviewers on the `release` Environment, and secret scanning with push protection.[^security]

[^security]: SECURITY.md, the whole file
