-- # Class: NvdResponseMixin Description: The fields of a page of results, which every NVD API response carries.
--     * Slot: id
--     * Slot: format Description: The name NVD gives this kind of response.
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: resultsPerPage Description: How many results this page holds.
--     * Slot: startIndex Description: The position of this page's first result among all the results.
--     * Slot: totalResults Description: How many results the request matched in all.
--     * Slot: version Description: The version of the response format.
-- # Class: CvssSeverityBandsMixin Description: The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
--     * Slot: id
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV20 Description: A score under CVSS version 2.0, which has no severity bands.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: accessVector Description: How far away an attacker can be when using the flaw, in CVSS 2.0's terms.
--     * Slot: accessComplexity Description: How hard the flaw is to use once the attacker can reach it.
--     * Slot: authentication Description: How many times an attacker must log in before using the flaw.
--     * Slot: exploitability Description: How far working attack code has come, in CVSS 2.0's terms.
--     * Slot: collateralDamagePotential Description: How much loss a successful attack could cause beyond the system itself.
--     * Slot: targetDistribution Description: How much of the scorer's environment is exposed to the flaw.
-- # Class: CvssV30 Description: A score under CVSS version 3.0.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: scope Description: Whether an attack can reach beyond the component that holds the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: exploitCodeMaturity Description: How far working attack code has come.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: temporalSeverity Description: The rating in words for the temporal score.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: modifiedScope Description: The scope as the scorer's own environment changes it.
--     * Slot: modifiedConfidentialityImpact Description: The confidentiality impact as the scorer's own environment changes it.
--     * Slot: modifiedIntegrityImpact Description: The integrity impact as the scorer's own environment changes it.
--     * Slot: modifiedAvailabilityImpact Description: The availability impact as the scorer's own environment changes it.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: environmentalSeverity Description: The rating in words for the environmental score.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV31 Description: A score under CVSS version 3.1.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: scope Description: Whether an attack can reach beyond the component that holds the flaw.
--     * Slot: confidentialityImpact Description: How much information an attack could expose.
--     * Slot: integrityImpact Description: How much an attack could change that should not change.
--     * Slot: availabilityImpact Description: How much an attack could disrupt the service.
--     * Slot: exploitCodeMaturity Description: How far working attack code has come.
--     * Slot: remediationLevel Description: What kind of fix is available.
--     * Slot: reportConfidence Description: How far the flaw's existence and details have been confirmed.
--     * Slot: temporalScore Description: The base score adjusted for what changes over time, such as a fix appearing.
--     * Slot: temporalSeverity Description: The rating in words for the temporal score.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: modifiedScope Description: The scope as the scorer's own environment changes it.
--     * Slot: modifiedConfidentialityImpact Description: The confidentiality impact as the scorer's own environment changes it.
--     * Slot: modifiedIntegrityImpact Description: The integrity impact as the scorer's own environment changes it.
--     * Slot: modifiedAvailabilityImpact Description: The availability impact as the scorer's own environment changes it.
--     * Slot: environmentalScore Description: The score adjusted for the scorer's own environment.
--     * Slot: environmentalSeverity Description: The rating in words for the environmental score.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: CvssV40 Description: A score under CVSS version 4.0.
--     * Slot: id
--     * Slot: version Description: A version string. On a score it is the CVSS version; on a product entry, the product's.
--     * Slot: vectorString Description: The scores' metric values written as one compact string.
--     * Slot: attackVector Description: How far away an attacker can be when using the flaw.
--     * Slot: attackComplexity Description: How much is outside the attacker's control when using the flaw.
--     * Slot: privilegesRequired Description: What level of access an attacker needs before using the flaw.
--     * Slot: userInteraction Description: Whether someone other than the attacker has to take part.
--     * Slot: confidentialityRequirement Description: How much confidentiality matters to the scorer for the affected system.
--     * Slot: integrityRequirement Description: How much integrity matters to the scorer for the affected system.
--     * Slot: availabilityRequirement Description: How much availability matters to the scorer for the affected system.
--     * Slot: modifiedAttackVector Description: The attack vector as the scorer's own environment changes it.
--     * Slot: modifiedAttackComplexity Description: The attack complexity as the scorer's own environment changes it.
--     * Slot: modifiedPrivilegesRequired Description: The privileges needed as the scorer's own environment changes them.
--     * Slot: modifiedUserInteraction Description: The user interaction as the scorer's own environment changes it.
--     * Slot: attackRequirements Description: Whether the attack needs conditions in the target that the attacker does not control.
--     * Slot: vulnConfidentialityImpact Description: How much information in the vulnerable system an attack could expose.
--     * Slot: vulnIntegrityImpact Description: How much an attack could change in the vulnerable system.
--     * Slot: vulnAvailabilityImpact Description: How much an attack could disrupt the vulnerable system.
--     * Slot: subConfidentialityImpact Description: How much information in other, connected systems an attack could expose.
--     * Slot: subIntegrityImpact Description: How much an attack could change in other, connected systems.
--     * Slot: subAvailabilityImpact Description: How much an attack could disrupt other, connected systems.
--     * Slot: exploitMaturity Description: How much is known about attacks on this flaw, in CVSS 4.0's terms.
--     * Slot: modifiedAttackRequirements Description: The attack requirements as the scorer's own environment changes them.
--     * Slot: modifiedVulnConfidentialityImpact Description: The confidentiality impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedVulnIntegrityImpact Description: The integrity impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedVulnAvailabilityImpact Description: The availability impact on the vulnerable system, in the scorer's environment.
--     * Slot: modifiedSubConfidentialityImpact Description: The confidentiality impact on connected systems, in the scorer's environment.
--     * Slot: modifiedSubIntegrityImpact Description: The integrity impact on connected systems, in the scorer's environment.
--     * Slot: modifiedSubAvailabilityImpact Description: The availability impact on connected systems, in the scorer's environment.
--     * Slot: Safety Description: Whether an attack could put people's safety at risk.
--     * Slot: Automatable Description: Whether an attacker could automate every step of an attack across many targets.
--     * Slot: Recovery Description: How the affected system comes back after an attack.
--     * Slot: valueDensity Description: Whether one successful attack gains the attacker a little or a lot of a resource.
--     * Slot: vulnerabilityResponseEffort Description: How much work it takes a consumer to respond to the flaw.
--     * Slot: providerUrgency Description: How urgent the product's supplier says the flaw is, as a colour.
--     * Slot: baseScore Description: The score from 0 to 10 for what is inherent in the flaw.
--     * Slot: baseSeverity Description: The rating in words that the base score falls under.
-- # Class: NvdCveResponse Description: A page of the vulnerability API's results, or a whole data feed.
--     * Slot: id
--     * Slot: format Description: The name NVD gives this kind of response.
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: resultsPerPage Description: How many results this page holds.
--     * Slot: startIndex Description: The position of this page's first result among all the results.
--     * Slot: totalResults Description: How many results the request matched in all.
--     * Slot: version Description: The version of the response format.
-- # Class: NvdVulnerability Description: One entry of a response, which only wraps the vulnerability.
--     * Slot: id
--     * Slot: NvdCveResponse_id Description: Autocreated FK slot
--     * Slot: cve_id Description: The vulnerability.
-- # Class: NvdCve Description: A vulnerability as NVD holds it, under its CVE identifier.
--     * Slot: id Description: The vulnerability's CVE identifier.
--     * Slot: sourceIdentifier Description: The email address or UUID of the organization that supplied this.
--     * Slot: lastModified Description: When NVD last changed this.
--     * Slot: vulnStatus Description: Where this vulnerability stands in NVD's analysis.
--     * Slot: published Description: When NVD published this vulnerability.
--     * Slot: evaluatorComment Description: A remark from NVD's analyst.
--     * Slot: evaluatorSolution Description: A way to resolve the vulnerability, from NVD's analyst.
--     * Slot: evaluatorImpact Description: What the vulnerability can lead to, from NVD's analyst.
--     * Slot: cisaExploitAdd Description: The day CISA added this vulnerability to its Known Exploited Vulnerabilities catalog.
--     * Slot: cisaActionDue Description: The day by which CISA says federal agencies must act.
--     * Slot: cisaRequiredAction Description: What CISA says agencies must do about this vulnerability.
--     * Slot: cisaVulnerabilityName Description: The name CISA gives this vulnerability in its catalog.
--     * Slot: metrics_id Description: The scores that NVD and others give this vulnerability.
-- # Class: NvdCveTag Description: The labels that one source puts on a record.
--     * Slot: id
--     * Slot: sourceIdentifier Description: The email address or UUID of the organization that supplied this.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdLangString Description: A piece of text and the language it is in.
--     * Slot: id
--     * Slot: lang Description: The language of the text beside it, as a language code.
--     * Slot: value Description: The text.
--     * Slot: NvdCve_id Description: Autocreated FK slot
--     * Slot: NvdWeakness_id Description: Autocreated FK slot
-- # Class: NvdReference Description: A page about a vulnerability, with NVD's labels for what it is.
--     * Slot: id
--     * Slot: url Description: The address of the page.
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdMetrics Description: The scores of a vulnerability, in a list per scoring system and version.
--     * Slot: id
-- # Class: NvdCvssMetricV2 Description: A CVSS 2.0 score, who gave it, and NVD's figures beside it.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: exploitabilityScore Description: The CVSS exploitability subscore.
--     * Slot: impactScore Description: The CVSS impact subscore.
--     * Slot: baseSeverity Description: The severity band of the base score, which CVSS 2.0 leaves to NVD.
--     * Slot: acInsufInfo Description: Whether NVD lacked the information to rate the access complexity.
--     * Slot: obtainAllPrivilege Description: Whether exploiting this gains every privilege.
--     * Slot: obtainUserPrivilege Description: Whether exploiting this gains a user's privileges.
--     * Slot: obtainOtherPrivilege Description: Whether exploiting this gains some other privilege.
--     * Slot: userInteractionRequired Description: Whether exploiting this needs a user to act.
--     * Slot: NvdMetrics_id Description: Autocreated FK slot
--     * Slot: cvssData_id Description: The CVSS score itself, in FIRST's form for its version.
-- # Class: NvdCvssMetricV30 Description: A CVSS 3.0 score, who gave it, and its subscores.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: exploitabilityScore Description: The CVSS exploitability subscore.
--     * Slot: impactScore Description: The CVSS impact subscore.
--     * Slot: NvdMetrics_id Description: Autocreated FK slot
--     * Slot: cvssData_id Description: The CVSS score itself, in FIRST's form for its version.
-- # Class: NvdCvssMetricV31 Description: A CVSS 3.1 score, who gave it, and its subscores.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: exploitabilityScore Description: The CVSS exploitability subscore.
--     * Slot: impactScore Description: The CVSS impact subscore.
--     * Slot: NvdMetrics_id Description: Autocreated FK slot
--     * Slot: cvssData_id Description: The CVSS score itself, in FIRST's form for its version.
-- # Class: NvdCvssMetricV40 Description: A CVSS 4.0 score and who gave it.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: NvdMetrics_id Description: Autocreated FK slot
--     * Slot: cvssData_id Description: The CVSS score itself, in FIRST's form for its version.
-- # Class: NvdSsvcMetricV203 Description: A Stakeholder-Specific Vulnerability Categorization (SSVC) decision and who made it.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: NvdMetrics_id Description: Autocreated FK slot
--     * Slot: ssvcData_uid Description: The decision.
-- # Class: NvdSsvcData Description: One SSVC decision, as the answers chosen on the way through a decision tree.
--     * Slot: uid
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: computed Description: The decision in a short form.
--     * Slot: role Description: The role of whoever made the decision, such as CISA Coordinator.
--     * Slot: version Description: The version of SSVC used.
--     * Slot: id Description: The vulnerability the decision is about, by whatever identifier.
--     * Slot: decisionTreeUrl Description: The address of the decision tree that was used.
--     * Slot: generator Description: The tool that wrote this decision.
--     * Slot: decisionTree_id Description: The whole decision tree that was used.
-- # Class: NvdSsvcOption Description: One answer on the way through a decision tree, keyed by its decision point.
--     * Slot: id
--     * Slot: exploitation Description: How far the vulnerability is known to be exploited, such as none, poc or active.
--     * Slot: automatable Description: Whether an attacker could automate the attack, as yes or no.
--     * Slot: technicalImpact Description: How much control an attacker would gain, as partial or total.
--     * Slot: NvdSsvcData_uid Description: Autocreated FK slot
-- # Class: NvdSsvcDecisionTree Description: A whole SSVC decision tree, in the form of the schema NVD's file names.
--     * Slot: id
-- # Class: NvdAffected Description: The products that one source says the vulnerability affects.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdAffectedProduct Description: A product and which of its versions have the vulnerability.
--     * Slot: id
--     * Slot: defaultStatus Description: The status of any version the versions list does not name.
--     * Slot: vendor Description: Who makes or maintains the product.
--     * Slot: product Description: The product's name.
--     * Slot: collectionURL Description: The address of the package collection that holds the product.
--     * Slot: packageName Description: The package's name within that collection.
--     * Slot: repo Description: The address of the product's source code repository.
--     * Slot: packageURL Description: The product's Package URL, with no version in it.
--     * Slot: NvdAffected_id Description: Autocreated FK slot
-- # Class: NvdProgramRoutine Description: One affected source code routine.
--     * Slot: id
--     * Slot: name Description: The name of the source code routine.
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
-- # Class: NvdAffectedVersion Description: The status of one version of a product, or of a range of its versions.
--     * Slot: id
--     * Slot: version Description: The version, or the start of the range.
--     * Slot: status Description: The state of this thing, from the list its class names.
--     * Slot: versionType Description: The numbering scheme that orders the versions, such as semver or git.
--     * Slot: lessThan Description: The first version after the range.
--     * Slot: lessThanOrEqual Description: The last version in the range.
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
-- # Class: NvdVersionChange Description: A point within a range of versions where the status changes.
--     * Slot: id
--     * Slot: at Description: The version at which the status changes.
--     * Slot: status Description: The state of this thing, from the list its class names.
--     * Slot: NvdAffectedVersion_id Description: Autocreated FK slot
-- # Class: NvdWeakness Description: The weaknesses that one source says lie behind a vulnerability.
--     * Slot: id
--     * Slot: source Description: The email address or UUID of the organization that supplied this.
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdConfiguration Description: A statement of which product configurations have the vulnerability.
--     * Slot: id
--     * Slot: operator Description: How the parts of this configuration combine.
--     * Slot: negate Description: Whether the result of the configuration is reversed.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdConfigurationNode Description: One part of a configuration statement, as a set of CPE matches.
--     * Slot: id
--     * Slot: operator Description: How the parts of this configuration combine.
--     * Slot: negate Description: Whether the result of the configuration is reversed.
--     * Slot: NvdConfiguration_id Description: Autocreated FK slot
-- # Class: NvdCpeMatch Description: A CPE match string or range, and whether what it matches is vulnerable.
--     * Slot: id
--     * Slot: criteria Description: A CPE match string, which may hold wildcards.
--     * Slot: matchCriteriaId Description: The UUID that NVD gives a CPE match string.
--     * Slot: versionStartExcluding Description: The version above which the match starts, itself left out.
--     * Slot: versionStartIncluding Description: The first version the match covers.
--     * Slot: versionEndExcluding Description: The version below which the match ends, itself left out.
--     * Slot: versionEndIncluding Description: The last version the match covers.
--     * Slot: vulnerable Description: Whether what this matches has the vulnerability, rather than only setting the scene.
--     * Slot: NvdConfigurationNode_id Description: Autocreated FK slot
-- # Class: NvdVendorComment Description: What a product's vendor has said about a vulnerability.
--     * Slot: id
--     * Slot: lastModified Description: When NVD last changed this.
--     * Slot: organization Description: The vendor's name.
--     * Slot: comment Description: What the vendor said.
--     * Slot: NvdCve_id Description: Autocreated FK slot
-- # Class: NvdCpeResponse Description: A page of the product API's results.
--     * Slot: id
--     * Slot: format Description: The name NVD gives this kind of response.
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: resultsPerPage Description: How many results this page holds.
--     * Slot: startIndex Description: The position of this page's first result among all the results.
--     * Slot: totalResults Description: How many results the request matched in all.
--     * Slot: version Description: The version of the response format.
-- # Class: NvdCpeItem Description: One entry of a product response, which only wraps the CPE name.
--     * Slot: id
--     * Slot: NvdCpeResponse_id Description: Autocreated FK slot
--     * Slot: cpe_cpeNameId Description: The CPE name and what NVD holds about it.
-- # Class: NvdCpe Description: A CPE name as NVD holds it, with its UUID.
--     * Slot: cpeName Description: A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.
--     * Slot: cpeNameId Description: The UUID that NVD gives a CPE name.
--     * Slot: created Description: When NVD first recorded this.
--     * Slot: lastModified Description: When NVD last changed this.
--     * Slot: deprecated Description: Whether NVD has retired this CPE name.
-- # Class: NvdCpeTitle Description: A product's title in one language.
--     * Slot: id
--     * Slot: title Description: The human-readable title.
--     * Slot: lang Description: The language of the text beside it, as a language code.
--     * Slot: NvdCpe_cpeNameId Description: Autocreated FK slot
-- # Class: NvdCpeReference Description: A page about a product, and what kind of page it is.
--     * Slot: id
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: ref Description: The page's address.
--     * Slot: NvdCpe_cpeNameId Description: Autocreated FK slot
-- # Class: NvdCpeNameLink Description: A pointer from one CPE name to another.
--     * Slot: id
--     * Slot: cpeName Description: A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.
--     * Slot: cpeNameId Description: The UUID that NVD gives a CPE name.
--     * Slot: NvdCpe_cpeNameId Description: Autocreated FK slot
-- # Class: NvdCpeMatchResponse Description: A page of the match-string API's results.
--     * Slot: id
--     * Slot: format Description: The name NVD gives this kind of response.
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: resultsPerPage Description: How many results this page holds.
--     * Slot: startIndex Description: The position of this page's first result among all the results.
--     * Slot: totalResults Description: How many results the request matched in all.
--     * Slot: version Description: The version of the response format.
-- # Class: NvdMatchStringItem Description: One entry of a match-string response, which only wraps the match string.
--     * Slot: id
--     * Slot: NvdCpeMatchResponse_id Description: Autocreated FK slot
--     * Slot: matchString_matchCriteriaId Description: The match string and what NVD holds about it.
-- # Class: NvdMatchString Description: A CPE match string or range as NVD holds it, and the CPE names it matches.
--     * Slot: criteria Description: A CPE match string, which may hold wildcards.
--     * Slot: matchCriteriaId Description: The UUID that NVD gives a CPE match string.
--     * Slot: versionStartExcluding Description: The version above which the match starts, itself left out.
--     * Slot: versionStartIncluding Description: The first version the match covers.
--     * Slot: versionEndExcluding Description: The version below which the match ends, itself left out.
--     * Slot: versionEndIncluding Description: The last version the match covers.
--     * Slot: created Description: When NVD first recorded this.
--     * Slot: lastModified Description: When NVD last changed this.
--     * Slot: status Description: The state of this thing, from the list its class names.
--     * Slot: cpeLastModified Description: When NVD last changed the list of CPE names this matches.
-- # Class: NvdMatchedCpe Description: A CPE name that a match string matches.
--     * Slot: id
--     * Slot: cpeName Description: A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.
--     * Slot: cpeNameId Description: The UUID that NVD gives a CPE name.
--     * Slot: NvdMatchString_matchCriteriaId Description: Autocreated FK slot
-- # Class: NvdHistoryResponse Description: A page of the change-history API's results.
--     * Slot: id
--     * Slot: format Description: The name NVD gives this kind of response.
--     * Slot: timestamp Description: When NVD produced this response or this decision.
--     * Slot: resultsPerPage Description: How many results this page holds.
--     * Slot: startIndex Description: The position of this page's first result among all the results.
--     * Slot: totalResults Description: How many results the request matched in all.
--     * Slot: version Description: The version of the response format.
-- # Class: NvdChangeItem Description: One entry of a change-history response, which only wraps the change.
--     * Slot: id
--     * Slot: NvdHistoryResponse_id Description: Autocreated FK slot
--     * Slot: change_cveChangeId Description: The change.
-- # Class: NvdChange Description: One change to a vulnerability's record at NVD.
--     * Slot: cveChangeId Description: The UUID that NVD gives this change.
--     * Slot: sourceIdentifier Description: The email address or UUID of the organization that supplied this.
--     * Slot: created Description: When NVD first recorded this.
--     * Slot: cveId Description: The vulnerability the change is to.
--     * Slot: eventName Description: The kind of event, such as Initial Analysis or CVE Modified.
-- # Class: NvdChangeDetail Description: One part of a change, naming what kind of data changed and how.
--     * Slot: id
--     * Slot: type Description: The kind of this thing, from the list its class names.
--     * Slot: action Description: How the data changed, such as Added.
--     * Slot: oldValue Description: The value before the change.
--     * Slot: newValue Description: The value after the change.
--     * Slot: NvdChange_cveChangeId Description: Autocreated FK slot
-- # Class: NvdChangeObject Description: A value before or after a change that is an object, with any keys.
--     * Slot: id
-- # Class: NvdCveTag_tags
--     * Slot: NvdCveTag_id Description: Autocreated FK slot
--     * Slot: tags Description: Labels on this thing, from the list its class names.
-- # Class: NvdReference_tags
--     * Slot: NvdReference_id Description: Autocreated FK slot
--     * Slot: tags Description: Labels on this thing, from the list its class names.
-- # Class: NvdAffectedProduct_cpes
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
--     * Slot: cpes Description: The product's CPE names, in the 2.2 or the 2.3 form.
-- # Class: NvdAffectedProduct_modules
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
--     * Slot: modules Description: The affected parts of the product.
-- # Class: NvdAffectedProduct_programFiles
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
--     * Slot: programFiles Description: The affected source code files.
-- # Class: NvdAffectedProduct_platforms
--     * Slot: NvdAffectedProduct_id Description: Autocreated FK slot
--     * Slot: platforms Description: The platforms the vulnerability is limited to.

