export type VulnerabilityCveId = string;
export type NVDEntryCveId = string;
export type CVSSScoreNoteNoteId = string;
export type StatusTransitionTransitionId = string;
/**
* Lifecycle state of a vulnerability record.
*/
export enum VulnerabilityStatus {
    
    /** Vulnerability is actively maintained and published. */
    ACTIVE = "ACTIVE",
    /** CVE ID was rejected and should not be used. */
    REJECTED = "REJECTED",
    /** The vulnerability details are disputed by a party. */
    DISPUTED = "DISPUTED",
    /** CVE ID is reserved but details are not yet published. */
    RESERVED = "RESERVED",
    /** Entry has been superseded or withdrawn. */
    DEPRECATED = "DEPRECATED",
};
/**
* CVSS qualitative severity rating.
*/
export enum ImpactSeverity {
    
    /** No measurable impact. */
    NONE = "NONE",
    /** Limited impact; exploitation requires specific conditions. */
    LOW = "LOW",
    /** Moderate impact; partial compromise of security properties. */
    MEDIUM = "MEDIUM",
    /** High impact; significant compromise of security properties. */
    HIGH = "HIGH",
    /** Critical impact; complete compromise; remote exploitation likely. */
    CRITICAL = "CRITICAL",
    /** Severity has not been assessed or is unavailable. */
    UNKNOWN = "UNKNOWN",
};
/**
* Supported CVSS versions displayed in NVD metrics tabs.
*/
export enum CVSSVersion {
    
    V2_0 = "V2_0",
    V3_0 = "V3_0",
    V3_1 = "V3_1",
    V4_0 = "V4_0",
};
/**
* NVD analysis tags attached to vulnerability records.
*/
export enum NVDTag {
    
    ANALYSIS_PENDING = "ANALYSIS_PENDING",
    ADDITIONAL_INFORMATION = "ADDITIONAL_INFORMATION",
};
/**
* Provider of CVSS vectors and scores.
*/
export enum ScoreSource {
    
    NVD = "NVD",
    CNA = "CNA",
    ADP = "ADP",
    VENDOR = "VENDOR",
    THIRD_PARTY = "THIRD_PARTY",
};
/**
* Resource tag labels used by NVD references.
*/
export enum ReferenceTag {
    
    THIRD_PARTY_ADVISORY = "THIRD_PARTY_ADVISORY",
    VENDOR_ADVISORY = "VENDOR_ADVISORY",
    ISSUE_TRACKING = "ISSUE_TRACKING",
    PATCH = "PATCH",
    TECHNICAL_DESCRIPTION = "TECHNICAL_DESCRIPTION",
    PRESS_MEDIA_COVERAGE = "PRESS_MEDIA_COVERAGE",
    VDB_ENTRY = "VDB_ENTRY",
};
/**
* NVD configuration rendering category.
*/
export enum ConfigurationType {
    
    BASIC = "BASIC",
    RUNNING_ON_WITH = "RUNNING_ON_WITH",
    ADVANCED = "ADVANCED",
};
/**
* Enrichment state labels shown by NVD for CVEs.
*/
export enum NVDWorkflowStatus {
    
    AWAITING_ENRICHMENT = "AWAITING_ENRICHMENT",
    UNDERGOING_ENRICHMENT = "UNDERGOING_ENRICHMENT",
    ENRICHED = "ENRICHED",
    MODIFIED_AFTER_ENRICHMENT = "MODIFIED_AFTER_ENRICHMENT",
    NOT_SCHEDULED = "NOT_SCHEDULED",
    REJECTED = "REJECTED",
};
/**
* Source of state transition decisions in the status flow.
*/
export enum NVDWorkflowEventSource {
    
    NVD_PROCESS = "NVD_PROCESS",
    NVD_STAFF_DECISION = "NVD_STAFF_DECISION",
    CVE_PROGRAM_PROCESS = "CVE_PROGRAM_PROCESS",
    USER_REQUEST = "USER_REQUEST",
};
/**
* Boundary type for version-range constraints.
*/
export enum VersionBoundType {
    
