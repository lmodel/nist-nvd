# Change Log

## 2026-11-06

* **Changed**: `lokf.yaml` and `nist-nvd.yaml` moved into `.lokf/schema/`, where KTL v0.62.0 keeps a sidecar's schema files, and the concepts that name them follow.

## 2026-11-04

* **Changed**: the description names lmodel/cve and lmodel/kev-catalog as released.
* **Changed**: lmodel/cve's and lmodel/kev-catalog's neighbour copies are their v0.1.0 release assets.
* **Changed**: the vendored CVSS module comes from lmodel/cve's release v0.1.0.

## 2026-11-03

* **Prose**: reworded 9 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the playbook says why `linkml-validate` reports a rejected record in a `.json` file.
* **Removal**: the sidecar's example service.
* **Added**: NVD LinkML schema.
* **Added**: Vendored CVSS module.
* **Added**: Generated artefacts.
* **Added**: The adapt copy.
* **Added**: Copies of NIST's JSON schemas.
* **Added**: Example data.
* **Added**: Extract of real NVD responses.
* **Added**: Neighbours' adapt copies.
* **Added**: Mapping terms read at their sources.
* **Added**: The record for CVE-2023-29357.
* **Added**: NIST's NVD API JSON schemas.
* **Added**: The NVD API and data feeds.
* **Added**: FIRST's CVSS schemas.
* **Added**: Where the schema departs from NIST's files.
* **Added**: The crosswalk to CVE and KEV, and other mappings.
* **Added**: What each checker checks.
* **Added**: National Vulnerability Database (NVD).
* **Added**: vulnStatus.
* **Added**: SSVC.
* **Added**: CPE match string.
* **Added**: Regenerate and test.
* **Added**: Validate an NVD response.
* **Added**: Move the upstream pins.
* **Added**: Release a version.
* **Added**: Security policy.
* **Added**: AI covenant.
* **Added**: License and attribution.
* **Added**: Documentation site.
* **Added**: Build and test (main.yaml).
* **Added**: Lint and docs (lint-and-docs.yaml).
* **Added**: Upstream watch (upstream-watch.yaml).
* **Added**: Semantic release (semantic-release.yml).
* **Added**: Knowledge Release (knowledge-release.yaml).
* **Added**: Knowledge Registrar (knowledge-registrar.yaml).
* **Added**: Knowledge Librarian (knowledge-librarian.yaml).
* **Added**: Knowledge sync (knowledge-sync.yaml).
* **Added**: Knowledge website (knowledge-website.yaml).
* **Added**: Knowledge sources map.
* **Initialization**: Scaffolded the LOKF bundle for nist-nvd with placeholder
  services. Real concepts to follow.
