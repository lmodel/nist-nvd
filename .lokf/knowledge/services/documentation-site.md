---
type: Service
id: https://w3id.org/lmodel/nist-nvd/knowledge/services/documentation-site
title: Documentation site
description: "The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-nvd/`: the README as its home page, the docs, the schema's pages and the bundle, with redirects for the retired mkdocs addresses."
genre: reference
resource: website
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/knowledge-website
derivedFrom:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: site-config
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: the table of what the site shows
  - resource: website
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:08:43Z"
status: draft
---

# Documentation site

`website/` is a Hugo site, and `website/site.toml` names the repository, its address and what it shows. Its home page is the README. It shows the docs under `docs/`, the schema's pages and the bundle.[^site-config] The build writes the schema's pages with LinkML's `gen-doc`.[^website-readme.md]

The redirects in `website/site.toml` keep the addresses of the retired mkdocs site. An old element page goes to its successor, where one exists, and otherwise to the schema's index.[^site-config]

[^site-config]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the table of what the site shows