CREATE TABLE "NvdResponseMixin" (
	id INTEGER NOT NULL,
	format TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	"resultsPerPage" INTEGER NOT NULL,
	"startIndex" INTEGER NOT NULL,
	"totalResults" INTEGER NOT NULL,
	version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdResponseMixin_id" ON "NvdResponseMixin" (id);

CREATE TABLE "CvssSeverityBandsMixin" (
	id INTEGER NOT NULL,
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssSeverityBandsMixin_id" ON "CvssSeverityBandsMixin" (id);

CREATE TABLE "CvssV20" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"baseScore" FLOAT NOT NULL,
	"confidentialityImpact" VARCHAR(8),
	"integrityImpact" VARCHAR(8),
	"availabilityImpact" VARCHAR(8),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(14),
	"temporalScore" FLOAT,
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"environmentalScore" FLOAT,
	"accessVector" VARCHAR(16),
	"accessComplexity" VARCHAR(6),
	authentication VARCHAR(8),
	exploitability VARCHAR(16),
	"collateralDamagePotential" VARCHAR(11),
	"targetDistribution" VARCHAR(11),
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV20_id" ON "CvssV20" (id);

CREATE TABLE "CvssV30" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(16),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(8),
	scope VARCHAR(9),
	"confidentialityImpact" VARCHAR(4),
	"integrityImpact" VARCHAR(4),
	"availabilityImpact" VARCHAR(4),
	"exploitCodeMaturity" VARCHAR(16),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(11),
	"temporalScore" FLOAT,
	"temporalSeverity" VARCHAR(8),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(16),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"modifiedScope" VARCHAR(11),
	"modifiedConfidentialityImpact" VARCHAR(11),
	"modifiedIntegrityImpact" VARCHAR(11),
	"modifiedAvailabilityImpact" VARCHAR(11),
	"environmentalScore" FLOAT,
	"environmentalSeverity" VARCHAR(8),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV30_id" ON "CvssV30" (id);

CREATE TABLE "CvssV31" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(16),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(8),
	scope VARCHAR(9),
	"confidentialityImpact" VARCHAR(4),
	"integrityImpact" VARCHAR(4),
	"availabilityImpact" VARCHAR(4),
	"exploitCodeMaturity" VARCHAR(16),
	"remediationLevel" VARCHAR(13),
	"reportConfidence" VARCHAR(11),
	"temporalScore" FLOAT,
	"temporalSeverity" VARCHAR(8),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(16),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"modifiedScope" VARCHAR(11),
	"modifiedConfidentialityImpact" VARCHAR(11),
	"modifiedIntegrityImpact" VARCHAR(11),
	"modifiedAvailabilityImpact" VARCHAR(11),
	"environmentalScore" FLOAT,
	"environmentalSeverity" VARCHAR(8),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV31_id" ON "CvssV31" (id);

CREATE TABLE "CvssV40" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	"vectorString" TEXT NOT NULL,
	"attackVector" VARCHAR(8),
	"attackComplexity" VARCHAR(4),
	"privilegesRequired" VARCHAR(4),
	"userInteraction" VARCHAR(7),
	"confidentialityRequirement" VARCHAR(11),
	"integrityRequirement" VARCHAR(11),
	"availabilityRequirement" VARCHAR(11),
	"modifiedAttackVector" VARCHAR(11),
	"modifiedAttackComplexity" VARCHAR(11),
	"modifiedPrivilegesRequired" VARCHAR(11),
	"modifiedUserInteraction" VARCHAR(11),
	"attackRequirements" VARCHAR(7),
	"vulnConfidentialityImpact" VARCHAR(4),
	"vulnIntegrityImpact" VARCHAR(4),
	"vulnAvailabilityImpact" VARCHAR(4),
	"subConfidentialityImpact" VARCHAR(4),
	"subIntegrityImpact" VARCHAR(4),
	"subAvailabilityImpact" VARCHAR(4),
	"exploitMaturity" VARCHAR(16),
	"modifiedAttackRequirements" VARCHAR(11),
	"modifiedVulnConfidentialityImpact" VARCHAR(11),
	"modifiedVulnIntegrityImpact" VARCHAR(11),
	"modifiedVulnAvailabilityImpact" VARCHAR(11),
	"modifiedSubConfidentialityImpact" VARCHAR(11),
	"modifiedSubIntegrityImpact" VARCHAR(11),
	"modifiedSubAvailabilityImpact" VARCHAR(11),
	"Safety" VARCHAR(11),
	"Automatable" VARCHAR(11),
	"Recovery" VARCHAR(13),
	"valueDensity" VARCHAR(12),
	"vulnerabilityResponseEffort" VARCHAR(11),
	"providerUrgency" VARCHAR(11),
	"baseScore" FLOAT NOT NULL,
	"baseSeverity" VARCHAR(8) NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_CvssV40_id" ON "CvssV40" (id);

CREATE TABLE "NvdCveResponse" (
	id INTEGER NOT NULL,
	format TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	"resultsPerPage" INTEGER NOT NULL,
	"startIndex" INTEGER NOT NULL,
	"totalResults" INTEGER NOT NULL,
	version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdCveResponse_id" ON "NvdCveResponse" (id);

CREATE TABLE "NvdMetrics" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdMetrics_id" ON "NvdMetrics" (id);

CREATE TABLE "NvdSsvcDecisionTree" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdSsvcDecisionTree_id" ON "NvdSsvcDecisionTree" (id);

CREATE TABLE "NvdCpeResponse" (
	id INTEGER NOT NULL,
	format TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	"resultsPerPage" INTEGER NOT NULL,
	"startIndex" INTEGER NOT NULL,
	"totalResults" INTEGER NOT NULL,
	version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdCpeResponse_id" ON "NvdCpeResponse" (id);

CREATE TABLE "NvdCpe" (
	"cpeName" TEXT NOT NULL,
	"cpeNameId" TEXT NOT NULL,
	created TEXT NOT NULL,
	"lastModified" TEXT NOT NULL,
	deprecated BOOLEAN NOT NULL,
	PRIMARY KEY ("cpeNameId")
);
CREATE INDEX "ix_NvdCpe_cpeNameId" ON "NvdCpe" ("cpeNameId");

CREATE TABLE "NvdCpeMatchResponse" (
	id INTEGER NOT NULL,
	format TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	"resultsPerPage" INTEGER NOT NULL,
	"startIndex" INTEGER NOT NULL,
	"totalResults" INTEGER NOT NULL,
	version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdCpeMatchResponse_id" ON "NvdCpeMatchResponse" (id);

CREATE TABLE "NvdMatchString" (
	criteria TEXT NOT NULL,
	"matchCriteriaId" TEXT NOT NULL,
	"versionStartExcluding" TEXT,
	"versionStartIncluding" TEXT,
	"versionEndExcluding" TEXT,
	"versionEndIncluding" TEXT,
	created TEXT NOT NULL,
	"lastModified" TEXT NOT NULL,
	status VARCHAR(8) NOT NULL,
	"cpeLastModified" TEXT,
	PRIMARY KEY ("matchCriteriaId")
);
CREATE INDEX "ix_NvdMatchString_matchCriteriaId" ON "NvdMatchString" ("matchCriteriaId");

CREATE TABLE "NvdHistoryResponse" (
	id INTEGER NOT NULL,
	format TEXT NOT NULL,
	timestamp TEXT NOT NULL,
	"resultsPerPage" INTEGER NOT NULL,
	"startIndex" INTEGER NOT NULL,
	"totalResults" INTEGER NOT NULL,
	version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdHistoryResponse_id" ON "NvdHistoryResponse" (id);

CREATE TABLE "NvdChangeObject" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NvdChangeObject_id" ON "NvdChangeObject" (id);

CREATE TABLE "NvdCve" (
	id TEXT NOT NULL,
	"sourceIdentifier" TEXT,
	"lastModified" TEXT NOT NULL,
	"vulnStatus" VARCHAR(19),
	published TEXT NOT NULL,
	"evaluatorComment" TEXT,
	"evaluatorSolution" TEXT,
	"evaluatorImpact" TEXT,
	"cisaExploitAdd" DATE,
	"cisaActionDue" DATE,
	"cisaRequiredAction" TEXT,
	"cisaVulnerabilityName" TEXT,
	metrics_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metrics_id) REFERENCES "NvdMetrics" (id)
);
CREATE INDEX "ix_NvdCve_id" ON "NvdCve" (id);

CREATE TABLE "NvdCvssMetricV2" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	"exploitabilityScore" FLOAT,
	"impactScore" FLOAT,
	"baseSeverity" VARCHAR(6),
	"acInsufInfo" BOOLEAN,
	"obtainAllPrivilege" BOOLEAN,
	"obtainUserPrivilege" BOOLEAN,
	"obtainOtherPrivilege" BOOLEAN,
	"userInteractionRequired" BOOLEAN,
	"NvdMetrics_id" INTEGER,
	"cvssData_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMetrics_id") REFERENCES "NvdMetrics" (id),
	FOREIGN KEY("cvssData_id") REFERENCES "CvssV20" (id)
);
CREATE INDEX "ix_NvdCvssMetricV2_id" ON "NvdCvssMetricV2" (id);

CREATE TABLE "NvdCvssMetricV30" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	"exploitabilityScore" FLOAT,
	"impactScore" FLOAT,
	"NvdMetrics_id" INTEGER,
	"cvssData_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMetrics_id") REFERENCES "NvdMetrics" (id),
	FOREIGN KEY("cvssData_id") REFERENCES "CvssV30" (id)
);
CREATE INDEX "ix_NvdCvssMetricV30_id" ON "NvdCvssMetricV30" (id);

CREATE TABLE "NvdCvssMetricV31" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	"exploitabilityScore" FLOAT,
	"impactScore" FLOAT,
	"NvdMetrics_id" INTEGER,
	"cvssData_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMetrics_id") REFERENCES "NvdMetrics" (id),
	FOREIGN KEY("cvssData_id") REFERENCES "CvssV31" (id)
);
CREATE INDEX "ix_NvdCvssMetricV31_id" ON "NvdCvssMetricV31" (id);

