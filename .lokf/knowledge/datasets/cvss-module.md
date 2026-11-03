---
type: Dataset
id: https://w3id.org/lmodel/nist-nvd/knowledge/datasets/cvss-module
title: Vendored CVSS module
description: lmodel/cve's `cve_cvss` module, copied unchanged to `src/nist_nvd/schema/cve/` and held to its git object hash by `tests/test_cve_import.py`, which also walks NVD's own CVSS files against it. Its classes are `CvssV20`, `CvssV30`, `CvssV31` and `CvssV40`.
genre: reference
resource: src/nist_nvd/schema/cve/cve_cvss.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-nvd/knowledge/datasets/nist-nvd-linkml-schema
references:
  - https://w3id.org/lmodel/nist-nvd/knowledge/references/first-cvss-schemas
sources:
  - id: test_cve_import.py
    resource: tests/test_cve_import.py
    title: the pins and KNOWN_MISSING_KEYS
  - id: contributing
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - resource: src/nist_nvd/schema/cve
generated:
  by: process:ktl-librarian
  at: "2026-11-03T22:34:15Z"
status: draft
---

# Vendored CVSS module

`src/nist_nvd/schema/cve/cve_cvss.yaml` is lmodel/cve's module, copied unchanged. `nvd_cve` imports it, and NVD's wrapper classes, such as `NvdCvssMetricV31`, range their `cvssData` over its classes.[^test_cve_import.py]

`tests/test_cve_import.py` holds the file to the git object hash it pins, and names the commit of lmodel/cve it came from. lmodel/cve has no release yet, so the commit is on its `feat/first-release` branch.[^test_cve_import.py]

The same test walks NVD's copies of the CVSS schemas against the module, and fails on a key or a value NVD has that the module lacks. It lists what NVD's CVSS 4.0 file allows and the module refuses: the keys `threatScore`, `threatSeverity`, `environmentalScore` and `environmentalSeverity`, and the value `NEGLIGIBLE` of the three modified impacts on connected systems. The CVE Program's copy differs there, and no record read on 2026-11-03 holds any of them.[^test_cve_import.py]

The file is lmodel/cve's. A change to it goes there, and this repository then copies it from a release.[^contributing]

[^test_cve_import.py]: tests/test_cve_import.py, the pins and KNOWN_MISSING_KEYS
[^contributing]: CONTRIBUTING.md, Before opening a pull request
