---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/vocabulary-terms
title: Mapping terms read at their sources
description: "`tests/vocabulary-terms.txt`, the IRI of every term outside lmodel that the schema's mappings name, each read at its source on 2026-11-03: Dublin Core, schema.org, DCAT, PROV-O, SPDX 3.0.1, the SEPSES vocabularies and Wikidata."
genre: reference
resource: tests/vocabulary-terms.txt
relatedTo:
  - https://w3id.org/lmodel/nist-nvd/knowledge/explanations/crosswalk-and-mappings
sources:
  - id: terms
    resource: tests/vocabulary-terms.txt
    title: the header
  - id: mappings
    resource: tests/test_mappings.py
    title: test_mapping_names_a_term_that_exists
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Mapping terms read at their sources

`tests/vocabulary-terms.txt` lists the IRI of each term outside lmodel that a mapping names. Its header names the file each was read from on 2026-11-03.[^terms]

`tests/test_mappings.py` holds every such mapping to this list, and fails when a listed term is no longer used.[^mappings]

[^terms]: tests/vocabulary-terms.txt, the header
[^mappings]: tests/test_mappings.py, test_mapping_names_a_term_that_exists
