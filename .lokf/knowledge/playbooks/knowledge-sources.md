---
type: Playbook
id: https://w3id.org/lmodel/nist-nvd/knowledge/playbooks/knowledge-sources
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external source this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out with a reason."
genre: reference
resource: .
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/nist_nvd/schema
  - resource: src/nist_nvd/datamodel
  - resource: project.justfile
  - resource: .lokf/nist-nvd.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: NOTICE
  - resource: LICENSE
  - resource: scripts
  - resource: .github/scripts
  - resource: .github/workflows
  - resource: .github/dependabot.yml
  - resource: .github/release
  - resource: justfile
  - resource: .linkml/generators.yaml
  - resource: .linkmllint.yaml
  - resource: project
  - resource: docs/schema
  - resource: tests
  - resource: upstream
  - resource: CONTRIBUTING.md
  - resource: .releaserc.json
  - resource: CHANGELOG.md
  - resource: website
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: config.public.mk
exclusions:
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The knowledge sync's pull request form, a copy from the sidecar.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: docs/elements
    reason: "A placeholder: gen-doc writes the pages and git ignores them."
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/nist_nvd/__init__.py
    reason: Package plumbing.
  - resource: src/nist_nvd/_version.py
    reason: Package plumbing.
  - resource: tests/__init__.py
    reason: Package plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .lokf/README.md
    reason: The sidecar's own guide, a copy from its template.
  - resource: .lokf/.gitattributes
    reason: The sidecar's line-ending settings.
  - resource: .lokf/.gitignore
    reason: The sidecar's ignore list.
  - resource: .lokf/ingest.yaml.sample
    reason: The ingest's example manifest, unused here.
  - resource: .lokf/lokf.yaml
    reason: LOKF's own schema, pinned from the installed package.
  - resource: .lokf/queries.http
    reason: The sidecar's sample queries.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, copies from its templates.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill builder, a copy from its template.
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Knowledge sources map

| Source | Yields | Re-check |
| --- | --- | --- |
| `src/nist_nvd/schema`, `project.justfile`, `.lokf/nist-nvd.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml` | `datasets/nist-nvd-linkml-schema.md`, `datasets/cvss-module.md`, `datasets/adapt-copy.md`, `glossary/vuln-status.md`, `glossary/ssvc.md`, `glossary/cpe-match-string.md` | the schema's headers and classes, and the adapt recipes |
| `upstream`, `scripts` | `references/nvd-json-schemas.md`, `references/first-cvss-schemas.md`, `references/nvd-api.md`, `datasets/upstream-copies.md`, `playbooks/move-the-upstream-pins.md` | the pins, and what the upstream watch reports |
| `tests/data`, `tests` | `datasets/example-data.md`, `datasets/nvd-extract.md`, `datasets/worked-record-cve-2023-29357.md`, `datasets/neighbour-copies.md`, `datasets/vocabulary-terms.md` | the lists at the top of each test |
| `README.md`, `docs/about.md`, `docs/index.md`, `CHANGELOG.md` | `glossary/nvd.md`, `explanations/departures-from-nists-files.md`, `explanations/crosswalk-and-mappings.md`, `explanations/what-each-checker-checks.md`, `playbooks/validate-an-nvd-response.md` | each page's sections |
| `justfile`, `CONTRIBUTING.md`, `.releaserc.json` | `playbooks/regenerate-and-test.md`, `playbooks/release.md` | the recipes and the release rules |
| `project`, `docs/schema`, `src/nist_nvd/datamodel`, `.linkml/generators.yaml`, `config.public.mk` | `datasets/generated-artefacts.md` | the generators' settings |
| `.linkmllint.yaml` | `datasets/nist-nvd-linkml-schema.md` | the naming rule's comment |
| `SECURITY.md`, `AI_COVENANT.md`, `NOTICE`, `LICENSE`, `.github/dependabot.yml`, `.github/release` | `policies/security-policy.md`, `policies/ai-covenant.md`, `policies/license-and-attribution.md` | each file's sections |
| `.github/workflows`, `.github/scripts` | one concept under `workflows/` per workflow | the on key and the jobs |
| `website` | `services/documentation-site.md` | `website/README.md` and `site.config.mjs` |

The modified feed changes about every two hours, and the extract and the enums' comments are dated, so the bundle's numbers follow the dates they name and not NVD's latest data.
