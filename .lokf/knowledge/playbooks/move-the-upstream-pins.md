---
type: Playbook
id: https://w3id.org/lmodel/nist-nvd/knowledge/playbooks/move-the-upstream-pins
title: Move the upstream pins
description: "What to do when the watch reports that a file of NIST's differs: compare it with `upstream/`, move the copy, the pin in `scripts/check_upstream_release.py` and the module's header together, and let `tests/test_upstream.py` say what the schema must follow."
genre: how-to
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/upstream-copies
dependsOn:
  - https://w3id.org/lmodel/nist-nvd/knowledge/workflows/upstream-watch
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring and check_file
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the module's docstring
  - id: notice
    resource: NOTICE
    title: NIST's SSVC schema
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Move the upstream pins

When the upstream watch says NIST changed a file:[^watch]

1. Compare the published file with its copy under `upstream/`.
2. Replace the copy, and move its SHA-256 in `PINNED_SHA256` in `scripts/check_upstream_release.py`.
3. Move the module's header: `version`, `source` and the `upstream_sha256` annotation.
4. Run `just test`. `tests/test_upstream.py` says which definition, property or enum value the schema must now follow.[^test_upstream.py]

For the SSVC file, regenerate `upstream/ssvc-v2.0.3.structure.json` with the script's `structure` function, and copy none of its prose.[^notice]

A report that a check could not run says nothing about NIST's files. The script exits 2 for it and 1 for a change.[^watch]

[^watch]: scripts/check_upstream_release.py, the docstring and check_file
[^test_upstream.py]: tests/test_upstream.py, the module's docstring
[^notice]: NOTICE, NIST's SSVC schema
