# About nist-nvd

This page is for anyone reading the [LinkML](https://linkml.io) schema's elements: it says how they are named, where they depart from NIST's files and what the model leaves out.

The National Vulnerability Database (NVD) republishes each CVE record with its own analysis: a status, scores, weaknesses and the product configurations that have the vulnerability. Its API has four responses, and each has a JSON schema that NIST publishes. `upstream/` holds them, and the model's modules follow them:

| Module | Renders | Edition |
| --- | --- | --- |
| `nvd_cve` | the vulnerability response, which NVD's data feeds share, with its CVSS wrappers, SSVC decisions and affected products | 2.2.4 |
| `nvd_cpe` | the product response | 2.0 |
| `nvd_cpematch` | the match-string response | 2.0 |
| `nvd_history` | the change-history response | 2.0.1 |
| `nvd_core` | the fields of a page and the keys several responses share | |
| `cve/cve_cvss` | the CVSS score objects, copied unchanged from [lmodel/cve](https://github.com/lmodel/cve) | |

## Names

Slots and permissible values keep NVD's spelling, so data validates unchanged: `sourceIdentifier`, `vulnStatus`, `Awaiting Analysis`. Classes and enums carry the `Nvd` prefix so they can be imported beside other vocabularies, and each class that renders a named definition of NIST's file gives that name as an alias: `NvdCve` is `cve_item`. Every element is in the `nist_nvd:` namespace (`https://w3id.org/lmodel/nist-nvd/`), and the CVSS module's in `cve:`.

A list NIST's file leaves as a plain string is an enum where the data fixes it: `vulnStatus`, a reference's `tags`, a weakness's `type`, CVSS 2.0's `baseSeverity` and a match string's `status`. Each enum's comment says which data. A new value then fails validation, and the feed test reports it. An event's `eventName` and a change's `type` and `action` stay strings, because too little of 2.4 million changes was read to close them.

Descriptions are this project's own words. Those of the permissible values of `NvdVulnStatus` say only what the name and the data show, because the NVD page that defines them refuses an automated client (<https://nvd.nist.gov/vuln/vulnerability-status>, tried on 2026-11-03).

## Where the model departs from NIST's files

`tests/test_upstream.py` lists each departure with its reason. They are:

- **Timestamps.** NIST's files say `format: date-time`, which is RFC 3339 and needs a UTC offset. NVD's data writes none, so a validator that checks the format, as `linkml-validate` does, would refuse every record. The `nvd_timestamp` type admits both forms.
- **A repository's address.** NIST's file says `format: uri`, and some records write `git://git@gitlab.com:gitlab-org/gitlab.git`, which RFC 3986 refuses. `repo` is a string.
- **SSVC's `$schema`.** A slot of that name breaks the generated Python, and no record of the modified feed holds it.
- **SSVC's decision tree.** NIST's file refers to a schema at democert.org, which this model does not render. No record of the modified feed holds a decision tree.
- **Closed classes.** NIST leaves some objects open to other keys. The classes are closed, so a key NVD adds fails validation and the feed test reports it.

## The CVSS module

NVD's copies of FIRST's CVSS schemas have the same property names and required lists as the CVE Program's, and `tests/test_cve_import.py` walks NVD's against the module. NVD's CVSS 4.0 file allows a few things the module refuses, because the CVE Program's copy differs: the keys `threatScore`, `threatSeverity`, `environmentalScore` and `environmentalSeverity`, and the value `NEGLIGIBLE` for a modified impact on connected systems, where the CVE Program writes `NONE`. No record read on 2026-11-03 holds any of them.

## What is left out

The model renders NVD's responses, not NVD's web pages, and it has no class for a CVE record: that is lmodel/cve's, and the mappings cross to it. Its reference tags are NVD's own vocabulary and not the CVE Program's, so the two are not mapped to each other. It says nothing about how NVD scores or analyses a record.