    START_INCLUDING = "START_INCLUDING",
    START_EXCLUDING = "START_EXCLUDING",
    END_INCLUDING = "END_INCLUDING",
    END_EXCLUDING = "END_EXCLUDING",
};


/**
 * Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
 */
export interface Vulnerability {
    /** The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN. */
    cve_id: string,
    /** Short human-readable title or name for this entity. */
    title?: string,
    /** Narrative description of the vulnerability. */
    description: string,
    /** Date and time the vulnerability was first published. */
    published_date?: string,
    /** Date and time the vulnerability record was last modified. */
    last_modified_date?: string,
    /** Products affected by this vulnerability. */
    products?: Product[],
    /** Weakness classifications (e.g. CWE) associated with this vulnerability. */
    weaknesses?: Weakness[],
    /** External references such as advisories and articles. */
    references?: Reference[],
    /** Impact and severity assessment for this vulnerability. */
    impact?: Impact,
    /** Current lifecycle state of the vulnerability record. */
    status?: string,
}


/**
 * Software or hardware entity affected by the vulnerability.
 */
export interface Product {
    /** Name of the vendor or organization responsible for the product. */
    vendor?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Version string of the affected product. */
    version?: string,
    /** Platforms or operating environments affected. */
    platforms?: string[],
}


/**
 * External reference such as an advisory or article.
 */
export interface Reference {
    /** URL pointing to the reference resource. */
    url?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Source or origin of the reference or data. */
    source?: string,
}


/**
 * Weakness classification from CWE or a similar taxonomy.
 */
export interface Weakness {
    /** CWE identifier for the weakness classification (e.g. CWE-79). */
    cwe_id?: string,
    /** Name of the entity (product, weakness, reference, etc.). */
    name?: string,
    /** Narrative description of the vulnerability. */
    description?: string,
}


/**
 * Assessment of the vulnerability's impact and severity.
 */
export interface Impact {
    /** Qualitative severity rating. */
    severity?: string,
    /** CVSS vector string or equivalent scoring vector expression. */
    vector?: string,
    /** Numeric vulnerability score (e.g. CVSS base score). */
    score?: number,
}


/**
 * Logical grouping of CPE match expressions.
 */
export interface Configuration {
    /** CPE 2.2 URI identifying an affected product configuration. */
    cpe_uri?: string,
    /** Logical operator (AND/OR) used in configuration node groupings. */
    operator?: string,
}


/**
 * Enriched NVD representation of a CVE entry.
 */
export interface NVDEntry extends Vulnerability {
    /** Source attribution shown beneath Current Description. */
    description_source?: string,
    /** Description available at enrichment time and shown under Analysis Description. */
    analysis_description?: string,
    /** Grouped CVSS displays and notes for this entry. */
    metrics?: MetricSet,
    /** Affected software configuration statements. */
    configurations?: CPEConfiguration[],
    /** External references such as advisories and articles. */
    references?: NVDReference[],
    /** Weakness classifications (e.g. CWE) associated with this vulnerability. */
    weaknesses?: NVDWeakness[],
    /** Vendor comments associated with the vulnerability record. */
    vendor_comments?: VendorComment[],
    /** NVD analysis tag values. */
    nvd_tags?: string,
    /** CVE tags passed through the CVE List and rendered by NVD. */
    cve_tags?: string[],
    /** Current NVD workflow status for the CVE. */
    workflow_status?: string,
    /** Timeline of status transitions in NVD workflow. */
    status_transitions?: StatusTransitionTransitionId[],
    /** KEV banner details when this CVE is listed by CISA. */
    known_exploited?: KnownExploitedVulnerability,
    /** CWE view used for weakness mapping, typically CWE-1003. */
    cwe_view?: string,
    /** Date/time when NVD received the CVE record for processing. */
    date_received?: string,
}


