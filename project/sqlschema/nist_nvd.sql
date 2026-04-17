-- # Class: NVDEntry Description: Enriched NVD representation of a CVE entry.
--     * Slot: description_source Description: Source attribution shown beneath Current Description.
--     * Slot: analysis_description Description: Description available at enrichment time and shown under Analysis Description.
--     * Slot: workflow_status Description: Current NVD workflow status for the CVE.
--     * Slot: cwe_view Description: CWE view used for weakness mapping, typically CWE-1003.
--     * Slot: date_received Description: Date/time when NVD received the CVE record for processing.
--     * Slot: cve_id Description: The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.
--     * Slot: title Description: Short human-readable title or name for this entity.
--     * Slot: description Description: Current Description shown on the NVD detail page.
--     * Slot: published_date Description: Date and time the vulnerability was first published.
--     * Slot: last_modified_date Description: Date and time the vulnerability record was last modified.
--     * Slot: status Description: Current lifecycle state of the vulnerability record.
--     * Slot: metrics_id Description: Grouped CVSS displays and notes for this entry.
--     * Slot: known_exploited_id Description: KEV banner details when this CVE is listed by CISA.
--     * Slot: impact_id Description: Impact and severity assessment for this vulnerability.
-- # Class: MetricSet Description: Container for all metric views across CVSS versions.
--     * Slot: id
-- # Class: CVSSMetric Description: Individual CVSS vector and score attribution.
--     * Slot: id
--     * Slot: version Description: Version string of the affected product.
--     * Slot: vector_string Description: Serialized CVSS vector string.
--     * Slot: base_score
--     * Slot: base_severity
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: provider_label Description: Display label for score source, such as NIST NVD or CNA Example.
--     * Slot: scoring_justification Description: Supplemental rationale or caveat for a CVSS score.
--     * Slot: MetricSet_id Description: Autocreated FK slot
-- # Class: CVSSScoreNote Description: Additional explanatory note for CVSS display conditions.
--     * Slot: note_id
--     * Slot: message Description: Human-readable explanatory note text.
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: created
--     * Slot: MetricSet_id Description: Autocreated FK slot
-- # Class: CPEConfiguration Description: Logical grouping of CPE match criteria for affected software.
--     * Slot: id
--     * Slot: configuration_id Description: Display identifier, for example Configuration 1.
--     * Slot: configuration_type Description: Simplified configuration rendering type.
--     * Slot: operator Description: Logical operator (AND/OR) used in configuration node groupings.
--     * Slot: summary Description: Human-oriented explanation of configuration logic.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
--     * Slot: CPEConfiguration_id Description: Autocreated FK slot
-- # Class: CPEMatch Description: Leaf-level CPE match criterion and optional version bounds.
--     * Slot: id
--     * Slot: match_criteria_id Description: Identifier for a match criterion.
--     * Slot: criteria Description: CPE 2.3 match criterion expression.
--     * Slot: cpe23_uri Description: Concrete CPE 2.3 URI.
--     * Slot: vulnerable Description: Whether the criterion indicates a vulnerable product context.
--     * Slot: version_start_including Description: Inclusive lower version bound.
--     * Slot: version_start_excluding Description: Exclusive lower version bound.
--     * Slot: version_end_including Description: Inclusive upper version bound.
--     * Slot: version_end_excluding Description: Exclusive upper version bound.
--     * Slot: CPEConfiguration_id Description: Autocreated FK slot
-- # Class: NVDReference Description: Reference URL with NVD resource tags.
--     * Slot: id
--     * Slot: url Description: URL pointing to the reference resource.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
-- # Class: NVDWeakness Description: Weakness row as presented on the NVD detail page.
--     * Slot: id
--     * Slot: source Description: Source column value, such as NIST or ASSIGNER.
--     * Slot: cwe_id Description: CWE identifier for the weakness classification (e.g. CWE-79).
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: description Description: Narrative description of the vulnerability.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
-- # Class: VendorComment Description: Comment provided by vendor during NVD analysis.
--     * Slot: id
--     * Slot: vendor Description: Name of the vendor or organization responsible for the product.
--     * Slot: comment Description: Vendor-provided comment text.
--     * Slot: last_modified_date Description: Date and time the vulnerability record was last modified.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
-- # Class: KnownExploitedVulnerability Description: CISA KEV information rendered on the NVD detail page.
--     * Slot: id
--     * Slot: date_added
--     * Slot: due_date
--     * Slot: required_action
--     * Slot: kev_reference
-- # Class: StatusTransition Description: State transition event in NVD enrichment workflow.
--     * Slot: transition_id
--     * Slot: from_status
--     * Slot: to_status
--     * Slot: event_source
--     * Slot: transition_time
--     * Slot: rationale Description: Optional reason for transition.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
-- # Abstract Class: Vulnerability Description: Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
--     * Slot: cve_id Description: The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.
--     * Slot: title Description: Short human-readable title or name for this entity.
--     * Slot: description Description: Narrative description of the vulnerability.
--     * Slot: published_date Description: Date and time the vulnerability was first published.
--     * Slot: last_modified_date Description: Date and time the vulnerability record was last modified.
--     * Slot: status Description: Current lifecycle state of the vulnerability record.
--     * Slot: impact_id Description: Impact and severity assessment for this vulnerability.
-- # Class: Product Description: Software or hardware entity affected by the vulnerability.
--     * Slot: id
--     * Slot: vendor Description: Name of the vendor or organization responsible for the product.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: version Description: Version string of the affected product.
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Reference Description: External reference such as an advisory or article.
--     * Slot: id
--     * Slot: url Description: URL pointing to the reference resource.
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: source Description: Source or origin of the reference or data.
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Weakness Description: Weakness classification from CWE or a similar taxonomy.
--     * Slot: id
--     * Slot: cwe_id Description: CWE identifier for the weakness classification (e.g. CWE-79).
--     * Slot: name Description: Name of the entity (product, weakness, reference, etc.).
--     * Slot: description Description: Narrative description of the vulnerability.
--     * Slot: Vulnerability_cve_id Description: Autocreated FK slot
-- # Class: Impact Description: Assessment of the vulnerability's impact and severity.
--     * Slot: id
--     * Slot: severity Description: Qualitative severity rating.
--     * Slot: vector Description: CVSS vector string or equivalent scoring vector expression.
--     * Slot: score Description: Numeric vulnerability score (e.g. CVSS base score).
-- # Class: Configuration Description: Logical grouping of CPE match expressions.
--     * Slot: id
--     * Slot: cpe_uri Description: CPE 2.2 URI identifying an affected product configuration.
--     * Slot: operator Description: Logical operator (AND/OR) used in configuration node groupings.
-- # Class: NVDEntry_nvd_tags
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
--     * Slot: nvd_tags Description: NVD analysis tag values.
-- # Class: NVDEntry_cve_tags
--     * Slot: NVDEntry_cve_id Description: Autocreated FK slot
--     * Slot: cve_tags Description: CVE tags passed through the CVE List and rendered by NVD.
-- # Class: CPEMatch_matched_cpe_names
--     * Slot: CPEMatch_id Description: Autocreated FK slot
--     * Slot: matched_cpe_names Description: Expanded list of matching CPE names shown in detail UI.
-- # Class: NVDReference_resource_tags
--     * Slot: NVDReference_id Description: Autocreated FK slot
--     * Slot: resource_tags Description: NVD resource categories attached to references.
-- # Class: Product_platforms
--     * Slot: Product_id Description: Autocreated FK slot
--     * Slot: platforms Description: Platforms or operating environments affected.

