# Real NVD responses

Each file here is one answer of the NVD API 2.0, read on 2026-11-03 and unchanged. The default tests validate each against the class of its kind.

- `cve-<CVE identifier>.json` comes from `cves/2.0?cveId=`. Each is the smallest record of the modified feed, the known-exploited records and eight pages of the API's results that shows one case: each `vulnStatus`, each CVSS version, SSVC, the CISA fields, vendor comments, each evaluator field, each CVE tag, a nested configuration, a version range, status changes, a source routine, a platform, a package address, a CPE list and a `git://` repository address that RFC 3986 refuses.
- `cpe-<UUID>.json` comes from `cpes/2.0?cpeNameId=`: a deprecated name, one that replaces another, one with references, and one with titles in two languages.
- `cpematch-<UUID>.json` comes from `cpematch/2.0?matchCriteriaId=`: a range with matches, an inactive string and a string with no matches.
- `history-<CVE identifier>.json` comes from `cvehistory/2.0?cveId=`.

This product uses data from the NVD API but is not endorsed or certified by the NVD. [NOTICE](../../../NOTICE) gives NIST's statement on its data.
