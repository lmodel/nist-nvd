# NIST's JSON schemas

This folder holds the JSON schemas of the National Vulnerability Database (NVD) API 2.0, as NIST publishes them at <https://csrc.nist.gov/schema/nvd/api/2.0/>, read on 2026-11-03. Every file is unchanged but one.

| File | What it defines | Edition its title names |
| --- | --- | --- |
| `cve_api_json_2.0.schema` | The vulnerability response and its items | 2.2.4 |
| `cpe_api_json_2.0.schema` | The product response | 2.0 |
| `cpematch_api_json_2.0.schema` | The match-string response | 2.0 |
| `cve_history_api_json_2.0.schema` | The change-history response | 2.0.1 |
| `cve_affected_1.0.json` | An affected product, which the vulnerability response references | 1.0, in its address |
| `ssvc-v2.0.3.structure.json` | The structure of `ssvc-v2.0.3.json`, which the vulnerability response references | 2.0.3, in its address |
| `external/cvss-v*.json` | NIST's copies of FIRST's CVSS schemas | 2.0, 3.0, 3.1 and 4.0 |

`ssvc-v2.0.3.structure.json` is NIST's file with every description, title and example removed. [NOTICE](../NOTICE) says why.

NIST's files have no release and no git object. `scripts/check_upstream_release.py` pins each file's SHA-256, and `upstream-watch.yaml` reports each week when one differs. `tests/test_upstream.py` walks these files and holds the schema to them.