CREATE TABLE "MetricSet" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_MetricSet_id" ON "MetricSet" (id);

CREATE TABLE "KnownExploitedVulnerability" (
	id INTEGER NOT NULL,
	date_added DATE,
	due_date DATE,
	required_action TEXT,
	kev_reference TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_KnownExploitedVulnerability_id" ON "KnownExploitedVulnerability" (id);

CREATE TABLE "Impact" (
	id INTEGER NOT NULL,
	severity VARCHAR(8),
	vector TEXT,
	score FLOAT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Impact_id" ON "Impact" (id);

CREATE TABLE "Configuration" (
	id INTEGER NOT NULL,
	cpe_uri TEXT,
	operator TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Configuration_id" ON "Configuration" (id);

CREATE TABLE "NVDEntry" (
	description_source TEXT,
	analysis_description TEXT,
	workflow_status VARCHAR(25),
	cwe_view TEXT,
	date_received DATETIME,
	cve_id TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	published_date DATETIME,
	last_modified_date DATETIME,
	status VARCHAR(25),
	metrics_id INTEGER,
	known_exploited_id INTEGER,
	impact_id INTEGER,
	PRIMARY KEY (cve_id),
	FOREIGN KEY(metrics_id) REFERENCES "MetricSet" (id),
	FOREIGN KEY(known_exploited_id) REFERENCES "KnownExploitedVulnerability" (id),
	FOREIGN KEY(impact_id) REFERENCES "Impact" (id)
);
CREATE INDEX "ix_NVDEntry_cve_id" ON "NVDEntry" (cve_id);

CREATE TABLE "CVSSMetric" (
	id INTEGER NOT NULL,
	version TEXT,
	vector_string TEXT,
	base_score FLOAT,
	base_severity VARCHAR(8),
	source VARCHAR(11),
	provider_label TEXT,
	scoring_justification TEXT,
	"MetricSet_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("MetricSet_id") REFERENCES "MetricSet" (id)
);
CREATE INDEX "ix_CVSSMetric_id" ON "CVSSMetric" (id);

CREATE TABLE "CVSSScoreNote" (
	note_id TEXT NOT NULL,
	message TEXT,
	source TEXT,
	created DATETIME,
	"MetricSet_id" INTEGER,
	PRIMARY KEY (note_id),
	FOREIGN KEY("MetricSet_id") REFERENCES "MetricSet" (id)
);
CREATE INDEX "ix_CVSSScoreNote_note_id" ON "CVSSScoreNote" (note_id);

CREATE TABLE "Vulnerability" (
	cve_id TEXT NOT NULL,
	title TEXT,
	description TEXT NOT NULL,
	published_date DATETIME,
	last_modified_date DATETIME,
	status VARCHAR(10),
	impact_id INTEGER,
	PRIMARY KEY (cve_id),
	FOREIGN KEY(impact_id) REFERENCES "Impact" (id)
);
CREATE INDEX "ix_Vulnerability_cve_id" ON "Vulnerability" (cve_id);

CREATE TABLE "CPEConfiguration" (
	id INTEGER NOT NULL,
	configuration_id TEXT,
	configuration_type VARCHAR(15),
	operator TEXT,
	summary TEXT,
	"NVDEntry_cve_id" TEXT,
	"CPEConfiguration_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id),
	FOREIGN KEY("CPEConfiguration_id") REFERENCES "CPEConfiguration" (id)
);
CREATE INDEX "ix_CPEConfiguration_id" ON "CPEConfiguration" (id);

CREATE TABLE "NVDReference" (
	id INTEGER NOT NULL,
	url TEXT NOT NULL,
	name TEXT,
	source TEXT,
	"NVDEntry_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_NVDReference_id" ON "NVDReference" (id);

CREATE TABLE "NVDWeakness" (
	id INTEGER NOT NULL,
	source TEXT NOT NULL,
	cwe_id TEXT NOT NULL,
	name TEXT NOT NULL,
	description TEXT,
	"NVDEntry_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_NVDWeakness_id" ON "NVDWeakness" (id);

CREATE TABLE "VendorComment" (
	id INTEGER NOT NULL,
	vendor TEXT,
	comment TEXT,
	last_modified_date DATETIME,
	"NVDEntry_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_VendorComment_id" ON "VendorComment" (id);

CREATE TABLE "StatusTransition" (
	transition_id TEXT NOT NULL,
	from_status VARCHAR(25),
	to_status VARCHAR(25),
	event_source VARCHAR(19),
	transition_time DATETIME,
	rationale TEXT,
	"NVDEntry_cve_id" TEXT,
	PRIMARY KEY (transition_id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_StatusTransition_transition_id" ON "StatusTransition" (transition_id);

CREATE TABLE "Product" (
	id INTEGER NOT NULL,
	vendor TEXT,
	name TEXT,
	version TEXT,
	"NVDEntry_cve_id" TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Product_id" ON "Product" (id);

CREATE TABLE "Reference" (
	id INTEGER NOT NULL,
	url TEXT,
	name TEXT,
	source TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Reference_id" ON "Reference" (id);

CREATE TABLE "Weakness" (
	id INTEGER NOT NULL,
	cwe_id TEXT,
	name TEXT,
	description TEXT,
	"Vulnerability_cve_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Vulnerability_cve_id") REFERENCES "Vulnerability" (cve_id)
);
CREATE INDEX "ix_Weakness_id" ON "Weakness" (id);

CREATE TABLE "NVDEntry_nvd_tags" (
	"NVDEntry_cve_id" TEXT,
	nvd_tags VARCHAR(22),
	PRIMARY KEY ("NVDEntry_cve_id", nvd_tags),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_NVDEntry_nvd_tags_nvd_tags" ON "NVDEntry_nvd_tags" (nvd_tags);
CREATE INDEX "ix_NVDEntry_nvd_tags_NVDEntry_cve_id" ON "NVDEntry_nvd_tags" ("NVDEntry_cve_id");

CREATE TABLE "NVDEntry_cve_tags" (
	"NVDEntry_cve_id" TEXT,
	cve_tags TEXT,
	PRIMARY KEY ("NVDEntry_cve_id", cve_tags),
	FOREIGN KEY("NVDEntry_cve_id") REFERENCES "NVDEntry" (cve_id)
);
CREATE INDEX "ix_NVDEntry_cve_tags_NVDEntry_cve_id" ON "NVDEntry_cve_tags" ("NVDEntry_cve_id");
CREATE INDEX "ix_NVDEntry_cve_tags_cve_tags" ON "NVDEntry_cve_tags" (cve_tags);

CREATE TABLE "CPEMatch" (
	id INTEGER NOT NULL,
	match_criteria_id TEXT,
	criteria TEXT,
	cpe23_uri TEXT,
	vulnerable BOOLEAN,
	version_start_including TEXT,
	version_start_excluding TEXT,
	version_end_including TEXT,
	version_end_excluding TEXT,
	"CPEConfiguration_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("CPEConfiguration_id") REFERENCES "CPEConfiguration" (id)
);
CREATE INDEX "ix_CPEMatch_id" ON "CPEMatch" (id);

CREATE TABLE "NVDReference_resource_tags" (
	"NVDReference_id" INTEGER,
	resource_tags VARCHAR(21),
	PRIMARY KEY ("NVDReference_id", resource_tags),
	FOREIGN KEY("NVDReference_id") REFERENCES "NVDReference" (id)
);
CREATE INDEX "ix_NVDReference_resource_tags_NVDReference_id" ON "NVDReference_resource_tags" ("NVDReference_id");
CREATE INDEX "ix_NVDReference_resource_tags_resource_tags" ON "NVDReference_resource_tags" (resource_tags);

CREATE TABLE "Product_platforms" (
	"Product_id" INTEGER,
	platforms TEXT,
	PRIMARY KEY ("Product_id", platforms),
	FOREIGN KEY("Product_id") REFERENCES "Product" (id)
);
CREATE INDEX "ix_Product_platforms_Product_id" ON "Product_platforms" ("Product_id");
CREATE INDEX "ix_Product_platforms_platforms" ON "Product_platforms" (platforms);

CREATE TABLE "CPEMatch_matched_cpe_names" (
	"CPEMatch_id" INTEGER,
	matched_cpe_names TEXT,
	PRIMARY KEY ("CPEMatch_id", matched_cpe_names),
	FOREIGN KEY("CPEMatch_id") REFERENCES "CPEMatch" (id)
);
CREATE INDEX "ix_CPEMatch_matched_cpe_names_CPEMatch_id" ON "CPEMatch_matched_cpe_names" ("CPEMatch_id");
CREATE INDEX "ix_CPEMatch_matched_cpe_names_matched_cpe_names" ON "CPEMatch_matched_cpe_names" (matched_cpe_names);
