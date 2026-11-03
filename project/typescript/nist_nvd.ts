export type NvdCveId = string;
export type NvdCpeCpeNameId = string;
export type NvdMatchStringMatchCriteriaId = string;
export type NvdChangeCveChangeId = string;
/**
* A CVSS rating in words.
*/
export enum CvssSeverity {
    
    /** No severity at all, for a score of 0. */
    NONE = "NONE",
    /** The lowest rating above none. */
    LOW = "LOW",
    /** The middle rating. */
    MEDIUM = "MEDIUM",
    /** The rating below critical. */
    HIGH = "HIGH",
    /** The highest rating. */
    CRITICAL = "CRITICAL",
};
/**
* How far away an attacker can be, in CVSS 2.0's terms.
*/
export enum CvssV2AccessVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from the same local network segment. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only with an account on the system or hands on it. */
    LOCAL = "LOCAL",
};
/**
* How hard the flaw is to use, in CVSS 2.0's terms.
*/
export enum CvssV2AccessComplexity {
    
    /** Only under unusual, hard-to-arrange conditions. */
    HIGH = "HIGH",
    /** Under conditions that take some arranging. */
    MEDIUM = "MEDIUM",
    /** With no special conditions. */
    LOW = "LOW",
};
/**
* How many logins an attacker needs, in CVSS 2.0's terms.
*/
export enum CvssV2Authentication {
    
    /** More than one login. */
    MULTIPLE = "MULTIPLE",
    /** One login. */
    SINGLE = "SINGLE",
    /** No login at all. */
    NONE = "NONE",
};
/**
* How much of one security property an attack could cost, in CVSS 2.0's terms.
*/
export enum CvssV2Impact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, and the attacker cannot choose all of it. */
    PARTIAL = "PARTIAL",
    /** All of it is lost. */
    COMPLETE = "COMPLETE",
};
/**
* How far working attack code has come.
*/
export enum CvssExploitCodeMaturity {
    
    /** No attack code is known, or the attack is only theory. */
    UNPROVEN = "UNPROVEN",
    /** A demonstration exists that needs skilled work to use. */
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    /** Working attack code exists for most situations. */
    FUNCTIONAL = "FUNCTIONAL",
    /** Attack code is reliable and widely available, or no code is needed. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* What kind of fix is available.
*/
export enum CvssRemediationLevel {
    
    /** The vendor offers a complete fix. */
    OFFICIAL_FIX = "OFFICIAL_FIX",
    /** The vendor offers a stopgap for now. */
    TEMPORARY_FIX = "TEMPORARY_FIX",
    /** Others offer a way round the flaw that is not from the vendor. */
    WORKAROUND = "WORKAROUND",
    /** No fix exists, or it cannot be applied. */
    UNAVAILABLE = "UNAVAILABLE",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far the flaw has been confirmed, in CVSS 2.0's terms.
*/
export enum CvssV2ReportConfidence {
    
    /** A single report or conflicting reports that nobody has checked. */
    UNCONFIRMED = "UNCONFIRMED",
    /** Several unofficial sources agree, with some doubt remaining. */
    UNCORROBORATED = "UNCORROBORATED",
    /** The vendor accepts it, or a working attack shows it. */
    CONFIRMED = "CONFIRMED",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much loss could follow beyond the system itself.
*/
export enum CvssV2CollateralDamagePotential {
    
    /** No such loss. */
    NONE = "NONE",
    /** Slight loss. */
    LOW = "LOW",
    /** Moderate loss. */
    LOW_MEDIUM = "LOW_MEDIUM",
    /** Significant loss. */
    MEDIUM_HIGH = "MEDIUM_HIGH",
    /** Catastrophic loss. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of the environment the flaw exposes.
*/
export enum CvssV2TargetDistribution {
    
    /** No systems at all, or only in a lab. */
    NONE = "NONE",
    /** Up to about a quarter of systems. */
    LOW = "LOW",
    /** About a quarter to three quarters of systems. */
    MEDIUM = "MEDIUM",
    /** More than about three quarters of systems. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much one security property matters to the scorer.
*/
export enum CvssRequirement {
    
    /** A loss would have limited effect. */
    LOW = "LOW",
    /** A loss would have serious effect. */
    MEDIUM = "MEDIUM",
    /** A loss would have catastrophic effect. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far away an attacker can be, in CVSS 3's terms.
*/
export enum CvssV3AttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from a logically nearby network. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
};
/**
* The attack vector as the scorer's environment changes it, in CVSS 3's terms.
*/
export enum CvssV3ModifiedAttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from a logically nearby network. */
    ADJACENT_NETWORK = "ADJACENT_NETWORK",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much is outside the attacker's control.
*/
export enum CvssAttackComplexity {
    
    /** Success depends on conditions the attacker must overcome or wait for. */
    HIGH = "HIGH",
    /** The attacker can succeed again and again with no special effort. */
    LOW = "LOW",
};
/**
* The attack complexity as the scorer's environment changes it.
*/
export enum CvssModifiedAttackComplexity {
    
