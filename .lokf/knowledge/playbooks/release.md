---
type: Playbook
id: https://w3id.org/lmodel/nist-nvd/knowledge/playbooks/release
title: Release a version
description: "How a version is released: changelog entries under `## [Unreleased]`, a releasing commit type, the `v0.0.0` baseline tag before the first release, and `semantic-release.yml`, which tags and publishes on the merge and dispatches the knowledge release."
genre: how-to
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/knowledge-release
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/semantic-release
sources:
  - id: contributing
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: releaserc
    resource: .releaserc.json
    title: the release rules
  - id: changelog
    resource: CHANGELOG.md
    title: the baseline paragraph
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Release a version

1. Write each change under `## [Unreleased]` in `CHANGELOG.md`. The release job refuses an empty section.[^contributing]
2. Type the commit for what it is. Only `feat:`, `fix:`, `security:` and a breaking change start a release, and below 1.0.0 a breaking change bumps the minor version.[^releaserc]
3. Before the first releasing merge, push the `v0.0.0` baseline tag on `main`, so the first release is 0.1.0.[^changelog]
4. On the merge, `semantic-release.yml` retitles the section, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub release. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches the knowledge release.[^contributing]

[^contributing]: CONTRIBUTING.md, Releasing (maintainers)
[^releaserc]: .releaserc.json, the release rules
[^changelog]: CHANGELOG.md, the baseline paragraph
