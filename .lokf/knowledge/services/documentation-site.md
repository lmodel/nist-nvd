---
type: Service
id: https://w3id.org/lmodel/nist-nvd/knowledge/services/documentation-site
title: Documentation site
description: "The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-nvd/`: the README as its home page, the docs, the schema's pages and the bundle, with redirects for the retired mkdocs addresses."
genre: reference
resource: website
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/knowledge-website
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: site-config
    resource: website/site.config.mjs
    title: REPO, SITE, BASE, DOCS and REDIRECTS
  - resource: website
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Documentation site

`website/` is an Astro Starlight site, and `website/site.config.mjs` names the repository, its address and what it shows. Its home page is the README. It shows the docs under `docs/`, the schema's pages that `just gen-doc` writes, and the bundle.[^site-config]

`REDIRECTS` keeps the addresses of the retired mkdocs site. An old element page goes to its successor, where one exists, and otherwise to the schema's index.[^site-config]

[^site-config]: website/site.config.mjs, REPO, SITE, BASE, DOCS and REDIRECTS
