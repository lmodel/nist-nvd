# Auto generated from nist_nvd.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-31T01:50:50
# Schema: nist-nvd
#
# id: https://w3id.org/lmodel/nist-nvd
# description: NIST National Vulnerability Database (NVD) LinkML Schema.
#   Captures enriched vulnerability records, CVSS metric views, CPE
#   applicability statements, weakness attributions, reference resource tags,
#   KEV indicator details, and NVD lifecycle status transitions.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Datetime, Float, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate, XSDDateTime

# fix-protocol patch: enum hash/eq
from linkml_runtime.linkml_model.meta import PermissibleValue as _PV
from linkml_runtime.utils.enumerations import EnumDefinitionImpl as _EDI
if not getattr(_PV, "_fix_protocol_patched", False):
    _orig_pv_eq = _PV.__eq__
    def _pv_eq(self, other):
        if isinstance(other, str):
            return self.text == other
        return _orig_pv_eq(self, other)
    _PV.__eq__ = _pv_eq
    _PV.__hash__ = lambda self: hash(self.text)
    _PV._fix_protocol_patched = True
if not getattr(_EDI, "_fix_protocol_patched", False):
    _orig_edi_eq = _EDI.__eq__
    def _edi_eq(self, other):
        if isinstance(other, str):
            return str(self) == other
        return _orig_edi_eq(self, other)
    # Bypass EnumDefinitionMeta.__setattr__, which routes assignments on
    # enum subclasses through PermissibleValue handling.
    type.__setattr__(_EDI, "__eq__", _edi_eq)
    type.__setattr__(_EDI, "__hash__", lambda self: hash(str(self)))
    type.__setattr__(_EDI, "_fix_protocol_patched", True)

metamodel_version = "1.7.0"
version = None