CREATE TABLE "NvdCvssMetricV40" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	"NvdMetrics_id" INTEGER,
	"cvssData_id" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMetrics_id") REFERENCES "NvdMetrics" (id),
	FOREIGN KEY("cvssData_id") REFERENCES "CvssV40" (id)
);
CREATE INDEX "ix_NvdCvssMetricV40_id" ON "NvdCvssMetricV40" (id);

CREATE TABLE "NvdSsvcData" (
	uid INTEGER NOT NULL,
	timestamp TEXT,
	computed TEXT,
	role TEXT NOT NULL,
	version TEXT NOT NULL,
	id TEXT,
	"decisionTreeUrl" TEXT,
	generator TEXT,
	"decisionTree_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("decisionTree_id") REFERENCES "NvdSsvcDecisionTree" (id)
);
CREATE INDEX "ix_NvdSsvcData_uid" ON "NvdSsvcData" (uid);

CREATE TABLE "NvdCpeItem" (
	id INTEGER NOT NULL,
	"NvdCpeResponse_id" INTEGER,
	"cpe_cpeNameId" TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCpeResponse_id") REFERENCES "NvdCpeResponse" (id),
	FOREIGN KEY("cpe_cpeNameId") REFERENCES "NvdCpe" ("cpeNameId")
);
CREATE INDEX "ix_NvdCpeItem_id" ON "NvdCpeItem" (id);

