from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2.2.4"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'upstream_sha256': {'tag': 'upstream_sha256',
                                         'value': '2b9c4e8ab7e6e42aa17ea787f58167beff47c119c6f291405f86ac19c6149e01'}},
     'comments': ["The version is the edition of NVD's vulnerability schema, as "
                  "its title names it. Each module's header carries the edition of "
                  'its own schema: 2.0 for the product and match-string responses, '
                  'and 2.0.1 for the change history. '
                  "scripts/check_upstream_release.py compares each file's SHA-256 "
                  'with its pin, since NIST changes them in place with no release.',
                  'NVD has four kinds of response and no document that holds them, '
                  'so each response module marks its own response as a tree root, '
                  'and the generators write NvdCveResponse as the top class. Name '
                  'the kind when validating, with linkml-validate -C '
                  'NvdCpeResponse.'],
     'default_prefix': 'nist_nvd',
     'default_range': 'string',
     'description': 'A LinkML model of the JSON responses of the NVD API 2.0, from '
                    'the JSON schemas NIST publishes: vulnerabilities, products, '
                    "match strings and change history. NVD's own keys are the "
                    "schema's keys, so a real response validates unchanged.",
     'id': 'https://w3id.org/lmodel/nist-nvd',
     'imports': ['linkml:types',
                 './nvd_core',
                 './nvd_cve',
                 './nvd_cpe',
                 './nvd_cpematch',
                 './nvd_history'],
     'license': 'Apache-2.0',
     'name': 'nist_nvd',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_nvd': {'prefix_prefix': 'nist_nvd',
                               'prefix_reference': 'https://w3id.org/lmodel/nist-nvd/'}},
     'see_also': ['https://lmodel.github.io/nist-nvd',
                  'https://nvd.nist.gov/developers/start-here'],
     'source': 'https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema',
     'source_file': 'src/nist_nvd/schema/nist_nvd.yaml',
     'title': 'National Vulnerability Database (NVD)'} )

class CvssSeverity(str, Enum):
    """
    A CVSS rating in words.
    """
    NONE = "NONE"
    """
    No severity at all, for a score of 0.
    """
    LOW = "LOW"
    """
    The lowest rating above none.
    """
    MEDIUM = "MEDIUM"
    """
    The middle rating.
    """
    HIGH = "HIGH"
    """
    The rating below critical.
    """
    CRITICAL = "CRITICAL"
    """
    The highest rating.
    """


class CvssV2AccessVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 2.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from the same local network segment.
    """
    LOCAL = "LOCAL"
    """
    Only with an account on the system or hands on it.
    """


class CvssV2AccessComplexity(str, Enum):
    """
    How hard the flaw is to use, in CVSS 2.0's terms.
    """
    HIGH = "HIGH"
    """
    Only under unusual, hard-to-arrange conditions.
    """
    MEDIUM = "MEDIUM"
    """
    Under conditions that take some arranging.
    """
    LOW = "LOW"
    """
    With no special conditions.
    """


class CvssV2Authentication(str, Enum):
    """
    How many logins an attacker needs, in CVSS 2.0's terms.
    """
    MULTIPLE = "MULTIPLE"
    """
    More than one login.
    """
    SINGLE = "SINGLE"
    """
    One login.
    """
    NONE = "NONE"
    """
    No login at all.
    """


class CvssV2Impact(str, Enum):
    """
    How much of one security property an attack could cost, in CVSS 2.0's terms.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    PARTIAL = "PARTIAL"
    """
    Some is lost, and the attacker cannot choose all of it.
    """
    COMPLETE = "COMPLETE"
    """
    All of it is lost.
    """


class CvssExploitCodeMaturity(str, Enum):
    """
    How far working attack code has come.
    """
    UNPROVEN = "UNPROVEN"
    """
    No attack code is known, or the attack is only theory.
    """
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    """
    A demonstration exists that needs skilled work to use.
    """
    FUNCTIONAL = "FUNCTIONAL"
    """
    Working attack code exists for most situations.
    """
    HIGH = "HIGH"
    """
    Attack code is reliable and widely available, or no code is needed.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssRemediationLevel(str, Enum):
    """
    What kind of fix is available.
    """
    OFFICIAL_FIX = "OFFICIAL_FIX"
    """
    The vendor offers a complete fix.
    """
    TEMPORARY_FIX = "TEMPORARY_FIX"
    """
    The vendor offers a stopgap for now.
    """
    WORKAROUND = "WORKAROUND"
    """
    Others offer a way round the flaw that is not from the vendor.
    """
    UNAVAILABLE = "UNAVAILABLE"
    """
    No fix exists, or it cannot be applied.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2ReportConfidence(str, Enum):
    """
    How far the flaw has been confirmed, in CVSS 2.0's terms.
    """
    UNCONFIRMED = "UNCONFIRMED"
    """
    A single report or conflicting reports that nobody has checked.
    """
    UNCORROBORATED = "UNCORROBORATED"
    """
    Several unofficial sources agree, with some doubt remaining.
    """
    CONFIRMED = "CONFIRMED"
    """
    The vendor accepts it, or a working attack shows it.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2CollateralDamagePotential(str, Enum):
    """
    How much loss could follow beyond the system itself.
    """
    NONE = "NONE"
    """
    No such loss.
    """
    LOW = "LOW"
    """
    Slight loss.
    """
    LOW_MEDIUM = "LOW_MEDIUM"
    """
    Moderate loss.
    """
    MEDIUM_HIGH = "MEDIUM_HIGH"
    """
    Significant loss.
    """
    HIGH = "HIGH"
    """
    Catastrophic loss.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV2TargetDistribution(str, Enum):
    """
    How much of the environment the flaw exposes.
    """
    NONE = "NONE"
    """
    No systems at all, or only in a lab.
    """
    LOW = "LOW"
    """
    Up to about a quarter of systems.
    """
    MEDIUM = "MEDIUM"
    """
    About a quarter to three quarters of systems.
    """
    HIGH = "HIGH"
    """
    More than about three quarters of systems.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssRequirement(str, Enum):
    """
    How much one security property matters to the scorer.
    """
    LOW = "LOW"
    """
    A loss would have limited effect.
    """
    MEDIUM = "MEDIUM"
    """
    A loss would have serious effect.
    """
    HIGH = "HIGH"
    """
    A loss would have catastrophic effect.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV3AttackVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 3's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from a logically nearby network.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """


class CvssV3ModifiedAttackVector(str, Enum):
    """
    The attack vector as the scorer's environment changes it, in CVSS 3's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT_NETWORK = "ADJACENT_NETWORK"
    """
    Only from a logically nearby network.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssAttackComplexity(str, Enum):
    """
    How much is outside the attacker's control.
    """
    HIGH = "HIGH"
    """
    Success depends on conditions the attacker must overcome or wait for.
    """
    LOW = "LOW"
    """
    The attacker can succeed again and again with no special effort.
    """


class CvssModifiedAttackComplexity(str, Enum):
    """
    The attack complexity as the scorer's environment changes it.
    """
    HIGH = "HIGH"
    """
    Success depends on conditions the attacker must overcome or wait for.
    """
    LOW = "LOW"
    """
    The attacker can succeed again and again with no special effort.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssPrivilegesRequired(str, Enum):
    """
    What access an attacker needs beforehand.
    """
    HIGH = "HIGH"
    """
    Administrator-level access.
    """
    LOW = "LOW"
    """
    Ordinary user access.
    """
    NONE = "NONE"
    """
    No access at all.
    """


class CvssModifiedPrivilegesRequired(str, Enum):
    """
    The access needed as the scorer's environment changes it.
    """
    HIGH = "HIGH"
    """
    Administrator-level access.
    """
    LOW = "LOW"
    """
    Ordinary user access.
    """
    NONE = "NONE"
    """
    No access at all.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3UserInteraction(str, Enum):
    """
    Whether someone else has to take part, in CVSS 3's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    REQUIRED = "REQUIRED"
    """
    Someone other than the attacker has to do something.
    """


class CvssV3ModifiedUserInteraction(str, Enum):
    """
    The user interaction as the scorer's environment changes it, in CVSS 3's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    REQUIRED = "REQUIRED"
    """
    Someone other than the attacker has to do something.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3Scope(str, Enum):
    """
    Whether an attack can reach beyond the flawed component.
    """
    UNCHANGED = "UNCHANGED"
    """
    The harm stays within the same security authority.
    """
    CHANGED = "CHANGED"
    """
    The harm can reach something under another security authority.
    """


class CvssV3ModifiedScope(str, Enum):
    """
    The scope as the scorer's environment changes it.
    """
    UNCHANGED = "UNCHANGED"
    """
    The harm stays within the same security authority.
    """
    CHANGED = "CHANGED"
    """
    The harm can reach something under another security authority.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssImpact(str, Enum):
    """
    How much of one security property an attack could cost.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """


class CvssModifiedImpact(str, Enum):
    """
    The impact on one security property as the scorer's environment changes it.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV3ReportConfidence(str, Enum):
    """
    How far the flaw has been confirmed, in CVSS 3's terms.
    """
    UNKNOWN = "UNKNOWN"
    """
    Reports say something is wrong, but the cause is not clear.
    """
    REASONABLE = "REASONABLE"
    """
    Solid details exist, without full confirmation of the cause.
    """
    CONFIRMED = "CONFIRMED"
    """
    The flaw is shown beyond doubt, or the vendor accepts it.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the metric does not change the score.
    """


class CvssV4AttackVector(str, Enum):
    """
    How far away an attacker can be, in CVSS 4.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT = "ADJACENT"
    """
    Only from something logically or physically nearby.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """


class CvssV4ModifiedAttackVector(str, Enum):
    """
    The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NETWORK = "NETWORK"
    """
    From anywhere that can route to the system.
    """
    ADJACENT = "ADJACENT"
    """
    Only from something logically or physically nearby.
    """
    LOCAL = "LOCAL"
    """
    Only by acting on the system itself, directly or through a user.
    """
    PHYSICAL = "PHYSICAL"
    """
    Only by touching the hardware.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4AttackRequirements(str, Enum):
    """
    Whether the attack needs conditions in the target beyond the attacker's control.
    """
    NONE = "NONE"
    """
    The attack works whatever the target's state.
    """
    PRESENT = "PRESENT"
    """
    The attack works only when the target is in a certain state.
    """


class CvssV4ModifiedAttackRequirements(str, Enum):
    """
    The attack requirements as the scorer's environment changes them.
    """
    NONE = "NONE"
    """
    The attack works whatever the target's state.
    """
    PRESENT = "PRESENT"
    """
    The attack works only when the target is in a certain state.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4UserInteraction(str, Enum):
    """
    Whether someone else has to take part, in CVSS 4.0's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    PASSIVE = "PASSIVE"
    """
    Someone has to act only in the ordinary course of their work.
    """
    ACTIVE = "ACTIVE"
    """
    Someone has to take a deliberate step.
    """


class CvssV4ModifiedUserInteraction(str, Enum):
    """
    The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NONE = "NONE"
    """
    The attack needs nobody else.
    """
    PASSIVE = "PASSIVE"
    """
    Someone has to act only in the ordinary course of their work.
    """
    ACTIVE = "ACTIVE"
    """
    Someone has to take a deliberate step.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4ModifiedSubsequentImpact(str, Enum):
    """
    The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.
    """
    NONE = "NONE"
    """
    Nothing is lost.
    """
    LOW = "LOW"
    """
    Some is lost, with limited consequences.
    """
    HIGH = "HIGH"
    """
    All of it is lost, or the loss has serious consequences.
    """
    SAFETY = "SAFETY"
    """
    The loss could injure people.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the base metric stands.
    """


