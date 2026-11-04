# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML model of the JSON responses of the NVD API 2.0, from the JSON schemas NIST publishes: the vulnerability response at edition 2.2.4, the product and match-string responses at 2.0, and the change history at 2.0.1.** NVD's own keys and values are the schema's, so a real response validates unchanged.
- **The rule of NIST's `oneOf` on an affected version, the cardinalities, patterns and bounds of its files, and enums where the real data fixes a list**, such as the seven values of `vulnStatus`.
- **A vendored copy of lmodel/cve's `cve_cvss` module** for the score objects, held to its git object hash and walked against NVD's own CVSS files.
- **A crosswalk to CVE and KEV**: the `id` and the four CISA fields are exact, checked on real data against all 1,766 entries of the catalog; NVD's timestamps are related to the CVE record's, and its other parts close. Mappings to schema.org, Dublin Core, DCAT, PROV-O, SPDX 3.0.1 Security, STIX, the SEPSES vocabularies and Wikidata were each read at their source.
- **Coverage held by tests**: `tests/test_upstream.py` walks NIST's files and lists each departure with its reason, and `tests/test_mappings.py` holds each mapping to what was read or to a neighbour's copy.
- **Real data in tests**: a committed extract of the API's answers, and `just test-nvd-feed` and a CI job that validate every record of NVD's live modified feed.
- **A weekly upstream watch** that compares each of NIST's files with its pinned SHA-256, and says when a check could not run rather than calling that a change.
- **`.lokf/nist-nvd.yaml`, the schema's `lokf adapt` copy, rooted on `NvdCve`.** The knowledge release attaches it as `schema-<tag>-nist-nvd.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of the neighbours' copies.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **The project moves to linkml-project-copier v0.5.0, with linkml and linkml-runtime locked at 1.12.1.** Its Python project is named `nist-nvd-linkml`, PyPI publishing stays off, and the generators' settings are in `.linkml/generators.yaml`.
- **The repository takes the family's governance files and hardened continuous integration**: `SECURITY.md`, `AI_COVENANT.md`, `NOTICE`, the `CONTRIBUTING` checklist, lychee and markdownlint settings and `lint-and-docs.yaml`.
- **Every class, slot and value is renamed to NVD's own**, with classes under the `Nvd` prefix. The old names were the schema's own, and no real record used them.

### Removed

- **The schema's import of `vulnerability-core`**, whose base classes fit no real record.
- **`MetricSet`, `CVSSScoreNote`, `StatusTransition` and `KnownExploitedVulnerability`, and the invented status list**, which model NVD's detail page and match no response.
- **`src/nist_nvd/mappings/cve_to_nist_nvd.sssom.tsv`, whose rows named elements that are gone and rested on unverified language-model matches.** The schema's mappings are now the one home for mappings, each held by a test.
- **`BUG.txt`, the three scripts that patched LinkML 1.11's output, the PyPI publishing workflow and the mkdocs site.** LinkML 1.12.1 and the new schema need no patches, and the knowledge website replaces the site.
