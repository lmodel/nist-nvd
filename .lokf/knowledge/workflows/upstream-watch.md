---
type: Service
id: https://w3id.org/lmodel/nist-nvd/knowledge/workflows/upstream-watch
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its `nvd-schemas` job runs `scripts/check_upstream_release.py` against NIST's files, and on a finding, or a check that could not run, opens or updates an issue."
genre: reference
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` runs every Monday at 07:00 UTC and by hand. Its one job, `nvd-schemas`, reads the checkout and holds `issues: write`. It runs `scripts/check_upstream_release.py` with no token. When that fails, `.github/scripts/report-issue.sh` opens an issue, or comments on the one already open.[^upstream-watch.yaml]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the jobs