CREATE TABLE "NvdCpeTitle" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	lang TEXT NOT NULL,
	"NvdCpe_cpeNameId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCpe_cpeNameId") REFERENCES "NvdCpe" ("cpeNameId")
);
CREATE INDEX "ix_NvdCpeTitle_id" ON "NvdCpeTitle" (id);

CREATE TABLE "NvdCpeReference" (
	id INTEGER NOT NULL,
	type VARCHAR(10),
	ref TEXT NOT NULL,
	"NvdCpe_cpeNameId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCpe_cpeNameId") REFERENCES "NvdCpe" ("cpeNameId")
);
CREATE INDEX "ix_NvdCpeReference_id" ON "NvdCpeReference" (id);

CREATE TABLE "NvdCpeNameLink" (
	id INTEGER NOT NULL,
	"cpeName" TEXT,
	"cpeNameId" TEXT,
	"NvdCpe_cpeNameId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCpe_cpeNameId") REFERENCES "NvdCpe" ("cpeNameId")
);
CREATE INDEX "ix_NvdCpeNameLink_id" ON "NvdCpeNameLink" (id);

CREATE TABLE "NvdMatchStringItem" (
	id INTEGER NOT NULL,
	"NvdCpeMatchResponse_id" INTEGER,
	"matchString_matchCriteriaId" TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCpeMatchResponse_id") REFERENCES "NvdCpeMatchResponse" (id),
	FOREIGN KEY("matchString_matchCriteriaId") REFERENCES "NvdMatchString" ("matchCriteriaId")
);
CREATE INDEX "ix_NvdMatchStringItem_id" ON "NvdMatchStringItem" (id);