    /** Success depends on conditions the attacker must overcome or wait for. */
    HIGH = "HIGH",
    /** The attacker can succeed again and again with no special effort. */
    LOW = "LOW",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* What access an attacker needs beforehand.
*/
export enum CvssPrivilegesRequired {
    
    /** Administrator-level access. */
    HIGH = "HIGH",
    /** Ordinary user access. */
    LOW = "LOW",
    /** No access at all. */
    NONE = "NONE",
};
/**
* The access needed as the scorer's environment changes it.
*/
export enum CvssModifiedPrivilegesRequired {
    
    /** Administrator-level access. */
    HIGH = "HIGH",
    /** Ordinary user access. */
    LOW = "LOW",
    /** No access at all. */
    NONE = "NONE",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether someone else has to take part, in CVSS 3's terms.
*/
export enum CvssV3UserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone other than the attacker has to do something. */
    REQUIRED = "REQUIRED",
};
/**
* The user interaction as the scorer's environment changes it, in CVSS 3's terms.
*/
export enum CvssV3ModifiedUserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone other than the attacker has to do something. */
    REQUIRED = "REQUIRED",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether an attack can reach beyond the flawed component.
*/
export enum CvssV3Scope {
    
    /** The harm stays within the same security authority. */
    UNCHANGED = "UNCHANGED",
    /** The harm can reach something under another security authority. */
    CHANGED = "CHANGED",
};
/**
* The scope as the scorer's environment changes it.
*/
export enum CvssV3ModifiedScope {
    
    /** The harm stays within the same security authority. */
    UNCHANGED = "UNCHANGED",
    /** The harm can reach something under another security authority. */
    CHANGED = "CHANGED",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of one security property an attack could cost.
*/
export enum CvssImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
};
/**
* The impact on one security property as the scorer's environment changes it.
*/
export enum CvssModifiedImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far the flaw has been confirmed, in CVSS 3's terms.
*/
export enum CvssV3ReportConfidence {
    
    /** Reports say something is wrong, but the cause is not clear. */
    UNKNOWN = "UNKNOWN",
    /** Solid details exist, without full confirmation of the cause. */
    REASONABLE = "REASONABLE",
    /** The flaw is shown beyond doubt, or the vendor accepts it. */
    CONFIRMED = "CONFIRMED",
    /** The scorer gave no value, so the metric does not change the score. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How far away an attacker can be, in CVSS 4.0's terms.
*/
export enum CvssV4AttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from something logically or physically nearby. */
    ADJACENT = "ADJACENT",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
};
/**
* The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
*/
export enum CvssV4ModifiedAttackVector {
    
    /** From anywhere that can route to the system. */
    NETWORK = "NETWORK",
    /** Only from something logically or physically nearby. */
    ADJACENT = "ADJACENT",
    /** Only by acting on the system itself, directly or through a user. */
    LOCAL = "LOCAL",
    /** Only by touching the hardware. */
    PHYSICAL = "PHYSICAL",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether the attack needs conditions in the target beyond the attacker's control.
*/
export enum CvssV4AttackRequirements {
    
    /** The attack works whatever the target's state. */
    NONE = "NONE",
    /** The attack works only when the target is in a certain state. */
    PRESENT = "PRESENT",
};
/**
* The attack requirements as the scorer's environment changes them.
*/
export enum CvssV4ModifiedAttackRequirements {
    
    /** The attack works whatever the target's state. */
    NONE = "NONE",
    /** The attack works only when the target is in a certain state. */
    PRESENT = "PRESENT",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether someone else has to take part, in CVSS 4.0's terms.
*/
export enum CvssV4UserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone has to act only in the ordinary course of their work. */
    PASSIVE = "PASSIVE",
    /** Someone has to take a deliberate step. */
    ACTIVE = "ACTIVE",
};
/**
* The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
*/
export enum CvssV4ModifiedUserInteraction {
    
    /** The attack needs nobody else. */
    NONE = "NONE",
    /** Someone has to act only in the ordinary course of their work. */
    PASSIVE = "PASSIVE",
    /** Someone has to take a deliberate step. */
    ACTIVE = "ACTIVE",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.
*/
export enum CvssV4ModifiedSubsequentImpact {
    
    /** Nothing is lost. */
    NONE = "NONE",
    /** Some is lost, with limited consequences. */
    LOW = "LOW",
    /** All of it is lost, or the loss has serious consequences. */
    HIGH = "HIGH",
    /** The loss could injure people. */
    SAFETY = "SAFETY",
    /** The scorer gave no value, so the base metric stands. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much is known about attacks on the flaw.
*/
export enum CvssV4ExploitMaturity {
    
