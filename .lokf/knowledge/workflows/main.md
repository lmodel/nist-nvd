---
type: Service
id: https://w3id.org/lmodel/nist-nvd/knowledge/workflows/main
title: Build and test (main.yaml)
description: "The Build and test workflow, `.github/workflows/main.yaml`: on a push to `main` and every pull request, its `test` job lints, tests and checks the adapt copy across Python 3.10 to 3.14, and its `nvd-feed` job validates NVD's live modified feed."
genre: reference
resource: .github/workflows/main.yaml
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/example-data
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-api
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` runs on a push to `main` and on every pull request. Its `test` job runs `just test` on Python 3.10 to 3.14. On 3.13 alone it also runs `just lint` and `just lokf-adapt-check`. Its `nvd-feed` job runs `just test-nvd-feed`, which fetches the feed and validates every record. The feed is live, so a red `nvd-feed` job can be NVD's change and not the pull request's, and its comment says to keep it out of a ruleset's required checks. Both jobs read the checkout only, and install with `uv sync --locked`.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml, the header comment, the on key and the jobs