CREATE TABLE "NvdMatchedCpe" (
	id INTEGER NOT NULL,
	"cpeName" TEXT NOT NULL,
	"cpeNameId" TEXT NOT NULL,
	"NvdMatchString_matchCriteriaId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMatchString_matchCriteriaId") REFERENCES "NvdMatchString" ("matchCriteriaId")
);
CREATE INDEX "ix_NvdMatchedCpe_id" ON "NvdMatchedCpe" (id);

CREATE TABLE "NvdVulnerability" (
	id INTEGER NOT NULL,
	"NvdCveResponse_id" INTEGER,
	cve_id TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCveResponse_id") REFERENCES "NvdCveResponse" (id),
	FOREIGN KEY(cve_id) REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdVulnerability_id" ON "NvdVulnerability" (id);

CREATE TABLE "NvdCveTag" (
	id INTEGER NOT NULL,
	"sourceIdentifier" TEXT,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdCveTag_id" ON "NvdCveTag" (id);

CREATE TABLE "NvdReference" (
	id INTEGER NOT NULL,
	url TEXT NOT NULL,
	source TEXT,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdReference_id" ON "NvdReference" (id);

CREATE TABLE "NvdSsvcMetricV203" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	"NvdMetrics_id" INTEGER,
	"ssvcData_uid" INTEGER NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdMetrics_id") REFERENCES "NvdMetrics" (id),
	FOREIGN KEY("ssvcData_uid") REFERENCES "NvdSsvcData" (uid)
);
CREATE INDEX "ix_NvdSsvcMetricV203_id" ON "NvdSsvcMetricV203" (id);

CREATE TABLE "NvdSsvcOption" (
	id INTEGER NOT NULL,
	exploitation TEXT,
	automatable TEXT,
	"technicalImpact" TEXT,
	"NvdSsvcData_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdSsvcData_uid") REFERENCES "NvdSsvcData" (uid)
);
CREATE INDEX "ix_NvdSsvcOption_id" ON "NvdSsvcOption" (id);

CREATE TABLE "NvdAffected" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdAffected_id" ON "NvdAffected" (id);

CREATE TABLE "NvdWeakness" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	type VARCHAR(9) NOT NULL,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdWeakness_id" ON "NvdWeakness" (id);

CREATE TABLE "NvdConfiguration" (
	id INTEGER NOT NULL,
	operator VARCHAR(3),
	negate BOOLEAN,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdConfiguration_id" ON "NvdConfiguration" (id);

CREATE TABLE "NvdVendorComment" (
	id INTEGER NOT NULL,
	"lastModified" TEXT NOT NULL,
	organization TEXT NOT NULL,
	comment TEXT NOT NULL,
	"NvdCve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdVendorComment_id" ON "NvdVendorComment" (id);

CREATE TABLE "NvdChange" (
	"cveChangeId" TEXT NOT NULL,
	"sourceIdentifier" TEXT NOT NULL,
	created TEXT,
	"cveId" TEXT NOT NULL,
	"eventName" TEXT NOT NULL,
	PRIMARY KEY ("cveChangeId"),
	FOREIGN KEY("cveId") REFERENCES "NvdCve" (id)
);
CREATE INDEX "ix_NvdChange_cveChangeId" ON "NvdChange" ("cveChangeId");

CREATE TABLE "NvdLangString" (
	id INTEGER NOT NULL,
	lang TEXT NOT NULL,
	value TEXT NOT NULL,
	"NvdCve_id" TEXT,
	"NvdWeakness_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdCve_id") REFERENCES "NvdCve" (id),
	FOREIGN KEY("NvdWeakness_id") REFERENCES "NvdWeakness" (id)
);
CREATE INDEX "ix_NvdLangString_id" ON "NvdLangString" (id);

CREATE TABLE "NvdAffectedProduct" (
	id INTEGER NOT NULL,
	"defaultStatus" VARCHAR(10),
	vendor TEXT,
	product TEXT,
	"collectionURL" TEXT,
	"packageName" TEXT,
	repo TEXT,
	"packageURL" TEXT,
	"NvdAffected_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdAffected_id") REFERENCES "NvdAffected" (id)
);
CREATE INDEX "ix_NvdAffectedProduct_id" ON "NvdAffectedProduct" (id);

CREATE TABLE "NvdConfigurationNode" (
	id INTEGER NOT NULL,
	operator VARCHAR(3) NOT NULL,
	negate BOOLEAN,
	"NvdConfiguration_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdConfiguration_id") REFERENCES "NvdConfiguration" (id)
);
CREATE INDEX "ix_NvdConfigurationNode_id" ON "NvdConfigurationNode" (id);