    /** No demonstration or attack has been reported. */
    UNREPORTED = "UNREPORTED",
    /** A demonstration is public, with no reported attack. */
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT",
    /** Attacks have been reported, or tools for them are public. */
    ATTACKED = "ATTACKED",
    /** The scorer gave no value, so the worst case is assumed. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether an attack could put people's safety at risk.
*/
export enum CvssV4Safety {
    
    /** Any harm to people would be slight at most. */
    NEGLIGIBLE = "NEGLIGIBLE",
    /** People could be seriously hurt. */
    PRESENT = "PRESENT",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Whether every step of an attack could be automated across many targets.
*/
export enum CvssV4Automatable {
    
    /** At least one step resists automation. */
    NO = "NO",
    /** Every step can be automated. */
    YES = "YES",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How the affected system comes back after an attack.
*/
export enum CvssV4Recovery {
    
    /** The system recovers by itself. */
    AUTOMATIC = "AUTOMATIC",
    /** Someone has to step in and restore it. */
    USER = "USER",
    /** The system cannot be restored. */
    IRRECOVERABLE = "IRRECOVERABLE",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much of a resource one successful attack gains the attacker.
*/
export enum CvssV4ValueDensity {
    
    /** Each target holds little, so an attacker must take many. */
    DIFFUSE = "DIFFUSE",
    /** A single target holds a lot. */
    CONCENTRATED = "CONCENTRATED",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How much work it takes a consumer to respond to the flaw.
*/
export enum CvssV4ResponseEffort {
    
    /** Little work, such as reading advice or a small configuration change. */
    LOW = "LOW",
    /** Some work, with a noticeable effect on the service. */
    MODERATE = "MODERATE",
    /** Much work, or a long outage. */
    HIGH = "HIGH",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* How urgent the product's supplier says the flaw is, as a colour.
*/
export enum CvssV4ProviderUrgency {
    
    /** The supplier sees little or no urgency. */
    CLEAR = "CLEAR",
    /** The supplier says the flaw can wait for regular work. */
    GREEN = "GREEN",
    /** The supplier says the flaw matters soon. */
    AMBER = "AMBER",
    /** The supplier says the flaw is at the highest urgency. */
    RED = "RED",
    /** The scorer gave no value. */
    NOT_DEFINED = "NOT_DEFINED",
};
/**
* Where a vulnerability stands in NVD's own analysis.
*/
export enum NvdVulnStatus {
    
    /** NVD has finished its analysis of the record. */
    Analyzed = "Analyzed",
    /** NVD has put off analysing the record. */
    Deferred = "Deferred",
    /** NVD has the record and has not begun to analyse it. */
    Awaiting_Analysis = "Awaiting Analysis",
    /** The record has changed since NVD analysed it. */
    Modified = "Modified",
    /** The record has just reached NVD. */
    Received = "Received",
    /** NVD is analysing the record now. */
    Undergoing_Analysis = "Undergoing Analysis",
    /** The CVE identifier has been rejected. */
    Rejected = "Rejected",
};
/**
* A label that a CVE record's source puts on the record.
*/
export enum NvdCveTagName {
    
    /** The product had lost its support when the identifier was assigned. */
    unsupported_when_assigned = "unsupported-when-assigned",
    /** The product exists only as a hosted service. */
    exclusively_hosted_service = "exclusively-hosted-service",
    /** A party disputes that this is a vulnerability. */
    disputed = "disputed",
};
/**
* NVD's label for what a reference is.
*/
export enum NvdReferenceTag {
    
    /** The address no longer leads to the content. */
    Broken_Link = "Broken Link",
    /** The page shows or gives a way to exploit the vulnerability. */
    Exploit = "Exploit",
    /** An entry in a bug or issue tracker. */
    Issue_Tracking = "Issue Tracking",
    /** A message in a mailing list archive. */
    Mailing_List = "Mailing List",
    /** The page says how to reduce the risk without a fix. */
    Mitigation = "Mitigation",
    /** The page does not bear on the vulnerability. */
    Not_Applicable = "Not Applicable",
    /** The page holds or points to a fix. */
    Patch = "Patch",
    /** Reading the page takes an account or some other access. */
    Permissions_Required = "Permissions Required",
    /** A report in the press or other media. */
    PressSOLIDUSMedia_Coverage = "Press/Media Coverage",
    /** A page on a related matter. */
    Related = "Related",
    /** A page about the affected product. */
    Product = "Product",
    /** The notes of a product release. */
    Release_Notes = "Release Notes",
    /** A technical account of the vulnerability. */
    Technical_Description = "Technical Description",
    /** An advisory from someone other than the vendor. */
    Third_Party_Advisory = "Third Party Advisory",
    /** A signature that a detection tool can use. */
    Tool_Signature = "Tool Signature",
    /** The address now leads to something else. */
    URL_Repurposed = "URL Repurposed",
    /** A page from a body of the United States government. */
    US_Government_Resource = "US Government Resource",
    /** An entry in a vulnerability database. */
    VDB_Entry = "VDB Entry",
    /** An advisory from the product's vendor. */
    Vendor_Advisory = "Vendor Advisory",
};
/**
* Whether a score or a weakness comes from the party NVD treats as first.
*/
export enum NvdSourceType {
    
