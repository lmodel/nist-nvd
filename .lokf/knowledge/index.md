---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-nvd/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-nvd Knowledge Bundle
description: A LinkML model of the JSON responses of the National Vulnerability Database (NVD) API 2.0, from the JSON schemas NIST publishes.
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-nvd/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-nvd Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-nvd. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-nvd/`: the README as its home page, the docs, the schema's pages and the bundle, with redirects for the retired mkdocs addresses.

# Datasets

* [NVD LinkML schema](datasets/nist-nvd-linkml-schema.md) - The LinkML schema of the NVD API 2.0's JSON responses, under `src/nist_nvd/schema/`: the umbrella `nist_nvd` over the modules `nvd_core`, `nvd_cve`, `nvd_cpe`, `nvd_cpematch` and `nvd_history`, and the vendored `cve_cvss`. It keeps NVD's keys, so a real response validates unchanged.
* [Vendored CVSS module](datasets/cvss-module.md) - lmodel/cve's `cve_cvss` module, copied unchanged to `src/nist_nvd/schema/cve/` and held to its git object hash by `tests/test_cve_import.py`, which also walks NVD's own CVSS files against it. Its classes are `CvssV20`, `CvssV30`, `CvssV31` and `CvssV40`.
* [Generated artefacts](datasets/generated-artefacts.md) - What the generators write from the schema, and which is never edited by hand: `project/`, `src/nist_nvd/datamodel/` and `docs/schema/nist_nvd.yaml`, under the settings in `.linkml/generators.yaml`.
* [The adapt copy](datasets/adapt-copy.md) - `.lokf/nist-nvd.yaml`, the copy `just lokf-adapt` writes from the schema with `--root NvdCve --prefix cve`, so it can sit beside LOKF's schema. It is the bundle's domain schema, and a release attaches it as `schema-<tag>-nist-nvd.yaml`.
* [Copies of NIST's JSON schemas](datasets/upstream-copies.md) - `upstream/`, the JSON schemas of the NVD API 2.0 as NIST publishes them, each pinned by SHA-256 in the watch. All are copied unchanged but the SSVC schema, of which only the structure is held.
* [Example data](datasets/example-data.md) - The examples the tests hold the schema to, under `tests/data/`: valid examples, counter-examples that each name the JSON pointer they fail at, a folder for valid data LinkML's example runner cannot take, and a committed extract of real NVD responses.
* [Extract of real NVD responses](datasets/nvd-extract.md) - `tests/data/nvd/`, real answers of the NVD API read on 2026-11-03 and unchanged: one record for each case worth showing, and samples of the product, match-string and change-history responses.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - `tests/neighbours/`, the adapt copies of other lmodel schemas, each pinned by SHA-256 in `tests/test_schema_rules.py`. The released ones are slsa, github-actions, in-toto, oscal, spdx, stix and uco; `cve` and `kev-catalog` come from their unreleased branches for now.
* [Mapping terms read at their sources](datasets/vocabulary-terms.md) - `tests/vocabulary-terms.txt`, the IRI of every term outside lmodel that the schema's mappings name, each read at its source on 2026-11-03: Dublin Core, schema.org, DCAT, PROV-O, SPDX 3.0.1, the SEPSES vocabularies and Wikidata.
* [The record for CVE-2023-29357](datasets/worked-record-cve-2023-29357.md) - NVD's record for CVE-2023-29357, a Microsoft SharePoint Server flaw in the KEV catalog, as a worked example of a concept typed `NvdCve`. Its keys come from `tests/data/nvd/cve-CVE-2023-29357.json`, cut down to the ones it needs.

# References

* [NIST's NVD API JSON schemas](references/nvd-json-schemas.md) - The JSON schemas NIST publishes at `https://csrc.nist.gov/schema/nvd/api/2.0/`: the vulnerability schema at edition 2.2.4, products and match strings at 2.0, change history at 2.0.1. NIST changes them in place, so they are pinned by SHA-256.
* [The NVD API and data feeds](references/nvd-api.md) - NVD's vulnerability, product and match-string APIs at `services.nvd.nist.gov/rest/json/`, and the modified feed at `nvd.nist.gov/feeds/json/cve/2.0/`, whose `.meta` file gives its size and SHA-256. NVD's `nvd.nist.gov` web pages refuse an automated client.
* [FIRST's CVSS schemas](references/first-cvss-schemas.md) - The CVSS JSON schemas of the Forum of Incident Response and Security Teams (FIRST), versions 2.0, 3.0, 3.1 and 4.0, of which NIST publishes copies under `external/`. Each carries FIRST's copyright notice and BSD-style licence inside the file.

# Explanations

* [Where the schema departs from NIST's files](explanations/departures-from-nists-files.md) - The places where the schema and NIST's JSON schemas part, each with its reason: timestamps with no UTC offset, a repository address RFC 3986 refuses, SSVC's `$schema` and decision tree, closed classes, and the enums the data fixes. `tests/test_upstream.py` lists each.
* [The crosswalk to CVE and KEV, and other mappings](explanations/crosswalk-and-mappings.md) - How the schema maps to lmodel/cve, lmodel/kev-catalog and public vocabularies, and which mappings rest on data: the `id` and the four CISA fields are exact, NVD's timestamps only related. The hand-kept SSSOM file is gone, and the schema is the one home for mappings.
* [What each checker checks](explanations/what-each-checker-checks.md) - What the validator, the Python rules and the generated Python models each check: `linkml-validate` covers NIST's keys, value lists, patterns and bounds and the version rule, `tests/nvd_rules.py` covers uniqueness and the CVSS 4.0 score step, and the generated models check less.

# Glossary

* [National Vulnerability Database (NVD)](glossary/nvd.md) - The National Vulnerability Database, which NIST runs. It republishes each CVE record with its own analysis: a status, scores, weaknesses and the product configurations that have the vulnerability.
* [vulnStatus](glossary/vuln-status.md) - A record's place in NVD's own analysis. NIST's schema says only that it is a string; the schema's enum holds the seven values of the real data: Analyzed, Deferred, Awaiting Analysis, Modified, Received, Undergoing Analysis and Rejected.
* [SSVC](glossary/ssvc.md) - Stakeholder-Specific Vulnerability Categorization, a decision through a tree of questions. NVD's `ssvcV203` metric records the answers chosen, as one-key objects such as `exploitation`, `automatable` and `technicalImpact`, with the role of whoever decided.
* [CPE match string](glossary/cpe-match-string.md) - A Common Platform Enumeration (CPE) pattern, with an optional version range, that a vulnerability's configurations use and the match-string API lists with the CPE names it matches. `matchCriteriaId` is its UUID.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/nist_nvd/schema/`, run `just lint`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just test`, and commit the output.
* [Validate an NVD response](playbooks/validate-an-nvd-response.md) - How to validate a file against the schema with `linkml-validate`, naming the kind of response with `-C NvdCveResponse`, `NvdCpeResponse`, `NvdCpeMatchResponse` or `NvdHistoryResponse`.
* [Move the upstream pins](playbooks/move-the-upstream-pins.md) - What to do when the watch reports that a file of NIST's differs: compare it with `upstream/`, move the copy, the pin in `scripts/check_upstream_release.py` and the module's header together, and let `tests/test_upstream.py` say what the schema must follow.
* [Release a version](playbooks/release.md) - How a version is released: changelog entries under `## [Unreleased]`, a releasing commit type, the `v0.0.0` baseline tag before the first release, and `semantic-release.yml`, which tags and publishes on the merge and dispatches the knowledge release.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out with a reason.

# Policies

* [Security policy](policies/security-policy.md) - `SECURITY.md`: report by GitHub's private vulnerability reporting, only the latest release gets fixes, what each workflow may do, what the watch and the feed fetch read, and what is not covered, such as NVD's data and a flaw in a product NVD lists.
* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: a person owns every contribution, an element says what NVD says, a mapping is read at its source and never guessed, descriptions are one's own words, and the scheduled librarian's changes need a person's review.
* [License and attribution](policies/license-and-attribution.md) - The code is under Apache-2.0 and the bundle under CC BY 4.0. NOTICE carries NVD's notice that it does not endorse or certify this product, NIST's statement on its works, FIRST's position on the CVSS schemas, and why the SSVC file's descriptions are not copied.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to `main` and every pull request, its `test` job lints, tests and checks the adapt copy across Python 3.10 to 3.14, and its `nvd-feed` job validates NVD's live modified feed.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint and docs workflow, `.github/workflows/lint-and-docs.yaml`: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell, on a push to `main`, every pull request and Mondays at 06:00 UTC.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its `nvd-schemas` job runs `scripts/check_upstream_release.py` against NIST's files, and on a finding, or a check that could not run, opens or updates an issue.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: `plan` previews a pull request's release, and `release`, on a push to `main` in the `release` Environment, promotes the changelog, tags, publishes and dispatches the knowledge release.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: on a published release once `KNOWLEDGE_RELEASE_ENABLED` is `true`, or when dispatched, it attaches the schema copy, the bundle zip and the Copilot skill zip, each with its `.sha256` and an attestation.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate of the sidecar. It validates the bundle and its conventions, and checks that each new `human:` confirmation is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC, once `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`, it runs the ktl-librarian skill with no write token and opens a pull request a person reviews.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC it copies the sidecar files from KTL's newest release when the skills pin is behind, and opens one pull request.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: it builds the site on a change to its inputs and on Mondays at 05:23 UTC, and its `deploy` job publishes to GitHub Pages from `main` once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