CREATE TABLE "NvdChangeItem" (
	id INTEGER NOT NULL,
	"NvdHistoryResponse_id" INTEGER,
	"change_cveChangeId" TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdHistoryResponse_id") REFERENCES "NvdHistoryResponse" (id),
	FOREIGN KEY("change_cveChangeId") REFERENCES "NvdChange" ("cveChangeId")
);
CREATE INDEX "ix_NvdChangeItem_id" ON "NvdChangeItem" (id);

CREATE TABLE "NvdChangeDetail" (
	id INTEGER NOT NULL,
	type TEXT NOT NULL,
	action TEXT,
	"oldValue" TEXT,
	"newValue" TEXT,
	"NvdChange_cveChangeId" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdChange_cveChangeId") REFERENCES "NvdChange" ("cveChangeId")
);
CREATE INDEX "ix_NvdChangeDetail_id" ON "NvdChangeDetail" (id);

CREATE TABLE "NvdCveTag_tags" (
	"NvdCveTag_id" INTEGER,
	tags VARCHAR(26),
	PRIMARY KEY ("NvdCveTag_id", tags),
	FOREIGN KEY("NvdCveTag_id") REFERENCES "NvdCveTag" (id)
);
CREATE INDEX "ix_NvdCveTag_tags_tags" ON "NvdCveTag_tags" (tags);
CREATE INDEX "ix_NvdCveTag_tags_NvdCveTag_id" ON "NvdCveTag_tags" ("NvdCveTag_id");

