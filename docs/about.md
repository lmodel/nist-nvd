# About nist-nvd

A [LinkML](https://linkml.io) model of the **NIST National Vulnerability
Database (NVD)** view of a CVE — the *enriched* data NVD layers on top of the
upstream CVE record: CVSS metric tabs, CPE applicability statements, CWE
weakness attributions, reference resource tags, CISA KEV details, and the NVD
enrichment status lifecycle. It models what NVD *adds and renders*, not the raw
CVE record (that is the upstream `cve` schema, to which nist-nvd maps).

- **Schema source:** [src/nist_nvd/schema/nist_nvd.yaml](../src/nist_nvd/schema/nist_nvd.yaml) (IRI `https://w3id.org/lmodel/nist-nvd`)
- **Docs site:** [https://lmodel.github.io/nist-nvd](https://lmodel.github.io/nist-nvd)
- **Upstream:** [NVD data feeds](https://nvd.nist.gov/vuln/data-feeds), [CVE API 2.0 schema](https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema)

## Design

- **Extends a shared core.** Imports `vulnerability-core` and subclasses its
  abstract `Vulnerability`, `Reference`, and `Weakness` rather than restating
  common fields. NVD-specific enrichment lives here.
- **Tracks the detail page.** Class and slot names mirror what an analyst sees
  (Current vs Analysis description, CVSS version tabs, "Configuration 1"
  groupings); `comments:`/`notes:` record NVD display rules.
- **Enums for closed lists.** CVSS versions, resource tags, workflow states,
  transition sources, and version bounds are validated `enum`s.
- **Resolvable identity.** URIs use the project's `nvd:` namespace; upstream
  equivalence is recorded via `*_mappings`.

## Class model

`NVDEntry` (`is_a: Vulnerability`) is the tree root and aggregates the views:

```
NVDEntry
├── metrics            → MetricSet
│     ├── cvss_v{4,3,2}_metrics → CVSSMetric
│     └── score_notes           → CVSSScoreNote
├── configurations     → CPEConfiguration (children: recursive; matches → CPEMatch)
├── references         → NVDReference (is_a Reference, + resource_tags)
├── weaknesses         → NVDWeakness (is_a Weakness, + source)
├── vendor_comments    → VendorComment
├── known_exploited    → KnownExploitedVulnerability (CISA KEV)
└── status_transitions → StatusTransition
```

## Enums

| Enum | Vocabulary |
|---|---|
| `CVSSVersion` | `V2_0`, `V3_0`, `V3_1`, `V4_0` |
| `ScoreSource` | `NVD`, `CNA`, `ADP`, `VENDOR`, `THIRD_PARTY` |
| `ReferenceTag` | `THIRD_PARTY_ADVISORY`, `VENDOR_ADVISORY`, `ISSUE_TRACKING`, `PATCH`, … |
| `ConfigurationType` | `BASIC`, `RUNNING_ON_WITH`, `ADVANCED` |
| `NVDWorkflowStatus` | `AWAITING_ENRICHMENT` → `UNDERGOING_ENRICHMENT` → `ENRICHED`, `MODIFIED_AFTER_ENRICHMENT`, `NOT_SCHEDULED`, `REJECTED` |
| `NVDWorkflowEventSource` | `NVD_PROCESS`, `NVD_STAFF_DECISION`, `CVE_PROGRAM_PROCESS`, `USER_REQUEST` |
| `VersionBoundType` | `START_INCLUDING`, `START_EXCLUDING`, `END_INCLUDING`, `END_EXCLUDING` |
| `NVDTag` | `ANALYSIS_PENDING`, `ADDITIONAL_INFORMATION` |

Subsets partition fields into views: `nvd_feed`, `metrics`, `detail_page`,
`status_workflow`.

## Mappings to CVE

Correspondence to the upstream `cve` schema is recorded inline via `*_mappings`
(e.g. `CPEMatch` ↔ `cve:CpeMatch`, `NVDWeakness` ↔ `cve:ProblemType`) and as an
SSSOM mapping set, [cve_to_nist_nvd.sssom.tsv](../src/nist_nvd/mappings/cve_to_nist_nvd.sssom.tsv).

## Testing & build

Example-driven tests in [tests/](../tests): `data/valid/` and
`data/classes/valid/` (must load), `data/invalid/` (must be rejected). The
filename stem before the first `-` names the target class.
[tests/test_data.py](../tests/test_data.py) parametrizes over these folders.

Recipes use [just](https://github.com/casey/just/): `just lint`,
`just gen-project`, `just test`. Known issues:

- `_test-examples` RDF dump fails with `Unknown CURIE prefix: @base` when
  minting an IRI from a plain-string identifier (`NVDEntry`'s `cve_id`). Pass a
  base via the runner's `--prefixes` flag (`"@base": https://w3id.org/lmodel/nist-nvd/`).
- Imported abstract base classes can cause example field mismatches