class CvssV4ExploitMaturity(str, Enum):
    """
    How much is known about attacks on the flaw.
    """
    UNREPORTED = "UNREPORTED"
    """
    No demonstration or attack has been reported.
    """
    PROOF_OF_CONCEPT = "PROOF_OF_CONCEPT"
    """
    A demonstration is public, with no reported attack.
    """
    ATTACKED = "ATTACKED"
    """
    Attacks have been reported, or tools for them are public.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value, so the worst case is assumed.
    """


class CvssV4Safety(str, Enum):
    """
    Whether an attack could put people's safety at risk.
    """
    NEGLIGIBLE = "NEGLIGIBLE"
    """
    Any harm to people would be slight at most.
    """
    PRESENT = "PRESENT"
    """
    People could be seriously hurt.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4Automatable(str, Enum):
    """
    Whether every step of an attack could be automated across many targets.
    """
    NO = "NO"
    """
    At least one step resists automation.
    """
    YES = "YES"
    """
    Every step can be automated.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4Recovery(str, Enum):
    """
    How the affected system comes back after an attack.
    """
    AUTOMATIC = "AUTOMATIC"
    """
    The system recovers by itself.
    """
    USER = "USER"
    """
    Someone has to step in and restore it.
    """
    IRRECOVERABLE = "IRRECOVERABLE"
    """
    The system cannot be restored.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ValueDensity(str, Enum):
    """
    How much of a resource one successful attack gains the attacker.
    """
    DIFFUSE = "DIFFUSE"
    """
    Each target holds little, so an attacker must take many.
    """
    CONCENTRATED = "CONCENTRATED"
    """
    A single target holds a lot.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ResponseEffort(str, Enum):
    """
    How much work it takes a consumer to respond to the flaw.
    """
    LOW = "LOW"
    """
    Little work, such as reading advice or a small configuration change.
    """
    MODERATE = "MODERATE"
    """
    Some work, with a noticeable effect on the service.
    """
    HIGH = "HIGH"
    """
    Much work, or a long outage.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class CvssV4ProviderUrgency(str, Enum):
    """
    How urgent the product's supplier says the flaw is, as a colour.
    """
    CLEAR = "CLEAR"
    """
    The supplier sees little or no urgency.
    """
    GREEN = "GREEN"
    """
    The supplier says the flaw can wait for regular work.
    """
    AMBER = "AMBER"
    """
    The supplier says the flaw matters soon.
    """
    RED = "RED"
    """
    The supplier says the flaw is at the highest urgency.
    """
    NOT_DEFINED = "NOT_DEFINED"
    """
    The scorer gave no value.
    """


class NvdVulnStatus(str, Enum):
    """
    Where a vulnerability stands in NVD's own analysis.
    """
    Analyzed = "Analyzed"
    """
    NVD has finished its analysis of the record.
    """
    Deferred = "Deferred"
    """
    NVD has put off analysing the record.
    """
    Awaiting_Analysis = "Awaiting Analysis"
    """
    NVD has the record and has not begun to analyse it.
    """
    Modified = "Modified"
    """
    The record has changed since NVD analysed it.
    """
    Received = "Received"
    """
    The record has just reached NVD.
    """
    Undergoing_Analysis = "Undergoing Analysis"
    """
    NVD is analysing the record now.
    """
    Rejected = "Rejected"
    """
    The CVE identifier has been rejected.
    """


class NvdCveTagName(str, Enum):
    """
    A label that a CVE record's source puts on the record.
    """
    unsupported_when_assigned = "unsupported-when-assigned"
    """
    The product had lost its support when the identifier was assigned.
    """
    exclusively_hosted_service = "exclusively-hosted-service"
    """
    The product exists only as a hosted service.
    """
    disputed = "disputed"
    """
    A party disputes that this is a vulnerability.
    """


class NvdReferenceTag(str, Enum):
    """
    NVD's label for what a reference is.
    """
    Broken_Link = "Broken Link"
    """
    The address no longer leads to the content.
    """
    Exploit = "Exploit"
    """
    The page shows or gives a way to exploit the vulnerability.
    """
    Issue_Tracking = "Issue Tracking"
    """
    An entry in a bug or issue tracker.
    """
    Mailing_List = "Mailing List"
    """
    A message in a mailing list archive.
    """
    Mitigation = "Mitigation"
    """
    The page says how to reduce the risk without a fix.
    """
    Not_Applicable = "Not Applicable"
    """
    The page does not bear on the vulnerability.
    """
    Patch = "Patch"
    """
    The page holds or points to a fix.
    """
    Permissions_Required = "Permissions Required"
    """
    Reading the page takes an account or some other access.
    """
    PressSOLIDUSMedia_Coverage = "Press/Media Coverage"
    """
    A report in the press or other media.
    """
    Related = "Related"
    """
    A page on a related matter.
    """
    Product = "Product"
    """
    A page about the affected product.
    """
    Release_Notes = "Release Notes"
    """
    The notes of a product release.
    """
    Technical_Description = "Technical Description"
    """
    A technical account of the vulnerability.
    """
    Third_Party_Advisory = "Third Party Advisory"
    """
    An advisory from someone other than the vendor.
    """
    Tool_Signature = "Tool Signature"
    """
    A signature that a detection tool can use.
    """
    URL_Repurposed = "URL Repurposed"
    """
    The address now leads to something else.
    """
    US_Government_Resource = "US Government Resource"
    """
    A page from a body of the United States government.
    """
    VDB_Entry = "VDB Entry"
    """
    An entry in a vulnerability database.
    """
    Vendor_Advisory = "Vendor Advisory"
    """
    An advisory from the product's vendor.
    """


class NvdSourceType(str, Enum):
    """
    Whether a score or a weakness comes from the party NVD treats as first.
    """
    Primary = "Primary"
    """
    NVD's first source for the record.
    """
    Secondary = "Secondary"
    """
    Any other source.
    """


class NvdCvssV2Severity(str, Enum):
    """
    The severity band NVD gives a CVSS 2.0 base score.
    """
    LOW = "LOW"
    """
    The low band of CVSS 2.0 base scores.
    """
    MEDIUM = "MEDIUM"
    """
    The middle band of CVSS 2.0 base scores.
    """
    HIGH = "HIGH"
    """
    The high band of CVSS 2.0 base scores.
    """


class NvdVersionStatus(str, Enum):
    """
    Whether a version of a product has the vulnerability.
    """
    affected = "affected"
    """
    This version has the vulnerability.
    """
    unaffected = "unaffected"
    """
    This version does not have the vulnerability.
    """
    unknown = "unknown"
    """
    Nobody has said whether this version has the vulnerability.
    """


class NvdOperator(str, Enum):
    """
    How the parts of a configuration combine.
    """
    AND = "AND"
    """
    Every part must hold.
    """
    OR = "OR"
    """
    At least one part must hold.
    """


class NvdCpeReferenceType(str, Enum):
    """
    What a CPE name's reference points to.
    """
    Advisory = "Advisory"
    """
    A security advisory.
    """
    Change_Log = "Change Log"
    """
    A list of the product's changes.
    """
    Product = "Product"
    """
    A page about the product.
    """
    Project = "Project"
    """
    A page about the project behind the product.
    """
    Vendor = "Vendor"
    """
    A page about the vendor.
    """
    Version = "Version"
    """
    A page about this version.
    """


class NvdMatchStringStatus(str, Enum):
    """
    Whether NVD still uses a match string.
    """
    Active = "Active"
    """
    NVD uses this match string.
    """
    Inactive = "Inactive"
    """
    NVD no longer uses this match string.
    """



class NvdResponseMixin(ConfiguredBaseModel):
    """
    The fields of a page of results, which every NVD API response carries.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_core',
         'mixin': True,
         'slot_usage': {'timestamp': {'name': 'timestamp', 'required': True}}})

    format: str = Field(default=..., description="""The name NVD gives this kind of response.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schemas say only that this is a string. Each response "
                      "class pins the one value the API's answers carry."],
         'domain_of': ['NvdResponseMixin'],
         'slot_uri': 'nist_nvd:format'} })
    timestamp: str = Field(default=..., description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    resultsPerPage: int = Field(default=..., description="""How many results this page holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:resultsPerPage'} })
    startIndex: int = Field(default=..., description="""The position of this page's first result among all the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:startIndex'} })
    totalResults: int = Field(default=..., description="""How many results the request matched in all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:totalResults'} })
    version: str = Field(default=..., description="""The version of the response format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:responseVersion'} })


class CvssSeverityBandsMixin(ConfiguredBaseModel):
    """
    The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/anyOf '
                                                    'imports/cvss/cvss-v3.1.json#/anyOf '
                                                    'imports/cvss/cvss-v4.0.json#/allOf/0/anyOf'}},
         'comments': ['The upstream also rules out a score that is not a multiple of '
                      '0.1, as a list of numbers no LinkML range can state. '
                      'tests/cve_rules.py checks that.'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixin': True,
         'rules': [{'description': 'A base severity of NONE goes with a base score of '
                                   'exactly 0.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 0,
                                                                         'minimum_value': 0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'NONE',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity NONE'},
                   {'description': 'A base severity of LOW goes with a base score from '
                                   '0.1 to 3.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 3.9,
                                                                         'minimum_value': 0.1,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'LOW',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity LOW'},
                   {'description': 'A base severity of MEDIUM goes with a base score '
                                   'from 4.0 to 6.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 6.9,
                                                                         'minimum_value': 4.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'MEDIUM',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity MEDIUM'},
                   {'description': 'A base severity of HIGH goes with a base score '
                                   'from 7.0 to 8.9.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 8.9,
                                                                         'minimum_value': 7.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'HIGH',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity HIGH'},
                   {'description': 'A base severity of CRITICAL goes with a base score '
                                   'from 9.0 to 10.',
                    'postconditions': {'slot_conditions': {'baseScore': {'maximum_value': 10.0,
                                                                         'minimum_value': 9.0,
                                                                         'name': 'baseScore'}}},
                    'preconditions': {'slot_conditions': {'baseSeverity': {'equals_string': 'CRITICAL',
                                                                           'name': 'baseSeverity'}}},
                    'title': 'base severity CRITICAL'}]})

    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin', 'NvdCvssMetricV2']} })


class CvssV20(ConfiguredBaseModel):
    """
    A score under CVSS version 2.0, which has no severity bands.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS2BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'related_mappings': ['spdx_security:CvssV2VulnAssessmentRelationship'],
         'slot_usage': {'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssV2Impact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssV2Impact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssV2Impact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV2ReportConfidence'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'},
                        'version': {'equals_string': '2.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["2.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'equals_string': '2.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    confidentialityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssV2Impact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV2ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    accessVector: Optional[CvssV2AccessVector] = Field(default=None, description="""How far away an attacker can be when using the flaw, in CVSS 2.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/accessVector'}},
         'close_mappings': ['sepses_cvss:accessVector'],
         'domain_of': ['CvssV20']} })
    accessComplexity: Optional[CvssV2AccessComplexity] = Field(default=None, description="""How hard the flaw is to use once the attacker can reach it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/accessComplexity'}},
         'close_mappings': ['sepses_cvss:accessComplexity'],
         'domain_of': ['CvssV20']} })
    authentication: Optional[CvssV2Authentication] = Field(default=None, description="""How many times an attacker must log in before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/authentication'}},
         'close_mappings': ['sepses_cvss:authentication'],
         'domain_of': ['CvssV20']} })
    exploitability: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come, in CVSS 2.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/exploitability'}},
         'domain_of': ['CvssV20']} })
    collateralDamagePotential: Optional[CvssV2CollateralDamagePotential] = Field(default=None, description="""How much loss a successful attack could cause beyond the system itself.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/collateralDamagePotential'}},
         'domain_of': ['CvssV20']} })
    targetDistribution: Optional[CvssV2TargetDistribution] = Field(default=None, description="""How much of the scorer's environment is exposed to the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/targetDistribution'}},
         'domain_of': ['CvssV20']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV30(CvssSeverityBandsMixin):
    """
    A score under CVSS version 3.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV3AttackVector'},
                        'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssImpact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssImpact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssImpact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'name': 'modifiedAttackVector',
                                                 'range': 'CvssV3ModifiedAttackVector'},
                        'modifiedAvailabilityImpact': {'name': 'modifiedAvailabilityImpact',
                                                       'range': 'CvssModifiedImpact'},
                        'modifiedConfidentialityImpact': {'name': 'modifiedConfidentialityImpact',
                                                          'range': 'CvssModifiedImpact'},
                        'modifiedIntegrityImpact': {'name': 'modifiedIntegrityImpact',
                                                    'range': 'CvssModifiedImpact'},
                        'modifiedPrivilegesRequired': {'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV3ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV3ReportConfidence'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV3UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'},
                        'version': {'equals_string': '3.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["3.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'equals_string': '3.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV3AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV3UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    scope: Optional[CvssV3Scope] = Field(default=None, description="""Whether an attack can reach beyond the component that holds the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/scope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/scope'}},
         'close_mappings': ['sepses_cvss:scope'],
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    exploitCodeMaturity: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/exploitCodeMaturity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/exploitCodeMaturity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV3ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the temporal score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/temporalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackVector: Optional[CvssV3ModifiedAttackVector] = Field(default=None, description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=None, description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=None, description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedUserInteraction: Optional[CvssV3ModifiedUserInteraction] = Field(default=None, description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedScope: Optional[CvssV3ModifiedScope] = Field(default=None, description="""The scope as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedScope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedScope'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The confidentiality impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedConfidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedConfidentialityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The integrity impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedIntegrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedIntegrityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The availability impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAvailabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAvailabilityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    environmentalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the environmental score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/environmentalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin', 'NvdCvssMetricV2']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV31(CvssSeverityBandsMixin):
    """
    A score under CVSS version 3.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.1.json#/'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV3AttackVector'},
                        'availabilityImpact': {'name': 'availabilityImpact',
                                               'range': 'CvssImpact'},
                        'availabilityRequirement': {'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityImpact': {'name': 'confidentialityImpact',
                                                  'range': 'CvssImpact'},
                        'confidentialityRequirement': {'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityImpact': {'name': 'integrityImpact',
                                            'range': 'CvssImpact'},
                        'integrityRequirement': {'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'name': 'modifiedAttackVector',
                                                 'range': 'CvssV3ModifiedAttackVector'},
                        'modifiedAvailabilityImpact': {'name': 'modifiedAvailabilityImpact',
                                                       'range': 'CvssModifiedImpact'},
                        'modifiedConfidentialityImpact': {'name': 'modifiedConfidentialityImpact',
                                                          'range': 'CvssModifiedImpact'},
                        'modifiedIntegrityImpact': {'name': 'modifiedIntegrityImpact',
                                                    'range': 'CvssModifiedImpact'},
                        'modifiedPrivilegesRequired': {'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV3ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'remediationLevel': {'name': 'remediationLevel',
                                             'range': 'CvssRemediationLevel'},
                        'reportConfidence': {'name': 'reportConfidence',
                                             'range': 'CvssV3ReportConfidence'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV3UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'},
                        'version': {'equals_string': '3.1',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["3.1"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'equals_string': '3.1',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV3AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV3UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    scope: Optional[CvssV3Scope] = Field(default=None, description="""Whether an attack can reach beyond the component that holds the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/scope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/scope'}},
         'close_mappings': ['sepses_cvss:scope'],
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityImpact'}},
         'close_mappings': ['sepses_cvss:confidentialityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    integrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change that should not change.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityImpact'}},
         'close_mappings': ['sepses_cvss:integrityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    availabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the service.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityImpact'}},
         'close_mappings': ['sepses_cvss:availabilityImpact'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    exploitCodeMaturity: Optional[CvssExploitCodeMaturity] = Field(default=None, description="""How far working attack code has come.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/exploitCodeMaturity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/exploitCodeMaturity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    remediationLevel: Optional[CvssRemediationLevel] = Field(default=None, description="""What kind of fix is available.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.0.json#/properties/remediationLevel '
                                                    'imports/cvss/cvss-v3.1.json#/properties/remediationLevel'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    reportConfidence: Optional[CvssV3ReportConfidence] = Field(default=None, description="""How far the flaw's existence and details have been confirmed.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.0.json#/properties/reportConfidence '
                                                    'imports/cvss/cvss-v3.1.json#/properties/reportConfidence'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalScore: Optional[float] = Field(default=None, description="""The base score adjusted for what changes over time, such as a fix appearing.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/temporalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    temporalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the temporal score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/temporalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/temporalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=None, description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackVector: Optional[CvssV3ModifiedAttackVector] = Field(default=None, description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=None, description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=None, description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedUserInteraction: Optional[CvssV3ModifiedUserInteraction] = Field(default=None, description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    modifiedScope: Optional[CvssV3ModifiedScope] = Field(default=None, description="""The scope as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedScope '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedScope'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The confidentiality impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedConfidentialityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedConfidentialityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The integrity impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedIntegrityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedIntegrityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    modifiedAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=None, description="""The availability impact as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAvailabilityImpact '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAvailabilityImpact'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    environmentalScore: Optional[float] = Field(default=None, description="""The score adjusted for the scorer's own environment.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.0.json#/properties/environmentalScore '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalScore'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31']} })
    environmentalSeverity: Optional[CvssSeverity] = Field(default=None, description="""The rating in words for the environmental score.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/environmentalSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/environmentalSeverity'}},
         'domain_of': ['CvssV30', 'CvssV31']} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin', 'NvdCvssMetricV2']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class CvssV40(CvssSeverityBandsMixin):
    """
    A score under CVSS version 4.0.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/'}},
         'broad_mappings': ['sepses_cvss:CVSS'],
         'comments': ["The upstream's rules name threatScore, threatSeverity, "
                      'environmentalScore and environmentalSeverity, but its list of '
                      'properties has none of them and it refuses any other key, so a '
                      'score object cannot carry them and this class has no such '
                      'slots.'],
         'from_schema': 'https://w3id.org/lmodel/cve/cve_cvss',
         'mixins': ['CvssSeverityBandsMixin'],
         'related_mappings': ['spdx_security:CvssV4VulnAssessmentRelationship'],
         'slot_usage': {'attackComplexity': {'name': 'attackComplexity',
                                             'range': 'CvssAttackComplexity'},
                        'attackVector': {'name': 'attackVector',
                                         'range': 'CvssV4AttackVector'},
                        'availabilityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                    'name': 'availabilityRequirement',
                                                    'range': 'CvssRequirement'},
                        'confidentialityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                       'name': 'confidentialityRequirement',
                                                       'range': 'CvssRequirement'},
                        'integrityRequirement': {'ifabsent': 'CvssRequirement(NOT_DEFINED)',
                                                 'name': 'integrityRequirement',
                                                 'range': 'CvssRequirement'},
                        'modifiedAttackComplexity': {'ifabsent': 'CvssModifiedAttackComplexity(NOT_DEFINED)',
                                                     'name': 'modifiedAttackComplexity',
                                                     'range': 'CvssModifiedAttackComplexity'},
                        'modifiedAttackVector': {'ifabsent': 'CvssV4ModifiedAttackVector(NOT_DEFINED)',
                                                 'name': 'modifiedAttackVector',
                                                 'range': 'CvssV4ModifiedAttackVector'},
                        'modifiedPrivilegesRequired': {'ifabsent': 'CvssModifiedPrivilegesRequired(NOT_DEFINED)',
                                                       'name': 'modifiedPrivilegesRequired',
                                                       'range': 'CvssModifiedPrivilegesRequired'},
                        'modifiedUserInteraction': {'ifabsent': 'CvssV4ModifiedUserInteraction(NOT_DEFINED)',
                                                    'name': 'modifiedUserInteraction',
                                                    'range': 'CvssV4ModifiedUserInteraction'},
                        'privilegesRequired': {'name': 'privilegesRequired',
                                               'range': 'CvssPrivilegesRequired'},
                        'userInteraction': {'name': 'userInteraction',
                                            'range': 'CvssV4UserInteraction'},
                        'vectorString': {'name': 'vectorString',
                                         'pattern': '^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'},
                        'version': {'equals_string': '4.0',
                                    'name': 'version',
                                    'required': True}}})

    version: Literal["4.0"] = Field(default=..., description="""A version string. On a score it is the CVSS version; on a product entry, the product's.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'equals_string': '4.0',
         'slot_uri': 'cve:version'} })
    vectorString: str = Field(default=..., description="""The scores' metric values written as one compact string.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.0.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v3.1.json#/properties/vectorString '
                                                    'imports/cvss/cvss-v4.0.json#/properties/vectorString'}},
         'close_mappings': ['sepses_cvss:vectorString', 'spdx_security:vectorString'],
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40']} })
    attackVector: Optional[CvssV4AttackVector] = Field(default=None, description="""How far away an attacker can be when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackVector'}},
         'close_mappings': ['sepses_cvss:attackVector'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    attackComplexity: Optional[CvssAttackComplexity] = Field(default=None, description="""How much is outside the attacker's control when using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/attackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/attackComplexity'}},
         'close_mappings': ['sepses_cvss:attackComplexity'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    privilegesRequired: Optional[CvssPrivilegesRequired] = Field(default=None, description="""What level of access an attacker needs before using the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/privilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/privilegesRequired'}},
         'close_mappings': ['sepses_cvss:privilegesRequired'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    userInteraction: Optional[CvssV4UserInteraction] = Field(default=None, description="""Whether someone other than the attacker has to take part.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/userInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/userInteraction'}},
         'close_mappings': ['sepses_cvss:userInteraction'],
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40']} })
    confidentialityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much confidentiality matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/confidentialityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/confidentialityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    integrityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much integrity matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/integrityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/integrityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    availabilityRequirement: Optional[CvssRequirement] = Field(default=CvssRequirement("NOT_DEFINED"), description="""How much availability matters to the scorer for the affected system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.0.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v3.1.json#/properties/availabilityRequirement '
                                                    'imports/cvss/cvss-v4.0.json#/properties/availabilityRequirement'}},
         'domain_of': ['CvssV20', 'CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssRequirement(NOT_DEFINED)'} })
    modifiedAttackVector: Optional[CvssV4ModifiedAttackVector] = Field(default=CvssV4ModifiedAttackVector("NOT_DEFINED"), description="""The attack vector as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackVector '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackVector'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssV4ModifiedAttackVector(NOT_DEFINED)'} })
    modifiedAttackComplexity: Optional[CvssModifiedAttackComplexity] = Field(default=CvssModifiedAttackComplexity("NOT_DEFINED"), description="""The attack complexity as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedAttackComplexity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackComplexity'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssModifiedAttackComplexity(NOT_DEFINED)'} })
    modifiedPrivilegesRequired: Optional[CvssModifiedPrivilegesRequired] = Field(default=CvssModifiedPrivilegesRequired("NOT_DEFINED"), description="""The privileges needed as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedPrivilegesRequired '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedPrivilegesRequired'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssModifiedPrivilegesRequired(NOT_DEFINED)'} })
    modifiedUserInteraction: Optional[CvssV4ModifiedUserInteraction] = Field(default=CvssV4ModifiedUserInteraction("NOT_DEFINED"), description="""The user interaction as the scorer's own environment changes it.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v3.1.json#/properties/modifiedUserInteraction '
                                                    'imports/cvss/cvss-v4.0.json#/properties/modifiedUserInteraction'}},
         'domain_of': ['CvssV30', 'CvssV31', 'CvssV40'],
         'ifabsent': 'CvssV4ModifiedUserInteraction(NOT_DEFINED)'} })
    attackRequirements: Optional[CvssV4AttackRequirements] = Field(default=None, description="""Whether the attack needs conditions in the target that the attacker does not control.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/attackRequirements'}},
         'domain_of': ['CvssV40']} })
    vulnConfidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information in the vulnerable system an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnConfidentialityImpact'}},
         'domain_of': ['CvssV40']} })
    vulnIntegrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change in the vulnerable system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnIntegrityImpact'}},
         'domain_of': ['CvssV40']} })
    vulnAvailabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt the vulnerable system.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnAvailabilityImpact'}},
         'domain_of': ['CvssV40']} })
    subConfidentialityImpact: Optional[CvssImpact] = Field(default=None, description="""How much information in other, connected systems an attack could expose.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subConfidentialityImpact'}},
         'domain_of': ['CvssV40']} })
    subIntegrityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could change in other, connected systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subIntegrityImpact'}},
         'domain_of': ['CvssV40']} })
    subAvailabilityImpact: Optional[CvssImpact] = Field(default=None, description="""How much an attack could disrupt other, connected systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/subAvailabilityImpact'}},
         'domain_of': ['CvssV40']} })
    exploitMaturity: Optional[CvssV4ExploitMaturity] = Field(default=CvssV4ExploitMaturity("NOT_DEFINED"), description="""How much is known about attacks on this flaw, in CVSS 4.0's terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/exploitMaturity'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ExploitMaturity(NOT_DEFINED)'} })
    modifiedAttackRequirements: Optional[CvssV4ModifiedAttackRequirements] = Field(default=CvssV4ModifiedAttackRequirements("NOT_DEFINED"), description="""The attack requirements as the scorer's own environment changes them.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedAttackRequirements'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedAttackRequirements(NOT_DEFINED)'} })
    modifiedVulnConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The confidentiality impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnConfidentialityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedVulnIntegrityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The integrity impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnIntegrityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedVulnAvailabilityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The availability impact on the vulnerable system, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedVulnAvailabilityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedSubConfidentialityImpact: Optional[CvssModifiedImpact] = Field(default=CvssModifiedImpact("NOT_DEFINED"), description="""The confidentiality impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubConfidentialityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssModifiedImpact(NOT_DEFINED)'} })
    modifiedSubIntegrityImpact: Optional[CvssV4ModifiedSubsequentImpact] = Field(default=CvssV4ModifiedSubsequentImpact("NOT_DEFINED"), description="""The integrity impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubIntegrityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedSubsequentImpact(NOT_DEFINED)'} })
    modifiedSubAvailabilityImpact: Optional[CvssV4ModifiedSubsequentImpact] = Field(default=CvssV4ModifiedSubsequentImpact("NOT_DEFINED"), description="""The availability impact on connected systems, in the scorer's environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/modifiedSubAvailabilityImpact'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ModifiedSubsequentImpact(NOT_DEFINED)'} })
    Safety: Optional[CvssV4Safety] = Field(default=CvssV4Safety("NOT_DEFINED"), description="""Whether an attack could put people's safety at risk.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Safety'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Safety(NOT_DEFINED)'} })
    Automatable: Optional[CvssV4Automatable] = Field(default=CvssV4Automatable("NOT_DEFINED"), description="""Whether an attacker could automate every step of an attack across many targets.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Automatable'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Automatable(NOT_DEFINED)'} })
    Recovery: Optional[CvssV4Recovery] = Field(default=CvssV4Recovery("NOT_DEFINED"), description="""How the affected system comes back after an attack.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/Recovery'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4Recovery(NOT_DEFINED)'} })
    valueDensity: Optional[CvssV4ValueDensity] = Field(default=CvssV4ValueDensity("NOT_DEFINED"), description="""Whether one successful attack gains the attacker a little or a lot of a resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/valueDensity'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ValueDensity(NOT_DEFINED)'} })
    vulnerabilityResponseEffort: Optional[CvssV4ResponseEffort] = Field(default=CvssV4ResponseEffort("NOT_DEFINED"), description="""How much work it takes a consumer to respond to the flaw.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/vulnerabilityResponseEffort'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ResponseEffort(NOT_DEFINED)'} })
    providerUrgency: Optional[CvssV4ProviderUrgency] = Field(default=CvssV4ProviderUrgency("NOT_DEFINED"), description="""How urgent the product's supplier says the flaw is, as a colour.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v4.0.json#/properties/providerUrgency'}},
         'domain_of': ['CvssV40'],
         'ifabsent': 'CvssV4ProviderUrgency(NOT_DEFINED)'} })
    baseScore: float = Field(default=..., description="""The score from 0 to 10 for what is inherent in the flaw.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.0.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v3.1.json#/definitions/scoreType '
                                                    'imports/cvss/cvss-v4.0.json#/definitions/scoreType'}},
         'close_mappings': ['sepses_cvss:baseScore', 'spdx_security:score'],
         'domain_of': ['CvssSeverityBandsMixin', 'CvssV20']} })
    baseSeverity: CvssSeverity = Field(default=..., description="""The rating in words that the base score falls under.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v3.0.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v3.1.json#/properties/baseSeverity '
                                                    'imports/cvss/cvss-v4.0.json#/properties/baseSeverity'}},
         'close_mappings': ['sepses_cvss:baseSeverity', 'spdx_security:severity'],
         'domain_of': ['CvssSeverityBandsMixin', 'NvdCvssMetricV2']} })

    @field_validator('vectorString')
    def pattern_vectorString(cls, v):
        pattern=re.compile(r"^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vectorString format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vectorString format: {v}"
            raise ValueError(err_msg)
        return v


class NvdCveResponse(NvdResponseMixin):
    """
    A page of the vulnerability API's results, or a whole data feed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#'}},
         'close_mappings': ['schema:DataFeed'],
         'comments': ["A feed file is one representation of NVD's data, so it relates "
                      'to a DCAT distribution, but this class also covers one page of '
                      'an API answer.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'mixins': ['NvdResponseMixin'],
         'related_mappings': ['dcat:Distribution'],
         'slot_usage': {'format': {'equals_string': 'NVD_CVE', 'name': 'format'}},
         'tree_root': True})

    vulnerabilities: list[NvdVulnerability] = Field(default=..., description="""The vulnerabilities on this page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCveResponse']} })
    format: Literal["NVD_CVE"] = Field(default=..., description="""The name NVD gives this kind of response.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schemas say only that this is a string. Each response "
                      "class pins the one value the API's answers carry."],
         'domain_of': ['NvdResponseMixin'],
         'equals_string': 'NVD_CVE',
         'slot_uri': 'nist_nvd:format'} })
    timestamp: str = Field(default=..., description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    resultsPerPage: int = Field(default=..., description="""How many results this page holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:resultsPerPage'} })
    startIndex: int = Field(default=..., description="""The position of this page's first result among all the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:startIndex'} })
    totalResults: int = Field(default=..., description="""How many results the request matched in all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:totalResults'} })
    version: str = Field(default=..., description="""The version of the response format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:responseVersion'} })


class NvdVulnerability(ConfiguredBaseModel):
    """
    One entry of a response, which only wraps the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['def_cve_item'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/def_cve_item'}},
         'close_mappings': ['schema:DataFeedItem'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    cve: NvdCve = Field(default=..., description="""The vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdVulnerability']} })


class NvdCve(ConfiguredBaseModel):
    """
    A vulnerability as NVD holds it, under its CVE identifier.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cve_item'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cve_item'}},
         'close_mappings': ['cve:CveRecord',
                            'stix:StixVulnerability',
                            'spdx3:Security/Vulnerability',
                            'sepses_cve:CVE',
                            'wd:Q631425'],
         'comments': ['NVD republishes CVE records and adds its own analysis, so this '
                      'is close to a CVE record and not the same thing. A record of '
                      'this class also repeats four fields of the CISA Known Exploited '
                      'Vulnerabilities catalog when the catalog lists it.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'lastModified': {'name': 'lastModified', 'required': True}}})

    id: str = Field(default=..., description="""The vulnerability's CVE identifier.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:identifier'],
         'comments': ['Every CVE identifier in the KEV catalog of 2026-11-03 is the id '
                      'of one record the API marks as known exploited, and the '
                      'reverse.'],
         'domain_of': ['NvdCve', 'NvdSsvcData'],
         'exact_mappings': ['cve:cveId', 'kev_catalog:cveID'],
         'slot_uri': 'nist_nvd:id'} })
    sourceIdentifier: Optional[str] = Field(default=None, description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve', 'NvdCveTag', 'NvdChange'],
         'slot_uri': 'nist_nvd:sourceIdentifier'} })
    lastModified: str = Field(default=..., description="""When NVD last changed this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx3:Security/modifiedTime'],
         'comments': ["On a vulnerability this is NVD's own time, not the CVE record's "
                      'dateUpdated: the two are set by different parties and often '
                      'differ, so the mapping to it is only a related one.'],
         'domain_of': ['NvdCve', 'NvdVendorComment', 'NvdCpe', 'NvdMatchString'],
         'related_mappings': ['cve:dateUpdated'],
         'slot_uri': 'nist_nvd:lastModified'} })
    references: list[NvdReference] = Field(default=..., description="""The pages that NVD lists about this vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:references', 'sepses_cve:hasReference'],
         'domain_of': ['NvdCve'],
         'slot_uri': 'nist_nvd:references'} })
    vulnStatus: Optional[NvdVulnStatus] = Field(default=None, description="""Where this vulnerability stands in NVD's analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve']} })
    published: str = Field(default=..., description="""When NVD published this vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:issued',
                            'schema:datePublished',
                            'spdx3:Security/publishedTime'],
         'comments': ["This is NVD's own time, not the CVE record's datePublished. For "
                      'CVE-2021-44228 the CVE record says 2021-12-10T00:00:00.000Z and '
                      'NVD 2021-12-10T10:15:09.143, so the mapping is only a related '
                      'one.'],
         'domain_of': ['NvdCve'],
         'related_mappings': ['cve:datePublished']} })
    evaluatorComment: Optional[str] = Field(default=None, description="""A remark from NVD's analyst.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve']} })
    evaluatorSolution: Optional[str] = Field(default=None, description="""A way to resolve the vulnerability, from NVD's analyst.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve']} })
    evaluatorImpact: Optional[str] = Field(default=None, description="""What the vulnerability can lead to, from NVD's analyst.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve']} })
    cisaExploitAdd: Optional[date] = Field(default=None, description="""The day CISA added this vulnerability to its Known Exploited Vulnerabilities catalog.""", json_schema_extra = { "linkml_meta": {'comments': ["Equal to the catalog's value for all 1,766 entries of the "
                      'catalog of 2026-11-03, read through the API.'],
         'domain_of': ['NvdCve'],
         'exact_mappings': ['kev_catalog:dateAdded']} })
    cisaActionDue: Optional[date] = Field(default=None, description="""The day by which CISA says federal agencies must act.""", json_schema_extra = { "linkml_meta": {'comments': ["Equal to the catalog's value for all 1,766 entries of the "
                      'catalog of 2026-11-03, read through the API.'],
         'domain_of': ['NvdCve'],
         'exact_mappings': ['kev_catalog:dueDate']} })
    cisaRequiredAction: Optional[str] = Field(default=None, description="""What CISA says agencies must do about this vulnerability.""", json_schema_extra = { "linkml_meta": {'comments': ["Equal to the catalog's value for all 1,766 entries of the "
                      'catalog of 2026-11-03, read through the API.'],
         'domain_of': ['NvdCve'],
         'exact_mappings': ['kev_catalog:requiredAction']} })
    cisaVulnerabilityName: Optional[str] = Field(default=None, description="""The name CISA gives this vulnerability in its catalog.""", json_schema_extra = { "linkml_meta": {'comments': ["Equal to the catalog's value for all 1,766 entries of the "
                      'catalog of 2026-11-03, read through the API.'],
         'domain_of': ['NvdCve'],
         'exact_mappings': ['kev_catalog:vulnerabilityName']} })
    cveTags: Optional[list[NvdCveTag]] = Field(default=None, description="""The labels the record's sources put on it.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:tags'], 'domain_of': ['NvdCve']} })
    descriptions: list[NvdLangString] = Field(default=..., description="""What the vulnerability is, in one or more languages.""", min_length=1, json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:descriptions'], 'domain_of': ['NvdCve']} })
    metrics: Optional[NvdMetrics] = Field(default=None, description="""The scores that NVD and others give this vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:metrics'],
         'domain_of': ['NvdCve'],
         'related_mappings': ['sepses_cvss:hasCVSS']} })
    affected: Optional[list[NvdAffected]] = Field(default=None, description="""The affected products, by the source that names them.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:affected'], 'domain_of': ['NvdCve']} })
    weaknesses: Optional[list[NvdWeakness]] = Field(default=None, description="""The weaknesses behind the vulnerability, by the source that names them.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:problemTypes'],
         'domain_of': ['NvdCve'],
         'related_mappings': ['sepses_cve:hasCWE']} })
    configurations: Optional[list[NvdConfiguration]] = Field(default=None, description="""The product configurations that have the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:cpeApplicability',
                            'sepses_cve:hasVulnerableConfiguration'],
         'domain_of': ['NvdCve']} })
    vendorComments: Optional[list[NvdVendorComment]] = Field(default=None, description="""What product vendors have said about this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve']} })


class NvdCveTag(ConfiguredBaseModel):
    """
    The labels that one source puts on a record.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cve_item/properties/cveTags/items'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'tags': {'name': 'tags', 'range': 'NvdCveTagName'}}})

    sourceIdentifier: Optional[str] = Field(default=None, description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve', 'NvdCveTag', 'NvdChange'],
         'slot_uri': 'nist_nvd:sourceIdentifier'} })
    tags: Optional[list[NvdCveTagName]] = Field(default=None, description="""Labels on this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCveTag', 'NvdReference'], 'slot_uri': 'nist_nvd:tags'} })


class NvdLangString(ConfiguredBaseModel):
    """
    A piece of text and the language it is in.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['lang_string'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/lang_string'}},
         'close_mappings': ['cve:CveDescription'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    lang: str = Field(default=..., description="""The language of the text beside it, as a language code.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['NvdLangString', 'NvdCpeTitle'],
         'slot_uri': 'nist_nvd:lang'} })
    value: str = Field(default=..., description="""The text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdLangString'], 'slot_uri': 'nist_nvd:langStringValue'} })

    @field_validator('value')
    def pattern_value(cls, v):
        pattern=re.compile(r"^[\s\S]{0,4096}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid value format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid value format: {v}"
            raise ValueError(err_msg)
        return v


class NvdReference(ConfiguredBaseModel):
    """
    A page about a vulnerability, with NVD's labels for what it is.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['reference'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/reference'}},
         'close_mappings': ['cve:CveReference', 'sepses_cve:Reference'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'source': {'close_mappings': ['sepses_cve:referenceSource'],
                                   'name': 'source'},
                        'tags': {'name': 'tags', 'range': 'NvdReferenceTag'}}})

    url: str = Field(default=..., description="""The address of the page.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:url', 'sepses_cve:referenceUrl'],
         'domain_of': ['NvdReference'],
         'slot_uri': 'nist_nvd:url'} })
    source: Optional[str] = Field(default=None, description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cve:referenceSource'],
         'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    tags: Optional[list[NvdReferenceTag]] = Field(default=None, description="""Labels on this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCveTag', 'NvdReference'], 'slot_uri': 'nist_nvd:tags'} })

    @field_validator('url')
    def pattern_url(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid url format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid url format: {v}"
            raise ValueError(err_msg)
        return v


class NvdMetrics(ConfiguredBaseModel):
    """
    The scores of a vulnerability, in a list per scoring system and version.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cve_item/properties/metrics'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    cvssMetricV40: Optional[list[NvdCvssMetricV40]] = Field(default=None, description="""The CVSS 4.0 scores.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMetrics']} })
    cvssMetricV31: Optional[list[NvdCvssMetricV31]] = Field(default=None, description="""The CVSS 3.1 scores.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMetrics']} })
    cvssMetricV30: Optional[list[NvdCvssMetricV30]] = Field(default=None, description="""The CVSS 3.0 scores.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMetrics']} })
    cvssMetricV2: Optional[list[NvdCvssMetricV2]] = Field(default=None, description="""The CVSS 2.0 scores.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMetrics']} })
    ssvcV203: Optional[list[NvdSsvcMetricV203]] = Field(default=None, description="""The SSVC 2.0.3 decisions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMetrics']} })


class NvdCvssMetricV2(ConfiguredBaseModel):
    """
    A CVSS 2.0 score, who gave it, and NVD's figures beside it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cvss-v2'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cvss-v2'}},
         'close_mappings': ['sepses_cvss:CVSS2BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'related_mappings': ['spdx3:Security/CvssV2VulnAssessmentRelationship'],
         'slot_usage': {'cvssData': {'name': 'cvssData', 'range': 'CvssV20'},
                        'source': {'name': 'source', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'NvdSourceType',
                                 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    type: NvdSourceType = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    cvssData: CvssV20 = Field(default=..., description="""The CVSS score itself, in FIRST's form for its version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40'],
         'slot_uri': 'nist_nvd:cvssData'} })
    exploitabilityScore: Optional[float] = Field(default=None, description="""The CVSS exploitability subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:exploitabilityScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:exploitabilityScore'} })
    impactScore: Optional[float] = Field(default=None, description="""The CVSS impact subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:impactScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:impactScore'} })
    baseSeverity: Optional[NvdCvssV2Severity] = Field(default=None, description="""The severity band of the base score, which CVSS 2.0 leaves to NVD.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:severity'],
         'domain_of': ['CvssSeverityBandsMixin', 'NvdCvssMetricV2'],
         'slot_uri': 'nist_nvd:baseSeverity'} })
    acInsufInfo: Optional[bool] = Field(default=None, description="""Whether NVD lacked the information to rate the access complexity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2']} })
    obtainAllPrivilege: Optional[bool] = Field(default=None, description="""Whether exploiting this gains every privilege.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2']} })
    obtainUserPrivilege: Optional[bool] = Field(default=None, description="""Whether exploiting this gains a user's privileges.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2']} })
    obtainOtherPrivilege: Optional[bool] = Field(default=None, description="""Whether exploiting this gains some other privilege.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2']} })
    userInteractionRequired: Optional[bool] = Field(default=None, description="""Whether exploiting this needs a user to act.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2']} })


class NvdCvssMetricV30(ConfiguredBaseModel):
    """
    A CVSS 3.0 score, who gave it, and its subscores.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cvss-v30'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cvss-v30'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'related_mappings': ['spdx3:Security/CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'cvssData': {'name': 'cvssData', 'range': 'CvssV30'},
                        'source': {'name': 'source', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'NvdSourceType',
                                 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    type: NvdSourceType = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    cvssData: CvssV30 = Field(default=..., description="""The CVSS score itself, in FIRST's form for its version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40'],
         'slot_uri': 'nist_nvd:cvssData'} })
    exploitabilityScore: Optional[float] = Field(default=None, description="""The CVSS exploitability subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:exploitabilityScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:exploitabilityScore'} })
    impactScore: Optional[float] = Field(default=None, description="""The CVSS impact subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:impactScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:impactScore'} })


class NvdCvssMetricV31(ConfiguredBaseModel):
    """
    A CVSS 3.1 score, who gave it, and its subscores.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cvss-v31'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cvss-v31'}},
         'close_mappings': ['sepses_cvss:CVSS3BaseMetric'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'related_mappings': ['spdx3:Security/CvssV3VulnAssessmentRelationship'],
         'slot_usage': {'cvssData': {'name': 'cvssData', 'range': 'CvssV31'},
                        'source': {'name': 'source', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'NvdSourceType',
                                 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    type: NvdSourceType = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    cvssData: CvssV31 = Field(default=..., description="""The CVSS score itself, in FIRST's form for its version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40'],
         'slot_uri': 'nist_nvd:cvssData'} })
    exploitabilityScore: Optional[float] = Field(default=None, description="""The CVSS exploitability subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:exploitabilityScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:exploitabilityScore'} })
    impactScore: Optional[float] = Field(default=None, description="""The CVSS impact subscore.""", ge=0, le=10, json_schema_extra = { "linkml_meta": {'close_mappings': ['sepses_cvss:impactScore'],
         'domain_of': ['NvdCvssMetricV2', 'NvdCvssMetricV30', 'NvdCvssMetricV31'],
         'slot_uri': 'nist_nvd:impactScore'} })


class NvdCvssMetricV40(ConfiguredBaseModel):
    """
    A CVSS 4.0 score and who gave it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cvss-v40'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cvss-v40'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'related_mappings': ['spdx3:Security/CvssV4VulnAssessmentRelationship'],
         'slot_usage': {'cvssData': {'name': 'cvssData', 'range': 'CvssV40'},
                        'source': {'name': 'source', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'NvdSourceType',
                                 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    type: NvdSourceType = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    cvssData: CvssV40 = Field(default=..., description="""The CVSS score itself, in FIRST's form for its version.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40'],
         'slot_uri': 'nist_nvd:cvssData'} })


class NvdSsvcMetricV203(ConfiguredBaseModel):
    """
    A Stakeholder-Specific Vulnerability Categorization (SSVC) decision and who made it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['ssvc-v203'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/ssvc-v203'}},
         'comments': ['SPDX records the outcome of an SSVC decision, and NVD the path '
                      'to it, so the mapping is only a related one.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'related_mappings': ['spdx3:Security/SsvcVulnAssessmentRelationship'],
         'slot_usage': {'source': {'name': 'source', 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    ssvcData: NvdSsvcData = Field(default=..., description="""The decision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcMetricV203']} })


class NvdSsvcData(ConfiguredBaseModel):
    """
    One SSVC decision, as the answers chosen on the way through a decision tree.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'ssvc-v2.0.3.json#'}},
         'comments': ["This class renders the structure of NVD's ssvc-v2.0.3.json. "
                      "NVD's file also names a $schema key, which LinkML's Python "
                      'generators cannot spell. No record of the modified feed of '
                      '2026-11-03 holds it, and tests/test_upstream.py lists the '
                      'departure.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    timestamp: Optional[str] = Field(default=None, description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    computed: Optional[str] = Field(default=None, description="""The decision in a short form.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData']} })
    options: list[NvdSsvcOption] = Field(default=..., description="""The answers given, each as a decision point and its value.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData'], 'list_elements_unique': True} })
    role: str = Field(default=..., description="""The role of whoever made the decision, such as CISA Coordinator.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData']} })
    version: str = Field(default=..., description="""The version of SSVC used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:ssvcVersion'} })
    decisionTree: Optional[Any] = Field(default=None, description="""The whole decision tree that was used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData']} })
    id: Optional[str] = Field(default=None, description="""The vulnerability the decision is about, by whatever identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve', 'NvdSsvcData'], 'slot_uri': 'nist_nvd:ssvcSubject'} })
    decisionTreeUrl: Optional[str] = Field(default=None, description="""The address of the decision tree that was used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData']} })
    generator: Optional[str] = Field(default=None, description="""The tool that wrote this decision.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdSsvcData']} })


class NvdSsvcOption(ConfiguredBaseModel):
    """
    One answer on the way through a decision tree, keyed by its decision point.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'ssvc-v2.0.3.json#/properties/options/items'}},
         'comments': ["NVD's file allows any key, with a string or a list of strings "
                      'as its value, and extra_slots states that. The real data holds '
                      'one key per object, and only these three, each with a string. '
                      "They are named here because LinkML's Pydantic generator ignores "
                      'extra_slots, so without them the Pydantic model refuses every '
                      'SSVC decision.'],
         'extra_slots': {'range_expression': {'any_of': [{'range': 'string'},
                                                         {'multivalued': True,
                                                          'range': 'string'}]}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    exploitation: Optional[str] = Field(default=None, description="""How far the vulnerability is known to be exploited, such as none, poc or active.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'multivalued': True, 'range': 'string'}],
         'domain_of': ['NvdSsvcOption']} })
    automatable: Optional[str] = Field(default=None, description="""Whether an attacker could automate the attack, as yes or no.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'multivalued': True, 'range': 'string'}],
         'domain_of': ['NvdSsvcOption'],
         'notes': ["CVSS 4.0's Automatable differs from this key only by case, so the "
                   'two share one page of the generated docs on a case-insensitive '
                   'filesystem. Both are real keys, so neither is renamed, and '
                   'tests/test_schema_rules.py pins this as the one such pair.']} })
    technicalImpact: Optional[str] = Field(default=None, description="""How much control an attacker would gain, as partial or total.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'}, {'multivalued': True, 'range': 'string'}],
         'domain_of': ['NvdSsvcOption']} })


class NvdAffected(ConfiguredBaseModel):
    """
    The products that one source says the vulnerability affects.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['affected'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/affected'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'source': {'name': 'source', 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    affectedData: list[NvdAffectedProduct] = Field(default=..., description="""The products.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffected']} })


class NvdAffectedProduct(ConfiguredBaseModel):
    """
    A product and which of its versions have the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_affected_1.0.json#'}},
         'close_mappings': ['cve:CveProduct'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'notes': ["NVD's file has the same keys as the CVE Record Format's product. "
                   'It drops the two rules that the CVE format states, that a product '
                   'names a vendor and product or a collection and package, and that '
                   'it has versions or a default status, so this class does not state '
                   "them. The default status keeps NVD's own enum beside it, so "
                   'nvd_cve needs no second copy of the CVE module.']})

    defaultStatus: Optional[NvdVersionStatus] = Field(default=None, description="""The status of any version the versions list does not name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedProduct'], 'slot_uri': 'nist_nvd:defaultStatus'} })
    vendor: Optional[str] = Field(default=None, description="""Who makes or maintains the product.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:vendor'], 'domain_of': ['NvdAffectedProduct']} })
    product: Optional[str] = Field(default=None, description="""The product's name.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:product'], 'domain_of': ['NvdAffectedProduct']} })
    collectionURL: Optional[str] = Field(default=None, description="""The address of the package collection that holds the product.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:collectionURL'], 'domain_of': ['NvdAffectedProduct']} })
    packageName: Optional[str] = Field(default=None, description="""The package's name within that collection.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:packageName'], 'domain_of': ['NvdAffectedProduct']} })
    cpes: Optional[list[str]] = Field(default=None, description="""The product's CPE names, in the 2.2 or the 2.3 form.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:cpes'],
         'comments': ["NVD's own pattern, with its quotes written as \\x22 and \\x27, "
                      'which mean the same. The Python generators cut a raw string at '
                      'a quote.'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    modules: Optional[list[str]] = Field(default=None, description="""The affected parts of the product.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:modules'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    programFiles: Optional[list[str]] = Field(default=None, description="""The affected source code files.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:programFiles'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    programRoutines: Optional[list[NvdProgramRoutine]] = Field(default=None, description="""The affected source code routines.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:programRoutines'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    platforms: Optional[list[str]] = Field(default=None, description="""The platforms the vulnerability is limited to.""", min_length=1, json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:platforms'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    repo: Optional[str] = Field(default=None, description="""The address of the product's source code repository.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:repo'],
         'comments': ["NVD's file says format uri. Some records write an address that "
                      'RFC 3986 refuses, such as '
                      'git://git@gitlab.com:gitlab-org/gitlab.git, so this is a string '
                      'and tests/test_upstream.py lists the departure.'],
         'domain_of': ['NvdAffectedProduct']} })
    versions: Optional[list[NvdAffectedVersion]] = Field(default=None, description="""The versions or ranges of versions whose status is known.""", min_length=1, json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:versions'],
         'domain_of': ['NvdAffectedProduct'],
         'list_elements_unique': True} })
    packageURL: Optional[str] = Field(default=None, description="""The product's Package URL, with no version in it.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['cve:packageURL'], 'domain_of': ['NvdAffectedProduct']} })

    @field_validator('vendor')
    def pattern_vendor(cls, v):
        pattern=re.compile(r"^[\s\S]{1,512}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid vendor format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid vendor format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('product')
    def pattern_product(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid product format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid product format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('collectionURL')
    def pattern_collectionURL(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid collectionURL format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid collectionURL format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('packageName')
    def pattern_packageName(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid packageName format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid packageName format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('cpes')
    def pattern_cpes(cls, v):
        pattern=re.compile(r"([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9._\-~%]*){0,6})|(cpe:2\.3:[aho*\-](:(((\?*|\*?)([a-zA-Z0-9\-._]|(\\[\\*?!\x22#$%&\x27()+,/:;<=>@\[\]\^`{|}~]))+(\?*|\*?))|[*\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[*\-]))(:(((\?*|\*?)([a-zA-Z0-9\-._]|(\\[\\*?!\x22#$%&\x27()+,/:;<=>@\[\]\^`{|}~]))+(\?*|\*?))|[*\-])){4})")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid cpes format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid cpes format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('modules')
    def pattern_modules(cls, v):
        pattern=re.compile(r"^[\s\S]{1,4096}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid modules format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid modules format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('programFiles')
    def pattern_programFiles(cls, v):
        pattern=re.compile(r"^[\s\S]{1,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid programFiles format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid programFiles format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('platforms')
    def pattern_platforms(cls, v):
        pattern=re.compile(r"^[\s\S]{0,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid platforms format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid platforms format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('repo')
    def pattern_repo(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid repo format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid repo format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('packageURL')
    def pattern_packageURL(cls, v):
        pattern=re.compile(r"^[\s\S]{1,2048}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid packageURL format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid packageURL format: {v}"
            raise ValueError(err_msg)
        return v


class NvdProgramRoutine(ConfiguredBaseModel):
    """
    One affected source code routine.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_affected_1.0.json#/properties/programRoutines/items'}},
         'close_mappings': ['cve:CveProgramRoutine'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    name: str = Field(default=..., description="""The name of the source code routine.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdProgramRoutine'], 'slot_uri': 'nist_nvd:name'} })

    @field_validator('name')
    def pattern_name(cls, v):
        pattern=re.compile(r"^[\s\S]{1,4096}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid name format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid name format: {v}"
            raise ValueError(err_msg)
        return v


class NvdAffectedVersion(ConfiguredBaseModel):
    """
    The status of one version of a product, or of a range of its versions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_affected_1.0.json#/properties/versions/items'}},
         'close_mappings': ['cve:CveProductVersion'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'notes': ["These four rules state the oneOf of NVD's file, which has four "
                   'branches: a version and a status alone, those with a numbering '
                   'scheme, and those with a scheme and one of the two limits.'],
         'rules': [{'description': 'A range with a less-than limit names the numbering '
                                   'scheme.',
                    'postconditions': {'slot_conditions': {'versionType': {'name': 'versionType',
                                                                           'value_presence': 'PRESENT'}}},
                    'preconditions': {'slot_conditions': {'lessThan': {'name': 'lessThan',
                                                                       'value_presence': 'PRESENT'}}}},
                   {'description': 'A range with a less-than-or-equal limit names the '
                                   'numbering scheme.',
                    'postconditions': {'slot_conditions': {'versionType': {'name': 'versionType',
                                                                           'value_presence': 'PRESENT'}}},
                    'preconditions': {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                              'value_presence': 'PRESENT'}}}},
                   {'description': 'A range has one upper limit, not two.',
                    'postconditions': {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                               'value_presence': 'ABSENT'}}},
                    'preconditions': {'slot_conditions': {'lessThan': {'name': 'lessThan',
                                                                       'value_presence': 'PRESENT'}}}},
                   {'description': 'Status changes belong to a range, so they need an '
                                   'upper limit.',
                    'postconditions': {'slot_conditions': {'lessThanOrEqual': {'name': 'lessThanOrEqual',
                                                                               'value_presence': 'PRESENT'}}},
                    'preconditions': {'slot_conditions': {'changes': {'name': 'changes',
                                                                      'value_presence': 'PRESENT'},
                                                          'lessThan': {'name': 'lessThan',
                                                                       'value_presence': 'ABSENT'}}}}],
         'slot_usage': {'status': {'name': 'status',
                                   'range': 'NvdVersionStatus',
                                   'required': True},
                        'version': {'description': 'The version, or the start of the '
                                                   'range.',
                                    'name': 'version',
                                    'pattern': '^[\\s\\S]{1,1024}$',
                                    'required': True}}})

    version: str = Field(default=..., description="""The version, or the start of the range.""", json_schema_extra = { "linkml_meta": {'annotations': {'upstream_path': {'tag': 'upstream_path',
                                           'value': 'imports/cvss/cvss-v2.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.0.json#/properties/version '
                                                    'imports/cvss/cvss-v3.1.json#/properties/version '
                                                    'imports/cvss/cvss-v4.0.json#/properties/version'}},
         'comments': ['Each class that uses it narrows it. A top-level slot, so that '
                      "lokf adapt renames it beside LOKF's version."],
         'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'cve:version'} })
    status: NvdVersionStatus = Field(default=..., description="""The state of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion', 'NvdVersionChange', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:status'} })
    versionType: Optional[str] = Field(default=None, description="""The numbering scheme that orders the versions, such as semver or git.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion']} })
    lessThan: Optional[str] = Field(default=None, description="""The first version after the range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion']} })
    lessThanOrEqual: Optional[str] = Field(default=None, description="""The last version in the range.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion']} })
    changes: Optional[list[NvdVersionChange]] = Field(default=None, description="""Where the status changes within the range.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion'], 'list_elements_unique': True} })

    @field_validator('version')
    def pattern_version(cls, v):
        pattern=re.compile(r"^[\s\S]{1,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid version format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('versionType')
    def pattern_versionType(cls, v):
        pattern=re.compile(r"^[\s\S]{1,128}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid versionType format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid versionType format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('lessThan')
    def pattern_lessThan(cls, v):
        pattern=re.compile(r"^[\s\S]{1,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid lessThan format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid lessThan format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('lessThanOrEqual')
    def pattern_lessThanOrEqual(cls, v):
        pattern=re.compile(r"^[\s\S]{1,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid lessThanOrEqual format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid lessThanOrEqual format: {v}"
            raise ValueError(err_msg)
        return v


class NvdVersionChange(ConfiguredBaseModel):
    """
    A point within a range of versions where the status changes.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_affected_1.0.json#/properties/versions/items/properties/changes/items'}},
         'close_mappings': ['cve:CveVersionChange'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'status': {'name': 'status',
                                   'range': 'NvdVersionStatus',
                                   'required': True}}})

    at: str = Field(default=..., description="""The version at which the status changes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdVersionChange'], 'slot_uri': 'nist_nvd:at'} })
    status: NvdVersionStatus = Field(default=..., description="""The state of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion', 'NvdVersionChange', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:status'} })

    @field_validator('at')
    def pattern_at(cls, v):
        pattern=re.compile(r"^[\s\S]{1,1024}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid at format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid at format: {v}"
            raise ValueError(err_msg)
        return v


class NvdWeakness(ConfiguredBaseModel):
    """
    The weaknesses that one source says lie behind a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['weakness'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/weakness'}},
         'close_mappings': ['cve:CveProblemType'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'source': {'name': 'source', 'required': True},
                        'type': {'name': 'type',
                                 'range': 'NvdSourceType',
                                 'required': True}}})

    source: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdReference',
                       'NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdSsvcMetricV203',
                       'NvdAffected',
                       'NvdWeakness'],
         'slot_uri': 'nist_nvd:source'} })
    type: NvdSourceType = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    description: list[NvdLangString] = Field(default=..., description="""The weakness, as language-tagged text, usually a CWE identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdWeakness'], 'slot_uri': 'nist_nvd:description'} })


class NvdConfiguration(ConfiguredBaseModel):
    """
    A statement of which product configurations have the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['config'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/config'}},
         'close_mappings': ['cve:CveCpeApplicabilityElement',
                            'sepses_cve:VulnerableConfiguration'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    operator: Optional[NvdOperator] = Field(default=None, description="""How the parts of this configuration combine.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfiguration', 'NvdConfigurationNode'],
         'slot_uri': 'nist_nvd:operator'} })
    negate: Optional[bool] = Field(default=None, description="""Whether the result of the configuration is reversed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfiguration', 'NvdConfigurationNode'],
         'slot_uri': 'nist_nvd:negate'} })
    nodes: list[NvdConfigurationNode] = Field(default=..., description="""The parts of the statement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfiguration']} })


class NvdConfigurationNode(ConfiguredBaseModel):
    """
    One part of a configuration statement, as a set of CPE matches.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['node'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/node'}},
         'close_mappings': ['cve:CveCpeNode'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'operator': {'name': 'operator', 'required': True}}})

    operator: NvdOperator = Field(default=..., description="""How the parts of this configuration combine.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfiguration', 'NvdConfigurationNode'],
         'slot_uri': 'nist_nvd:operator'} })
    negate: Optional[bool] = Field(default=None, description="""Whether the result of the configuration is reversed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfiguration', 'NvdConfigurationNode'],
         'slot_uri': 'nist_nvd:negate'} })
    cpeMatch: list[NvdCpeMatch] = Field(default=..., description="""The CPE matches of this part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdConfigurationNode']} })


class NvdCpeMatch(ConfiguredBaseModel):
    """
    A CPE match string or range, and whether what it matches is vulnerable.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['cpe_match'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/cpe_match'}},
         'close_mappings': ['cve:CveCpeMatch'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve'})

    criteria: str = Field(default=..., description="""A CPE match string, which may hold wildcards.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:criteria'} })
    matchCriteriaId: str = Field(default=..., description="""The UUID that NVD gives a CPE match string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:matchCriteriaId'} })
    versionStartExcluding: Optional[str] = Field(default=None, description="""The version above which the match starts, itself left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionStartExcluding'} })
    versionStartIncluding: Optional[str] = Field(default=None, description="""The first version the match covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionStartIncluding'} })
    versionEndExcluding: Optional[str] = Field(default=None, description="""The version below which the match ends, itself left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionEndExcluding'} })
    versionEndIncluding: Optional[str] = Field(default=None, description="""The last version the match covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionEndIncluding'} })
    vulnerable: bool = Field(default=..., description="""Whether what this matches has the vulnerability, rather than only setting the scene.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch']} })


class NvdVendorComment(ConfiguredBaseModel):
    """
    What a product's vendor has said about a vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['vendorComment'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_api_json_2.0.schema#/definitions/vendorComment'}},
         'close_mappings': ['schema:Comment'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cve',
         'slot_usage': {'lastModified': {'name': 'lastModified', 'required': True}}})

    lastModified: str = Field(default=..., description="""When NVD last changed this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx3:Security/modifiedTime'],
         'comments': ["On a vulnerability this is NVD's own time, not the CVE record's "
                      'dateUpdated: the two are set by different parties and often '
                      'differ, so the mapping to it is only a related one.'],
         'domain_of': ['NvdCve', 'NvdVendorComment', 'NvdCpe', 'NvdMatchString'],
         'related_mappings': ['cve:dateUpdated'],
         'slot_uri': 'nist_nvd:lastModified'} })
    organization: str = Field(default=..., description="""The vendor's name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdVendorComment']} })
    comment: str = Field(default=..., description="""What the vendor said.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdVendorComment']} })


class NvdCpeResponse(NvdResponseMixin):
    """
    A page of the product API's results.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#'}},
         'close_mappings': ['schema:DataFeed'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe',
         'mixins': ['NvdResponseMixin'],
         'slot_usage': {'format': {'equals_string': 'NVD_CPE', 'name': 'format'}},
         'tree_root': True})

    products: list[NvdCpeItem] = Field(default=..., description="""The products on this page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeResponse']} })
    format: Literal["NVD_CPE"] = Field(default=..., description="""The name NVD gives this kind of response.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schemas say only that this is a string. Each response "
                      "class pins the one value the API's answers carry."],
         'domain_of': ['NvdResponseMixin'],
         'equals_string': 'NVD_CPE',
         'slot_uri': 'nist_nvd:format'} })
    timestamp: str = Field(default=..., description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    resultsPerPage: int = Field(default=..., description="""How many results this page holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:resultsPerPage'} })
    startIndex: int = Field(default=..., description="""The position of this page's first result among all the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:startIndex'} })
    totalResults: int = Field(default=..., description="""How many results the request matched in all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:totalResults'} })
    version: str = Field(default=..., description="""The version of the response format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:responseVersion'} })


class NvdCpeItem(ConfiguredBaseModel):
    """
    One entry of a product response, which only wraps the CPE name.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['defCpe'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#/definitions/defCpe'}},
         'close_mappings': ['schema:DataFeedItem'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe'})

    cpe: NvdCpe = Field(default=..., description="""The CPE name and what NVD holds about it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeItem']} })


class NvdCpe(ConfiguredBaseModel):
    """
    A CPE name as NVD holds it, with its UUID.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe'}},
         'close_mappings': ['sepses_cpe:CPE'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe',
         'notes': ['The identifier is set on this class alone, because cpeNameId also '
                   'appears where one CPE name points to another. lokf adapt replaces '
                   "a slot that is an identifier with LOKF's id everywhere, which "
                   'would rename those keys too.'],
         'slot_usage': {'cpeName': {'name': 'cpeName', 'required': True},
                        'cpeNameId': {'identifier': True, 'name': 'cpeNameId'},
                        'created': {'name': 'created', 'required': True},
                        'lastModified': {'name': 'lastModified', 'required': True}}})

    cpeName: str = Field(default=..., description="""A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeName'} })
    cpeNameId: str = Field(default=..., description="""The UUID that NVD gives a CPE name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeNameId'} })
    created: str = Field(default=..., description="""When NVD first recorded this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:created'],
         'domain_of': ['NvdCpe', 'NvdMatchString', 'NvdChange'],
         'slot_uri': 'nist_nvd:created'} })
    lastModified: str = Field(default=..., description="""When NVD last changed this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx3:Security/modifiedTime'],
         'comments': ["On a vulnerability this is NVD's own time, not the CVE record's "
                      'dateUpdated: the two are set by different parties and often '
                      'differ, so the mapping to it is only a related one.'],
         'domain_of': ['NvdCve', 'NvdVendorComment', 'NvdCpe', 'NvdMatchString'],
         'related_mappings': ['cve:dateUpdated'],
         'slot_uri': 'nist_nvd:lastModified'} })
    deprecated: bool = Field(default=..., description="""Whether NVD has retired this CPE name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe']} })
    titles: Optional[list[NvdCpeTitle]] = Field(default=None, description="""The product's titles, in one or more languages.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe']} })
    refs: Optional[list[NvdCpeReference]] = Field(default=None, description="""Pages about the product.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:references'], 'domain_of': ['NvdCpe']} })
    deprecatedBy: Optional[list[NvdCpeNameLink]] = Field(default=None, description="""The CPE names that replace this one.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:isReplacedBy'], 'domain_of': ['NvdCpe']} })
    deprecates: Optional[list[NvdCpeNameLink]] = Field(default=None, description="""The CPE names this one replaces.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:replaces'], 'domain_of': ['NvdCpe']} })


class NvdCpeTitle(ConfiguredBaseModel):
    """
    A product's title in one language.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['defTitle'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#/definitions/defTitle'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe'})

    title: str = Field(default=..., description="""The human-readable title.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:title'],
         'domain_of': ['NvdCpeTitle'],
         'slot_uri': 'nist_nvd:title'} })
    lang: str = Field(default=..., description="""The language of the text beside it, as a language code.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:language', 'schema:inLanguage'],
         'domain_of': ['NvdLangString', 'NvdCpeTitle'],
         'slot_uri': 'nist_nvd:lang'} })


class NvdCpeReference(ConfiguredBaseModel):
    """
    A page about a product, and what kind of page it is.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['defReference'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#/definitions/defReference'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe',
         'slot_usage': {'type': {'name': 'type', 'range': 'NvdCpeReferenceType'}}})

    type: Optional[NvdCpeReferenceType] = Field(default=None, description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    ref: str = Field(default=..., description="""The page's address.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's own pattern, with its single quote written as \\x27, "
                      'which means the same. gen-python cuts a raw string at a single '
                      'quote.'],
         'domain_of': ['NvdCpeReference']} })

    @field_validator('ref')
    def pattern_ref(cls, v):
        pattern=re.compile(r"^([A-Za-z][A-Za-z0-9+.-]+):(\/\/([^@]+@)?([A-Za-z0-9.\-_~]+)(:\d+)?)?((?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@])+(?:\/(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@])*)*|(?:\/(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27()*+,;=:@])+)*)?(\?(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@]|[/?])*)?(\#(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@]|[/?])*)?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ref format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ref format: {v}"
            raise ValueError(err_msg)
        return v


class NvdCpeNameLink(ConfiguredBaseModel):
    """
    A pointer from one CPE name to another.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpe_api_json_2.0.schema#/definitions/defCpe/properties/cpe/properties/deprecatedBy/items'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpe'})

    cpeName: Optional[str] = Field(default=None, description="""A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeName'} })
    cpeNameId: Optional[str] = Field(default=None, description="""The UUID that NVD gives a CPE name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeNameId'} })


class NvdCpeMatchResponse(NvdResponseMixin):
    """
    A page of the match-string API's results.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpematch_api_json_2.0.schema#'}},
         'close_mappings': ['schema:DataFeed'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpematch',
         'mixins': ['NvdResponseMixin'],
         'slot_usage': {'format': {'equals_string': 'NVD_CPEMatchString',
                                   'name': 'format'}},
         'tree_root': True})

    matchStrings: list[NvdMatchStringItem] = Field(default=..., description="""The match strings on this page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatchResponse']} })
    format: Literal["NVD_CPEMatchString"] = Field(default=..., description="""The name NVD gives this kind of response.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schemas say only that this is a string. Each response "
                      "class pins the one value the API's answers carry."],
         'domain_of': ['NvdResponseMixin'],
         'equals_string': 'NVD_CPEMatchString',
         'slot_uri': 'nist_nvd:format'} })
    timestamp: str = Field(default=..., description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    resultsPerPage: int = Field(default=..., description="""How many results this page holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:resultsPerPage'} })
    startIndex: int = Field(default=..., description="""The position of this page's first result among all the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:startIndex'} })
    totalResults: int = Field(default=..., description="""How many results the request matched in all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:totalResults'} })
    version: str = Field(default=..., description="""The version of the response format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:responseVersion'} })


class NvdMatchStringItem(ConfiguredBaseModel):
    """
    One entry of a match-string response, which only wraps the match string.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['def_matchstring'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpematch_api_json_2.0.schema#/definitions/def_matchstring'}},
         'close_mappings': ['schema:DataFeedItem'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpematch'})

    matchString: NvdMatchString = Field(default=..., description="""The match string and what NVD holds about it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMatchStringItem']} })


class NvdMatchString(ConfiguredBaseModel):
    """
    A CPE match string or range as NVD holds it, and the CPE names it matches.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['def_match_data'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpematch_api_json_2.0.schema#/definitions/def_match_data'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpematch',
         'notes': ['The identifier is set on this class alone, because matchCriteriaId '
                   "also appears in a vulnerability's configurations, where the same "
                   'match string can recur with a different vulnerable flag. So it '
                   'identifies a match string here and not a use of one there.'],
         'slot_usage': {'created': {'name': 'created', 'required': True},
                        'lastModified': {'name': 'lastModified', 'required': True},
                        'matchCriteriaId': {'identifier': True,
                                            'name': 'matchCriteriaId'},
                        'status': {'name': 'status',
                                   'range': 'NvdMatchStringStatus',
                                   'required': True}}})

    criteria: str = Field(default=..., description="""A CPE match string, which may hold wildcards.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:criteria'} })
    matchCriteriaId: str = Field(default=..., description="""The UUID that NVD gives a CPE match string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:matchCriteriaId'} })
    versionStartExcluding: Optional[str] = Field(default=None, description="""The version above which the match starts, itself left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionStartExcluding'} })
    versionStartIncluding: Optional[str] = Field(default=None, description="""The first version the match covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionStartIncluding'} })
    versionEndExcluding: Optional[str] = Field(default=None, description="""The version below which the match ends, itself left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionEndExcluding'} })
    versionEndIncluding: Optional[str] = Field(default=None, description="""The last version the match covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpeMatch', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:versionEndIncluding'} })
    created: str = Field(default=..., description="""When NVD first recorded this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:created'],
         'domain_of': ['NvdCpe', 'NvdMatchString', 'NvdChange'],
         'slot_uri': 'nist_nvd:created'} })
    lastModified: str = Field(default=..., description="""When NVD last changed this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:modified',
                            'schema:dateModified',
                            'spdx3:Security/modifiedTime'],
         'comments': ["On a vulnerability this is NVD's own time, not the CVE record's "
                      'dateUpdated: the two are set by different parties and often '
                      'differ, so the mapping to it is only a related one.'],
         'domain_of': ['NvdCve', 'NvdVendorComment', 'NvdCpe', 'NvdMatchString'],
         'related_mappings': ['cve:dateUpdated'],
         'slot_uri': 'nist_nvd:lastModified'} })
    status: NvdMatchStringStatus = Field(default=..., description="""The state of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdAffectedVersion', 'NvdVersionChange', 'NvdMatchString'],
         'slot_uri': 'nist_nvd:status'} })
    cpeLastModified: Optional[str] = Field(default=None, description="""When NVD last changed the list of CPE names this matches.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMatchString']} })
    matches: Optional[list[NvdMatchedCpe]] = Field(default=None, description="""The CPE names this matches.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdMatchString']} })


class NvdMatchedCpe(ConfiguredBaseModel):
    """
    A CPE name that a match string matches.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['def_cpe_name'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cpematch_api_json_2.0.schema#/definitions/def_cpe_name'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_cpematch',
         'slot_usage': {'cpeName': {'name': 'cpeName', 'required': True},
                        'cpeNameId': {'name': 'cpeNameId', 'required': True}}})

    cpeName: str = Field(default=..., description="""A Common Platform Enumeration (CPE) name, in its 2.3 formatted string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeName'} })
    cpeNameId: str = Field(default=..., description="""The UUID that NVD gives a CPE name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCpe', 'NvdCpeNameLink', 'NvdMatchedCpe'],
         'slot_uri': 'nist_nvd:cpeNameId'} })


class NvdHistoryResponse(NvdResponseMixin):
    """
    A page of the change-history API's results.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_history_api_json_2.0.schema#'}},
         'close_mappings': ['schema:DataFeed'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_history',
         'mixins': ['NvdResponseMixin'],
         'slot_usage': {'format': {'equals_string': 'NVD_CVEHistory',
                                   'name': 'format'}},
         'tree_root': True})

    cveChanges: Optional[list[NvdChangeItem]] = Field(default=None, description="""The changes on this page.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdHistoryResponse']} })
    format: Literal["NVD_CVEHistory"] = Field(default=..., description="""The name NVD gives this kind of response.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schemas say only that this is a string. Each response "
                      "class pins the one value the API's answers carry."],
         'domain_of': ['NvdResponseMixin'],
         'equals_string': 'NVD_CVEHistory',
         'slot_uri': 'nist_nvd:format'} })
    timestamp: str = Field(default=..., description="""When NVD produced this response or this decision.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['schema:dateCreated'],
         'domain_of': ['NvdResponseMixin', 'NvdSsvcData'],
         'slot_uri': 'nist_nvd:timestamp'} })
    resultsPerPage: int = Field(default=..., description="""How many results this page holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:resultsPerPage'} })
    startIndex: int = Field(default=..., description="""The position of this page's first result among all the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:startIndex'} })
    totalResults: int = Field(default=..., description="""How many results the request matched in all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin'], 'slot_uri': 'nist_nvd:totalResults'} })
    version: str = Field(default=..., description="""The version of the response format.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdResponseMixin',
                       'CvssV20',
                       'CvssV30',
                       'CvssV31',
                       'CvssV40',
                       'NvdSsvcData',
                       'NvdAffectedVersion'],
         'slot_uri': 'nist_nvd:responseVersion'} })


class NvdChangeItem(ConfiguredBaseModel):
    """
    One entry of a change-history response, which only wraps the change.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['defChange'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_history_api_json_2.0.schema#/definitions/defChange'}},
         'close_mappings': ['schema:DataFeedItem'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_history'})

    change: NvdChange = Field(default=..., description="""The change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdChangeItem']} })


class NvdChange(ConfiguredBaseModel):
    """
    One change to a vulnerability's record at NVD.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['changeItem'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_history_api_json_2.0.schema#/definitions/changeItem'}},
         'comments': ['A change is something that happened to a record, so it relates '
                      'to a PROV activity, but NVD records only when and by whom, not '
                      'the entities it used.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_history',
         'notes': ['The identifier is set on this class and not on the slot, so that '
                   "lokf adapt keeps the key beside LOKF's id, as it does for "
                   'cpeNameId and matchCriteriaId.'],
         'related_mappings': ['prov:Activity'],
         'slot_usage': {'cveChangeId': {'identifier': True, 'name': 'cveChangeId'},
                        'sourceIdentifier': {'name': 'sourceIdentifier',
                                             'required': True}}})

    cveChangeId: str = Field(default=..., description="""The UUID that NVD gives this change.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdChange'], 'slot_uri': 'nist_nvd:cveChangeId'} })
    sourceIdentifier: str = Field(default=..., description="""The email address or UUID of the organization that supplied this.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdCve', 'NvdCveTag', 'NvdChange'],
         'slot_uri': 'nist_nvd:sourceIdentifier'} })
    created: Optional[str] = Field(default=None, description="""When NVD first recorded this.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['dcterms:created'],
         'domain_of': ['NvdCpe', 'NvdMatchString', 'NvdChange'],
         'slot_uri': 'nist_nvd:created'} })
    cveId: str = Field(default=..., description="""The vulnerability the change is to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdChange']} })
    eventName: str = Field(default=..., description="""The kind of event, such as Initial Analysis or CVE Modified.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schema says only that this is a string. The samples read "
                      'here hold too little of a list of 2.4 million changes to close '
                      'it, so it stays a string.'],
         'domain_of': ['NvdChange']} })
    details: Optional[list[NvdChangeDetail]] = Field(default=None, description="""What the change did, part by part.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdChange']} })

    @field_validator('cveId')
    def pattern_cveId(cls, v):
        pattern=re.compile(r"^CVE-[0-9]{4}-[0-9]{4,}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid cveId format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid cveId format: {v}"
            raise ValueError(err_msg)
        return v


class NvdChangeDetail(ConfiguredBaseModel):
    """
    One part of a change, naming what kind of data changed and how.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'aliases': ['detail'],
         'annotations': {'upstream_definition': {'tag': 'upstream_definition',
                                                 'value': 'cve_history_api_json_2.0.schema#/definitions/detail'}},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_history',
         'slot_usage': {'type': {'comments': ["NVD's schema says only that this is a "
                                              'string, such as CWE or CVSS V3.1. It '
                                              'stays a string for the reason eventName '
                                              'does.'],
                                 'name': 'type',
                                 'required': True}}})

    type: str = Field(default=..., description="""The kind of this thing, from the list its class names.""", json_schema_extra = { "linkml_meta": {'comments': ["NVD's schema says only that this is a string, such as CWE or "
                      'CVSS V3.1. It stays a string for the reason eventName does.'],
         'domain_of': ['NvdCvssMetricV2',
                       'NvdCvssMetricV30',
                       'NvdCvssMetricV31',
                       'NvdCvssMetricV40',
                       'NvdWeakness',
                       'NvdCpeReference',
                       'NvdChangeDetail'],
         'slot_uri': 'nist_nvd:type'} })
    action: Optional[str] = Field(default=None, description="""How the data changed, such as Added.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NvdChangeDetail']} })
    oldValue: Optional[Union[NvdChangeObject, str]] = Field(default=None, description="""The value before the change.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'},
                    {'multivalued': True, 'range': 'string'},
                    {'range': 'NvdChangeObject'}],
         'domain_of': ['NvdChangeDetail']} })
    newValue: Optional[Union[NvdChangeObject, str]] = Field(default=None, description="""The value after the change.""", json_schema_extra = { "linkml_meta": {'any_of': [{'range': 'string'},
                    {'multivalued': True, 'range': 'string'},
                    {'range': 'NvdChangeObject'}],
         'domain_of': ['NvdChangeDetail']} })


class NvdChangeObject(ConfiguredBaseModel):
    """
    A value before or after a change that is an object, with any keys.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["NVD's file allows a string, an array or an object as a value, "
                      "and states nothing of the object's keys. The 1,335 values of "
                      'the three pages read on 2026-11-03 are all strings, so no key '
                      "is named here, and LinkML's Pydantic generator, which ignores "
                      'extra_slots, would refuse an object.'],
         'extra_slots': {'allowed': True},
         'from_schema': 'https://w3id.org/lmodel/nist-nvd/nvd_history'})

    pass


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NvdResponseMixin.model_rebuild()
CvssSeverityBandsMixin.model_rebuild()
CvssV20.model_rebuild()
CvssV30.model_rebuild()
CvssV31.model_rebuild()
CvssV40.model_rebuild()
NvdCveResponse.model_rebuild()
NvdVulnerability.model_rebuild()
NvdCve.model_rebuild()
NvdCveTag.model_rebuild()
NvdLangString.model_rebuild()
NvdReference.model_rebuild()
NvdMetrics.model_rebuild()
NvdCvssMetricV2.model_rebuild()
NvdCvssMetricV30.model_rebuild()
NvdCvssMetricV31.model_rebuild()
NvdCvssMetricV40.model_rebuild()
NvdSsvcMetricV203.model_rebuild()
NvdSsvcData.model_rebuild()
NvdSsvcOption.model_rebuild()
NvdAffected.model_rebuild()
NvdAffectedProduct.model_rebuild()
NvdProgramRoutine.model_rebuild()
NvdAffectedVersion.model_rebuild()
NvdVersionChange.model_rebuild()
NvdWeakness.model_rebuild()
NvdConfiguration.model_rebuild()
NvdConfigurationNode.model_rebuild()
NvdCpeMatch.model_rebuild()
NvdVendorComment.model_rebuild()
NvdCpeResponse.model_rebuild()
NvdCpeItem.model_rebuild()
NvdCpe.model_rebuild()
NvdCpeTitle.model_rebuild()
NvdCpeReference.model_rebuild()
NvdCpeNameLink.model_rebuild()
NvdCpeMatchResponse.model_rebuild()
NvdMatchStringItem.model_rebuild()
NvdMatchString.model_rebuild()
NvdMatchedCpe.model_rebuild()
NvdHistoryResponse.model_rebuild()
NvdChangeItem.model_rebuild()
NvdChange.model_rebuild()
NvdChangeDetail.model_rebuild()
NvdChangeObject.model_rebuild()