    /** NVD's first source for the record. */
    Primary = "Primary",
    /** Any other source. */
    Secondary = "Secondary",
};
/**
* The severity band NVD gives a CVSS 2.0 base score.
*/
export enum NvdCvssV2Severity {
    
    /** The low band of CVSS 2.0 base scores. */
    LOW = "LOW",
    /** The middle band of CVSS 2.0 base scores. */
    MEDIUM = "MEDIUM",
    /** The high band of CVSS 2.0 base scores. */
    HIGH = "HIGH",
};
/**
* Whether a version of a product has the vulnerability.
*/
export enum NvdVersionStatus {
    
    /** This version has the vulnerability. */
    affected = "affected",
    /** This version does not have the vulnerability. */
    unaffected = "unaffected",
    /** Nobody has said whether this version has the vulnerability. */
    unknown = "unknown",
};
/**
* How the parts of a configuration combine.
*/
export enum NvdOperator {
    
    /** Every part must hold. */
    AND = "AND",
    /** At least one part must hold. */
    OR = "OR",
};
/**
* What a CPE name's reference points to.
*/
export enum NvdCpeReferenceType {
    
    /** A security advisory. */
    Advisory = "Advisory",
    /** A list of the product's changes. */
    Change_Log = "Change Log",
    /** A page about the product. */
    Product = "Product",
    /** A page about the project behind the product. */
    Project = "Project",
    /** A page about the vendor. */
    Vendor = "Vendor",
    /** A page about this version. */
    Version = "Version",
};
/**
* Whether NVD still uses a match string.
*/
export enum NvdMatchStringStatus {
    
