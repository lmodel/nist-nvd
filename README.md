<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-nvd

National Vulnerability Database (NVD) API 2.0 (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

This product uses data from the NVD API but is not endorsed or certified by the NVD.

## Documentation Website

[https://lmodel.github.io/nist-nvd](https://lmodel.github.io/nist-nvd)

## What it models

The schema renders the JSON responses of the [NVD API 2.0](https://nvd.nist.gov/developers/start-here), from the [JSON schemas](https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema) that the National Institute of Standards and Technology (NIST) publishes: vulnerabilities at edition 2.2.4, which NVD's data feeds share, products and match strings at 2.0, and change history at 2.0.1. Each CVSS score object comes from the `cve_cvss` module of [lmodel/cve](https://github.com/lmodel/cve).

NVD's keys and values are the schema's, such as `vulnStatus` and `Awaiting Analysis`, so a real response validates unchanged. `just test-nvd-feed` and a CI job validate every record of NVD's live modified feed. `upstream/` copies NIST's JSON schemas, and `tests/test_upstream.py` fails on any part of them with no element here. NIST changes those files in place, so a weekly workflow compares each with its pinned SHA-256 and opens an issue when one differs.

## Mappings

The schema's mappings are the one home for what it crosses to. The hand-kept SSSOM file this repository once held is gone, since its rows named removed elements and rested on language-model matches that no source confirmed. `tests/test_mappings.py` holds each mapping to a prefix the schema binds, and to a term read at its source or in a neighbour's copy under `tests/neighbours/`.

* `id`: `cve:cveId` and `kev_catalog:cveID` in `exact_mappings`, and `dcterms:identifier` in `close_mappings`.
* `cisaExploitAdd`, `cisaActionDue`, `cisaRequiredAction` and `cisaVulnerabilityName`: `kev_catalog:dateAdded`, `dueDate`, `requiredAction` and `vulnerabilityName` in `exact_mappings`. Each equals the catalog's value for all 1,766 entries of the catalog of 2026-11-03.
* `published` and `lastModified`: `cve:datePublished` and `cve:dateUpdated` in `related_mappings`, as they are NVD's own times, and Dublin Core, schema.org and SPDX 3.0.1 `publishedTime` and `modifiedTime` in `close_mappings`.
* `descriptions`, `references`, `weaknesses`, `configurations`, `affected`, `metrics` and `cveTags`: `cve:descriptions`, `references`, `problemTypes`, `cpeApplicability`, `affected`, `metrics` and `tags` in `close_mappings`.
* `NvdCve`: `cve:CveRecord`, `stix:StixVulnerability`, `spdx3:Security/Vulnerability`, `sepses_cve:CVE` and Wikidata `wd:Q631425` in `close_mappings`.
* `NvdAffectedProduct`, `NvdAffectedVersion`, `NvdVersionChange`, `NvdProgramRoutine`, `NvdReference`, `NvdWeakness`, `NvdLangString`, `NvdConfiguration`, `NvdConfigurationNode` and `NvdCpeMatch`: their `cve:` classes in `close_mappings`, and each product key its `cve:` key.
* The CVSS and SSVC wrappers: `sepses_cvss:` metrics in `close_mappings`, and SPDX 3.0.1's assessment relationships in `related_mappings`.
* The four responses and their items: `schema:DataFeed` and `schema:DataFeedItem` in `close_mappings`, and `dcat:Distribution` in `related_mappings` for a vulnerability response.
* `NvdCpe`, `NvdConfiguration` and `NvdReference`: `sepses_cpe:CPE` and the `sepses_cve:` classes in `close_mappings`.
* `NvdChange`: `prov:Activity` in `related_mappings`.
* `deprecatedBy`, `deprecates`, `refs`, `title`, `created` and `lang`: Dublin Core in `close_mappings`, and `NvdVendorComment`: `schema:Comment`.

A reference's `tags` map to nothing: they are NVD's own vocabulary, not the CVE Program's, and a test holds that.

## Not modelled here

* NVD's web pages and its analysis process. The status values come from real data, because NVD's page that defines them refuses an automated client.
* A CVE record, which is lmodel/cve's, and the KEV catalog, which is lmodel/kev-catalog's. Mappings cross to them.
* The `$schema` key of an SSVC decision, and the content of its decision tree. [docs/about.md](docs/about.md) says why, and lists every departure from NIST's files.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch and the feed's fetcher
* [src/nist_nvd/schema/](src/nist_nvd/schema): the LinkML modules, with `nist_nvd.yaml` the umbrella (edit these, but not `cve/`)
* [src/nist_nvd/datamodel/](src/nist_nvd/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data and real responses in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): NIST's JSON schemas
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/nist-nvd.yaml`, is the copy `just lokf-adapt` writes from `src/nist_nvd/schema/nist_nvd.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-nvd.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `NvdCve` on `Concept`, so a concept may name it as its `type`. In Obsidian, add it to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
NvdCve
```

A concept of that type holds the whole record, with its required keys. In the copy, LOKF's `id` replaces the schema's own, and the thirteen keys LOKF also defines, such as `references` and `source`, take a `cve_` prefix with their IRIs kept, so that the CVSS module's `version` matches lmodel/cve's copy. Both copies hold the CVSS classes, so a host imports one or the other, not both. `tests/test_schema_rules.py` lists every shared name and fails on a new one.

## License

The code is under the [Apache License 2.0](LICENSE). The knowledge bundle under `.lokf/knowledge/` is under CC BY 4.0.

NIST's works are not subject to copyright in the United States and may be elsewhere, FIRST holds the CVSS schemas under its own licence, and the descriptions of NIST's SSVC file are not copied here. [NOTICE](NOTICE) gives each position and NVD's terms. This project is not endorsed or certified by NIST or the NVD.