/**
 * Container for all metric views across CVSS versions.
 */
export interface MetricSet {
    /** CVSS v4.0 metrics. */
    cvss_v4_metrics?: CVSSMetric[],
    /** CVSS v3.x metrics. */
    cvss_v3_metrics?: CVSSMetric[],
    /** CVSS v2.0 metrics. */
    cvss_v2_metrics?: CVSSMetric[],
    /** Notes about CVSS display behavior and data provenance. */
    score_notes?: CVSSScoreNote[],
}


/**
 * Individual CVSS vector and score attribution.
 */
export interface CVSSMetric {
    /** Version string of the affected product. */
    version?: string,
    /** Serialized CVSS vector string. */
    vector_string?: string,
    base_score?: number,
    base_severity?: string,
    /** Source or origin of the reference or data. */
    source?: string,
    /** Display label for score source, such as NIST NVD or CNA Example. */
    provider_label?: string,
    /** Supplemental rationale or caveat for a CVSS score. */
    scoring_justification?: string,
}


/**
 * Additional explanatory note for CVSS display conditions.
 */
export interface CVSSScoreNote {
    note_id: string,
    /** Human-readable explanatory note text. */
    message?: string,
    /** Source or origin of the reference or data. */
    source?: string,
    created?: string,
}


/**
 * Logical grouping of CPE match criteria for affected software.
 */
export interface CPEConfiguration {
    /** Display identifier, for example Configuration 1. */
    configuration_id?: string,
    /** Simplified configuration rendering type. */
    configuration_type?: string,
    /** Logical operator (AND/OR) used in configuration node groupings. */
    operator?: string,
    /** Child configuration nodes. */
    children?: CPEConfiguration[],
    /** Match criteria for this configuration node. */
    matches?: CPEMatch[],
    /** Human-oriented explanation of configuration logic. */
    summary?: string,
}


/**
 * Leaf-level CPE match criterion and optional version bounds.
 */
export interface CPEMatch {
    /** Identifier for a match criterion. */
    match_criteria_id?: string,
    /** CPE 2.3 match criterion expression. */
    criteria?: string,
    /** Concrete CPE 2.3 URI. */
    cpe23_uri?: string,
    /** Whether the criterion indicates a vulnerable product context. */
    vulnerable?: boolean,
    /** Inclusive lower version bound. */
    version_start_including?: string,
    /** Exclusive lower version bound. */
    version_start_excluding?: string,
    /** Inclusive upper version bound. */
    version_end_including?: string,
    /** Exclusive upper version bound. */
    version_end_excluding?: string,
    /** Expanded list of matching CPE names shown in detail UI. */
    matched_cpe_names?: string[],
}


/**
 * Reference URL with NVD resource tags.
 */
export interface NVDReference extends Reference {
    /** NVD resource categories attached to references. */
    resource_tags?: string,
}


/**
 * Weakness row as presented on the NVD detail page.
 */
export interface NVDWeakness extends Weakness {
    /** Source column value, such as NIST or ASSIGNER. */
    source: string,
}


/**
 * Comment provided by vendor during NVD analysis.
 */
export interface VendorComment {
    /** Name of the vendor or organization responsible for the product. */
    vendor?: string,
    /** Vendor-provided comment text. */
    comment?: string,
    /** Date and time the vulnerability record was last modified. */
    last_modified_date?: string,
}


/**
 * CISA KEV information rendered on the NVD detail page.
 */
export interface KnownExploitedVulnerability {
    date_added?: date,
    due_date?: date,
    required_action?: string,
    kev_reference?: string,
}


/**
 * State transition event in NVD enrichment workflow.
 */
export interface StatusTransition {
    transition_id: string,
    from_status?: string,
    to_status?: string,
    event_source?: string,
    transition_time?: string,
    /** Optional reason for transition. */
    rationale?: string,
}



