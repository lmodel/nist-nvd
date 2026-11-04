---
type: Explanation
id: https://w3id.org/lmodel/nist-nvd/knowledge/explanations/departures-from-nists-files
title: Where the schema departs from NIST's files
description: "The places where the schema and NIST's JSON schemas part, each with its reason: timestamps with no UTC offset, a repository address RFC 3986 refuses, SSVC's `$schema` and decision tree, closed classes, and the enums the data fixes. `tests/test_upstream.py` lists each."
genre: reference
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/nvd-json-schemas
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
sources:
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: DEPARTURES and OPEN_UPSTREAM_OBJECTS
  - id: about.md
    resource: docs/about.md
    title: Names
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Where the schema departs from NIST's files

`tests/test_upstream.py` walks NIST's files and fails on a definition, property, enum value or required member with no element here, or a different cardinality. It lists each departure with its reason, and fails on one that no longer applies.[^test_upstream.py]

- **Timestamps.** NIST's files say `format: date-time`, which needs a UTC offset. NVD's data writes none, so all 15,762 records of the modified feed of 2026-11-03 break it twice. The `nvd_timestamp` type admits both forms.
- **A repository's address.** NIST's file says `format: uri`, and two records of that feed write `git://git@gitlab.com:gitlab-org/gitlab.git`, which RFC 3986 refuses. `repo` is a string.
- **SSVC's `$schema`.** A slot of that name breaks the generated Python, and no record of the feed holds the key.
- **SSVC's decision tree.** NIST's file refers to a schema at democert.org, which this schema does not render.
- **Closed classes.** NIST leaves some objects open. The classes are closed, so a key NVD adds fails validation and the feed test reports it.

A string in NIST's file becomes an enum where the real data fixes the list: `vulnStatus`, a reference's `tags`, a weakness's `type`, CVSS 2.0's `baseSeverity` and a match string's `status`. Each enum's comment says which data. `eventName` and a change's `type` and `action` stay strings, because too little of 2.4 million changes was read to close them.[^about.md]

[^test_upstream.py]: tests/test_upstream.py, DEPARTURES and OPEN_UPSTREAM_OBJECTS
[^about.md]: docs/about.md, Names