    /** NVD uses this match string. */
    Active = "Active",
    /** NVD no longer uses this match string. */
    Inactive = "Inactive",
};


/**
 * The fields of a page of results, which every NVD API response carries.
 */
export interface NvdResponseMixin {
    /** The name NVD gives this kind of response. */
    format: string,
    /** When NVD produced this response or this decision. */
    timestamp: string,
    /** How many results this page holds. */
    resultsPerPage: number,
    /** The position of this page's first result among all the results. */
    startIndex: number,
    /** How many results the request matched in all. */
    totalResults: number,
    /** The version of the response format. */
    version: string,
}


/**
 * The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
 */
export interface CvssSeverityBandsMixin {
    /** The score from 0 to 10 for what is inherent in the flaw. */
    baseScore: number,
    /** The rating in words that the base score falls under. */
    baseSeverity: string,
}


/**
 * A score under CVSS version 2.0, which has no severity bands.
 */
export interface CvssV20 {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** The score from 0 to 10 for what is inherent in the flaw. */
    baseScore: number,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** How far away an attacker can be when using the flaw, in CVSS 2.0's terms. */
    accessVector?: string,
    /** How hard the flaw is to use once the attacker can reach it. */
    accessComplexity?: string,
    /** How many times an attacker must log in before using the flaw. */
    authentication?: string,
    /** How far working attack code has come, in CVSS 2.0's terms. */
    exploitability?: string,
    /** How much loss a successful attack could cause beyond the system itself. */
    collateralDamagePotential?: string,
    /** How much of the scorer's environment is exposed to the flaw. */
    targetDistribution?: string,
}


/**
 * A score under CVSS version 3.0.
 */
export interface CvssV30 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** Whether an attack can reach beyond the component that holds the flaw. */
    scope?: string,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** How far working attack code has come. */
    exploitCodeMaturity?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** The rating in words for the temporal score. */
    temporalSeverity?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** The scope as the scorer's own environment changes it. */
    modifiedScope?: string,
    /** The confidentiality impact as the scorer's own environment changes it. */
    modifiedConfidentialityImpact?: string,
    /** The integrity impact as the scorer's own environment changes it. */
    modifiedIntegrityImpact?: string,
    /** The availability impact as the scorer's own environment changes it. */
    modifiedAvailabilityImpact?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** The rating in words for the environmental score. */
    environmentalSeverity?: string,
}


/**
 * A score under CVSS version 3.1.
 */
export interface CvssV31 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** Whether an attack can reach beyond the component that holds the flaw. */
    scope?: string,
    /** How much information an attack could expose. */
    confidentialityImpact?: string,
    /** How much an attack could change that should not change. */
    integrityImpact?: string,
    /** How much an attack could disrupt the service. */
    availabilityImpact?: string,
    /** How far working attack code has come. */
    exploitCodeMaturity?: string,
    /** What kind of fix is available. */
    remediationLevel?: string,
    /** How far the flaw's existence and details have been confirmed. */
    reportConfidence?: string,
    /** The base score adjusted for what changes over time, such as a fix appearing. */
    temporalScore?: number,
    /** The rating in words for the temporal score. */
    temporalSeverity?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** The scope as the scorer's own environment changes it. */
    modifiedScope?: string,
    /** The confidentiality impact as the scorer's own environment changes it. */
    modifiedConfidentialityImpact?: string,
    /** The integrity impact as the scorer's own environment changes it. */
    modifiedIntegrityImpact?: string,
    /** The availability impact as the scorer's own environment changes it. */
    modifiedAvailabilityImpact?: string,
    /** The score adjusted for the scorer's own environment. */
    environmentalScore?: number,
    /** The rating in words for the environmental score. */
    environmentalSeverity?: string,
}


/**
 * A score under CVSS version 4.0.
 */
export interface CvssV40 extends CvssSeverityBandsMixin {
    /** A version string. On a score it is the CVSS version; on a product entry, the product's. */
    version: string,
    /** The scores' metric values written as one compact string. */
    vectorString: string,
    /** How far away an attacker can be when using the flaw. */
    attackVector?: string,
    /** How much is outside the attacker's control when using the flaw. */
    attackComplexity?: string,
    /** What level of access an attacker needs before using the flaw. */
    privilegesRequired?: string,
    /** Whether someone other than the attacker has to take part. */
    userInteraction?: string,
    /** How much confidentiality matters to the scorer for the affected system. */
    confidentialityRequirement?: string,
    /** How much integrity matters to the scorer for the affected system. */
    integrityRequirement?: string,
    /** How much availability matters to the scorer for the affected system. */
    availabilityRequirement?: string,
    /** The attack vector as the scorer's own environment changes it. */
    modifiedAttackVector?: string,
    /** The attack complexity as the scorer's own environment changes it. */
    modifiedAttackComplexity?: string,
    /** The privileges needed as the scorer's own environment changes them. */
    modifiedPrivilegesRequired?: string,
    /** The user interaction as the scorer's own environment changes it. */
    modifiedUserInteraction?: string,
    /** Whether the attack needs conditions in the target that the attacker does not control. */
    attackRequirements?: string,
    /** How much information in the vulnerable system an attack could expose. */
    vulnConfidentialityImpact?: string,
    /** How much an attack could change in the vulnerable system. */
    vulnIntegrityImpact?: string,
    /** How much an attack could disrupt the vulnerable system. */
    vulnAvailabilityImpact?: string,
    /** How much information in other, connected systems an attack could expose. */
    subConfidentialityImpact?: string,
    /** How much an attack could change in other, connected systems. */
    subIntegrityImpact?: string,
    /** How much an attack could disrupt other, connected systems. */
    subAvailabilityImpact?: string,
    /** How much is known about attacks on this flaw, in CVSS 4.0's terms. */
    exploitMaturity?: string,
    /** The attack requirements as the scorer's own environment changes them. */
    modifiedAttackRequirements?: string,
    /** The confidentiality impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnConfidentialityImpact?: string,
    /** The integrity impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnIntegrityImpact?: string,
    /** The availability impact on the vulnerable system, in the scorer's environment. */
    modifiedVulnAvailabilityImpact?: string,
    /** The confidentiality impact on connected systems, in the scorer's environment. */
    modifiedSubConfidentialityImpact?: string,
    /** The integrity impact on connected systems, in the scorer's environment. */
    modifiedSubIntegrityImpact?: string,
    /** The availability impact on connected systems, in the scorer's environment. */
    modifiedSubAvailabilityImpact?: string,
    /** Whether an attack could put people's safety at risk. */
    Safety?: string,
    /** Whether an attacker could automate every step of an attack across many targets. */
    Automatable?: string,
    /** How the affected system comes back after an attack. */
    Recovery?: string,
    /** Whether one successful attack gains the attacker a little or a lot of a resource. */
    valueDensity?: string,
    /** How much work it takes a consumer to respond to the flaw. */
    vulnerabilityResponseEffort?: string,
    /** How urgent the product's supplier says the flaw is, as a colour. */
    providerUrgency?: string,
}


/**
 * A page of the vulnerability API's results, or a whole data feed.
 */
export interface NvdCveResponse extends NvdResponseMixin {
    /** The vulnerabilities on this page. */
    vulnerabilities: NvdVulnerability[],
}


/**
 * One entry of a response, which only wraps the vulnerability.
 */
export interface NvdVulnerability {
    /** The vulnerability. */
    cve: NvdCve,
}


/**
 * A vulnerability as NVD holds it, under its CVE identifier.
 */
export interface NvdCve {
    /** The vulnerability's CVE identifier. */
    id: string,
    /** The email address or UUID of the organization that supplied this. */
    sourceIdentifier?: string,
    /** When NVD last changed this. */
    lastModified: string,
    /** The pages that NVD lists about this vulnerability. */
    references: NvdReference[],
    /** Where this vulnerability stands in NVD's analysis. */
    vulnStatus?: string,
    /** When NVD published this vulnerability. */
    published: string,
    /** A remark from NVD's analyst. */
    evaluatorComment?: string,
    /** A way to resolve the vulnerability, from NVD's analyst. */
    evaluatorSolution?: string,
    /** What the vulnerability can lead to, from NVD's analyst. */
    evaluatorImpact?: string,
    /** The day CISA added this vulnerability to its Known Exploited Vulnerabilities catalog. */
    cisaExploitAdd?: date,
    /** The day by which CISA says federal agencies must act. */
    cisaActionDue?: date,
    /** What CISA says agencies must do about this vulnerability. */
    cisaRequiredAction?: string,
    /** The name CISA gives this vulnerability in its catalog. */
    cisaVulnerabilityName?: string,
    /** The labels the record's sources put on it. */
    cveTags?: NvdCveTag[],
    /** What the vulnerability is, in one or more languages. */
    descriptions: NvdLangString[],
    /** The scores that NVD and others give this vulnerability. */
    metrics?: NvdMetrics,
    /** The affected products, by the source that names them. */
    affected?: NvdAffected[],
    /** The weaknesses behind the vulnerability, by the source that names them. */
    weaknesses?: NvdWeakness[],
    /** The product configurations that have the vulnerability. */
    configurations?: NvdConfiguration[],
    /** What product vendors have said about this vulnerability. */
    vendorComments?: NvdVendorComment[],
}


/**
 * The labels that one source puts on a record.
 */
export interface NvdCveTag {
    /** The email address or UUID of the organization that supplied this. */
    sourceIdentifier?: string,
    /** Labels on this thing, from the list its class names. */
    tags?: string,
}


/**
 * A piece of text and the language it is in.
 */
export interface NvdLangString {
    /** The language of the text beside it, as a language code. */
    lang: string,
    /** The text. */
    value: string,
}


/**
 * A page about a vulnerability, with NVD's labels for what it is.
 */
export interface NvdReference {
    /** The address of the page. */
    url: string,
    /** The email address or UUID of the organization that supplied this. */
    source?: string,
    /** Labels on this thing, from the list its class names. */
    tags?: string,
}


/**
 * The scores of a vulnerability, in a list per scoring system and version.
 */
export interface NvdMetrics {
    /** The CVSS 4.0 scores. */
    cvssMetricV40?: NvdCvssMetricV40[],
    /** The CVSS 3.1 scores. */
    cvssMetricV31?: NvdCvssMetricV31[],
    /** The CVSS 3.0 scores. */
    cvssMetricV30?: NvdCvssMetricV30[],
    /** The CVSS 2.0 scores. */
    cvssMetricV2?: NvdCvssMetricV2[],
    /** The SSVC 2.0.3 decisions. */
    ssvcV203?: NvdSsvcMetricV203[],
}


/**
 * A CVSS 2.0 score, who gave it, and NVD's figures beside it.
 */
export interface NvdCvssMetricV2 {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** The CVSS score itself, in FIRST's form for its version. */
    cvssData: CvssV20,
    /** The CVSS exploitability subscore. */
    exploitabilityScore?: number,
    /** The CVSS impact subscore. */
    impactScore?: number,
    /** The severity band of the base score, which CVSS 2.0 leaves to NVD. */
    baseSeverity?: string,
    /** Whether NVD lacked the information to rate the access complexity. */
    acInsufInfo?: boolean,
    /** Whether exploiting this gains every privilege. */
    obtainAllPrivilege?: boolean,
    /** Whether exploiting this gains a user's privileges. */
    obtainUserPrivilege?: boolean,
    /** Whether exploiting this gains some other privilege. */
    obtainOtherPrivilege?: boolean,
    /** Whether exploiting this needs a user to act. */
    userInteractionRequired?: boolean,
}


/**
 * A CVSS 3.0 score, who gave it, and its subscores.
 */
export interface NvdCvssMetricV30 {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** The CVSS score itself, in FIRST's form for its version. */
    cvssData: CvssV30,
    /** The CVSS exploitability subscore. */
    exploitabilityScore?: number,
    /** The CVSS impact subscore. */
    impactScore?: number,
}


/**
 * A CVSS 3.1 score, who gave it, and its subscores.
 */
export interface NvdCvssMetricV31 {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** The CVSS score itself, in FIRST's form for its version. */
    cvssData: CvssV31,
    /** The CVSS exploitability subscore. */
    exploitabilityScore?: number,
    /** The CVSS impact subscore. */
    impactScore?: number,
}


/**
 * A CVSS 4.0 score and who gave it.
 */
export interface NvdCvssMetricV40 {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** The CVSS score itself, in FIRST's form for its version. */
    cvssData: CvssV40,
}


/**
 * A Stakeholder-Specific Vulnerability Categorization (SSVC) decision and who made it.
 */
export interface NvdSsvcMetricV203 {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The decision. */
    ssvcData: NvdSsvcData,
}


/**
 * One SSVC decision, as the answers chosen on the way through a decision tree.
 */
export interface NvdSsvcData {
    /** When NVD produced this response or this decision. */
    timestamp?: string,
    /** The decision in a short form. */
    computed?: string,
    /** The answers given, each as a decision point and its value. */
    options: NvdSsvcOption[],
    /** The role of whoever made the decision, such as CISA Coordinator. */
    role: string,
    /** The version of SSVC used. */
    version: string,
    /** The whole decision tree that was used. */
    decisionTree?: NvdSsvcDecisionTree,
    /** The vulnerability the decision is about, by whatever identifier. */
    id?: string,
    /** The address of the decision tree that was used. */
    decisionTreeUrl?: string,
    /** The tool that wrote this decision. */
    generator?: string,
}


/**
 * One answer on the way through a decision tree, keyed by its decision point.
 */
export interface NvdSsvcOption {
    /** How far the vulnerability is known to be exploited, such as none, poc or active. */
    exploitation?: string,
    /** Whether an attacker could automate the attack, as yes or no. */
    automatable?: string,
    /** How much control an attacker would gain, as partial or total. */
    technicalImpact?: string,
}


/**
 * A whole SSVC decision tree, in the form of the schema NVD's file names.
 */
export interface NvdSsvcDecisionTree {
}


/**
 * The products that one source says the vulnerability affects.
 */
export interface NvdAffected {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The products. */
    affectedData: NvdAffectedProduct[],
}


/**
 * A product and which of its versions have the vulnerability.
 */
export interface NvdAffectedProduct {
    /** The status of any version the versions list does not name. */
    defaultStatus?: string,
    /** Who makes or maintains the product. */
    vendor?: string,
    /** The product's name. */
    product?: string,
    /** The address of the package collection that holds the product. */
    collectionURL?: string,
    /** The package's name within that collection. */
    packageName?: string,
    /** The product's CPE names, in the 2.2 or the 2.3 form. */
    cpes?: string[],
    /** The affected parts of the product. */
    modules?: string[],
    /** The affected source code files. */
    programFiles?: string[],
    /** The affected source code routines. */
    programRoutines?: NvdProgramRoutine[],
    /** The platforms the vulnerability is limited to. */
    platforms?: string[],
    /** The address of the product's source code repository. */
    repo?: string,
    /** The versions or ranges of versions whose status is known. */
    versions?: NvdAffectedVersion[],
    /** The product's Package URL, with no version in it. */
    packageURL?: string,
}


/**
 * One affected source code routine.
 */
export interface NvdProgramRoutine {
    /** The name of the source code routine. */
    name: string,
}


/**
 * The status of one version of a product, or of a range of its versions.
 */
export interface NvdAffectedVersion {
    /** The version, or the start of the range. */
    version: string,
    /** The state of this thing, from the list its class names. */
    status: string,
    /** The numbering scheme that orders the versions, such as semver or git. */
    versionType?: string,
    /** The first version after the range. */
    lessThan?: string,
    /** The last version in the range. */
    lessThanOrEqual?: string,
    /** Where the status changes within the range. */
    changes?: NvdVersionChange[],
}


/**
 * A point within a range of versions where the status changes.
 */
export interface NvdVersionChange {
    /** The version at which the status changes. */
    at: string,
    /** The state of this thing, from the list its class names. */
    status: string,
}


/**
 * The weaknesses that one source says lie behind a vulnerability.
 */
export interface NvdWeakness {
    /** The email address or UUID of the organization that supplied this. */
    source: string,
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** The weakness, as language-tagged text, usually a CWE identifier. */
    description: NvdLangString[],
}


/**
 * A statement of which product configurations have the vulnerability.
 */
export interface NvdConfiguration {
    /** How the parts of this configuration combine. */
    operator?: string,
    /** Whether the result of the configuration is reversed. */
    negate?: boolean,
    /** The parts of the statement. */
    nodes: NvdConfigurationNode[],
}


/**
 * One part of a configuration statement, as a set of CPE matches.
 */
export interface NvdConfigurationNode {
    /** How the parts of this configuration combine. */
    operator: string,
    /** Whether the result of the configuration is reversed. */
    negate?: boolean,
    /** The CPE matches of this part. */
    cpeMatch: NvdCpeMatch[],
}


/**
 * A CPE match string or range, and whether what it matches is vulnerable.
 */
export interface NvdCpeMatch {
    /** A CPE match string, which may hold wildcards. */
    criteria: string,
    /** The UUID that NVD gives a CPE match string. */
    matchCriteriaId: string,
    /** The version above which the match starts, itself left out. */
    versionStartExcluding?: string,
    /** The first version the match covers. */
    versionStartIncluding?: string,
    /** The version below which the match ends, itself left out. */
    versionEndExcluding?: string,
    /** The last version the match covers. */
    versionEndIncluding?: string,
    /** Whether what this matches has the vulnerability, rather than only setting the scene. */
    vulnerable: boolean,
}


/**
 * What a product's vendor has said about a vulnerability.
 */
export interface NvdVendorComment {
    /** When NVD last changed this. */
    lastModified: string,
    /** The vendor's name. */
    organization: string,
    /** What the vendor said. */
    comment: string,
}


/**
 * A page of the product API's results.
 */
export interface NvdCpeResponse extends NvdResponseMixin {
    /** The products on this page. */
    products: NvdCpeItem[],
}


/**
 * One entry of a product response, which only wraps the CPE name.
 */
export interface NvdCpeItem {
    /** The CPE name and what NVD holds about it. */
    cpe: NvdCpe,
}


/**
 * A CPE name as NVD holds it, with its UUID.
 */
export interface NvdCpe {
    /** A Common Platform Enumeration (CPE) name, in its 2.3 formatted string. */
    cpeName: string,
    /** The UUID that NVD gives a CPE name. */
    cpeNameId: string,
    /** When NVD first recorded this. */
    created: string,
    /** When NVD last changed this. */
    lastModified: string,
    /** Whether NVD has retired this CPE name. */
    deprecated: boolean,
    /** The product's titles, in one or more languages. */
    titles?: NvdCpeTitle[],
    /** Pages about the product. */
    refs?: NvdCpeReference[],
    /** The CPE names that replace this one. */
    deprecatedBy?: NvdCpeNameLink[],
    /** The CPE names this one replaces. */
    deprecates?: NvdCpeNameLink[],
}


/**
 * A product's title in one language.
 */
export interface NvdCpeTitle {
    /** The human-readable title. */
    title: string,
    /** The language of the text beside it, as a language code. */
    lang: string,
}


/**
 * A page about a product, and what kind of page it is.
 */
export interface NvdCpeReference {
    /** The kind of this thing, from the list its class names. */
    type?: string,
    /** The page's address. */
    ref: string,
}


/**
 * A pointer from one CPE name to another.
 */
export interface NvdCpeNameLink {
    /** A Common Platform Enumeration (CPE) name, in its 2.3 formatted string. */
    cpeName?: string,
    /** The UUID that NVD gives a CPE name. */
    cpeNameId?: string,
}


/**
 * A page of the match-string API's results.
 */
export interface NvdCpeMatchResponse extends NvdResponseMixin {
    /** The match strings on this page. */
    matchStrings: NvdMatchStringItem[],
}


/**
 * One entry of a match-string response, which only wraps the match string.
 */
export interface NvdMatchStringItem {
    /** The match string and what NVD holds about it. */
    matchString: NvdMatchString,
}


/**
 * A CPE match string or range as NVD holds it, and the CPE names it matches.
 */
export interface NvdMatchString {
    /** A CPE match string, which may hold wildcards. */
    criteria: string,
    /** The UUID that NVD gives a CPE match string. */
    matchCriteriaId: string,
    /** The version above which the match starts, itself left out. */
    versionStartExcluding?: string,
    /** The first version the match covers. */
    versionStartIncluding?: string,
    /** The version below which the match ends, itself left out. */
    versionEndExcluding?: string,
    /** The last version the match covers. */
    versionEndIncluding?: string,
    /** When NVD first recorded this. */
    created: string,
    /** When NVD last changed this. */
    lastModified: string,
    /** The state of this thing, from the list its class names. */
    status: string,
    /** When NVD last changed the list of CPE names this matches. */
    cpeLastModified?: string,
    /** The CPE names this matches. */
    matches?: NvdMatchedCpe[],
}


/**
 * A CPE name that a match string matches.
 */
export interface NvdMatchedCpe {
    /** A Common Platform Enumeration (CPE) name, in its 2.3 formatted string. */
    cpeName: string,
    /** The UUID that NVD gives a CPE name. */
    cpeNameId: string,
}


/**
 * A page of the change-history API's results.
 */
export interface NvdHistoryResponse extends NvdResponseMixin {
    /** The changes on this page. */
    cveChanges?: NvdChangeItem[],
}


/**
 * One entry of a change-history response, which only wraps the change.
 */
export interface NvdChangeItem {
    /** The change. */
    change: NvdChange,
}


/**
 * One change to a vulnerability's record at NVD.
 */
export interface NvdChange {
    /** The email address or UUID of the organization that supplied this. */
    sourceIdentifier: string,
    /** When NVD first recorded this. */
    created?: string,
    /** The vulnerability the change is to. */
    cveId: NvdCveId,
    /** The kind of event, such as Initial Analysis or CVE Modified. */
    eventName: string,
    /** The UUID that NVD gives this change. */
    cveChangeId: string,
    /** What the change did, part by part. */
    details?: NvdChangeDetail[],
}


/**
 * One part of a change, naming what kind of data changed and how.
 */
export interface NvdChangeDetail {
    /** The kind of this thing, from the list its class names. */
    type: string,
    /** How the data changed, such as Added. */
    action?: string,
    /** The value before the change. */
    oldValue?: string,
    /** The value after the change. */
    newValue?: string,
}


/**
 * A value before or after a change that is an object, with any keys.
 */
export interface NvdChangeObject {
}



