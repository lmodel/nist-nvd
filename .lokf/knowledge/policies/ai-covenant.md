---
type: Policy
id: https://w3id.org/lmodel/nist-nvd/knowledge/policies/ai-covenant
title: AI covenant
description: "The rules for AI-assisted work here: a person owns every contribution, an element says what NVD says, a mapping is read at its source and never guessed, descriptions are one's own words, and the scheduled librarian's changes need a person's review."
genre: reference
resource: AI_COVENANT.md
about:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/knowledge-librarian
sources:
  - id: covenant
    resource: AI_COVENANT.md
    title: the note specific to this project and Repository-Owned Agent Automation
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that whoever submits a contribution owns it, whatever tools helped. For this repository, it adds three rules:[^covenant]

- An element says what NVD says, and `tests/test_upstream.py` walks NIST's files. An enum that NIST's schema leaves as a string comes from real data, and its comment says so.
- A mapping is read at its source. A term with no sure match stays unmapped.
- Descriptions are your own words, and nothing from the descriptions of NIST's SSVC schema belongs here.

The scheduled librarian commits under a labelled bot identity, opens a pull request, and needs a person's approval. AI co-authorship in commit messages is discouraged.[^covenant]

[^covenant]: AI_COVENANT.md, the note specific to this project and Repository-Owned Agent Automation