CREATE TABLE "NvdReference_tags" (
	"NvdReference_id" INTEGER,
	tags VARCHAR(22),
	PRIMARY KEY ("NvdReference_id", tags),
	FOREIGN KEY("NvdReference_id") REFERENCES "NvdReference" (id)
);
CREATE INDEX "ix_NvdReference_tags_NvdReference_id" ON "NvdReference_tags" ("NvdReference_id");
CREATE INDEX "ix_NvdReference_tags_tags" ON "NvdReference_tags" (tags);

CREATE TABLE "NvdProgramRoutine" (
	id INTEGER NOT NULL,
	name TEXT NOT NULL,
	"NvdAffectedProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdProgramRoutine_id" ON "NvdProgramRoutine" (id);

CREATE TABLE "NvdAffectedVersion" (
	id INTEGER NOT NULL,
	version TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	"versionType" TEXT,
	"lessThan" TEXT,
	"lessThanOrEqual" TEXT,
	"NvdAffectedProduct_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdAffectedVersion_id" ON "NvdAffectedVersion" (id);

CREATE TABLE "NvdCpeMatch" (
	id INTEGER NOT NULL,
	criteria TEXT NOT NULL,
	"matchCriteriaId" TEXT NOT NULL,
	"versionStartExcluding" TEXT,
	"versionStartIncluding" TEXT,
	"versionEndExcluding" TEXT,
	"versionEndIncluding" TEXT,
	vulnerable BOOLEAN NOT NULL,
	"NvdConfigurationNode_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdConfigurationNode_id") REFERENCES "NvdConfigurationNode" (id)
);
CREATE INDEX "ix_NvdCpeMatch_id" ON "NvdCpeMatch" (id);

CREATE TABLE "NvdAffectedProduct_cpes" (
	"NvdAffectedProduct_id" INTEGER,
	cpes TEXT,
	PRIMARY KEY ("NvdAffectedProduct_id", cpes),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdAffectedProduct_cpes_NvdAffectedProduct_id" ON "NvdAffectedProduct_cpes" ("NvdAffectedProduct_id");
CREATE INDEX "ix_NvdAffectedProduct_cpes_cpes" ON "NvdAffectedProduct_cpes" (cpes);

CREATE TABLE "NvdAffectedProduct_modules" (
	"NvdAffectedProduct_id" INTEGER,
	modules TEXT,
	PRIMARY KEY ("NvdAffectedProduct_id", modules),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdAffectedProduct_modules_modules" ON "NvdAffectedProduct_modules" (modules);
CREATE INDEX "ix_NvdAffectedProduct_modules_NvdAffectedProduct_id" ON "NvdAffectedProduct_modules" ("NvdAffectedProduct_id");

CREATE TABLE "NvdAffectedProduct_programFiles" (
	"NvdAffectedProduct_id" INTEGER,
	"programFiles" TEXT,
	PRIMARY KEY ("NvdAffectedProduct_id", "programFiles"),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdAffectedProduct_programFiles_NvdAffectedProduct_id" ON "NvdAffectedProduct_programFiles" ("NvdAffectedProduct_id");
CREATE INDEX "ix_NvdAffectedProduct_programFiles_programFiles" ON "NvdAffectedProduct_programFiles" ("programFiles");

CREATE TABLE "NvdAffectedProduct_platforms" (
	"NvdAffectedProduct_id" INTEGER,
	platforms TEXT,
	PRIMARY KEY ("NvdAffectedProduct_id", platforms),
	FOREIGN KEY("NvdAffectedProduct_id") REFERENCES "NvdAffectedProduct" (id)
);
CREATE INDEX "ix_NvdAffectedProduct_platforms_NvdAffectedProduct_id" ON "NvdAffectedProduct_platforms" ("NvdAffectedProduct_id");
CREATE INDEX "ix_NvdAffectedProduct_platforms_platforms" ON "NvdAffectedProduct_platforms" (platforms);

CREATE TABLE "NvdVersionChange" (
	id INTEGER NOT NULL,
	at TEXT NOT NULL,
	status VARCHAR(10) NOT NULL,
	"NvdAffectedVersion_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NvdAffectedVersion_id") REFERENCES "NvdAffectedVersion" (id)
);
CREATE INDEX "ix_NvdVersionChange_id" ON "NvdVersionChange" (id);
