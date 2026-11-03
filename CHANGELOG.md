# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Changed

- **The project moves to linkml-project-copier v0.5.0, with linkml and linkml-runtime locked at 1.12.1.** Its Python project is named `nist-nvd-linkml`, PyPI publishing stays off, and the generators' settings are in `.linkml/generators.yaml`.
- **The repository takes the family's governance files and hardened continuous integration**: `SECURITY.md`, `AI_COVENANT.md`, `NOTICE`, the `CONTRIBUTING` checklist, lychee and markdownlint settings and `lint-and-docs.yaml`.

### Removed

- **`src/nist_nvd/mappings/cve_to_nist_nvd.sssom.tsv`, whose rows named elements that are gone and rested on unverified language-model matches.** The schema's mappings are now the one home for mappings, each held by a test.
- **`BUG.txt` and the three scripts that patched LinkML 1.11's output**, which 1.12.1 and the new schema do not need.