# Namespaces
WIKIDATA = CurieNamespace('WIKIDATA', 'https://www.wikidata.org/wiki/')
CORE = CurieNamespace('core', 'https://w3id.org/lmodel/vulnerability-core/')
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
CWE = CurieNamespace('cwe', 'https://w3id.org/lmodel/cwe/')
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
KEV_CATALOG = CurieNamespace('kev_catalog', 'https://w3id.org/lmodel/kev-catalog/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NVD = CurieNamespace('nvd', 'https://w3id.org/lmodel/nist-nvd/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SCHEMA_VULNERABILITY_CORE = CurieNamespace('schema_vulnerability_core', 'https://w3id.org/lmodel/vulnerability-core/schema/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NVD


# Types
class CveId(str):
    """ A CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CveId"
    type_model_uri = NVD.CveId


class IsoDate(str):
    """ A calendar date in ISO 8601 format (YYYY-MM-DD). """
    type_class_uri = XSD["date"]
    type_class_curie = "xsd:date"
    type_name = "IsoDate"
    type_model_uri = NVD.IsoDate




# Enumerations
class CVSSVersion(EnumDefinitionImpl):
    """
    Supported CVSS versions displayed in NVD metrics tabs.
    """
    V2_0 = PermissibleValue(text="V2_0")
    V3_0 = PermissibleValue(text="V3_0")
    V3_1 = PermissibleValue(text="V3_1")
    V4_0 = PermissibleValue(text="V4_0")

    _defn = EnumDefinition(
        name="CVSSVersion",
        description="Supported CVSS versions displayed in NVD metrics tabs.",
    )

class NVDTag(EnumDefinitionImpl):
    """
    NVD analysis tags attached to vulnerability records.
    """
    ANALYSIS_PENDING = PermissibleValue(text="ANALYSIS_PENDING")
    ADDITIONAL_INFORMATION = PermissibleValue(text="ADDITIONAL_INFORMATION")

    _defn = EnumDefinition(
        name="NVDTag",
        description="NVD analysis tags attached to vulnerability records.",
    )

class ScoreSource(EnumDefinitionImpl):
    """
    Provider of CVSS vectors and scores.
    """
    NVD = PermissibleValue(text="NVD")
    CNA = PermissibleValue(text="CNA")
    ADP = PermissibleValue(text="ADP")
    VENDOR = PermissibleValue(text="VENDOR")
    THIRD_PARTY = PermissibleValue(text="THIRD_PARTY")

    _defn = EnumDefinition(
        name="ScoreSource",
        description="Provider of CVSS vectors and scores.",
    )

class ReferenceTag(EnumDefinitionImpl):
    """
    Resource tag labels used by NVD references.
    """
    THIRD_PARTY_ADVISORY = PermissibleValue(text="THIRD_PARTY_ADVISORY")
    VENDOR_ADVISORY = PermissibleValue(text="VENDOR_ADVISORY")
    ISSUE_TRACKING = PermissibleValue(text="ISSUE_TRACKING")
    PATCH = PermissibleValue(text="PATCH")
    TECHNICAL_DESCRIPTION = PermissibleValue(text="TECHNICAL_DESCRIPTION")
    PRESS_MEDIA_COVERAGE = PermissibleValue(text="PRESS_MEDIA_COVERAGE")
    VDB_ENTRY = PermissibleValue(text="VDB_ENTRY")

    _defn = EnumDefinition(
        name="ReferenceTag",
        description="Resource tag labels used by NVD references.",
    )

class ConfigurationType(EnumDefinitionImpl):
    """
    NVD configuration rendering category.
    """
    BASIC = PermissibleValue(text="BASIC")
    RUNNING_ON_WITH = PermissibleValue(text="RUNNING_ON_WITH")
    ADVANCED = PermissibleValue(text="ADVANCED")

    _defn = EnumDefinition(
        name="ConfigurationType",
        description="NVD configuration rendering category.",
    )

class NVDWorkflowStatus(EnumDefinitionImpl):
    """
    Enrichment state labels shown by NVD for CVEs.
    """
    AWAITING_ENRICHMENT = PermissibleValue(text="AWAITING_ENRICHMENT")
    UNDERGOING_ENRICHMENT = PermissibleValue(text="UNDERGOING_ENRICHMENT")
    ENRICHED = PermissibleValue(text="ENRICHED")
    MODIFIED_AFTER_ENRICHMENT = PermissibleValue(text="MODIFIED_AFTER_ENRICHMENT")
    NOT_SCHEDULED = PermissibleValue(text="NOT_SCHEDULED")
    REJECTED = PermissibleValue(text="REJECTED")

    _defn = EnumDefinition(
        name="NVDWorkflowStatus",
        description="Enrichment state labels shown by NVD for CVEs.",
    )

class NVDWorkflowEventSource(EnumDefinitionImpl):
    """
    Source of state transition decisions in the status flow.
    """
    NVD_PROCESS = PermissibleValue(text="NVD_PROCESS")
    NVD_STAFF_DECISION = PermissibleValue(text="NVD_STAFF_DECISION")
    CVE_PROGRAM_PROCESS = PermissibleValue(text="CVE_PROGRAM_PROCESS")
    USER_REQUEST = PermissibleValue(text="USER_REQUEST")

    _defn = EnumDefinition(
        name="NVDWorkflowEventSource",
        description="Source of state transition decisions in the status flow.",
    )

class VersionBoundType(EnumDefinitionImpl):
    """
    Boundary type for version-range constraints.
    """
    START_INCLUDING = PermissibleValue(text="START_INCLUDING")
    START_EXCLUDING = PermissibleValue(text="START_EXCLUDING")
    END_INCLUDING = PermissibleValue(text="END_INCLUDING")
    END_EXCLUDING = PermissibleValue(text="END_EXCLUDING")

    _defn = EnumDefinition(
        name="VersionBoundType",
        description="Boundary type for version-range constraints.",
    )

class VulnerabilityStatus(EnumDefinitionImpl):
    """
    Lifecycle state of a vulnerability record.
    """
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Vulnerability is actively maintained and published.")
    REJECTED = PermissibleValue(
        text="REJECTED",
        description="CVE ID was rejected and should not be used.")
    DISPUTED = PermissibleValue(
        text="DISPUTED",
        description="The vulnerability details are disputed by a party.")
    RESERVED = PermissibleValue(
        text="RESERVED",
        description="CVE ID is reserved but details are not yet published.")
    DEPRECATED = PermissibleValue(
        text="DEPRECATED",
        description="Entry has been superseded or withdrawn.")

    _defn = EnumDefinition(
        name="VulnerabilityStatus",
        description="Lifecycle state of a vulnerability record.",
    )

class ImpactSeverity(EnumDefinitionImpl):
    """
    CVSS qualitative severity rating.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No measurable impact.")
    LOW = PermissibleValue(
        text="LOW",
        description="Limited impact; exploitation requires specific conditions.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="Moderate impact; partial compromise of security properties.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="High impact; significant compromise of security properties.")
    CRITICAL = PermissibleValue(
        text="CRITICAL",
        description="Critical impact; complete compromise; remote exploitation likely.")
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Severity has not been assessed or is unavailable.")

    _defn = EnumDefinition(
        name="ImpactSeverity",
        description="CVSS qualitative severity rating.",
    )


# Class references
class CVSSScoreNoteNoteId(extended_str):
    pass


class StatusTransitionTransitionId(extended_str):
    pass


class VulnerabilityCveId(extended_str):
    pass


class NVDEntryCveId(VulnerabilityCveId):
    pass


@dataclass(repr=False)
class MetricSet(YAMLRoot):
    """
    Container for all metric views across CVSS versions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["MetricSet"]
    class_class_curie: ClassVar[str] = "nvd:MetricSet"
    class_name: ClassVar[str] = "MetricSet"
    class_model_uri: ClassVar[URIRef] = NVD.MetricSet

    cvss_v4_metrics: Optional[Union[Union[dict, "CVSSMetric"], list[Union[dict, "CVSSMetric"]]]] = empty_list()
    cvss_v3_metrics: Optional[Union[Union[dict, "CVSSMetric"], list[Union[dict, "CVSSMetric"]]]] = empty_list()
    cvss_v2_metrics: Optional[Union[Union[dict, "CVSSMetric"], list[Union[dict, "CVSSMetric"]]]] = empty_list()
    score_notes: Optional[Union[dict[Union[str, CVSSScoreNoteNoteId], Union[dict, "CVSSScoreNote"]], list[Union[dict, "CVSSScoreNote"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.cvss_v4_metrics, list):
            self.cvss_v4_metrics = [self.cvss_v4_metrics] if self.cvss_v4_metrics is not None else []
        self.cvss_v4_metrics = [v if isinstance(v, CVSSMetric) else CVSSMetric(**as_dict(v)) for v in self.cvss_v4_metrics]

        if not isinstance(self.cvss_v3_metrics, list):
            self.cvss_v3_metrics = [self.cvss_v3_metrics] if self.cvss_v3_metrics is not None else []
        self.cvss_v3_metrics = [v if isinstance(v, CVSSMetric) else CVSSMetric(**as_dict(v)) for v in self.cvss_v3_metrics]

        if not isinstance(self.cvss_v2_metrics, list):
            self.cvss_v2_metrics = [self.cvss_v2_metrics] if self.cvss_v2_metrics is not None else []
        self.cvss_v2_metrics = [v if isinstance(v, CVSSMetric) else CVSSMetric(**as_dict(v)) for v in self.cvss_v2_metrics]

        self._normalize_inlined_as_list(slot_name="score_notes", slot_type=CVSSScoreNote, key_name="note_id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVSSMetric(YAMLRoot):
    """
    Individual CVSS vector and score attribution.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["CVSSMetric"]
    class_class_curie: ClassVar[str] = "nvd:CVSSMetric"
    class_name: ClassVar[str] = "CVSSMetric"
    class_model_uri: ClassVar[URIRef] = NVD.CVSSMetric

    version: Optional[str] = None
    vector_string: Optional[str] = None
    base_score: Optional[float] = None
    base_severity: Optional[Union[str, "ImpactSeverity"]] = None
    source: Optional[Union[str, "ScoreSource"]] = None
    provider_label: Optional[str] = None
    scoring_justification: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.vector_string is not None and not isinstance(self.vector_string, str):
            self.vector_string = str(self.vector_string)

        if self.base_score is not None and not isinstance(self.base_score, float):
            self.base_score = float(self.base_score)

        if self.base_severity is not None and not isinstance(self.base_severity, ImpactSeverity):
            self.base_severity = ImpactSeverity(self.base_severity)

        if self.source is not None and not isinstance(self.source, ScoreSource):
            self.source = ScoreSource(self.source)

        if self.provider_label is not None and not isinstance(self.provider_label, str):
            self.provider_label = str(self.provider_label)

        if self.scoring_justification is not None and not isinstance(self.scoring_justification, str):
            self.scoring_justification = str(self.scoring_justification)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVSSScoreNote(YAMLRoot):
    """
    Additional explanatory note for CVSS display conditions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["CVSSScoreNote"]
    class_class_curie: ClassVar[str] = "nvd:CVSSScoreNote"
    class_name: ClassVar[str] = "CVSSScoreNote"
    class_model_uri: ClassVar[URIRef] = NVD.CVSSScoreNote

    note_id: Union[str, CVSSScoreNoteNoteId] = None
    message: Optional[str] = None
    source: Optional[str] = None
    created: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.note_id):
            self.MissingRequiredField("note_id")
        if not isinstance(self.note_id, CVSSScoreNoteNoteId):
            self.note_id = CVSSScoreNoteNoteId(self.note_id)

        if self.message is not None and not isinstance(self.message, str):
            self.message = str(self.message)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.created is not None and not isinstance(self.created, XSDDateTime):
            self.created = XSDDateTime(self.created)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CPEConfiguration(YAMLRoot):
    """
    Logical grouping of CPE match criteria for affected software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["CPEConfiguration"]
    class_class_curie: ClassVar[str] = "nvd:CPEConfiguration"
    class_name: ClassVar[str] = "CPEConfiguration"
    class_model_uri: ClassVar[URIRef] = NVD.CPEConfiguration

    configuration_id: Optional[str] = None
    configuration_type: Optional[Union[str, "ConfigurationType"]] = None
    operator: Optional[str] = None
    children: Optional[Union[Union[dict, "CPEConfiguration"], list[Union[dict, "CPEConfiguration"]]]] = empty_list()
    matches: Optional[Union[Union[dict, "CPEMatch"], list[Union[dict, "CPEMatch"]]]] = empty_list()
    summary: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.configuration_id is not None and not isinstance(self.configuration_id, str):
            self.configuration_id = str(self.configuration_id)

        if self.configuration_type is not None and not isinstance(self.configuration_type, ConfigurationType):
            self.configuration_type = ConfigurationType(self.configuration_type)

        if self.operator is not None and not isinstance(self.operator, str):
            self.operator = str(self.operator)

        if not isinstance(self.children, list):
            self.children = [self.children] if self.children is not None else []
        self.children = [v if isinstance(v, CPEConfiguration) else CPEConfiguration(**as_dict(v)) for v in self.children]

        if not isinstance(self.matches, list):
            self.matches = [self.matches] if self.matches is not None else []
        self.matches = [v if isinstance(v, CPEMatch) else CPEMatch(**as_dict(v)) for v in self.matches]

        if self.summary is not None and not isinstance(self.summary, str):
            self.summary = str(self.summary)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CPEMatch(YAMLRoot):
    """
    Leaf-level CPE match criterion and optional version bounds.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["CPEMatch"]
    class_class_curie: ClassVar[str] = "nvd:CPEMatch"
    class_name: ClassVar[str] = "CPEMatch"
    class_model_uri: ClassVar[URIRef] = NVD.CPEMatch

    match_criteria_id: Optional[str] = None
    criteria: Optional[str] = None
    cpe23_uri: Optional[str] = None
    vulnerable: Optional[Union[bool, Bool]] = None
    version_start_including: Optional[str] = None
    version_start_excluding: Optional[str] = None
    version_end_including: Optional[str] = None
    version_end_excluding: Optional[str] = None
    matched_cpe_names: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.match_criteria_id is not None and not isinstance(self.match_criteria_id, str):
            self.match_criteria_id = str(self.match_criteria_id)

        if self.criteria is not None and not isinstance(self.criteria, str):
            self.criteria = str(self.criteria)

        if self.cpe23_uri is not None and not isinstance(self.cpe23_uri, str):
            self.cpe23_uri = str(self.cpe23_uri)

        if self.vulnerable is not None and not isinstance(self.vulnerable, Bool):
            self.vulnerable = Bool(self.vulnerable)

        if self.version_start_including is not None and not isinstance(self.version_start_including, str):
            self.version_start_including = str(self.version_start_including)

        if self.version_start_excluding is not None and not isinstance(self.version_start_excluding, str):
            self.version_start_excluding = str(self.version_start_excluding)

        if self.version_end_including is not None and not isinstance(self.version_end_including, str):
            self.version_end_including = str(self.version_end_including)

        if self.version_end_excluding is not None and not isinstance(self.version_end_excluding, str):
            self.version_end_excluding = str(self.version_end_excluding)

        if not isinstance(self.matched_cpe_names, list):
            self.matched_cpe_names = [self.matched_cpe_names] if self.matched_cpe_names is not None else []
        self.matched_cpe_names = [v if isinstance(v, str) else str(v) for v in self.matched_cpe_names]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VendorComment(YAMLRoot):
    """
    Comment provided by vendor during NVD analysis.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["VendorComment"]
    class_class_curie: ClassVar[str] = "nvd:VendorComment"
    class_name: ClassVar[str] = "VendorComment"
    class_model_uri: ClassVar[URIRef] = NVD.VendorComment

    vendor: Optional[str] = None
    comment: Optional[str] = None
    last_modified_date: Optional[Union[str, XSDDateTime]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        if self.last_modified_date is not None and not isinstance(self.last_modified_date, XSDDateTime):
            self.last_modified_date = XSDDateTime(self.last_modified_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class KnownExploitedVulnerability(YAMLRoot):
    """
    CISA KEV information rendered on the NVD detail page.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["KnownExploitedVulnerability"]
    class_class_curie: ClassVar[str] = "nvd:KnownExploitedVulnerability"
    class_name: ClassVar[str] = "KnownExploitedVulnerability"
    class_model_uri: ClassVar[URIRef] = NVD.KnownExploitedVulnerability

    date_added: Optional[Union[str, XSDDate]] = None
    due_date: Optional[Union[str, XSDDate]] = None
    required_action: Optional[str] = None
    kev_reference: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.date_added is not None and not isinstance(self.date_added, XSDDate):
            self.date_added = XSDDate(self.date_added)

        if self.due_date is not None and not isinstance(self.due_date, XSDDate):
            self.due_date = XSDDate(self.due_date)

        if self.required_action is not None and not isinstance(self.required_action, str):
            self.required_action = str(self.required_action)

        if self.kev_reference is not None and not isinstance(self.kev_reference, URI):
            self.kev_reference = URI(self.kev_reference)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StatusTransition(YAMLRoot):
    """
    State transition event in NVD enrichment workflow.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["StatusTransition"]
    class_class_curie: ClassVar[str] = "nvd:StatusTransition"
    class_name: ClassVar[str] = "StatusTransition"
    class_model_uri: ClassVar[URIRef] = NVD.StatusTransition

    transition_id: Union[str, StatusTransitionTransitionId] = None
    from_status: Optional[Union[str, "NVDWorkflowStatus"]] = None
    to_status: Optional[Union[str, "NVDWorkflowStatus"]] = None
    event_source: Optional[Union[str, "NVDWorkflowEventSource"]] = None
    transition_time: Optional[Union[str, XSDDateTime]] = None
    rationale: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.transition_id):
            self.MissingRequiredField("transition_id")
        if not isinstance(self.transition_id, StatusTransitionTransitionId):
            self.transition_id = StatusTransitionTransitionId(self.transition_id)

        if self.from_status is not None and not isinstance(self.from_status, NVDWorkflowStatus):
            self.from_status = NVDWorkflowStatus(self.from_status)

        if self.to_status is not None and not isinstance(self.to_status, NVDWorkflowStatus):
            self.to_status = NVDWorkflowStatus(self.to_status)

        if self.event_source is not None and not isinstance(self.event_source, NVDWorkflowEventSource):
            self.event_source = NVDWorkflowEventSource(self.event_source)

        if self.transition_time is not None and not isinstance(self.transition_time, XSDDateTime):
            self.transition_time = XSDDateTime(self.transition_time)

        if self.rationale is not None and not isinstance(self.rationale, str):
            self.rationale = str(self.rationale)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Vulnerability(YAMLRoot):
    """
    Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Vulnerability"]
    class_class_curie: ClassVar[str] = "core:Vulnerability"
    class_name: ClassVar[str] = "Vulnerability"
    class_model_uri: ClassVar[URIRef] = NVD.Vulnerability

    cve_id: Union[str, VulnerabilityCveId] = None
    title: Optional[str] = None
    description: Optional[str] = None
    published_date: Optional[Union[str, XSDDateTime]] = None
    last_modified_date: Optional[Union[str, XSDDateTime]] = None
    products: Optional[Union[Union[dict, "Product"], list[Union[dict, "Product"]]]] = empty_list()
    weaknesses: Optional[Union[Union[dict, "Weakness"], list[Union[dict, "Weakness"]]]] = empty_list()
    references: Optional[Union[Union[dict, "Reference"], list[Union[dict, "Reference"]]]] = empty_list()
    impact: Optional[Union[dict, "Impact"]] = None
    status: Optional[Union[str, "VulnerabilityStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cve_id):
            self.MissingRequiredField("cve_id")
        if not isinstance(self.cve_id, VulnerabilityCveId):
            self.cve_id = VulnerabilityCveId(self.cve_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.published_date is not None and not isinstance(self.published_date, XSDDateTime):
            self.published_date = XSDDateTime(self.published_date)

        if self.last_modified_date is not None and not isinstance(self.last_modified_date, XSDDateTime):
            self.last_modified_date = XSDDateTime(self.last_modified_date)

        if not isinstance(self.products, list):
            self.products = [self.products] if self.products is not None else []
        self.products = [v if isinstance(v, Product) else Product(**as_dict(v)) for v in self.products]

        if not isinstance(self.weaknesses, list):
            self.weaknesses = [self.weaknesses] if self.weaknesses is not None else []
        self.weaknesses = [v if isinstance(v, Weakness) else Weakness(**as_dict(v)) for v in self.weaknesses]

        if not isinstance(self.references, list):
            self.references = [self.references] if self.references is not None else []
        self.references = [v if isinstance(v, Reference) else Reference(**as_dict(v)) for v in self.references]

        if self.impact is not None and not isinstance(self.impact, Impact):
            self.impact = Impact(**as_dict(self.impact))

        if self.status is not None and not isinstance(self.status, VulnerabilityStatus):
            self.status = VulnerabilityStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NVDEntry(Vulnerability):
    """
    Enriched NVD representation of a CVE entry.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["NVDEntry"]
    class_class_curie: ClassVar[str] = "nvd:NVDEntry"
    class_name: ClassVar[str] = "NVDEntry"
    class_model_uri: ClassVar[URIRef] = NVD.NVDEntry

    cve_id: Union[str, NVDEntryCveId] = None
    description: str = None
    description_source: Optional[str] = None
    analysis_description: Optional[str] = None
    metrics: Optional[Union[dict, MetricSet]] = None
    configurations: Optional[Union[Union[dict, CPEConfiguration], list[Union[dict, CPEConfiguration]]]] = empty_list()
    references: Optional[Union[Union[dict, "NVDReference"], list[Union[dict, "NVDReference"]]]] = empty_list()
    weaknesses: Optional[Union[Union[dict, "NVDWeakness"], list[Union[dict, "NVDWeakness"]]]] = empty_list()
    vendor_comments: Optional[Union[Union[dict, VendorComment], list[Union[dict, VendorComment]]]] = empty_list()
    nvd_tags: Optional[Union[Union[str, "NVDTag"], list[Union[str, "NVDTag"]]]] = empty_list()
    cve_tags: Optional[Union[str, list[str]]] = empty_list()
    workflow_status: Optional[Union[str, "NVDWorkflowStatus"]] = None
    status_transitions: Optional[Union[dict[Union[str, StatusTransitionTransitionId], Union[dict, StatusTransition]], list[Union[dict, StatusTransition]]]] = empty_dict()
    known_exploited: Optional[Union[dict, KnownExploitedVulnerability]] = None
    cwe_view: Optional[str] = None
    date_received: Optional[Union[str, XSDDateTime]] = None
    status: Optional[Union[str, "NVDWorkflowStatus"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cve_id):
            self.MissingRequiredField("cve_id")
        if not isinstance(self.cve_id, NVDEntryCveId):
            self.cve_id = NVDEntryCveId(self.cve_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self.description_source is not None and not isinstance(self.description_source, str):
            self.description_source = str(self.description_source)

        if self.analysis_description is not None and not isinstance(self.analysis_description, str):
            self.analysis_description = str(self.analysis_description)

        if self.metrics is not None and not isinstance(self.metrics, MetricSet):
            self.metrics = MetricSet(**as_dict(self.metrics))

        if not isinstance(self.configurations, list):
            self.configurations = [self.configurations] if self.configurations is not None else []
        self.configurations = [v if isinstance(v, CPEConfiguration) else CPEConfiguration(**as_dict(v)) for v in self.configurations]

        self._normalize_inlined_as_list(slot_name="references", slot_type=NVDReference, key_name="url", keyed=False)

        self._normalize_inlined_as_list(slot_name="weaknesses", slot_type=NVDWeakness, key_name="source", keyed=False)

        if not isinstance(self.vendor_comments, list):
            self.vendor_comments = [self.vendor_comments] if self.vendor_comments is not None else []
        self.vendor_comments = [v if isinstance(v, VendorComment) else VendorComment(**as_dict(v)) for v in self.vendor_comments]

        if not isinstance(self.nvd_tags, list):
            self.nvd_tags = [self.nvd_tags] if self.nvd_tags is not None else []
        self.nvd_tags = [v if isinstance(v, NVDTag) else NVDTag(v) for v in self.nvd_tags]

        if not isinstance(self.cve_tags, list):
            self.cve_tags = [self.cve_tags] if self.cve_tags is not None else []
        self.cve_tags = [v if isinstance(v, str) else str(v) for v in self.cve_tags]

        if self.workflow_status is not None and not isinstance(self.workflow_status, NVDWorkflowStatus):
            self.workflow_status = NVDWorkflowStatus(self.workflow_status)

        self._normalize_inlined_as_list(slot_name="status_transitions", slot_type=StatusTransition, key_name="transition_id", keyed=True)

        if self.known_exploited is not None and not isinstance(self.known_exploited, KnownExploitedVulnerability):
            self.known_exploited = KnownExploitedVulnerability(**as_dict(self.known_exploited))

        if self.cwe_view is not None and not isinstance(self.cwe_view, str):
            self.cwe_view = str(self.cwe_view)

        if self.date_received is not None and not isinstance(self.date_received, XSDDateTime):
            self.date_received = XSDDateTime(self.date_received)

        if self.status is not None and not isinstance(self.status, NVDWorkflowStatus):
            self.status = NVDWorkflowStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Product(YAMLRoot):
    """
    Software or hardware entity affected by the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Product"]
    class_class_curie: ClassVar[str] = "core:Product"
    class_name: ClassVar[str] = "Product"
    class_model_uri: ClassVar[URIRef] = NVD.Product

    vendor: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platforms: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.platforms, list):
            self.platforms = [self.platforms] if self.platforms is not None else []
        self.platforms = [v if isinstance(v, str) else str(v) for v in self.platforms]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reference(YAMLRoot):
    """
    External reference such as an advisory or article.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Reference"]
    class_class_curie: ClassVar[str] = "core:Reference"
    class_name: ClassVar[str] = "Reference"
    class_model_uri: ClassVar[URIRef] = NVD.Reference

    url: Optional[Union[str, URI]] = None
    name: Optional[str] = None
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NVDReference(Reference):
    """
    Reference URL with NVD resource tags.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["NVDReference"]
    class_class_curie: ClassVar[str] = "nvd:NVDReference"
    class_name: ClassVar[str] = "NVDReference"
    class_model_uri: ClassVar[URIRef] = NVD.NVDReference

    url: Union[str, URI] = None
    resource_tags: Optional[Union[Union[str, "ReferenceTag"], list[Union[str, "ReferenceTag"]]]] = empty_list()
    source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if not isinstance(self.resource_tags, list):
            self.resource_tags = [self.resource_tags] if self.resource_tags is not None else []
        self.resource_tags = [v if isinstance(v, ReferenceTag) else ReferenceTag(v) for v in self.resource_tags]

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Weakness(YAMLRoot):
    """
    Weakness classification from CWE or a similar taxonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Weakness"]
    class_class_curie: ClassVar[str] = "core:Weakness"
    class_name: ClassVar[str] = "Weakness"
    class_model_uri: ClassVar[URIRef] = NVD.Weakness

    cwe_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cwe_id is not None and not isinstance(self.cwe_id, str):
            self.cwe_id = str(self.cwe_id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NVDWeakness(Weakness):
    """
    Weakness row as presented on the NVD detail page.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NVD["NVDWeakness"]
    class_class_curie: ClassVar[str] = "nvd:NVDWeakness"
    class_name: ClassVar[str] = "NVDWeakness"
    class_model_uri: ClassVar[URIRef] = NVD.NVDWeakness

    source: str = None
    cwe_id: str = None
    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.cwe_id):
            self.MissingRequiredField("cwe_id")
        if not isinstance(self.cwe_id, str):
            self.cwe_id = str(self.cwe_id)

        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Impact(YAMLRoot):
    """
    Assessment of the vulnerability's impact and severity.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Impact"]
    class_class_curie: ClassVar[str] = "core:Impact"
    class_name: ClassVar[str] = "Impact"
    class_model_uri: ClassVar[URIRef] = NVD.Impact

    severity: Optional[Union[str, "ImpactSeverity"]] = None
    vector: Optional[str] = None
    score: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.severity is not None and not isinstance(self.severity, ImpactSeverity):
            self.severity = ImpactSeverity(self.severity)

        if self.vector is not None and not isinstance(self.vector, str):
            self.vector = str(self.vector)

        if self.score is not None and not isinstance(self.score, float):
            self.score = float(self.score)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Configuration(YAMLRoot):
    """
    Logical grouping of CPE match expressions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CORE["Configuration"]
    class_class_curie: ClassVar[str] = "core:Configuration"
    class_name: ClassVar[str] = "Configuration"
    class_model_uri: ClassVar[URIRef] = NVD.Configuration

    cpe_uri: Optional[str] = None
    operator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpe_uri is not None and not isinstance(self.cpe_uri, str):
            self.cpe_uri = str(self.cpe_uri)

        if self.operator is not None and not isinstance(self.operator, str):
            self.operator = str(self.operator)

        super().__post_init__(**kwargs)

# Slots
class slots:
    pass

slots.description_source = Slot(uri=DCT.source, name="description_source", curie=DCT.curie('source'),
                   model_uri=NVD.description_source, domain=None, range=Optional[str])

slots.analysis_description = Slot(uri=DCT.description, name="analysis_description", curie=DCT.curie('description'),
                   model_uri=NVD.analysis_description, domain=None, range=Optional[str])

slots.metrics = Slot(uri=NVD.metrics, name="metrics", curie=NVD.curie('metrics'),
                   model_uri=NVD.metrics, domain=None, range=Optional[Union[dict, MetricSet]])

slots.configurations = Slot(uri=NVD.configurations, name="configurations", curie=NVD.curie('configurations'),
                   model_uri=NVD.configurations, domain=None, range=Optional[Union[Union[dict, CPEConfiguration], list[Union[dict, CPEConfiguration]]]])

slots.workflow_status = Slot(uri=NVD.workflow_status, name="workflow_status", curie=NVD.curie('workflow_status'),
                   model_uri=NVD.workflow_status, domain=None, range=Optional[Union[str, "NVDWorkflowStatus"]])

slots.status_transitions = Slot(uri=NVD.status_transitions, name="status_transitions", curie=NVD.curie('status_transitions'),
                   model_uri=NVD.status_transitions, domain=None, range=Optional[Union[dict[Union[str, StatusTransitionTransitionId], Union[dict, StatusTransition]], list[Union[dict, StatusTransition]]]])

slots.known_exploited = Slot(uri=NVD.known_exploited, name="known_exploited", curie=NVD.curie('known_exploited'),
                   model_uri=NVD.known_exploited, domain=None, range=Optional[Union[dict, KnownExploitedVulnerability]])

slots.cve_tags = Slot(uri=NVD.cve_tags, name="cve_tags", curie=NVD.curie('cve_tags'),
                   model_uri=NVD.cve_tags, domain=None, range=Optional[Union[str, list[str]]])

slots.cwe_view = Slot(uri=NVD.cwe_view, name="cwe_view", curie=NVD.curie('cwe_view'),
                   model_uri=NVD.cwe_view, domain=None, range=Optional[str])

slots.date_received = Slot(uri=NVD.date_received, name="date_received", curie=NVD.curie('date_received'),
                   model_uri=NVD.date_received, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.cvss_v4_metrics = Slot(uri=NVD.cvss_v4_metrics, name="cvss_v4_metrics", curie=NVD.curie('cvss_v4_metrics'),
                   model_uri=NVD.cvss_v4_metrics, domain=None, range=Optional[Union[Union[dict, CVSSMetric], list[Union[dict, CVSSMetric]]]])

slots.cvss_v3_metrics = Slot(uri=NVD.cvss_v3_metrics, name="cvss_v3_metrics", curie=NVD.curie('cvss_v3_metrics'),
                   model_uri=NVD.cvss_v3_metrics, domain=None, range=Optional[Union[Union[dict, CVSSMetric], list[Union[dict, CVSSMetric]]]])

slots.cvss_v2_metrics = Slot(uri=NVD.cvss_v2_metrics, name="cvss_v2_metrics", curie=NVD.curie('cvss_v2_metrics'),
                   model_uri=NVD.cvss_v2_metrics, domain=None, range=Optional[Union[Union[dict, CVSSMetric], list[Union[dict, CVSSMetric]]]])

slots.score_notes = Slot(uri=NVD.score_notes, name="score_notes", curie=NVD.curie('score_notes'),
                   model_uri=NVD.score_notes, domain=None, range=Optional[Union[dict[Union[str, CVSSScoreNoteNoteId], Union[dict, CVSSScoreNote]], list[Union[dict, CVSSScoreNote]]]])

slots.note_id = Slot(uri=DCT.identifier, name="note_id", curie=DCT.curie('identifier'),
                   model_uri=NVD.note_id, domain=None, range=URIRef)

slots.message = Slot(uri=NVD.message, name="message", curie=NVD.curie('message'),
                   model_uri=NVD.message, domain=None, range=Optional[str])

slots.created = Slot(uri=DCT.created, name="created", curie=DCT.curie('created'),
                   model_uri=NVD.created, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.provider_label = Slot(uri=NVD.provider_label, name="provider_label", curie=NVD.curie('provider_label'),
                   model_uri=NVD.provider_label, domain=None, range=Optional[str])

slots.scoring_justification = Slot(uri=NVD.scoring_justification, name="scoring_justification", curie=NVD.curie('scoring_justification'),
                   model_uri=NVD.scoring_justification, domain=None, range=Optional[str])

slots.configuration_id = Slot(uri=NVD.configuration_id, name="configuration_id", curie=NVD.curie('configuration_id'),
                   model_uri=NVD.configuration_id, domain=None, range=Optional[str])

slots.configuration_type = Slot(uri=NVD.configuration_type, name="configuration_type", curie=NVD.curie('configuration_type'),
                   model_uri=NVD.configuration_type, domain=None, range=Optional[Union[str, "ConfigurationType"]])

slots.summary = Slot(uri=NVD.summary, name="summary", curie=NVD.curie('summary'),
                   model_uri=NVD.summary, domain=None, range=Optional[str])

slots.match_criteria_id = Slot(uri=NVD.match_criteria_id, name="match_criteria_id", curie=NVD.curie('match_criteria_id'),
                   model_uri=NVD.match_criteria_id, domain=None, range=Optional[str])

slots.criteria = Slot(uri=NVD.criteria, name="criteria", curie=NVD.curie('criteria'),
                   model_uri=NVD.criteria, domain=None, range=Optional[str])

slots.cpe23_uri = Slot(uri=NVD.cpe23_uri, name="cpe23_uri", curie=NVD.curie('cpe23_uri'),
                   model_uri=NVD.cpe23_uri, domain=None, range=Optional[str])

slots.version_start_including = Slot(uri=NVD.version_start_including, name="version_start_including", curie=NVD.curie('version_start_including'),
                   model_uri=NVD.version_start_including, domain=None, range=Optional[str])

slots.version_start_excluding = Slot(uri=NVD.version_start_excluding, name="version_start_excluding", curie=NVD.curie('version_start_excluding'),
                   model_uri=NVD.version_start_excluding, domain=None, range=Optional[str])

slots.version_end_including = Slot(uri=NVD.version_end_including, name="version_end_including", curie=NVD.curie('version_end_including'),
                   model_uri=NVD.version_end_including, domain=None, range=Optional[str])

slots.version_end_excluding = Slot(uri=NVD.version_end_excluding, name="version_end_excluding", curie=NVD.curie('version_end_excluding'),
                   model_uri=NVD.version_end_excluding, domain=None, range=Optional[str])

slots.matched_cpe_names = Slot(uri=NVD.matched_cpe_names, name="matched_cpe_names", curie=NVD.curie('matched_cpe_names'),
                   model_uri=NVD.matched_cpe_names, domain=None, range=Optional[Union[str, list[str]]])

slots.nvd_tags = Slot(uri=NVD.nvd_tags, name="nvd_tags", curie=NVD.curie('nvd_tags'),
                   model_uri=NVD.nvd_tags, domain=None, range=Optional[Union[Union[str, "NVDTag"], list[Union[str, "NVDTag"]]]])

slots.vendor_comments = Slot(uri=NVD.vendor_comments, name="vendor_comments", curie=NVD.curie('vendor_comments'),
                   model_uri=NVD.vendor_comments, domain=None, range=Optional[Union[Union[dict, VendorComment], list[Union[dict, VendorComment]]]])

slots.resource_tags = Slot(uri=NVD.resource_tags, name="resource_tags", curie=NVD.curie('resource_tags'),
                   model_uri=NVD.resource_tags, domain=None, range=Optional[Union[Union[str, "ReferenceTag"], list[Union[str, "ReferenceTag"]]]])

slots.vector_string = Slot(uri=NVD.vector_string, name="vector_string", curie=NVD.curie('vector_string'),
                   model_uri=NVD.vector_string, domain=None, range=Optional[str])

slots.base_score = Slot(uri=NVD.base_score, name="base_score", curie=NVD.curie('base_score'),
                   model_uri=NVD.base_score, domain=None, range=Optional[float])

slots.base_severity = Slot(uri=NVD.base_severity, name="base_severity", curie=NVD.curie('base_severity'),
                   model_uri=NVD.base_severity, domain=None, range=Optional[Union[str, "ImpactSeverity"]])

slots.children = Slot(uri=NVD.children, name="children", curie=NVD.curie('children'),
                   model_uri=NVD.children, domain=None, range=Optional[Union[Union[dict, CPEConfiguration], list[Union[dict, CPEConfiguration]]]])

slots.matches = Slot(uri=NVD.matches, name="matches", curie=NVD.curie('matches'),
                   model_uri=NVD.matches, domain=None, range=Optional[Union[Union[dict, CPEMatch], list[Union[dict, CPEMatch]]]])

slots.vulnerable = Slot(uri=NVD.vulnerable, name="vulnerable", curie=NVD.curie('vulnerable'),
                   model_uri=NVD.vulnerable, domain=None, range=Optional[Union[bool, Bool]])

slots.date_added = Slot(uri=DCT.created, name="date_added", curie=DCT.curie('created'),
                   model_uri=NVD.date_added, domain=None, range=Optional[Union[str, XSDDate]])

slots.due_date = Slot(uri=DCT.date, name="due_date", curie=DCT.curie('date'),
                   model_uri=NVD.due_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.required_action = Slot(uri=DCT.description, name="required_action", curie=DCT.curie('description'),
                   model_uri=NVD.required_action, domain=None, range=Optional[str])

slots.kev_reference = Slot(uri=SCHEMA.url, name="kev_reference", curie=SCHEMA.curie('url'),
                   model_uri=NVD.kev_reference, domain=None, range=Optional[Union[str, URI]])

slots.transition_id = Slot(uri=DCT.identifier, name="transition_id", curie=DCT.curie('identifier'),
                   model_uri=NVD.transition_id, domain=None, range=URIRef)

slots.from_status = Slot(uri=NVD.from_status, name="from_status", curie=NVD.curie('from_status'),
                   model_uri=NVD.from_status, domain=None, range=Optional[Union[str, "NVDWorkflowStatus"]])

slots.to_status = Slot(uri=NVD.to_status, name="to_status", curie=NVD.curie('to_status'),
                   model_uri=NVD.to_status, domain=None, range=Optional[Union[str, "NVDWorkflowStatus"]])

slots.event_source = Slot(uri=NVD.event_source, name="event_source", curie=NVD.curie('event_source'),
                   model_uri=NVD.event_source, domain=None, range=Optional[Union[str, "NVDWorkflowEventSource"]])

slots.transition_time = Slot(uri=DCT.modified, name="transition_time", curie=DCT.curie('modified'),
                   model_uri=NVD.transition_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.rationale = Slot(uri=NVD.rationale, name="rationale", curie=NVD.curie('rationale'),
                   model_uri=NVD.rationale, domain=None, range=Optional[str])

slots.comment = Slot(uri=NVD.comment, name="comment", curie=NVD.curie('comment'),
                   model_uri=NVD.comment, domain=None, range=Optional[str])

slots.cve_id = Slot(uri=DCTERMS.identifier, name="cve_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NVD.cve_id, domain=None, range=URIRef)

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=NVD.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NVD.description, domain=None, range=Optional[str])

slots.published_date = Slot(uri=DCTERMS.created, name="published_date", curie=DCTERMS.curie('created'),
                   model_uri=NVD.published_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.last_modified_date = Slot(uri=DCTERMS.modified, name="last_modified_date", curie=DCTERMS.curie('modified'),
                   model_uri=NVD.last_modified_date, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.products = Slot(uri=CORE.products, name="products", curie=CORE.curie('products'),
                   model_uri=NVD.products, domain=None, range=Optional[Union[Union[dict, Product], list[Union[dict, Product]]]])

slots.weaknesses = Slot(uri=CORE.weaknesses, name="weaknesses", curie=CORE.curie('weaknesses'),
                   model_uri=NVD.weaknesses, domain=None, range=Optional[Union[Union[dict, Weakness], list[Union[dict, Weakness]]]])

slots.references = Slot(uri=CORE.references, name="references", curie=CORE.curie('references'),
                   model_uri=NVD.references, domain=None, range=Optional[Union[Union[dict, Reference], list[Union[dict, Reference]]]])

slots.impact = Slot(uri=CORE.impact, name="impact", curie=CORE.curie('impact'),
                   model_uri=NVD.impact, domain=None, range=Optional[Union[dict, Impact]])

slots.status = Slot(uri=CORE.status, name="status", curie=CORE.curie('status'),
                   model_uri=NVD.status, domain=None, range=Optional[Union[str, "VulnerabilityStatus"]])

slots.vendor = Slot(uri=SCHEMA.name, name="vendor", curie=SCHEMA.curie('name'),
                   model_uri=NVD.vendor, domain=None, range=Optional[str])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=NVD.name, domain=None, range=Optional[str])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=NVD.version, domain=None, range=Optional[str])

slots.platforms = Slot(uri=CORE.platforms, name="platforms", curie=CORE.curie('platforms'),
                   model_uri=NVD.platforms, domain=None, range=Optional[Union[str, list[str]]])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=NVD.url, domain=None, range=Optional[Union[str, URI]])

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=NVD.source, domain=None, range=Optional[str])

slots.cwe_id = Slot(uri=DCTERMS.identifier, name="cwe_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NVD.cwe_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^CWE-[1-9][0-9]*$'))

slots.severity = Slot(uri=CORE.severity, name="severity", curie=CORE.curie('severity'),
                   model_uri=NVD.severity, domain=None, range=Optional[Union[str, "ImpactSeverity"]])

slots.vector = Slot(uri=CORE.vector, name="vector", curie=CORE.curie('vector'),
                   model_uri=NVD.vector, domain=None, range=Optional[str])

slots.score = Slot(uri=CORE.score, name="score", curie=CORE.curie('score'),
                   model_uri=NVD.score, domain=None, range=Optional[float])

slots.cpe_uri = Slot(uri=CORE.cpe_uri, name="cpe_uri", curie=CORE.curie('cpe_uri'),
                   model_uri=NVD.cpe_uri, domain=None, range=Optional[str])

slots.operator = Slot(uri=CORE.operator, name="operator", curie=CORE.curie('operator'),
                   model_uri=NVD.operator, domain=None, range=Optional[str])

slots.NVDEntry_references = Slot(uri=CORE.references, name="NVDEntry_references", curie=CORE.curie('references'),
                   model_uri=NVD.NVDEntry_references, domain=NVDEntry, range=Optional[Union[Union[dict, "NVDReference"], list[Union[dict, "NVDReference"]]]])

slots.NVDEntry_weaknesses = Slot(uri=CORE.weaknesses, name="NVDEntry_weaknesses", curie=CORE.curie('weaknesses'),
                   model_uri=NVD.NVDEntry_weaknesses, domain=NVDEntry, range=Optional[Union[Union[dict, "NVDWeakness"], list[Union[dict, "NVDWeakness"]]]])

slots.NVDEntry_status = Slot(uri=CORE.status, name="NVDEntry_status", curie=CORE.curie('status'),
                   model_uri=NVD.NVDEntry_status, domain=NVDEntry, range=Optional[Union[str, "NVDWorkflowStatus"]])

slots.NVDEntry_description = Slot(uri=DCTERMS.description, name="NVDEntry_description", curie=DCTERMS.curie('description'),
                   model_uri=NVD.NVDEntry_description, domain=NVDEntry, range=str)

slots.CVSSMetric_source = Slot(uri=DCTERMS.source, name="CVSSMetric_source", curie=DCTERMS.curie('source'),
                   model_uri=NVD.CVSSMetric_source, domain=CVSSMetric, range=Optional[Union[str, "ScoreSource"]])

slots.NVDReference_url = Slot(uri=SCHEMA.url, name="NVDReference_url", curie=SCHEMA.curie('url'),
                   model_uri=NVD.NVDReference_url, domain=NVDReference, range=Union[str, URI])

slots.NVDReference_source = Slot(uri=DCTERMS.source, name="NVDReference_source", curie=DCTERMS.curie('source'),
                   model_uri=NVD.NVDReference_source, domain=NVDReference, range=Optional[str])

slots.NVDWeakness_cwe_id = Slot(uri=DCTERMS.identifier, name="NVDWeakness_cwe_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NVD.NVDWeakness_cwe_id, domain=NVDWeakness, range=str,
                   pattern=re.compile(r'^CWE-[1-9][0-9]*$'))

slots.NVDWeakness_name = Slot(uri=RDFS.label, name="NVDWeakness_name", curie=RDFS.curie('label'),
                   model_uri=NVD.NVDWeakness_name, domain=NVDWeakness, range=str)

slots.NVDWeakness_source = Slot(uri=DCTERMS.source, name="NVDWeakness_source", curie=DCTERMS.curie('source'),
                   model_uri=NVD.NVDWeakness_source, domain=NVDWeakness, range=str)

slots.Vulnerability_cve_id = Slot(uri=DCTERMS.identifier, name="Vulnerability_cve_id", curie=DCTERMS.curie('identifier'),
                   model_uri=NVD.Vulnerability_cve_id, domain=Vulnerability, range=Union[str, VulnerabilityCveId])

slots.Vulnerability_description = Slot(uri=DCTERMS.description, name="Vulnerability_description", curie=DCTERMS.curie('description'),
                   model_uri=NVD.Vulnerability_description, domain=Vulnerability, range=Optional[str])
