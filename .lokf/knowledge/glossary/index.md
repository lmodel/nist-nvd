# Glossary

* [National Vulnerability Database (NVD)](nvd.md) - The National Vulnerability Database, which NIST runs. It republishes each CVE record with its own analysis: a status, scores, weaknesses and the product configurations that have the vulnerability.
* [vulnStatus](vuln-status.md) - A record's place in NVD's own analysis. NIST's schema says only that it is a string; the schema's enum holds the seven values of the real data: Analyzed, Deferred, Awaiting Analysis, Modified, Received, Undergoing Analysis and Rejected.
* [SSVC](ssvc.md) - Stakeholder-Specific Vulnerability Categorization, a decision through a tree of questions. NVD's `ssvcV203` metric records the answers chosen, as one-key objects such as `exploitation`, `automatable` and `technicalImpact`, with the role of whoever decided.
* [CPE match string](cpe-match-string.md) - A Common Platform Enumeration (CPE) pattern, with an optional version range, that a vulnerability's configurations use and the match-string API lists with the CPE names it matches. `matchCriteriaId` is its UUID.
