# Auto generated from nist_nvd.yaml by pythongen.py version: 0.0.1
# Schema: nist_nvd
#
# id: https://w3id.org/lmodel/nist-nvd
# description: A LinkML model of the JSON responses of the NVD API 2.0, from the JSON schemas NIST publishes: vulnerabilities, products, match strings and change history. NVD's own keys are the schema's keys, so a real response validates unchanged.
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

from linkml_runtime.linkml_model.types import Boolean, Date, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

metamodel_version = "1.12.0"
version = "2.2.4"

# Namespaces
CVE = CurieNamespace('cve', 'https://w3id.org/lmodel/cve/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
KEV_CATALOG = CurieNamespace('kev_catalog', 'https://w3id.org/lmodel/kev-catalog/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_NVD = CurieNamespace('nist_nvd', 'https://w3id.org/lmodel/nist-nvd/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SEPSES_CPE = CurieNamespace('sepses_cpe', 'http://w3id.org/sepses/vocab/ref/cpe#')
SEPSES_CVE = CurieNamespace('sepses_cve', 'http://w3id.org/sepses/vocab/ref/cve#')
SEPSES_CVSS = CurieNamespace('sepses_cvss', 'http://w3id.org/sepses/vocab/ref/cvss#')
SPDX3 = CurieNamespace('spdx3', 'https://spdx.org/rdf/3.0.1/terms/')
SPDX_SECURITY = CurieNamespace('spdx_security', 'https://spdx.org/rdf/3.0.1/terms/Security/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
WD = CurieNamespace('wd', 'http://www.wikidata.org/entity/')
WDT = CurieNamespace('wdt', 'http://www.wikidata.org/prop/direct/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_NVD


# Types
class NvdTimestamp(String):
    """ A date and time as NVD writes it: ISO 8601, with fractional seconds and a UTC offset where the writer gives them. """
    type_class_uri = XSD["dateTime"]
    type_class_curie = "xsd:dateTime"
    type_name = "nvd_timestamp"
    type_model_uri = NIST_NVD.NvdTimestamp


class NvdUuid(String):
    """ A UUID in its usual hexadecimal form with four hyphens. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "nvd_uuid"
    type_model_uri = NIST_NVD.NvdUuid


class NvdCveIdentifier(String):
    """ A CVE identifier, such as CVE-2021-44228. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "nvd_cve_identifier"
    type_model_uri = NIST_NVD.NvdCveIdentifier


# Class references
class NvdCveId(NvdCveIdentifier):
    pass


class NvdCpeCpeNameId(NvdUuid):
    pass


class NvdMatchStringMatchCriteriaId(NvdUuid):
    pass


class NvdChangeCveChangeId(NvdUuid):
    pass


@dataclass(repr=False)
class NvdResponseMixin(YAMLRoot):
    """
    The fields of a page of results, which every NVD API response carries.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdResponseMixin"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdResponseMixin"
    class_name: ClassVar[str] = "NvdResponseMixin"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdResponseMixin

    format: str = None
    timestamp: Union[str, NvdTimestamp] = None
    resultsPerPage: int = None
    startIndex: int = None
    totalResults: int = None
    version: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self._is_empty(self.resultsPerPage):
            self.MissingRequiredField("resultsPerPage")
        if not isinstance(self.resultsPerPage, int):
            self.resultsPerPage = int(self.resultsPerPage)

        if self._is_empty(self.startIndex):
            self.MissingRequiredField("startIndex")
        if not isinstance(self.startIndex, int):
            self.startIndex = int(self.startIndex)

        if self._is_empty(self.totalResults):
            self.MissingRequiredField("totalResults")
        if not isinstance(self.totalResults, int):
            self.totalResults = int(self.totalResults)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCveResponse(YAMLRoot):
    """
    A page of the vulnerability API's results, or a whole data feed.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCveResponse"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCveResponse"
    class_name: ClassVar[str] = "NvdCveResponse"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCveResponse

    vulnerabilities: Union[Union[dict, "NvdVulnerability"], list[Union[dict, "NvdVulnerability"]]] = None
    format: str = None
    timestamp: Union[str, NvdTimestamp] = None
    resultsPerPage: int = None
    startIndex: int = None
    totalResults: int = None
    version: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.vulnerabilities):
            self.MissingRequiredField("vulnerabilities")
        if not isinstance(self.vulnerabilities, list):
            self.vulnerabilities = [self.vulnerabilities] if self.vulnerabilities is not None else []
        self.vulnerabilities = [v if isinstance(v, NvdVulnerability) else NvdVulnerability(**as_dict(v)) for v in self.vulnerabilities]

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self._is_empty(self.resultsPerPage):
            self.MissingRequiredField("resultsPerPage")
        if not isinstance(self.resultsPerPage, int):
            self.resultsPerPage = int(self.resultsPerPage)

        if self._is_empty(self.startIndex):
            self.MissingRequiredField("startIndex")
        if not isinstance(self.startIndex, int):
            self.startIndex = int(self.startIndex)

        if self._is_empty(self.totalResults):
            self.MissingRequiredField("totalResults")
        if not isinstance(self.totalResults, int):
            self.totalResults = int(self.totalResults)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdVulnerability(YAMLRoot):
    """
    One entry of a response, which only wraps the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdVulnerability"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdVulnerability"
    class_name: ClassVar[str] = "NvdVulnerability"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdVulnerability

    cve: Union[dict, "NvdCve"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cve):
            self.MissingRequiredField("cve")
        if not isinstance(self.cve, NvdCve):
            self.cve = NvdCve(**as_dict(self.cve))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCve(YAMLRoot):
    """
    A vulnerability as NVD holds it, under its CVE identifier.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCve"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCve"
    class_name: ClassVar[str] = "NvdCve"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCve

    id: Union[str, NvdCveId] = None
    lastModified: Union[str, NvdTimestamp] = None
    references: Union[Union[dict, "NvdReference"], list[Union[dict, "NvdReference"]]] = None
    published: Union[str, NvdTimestamp] = None
    descriptions: Union[Union[dict, "NvdLangString"], list[Union[dict, "NvdLangString"]]] = None
    sourceIdentifier: Optional[str] = None
    vulnStatus: Optional[Union[str, "NvdVulnStatus"]] = None
    evaluatorComment: Optional[str] = None
    evaluatorSolution: Optional[str] = None
    evaluatorImpact: Optional[str] = None
    cisaExploitAdd: Optional[Union[str, XSDDate]] = None
    cisaActionDue: Optional[Union[str, XSDDate]] = None
    cisaRequiredAction: Optional[str] = None
    cisaVulnerabilityName: Optional[str] = None
    cveTags: Optional[Union[Union[dict, "NvdCveTag"], list[Union[dict, "NvdCveTag"]]]] = empty_list()
    metrics: Optional[Union[dict, "NvdMetrics"]] = None
    affected: Optional[Union[Union[dict, "NvdAffected"], list[Union[dict, "NvdAffected"]]]] = empty_list()
    weaknesses: Optional[Union[Union[dict, "NvdWeakness"], list[Union[dict, "NvdWeakness"]]]] = empty_list()
    configurations: Optional[Union[Union[dict, "NvdConfiguration"], list[Union[dict, "NvdConfiguration"]]]] = empty_list()
    vendorComments: Optional[Union[Union[dict, "NvdVendorComment"], list[Union[dict, "NvdVendorComment"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NvdCveId):
            self.id = NvdCveId(self.id)

        if self._is_empty(self.lastModified):
            self.MissingRequiredField("lastModified")
        if not isinstance(self.lastModified, NvdTimestamp):
            self.lastModified = NvdTimestamp(self.lastModified)

        if self._is_empty(self.references):
            self.MissingRequiredField("references")
        self._normalize_inlined_as_list(slot_name="references", slot_type=NvdReference, key_name="url", keyed=False)

        if self._is_empty(self.published):
            self.MissingRequiredField("published")
        if not isinstance(self.published, NvdTimestamp):
            self.published = NvdTimestamp(self.published)

        if self._is_empty(self.descriptions):
            self.MissingRequiredField("descriptions")
        self._normalize_inlined_as_list(slot_name="descriptions", slot_type=NvdLangString, key_name="lang", keyed=False)

        if self.sourceIdentifier is not None and not isinstance(self.sourceIdentifier, str):
            self.sourceIdentifier = str(self.sourceIdentifier)

        if self.vulnStatus is not None and not isinstance(self.vulnStatus, NvdVulnStatus):
            self.vulnStatus = NvdVulnStatus(self.vulnStatus)

        if self.evaluatorComment is not None and not isinstance(self.evaluatorComment, str):
            self.evaluatorComment = str(self.evaluatorComment)

        if self.evaluatorSolution is not None and not isinstance(self.evaluatorSolution, str):
            self.evaluatorSolution = str(self.evaluatorSolution)

        if self.evaluatorImpact is not None and not isinstance(self.evaluatorImpact, str):
            self.evaluatorImpact = str(self.evaluatorImpact)

        if self.cisaExploitAdd is not None and not isinstance(self.cisaExploitAdd, XSDDate):
            self.cisaExploitAdd = XSDDate(self.cisaExploitAdd)

        if self.cisaActionDue is not None and not isinstance(self.cisaActionDue, XSDDate):
            self.cisaActionDue = XSDDate(self.cisaActionDue)

        if self.cisaRequiredAction is not None and not isinstance(self.cisaRequiredAction, str):
            self.cisaRequiredAction = str(self.cisaRequiredAction)

        if self.cisaVulnerabilityName is not None and not isinstance(self.cisaVulnerabilityName, str):
            self.cisaVulnerabilityName = str(self.cisaVulnerabilityName)

        if not isinstance(self.cveTags, list):
            self.cveTags = [self.cveTags] if self.cveTags is not None else []
        self.cveTags = [v if isinstance(v, NvdCveTag) else NvdCveTag(**as_dict(v)) for v in self.cveTags]

        if self.metrics is not None and not isinstance(self.metrics, NvdMetrics):
            self.metrics = NvdMetrics(**as_dict(self.metrics))

        self._normalize_inlined_as_list(slot_name="affected", slot_type=NvdAffected, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="weaknesses", slot_type=NvdWeakness, key_name="source", keyed=False)

        if not isinstance(self.configurations, list):
            self.configurations = [self.configurations] if self.configurations is not None else []
        self.configurations = [v if isinstance(v, NvdConfiguration) else NvdConfiguration(**as_dict(v)) for v in self.configurations]

        self._normalize_inlined_as_list(slot_name="vendorComments", slot_type=NvdVendorComment, key_name="lastModified", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCveTag(YAMLRoot):
    """
    The labels that one source puts on a record.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCveTag"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCveTag"
    class_name: ClassVar[str] = "NvdCveTag"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCveTag

    sourceIdentifier: Optional[str] = None
    tags: Optional[Union[Union[str, "NvdCveTagName"], list[Union[str, "NvdCveTagName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.sourceIdentifier is not None and not isinstance(self.sourceIdentifier, str):
            self.sourceIdentifier = str(self.sourceIdentifier)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, NvdCveTagName) else NvdCveTagName(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdLangString(YAMLRoot):
    """
    A piece of text and the language it is in.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdLangString"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdLangString"
    class_name: ClassVar[str] = "NvdLangString"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdLangString

    lang: str = None
    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdReference(YAMLRoot):
    """
    A page about a vulnerability, with NVD's labels for what it is.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdReference"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdReference"
    class_name: ClassVar[str] = "NvdReference"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdReference

    url: Union[str, URI] = None
    source: Optional[str] = None
    tags: Optional[Union[Union[str, "NvdReferenceTag"], list[Union[str, "NvdReferenceTag"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.url):
            self.MissingRequiredField("url")
        if not isinstance(self.url, URI):
            self.url = URI(self.url)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if not isinstance(self.tags, list):
            self.tags = [self.tags] if self.tags is not None else []
        self.tags = [v if isinstance(v, NvdReferenceTag) else NvdReferenceTag(v) for v in self.tags]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdMetrics(YAMLRoot):
    """
    The scores of a vulnerability, in a list per scoring system and version.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdMetrics"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdMetrics"
    class_name: ClassVar[str] = "NvdMetrics"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdMetrics

    cvssMetricV40: Optional[Union[Union[dict, "NvdCvssMetricV40"], list[Union[dict, "NvdCvssMetricV40"]]]] = empty_list()
    cvssMetricV31: Optional[Union[Union[dict, "NvdCvssMetricV31"], list[Union[dict, "NvdCvssMetricV31"]]]] = empty_list()
    cvssMetricV30: Optional[Union[Union[dict, "NvdCvssMetricV30"], list[Union[dict, "NvdCvssMetricV30"]]]] = empty_list()
    cvssMetricV2: Optional[Union[Union[dict, "NvdCvssMetricV2"], list[Union[dict, "NvdCvssMetricV2"]]]] = empty_list()
    ssvcV203: Optional[Union[Union[dict, "NvdSsvcMetricV203"], list[Union[dict, "NvdSsvcMetricV203"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="cvssMetricV40", slot_type=NvdCvssMetricV40, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="cvssMetricV31", slot_type=NvdCvssMetricV31, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="cvssMetricV30", slot_type=NvdCvssMetricV30, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="cvssMetricV2", slot_type=NvdCvssMetricV2, key_name="source", keyed=False)

        self._normalize_inlined_as_list(slot_name="ssvcV203", slot_type=NvdSsvcMetricV203, key_name="source", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCvssMetricV2(YAMLRoot):
    """
    A CVSS 2.0 score, who gave it, and NVD's figures beside it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCvssMetricV2"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCvssMetricV2"
    class_name: ClassVar[str] = "NvdCvssMetricV2"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCvssMetricV2

    source: str = None
    type: Union[str, "NvdSourceType"] = None
    cvssData: Union[dict, "CvssV20"] = None
    exploitabilityScore: Optional[float] = None
    impactScore: Optional[float] = None
    baseSeverity: Optional[Union[str, "NvdCvssV2Severity"]] = None
    acInsufInfo: Optional[Union[bool, Bool]] = None
    obtainAllPrivilege: Optional[Union[bool, Bool]] = None
    obtainUserPrivilege: Optional[Union[bool, Bool]] = None
    obtainOtherPrivilege: Optional[Union[bool, Bool]] = None
    userInteractionRequired: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NvdSourceType):
            self.type = NvdSourceType(self.type)

        if self._is_empty(self.cvssData):
            self.MissingRequiredField("cvssData")
        if not isinstance(self.cvssData, CvssV20):
            self.cvssData = CvssV20(**as_dict(self.cvssData))

        if self.exploitabilityScore is not None and not isinstance(self.exploitabilityScore, float):
            self.exploitabilityScore = float(self.exploitabilityScore)

        if self.impactScore is not None and not isinstance(self.impactScore, float):
            self.impactScore = float(self.impactScore)

        if self.baseSeverity is not None and not isinstance(self.baseSeverity, NvdCvssV2Severity):
            self.baseSeverity = NvdCvssV2Severity(self.baseSeverity)

        if self.acInsufInfo is not None and not isinstance(self.acInsufInfo, Bool):
            self.acInsufInfo = Bool(self.acInsufInfo)

        if self.obtainAllPrivilege is not None and not isinstance(self.obtainAllPrivilege, Bool):
            self.obtainAllPrivilege = Bool(self.obtainAllPrivilege)

        if self.obtainUserPrivilege is not None and not isinstance(self.obtainUserPrivilege, Bool):
            self.obtainUserPrivilege = Bool(self.obtainUserPrivilege)

        if self.obtainOtherPrivilege is not None and not isinstance(self.obtainOtherPrivilege, Bool):
            self.obtainOtherPrivilege = Bool(self.obtainOtherPrivilege)

        if self.userInteractionRequired is not None and not isinstance(self.userInteractionRequired, Bool):
            self.userInteractionRequired = Bool(self.userInteractionRequired)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCvssMetricV30(YAMLRoot):
    """
    A CVSS 3.0 score, who gave it, and its subscores.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCvssMetricV30"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCvssMetricV30"
    class_name: ClassVar[str] = "NvdCvssMetricV30"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCvssMetricV30

    source: str = None
    type: Union[str, "NvdSourceType"] = None
    cvssData: Union[dict, "CvssV30"] = None
    exploitabilityScore: Optional[float] = None
    impactScore: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NvdSourceType):
            self.type = NvdSourceType(self.type)

        if self._is_empty(self.cvssData):
            self.MissingRequiredField("cvssData")
        if not isinstance(self.cvssData, CvssV30):
            self.cvssData = CvssV30(**as_dict(self.cvssData))

        if self.exploitabilityScore is not None and not isinstance(self.exploitabilityScore, float):
            self.exploitabilityScore = float(self.exploitabilityScore)

        if self.impactScore is not None and not isinstance(self.impactScore, float):
            self.impactScore = float(self.impactScore)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCvssMetricV31(YAMLRoot):
    """
    A CVSS 3.1 score, who gave it, and its subscores.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCvssMetricV31"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCvssMetricV31"
    class_name: ClassVar[str] = "NvdCvssMetricV31"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCvssMetricV31

    source: str = None
    type: Union[str, "NvdSourceType"] = None
    cvssData: Union[dict, "CvssV31"] = None
    exploitabilityScore: Optional[float] = None
    impactScore: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NvdSourceType):
            self.type = NvdSourceType(self.type)

        if self._is_empty(self.cvssData):
            self.MissingRequiredField("cvssData")
        if not isinstance(self.cvssData, CvssV31):
            self.cvssData = CvssV31(**as_dict(self.cvssData))

        if self.exploitabilityScore is not None and not isinstance(self.exploitabilityScore, float):
            self.exploitabilityScore = float(self.exploitabilityScore)

        if self.impactScore is not None and not isinstance(self.impactScore, float):
            self.impactScore = float(self.impactScore)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCvssMetricV40(YAMLRoot):
    """
    A CVSS 4.0 score and who gave it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCvssMetricV40"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCvssMetricV40"
    class_name: ClassVar[str] = "NvdCvssMetricV40"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCvssMetricV40

    source: str = None
    type: Union[str, "NvdSourceType"] = None
    cvssData: Union[dict, "CvssV40"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NvdSourceType):
            self.type = NvdSourceType(self.type)

        if self._is_empty(self.cvssData):
            self.MissingRequiredField("cvssData")
        if not isinstance(self.cvssData, CvssV40):
            self.cvssData = CvssV40(**as_dict(self.cvssData))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdSsvcMetricV203(YAMLRoot):
    """
    A Stakeholder-Specific Vulnerability Categorization (SSVC) decision and who made it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdSsvcMetricV203"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdSsvcMetricV203"
    class_name: ClassVar[str] = "NvdSsvcMetricV203"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdSsvcMetricV203

    source: str = None
    ssvcData: Union[dict, "NvdSsvcData"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.ssvcData):
            self.MissingRequiredField("ssvcData")
        if not isinstance(self.ssvcData, NvdSsvcData):
            self.ssvcData = NvdSsvcData(**as_dict(self.ssvcData))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdSsvcData(YAMLRoot):
    """
    One SSVC decision, as the answers chosen on the way through a decision tree.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdSsvcData"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdSsvcData"
    class_name: ClassVar[str] = "NvdSsvcData"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdSsvcData

    options: Union[Union[dict, "NvdSsvcOption"], list[Union[dict, "NvdSsvcOption"]]] = None
    role: str = None
    version: str = None
    timestamp: Optional[Union[str, NvdTimestamp]] = None
    computed: Optional[str] = None
    decisionTree: Optional[Union[dict, "NvdSsvcDecisionTree"]] = None
    id: Optional[str] = None
    decisionTreeUrl: Optional[Union[str, URI]] = None
    generator: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.options):
            self.MissingRequiredField("options")
        if not isinstance(self.options, list):
            self.options = [self.options] if self.options is not None else []
        self.options = [v if isinstance(v, NvdSsvcOption) else NvdSsvcOption(**as_dict(v)) for v in self.options]

        if self._is_empty(self.role):
            self.MissingRequiredField("role")
        if not isinstance(self.role, str):
            self.role = str(self.role)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self.timestamp is not None and not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self.computed is not None and not isinstance(self.computed, str):
            self.computed = str(self.computed)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.decisionTreeUrl is not None and not isinstance(self.decisionTreeUrl, URI):
            self.decisionTreeUrl = URI(self.decisionTreeUrl)

        if self.generator is not None and not isinstance(self.generator, str):
            self.generator = str(self.generator)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdSsvcOption(YAMLRoot):
    """
    One answer on the way through a decision tree, keyed by its decision point.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdSsvcOption"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdSsvcOption"
    class_name: ClassVar[str] = "NvdSsvcOption"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdSsvcOption

    exploitation: Optional[str] = None
    automatable: Optional[str] = None
    technicalImpact: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.exploitation is not None and not isinstance(self.exploitation, (str,)):
            value = self.exploitation
            for _coerce in (lambda: str(value),):
                try:
                    self.exploitation = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types str could be constructed from {value!r} for slot exploitation")

        if self.automatable is not None and not isinstance(self.automatable, (str,)):
            value = self.automatable
            for _coerce in (lambda: str(value),):
                try:
                    self.automatable = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types str could be constructed from {value!r} for slot automatable")

        if self.technicalImpact is not None and not isinstance(self.technicalImpact, (str,)):
            value = self.technicalImpact
            for _coerce in (lambda: str(value),):
                try:
                    self.technicalImpact = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types str could be constructed from {value!r} for slot technicalImpact")

        super().__post_init__(**kwargs)


NvdSsvcDecisionTree = Any

@dataclass(repr=False)
class NvdAffected(YAMLRoot):
    """
    The products that one source says the vulnerability affects.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdAffected"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdAffected"
    class_name: ClassVar[str] = "NvdAffected"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdAffected

    source: str = None
    affectedData: Union[Union[dict, "NvdAffectedProduct"], list[Union[dict, "NvdAffectedProduct"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.affectedData):
            self.MissingRequiredField("affectedData")
        if not isinstance(self.affectedData, list):
            self.affectedData = [self.affectedData] if self.affectedData is not None else []
        self.affectedData = [v if isinstance(v, NvdAffectedProduct) else NvdAffectedProduct(**as_dict(v)) for v in self.affectedData]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdAffectedProduct(YAMLRoot):
    """
    A product and which of its versions have the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdAffectedProduct"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdAffectedProduct"
    class_name: ClassVar[str] = "NvdAffectedProduct"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdAffectedProduct

    defaultStatus: Optional[Union[str, "NvdVersionStatus"]] = None
    vendor: Optional[str] = None
    product: Optional[str] = None
    collectionURL: Optional[Union[str, URI]] = None
    packageName: Optional[str] = None
    cpes: Optional[Union[str, list[str]]] = empty_list()
    modules: Optional[Union[str, list[str]]] = empty_list()
    programFiles: Optional[Union[str, list[str]]] = empty_list()
    programRoutines: Optional[Union[Union[dict, "NvdProgramRoutine"], list[Union[dict, "NvdProgramRoutine"]]]] = empty_list()
    platforms: Optional[Union[str, list[str]]] = empty_list()
    repo: Optional[str] = None
    versions: Optional[Union[Union[dict, "NvdAffectedVersion"], list[Union[dict, "NvdAffectedVersion"]]]] = empty_list()
    packageURL: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.defaultStatus is not None and not isinstance(self.defaultStatus, NvdVersionStatus):
            self.defaultStatus = NvdVersionStatus(self.defaultStatus)

        if self.vendor is not None and not isinstance(self.vendor, str):
            self.vendor = str(self.vendor)

        if self.product is not None and not isinstance(self.product, str):
            self.product = str(self.product)

        if self.collectionURL is not None and not isinstance(self.collectionURL, URI):
            self.collectionURL = URI(self.collectionURL)

        if self.packageName is not None and not isinstance(self.packageName, str):
            self.packageName = str(self.packageName)

        if not isinstance(self.cpes, list):
            self.cpes = [self.cpes] if self.cpes is not None else []
        self.cpes = [v if isinstance(v, str) else str(v) for v in self.cpes]

        if not isinstance(self.modules, list):
            self.modules = [self.modules] if self.modules is not None else []
        self.modules = [v if isinstance(v, str) else str(v) for v in self.modules]

        if not isinstance(self.programFiles, list):
            self.programFiles = [self.programFiles] if self.programFiles is not None else []
        self.programFiles = [v if isinstance(v, str) else str(v) for v in self.programFiles]

        self._normalize_inlined_as_list(slot_name="programRoutines", slot_type=NvdProgramRoutine, key_name="name", keyed=False)

        if not isinstance(self.platforms, list):
            self.platforms = [self.platforms] if self.platforms is not None else []
        self.platforms = [v if isinstance(v, str) else str(v) for v in self.platforms]

        if self.repo is not None and not isinstance(self.repo, str):
            self.repo = str(self.repo)

        self._normalize_inlined_as_list(slot_name="versions", slot_type=NvdAffectedVersion, key_name="version", keyed=False)

        if self.packageURL is not None and not isinstance(self.packageURL, URI):
            self.packageURL = URI(self.packageURL)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdProgramRoutine(YAMLRoot):
    """
    One affected source code routine.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdProgramRoutine"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdProgramRoutine"
    class_name: ClassVar[str] = "NvdProgramRoutine"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdProgramRoutine

    name: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdAffectedVersion(YAMLRoot):
    """
    The status of one version of a product, or of a range of its versions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdAffectedVersion"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdAffectedVersion"
    class_name: ClassVar[str] = "NvdAffectedVersion"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdAffectedVersion

    version: str = None
    status: Union[str, "NvdVersionStatus"] = None
    versionType: Optional[str] = None
    lessThan: Optional[str] = None
    lessThanOrEqual: Optional[str] = None
    changes: Optional[Union[Union[dict, "NvdVersionChange"], list[Union[dict, "NvdVersionChange"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, NvdVersionStatus):
            self.status = NvdVersionStatus(self.status)

        if self.versionType is not None and not isinstance(self.versionType, str):
            self.versionType = str(self.versionType)

        if self.lessThan is not None and not isinstance(self.lessThan, str):
            self.lessThan = str(self.lessThan)

        if self.lessThanOrEqual is not None and not isinstance(self.lessThanOrEqual, str):
            self.lessThanOrEqual = str(self.lessThanOrEqual)

        self._normalize_inlined_as_list(slot_name="changes", slot_type=NvdVersionChange, key_name="at", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdVersionChange(YAMLRoot):
    """
    A point within a range of versions where the status changes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdVersionChange"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdVersionChange"
    class_name: ClassVar[str] = "NvdVersionChange"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdVersionChange

    at: str = None
    status: Union[str, "NvdVersionStatus"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.at):
            self.MissingRequiredField("at")
        if not isinstance(self.at, str):
            self.at = str(self.at)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, NvdVersionStatus):
            self.status = NvdVersionStatus(self.status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdWeakness(YAMLRoot):
    """
    The weaknesses that one source says lie behind a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdWeakness"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdWeakness"
    class_name: ClassVar[str] = "NvdWeakness"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdWeakness

    source: str = None
    type: Union[str, "NvdSourceType"] = None
    description: Union[Union[dict, NvdLangString], list[Union[dict, NvdLangString]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.source):
            self.MissingRequiredField("source")
        if not isinstance(self.source, str):
            self.source = str(self.source)

        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, NvdSourceType):
            self.type = NvdSourceType(self.type)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        self._normalize_inlined_as_list(slot_name="description", slot_type=NvdLangString, key_name="lang", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdConfiguration(YAMLRoot):
    """
    A statement of which product configurations have the vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdConfiguration"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdConfiguration"
    class_name: ClassVar[str] = "NvdConfiguration"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdConfiguration

    nodes: Union[Union[dict, "NvdConfigurationNode"], list[Union[dict, "NvdConfigurationNode"]]] = None
    operator: Optional[Union[str, "NvdOperator"]] = None
    negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.nodes):
            self.MissingRequiredField("nodes")
        self._normalize_inlined_as_list(slot_name="nodes", slot_type=NvdConfigurationNode, key_name="operator", keyed=False)

        if self.operator is not None and not isinstance(self.operator, NvdOperator):
            self.operator = NvdOperator(self.operator)

        if self.negate is not None and not isinstance(self.negate, Bool):
            self.negate = Bool(self.negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdConfigurationNode(YAMLRoot):
    """
    One part of a configuration statement, as a set of CPE matches.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdConfigurationNode"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdConfigurationNode"
    class_name: ClassVar[str] = "NvdConfigurationNode"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdConfigurationNode

    operator: Union[str, "NvdOperator"] = None
    cpeMatch: Union[Union[dict, "NvdCpeMatch"], list[Union[dict, "NvdCpeMatch"]]] = None
    negate: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.operator):
            self.MissingRequiredField("operator")
        if not isinstance(self.operator, NvdOperator):
            self.operator = NvdOperator(self.operator)

        if self._is_empty(self.cpeMatch):
            self.MissingRequiredField("cpeMatch")
        self._normalize_inlined_as_list(slot_name="cpeMatch", slot_type=NvdCpeMatch, key_name="criteria", keyed=False)

        if self.negate is not None and not isinstance(self.negate, Bool):
            self.negate = Bool(self.negate)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeMatch(YAMLRoot):
    """
    A CPE match string or range, and whether what it matches is vulnerable.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeMatch"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeMatch"
    class_name: ClassVar[str] = "NvdCpeMatch"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeMatch

    criteria: str = None
    matchCriteriaId: Union[str, NvdUuid] = None
    vulnerable: Union[bool, Bool] = None
    versionStartExcluding: Optional[str] = None
    versionStartIncluding: Optional[str] = None
    versionEndExcluding: Optional[str] = None
    versionEndIncluding: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.criteria):
            self.MissingRequiredField("criteria")
        if not isinstance(self.criteria, str):
            self.criteria = str(self.criteria)

        if self._is_empty(self.matchCriteriaId):
            self.MissingRequiredField("matchCriteriaId")
        if not isinstance(self.matchCriteriaId, NvdUuid):
            self.matchCriteriaId = NvdUuid(self.matchCriteriaId)

        if self._is_empty(self.vulnerable):
            self.MissingRequiredField("vulnerable")
        if not isinstance(self.vulnerable, Bool):
            self.vulnerable = Bool(self.vulnerable)

        if self.versionStartExcluding is not None and not isinstance(self.versionStartExcluding, str):
            self.versionStartExcluding = str(self.versionStartExcluding)

        if self.versionStartIncluding is not None and not isinstance(self.versionStartIncluding, str):
            self.versionStartIncluding = str(self.versionStartIncluding)

        if self.versionEndExcluding is not None and not isinstance(self.versionEndExcluding, str):
            self.versionEndExcluding = str(self.versionEndExcluding)

        if self.versionEndIncluding is not None and not isinstance(self.versionEndIncluding, str):
            self.versionEndIncluding = str(self.versionEndIncluding)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdVendorComment(YAMLRoot):
    """
    What a product's vendor has said about a vulnerability.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdVendorComment"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdVendorComment"
    class_name: ClassVar[str] = "NvdVendorComment"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdVendorComment

    lastModified: Union[str, NvdTimestamp] = None
    organization: str = None
    comment: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.lastModified):
            self.MissingRequiredField("lastModified")
        if not isinstance(self.lastModified, NvdTimestamp):
            self.lastModified = NvdTimestamp(self.lastModified)

        if self._is_empty(self.organization):
            self.MissingRequiredField("organization")
        if not isinstance(self.organization, str):
            self.organization = str(self.organization)

        if self._is_empty(self.comment):
            self.MissingRequiredField("comment")
        if not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeResponse(YAMLRoot):
    """
    A page of the product API's results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeResponse"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeResponse"
    class_name: ClassVar[str] = "NvdCpeResponse"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeResponse

    products: Union[Union[dict, "NvdCpeItem"], list[Union[dict, "NvdCpeItem"]]] = None
    format: str = None
    timestamp: Union[str, NvdTimestamp] = None
    resultsPerPage: int = None
    startIndex: int = None
    totalResults: int = None
    version: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.products):
            self.MissingRequiredField("products")
        if not isinstance(self.products, list):
            self.products = [self.products] if self.products is not None else []
        self.products = [v if isinstance(v, NvdCpeItem) else NvdCpeItem(**as_dict(v)) for v in self.products]

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self._is_empty(self.resultsPerPage):
            self.MissingRequiredField("resultsPerPage")
        if not isinstance(self.resultsPerPage, int):
            self.resultsPerPage = int(self.resultsPerPage)

        if self._is_empty(self.startIndex):
            self.MissingRequiredField("startIndex")
        if not isinstance(self.startIndex, int):
            self.startIndex = int(self.startIndex)

        if self._is_empty(self.totalResults):
            self.MissingRequiredField("totalResults")
        if not isinstance(self.totalResults, int):
            self.totalResults = int(self.totalResults)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeItem(YAMLRoot):
    """
    One entry of a product response, which only wraps the CPE name.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeItem"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeItem"
    class_name: ClassVar[str] = "NvdCpeItem"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeItem

    cpe: Union[dict, "NvdCpe"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpe):
            self.MissingRequiredField("cpe")
        if not isinstance(self.cpe, NvdCpe):
            self.cpe = NvdCpe(**as_dict(self.cpe))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpe(YAMLRoot):
    """
    A CPE name as NVD holds it, with its UUID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpe"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpe"
    class_name: ClassVar[str] = "NvdCpe"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpe

    cpeNameId: Union[str, NvdCpeCpeNameId] = None
    cpeName: str = None
    created: Union[str, NvdTimestamp] = None
    lastModified: Union[str, NvdTimestamp] = None
    deprecated: Union[bool, Bool] = None
    titles: Optional[Union[Union[dict, "NvdCpeTitle"], list[Union[dict, "NvdCpeTitle"]]]] = empty_list()
    refs: Optional[Union[Union[dict, "NvdCpeReference"], list[Union[dict, "NvdCpeReference"]]]] = empty_list()
    deprecatedBy: Optional[Union[Union[dict, "NvdCpeNameLink"], list[Union[dict, "NvdCpeNameLink"]]]] = empty_list()
    deprecates: Optional[Union[Union[dict, "NvdCpeNameLink"], list[Union[dict, "NvdCpeNameLink"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpeNameId):
            self.MissingRequiredField("cpeNameId")
        if not isinstance(self.cpeNameId, NvdCpeCpeNameId):
            self.cpeNameId = NvdCpeCpeNameId(self.cpeNameId)

        if self._is_empty(self.cpeName):
            self.MissingRequiredField("cpeName")
        if not isinstance(self.cpeName, str):
            self.cpeName = str(self.cpeName)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, NvdTimestamp):
            self.created = NvdTimestamp(self.created)

        if self._is_empty(self.lastModified):
            self.MissingRequiredField("lastModified")
        if not isinstance(self.lastModified, NvdTimestamp):
            self.lastModified = NvdTimestamp(self.lastModified)

        if self._is_empty(self.deprecated):
            self.MissingRequiredField("deprecated")
        if not isinstance(self.deprecated, Bool):
            self.deprecated = Bool(self.deprecated)

        self._normalize_inlined_as_list(slot_name="titles", slot_type=NvdCpeTitle, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="refs", slot_type=NvdCpeReference, key_name="ref", keyed=False)

        if not isinstance(self.deprecatedBy, list):
            self.deprecatedBy = [self.deprecatedBy] if self.deprecatedBy is not None else []
        self.deprecatedBy = [v if isinstance(v, NvdCpeNameLink) else NvdCpeNameLink(**as_dict(v)) for v in self.deprecatedBy]

        if not isinstance(self.deprecates, list):
            self.deprecates = [self.deprecates] if self.deprecates is not None else []
        self.deprecates = [v if isinstance(v, NvdCpeNameLink) else NvdCpeNameLink(**as_dict(v)) for v in self.deprecates]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeTitle(YAMLRoot):
    """
    A product's title in one language.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeTitle"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeTitle"
    class_name: ClassVar[str] = "NvdCpeTitle"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeTitle

    title: str = None
    lang: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.lang):
            self.MissingRequiredField("lang")
        if not isinstance(self.lang, str):
            self.lang = str(self.lang)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeReference(YAMLRoot):
    """
    A page about a product, and what kind of page it is.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeReference"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeReference"
    class_name: ClassVar[str] = "NvdCpeReference"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeReference

    ref: str = None
    type: Optional[Union[str, "NvdCpeReferenceType"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ref):
            self.MissingRequiredField("ref")
        if not isinstance(self.ref, str):
            self.ref = str(self.ref)

        if self.type is not None and not isinstance(self.type, NvdCpeReferenceType):
            self.type = NvdCpeReferenceType(self.type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeNameLink(YAMLRoot):
    """
    A pointer from one CPE name to another.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeNameLink"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeNameLink"
    class_name: ClassVar[str] = "NvdCpeNameLink"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeNameLink

    cpeName: Optional[str] = None
    cpeNameId: Optional[Union[str, NvdUuid]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpeName is not None and not isinstance(self.cpeName, str):
            self.cpeName = str(self.cpeName)

        if self.cpeNameId is not None and not isinstance(self.cpeNameId, NvdUuid):
            self.cpeNameId = NvdUuid(self.cpeNameId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdCpeMatchResponse(YAMLRoot):
    """
    A page of the match-string API's results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdCpeMatchResponse"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdCpeMatchResponse"
    class_name: ClassVar[str] = "NvdCpeMatchResponse"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdCpeMatchResponse

    matchStrings: Union[Union[dict, "NvdMatchStringItem"], list[Union[dict, "NvdMatchStringItem"]]] = None
    format: str = None
    timestamp: Union[str, NvdTimestamp] = None
    resultsPerPage: int = None
    startIndex: int = None
    totalResults: int = None
    version: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.matchStrings):
            self.MissingRequiredField("matchStrings")
        if not isinstance(self.matchStrings, list):
            self.matchStrings = [self.matchStrings] if self.matchStrings is not None else []
        self.matchStrings = [v if isinstance(v, NvdMatchStringItem) else NvdMatchStringItem(**as_dict(v)) for v in self.matchStrings]

        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self._is_empty(self.resultsPerPage):
            self.MissingRequiredField("resultsPerPage")
        if not isinstance(self.resultsPerPage, int):
            self.resultsPerPage = int(self.resultsPerPage)

        if self._is_empty(self.startIndex):
            self.MissingRequiredField("startIndex")
        if not isinstance(self.startIndex, int):
            self.startIndex = int(self.startIndex)

        if self._is_empty(self.totalResults):
            self.MissingRequiredField("totalResults")
        if not isinstance(self.totalResults, int):
            self.totalResults = int(self.totalResults)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdMatchStringItem(YAMLRoot):
    """
    One entry of a match-string response, which only wraps the match string.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdMatchStringItem"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdMatchStringItem"
    class_name: ClassVar[str] = "NvdMatchStringItem"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdMatchStringItem

    matchString: Union[dict, "NvdMatchString"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.matchString):
            self.MissingRequiredField("matchString")
        if not isinstance(self.matchString, NvdMatchString):
            self.matchString = NvdMatchString(**as_dict(self.matchString))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdMatchString(YAMLRoot):
    """
    A CPE match string or range as NVD holds it, and the CPE names it matches.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdMatchString"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdMatchString"
    class_name: ClassVar[str] = "NvdMatchString"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdMatchString

    matchCriteriaId: Union[str, NvdMatchStringMatchCriteriaId] = None
    criteria: str = None
    created: Union[str, NvdTimestamp] = None
    lastModified: Union[str, NvdTimestamp] = None
    status: Union[str, "NvdMatchStringStatus"] = None
    versionStartExcluding: Optional[str] = None
    versionStartIncluding: Optional[str] = None
    versionEndExcluding: Optional[str] = None
    versionEndIncluding: Optional[str] = None
    cpeLastModified: Optional[Union[str, NvdTimestamp]] = None
    matches: Optional[Union[Union[dict, "NvdMatchedCpe"], list[Union[dict, "NvdMatchedCpe"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.matchCriteriaId):
            self.MissingRequiredField("matchCriteriaId")
        if not isinstance(self.matchCriteriaId, NvdMatchStringMatchCriteriaId):
            self.matchCriteriaId = NvdMatchStringMatchCriteriaId(self.matchCriteriaId)

        if self._is_empty(self.criteria):
            self.MissingRequiredField("criteria")
        if not isinstance(self.criteria, str):
            self.criteria = str(self.criteria)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, NvdTimestamp):
            self.created = NvdTimestamp(self.created)

        if self._is_empty(self.lastModified):
            self.MissingRequiredField("lastModified")
        if not isinstance(self.lastModified, NvdTimestamp):
            self.lastModified = NvdTimestamp(self.lastModified)

        if self._is_empty(self.status):
            self.MissingRequiredField("status")
        if not isinstance(self.status, NvdMatchStringStatus):
            self.status = NvdMatchStringStatus(self.status)

        if self.versionStartExcluding is not None and not isinstance(self.versionStartExcluding, str):
            self.versionStartExcluding = str(self.versionStartExcluding)

        if self.versionStartIncluding is not None and not isinstance(self.versionStartIncluding, str):
            self.versionStartIncluding = str(self.versionStartIncluding)

        if self.versionEndExcluding is not None and not isinstance(self.versionEndExcluding, str):
            self.versionEndExcluding = str(self.versionEndExcluding)

        if self.versionEndIncluding is not None and not isinstance(self.versionEndIncluding, str):
            self.versionEndIncluding = str(self.versionEndIncluding)

        if self.cpeLastModified is not None and not isinstance(self.cpeLastModified, NvdTimestamp):
            self.cpeLastModified = NvdTimestamp(self.cpeLastModified)

        self._normalize_inlined_as_list(slot_name="matches", slot_type=NvdMatchedCpe, key_name="cpeName", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdMatchedCpe(YAMLRoot):
    """
    A CPE name that a match string matches.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdMatchedCpe"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdMatchedCpe"
    class_name: ClassVar[str] = "NvdMatchedCpe"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdMatchedCpe

    cpeName: str = None
    cpeNameId: Union[str, NvdUuid] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cpeName):
            self.MissingRequiredField("cpeName")
        if not isinstance(self.cpeName, str):
            self.cpeName = str(self.cpeName)

        if self._is_empty(self.cpeNameId):
            self.MissingRequiredField("cpeNameId")
        if not isinstance(self.cpeNameId, NvdUuid):
            self.cpeNameId = NvdUuid(self.cpeNameId)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdHistoryResponse(YAMLRoot):
    """
    A page of the change-history API's results.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdHistoryResponse"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdHistoryResponse"
    class_name: ClassVar[str] = "NvdHistoryResponse"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdHistoryResponse

    format: str = None
    timestamp: Union[str, NvdTimestamp] = None
    resultsPerPage: int = None
    startIndex: int = None
    totalResults: int = None
    version: str = None
    cveChanges: Optional[Union[Union[dict, "NvdChangeItem"], list[Union[dict, "NvdChangeItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.format):
            self.MissingRequiredField("format")
        if not isinstance(self.format, str):
            self.format = str(self.format)

        if self._is_empty(self.timestamp):
            self.MissingRequiredField("timestamp")
        if not isinstance(self.timestamp, NvdTimestamp):
            self.timestamp = NvdTimestamp(self.timestamp)

        if self._is_empty(self.resultsPerPage):
            self.MissingRequiredField("resultsPerPage")
        if not isinstance(self.resultsPerPage, int):
            self.resultsPerPage = int(self.resultsPerPage)

        if self._is_empty(self.startIndex):
            self.MissingRequiredField("startIndex")
        if not isinstance(self.startIndex, int):
            self.startIndex = int(self.startIndex)

        if self._is_empty(self.totalResults):
            self.MissingRequiredField("totalResults")
        if not isinstance(self.totalResults, int):
            self.totalResults = int(self.totalResults)

        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if not isinstance(self.cveChanges, list):
            self.cveChanges = [self.cveChanges] if self.cveChanges is not None else []
        self.cveChanges = [v if isinstance(v, NvdChangeItem) else NvdChangeItem(**as_dict(v)) for v in self.cveChanges]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdChangeItem(YAMLRoot):
    """
    One entry of a change-history response, which only wraps the change.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdChangeItem"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdChangeItem"
    class_name: ClassVar[str] = "NvdChangeItem"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdChangeItem

    change: Union[dict, "NvdChange"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.change):
            self.MissingRequiredField("change")
        if not isinstance(self.change, NvdChange):
            self.change = NvdChange(**as_dict(self.change))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdChange(YAMLRoot):
    """
    One change to a vulnerability's record at NVD.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdChange"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdChange"
    class_name: ClassVar[str] = "NvdChange"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdChange

    cveChangeId: Union[str, NvdChangeCveChangeId] = None
    sourceIdentifier: str = None
    cveId: Union[str, NvdCveId] = None
    eventName: str = None
    created: Optional[Union[str, NvdTimestamp]] = None
    details: Optional[Union[Union[dict, "NvdChangeDetail"], list[Union[dict, "NvdChangeDetail"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cveChangeId):
            self.MissingRequiredField("cveChangeId")
        if not isinstance(self.cveChangeId, NvdChangeCveChangeId):
            self.cveChangeId = NvdChangeCveChangeId(self.cveChangeId)

        if self._is_empty(self.sourceIdentifier):
            self.MissingRequiredField("sourceIdentifier")
        if not isinstance(self.sourceIdentifier, str):
            self.sourceIdentifier = str(self.sourceIdentifier)

        if self._is_empty(self.cveId):
            self.MissingRequiredField("cveId")
        if not isinstance(self.cveId, NvdCveId):
            self.cveId = NvdCveId(self.cveId)

        if self._is_empty(self.eventName):
            self.MissingRequiredField("eventName")
        if not isinstance(self.eventName, str):
            self.eventName = str(self.eventName)

        if self.created is not None and not isinstance(self.created, NvdTimestamp):
            self.created = NvdTimestamp(self.created)

        self._normalize_inlined_as_list(slot_name="details", slot_type=NvdChangeDetail, key_name="type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NvdChangeDetail(YAMLRoot):
    """
    One part of a change, naming what kind of data changed and how.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdChangeDetail"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdChangeDetail"
    class_name: ClassVar[str] = "NvdChangeDetail"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdChangeDetail

    type: str = None
    action: Optional[str] = None
    oldValue: Optional[Union[str, dict, "NvdChangeObject"]] = None
    newValue: Optional[Union[str, dict, "NvdChangeObject"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, str):
            self.type = str(self.type)

        if self.action is not None and not isinstance(self.action, str):
            self.action = str(self.action)

        if self.oldValue is not None and not isinstance(self.oldValue, (str, NvdChangeObject)):
            value = self.oldValue
            for _coerce in (lambda: str(value), lambda: NvdChangeObject()):
                try:
                    self.oldValue = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, NvdChangeObject] could be constructed from {value!r} for slot oldValue")

        if self.newValue is not None and not isinstance(self.newValue, (str, NvdChangeObject)):
            value = self.newValue
            for _coerce in (lambda: str(value), lambda: NvdChangeObject()):
                try:
                    self.newValue = _coerce()
                    break
                except (ValueError, TypeError):
                    continue
            else:
                raise ValueError(f"None of the candidate types Union[str, NvdChangeObject] could be constructed from {value!r} for slot newValue")

        super().__post_init__(**kwargs)


class NvdChangeObject(YAMLRoot):
    """
    A value before or after a change that is an object, with any keys.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_NVD["NvdChangeObject"]
    class_class_curie: ClassVar[str] = "nist_nvd:NvdChangeObject"
    class_name: ClassVar[str] = "NvdChangeObject"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.NvdChangeObject


@dataclass(repr=False)
class CvssSeverityBandsMixin(YAMLRoot):
    """
    The base score and base severity of a CVSS version with severity bands, and the bands that tie one to the other.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssSeverityBandsMixin"]
    class_class_curie: ClassVar[str] = "cve:CvssSeverityBandsMixin"
    class_name: ClassVar[str] = "CvssSeverityBandsMixin"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.CvssSeverityBandsMixin

    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV20(YAMLRoot):
    """
    A score under CVSS version 2.0, which has no severity bands.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV20"]
    class_class_curie: ClassVar[str] = "cve:CvssV20"
    class_name: ClassVar[str] = "CvssV20"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.CvssV20

    version: str = None
    vectorString: str = None
    baseScore: float = None
    confidentialityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    integrityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    availabilityImpact: Optional[Union[str, "CvssV2Impact"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV2ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    environmentalScore: Optional[float] = None
    accessVector: Optional[Union[str, "CvssV2AccessVector"]] = None
    accessComplexity: Optional[Union[str, "CvssV2AccessComplexity"]] = None
    authentication: Optional[Union[str, "CvssV2Authentication"]] = None
    exploitability: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    collateralDamagePotential: Optional[Union[str, "CvssV2CollateralDamagePotential"]] = None
    targetDistribution: Optional[Union[str, "CvssV2TargetDistribution"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssV2Impact):
            self.confidentialityImpact = CvssV2Impact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssV2Impact):
            self.integrityImpact = CvssV2Impact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssV2Impact):
            self.availabilityImpact = CvssV2Impact(self.availabilityImpact)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV2ReportConfidence):
            self.reportConfidence = CvssV2ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.accessVector is not None and not isinstance(self.accessVector, CvssV2AccessVector):
            self.accessVector = CvssV2AccessVector(self.accessVector)

        if self.accessComplexity is not None and not isinstance(self.accessComplexity, CvssV2AccessComplexity):
            self.accessComplexity = CvssV2AccessComplexity(self.accessComplexity)

        if self.authentication is not None and not isinstance(self.authentication, CvssV2Authentication):
            self.authentication = CvssV2Authentication(self.authentication)

        if self.exploitability is not None and not isinstance(self.exploitability, CvssExploitCodeMaturity):
            self.exploitability = CvssExploitCodeMaturity(self.exploitability)

        if self.collateralDamagePotential is not None and not isinstance(self.collateralDamagePotential, CvssV2CollateralDamagePotential):
            self.collateralDamagePotential = CvssV2CollateralDamagePotential(self.collateralDamagePotential)

        if self.targetDistribution is not None and not isinstance(self.targetDistribution, CvssV2TargetDistribution):
            self.targetDistribution = CvssV2TargetDistribution(self.targetDistribution)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV30(YAMLRoot):
    """
    A score under CVSS version 3.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV30"]
    class_class_curie: ClassVar[str] = "cve:CvssV30"
    class_name: ClassVar[str] = "CvssV30"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.CvssV30

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV3AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV3UserInteraction"]] = None
    scope: Optional[Union[str, "CvssV3Scope"]] = None
    confidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    integrityImpact: Optional[Union[str, "CvssImpact"]] = None
    availabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitCodeMaturity: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV3ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    temporalSeverity: Optional[Union[str, "CvssSeverity"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    modifiedAttackVector: Optional[Union[str, "CvssV3ModifiedAttackVector"]] = None
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = None
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = None
    modifiedUserInteraction: Optional[Union[str, "CvssV3ModifiedUserInteraction"]] = None
    modifiedScope: Optional[Union[str, "CvssV3ModifiedScope"]] = None
    modifiedConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    environmentalScore: Optional[float] = None
    environmentalSeverity: Optional[Union[str, "CvssSeverity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV3AttackVector):
            self.attackVector = CvssV3AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV3UserInteraction):
            self.userInteraction = CvssV3UserInteraction(self.userInteraction)

        if self.scope is not None and not isinstance(self.scope, CvssV3Scope):
            self.scope = CvssV3Scope(self.scope)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssImpact):
            self.confidentialityImpact = CvssImpact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssImpact):
            self.integrityImpact = CvssImpact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssImpact):
            self.availabilityImpact = CvssImpact(self.availabilityImpact)

        if self.exploitCodeMaturity is not None and not isinstance(self.exploitCodeMaturity, CvssExploitCodeMaturity):
            self.exploitCodeMaturity = CvssExploitCodeMaturity(self.exploitCodeMaturity)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV3ReportConfidence):
            self.reportConfidence = CvssV3ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.temporalSeverity is not None and not isinstance(self.temporalSeverity, CvssSeverity):
            self.temporalSeverity = CvssSeverity(self.temporalSeverity)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV3ModifiedAttackVector):
            self.modifiedAttackVector = CvssV3ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV3ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV3ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.modifiedScope is not None and not isinstance(self.modifiedScope, CvssV3ModifiedScope):
            self.modifiedScope = CvssV3ModifiedScope(self.modifiedScope)

        if self.modifiedConfidentialityImpact is not None and not isinstance(self.modifiedConfidentialityImpact, CvssModifiedImpact):
            self.modifiedConfidentialityImpact = CvssModifiedImpact(self.modifiedConfidentialityImpact)

        if self.modifiedIntegrityImpact is not None and not isinstance(self.modifiedIntegrityImpact, CvssModifiedImpact):
            self.modifiedIntegrityImpact = CvssModifiedImpact(self.modifiedIntegrityImpact)

        if self.modifiedAvailabilityImpact is not None and not isinstance(self.modifiedAvailabilityImpact, CvssModifiedImpact):
            self.modifiedAvailabilityImpact = CvssModifiedImpact(self.modifiedAvailabilityImpact)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.environmentalSeverity is not None and not isinstance(self.environmentalSeverity, CvssSeverity):
            self.environmentalSeverity = CvssSeverity(self.environmentalSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV31(YAMLRoot):
    """
    A score under CVSS version 3.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV31"]
    class_class_curie: ClassVar[str] = "cve:CvssV31"
    class_name: ClassVar[str] = "CvssV31"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.CvssV31

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV3AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV3UserInteraction"]] = None
    scope: Optional[Union[str, "CvssV3Scope"]] = None
    confidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    integrityImpact: Optional[Union[str, "CvssImpact"]] = None
    availabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitCodeMaturity: Optional[Union[str, "CvssExploitCodeMaturity"]] = None
    remediationLevel: Optional[Union[str, "CvssRemediationLevel"]] = None
    reportConfidence: Optional[Union[str, "CvssV3ReportConfidence"]] = None
    temporalScore: Optional[float] = None
    temporalSeverity: Optional[Union[str, "CvssSeverity"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = None
    modifiedAttackVector: Optional[Union[str, "CvssV3ModifiedAttackVector"]] = None
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = None
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = None
    modifiedUserInteraction: Optional[Union[str, "CvssV3ModifiedUserInteraction"]] = None
    modifiedScope: Optional[Union[str, "CvssV3ModifiedScope"]] = None
    modifiedConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    modifiedAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = None
    environmentalScore: Optional[float] = None
    environmentalSeverity: Optional[Union[str, "CvssSeverity"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV3AttackVector):
            self.attackVector = CvssV3AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV3UserInteraction):
            self.userInteraction = CvssV3UserInteraction(self.userInteraction)

        if self.scope is not None and not isinstance(self.scope, CvssV3Scope):
            self.scope = CvssV3Scope(self.scope)

        if self.confidentialityImpact is not None and not isinstance(self.confidentialityImpact, CvssImpact):
            self.confidentialityImpact = CvssImpact(self.confidentialityImpact)

        if self.integrityImpact is not None and not isinstance(self.integrityImpact, CvssImpact):
            self.integrityImpact = CvssImpact(self.integrityImpact)

        if self.availabilityImpact is not None and not isinstance(self.availabilityImpact, CvssImpact):
            self.availabilityImpact = CvssImpact(self.availabilityImpact)

        if self.exploitCodeMaturity is not None and not isinstance(self.exploitCodeMaturity, CvssExploitCodeMaturity):
            self.exploitCodeMaturity = CvssExploitCodeMaturity(self.exploitCodeMaturity)

        if self.remediationLevel is not None and not isinstance(self.remediationLevel, CvssRemediationLevel):
            self.remediationLevel = CvssRemediationLevel(self.remediationLevel)

        if self.reportConfidence is not None and not isinstance(self.reportConfidence, CvssV3ReportConfidence):
            self.reportConfidence = CvssV3ReportConfidence(self.reportConfidence)

        if self.temporalScore is not None and not isinstance(self.temporalScore, float):
            self.temporalScore = float(self.temporalScore)

        if self.temporalSeverity is not None and not isinstance(self.temporalSeverity, CvssSeverity):
            self.temporalSeverity = CvssSeverity(self.temporalSeverity)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV3ModifiedAttackVector):
            self.modifiedAttackVector = CvssV3ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV3ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV3ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.modifiedScope is not None and not isinstance(self.modifiedScope, CvssV3ModifiedScope):
            self.modifiedScope = CvssV3ModifiedScope(self.modifiedScope)

        if self.modifiedConfidentialityImpact is not None and not isinstance(self.modifiedConfidentialityImpact, CvssModifiedImpact):
            self.modifiedConfidentialityImpact = CvssModifiedImpact(self.modifiedConfidentialityImpact)

        if self.modifiedIntegrityImpact is not None and not isinstance(self.modifiedIntegrityImpact, CvssModifiedImpact):
            self.modifiedIntegrityImpact = CvssModifiedImpact(self.modifiedIntegrityImpact)

        if self.modifiedAvailabilityImpact is not None and not isinstance(self.modifiedAvailabilityImpact, CvssModifiedImpact):
            self.modifiedAvailabilityImpact = CvssModifiedImpact(self.modifiedAvailabilityImpact)

        if self.environmentalScore is not None and not isinstance(self.environmentalScore, float):
            self.environmentalScore = float(self.environmentalScore)

        if self.environmentalSeverity is not None and not isinstance(self.environmentalSeverity, CvssSeverity):
            self.environmentalSeverity = CvssSeverity(self.environmentalSeverity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CvssV40(YAMLRoot):
    """
    A score under CVSS version 4.0.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CVE["CvssV40"]
    class_class_curie: ClassVar[str] = "cve:CvssV40"
    class_name: ClassVar[str] = "CvssV40"
    class_model_uri: ClassVar[URIRef] = NIST_NVD.CvssV40

    version: str = None
    vectorString: str = None
    baseScore: float = None
    baseSeverity: Union[str, "CvssSeverity"] = None
    attackVector: Optional[Union[str, "CvssV4AttackVector"]] = None
    attackComplexity: Optional[Union[str, "CvssAttackComplexity"]] = None
    privilegesRequired: Optional[Union[str, "CvssPrivilegesRequired"]] = None
    userInteraction: Optional[Union[str, "CvssV4UserInteraction"]] = None
    confidentialityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    integrityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    availabilityRequirement: Optional[Union[str, "CvssRequirement"]] = 'NOT_DEFINED'
    modifiedAttackVector: Optional[Union[str, "CvssV4ModifiedAttackVector"]] = 'NOT_DEFINED'
    modifiedAttackComplexity: Optional[Union[str, "CvssModifiedAttackComplexity"]] = 'NOT_DEFINED'
    modifiedPrivilegesRequired: Optional[Union[str, "CvssModifiedPrivilegesRequired"]] = 'NOT_DEFINED'
    modifiedUserInteraction: Optional[Union[str, "CvssV4ModifiedUserInteraction"]] = 'NOT_DEFINED'
    attackRequirements: Optional[Union[str, "CvssV4AttackRequirements"]] = None
    vulnConfidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    vulnIntegrityImpact: Optional[Union[str, "CvssImpact"]] = None
    vulnAvailabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    subConfidentialityImpact: Optional[Union[str, "CvssImpact"]] = None
    subIntegrityImpact: Optional[Union[str, "CvssImpact"]] = None
    subAvailabilityImpact: Optional[Union[str, "CvssImpact"]] = None
    exploitMaturity: Optional[Union[str, "CvssV4ExploitMaturity"]] = 'NOT_DEFINED'
    modifiedAttackRequirements: Optional[Union[str, "CvssV4ModifiedAttackRequirements"]] = 'NOT_DEFINED'
    modifiedVulnConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedVulnIntegrityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedVulnAvailabilityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedSubConfidentialityImpact: Optional[Union[str, "CvssModifiedImpact"]] = 'NOT_DEFINED'
    modifiedSubIntegrityImpact: Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]] = 'NOT_DEFINED'
    modifiedSubAvailabilityImpact: Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]] = 'NOT_DEFINED'
    Safety: Optional[Union[str, "CvssV4Safety"]] = 'NOT_DEFINED'
    Automatable: Optional[Union[str, "CvssV4Automatable"]] = 'NOT_DEFINED'
    Recovery: Optional[Union[str, "CvssV4Recovery"]] = 'NOT_DEFINED'
    valueDensity: Optional[Union[str, "CvssV4ValueDensity"]] = 'NOT_DEFINED'
    vulnerabilityResponseEffort: Optional[Union[str, "CvssV4ResponseEffort"]] = 'NOT_DEFINED'
    providerUrgency: Optional[Union[str, "CvssV4ProviderUrgency"]] = 'NOT_DEFINED'

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.version):
            self.MissingRequiredField("version")
        if not isinstance(self.version, str):
            self.version = str(self.version)

        if self._is_empty(self.vectorString):
            self.MissingRequiredField("vectorString")
        if not isinstance(self.vectorString, str):
            self.vectorString = str(self.vectorString)

        if self._is_empty(self.baseScore):
            self.MissingRequiredField("baseScore")
        if not isinstance(self.baseScore, float):
            self.baseScore = float(self.baseScore)

        if self._is_empty(self.baseSeverity):
            self.MissingRequiredField("baseSeverity")
        if not isinstance(self.baseSeverity, CvssSeverity):
            self.baseSeverity = CvssSeverity(self.baseSeverity)

        if self.attackVector is not None and not isinstance(self.attackVector, CvssV4AttackVector):
            self.attackVector = CvssV4AttackVector(self.attackVector)

        if self.attackComplexity is not None and not isinstance(self.attackComplexity, CvssAttackComplexity):
            self.attackComplexity = CvssAttackComplexity(self.attackComplexity)

        if self.privilegesRequired is not None and not isinstance(self.privilegesRequired, CvssPrivilegesRequired):
            self.privilegesRequired = CvssPrivilegesRequired(self.privilegesRequired)

        if self.userInteraction is not None and not isinstance(self.userInteraction, CvssV4UserInteraction):
            self.userInteraction = CvssV4UserInteraction(self.userInteraction)

        if self.confidentialityRequirement is not None and not isinstance(self.confidentialityRequirement, CvssRequirement):
            self.confidentialityRequirement = CvssRequirement(self.confidentialityRequirement)

        if self.integrityRequirement is not None and not isinstance(self.integrityRequirement, CvssRequirement):
            self.integrityRequirement = CvssRequirement(self.integrityRequirement)

        if self.availabilityRequirement is not None and not isinstance(self.availabilityRequirement, CvssRequirement):
            self.availabilityRequirement = CvssRequirement(self.availabilityRequirement)

        if self.modifiedAttackVector is not None and not isinstance(self.modifiedAttackVector, CvssV4ModifiedAttackVector):
            self.modifiedAttackVector = CvssV4ModifiedAttackVector(self.modifiedAttackVector)

        if self.modifiedAttackComplexity is not None and not isinstance(self.modifiedAttackComplexity, CvssModifiedAttackComplexity):
            self.modifiedAttackComplexity = CvssModifiedAttackComplexity(self.modifiedAttackComplexity)

        if self.modifiedPrivilegesRequired is not None and not isinstance(self.modifiedPrivilegesRequired, CvssModifiedPrivilegesRequired):
            self.modifiedPrivilegesRequired = CvssModifiedPrivilegesRequired(self.modifiedPrivilegesRequired)

        if self.modifiedUserInteraction is not None and not isinstance(self.modifiedUserInteraction, CvssV4ModifiedUserInteraction):
            self.modifiedUserInteraction = CvssV4ModifiedUserInteraction(self.modifiedUserInteraction)

        if self.attackRequirements is not None and not isinstance(self.attackRequirements, CvssV4AttackRequirements):
            self.attackRequirements = CvssV4AttackRequirements(self.attackRequirements)

        if self.vulnConfidentialityImpact is not None and not isinstance(self.vulnConfidentialityImpact, CvssImpact):
            self.vulnConfidentialityImpact = CvssImpact(self.vulnConfidentialityImpact)

        if self.vulnIntegrityImpact is not None and not isinstance(self.vulnIntegrityImpact, CvssImpact):
            self.vulnIntegrityImpact = CvssImpact(self.vulnIntegrityImpact)

        if self.vulnAvailabilityImpact is not None and not isinstance(self.vulnAvailabilityImpact, CvssImpact):
            self.vulnAvailabilityImpact = CvssImpact(self.vulnAvailabilityImpact)

        if self.subConfidentialityImpact is not None and not isinstance(self.subConfidentialityImpact, CvssImpact):
            self.subConfidentialityImpact = CvssImpact(self.subConfidentialityImpact)

        if self.subIntegrityImpact is not None and not isinstance(self.subIntegrityImpact, CvssImpact):
            self.subIntegrityImpact = CvssImpact(self.subIntegrityImpact)

        if self.subAvailabilityImpact is not None and not isinstance(self.subAvailabilityImpact, CvssImpact):
            self.subAvailabilityImpact = CvssImpact(self.subAvailabilityImpact)

        if self.exploitMaturity is not None and not isinstance(self.exploitMaturity, CvssV4ExploitMaturity):
            self.exploitMaturity = CvssV4ExploitMaturity(self.exploitMaturity)

        if self.modifiedAttackRequirements is not None and not isinstance(self.modifiedAttackRequirements, CvssV4ModifiedAttackRequirements):
            self.modifiedAttackRequirements = CvssV4ModifiedAttackRequirements(self.modifiedAttackRequirements)

        if self.modifiedVulnConfidentialityImpact is not None and not isinstance(self.modifiedVulnConfidentialityImpact, CvssModifiedImpact):
            self.modifiedVulnConfidentialityImpact = CvssModifiedImpact(self.modifiedVulnConfidentialityImpact)

        if self.modifiedVulnIntegrityImpact is not None and not isinstance(self.modifiedVulnIntegrityImpact, CvssModifiedImpact):
            self.modifiedVulnIntegrityImpact = CvssModifiedImpact(self.modifiedVulnIntegrityImpact)

        if self.modifiedVulnAvailabilityImpact is not None and not isinstance(self.modifiedVulnAvailabilityImpact, CvssModifiedImpact):
            self.modifiedVulnAvailabilityImpact = CvssModifiedImpact(self.modifiedVulnAvailabilityImpact)

        if self.modifiedSubConfidentialityImpact is not None and not isinstance(self.modifiedSubConfidentialityImpact, CvssModifiedImpact):
            self.modifiedSubConfidentialityImpact = CvssModifiedImpact(self.modifiedSubConfidentialityImpact)

        if self.modifiedSubIntegrityImpact is not None and not isinstance(self.modifiedSubIntegrityImpact, CvssV4ModifiedSubsequentImpact):
            self.modifiedSubIntegrityImpact = CvssV4ModifiedSubsequentImpact(self.modifiedSubIntegrityImpact)

        if self.modifiedSubAvailabilityImpact is not None and not isinstance(self.modifiedSubAvailabilityImpact, CvssV4ModifiedSubsequentImpact):
            self.modifiedSubAvailabilityImpact = CvssV4ModifiedSubsequentImpact(self.modifiedSubAvailabilityImpact)

        if self.Safety is not None and not isinstance(self.Safety, CvssV4Safety):
            self.Safety = CvssV4Safety(self.Safety)

        if self.Automatable is not None and not isinstance(self.Automatable, CvssV4Automatable):
            self.Automatable = CvssV4Automatable(self.Automatable)

        if self.Recovery is not None and not isinstance(self.Recovery, CvssV4Recovery):
            self.Recovery = CvssV4Recovery(self.Recovery)

        if self.valueDensity is not None and not isinstance(self.valueDensity, CvssV4ValueDensity):
            self.valueDensity = CvssV4ValueDensity(self.valueDensity)

        if self.vulnerabilityResponseEffort is not None and not isinstance(self.vulnerabilityResponseEffort, CvssV4ResponseEffort):
            self.vulnerabilityResponseEffort = CvssV4ResponseEffort(self.vulnerabilityResponseEffort)

        if self.providerUrgency is not None and not isinstance(self.providerUrgency, CvssV4ProviderUrgency):
            self.providerUrgency = CvssV4ProviderUrgency(self.providerUrgency)

        super().__post_init__(**kwargs)


# Enumerations
class NvdVulnStatus(EnumDefinitionImpl):
    """
    Where a vulnerability stands in NVD's own analysis.
    """
    Analyzed = PermissibleValue(
        text="Analyzed",
        description="NVD has finished its analysis of the record.")
    Deferred = PermissibleValue(
        text="Deferred",
        description="NVD has put off analysing the record.")
    Modified = PermissibleValue(
        text="Modified",
        description="The record has changed since NVD analysed it.")
    Received = PermissibleValue(
        text="Received",
        description="The record has just reached NVD.")
    Rejected = PermissibleValue(
        text="Rejected",
        description="The CVE identifier has been rejected.")

    _defn = EnumDefinition(
        name="NvdVulnStatus",
        description="Where a vulnerability stands in NVD's own analysis.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Awaiting Analysis",
            PermissibleValue(
                text="Awaiting Analysis",
                description="NVD has the record and has not begun to analyse it."))
        setattr(cls, "Undergoing Analysis",
            PermissibleValue(
                text="Undergoing Analysis",
                description="NVD is analysing the record now."))

class NvdCveTagName(EnumDefinitionImpl):
    """
    A label that a CVE record's source puts on the record.
    """
    disputed = PermissibleValue(
        text="disputed",
        description="A party disputes that this is a vulnerability.")

    _defn = EnumDefinition(
        name="NvdCveTagName",
        description="A label that a CVE record's source puts on the record.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "unsupported-when-assigned",
            PermissibleValue(
                text="unsupported-when-assigned",
                description="The product had lost its support when the identifier was assigned."))
        setattr(cls, "exclusively-hosted-service",
            PermissibleValue(
                text="exclusively-hosted-service",
                description="The product exists only as a hosted service."))

class NvdReferenceTag(EnumDefinitionImpl):
    """
    NVD's label for what a reference is.
    """
    Exploit = PermissibleValue(
        text="Exploit",
        description="The page shows or gives a way to exploit the vulnerability.")
    Mitigation = PermissibleValue(
        text="Mitigation",
        description="The page says how to reduce the risk without a fix.")
    Patch = PermissibleValue(
        text="Patch",
        description="The page holds or points to a fix.")
    Related = PermissibleValue(
        text="Related",
        description="A page on a related matter.")
    Product = PermissibleValue(
        text="Product",
        description="A page about the affected product.")

    _defn = EnumDefinition(
        name="NvdReferenceTag",
        description="NVD's label for what a reference is.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Broken Link",
            PermissibleValue(
                text="Broken Link",
                description="The address no longer leads to the content."))
        setattr(cls, "Issue Tracking",
            PermissibleValue(
                text="Issue Tracking",
                description="An entry in a bug or issue tracker."))
        setattr(cls, "Mailing List",
            PermissibleValue(
                text="Mailing List",
                description="A message in a mailing list archive."))
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="The page does not bear on the vulnerability."))
        setattr(cls, "Permissions Required",
            PermissibleValue(
                text="Permissions Required",
                description="Reading the page takes an account or some other access."))
        setattr(cls, "Press/Media Coverage",
            PermissibleValue(
                text="Press/Media Coverage",
                description="A report in the press or other media."))
        setattr(cls, "Release Notes",
            PermissibleValue(
                text="Release Notes",
                description="The notes of a product release."))
        setattr(cls, "Technical Description",
            PermissibleValue(
                text="Technical Description",
                description="A technical account of the vulnerability."))
        setattr(cls, "Third Party Advisory",
            PermissibleValue(
                text="Third Party Advisory",
                description="An advisory from someone other than the vendor."))
        setattr(cls, "Tool Signature",
            PermissibleValue(
                text="Tool Signature",
                description="A signature that a detection tool can use."))
        setattr(cls, "URL Repurposed",
            PermissibleValue(
                text="URL Repurposed",
                description="The address now leads to something else."))
        setattr(cls, "US Government Resource",
            PermissibleValue(
                text="US Government Resource",
                description="A page from a body of the United States government."))
        setattr(cls, "VDB Entry",
            PermissibleValue(
                text="VDB Entry",
                description="An entry in a vulnerability database."))
        setattr(cls, "Vendor Advisory",
            PermissibleValue(
                text="Vendor Advisory",
                description="An advisory from the product's vendor."))

class NvdSourceType(EnumDefinitionImpl):
    """
    Whether a score or a weakness comes from the party NVD treats as first.
    """
    Primary = PermissibleValue(
        text="Primary",
        description="NVD's first source for the record.")
    Secondary = PermissibleValue(
        text="Secondary",
        description="Any other source.")

    _defn = EnumDefinition(
        name="NvdSourceType",
        description="Whether a score or a weakness comes from the party NVD treats as first.",
    )

class NvdCvssV2Severity(EnumDefinitionImpl):
    """
    The severity band NVD gives a CVSS 2.0 base score.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="The low band of CVSS 2.0 base scores.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="The middle band of CVSS 2.0 base scores.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="The high band of CVSS 2.0 base scores.")

    _defn = EnumDefinition(
        name="NvdCvssV2Severity",
        description="The severity band NVD gives a CVSS 2.0 base score.",
    )

class NvdVersionStatus(EnumDefinitionImpl):
    """
    Whether a version of a product has the vulnerability.
    """
    affected = PermissibleValue(
        text="affected",
        description="This version has the vulnerability.")
    unaffected = PermissibleValue(
        text="unaffected",
        description="This version does not have the vulnerability.")
    unknown = PermissibleValue(
        text="unknown",
        description="Nobody has said whether this version has the vulnerability.")

    _defn = EnumDefinition(
        name="NvdVersionStatus",
        description="Whether a version of a product has the vulnerability.",
    )

class NvdOperator(EnumDefinitionImpl):
    """
    How the parts of a configuration combine.
    """
    AND = PermissibleValue(
        text="AND",
        description="Every part must hold.")
    OR = PermissibleValue(
        text="OR",
        description="At least one part must hold.")

    _defn = EnumDefinition(
        name="NvdOperator",
        description="How the parts of a configuration combine.",
    )

class NvdCpeReferenceType(EnumDefinitionImpl):
    """
    What a CPE name's reference points to.
    """
    Advisory = PermissibleValue(
        text="Advisory",
        description="A security advisory.")
    Product = PermissibleValue(
        text="Product",
        description="A page about the product.")
    Project = PermissibleValue(
        text="Project",
        description="A page about the project behind the product.")
    Vendor = PermissibleValue(
        text="Vendor",
        description="A page about the vendor.")
    Version = PermissibleValue(
        text="Version",
        description="A page about this version.")

    _defn = EnumDefinition(
        name="NvdCpeReferenceType",
        description="What a CPE name's reference points to.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Change Log",
            PermissibleValue(
                text="Change Log",
                description="A list of the product's changes."))

class NvdMatchStringStatus(EnumDefinitionImpl):
    """
    Whether NVD still uses a match string.
    """
    Active = PermissibleValue(
        text="Active",
        description="NVD uses this match string.")
    Inactive = PermissibleValue(
        text="Inactive",
        description="NVD no longer uses this match string.")

    _defn = EnumDefinition(
        name="NvdMatchStringStatus",
        description="Whether NVD still uses a match string.",
    )

class CvssSeverity(EnumDefinitionImpl):
    """
    A CVSS rating in words.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No severity at all, for a score of 0.",
        meaning=SPDX_SECURITY["CvssSeverityType/none"])
    LOW = PermissibleValue(
        text="LOW",
        description="The lowest rating above none.",
        meaning=SPDX_SECURITY["CvssSeverityType/low"])
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="The middle rating.",
        meaning=SPDX_SECURITY["CvssSeverityType/medium"])
    HIGH = PermissibleValue(
        text="HIGH",
        description="The rating below critical.",
        meaning=SPDX_SECURITY["CvssSeverityType/high"])
    CRITICAL = PermissibleValue(
        text="CRITICAL",
        description="The highest rating.",
        meaning=SPDX_SECURITY["CvssSeverityType/critical"])

    _defn = EnumDefinition(
        name="CvssSeverity",
        description="A CVSS rating in words.",
    )

class CvssV2AccessVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 2.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from the same local network segment.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only with an account on the system or hands on it.")

    _defn = EnumDefinition(
        name="CvssV2AccessVector",
        description="How far away an attacker can be, in CVSS 2.0's terms.",
    )

class CvssV2AccessComplexity(EnumDefinitionImpl):
    """
    How hard the flaw is to use, in CVSS 2.0's terms.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Only under unusual, hard-to-arrange conditions.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="Under conditions that take some arranging.")
    LOW = PermissibleValue(
        text="LOW",
        description="With no special conditions.")

    _defn = EnumDefinition(
        name="CvssV2AccessComplexity",
        description="How hard the flaw is to use, in CVSS 2.0's terms.",
    )

class CvssV2Authentication(EnumDefinitionImpl):
    """
    How many logins an attacker needs, in CVSS 2.0's terms.
    """
    MULTIPLE = PermissibleValue(
        text="MULTIPLE",
        description="More than one login.")
    SINGLE = PermissibleValue(
        text="SINGLE",
        description="One login.")
    NONE = PermissibleValue(
        text="NONE",
        description="No login at all.")

    _defn = EnumDefinition(
        name="CvssV2Authentication",
        description="How many logins an attacker needs, in CVSS 2.0's terms.",
    )

class CvssV2Impact(EnumDefinitionImpl):
    """
    How much of one security property an attack could cost, in CVSS 2.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    PARTIAL = PermissibleValue(
        text="PARTIAL",
        description="Some is lost, and the attacker cannot choose all of it.")
    COMPLETE = PermissibleValue(
        text="COMPLETE",
        description="All of it is lost.")

    _defn = EnumDefinition(
        name="CvssV2Impact",
        description="How much of one security property an attack could cost, in CVSS 2.0's terms.",
    )

class CvssExploitCodeMaturity(EnumDefinitionImpl):
    """
    How far working attack code has come.
    """
    UNPROVEN = PermissibleValue(
        text="UNPROVEN",
        description="No attack code is known, or the attack is only theory.")
    PROOF_OF_CONCEPT = PermissibleValue(
        text="PROOF_OF_CONCEPT",
        description="A demonstration exists that needs skilled work to use.")
    FUNCTIONAL = PermissibleValue(
        text="FUNCTIONAL",
        description="Working attack code exists for most situations.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Attack code is reliable and widely available, or no code is needed.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssExploitCodeMaturity",
        description="How far working attack code has come.",
    )

class CvssRemediationLevel(EnumDefinitionImpl):
    """
    What kind of fix is available.
    """
    OFFICIAL_FIX = PermissibleValue(
        text="OFFICIAL_FIX",
        description="The vendor offers a complete fix.")
    TEMPORARY_FIX = PermissibleValue(
        text="TEMPORARY_FIX",
        description="The vendor offers a stopgap for now.")
    WORKAROUND = PermissibleValue(
        text="WORKAROUND",
        description="Others offer a way round the flaw that is not from the vendor.")
    UNAVAILABLE = PermissibleValue(
        text="UNAVAILABLE",
        description="No fix exists, or it cannot be applied.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssRemediationLevel",
        description="What kind of fix is available.",
    )

class CvssV2ReportConfidence(EnumDefinitionImpl):
    """
    How far the flaw has been confirmed, in CVSS 2.0's terms.
    """
    UNCONFIRMED = PermissibleValue(
        text="UNCONFIRMED",
        description="A single report or conflicting reports that nobody has checked.")
    UNCORROBORATED = PermissibleValue(
        text="UNCORROBORATED",
        description="Several unofficial sources agree, with some doubt remaining.")
    CONFIRMED = PermissibleValue(
        text="CONFIRMED",
        description="The vendor accepts it, or a working attack shows it.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2ReportConfidence",
        description="How far the flaw has been confirmed, in CVSS 2.0's terms.",
    )

class CvssV2CollateralDamagePotential(EnumDefinitionImpl):
    """
    How much loss could follow beyond the system itself.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No such loss.")
    LOW = PermissibleValue(
        text="LOW",
        description="Slight loss.")
    LOW_MEDIUM = PermissibleValue(
        text="LOW_MEDIUM",
        description="Moderate loss.")
    MEDIUM_HIGH = PermissibleValue(
        text="MEDIUM_HIGH",
        description="Significant loss.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Catastrophic loss.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2CollateralDamagePotential",
        description="How much loss could follow beyond the system itself.",
    )

class CvssV2TargetDistribution(EnumDefinitionImpl):
    """
    How much of the environment the flaw exposes.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="No systems at all, or only in a lab.")
    LOW = PermissibleValue(
        text="LOW",
        description="Up to about a quarter of systems.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="About a quarter to three quarters of systems.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="More than about three quarters of systems.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV2TargetDistribution",
        description="How much of the environment the flaw exposes.",
    )

class CvssRequirement(EnumDefinitionImpl):
    """
    How much one security property matters to the scorer.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="A loss would have limited effect.")
    MEDIUM = PermissibleValue(
        text="MEDIUM",
        description="A loss would have serious effect.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="A loss would have catastrophic effect.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssRequirement",
        description="How much one security property matters to the scorer.",
    )

class CvssV3AttackVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 3's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from a logically nearby network.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")

    _defn = EnumDefinition(
        name="CvssV3AttackVector",
        description="How far away an attacker can be, in CVSS 3's terms.",
    )

class CvssV3ModifiedAttackVector(EnumDefinitionImpl):
    """
    The attack vector as the scorer's environment changes it, in CVSS 3's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT_NETWORK = PermissibleValue(
        text="ADJACENT_NETWORK",
        description="Only from a logically nearby network.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedAttackVector",
        description="The attack vector as the scorer's environment changes it, in CVSS 3's terms.",
    )

class CvssAttackComplexity(EnumDefinitionImpl):
    """
    How much is outside the attacker's control.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Success depends on conditions the attacker must overcome or wait for.")
    LOW = PermissibleValue(
        text="LOW",
        description="The attacker can succeed again and again with no special effort.")

    _defn = EnumDefinition(
        name="CvssAttackComplexity",
        description="How much is outside the attacker's control.",
    )

class CvssModifiedAttackComplexity(EnumDefinitionImpl):
    """
    The attack complexity as the scorer's environment changes it.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Success depends on conditions the attacker must overcome or wait for.")
    LOW = PermissibleValue(
        text="LOW",
        description="The attacker can succeed again and again with no special effort.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedAttackComplexity",
        description="The attack complexity as the scorer's environment changes it.",
    )

class CvssPrivilegesRequired(EnumDefinitionImpl):
    """
    What access an attacker needs beforehand.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Administrator-level access.")
    LOW = PermissibleValue(
        text="LOW",
        description="Ordinary user access.")
    NONE = PermissibleValue(
        text="NONE",
        description="No access at all.")

    _defn = EnumDefinition(
        name="CvssPrivilegesRequired",
        description="What access an attacker needs beforehand.",
    )

class CvssModifiedPrivilegesRequired(EnumDefinitionImpl):
    """
    The access needed as the scorer's environment changes it.
    """
    HIGH = PermissibleValue(
        text="HIGH",
        description="Administrator-level access.")
    LOW = PermissibleValue(
        text="LOW",
        description="Ordinary user access.")
    NONE = PermissibleValue(
        text="NONE",
        description="No access at all.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedPrivilegesRequired",
        description="The access needed as the scorer's environment changes it.",
    )

class CvssV3UserInteraction(EnumDefinitionImpl):
    """
    Whether someone else has to take part, in CVSS 3's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    REQUIRED = PermissibleValue(
        text="REQUIRED",
        description="Someone other than the attacker has to do something.")

    _defn = EnumDefinition(
        name="CvssV3UserInteraction",
        description="Whether someone else has to take part, in CVSS 3's terms.",
    )

class CvssV3ModifiedUserInteraction(EnumDefinitionImpl):
    """
    The user interaction as the scorer's environment changes it, in CVSS 3's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    REQUIRED = PermissibleValue(
        text="REQUIRED",
        description="Someone other than the attacker has to do something.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedUserInteraction",
        description="The user interaction as the scorer's environment changes it, in CVSS 3's terms.",
    )

class CvssV3Scope(EnumDefinitionImpl):
    """
    Whether an attack can reach beyond the flawed component.
    """
    UNCHANGED = PermissibleValue(
        text="UNCHANGED",
        description="The harm stays within the same security authority.")
    CHANGED = PermissibleValue(
        text="CHANGED",
        description="The harm can reach something under another security authority.")

    _defn = EnumDefinition(
        name="CvssV3Scope",
        description="Whether an attack can reach beyond the flawed component.",
    )

class CvssV3ModifiedScope(EnumDefinitionImpl):
    """
    The scope as the scorer's environment changes it.
    """
    UNCHANGED = PermissibleValue(
        text="UNCHANGED",
        description="The harm stays within the same security authority.")
    CHANGED = PermissibleValue(
        text="CHANGED",
        description="The harm can reach something under another security authority.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV3ModifiedScope",
        description="The scope as the scorer's environment changes it.",
    )

class CvssImpact(EnumDefinitionImpl):
    """
    How much of one security property an attack could cost.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")

    _defn = EnumDefinition(
        name="CvssImpact",
        description="How much of one security property an attack could cost.",
    )

class CvssModifiedImpact(EnumDefinitionImpl):
    """
    The impact on one security property as the scorer's environment changes it.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssModifiedImpact",
        description="The impact on one security property as the scorer's environment changes it.",
    )

class CvssV3ReportConfidence(EnumDefinitionImpl):
    """
    How far the flaw has been confirmed, in CVSS 3's terms.
    """
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="Reports say something is wrong, but the cause is not clear.")
    REASONABLE = PermissibleValue(
        text="REASONABLE",
        description="Solid details exist, without full confirmation of the cause.")
    CONFIRMED = PermissibleValue(
        text="CONFIRMED",
        description="The flaw is shown beyond doubt, or the vendor accepts it.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the metric does not change the score.")

    _defn = EnumDefinition(
        name="CvssV3ReportConfidence",
        description="How far the flaw has been confirmed, in CVSS 3's terms.",
    )

class CvssV4AttackVector(EnumDefinitionImpl):
    """
    How far away an attacker can be, in CVSS 4.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT = PermissibleValue(
        text="ADJACENT",
        description="Only from something logically or physically nearby.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")

    _defn = EnumDefinition(
        name="CvssV4AttackVector",
        description="How far away an attacker can be, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedAttackVector(EnumDefinitionImpl):
    """
    The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NETWORK = PermissibleValue(
        text="NETWORK",
        description="From anywhere that can route to the system.")
    ADJACENT = PermissibleValue(
        text="ADJACENT",
        description="Only from something logically or physically nearby.")
    LOCAL = PermissibleValue(
        text="LOCAL",
        description="Only by acting on the system itself, directly or through a user.")
    PHYSICAL = PermissibleValue(
        text="PHYSICAL",
        description="Only by touching the hardware.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedAttackVector",
        description="The attack vector as the scorer's environment changes it, in CVSS 4.0's terms.",
    )

class CvssV4AttackRequirements(EnumDefinitionImpl):
    """
    Whether the attack needs conditions in the target beyond the attacker's control.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack works whatever the target's state.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The attack works only when the target is in a certain state.")

    _defn = EnumDefinition(
        name="CvssV4AttackRequirements",
        description="Whether the attack needs conditions in the target beyond the attacker's control.",
    )

class CvssV4ModifiedAttackRequirements(EnumDefinitionImpl):
    """
    The attack requirements as the scorer's environment changes them.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack works whatever the target's state.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="The attack works only when the target is in a certain state.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedAttackRequirements",
        description="The attack requirements as the scorer's environment changes them.",
    )

class CvssV4UserInteraction(EnumDefinitionImpl):
    """
    Whether someone else has to take part, in CVSS 4.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    PASSIVE = PermissibleValue(
        text="PASSIVE",
        description="Someone has to act only in the ordinary course of their work.")
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Someone has to take a deliberate step.")

    _defn = EnumDefinition(
        name="CvssV4UserInteraction",
        description="Whether someone else has to take part, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedUserInteraction(EnumDefinitionImpl):
    """
    The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="The attack needs nobody else.")
    PASSIVE = PermissibleValue(
        text="PASSIVE",
        description="Someone has to act only in the ordinary course of their work.")
    ACTIVE = PermissibleValue(
        text="ACTIVE",
        description="Someone has to take a deliberate step.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedUserInteraction",
        description="The user interaction as the scorer's environment changes it, in CVSS 4.0's terms.",
    )

class CvssV4ModifiedSubsequentImpact(EnumDefinitionImpl):
    """
    The integrity or availability impact on connected systems as the scorer's environment changes it, which may
    include a risk to safety.
    """
    NONE = PermissibleValue(
        text="NONE",
        description="Nothing is lost.")
    LOW = PermissibleValue(
        text="LOW",
        description="Some is lost, with limited consequences.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="All of it is lost, or the loss has serious consequences.")
    SAFETY = PermissibleValue(
        text="SAFETY",
        description="The loss could injure people.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the base metric stands.")

    _defn = EnumDefinition(
        name="CvssV4ModifiedSubsequentImpact",
        description="""The integrity or availability impact on connected systems as the scorer's environment changes it, which may include a risk to safety.""",
    )

class CvssV4ExploitMaturity(EnumDefinitionImpl):
    """
    How much is known about attacks on the flaw.
    """
    UNREPORTED = PermissibleValue(
        text="UNREPORTED",
        description="No demonstration or attack has been reported.")
    PROOF_OF_CONCEPT = PermissibleValue(
        text="PROOF_OF_CONCEPT",
        description="A demonstration is public, with no reported attack.")
    ATTACKED = PermissibleValue(
        text="ATTACKED",
        description="Attacks have been reported, or tools for them are public.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value, so the worst case is assumed.")

    _defn = EnumDefinition(
        name="CvssV4ExploitMaturity",
        description="How much is known about attacks on the flaw.",
    )

class CvssV4Safety(EnumDefinitionImpl):
    """
    Whether an attack could put people's safety at risk.
    """
    NEGLIGIBLE = PermissibleValue(
        text="NEGLIGIBLE",
        description="Any harm to people would be slight at most.")
    PRESENT = PermissibleValue(
        text="PRESENT",
        description="People could be seriously hurt.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Safety",
        description="Whether an attack could put people's safety at risk.",
    )

class CvssV4Automatable(EnumDefinitionImpl):
    """
    Whether every step of an attack could be automated across many targets.
    """
    NO = PermissibleValue(
        text="NO",
        description="At least one step resists automation.")
    YES = PermissibleValue(
        text="YES",
        description="Every step can be automated.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Automatable",
        description="Whether every step of an attack could be automated across many targets.",
    )

class CvssV4Recovery(EnumDefinitionImpl):
    """
    How the affected system comes back after an attack.
    """
    AUTOMATIC = PermissibleValue(
        text="AUTOMATIC",
        description="The system recovers by itself.")
    USER = PermissibleValue(
        text="USER",
        description="Someone has to step in and restore it.")
    IRRECOVERABLE = PermissibleValue(
        text="IRRECOVERABLE",
        description="The system cannot be restored.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4Recovery",
        description="How the affected system comes back after an attack.",
    )

class CvssV4ValueDensity(EnumDefinitionImpl):
    """
    How much of a resource one successful attack gains the attacker.
    """
    DIFFUSE = PermissibleValue(
        text="DIFFUSE",
        description="Each target holds little, so an attacker must take many.")
    CONCENTRATED = PermissibleValue(
        text="CONCENTRATED",
        description="A single target holds a lot.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ValueDensity",
        description="How much of a resource one successful attack gains the attacker.",
    )

class CvssV4ResponseEffort(EnumDefinitionImpl):
    """
    How much work it takes a consumer to respond to the flaw.
    """
    LOW = PermissibleValue(
        text="LOW",
        description="Little work, such as reading advice or a small configuration change.")
    MODERATE = PermissibleValue(
        text="MODERATE",
        description="Some work, with a noticeable effect on the service.")
    HIGH = PermissibleValue(
        text="HIGH",
        description="Much work, or a long outage.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ResponseEffort",
        description="How much work it takes a consumer to respond to the flaw.",
    )

class CvssV4ProviderUrgency(EnumDefinitionImpl):
    """
    How urgent the product's supplier says the flaw is, as a colour.
    """
    CLEAR = PermissibleValue(
        text="CLEAR",
        description="The supplier sees little or no urgency.")
    GREEN = PermissibleValue(
        text="GREEN",
        description="The supplier says the flaw can wait for regular work.")
    AMBER = PermissibleValue(
        text="AMBER",
        description="The supplier says the flaw matters soon.")
    RED = PermissibleValue(
        text="RED",
        description="The supplier says the flaw is at the highest urgency.")
    NOT_DEFINED = PermissibleValue(
        text="NOT_DEFINED",
        description="The scorer gave no value.")

    _defn = EnumDefinition(
        name="CvssV4ProviderUrgency",
        description="How urgent the product's supplier says the flaw is, as a colour.",
    )

# Slots
class slots:
    pass

slots.format = Slot(uri=NIST_NVD.format, name="format", curie=NIST_NVD.curie('format'),
                   model_uri=NIST_NVD.format, domain=None, range=str)

slots.timestamp = Slot(uri=NIST_NVD.timestamp, name="timestamp", curie=NIST_NVD.curie('timestamp'),
                   model_uri=NIST_NVD.timestamp, domain=None, range=Optional[Union[str, NvdTimestamp]])

slots.created = Slot(uri=NIST_NVD.created, name="created", curie=NIST_NVD.curie('created'),
                   model_uri=NIST_NVD.created, domain=None, range=Optional[Union[str, NvdTimestamp]])

slots.lastModified = Slot(uri=NIST_NVD.lastModified, name="lastModified", curie=NIST_NVD.curie('lastModified'),
                   model_uri=NIST_NVD.lastModified, domain=None, range=Optional[Union[str, NvdTimestamp]])

slots.sourceIdentifier = Slot(uri=NIST_NVD.sourceIdentifier, name="sourceIdentifier", curie=NIST_NVD.curie('sourceIdentifier'),
                   model_uri=NIST_NVD.sourceIdentifier, domain=None, range=Optional[str])

slots.source = Slot(uri=NIST_NVD.source, name="source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.source, domain=None, range=Optional[str])

slots.type = Slot(uri=NIST_NVD.type, name="type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.type, domain=None, range=Optional[str])

slots.status = Slot(uri=NIST_NVD.status, name="status", curie=NIST_NVD.curie('status'),
                   model_uri=NIST_NVD.status, domain=None, range=Optional[str])

slots.lang = Slot(uri=NIST_NVD.lang, name="lang", curie=NIST_NVD.curie('lang'),
                   model_uri=NIST_NVD.lang, domain=None, range=str)

slots.cpeName = Slot(uri=NIST_NVD.cpeName, name="cpeName", curie=NIST_NVD.curie('cpeName'),
                   model_uri=NIST_NVD.cpeName, domain=None, range=Optional[str])

slots.cpeNameId = Slot(uri=NIST_NVD.cpeNameId, name="cpeNameId", curie=NIST_NVD.curie('cpeNameId'),
                   model_uri=NIST_NVD.cpeNameId, domain=None, range=Optional[Union[str, NvdUuid]])

slots.criteria = Slot(uri=NIST_NVD.criteria, name="criteria", curie=NIST_NVD.curie('criteria'),
                   model_uri=NIST_NVD.criteria, domain=None, range=str)

slots.matchCriteriaId = Slot(uri=NIST_NVD.matchCriteriaId, name="matchCriteriaId", curie=NIST_NVD.curie('matchCriteriaId'),
                   model_uri=NIST_NVD.matchCriteriaId, domain=None, range=Union[str, NvdUuid])

slots.versionStartExcluding = Slot(uri=NIST_NVD.versionStartExcluding, name="versionStartExcluding", curie=NIST_NVD.curie('versionStartExcluding'),
                   model_uri=NIST_NVD.versionStartExcluding, domain=None, range=Optional[str])

slots.versionStartIncluding = Slot(uri=NIST_NVD.versionStartIncluding, name="versionStartIncluding", curie=NIST_NVD.curie('versionStartIncluding'),
                   model_uri=NIST_NVD.versionStartIncluding, domain=None, range=Optional[str])

slots.versionEndExcluding = Slot(uri=NIST_NVD.versionEndExcluding, name="versionEndExcluding", curie=NIST_NVD.curie('versionEndExcluding'),
                   model_uri=NIST_NVD.versionEndExcluding, domain=None, range=Optional[str])

slots.versionEndIncluding = Slot(uri=NIST_NVD.versionEndIncluding, name="versionEndIncluding", curie=NIST_NVD.curie('versionEndIncluding'),
                   model_uri=NIST_NVD.versionEndIncluding, domain=None, range=Optional[str])

slots.id = Slot(uri=NIST_NVD.id, name="id", curie=NIST_NVD.curie('id'),
                   model_uri=NIST_NVD.id, domain=None, range=URIRef)

slots.references = Slot(uri=NIST_NVD.references, name="references", curie=NIST_NVD.curie('references'),
                   model_uri=NIST_NVD.references, domain=None, range=Union[Union[dict, NvdReference], list[Union[dict, NvdReference]]])

slots.description = Slot(uri=NIST_NVD.description, name="description", curie=NIST_NVD.curie('description'),
                   model_uri=NIST_NVD.description, domain=None, range=Union[Union[dict, NvdLangString], list[Union[dict, NvdLangString]]])

slots.tags = Slot(uri=NIST_NVD.tags, name="tags", curie=NIST_NVD.curie('tags'),
                   model_uri=NIST_NVD.tags, domain=None, range=Optional[Union[str, list[str]]])

slots.url = Slot(uri=NIST_NVD.url, name="url", curie=NIST_NVD.curie('url'),
                   model_uri=NIST_NVD.url, domain=None, range=Union[str, URI],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.name = Slot(uri=NIST_NVD.name, name="name", curie=NIST_NVD.curie('name'),
                   model_uri=NIST_NVD.name, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{1,4096}$'))

slots.at = Slot(uri=NIST_NVD.at, name="at", curie=NIST_NVD.curie('at'),
                   model_uri=NIST_NVD.at, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{1,1024}$'))

slots.operator = Slot(uri=NIST_NVD.operator, name="operator", curie=NIST_NVD.curie('operator'),
                   model_uri=NIST_NVD.operator, domain=None, range=Optional[Union[str, "NvdOperator"]])

slots.negate = Slot(uri=NIST_NVD.negate, name="negate", curie=NIST_NVD.curie('negate'),
                   model_uri=NIST_NVD.negate, domain=None, range=Optional[Union[bool, Bool]])

slots.cvssData = Slot(uri=NIST_NVD.cvssData, name="cvssData", curie=NIST_NVD.curie('cvssData'),
                   model_uri=NIST_NVD.cvssData, domain=None, range=str)

slots.exploitabilityScore = Slot(uri=NIST_NVD.exploitabilityScore, name="exploitabilityScore", curie=NIST_NVD.curie('exploitabilityScore'),
                   model_uri=NIST_NVD.exploitabilityScore, domain=None, range=Optional[float])

slots.impactScore = Slot(uri=NIST_NVD.impactScore, name="impactScore", curie=NIST_NVD.curie('impactScore'),
                   model_uri=NIST_NVD.impactScore, domain=None, range=Optional[float])

slots.defaultStatus = Slot(uri=NIST_NVD.defaultStatus, name="defaultStatus", curie=NIST_NVD.curie('defaultStatus'),
                   model_uri=NIST_NVD.defaultStatus, domain=None, range=Optional[Union[str, "NvdVersionStatus"]])

slots.title = Slot(uri=NIST_NVD.title, name="title", curie=NIST_NVD.curie('title'),
                   model_uri=NIST_NVD.title, domain=None, range=str)

slots.cveChangeId = Slot(uri=NIST_NVD.cveChangeId, name="cveChangeId", curie=NIST_NVD.curie('cveChangeId'),
                   model_uri=NIST_NVD.cveChangeId, domain=None, range=Union[str, NvdUuid])

slots.version = Slot(uri=CVE.version, name="version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.version, domain=None, range=Optional[str])

slots.vectorString = Slot(uri=CVE.vectorString, name="vectorString", curie=CVE.curie('vectorString'),
                   model_uri=NIST_NVD.vectorString, domain=None, range=str)

slots.baseScore = Slot(uri=CVE.baseScore, name="baseScore", curie=CVE.curie('baseScore'),
                   model_uri=NIST_NVD.baseScore, domain=None, range=float)

slots.baseSeverity = Slot(uri=CVE.baseSeverity, name="baseSeverity", curie=CVE.curie('baseSeverity'),
                   model_uri=NIST_NVD.baseSeverity, domain=None, range=Union[str, "CvssSeverity"])

slots.temporalScore = Slot(uri=CVE.temporalScore, name="temporalScore", curie=CVE.curie('temporalScore'),
                   model_uri=NIST_NVD.temporalScore, domain=None, range=Optional[float])

slots.temporalSeverity = Slot(uri=CVE.temporalSeverity, name="temporalSeverity", curie=CVE.curie('temporalSeverity'),
                   model_uri=NIST_NVD.temporalSeverity, domain=None, range=Optional[Union[str, "CvssSeverity"]])

slots.environmentalScore = Slot(uri=CVE.environmentalScore, name="environmentalScore", curie=CVE.curie('environmentalScore'),
                   model_uri=NIST_NVD.environmentalScore, domain=None, range=Optional[float])

slots.environmentalSeverity = Slot(uri=CVE.environmentalSeverity, name="environmentalSeverity", curie=CVE.curie('environmentalSeverity'),
                   model_uri=NIST_NVD.environmentalSeverity, domain=None, range=Optional[Union[str, "CvssSeverity"]])

slots.attackVector = Slot(uri=CVE.attackVector, name="attackVector", curie=CVE.curie('attackVector'),
                   model_uri=NIST_NVD.attackVector, domain=None, range=Optional[str])

slots.attackComplexity = Slot(uri=CVE.attackComplexity, name="attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=NIST_NVD.attackComplexity, domain=None, range=Optional[str])

slots.privilegesRequired = Slot(uri=CVE.privilegesRequired, name="privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=NIST_NVD.privilegesRequired, domain=None, range=Optional[str])

slots.userInteraction = Slot(uri=CVE.userInteraction, name="userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=NIST_NVD.userInteraction, domain=None, range=Optional[str])

slots.scope = Slot(uri=CVE.scope, name="scope", curie=CVE.curie('scope'),
                   model_uri=NIST_NVD.scope, domain=None, range=Optional[Union[str, "CvssV3Scope"]])

slots.confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=NIST_NVD.confidentialityImpact, domain=None, range=Optional[str])

slots.integrityImpact = Slot(uri=CVE.integrityImpact, name="integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=NIST_NVD.integrityImpact, domain=None, range=Optional[str])

slots.availabilityImpact = Slot(uri=CVE.availabilityImpact, name="availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=NIST_NVD.availabilityImpact, domain=None, range=Optional[str])

slots.exploitCodeMaturity = Slot(uri=CVE.exploitCodeMaturity, name="exploitCodeMaturity", curie=CVE.curie('exploitCodeMaturity'),
                   model_uri=NIST_NVD.exploitCodeMaturity, domain=None, range=Optional[Union[str, "CvssExploitCodeMaturity"]])

slots.remediationLevel = Slot(uri=CVE.remediationLevel, name="remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=NIST_NVD.remediationLevel, domain=None, range=Optional[str])

slots.reportConfidence = Slot(uri=CVE.reportConfidence, name="reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=NIST_NVD.reportConfidence, domain=None, range=Optional[str])

slots.confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=NIST_NVD.confidentialityRequirement, domain=None, range=Optional[str])

slots.integrityRequirement = Slot(uri=CVE.integrityRequirement, name="integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=NIST_NVD.integrityRequirement, domain=None, range=Optional[str])

slots.availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=NIST_NVD.availabilityRequirement, domain=None, range=Optional[str])

slots.modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=NIST_NVD.modifiedAttackVector, domain=None, range=Optional[str])

slots.modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=NIST_NVD.modifiedAttackComplexity, domain=None, range=Optional[str])

slots.modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=NIST_NVD.modifiedPrivilegesRequired, domain=None, range=Optional[str])

slots.modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=NIST_NVD.modifiedUserInteraction, domain=None, range=Optional[str])

slots.modifiedScope = Slot(uri=CVE.modifiedScope, name="modifiedScope", curie=CVE.curie('modifiedScope'),
                   model_uri=NIST_NVD.modifiedScope, domain=None, range=Optional[Union[str, "CvssV3ModifiedScope"]])

slots.modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=NIST_NVD.modifiedConfidentialityImpact, domain=None, range=Optional[str])

slots.modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=NIST_NVD.modifiedIntegrityImpact, domain=None, range=Optional[str])

slots.modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=NIST_NVD.modifiedAvailabilityImpact, domain=None, range=Optional[str])

slots.nvdResponseMixin__resultsPerPage = Slot(uri=NIST_NVD.resultsPerPage, name="nvdResponseMixin__resultsPerPage", curie=NIST_NVD.curie('resultsPerPage'),
                   model_uri=NIST_NVD.nvdResponseMixin__resultsPerPage, domain=None, range=int)

slots.nvdResponseMixin__startIndex = Slot(uri=NIST_NVD.startIndex, name="nvdResponseMixin__startIndex", curie=NIST_NVD.curie('startIndex'),
                   model_uri=NIST_NVD.nvdResponseMixin__startIndex, domain=None, range=int)

slots.nvdResponseMixin__totalResults = Slot(uri=NIST_NVD.totalResults, name="nvdResponseMixin__totalResults", curie=NIST_NVD.curie('totalResults'),
                   model_uri=NIST_NVD.nvdResponseMixin__totalResults, domain=None, range=int)

slots.nvdResponseMixin__version = Slot(uri=NIST_NVD.responseVersion, name="nvdResponseMixin__version", curie=NIST_NVD.curie('responseVersion'),
                   model_uri=NIST_NVD.nvdResponseMixin__version, domain=None, range=str)

slots.nvdCveResponse__vulnerabilities = Slot(uri=NIST_NVD.vulnerabilities, name="nvdCveResponse__vulnerabilities", curie=NIST_NVD.curie('vulnerabilities'),
                   model_uri=NIST_NVD.nvdCveResponse__vulnerabilities, domain=None, range=Union[Union[dict, NvdVulnerability], list[Union[dict, NvdVulnerability]]])

slots.nvdVulnerability__cve = Slot(uri=NIST_NVD.cve, name="nvdVulnerability__cve", curie=NIST_NVD.curie('cve'),
                   model_uri=NIST_NVD.nvdVulnerability__cve, domain=None, range=Union[dict, NvdCve])

slots.nvdCve__vulnStatus = Slot(uri=NIST_NVD.vulnStatus, name="nvdCve__vulnStatus", curie=NIST_NVD.curie('vulnStatus'),
                   model_uri=NIST_NVD.nvdCve__vulnStatus, domain=None, range=Optional[Union[str, "NvdVulnStatus"]])

slots.nvdCve__published = Slot(uri=NIST_NVD.published, name="nvdCve__published", curie=NIST_NVD.curie('published'),
                   model_uri=NIST_NVD.nvdCve__published, domain=None, range=Union[str, NvdTimestamp])

slots.nvdCve__evaluatorComment = Slot(uri=NIST_NVD.evaluatorComment, name="nvdCve__evaluatorComment", curie=NIST_NVD.curie('evaluatorComment'),
                   model_uri=NIST_NVD.nvdCve__evaluatorComment, domain=None, range=Optional[str])

slots.nvdCve__evaluatorSolution = Slot(uri=NIST_NVD.evaluatorSolution, name="nvdCve__evaluatorSolution", curie=NIST_NVD.curie('evaluatorSolution'),
                   model_uri=NIST_NVD.nvdCve__evaluatorSolution, domain=None, range=Optional[str])

slots.nvdCve__evaluatorImpact = Slot(uri=NIST_NVD.evaluatorImpact, name="nvdCve__evaluatorImpact", curie=NIST_NVD.curie('evaluatorImpact'),
                   model_uri=NIST_NVD.nvdCve__evaluatorImpact, domain=None, range=Optional[str])

slots.nvdCve__cisaExploitAdd = Slot(uri=NIST_NVD.cisaExploitAdd, name="nvdCve__cisaExploitAdd", curie=NIST_NVD.curie('cisaExploitAdd'),
                   model_uri=NIST_NVD.nvdCve__cisaExploitAdd, domain=None, range=Optional[Union[str, XSDDate]])

slots.nvdCve__cisaActionDue = Slot(uri=NIST_NVD.cisaActionDue, name="nvdCve__cisaActionDue", curie=NIST_NVD.curie('cisaActionDue'),
                   model_uri=NIST_NVD.nvdCve__cisaActionDue, domain=None, range=Optional[Union[str, XSDDate]])

slots.nvdCve__cisaRequiredAction = Slot(uri=NIST_NVD.cisaRequiredAction, name="nvdCve__cisaRequiredAction", curie=NIST_NVD.curie('cisaRequiredAction'),
                   model_uri=NIST_NVD.nvdCve__cisaRequiredAction, domain=None, range=Optional[str])

slots.nvdCve__cisaVulnerabilityName = Slot(uri=NIST_NVD.cisaVulnerabilityName, name="nvdCve__cisaVulnerabilityName", curie=NIST_NVD.curie('cisaVulnerabilityName'),
                   model_uri=NIST_NVD.nvdCve__cisaVulnerabilityName, domain=None, range=Optional[str])

slots.nvdCve__cveTags = Slot(uri=NIST_NVD.cveTags, name="nvdCve__cveTags", curie=NIST_NVD.curie('cveTags'),
                   model_uri=NIST_NVD.nvdCve__cveTags, domain=None, range=Optional[Union[Union[dict, NvdCveTag], list[Union[dict, NvdCveTag]]]])

slots.nvdCve__descriptions = Slot(uri=NIST_NVD.descriptions, name="nvdCve__descriptions", curie=NIST_NVD.curie('descriptions'),
                   model_uri=NIST_NVD.nvdCve__descriptions, domain=None, range=Union[Union[dict, NvdLangString], list[Union[dict, NvdLangString]]])

slots.nvdCve__metrics = Slot(uri=NIST_NVD.metrics, name="nvdCve__metrics", curie=NIST_NVD.curie('metrics'),
                   model_uri=NIST_NVD.nvdCve__metrics, domain=None, range=Optional[Union[dict, NvdMetrics]])

slots.nvdCve__affected = Slot(uri=NIST_NVD.affected, name="nvdCve__affected", curie=NIST_NVD.curie('affected'),
                   model_uri=NIST_NVD.nvdCve__affected, domain=None, range=Optional[Union[Union[dict, NvdAffected], list[Union[dict, NvdAffected]]]])

slots.nvdCve__weaknesses = Slot(uri=NIST_NVD.weaknesses, name="nvdCve__weaknesses", curie=NIST_NVD.curie('weaknesses'),
                   model_uri=NIST_NVD.nvdCve__weaknesses, domain=None, range=Optional[Union[Union[dict, NvdWeakness], list[Union[dict, NvdWeakness]]]])

slots.nvdCve__configurations = Slot(uri=NIST_NVD.configurations, name="nvdCve__configurations", curie=NIST_NVD.curie('configurations'),
                   model_uri=NIST_NVD.nvdCve__configurations, domain=None, range=Optional[Union[Union[dict, NvdConfiguration], list[Union[dict, NvdConfiguration]]]])

slots.nvdCve__vendorComments = Slot(uri=NIST_NVD.vendorComments, name="nvdCve__vendorComments", curie=NIST_NVD.curie('vendorComments'),
                   model_uri=NIST_NVD.nvdCve__vendorComments, domain=None, range=Optional[Union[Union[dict, NvdVendorComment], list[Union[dict, NvdVendorComment]]]])

slots.nvdLangString__value = Slot(uri=NIST_NVD.langStringValue, name="nvdLangString__value", curie=NIST_NVD.curie('langStringValue'),
                   model_uri=NIST_NVD.nvdLangString__value, domain=None, range=str,
                   pattern=re.compile(r'^[\s\S]{0,4096}$'))

slots.nvdMetrics__cvssMetricV40 = Slot(uri=NIST_NVD.cvssMetricV40, name="nvdMetrics__cvssMetricV40", curie=NIST_NVD.curie('cvssMetricV40'),
                   model_uri=NIST_NVD.nvdMetrics__cvssMetricV40, domain=None, range=Optional[Union[Union[dict, NvdCvssMetricV40], list[Union[dict, NvdCvssMetricV40]]]])

slots.nvdMetrics__cvssMetricV31 = Slot(uri=NIST_NVD.cvssMetricV31, name="nvdMetrics__cvssMetricV31", curie=NIST_NVD.curie('cvssMetricV31'),
                   model_uri=NIST_NVD.nvdMetrics__cvssMetricV31, domain=None, range=Optional[Union[Union[dict, NvdCvssMetricV31], list[Union[dict, NvdCvssMetricV31]]]])

slots.nvdMetrics__cvssMetricV30 = Slot(uri=NIST_NVD.cvssMetricV30, name="nvdMetrics__cvssMetricV30", curie=NIST_NVD.curie('cvssMetricV30'),
                   model_uri=NIST_NVD.nvdMetrics__cvssMetricV30, domain=None, range=Optional[Union[Union[dict, NvdCvssMetricV30], list[Union[dict, NvdCvssMetricV30]]]])

slots.nvdMetrics__cvssMetricV2 = Slot(uri=NIST_NVD.cvssMetricV2, name="nvdMetrics__cvssMetricV2", curie=NIST_NVD.curie('cvssMetricV2'),
                   model_uri=NIST_NVD.nvdMetrics__cvssMetricV2, domain=None, range=Optional[Union[Union[dict, NvdCvssMetricV2], list[Union[dict, NvdCvssMetricV2]]]])

slots.nvdMetrics__ssvcV203 = Slot(uri=NIST_NVD.ssvcV203, name="nvdMetrics__ssvcV203", curie=NIST_NVD.curie('ssvcV203'),
                   model_uri=NIST_NVD.nvdMetrics__ssvcV203, domain=None, range=Optional[Union[Union[dict, NvdSsvcMetricV203], list[Union[dict, NvdSsvcMetricV203]]]])

slots.nvdCvssMetricV2__baseSeverity = Slot(uri=NIST_NVD.baseSeverity, name="nvdCvssMetricV2__baseSeverity", curie=NIST_NVD.curie('baseSeverity'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__baseSeverity, domain=None, range=Optional[Union[str, "NvdCvssV2Severity"]])

slots.nvdCvssMetricV2__acInsufInfo = Slot(uri=NIST_NVD.acInsufInfo, name="nvdCvssMetricV2__acInsufInfo", curie=NIST_NVD.curie('acInsufInfo'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__acInsufInfo, domain=None, range=Optional[Union[bool, Bool]])

slots.nvdCvssMetricV2__obtainAllPrivilege = Slot(uri=NIST_NVD.obtainAllPrivilege, name="nvdCvssMetricV2__obtainAllPrivilege", curie=NIST_NVD.curie('obtainAllPrivilege'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__obtainAllPrivilege, domain=None, range=Optional[Union[bool, Bool]])

slots.nvdCvssMetricV2__obtainUserPrivilege = Slot(uri=NIST_NVD.obtainUserPrivilege, name="nvdCvssMetricV2__obtainUserPrivilege", curie=NIST_NVD.curie('obtainUserPrivilege'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__obtainUserPrivilege, domain=None, range=Optional[Union[bool, Bool]])

slots.nvdCvssMetricV2__obtainOtherPrivilege = Slot(uri=NIST_NVD.obtainOtherPrivilege, name="nvdCvssMetricV2__obtainOtherPrivilege", curie=NIST_NVD.curie('obtainOtherPrivilege'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__obtainOtherPrivilege, domain=None, range=Optional[Union[bool, Bool]])

slots.nvdCvssMetricV2__userInteractionRequired = Slot(uri=NIST_NVD.userInteractionRequired, name="nvdCvssMetricV2__userInteractionRequired", curie=NIST_NVD.curie('userInteractionRequired'),
                   model_uri=NIST_NVD.nvdCvssMetricV2__userInteractionRequired, domain=None, range=Optional[Union[bool, Bool]])

slots.nvdSsvcMetricV203__ssvcData = Slot(uri=NIST_NVD.ssvcData, name="nvdSsvcMetricV203__ssvcData", curie=NIST_NVD.curie('ssvcData'),
                   model_uri=NIST_NVD.nvdSsvcMetricV203__ssvcData, domain=None, range=Union[dict, NvdSsvcData])

slots.nvdSsvcData__computed = Slot(uri=NIST_NVD.computed, name="nvdSsvcData__computed", curie=NIST_NVD.curie('computed'),
                   model_uri=NIST_NVD.nvdSsvcData__computed, domain=None, range=Optional[str])

slots.nvdSsvcData__options = Slot(uri=NIST_NVD.options, name="nvdSsvcData__options", curie=NIST_NVD.curie('options'),
                   model_uri=NIST_NVD.nvdSsvcData__options, domain=None, range=Union[Union[dict, NvdSsvcOption], list[Union[dict, NvdSsvcOption]]])

slots.nvdSsvcData__role = Slot(uri=NIST_NVD.role, name="nvdSsvcData__role", curie=NIST_NVD.curie('role'),
                   model_uri=NIST_NVD.nvdSsvcData__role, domain=None, range=str)

slots.nvdSsvcData__version = Slot(uri=NIST_NVD.ssvcVersion, name="nvdSsvcData__version", curie=NIST_NVD.curie('ssvcVersion'),
                   model_uri=NIST_NVD.nvdSsvcData__version, domain=None, range=str)

slots.nvdSsvcData__decisionTree = Slot(uri=NIST_NVD.decisionTree, name="nvdSsvcData__decisionTree", curie=NIST_NVD.curie('decisionTree'),
                   model_uri=NIST_NVD.nvdSsvcData__decisionTree, domain=None, range=Optional[Union[dict, NvdSsvcDecisionTree]])

slots.nvdSsvcData__id = Slot(uri=NIST_NVD.ssvcSubject, name="nvdSsvcData__id", curie=NIST_NVD.curie('ssvcSubject'),
                   model_uri=NIST_NVD.nvdSsvcData__id, domain=None, range=Optional[str])

slots.nvdSsvcData__decisionTreeUrl = Slot(uri=NIST_NVD.decisionTreeUrl, name="nvdSsvcData__decisionTreeUrl", curie=NIST_NVD.curie('decisionTreeUrl'),
                   model_uri=NIST_NVD.nvdSsvcData__decisionTreeUrl, domain=None, range=Optional[Union[str, URI]])

slots.nvdSsvcData__generator = Slot(uri=NIST_NVD.generator, name="nvdSsvcData__generator", curie=NIST_NVD.curie('generator'),
                   model_uri=NIST_NVD.nvdSsvcData__generator, domain=None, range=Optional[str])

slots.nvdSsvcOption__exploitation = Slot(uri=NIST_NVD.exploitation, name="nvdSsvcOption__exploitation", curie=NIST_NVD.curie('exploitation'),
                   model_uri=NIST_NVD.nvdSsvcOption__exploitation, domain=None, range=Optional[str])

slots.nvdSsvcOption__automatable = Slot(uri=NIST_NVD.automatable, name="nvdSsvcOption__automatable", curie=NIST_NVD.curie('automatable'),
                   model_uri=NIST_NVD.nvdSsvcOption__automatable, domain=None, range=Optional[str])

slots.nvdSsvcOption__technicalImpact = Slot(uri=NIST_NVD.technicalImpact, name="nvdSsvcOption__technicalImpact", curie=NIST_NVD.curie('technicalImpact'),
                   model_uri=NIST_NVD.nvdSsvcOption__technicalImpact, domain=None, range=Optional[str])

slots.nvdAffected__affectedData = Slot(uri=NIST_NVD.affectedData, name="nvdAffected__affectedData", curie=NIST_NVD.curie('affectedData'),
                   model_uri=NIST_NVD.nvdAffected__affectedData, domain=None, range=Union[Union[dict, NvdAffectedProduct], list[Union[dict, NvdAffectedProduct]]])

slots.nvdAffectedProduct__vendor = Slot(uri=NIST_NVD.vendor, name="nvdAffectedProduct__vendor", curie=NIST_NVD.curie('vendor'),
                   model_uri=NIST_NVD.nvdAffectedProduct__vendor, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,512}$'))

slots.nvdAffectedProduct__product = Slot(uri=NIST_NVD.product, name="nvdAffectedProduct__product", curie=NIST_NVD.curie('product'),
                   model_uri=NIST_NVD.nvdAffectedProduct__product, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.nvdAffectedProduct__collectionURL = Slot(uri=NIST_NVD.collectionURL, name="nvdAffectedProduct__collectionURL", curie=NIST_NVD.curie('collectionURL'),
                   model_uri=NIST_NVD.nvdAffectedProduct__collectionURL, domain=None, range=Optional[Union[str, URI]],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.nvdAffectedProduct__packageName = Slot(uri=NIST_NVD.packageName, name="nvdAffectedProduct__packageName", curie=NIST_NVD.curie('packageName'),
                   model_uri=NIST_NVD.nvdAffectedProduct__packageName, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.nvdAffectedProduct__cpes = Slot(uri=NIST_NVD.cpes, name="nvdAffectedProduct__cpes", curie=NIST_NVD.curie('cpes'),
                   model_uri=NIST_NVD.nvdAffectedProduct__cpes, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'([c][pP][eE]:/[AHOaho]?(:[A-Za-z0-9._\-~%]*){0,6})|(cpe:2\.3:[aho*\-](:(((\?*|\*?)([a-zA-Z0-9\-._]|(\\[\\*?!\x22#$%&\x27()+,/:;<=>@\[\]\^`{|}~]))+(\?*|\*?))|[*\-])){5}(:(([a-zA-Z]{2,3}(-([a-zA-Z]{2}|[0-9]{3}))?)|[*\-]))(:(((\?*|\*?)([a-zA-Z0-9\-._]|(\\[\\*?!\x22#$%&\x27()+,/:;<=>@\[\]\^`{|}~]))+(\?*|\*?))|[*\-])){4})'))

slots.nvdAffectedProduct__modules = Slot(uri=NIST_NVD.modules, name="nvdAffectedProduct__modules", curie=NIST_NVD.curie('modules'),
                   model_uri=NIST_NVD.nvdAffectedProduct__modules, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[\s\S]{1,4096}$'))

slots.nvdAffectedProduct__programFiles = Slot(uri=NIST_NVD.programFiles, name="nvdAffectedProduct__programFiles", curie=NIST_NVD.curie('programFiles'),
                   model_uri=NIST_NVD.nvdAffectedProduct__programFiles, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[\s\S]{1,1024}$'))

slots.nvdAffectedProduct__programRoutines = Slot(uri=NIST_NVD.programRoutines, name="nvdAffectedProduct__programRoutines", curie=NIST_NVD.curie('programRoutines'),
                   model_uri=NIST_NVD.nvdAffectedProduct__programRoutines, domain=None, range=Optional[Union[Union[dict, NvdProgramRoutine], list[Union[dict, NvdProgramRoutine]]]])

slots.nvdAffectedProduct__platforms = Slot(uri=NIST_NVD.platforms, name="nvdAffectedProduct__platforms", curie=NIST_NVD.curie('platforms'),
                   model_uri=NIST_NVD.nvdAffectedProduct__platforms, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^[\s\S]{0,1024}$'))

slots.nvdAffectedProduct__repo = Slot(uri=NIST_NVD.repo, name="nvdAffectedProduct__repo", curie=NIST_NVD.curie('repo'),
                   model_uri=NIST_NVD.nvdAffectedProduct__repo, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.nvdAffectedProduct__versions = Slot(uri=NIST_NVD.versions, name="nvdAffectedProduct__versions", curie=NIST_NVD.curie('versions'),
                   model_uri=NIST_NVD.nvdAffectedProduct__versions, domain=None, range=Optional[Union[Union[dict, NvdAffectedVersion], list[Union[dict, NvdAffectedVersion]]]])

slots.nvdAffectedProduct__packageURL = Slot(uri=NIST_NVD.packageURL, name="nvdAffectedProduct__packageURL", curie=NIST_NVD.curie('packageURL'),
                   model_uri=NIST_NVD.nvdAffectedProduct__packageURL, domain=None, range=Optional[Union[str, URI]],
                   pattern=re.compile(r'^[\s\S]{1,2048}$'))

slots.nvdAffectedVersion__versionType = Slot(uri=NIST_NVD.versionType, name="nvdAffectedVersion__versionType", curie=NIST_NVD.curie('versionType'),
                   model_uri=NIST_NVD.nvdAffectedVersion__versionType, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,128}$'))

slots.nvdAffectedVersion__lessThan = Slot(uri=NIST_NVD.lessThan, name="nvdAffectedVersion__lessThan", curie=NIST_NVD.curie('lessThan'),
                   model_uri=NIST_NVD.nvdAffectedVersion__lessThan, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,1024}$'))

slots.nvdAffectedVersion__lessThanOrEqual = Slot(uri=NIST_NVD.lessThanOrEqual, name="nvdAffectedVersion__lessThanOrEqual", curie=NIST_NVD.curie('lessThanOrEqual'),
                   model_uri=NIST_NVD.nvdAffectedVersion__lessThanOrEqual, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[\s\S]{1,1024}$'))

slots.nvdAffectedVersion__changes = Slot(uri=NIST_NVD.changes, name="nvdAffectedVersion__changes", curie=NIST_NVD.curie('changes'),
                   model_uri=NIST_NVD.nvdAffectedVersion__changes, domain=None, range=Optional[Union[Union[dict, NvdVersionChange], list[Union[dict, NvdVersionChange]]]])

slots.nvdConfiguration__nodes = Slot(uri=NIST_NVD.nodes, name="nvdConfiguration__nodes", curie=NIST_NVD.curie('nodes'),
                   model_uri=NIST_NVD.nvdConfiguration__nodes, domain=None, range=Union[Union[dict, NvdConfigurationNode], list[Union[dict, NvdConfigurationNode]]])

slots.nvdConfigurationNode__cpeMatch = Slot(uri=NIST_NVD.cpeMatch, name="nvdConfigurationNode__cpeMatch", curie=NIST_NVD.curie('cpeMatch'),
                   model_uri=NIST_NVD.nvdConfigurationNode__cpeMatch, domain=None, range=Union[Union[dict, NvdCpeMatch], list[Union[dict, NvdCpeMatch]]])

slots.nvdCpeMatch__vulnerable = Slot(uri=NIST_NVD.vulnerable, name="nvdCpeMatch__vulnerable", curie=NIST_NVD.curie('vulnerable'),
                   model_uri=NIST_NVD.nvdCpeMatch__vulnerable, domain=None, range=Union[bool, Bool])

slots.nvdVendorComment__organization = Slot(uri=NIST_NVD.organization, name="nvdVendorComment__organization", curie=NIST_NVD.curie('organization'),
                   model_uri=NIST_NVD.nvdVendorComment__organization, domain=None, range=str)

slots.nvdVendorComment__comment = Slot(uri=NIST_NVD.comment, name="nvdVendorComment__comment", curie=NIST_NVD.curie('comment'),
                   model_uri=NIST_NVD.nvdVendorComment__comment, domain=None, range=str)

slots.nvdCpeResponse__products = Slot(uri=NIST_NVD.products, name="nvdCpeResponse__products", curie=NIST_NVD.curie('products'),
                   model_uri=NIST_NVD.nvdCpeResponse__products, domain=None, range=Union[Union[dict, NvdCpeItem], list[Union[dict, NvdCpeItem]]])

slots.nvdCpeItem__cpe = Slot(uri=NIST_NVD.cpe, name="nvdCpeItem__cpe", curie=NIST_NVD.curie('cpe'),
                   model_uri=NIST_NVD.nvdCpeItem__cpe, domain=None, range=Union[dict, NvdCpe])

slots.nvdCpe__deprecated = Slot(uri=NIST_NVD.deprecated, name="nvdCpe__deprecated", curie=NIST_NVD.curie('deprecated'),
                   model_uri=NIST_NVD.nvdCpe__deprecated, domain=None, range=Union[bool, Bool])

slots.nvdCpe__titles = Slot(uri=NIST_NVD.titles, name="nvdCpe__titles", curie=NIST_NVD.curie('titles'),
                   model_uri=NIST_NVD.nvdCpe__titles, domain=None, range=Optional[Union[Union[dict, NvdCpeTitle], list[Union[dict, NvdCpeTitle]]]])

slots.nvdCpe__refs = Slot(uri=NIST_NVD.refs, name="nvdCpe__refs", curie=NIST_NVD.curie('refs'),
                   model_uri=NIST_NVD.nvdCpe__refs, domain=None, range=Optional[Union[Union[dict, NvdCpeReference], list[Union[dict, NvdCpeReference]]]])

slots.nvdCpe__deprecatedBy = Slot(uri=NIST_NVD.deprecatedBy, name="nvdCpe__deprecatedBy", curie=NIST_NVD.curie('deprecatedBy'),
                   model_uri=NIST_NVD.nvdCpe__deprecatedBy, domain=None, range=Optional[Union[Union[dict, NvdCpeNameLink], list[Union[dict, NvdCpeNameLink]]]])

slots.nvdCpe__deprecates = Slot(uri=NIST_NVD.deprecates, name="nvdCpe__deprecates", curie=NIST_NVD.curie('deprecates'),
                   model_uri=NIST_NVD.nvdCpe__deprecates, domain=None, range=Optional[Union[Union[dict, NvdCpeNameLink], list[Union[dict, NvdCpeNameLink]]]])

slots.nvdCpeReference__ref = Slot(uri=NIST_NVD.ref, name="nvdCpeReference__ref", curie=NIST_NVD.curie('ref'),
                   model_uri=NIST_NVD.nvdCpeReference__ref, domain=None, range=str,
                   pattern=re.compile(r'^([A-Za-z][A-Za-z0-9+.-]+):(\/\/([^@]+@)?([A-Za-z0-9.\-_~]+)(:\d+)?)?((?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@])+(?:\/(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@])*)*|(?:\/(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27()*+,;=:@])+)*)?(\?(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@]|[/?])*)?(\#(?:[A-Za-z0-9-._~]|%[A-Fa-f0-9]|[!$&\x27\[\]()*+,;=:@]|[/?])*)?$'))

slots.nvdCpeMatchResponse__matchStrings = Slot(uri=NIST_NVD.matchStrings, name="nvdCpeMatchResponse__matchStrings", curie=NIST_NVD.curie('matchStrings'),
                   model_uri=NIST_NVD.nvdCpeMatchResponse__matchStrings, domain=None, range=Union[Union[dict, NvdMatchStringItem], list[Union[dict, NvdMatchStringItem]]])

slots.nvdMatchStringItem__matchString = Slot(uri=NIST_NVD.matchString, name="nvdMatchStringItem__matchString", curie=NIST_NVD.curie('matchString'),
                   model_uri=NIST_NVD.nvdMatchStringItem__matchString, domain=None, range=Union[dict, NvdMatchString])

slots.nvdMatchString__cpeLastModified = Slot(uri=NIST_NVD.cpeLastModified, name="nvdMatchString__cpeLastModified", curie=NIST_NVD.curie('cpeLastModified'),
                   model_uri=NIST_NVD.nvdMatchString__cpeLastModified, domain=None, range=Optional[Union[str, NvdTimestamp]])

slots.nvdMatchString__matches = Slot(uri=NIST_NVD.matches, name="nvdMatchString__matches", curie=NIST_NVD.curie('matches'),
                   model_uri=NIST_NVD.nvdMatchString__matches, domain=None, range=Optional[Union[Union[dict, NvdMatchedCpe], list[Union[dict, NvdMatchedCpe]]]])

slots.nvdHistoryResponse__cveChanges = Slot(uri=NIST_NVD.cveChanges, name="nvdHistoryResponse__cveChanges", curie=NIST_NVD.curie('cveChanges'),
                   model_uri=NIST_NVD.nvdHistoryResponse__cveChanges, domain=None, range=Optional[Union[Union[dict, NvdChangeItem], list[Union[dict, NvdChangeItem]]]])

slots.nvdChangeItem__change = Slot(uri=NIST_NVD.change, name="nvdChangeItem__change", curie=NIST_NVD.curie('change'),
                   model_uri=NIST_NVD.nvdChangeItem__change, domain=None, range=Union[dict, NvdChange])

slots.nvdChange__cveId = Slot(uri=NIST_NVD.cveId, name="nvdChange__cveId", curie=NIST_NVD.curie('cveId'),
                   model_uri=NIST_NVD.nvdChange__cveId, domain=None, range=Union[str, NvdCveId],
                   pattern=re.compile(r'^CVE-[0-9]{4}-[0-9]{4,}$'))

slots.nvdChange__eventName = Slot(uri=NIST_NVD.eventName, name="nvdChange__eventName", curie=NIST_NVD.curie('eventName'),
                   model_uri=NIST_NVD.nvdChange__eventName, domain=None, range=str)

slots.nvdChange__details = Slot(uri=NIST_NVD.details, name="nvdChange__details", curie=NIST_NVD.curie('details'),
                   model_uri=NIST_NVD.nvdChange__details, domain=None, range=Optional[Union[Union[dict, NvdChangeDetail], list[Union[dict, NvdChangeDetail]]]])

slots.nvdChangeDetail__action = Slot(uri=NIST_NVD.action, name="nvdChangeDetail__action", curie=NIST_NVD.curie('action'),
                   model_uri=NIST_NVD.nvdChangeDetail__action, domain=None, range=Optional[str])

slots.nvdChangeDetail__oldValue = Slot(uri=NIST_NVD.oldValue, name="nvdChangeDetail__oldValue", curie=NIST_NVD.curie('oldValue'),
                   model_uri=NIST_NVD.nvdChangeDetail__oldValue, domain=None, range=Optional[Union[str, dict, NvdChangeObject]])

slots.nvdChangeDetail__newValue = Slot(uri=NIST_NVD.newValue, name="nvdChangeDetail__newValue", curie=NIST_NVD.curie('newValue'),
                   model_uri=NIST_NVD.nvdChangeDetail__newValue, domain=None, range=Optional[Union[str, dict, NvdChangeObject]])

slots.cvssV20__accessVector = Slot(uri=CVE.accessVector, name="cvssV20__accessVector", curie=CVE.curie('accessVector'),
                   model_uri=NIST_NVD.cvssV20__accessVector, domain=None, range=Optional[Union[str, "CvssV2AccessVector"]])

slots.cvssV20__accessComplexity = Slot(uri=CVE.accessComplexity, name="cvssV20__accessComplexity", curie=CVE.curie('accessComplexity'),
                   model_uri=NIST_NVD.cvssV20__accessComplexity, domain=None, range=Optional[Union[str, "CvssV2AccessComplexity"]])

slots.cvssV20__authentication = Slot(uri=CVE.authentication, name="cvssV20__authentication", curie=CVE.curie('authentication'),
                   model_uri=NIST_NVD.cvssV20__authentication, domain=None, range=Optional[Union[str, "CvssV2Authentication"]])

slots.cvssV20__exploitability = Slot(uri=CVE.exploitability, name="cvssV20__exploitability", curie=CVE.curie('exploitability'),
                   model_uri=NIST_NVD.cvssV20__exploitability, domain=None, range=Optional[Union[str, "CvssExploitCodeMaturity"]])

slots.cvssV20__collateralDamagePotential = Slot(uri=CVE.collateralDamagePotential, name="cvssV20__collateralDamagePotential", curie=CVE.curie('collateralDamagePotential'),
                   model_uri=NIST_NVD.cvssV20__collateralDamagePotential, domain=None, range=Optional[Union[str, "CvssV2CollateralDamagePotential"]])

slots.cvssV20__targetDistribution = Slot(uri=CVE.targetDistribution, name="cvssV20__targetDistribution", curie=CVE.curie('targetDistribution'),
                   model_uri=NIST_NVD.cvssV20__targetDistribution, domain=None, range=Optional[Union[str, "CvssV2TargetDistribution"]])

slots.cvssV40__attackRequirements = Slot(uri=CVE.attackRequirements, name="cvssV40__attackRequirements", curie=CVE.curie('attackRequirements'),
                   model_uri=NIST_NVD.cvssV40__attackRequirements, domain=None, range=Optional[Union[str, "CvssV4AttackRequirements"]])

slots.cvssV40__vulnConfidentialityImpact = Slot(uri=CVE.vulnConfidentialityImpact, name="cvssV40__vulnConfidentialityImpact", curie=CVE.curie('vulnConfidentialityImpact'),
                   model_uri=NIST_NVD.cvssV40__vulnConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__vulnIntegrityImpact = Slot(uri=CVE.vulnIntegrityImpact, name="cvssV40__vulnIntegrityImpact", curie=CVE.curie('vulnIntegrityImpact'),
                   model_uri=NIST_NVD.cvssV40__vulnIntegrityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__vulnAvailabilityImpact = Slot(uri=CVE.vulnAvailabilityImpact, name="cvssV40__vulnAvailabilityImpact", curie=CVE.curie('vulnAvailabilityImpact'),
                   model_uri=NIST_NVD.cvssV40__vulnAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subConfidentialityImpact = Slot(uri=CVE.subConfidentialityImpact, name="cvssV40__subConfidentialityImpact", curie=CVE.curie('subConfidentialityImpact'),
                   model_uri=NIST_NVD.cvssV40__subConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subIntegrityImpact = Slot(uri=CVE.subIntegrityImpact, name="cvssV40__subIntegrityImpact", curie=CVE.curie('subIntegrityImpact'),
                   model_uri=NIST_NVD.cvssV40__subIntegrityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__subAvailabilityImpact = Slot(uri=CVE.subAvailabilityImpact, name="cvssV40__subAvailabilityImpact", curie=CVE.curie('subAvailabilityImpact'),
                   model_uri=NIST_NVD.cvssV40__subAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssImpact"]])

slots.cvssV40__exploitMaturity = Slot(uri=CVE.exploitMaturity, name="cvssV40__exploitMaturity", curie=CVE.curie('exploitMaturity'),
                   model_uri=NIST_NVD.cvssV40__exploitMaturity, domain=None, range=Optional[Union[str, "CvssV4ExploitMaturity"]])

slots.cvssV40__modifiedAttackRequirements = Slot(uri=CVE.modifiedAttackRequirements, name="cvssV40__modifiedAttackRequirements", curie=CVE.curie('modifiedAttackRequirements'),
                   model_uri=NIST_NVD.cvssV40__modifiedAttackRequirements, domain=None, range=Optional[Union[str, "CvssV4ModifiedAttackRequirements"]])

slots.cvssV40__modifiedVulnConfidentialityImpact = Slot(uri=CVE.modifiedVulnConfidentialityImpact, name="cvssV40__modifiedVulnConfidentialityImpact", curie=CVE.curie('modifiedVulnConfidentialityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedVulnConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedVulnIntegrityImpact = Slot(uri=CVE.modifiedVulnIntegrityImpact, name="cvssV40__modifiedVulnIntegrityImpact", curie=CVE.curie('modifiedVulnIntegrityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedVulnIntegrityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedVulnAvailabilityImpact = Slot(uri=CVE.modifiedVulnAvailabilityImpact, name="cvssV40__modifiedVulnAvailabilityImpact", curie=CVE.curie('modifiedVulnAvailabilityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedVulnAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedSubConfidentialityImpact = Slot(uri=CVE.modifiedSubConfidentialityImpact, name="cvssV40__modifiedSubConfidentialityImpact", curie=CVE.curie('modifiedSubConfidentialityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedSubConfidentialityImpact, domain=None, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.cvssV40__modifiedSubIntegrityImpact = Slot(uri=CVE.modifiedSubIntegrityImpact, name="cvssV40__modifiedSubIntegrityImpact", curie=CVE.curie('modifiedSubIntegrityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedSubIntegrityImpact, domain=None, range=Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]])

slots.cvssV40__modifiedSubAvailabilityImpact = Slot(uri=CVE.modifiedSubAvailabilityImpact, name="cvssV40__modifiedSubAvailabilityImpact", curie=CVE.curie('modifiedSubAvailabilityImpact'),
                   model_uri=NIST_NVD.cvssV40__modifiedSubAvailabilityImpact, domain=None, range=Optional[Union[str, "CvssV4ModifiedSubsequentImpact"]])

slots.cvssV40__Safety = Slot(uri=CVE.Safety, name="cvssV40__Safety", curie=CVE.curie('Safety'),
                   model_uri=NIST_NVD.cvssV40__Safety, domain=None, range=Optional[Union[str, "CvssV4Safety"]])

slots.cvssV40__Automatable = Slot(uri=CVE.Automatable, name="cvssV40__Automatable", curie=CVE.curie('Automatable'),
                   model_uri=NIST_NVD.cvssV40__Automatable, domain=None, range=Optional[Union[str, "CvssV4Automatable"]])

slots.cvssV40__Recovery = Slot(uri=CVE.Recovery, name="cvssV40__Recovery", curie=CVE.curie('Recovery'),
                   model_uri=NIST_NVD.cvssV40__Recovery, domain=None, range=Optional[Union[str, "CvssV4Recovery"]])

slots.cvssV40__valueDensity = Slot(uri=CVE.valueDensity, name="cvssV40__valueDensity", curie=CVE.curie('valueDensity'),
                   model_uri=NIST_NVD.cvssV40__valueDensity, domain=None, range=Optional[Union[str, "CvssV4ValueDensity"]])

slots.cvssV40__vulnerabilityResponseEffort = Slot(uri=CVE.vulnerabilityResponseEffort, name="cvssV40__vulnerabilityResponseEffort", curie=CVE.curie('vulnerabilityResponseEffort'),
                   model_uri=NIST_NVD.cvssV40__vulnerabilityResponseEffort, domain=None, range=Optional[Union[str, "CvssV4ResponseEffort"]])

slots.cvssV40__providerUrgency = Slot(uri=CVE.providerUrgency, name="cvssV40__providerUrgency", curie=CVE.curie('providerUrgency'),
                   model_uri=NIST_NVD.cvssV40__providerUrgency, domain=None, range=Optional[Union[str, "CvssV4ProviderUrgency"]])

slots.NvdResponseMixin_timestamp = Slot(uri=NIST_NVD.timestamp, name="NvdResponseMixin_timestamp", curie=NIST_NVD.curie('timestamp'),
                   model_uri=NIST_NVD.NvdResponseMixin_timestamp, domain=None, range=Union[str, NvdTimestamp])

slots.NvdCveResponse_format = Slot(uri=NIST_NVD.format, name="NvdCveResponse_format", curie=NIST_NVD.curie('format'),
                   model_uri=NIST_NVD.NvdCveResponse_format, domain=NvdCveResponse, range=str)

slots.NvdCve_lastModified = Slot(uri=NIST_NVD.lastModified, name="NvdCve_lastModified", curie=NIST_NVD.curie('lastModified'),
                   model_uri=NIST_NVD.NvdCve_lastModified, domain=NvdCve, range=Union[str, NvdTimestamp])

slots.NvdCveTag_tags = Slot(uri=NIST_NVD.tags, name="NvdCveTag_tags", curie=NIST_NVD.curie('tags'),
                   model_uri=NIST_NVD.NvdCveTag_tags, domain=NvdCveTag, range=Optional[Union[Union[str, "NvdCveTagName"], list[Union[str, "NvdCveTagName"]]]])

slots.NvdReference_tags = Slot(uri=NIST_NVD.tags, name="NvdReference_tags", curie=NIST_NVD.curie('tags'),
                   model_uri=NIST_NVD.NvdReference_tags, domain=NvdReference, range=Optional[Union[Union[str, "NvdReferenceTag"], list[Union[str, "NvdReferenceTag"]]]])

slots.NvdReference_source = Slot(uri=NIST_NVD.source, name="NvdReference_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdReference_source, domain=NvdReference, range=Optional[str])

slots.NvdCvssMetricV2_source = Slot(uri=NIST_NVD.source, name="NvdCvssMetricV2_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdCvssMetricV2_source, domain=NvdCvssMetricV2, range=str)

slots.NvdCvssMetricV2_type = Slot(uri=NIST_NVD.type, name="NvdCvssMetricV2_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdCvssMetricV2_type, domain=NvdCvssMetricV2, range=Union[str, "NvdSourceType"])

slots.NvdCvssMetricV2_cvssData = Slot(uri=NIST_NVD.cvssData, name="NvdCvssMetricV2_cvssData", curie=NIST_NVD.curie('cvssData'),
                   model_uri=NIST_NVD.NvdCvssMetricV2_cvssData, domain=NvdCvssMetricV2, range=Union[dict, "CvssV20"])

slots.NvdCvssMetricV30_source = Slot(uri=NIST_NVD.source, name="NvdCvssMetricV30_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdCvssMetricV30_source, domain=NvdCvssMetricV30, range=str)

slots.NvdCvssMetricV30_type = Slot(uri=NIST_NVD.type, name="NvdCvssMetricV30_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdCvssMetricV30_type, domain=NvdCvssMetricV30, range=Union[str, "NvdSourceType"])

slots.NvdCvssMetricV30_cvssData = Slot(uri=NIST_NVD.cvssData, name="NvdCvssMetricV30_cvssData", curie=NIST_NVD.curie('cvssData'),
                   model_uri=NIST_NVD.NvdCvssMetricV30_cvssData, domain=NvdCvssMetricV30, range=Union[dict, "CvssV30"])

slots.NvdCvssMetricV31_source = Slot(uri=NIST_NVD.source, name="NvdCvssMetricV31_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdCvssMetricV31_source, domain=NvdCvssMetricV31, range=str)

slots.NvdCvssMetricV31_type = Slot(uri=NIST_NVD.type, name="NvdCvssMetricV31_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdCvssMetricV31_type, domain=NvdCvssMetricV31, range=Union[str, "NvdSourceType"])

slots.NvdCvssMetricV31_cvssData = Slot(uri=NIST_NVD.cvssData, name="NvdCvssMetricV31_cvssData", curie=NIST_NVD.curie('cvssData'),
                   model_uri=NIST_NVD.NvdCvssMetricV31_cvssData, domain=NvdCvssMetricV31, range=Union[dict, "CvssV31"])

slots.NvdCvssMetricV40_source = Slot(uri=NIST_NVD.source, name="NvdCvssMetricV40_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdCvssMetricV40_source, domain=NvdCvssMetricV40, range=str)

slots.NvdCvssMetricV40_type = Slot(uri=NIST_NVD.type, name="NvdCvssMetricV40_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdCvssMetricV40_type, domain=NvdCvssMetricV40, range=Union[str, "NvdSourceType"])

slots.NvdCvssMetricV40_cvssData = Slot(uri=NIST_NVD.cvssData, name="NvdCvssMetricV40_cvssData", curie=NIST_NVD.curie('cvssData'),
                   model_uri=NIST_NVD.NvdCvssMetricV40_cvssData, domain=NvdCvssMetricV40, range=Union[dict, "CvssV40"])

slots.NvdSsvcMetricV203_source = Slot(uri=NIST_NVD.source, name="NvdSsvcMetricV203_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdSsvcMetricV203_source, domain=NvdSsvcMetricV203, range=str)

slots.NvdAffected_source = Slot(uri=NIST_NVD.source, name="NvdAffected_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdAffected_source, domain=NvdAffected, range=str)

slots.NvdAffectedVersion_version = Slot(uri=CVE.version, name="NvdAffectedVersion_version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.NvdAffectedVersion_version, domain=NvdAffectedVersion, range=str,
                   pattern=re.compile(r'^[\s\S]{1,1024}$'))

slots.NvdAffectedVersion_status = Slot(uri=NIST_NVD.status, name="NvdAffectedVersion_status", curie=NIST_NVD.curie('status'),
                   model_uri=NIST_NVD.NvdAffectedVersion_status, domain=NvdAffectedVersion, range=Union[str, "NvdVersionStatus"])

slots.NvdVersionChange_status = Slot(uri=NIST_NVD.status, name="NvdVersionChange_status", curie=NIST_NVD.curie('status'),
                   model_uri=NIST_NVD.NvdVersionChange_status, domain=NvdVersionChange, range=Union[str, "NvdVersionStatus"])

slots.NvdWeakness_source = Slot(uri=NIST_NVD.source, name="NvdWeakness_source", curie=NIST_NVD.curie('source'),
                   model_uri=NIST_NVD.NvdWeakness_source, domain=NvdWeakness, range=str)

slots.NvdWeakness_type = Slot(uri=NIST_NVD.type, name="NvdWeakness_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdWeakness_type, domain=NvdWeakness, range=Union[str, "NvdSourceType"])

slots.NvdConfigurationNode_operator = Slot(uri=NIST_NVD.operator, name="NvdConfigurationNode_operator", curie=NIST_NVD.curie('operator'),
                   model_uri=NIST_NVD.NvdConfigurationNode_operator, domain=NvdConfigurationNode, range=Union[str, "NvdOperator"])

slots.NvdVendorComment_lastModified = Slot(uri=NIST_NVD.lastModified, name="NvdVendorComment_lastModified", curie=NIST_NVD.curie('lastModified'),
                   model_uri=NIST_NVD.NvdVendorComment_lastModified, domain=NvdVendorComment, range=Union[str, NvdTimestamp])

slots.NvdCpeResponse_format = Slot(uri=NIST_NVD.format, name="NvdCpeResponse_format", curie=NIST_NVD.curie('format'),
                   model_uri=NIST_NVD.NvdCpeResponse_format, domain=NvdCpeResponse, range=str)

slots.NvdCpe_cpeName = Slot(uri=NIST_NVD.cpeName, name="NvdCpe_cpeName", curie=NIST_NVD.curie('cpeName'),
                   model_uri=NIST_NVD.NvdCpe_cpeName, domain=NvdCpe, range=str)

slots.NvdCpe_cpeNameId = Slot(uri=NIST_NVD.cpeNameId, name="NvdCpe_cpeNameId", curie=NIST_NVD.curie('cpeNameId'),
                   model_uri=NIST_NVD.NvdCpe_cpeNameId, domain=NvdCpe, range=Union[str, NvdCpeCpeNameId])

slots.NvdCpe_created = Slot(uri=NIST_NVD.created, name="NvdCpe_created", curie=NIST_NVD.curie('created'),
                   model_uri=NIST_NVD.NvdCpe_created, domain=NvdCpe, range=Union[str, NvdTimestamp])

slots.NvdCpe_lastModified = Slot(uri=NIST_NVD.lastModified, name="NvdCpe_lastModified", curie=NIST_NVD.curie('lastModified'),
                   model_uri=NIST_NVD.NvdCpe_lastModified, domain=NvdCpe, range=Union[str, NvdTimestamp])

slots.NvdCpeReference_type = Slot(uri=NIST_NVD.type, name="NvdCpeReference_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdCpeReference_type, domain=NvdCpeReference, range=Optional[Union[str, "NvdCpeReferenceType"]])

slots.NvdCpeMatchResponse_format = Slot(uri=NIST_NVD.format, name="NvdCpeMatchResponse_format", curie=NIST_NVD.curie('format'),
                   model_uri=NIST_NVD.NvdCpeMatchResponse_format, domain=NvdCpeMatchResponse, range=str)

slots.NvdMatchString_matchCriteriaId = Slot(uri=NIST_NVD.matchCriteriaId, name="NvdMatchString_matchCriteriaId", curie=NIST_NVD.curie('matchCriteriaId'),
                   model_uri=NIST_NVD.NvdMatchString_matchCriteriaId, domain=NvdMatchString, range=Union[str, NvdMatchStringMatchCriteriaId])

slots.NvdMatchString_created = Slot(uri=NIST_NVD.created, name="NvdMatchString_created", curie=NIST_NVD.curie('created'),
                   model_uri=NIST_NVD.NvdMatchString_created, domain=NvdMatchString, range=Union[str, NvdTimestamp])

slots.NvdMatchString_lastModified = Slot(uri=NIST_NVD.lastModified, name="NvdMatchString_lastModified", curie=NIST_NVD.curie('lastModified'),
                   model_uri=NIST_NVD.NvdMatchString_lastModified, domain=NvdMatchString, range=Union[str, NvdTimestamp])

slots.NvdMatchString_status = Slot(uri=NIST_NVD.status, name="NvdMatchString_status", curie=NIST_NVD.curie('status'),
                   model_uri=NIST_NVD.NvdMatchString_status, domain=NvdMatchString, range=Union[str, "NvdMatchStringStatus"])

slots.NvdMatchedCpe_cpeName = Slot(uri=NIST_NVD.cpeName, name="NvdMatchedCpe_cpeName", curie=NIST_NVD.curie('cpeName'),
                   model_uri=NIST_NVD.NvdMatchedCpe_cpeName, domain=NvdMatchedCpe, range=str)

slots.NvdMatchedCpe_cpeNameId = Slot(uri=NIST_NVD.cpeNameId, name="NvdMatchedCpe_cpeNameId", curie=NIST_NVD.curie('cpeNameId'),
                   model_uri=NIST_NVD.NvdMatchedCpe_cpeNameId, domain=NvdMatchedCpe, range=Union[str, NvdUuid])

slots.NvdHistoryResponse_format = Slot(uri=NIST_NVD.format, name="NvdHistoryResponse_format", curie=NIST_NVD.curie('format'),
                   model_uri=NIST_NVD.NvdHistoryResponse_format, domain=NvdHistoryResponse, range=str)

slots.NvdChange_cveChangeId = Slot(uri=NIST_NVD.cveChangeId, name="NvdChange_cveChangeId", curie=NIST_NVD.curie('cveChangeId'),
                   model_uri=NIST_NVD.NvdChange_cveChangeId, domain=NvdChange, range=Union[str, NvdChangeCveChangeId])

slots.NvdChange_sourceIdentifier = Slot(uri=NIST_NVD.sourceIdentifier, name="NvdChange_sourceIdentifier", curie=NIST_NVD.curie('sourceIdentifier'),
                   model_uri=NIST_NVD.NvdChange_sourceIdentifier, domain=NvdChange, range=str)

slots.NvdChangeDetail_type = Slot(uri=NIST_NVD.type, name="NvdChangeDetail_type", curie=NIST_NVD.curie('type'),
                   model_uri=NIST_NVD.NvdChangeDetail_type, domain=NvdChangeDetail, range=str)

slots.CvssV20_version = Slot(uri=CVE.version, name="CvssV20_version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.CvssV20_version, domain=CvssV20, range=str)

slots.CvssV20_vectorString = Slot(uri=CVE.vectorString, name="CvssV20_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=NIST_NVD.CvssV20_vectorString, domain=CvssV20, range=str,
                   pattern=re.compile(r'^((AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))/)*(AV:[NAL]|AC:[LMH]|Au:[MSN]|[CIA]:[NPC]|E:(U|POC|F|H|ND)|RL:(OF|TF|W|U|ND)|RC:(UC|UR|C|ND)|CDP:(N|L|LM|MH|H|ND)|TD:(N|L|M|H|ND)|[CIA]R:(L|M|H|ND))$'))

slots.CvssV20_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV20_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=NIST_NVD.CvssV20_confidentialityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV20_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=NIST_NVD.CvssV20_integrityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV20_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=NIST_NVD.CvssV20_availabilityImpact, domain=CvssV20, range=Optional[Union[str, "CvssV2Impact"]])

slots.CvssV20_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV20_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=NIST_NVD.CvssV20_remediationLevel, domain=CvssV20, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV20_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV20_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=NIST_NVD.CvssV20_reportConfidence, domain=CvssV20, range=Optional[Union[str, "CvssV2ReportConfidence"]])

slots.CvssV20_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV20_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=NIST_NVD.CvssV20_confidentialityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV20_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV20_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=NIST_NVD.CvssV20_integrityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV20_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV20_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=NIST_NVD.CvssV20_availabilityRequirement, domain=CvssV20, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_version = Slot(uri=CVE.version, name="CvssV30_version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.CvssV30_version, domain=CvssV30, range=str)

slots.CvssV30_vectorString = Slot(uri=CVE.vectorString, name="CvssV30_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=NIST_NVD.CvssV30_vectorString, domain=CvssV30, range=str,
                   pattern=re.compile(r'^CVSS:3[.]0/((AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[UNLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XUNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'))

slots.CvssV30_attackVector = Slot(uri=CVE.attackVector, name="CvssV30_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=NIST_NVD.CvssV30_attackVector, domain=CvssV30, range=Optional[Union[str, "CvssV3AttackVector"]])

slots.CvssV30_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV30_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=NIST_NVD.CvssV30_attackComplexity, domain=CvssV30, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV30_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV30_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=NIST_NVD.CvssV30_privilegesRequired, domain=CvssV30, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV30_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV30_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=NIST_NVD.CvssV30_userInteraction, domain=CvssV30, range=Optional[Union[str, "CvssV3UserInteraction"]])

slots.CvssV30_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV30_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=NIST_NVD.CvssV30_confidentialityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV30_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=NIST_NVD.CvssV30_integrityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV30_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=NIST_NVD.CvssV30_availabilityImpact, domain=CvssV30, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV30_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV30_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=NIST_NVD.CvssV30_remediationLevel, domain=CvssV30, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV30_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV30_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=NIST_NVD.CvssV30_reportConfidence, domain=CvssV30, range=Optional[Union[str, "CvssV3ReportConfidence"]])

slots.CvssV30_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV30_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=NIST_NVD.CvssV30_confidentialityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV30_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=NIST_NVD.CvssV30_integrityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV30_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=NIST_NVD.CvssV30_availabilityRequirement, domain=CvssV30, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV30_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV30_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=NIST_NVD.CvssV30_modifiedAttackVector, domain=CvssV30, range=Optional[Union[str, "CvssV3ModifiedAttackVector"]])

slots.CvssV30_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV30_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=NIST_NVD.CvssV30_modifiedAttackComplexity, domain=CvssV30, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV30_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV30_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=NIST_NVD.CvssV30_modifiedPrivilegesRequired, domain=CvssV30, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV30_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV30_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=NIST_NVD.CvssV30_modifiedUserInteraction, domain=CvssV30, range=Optional[Union[str, "CvssV3ModifiedUserInteraction"]])

slots.CvssV30_modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="CvssV30_modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=NIST_NVD.CvssV30_modifiedConfidentialityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV30_modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="CvssV30_modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=NIST_NVD.CvssV30_modifiedIntegrityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV30_modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="CvssV30_modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=NIST_NVD.CvssV30_modifiedAvailabilityImpact, domain=CvssV30, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_version = Slot(uri=CVE.version, name="CvssV31_version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.CvssV31_version, domain=CvssV31, range=str)

slots.CvssV31_vectorString = Slot(uri=CVE.vectorString, name="CvssV31_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=NIST_NVD.CvssV31_vectorString, domain=CvssV31, range=str,
                   pattern=re.compile(r'^CVSS:3[.]1/((AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])/)*(AV:[NALP]|AC:[LH]|PR:[NLH]|UI:[NR]|S:[UC]|[CIA]:[NLH]|E:[XUPFH]|RL:[XOTWU]|RC:[XURC]|[CIA]R:[XLMH]|MAV:[XNALP]|MAC:[XLH]|MPR:[XNLH]|MUI:[XNR]|MS:[XUC]|M[CIA]:[XNLH])$'))

slots.CvssV31_attackVector = Slot(uri=CVE.attackVector, name="CvssV31_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=NIST_NVD.CvssV31_attackVector, domain=CvssV31, range=Optional[Union[str, "CvssV3AttackVector"]])

slots.CvssV31_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV31_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=NIST_NVD.CvssV31_attackComplexity, domain=CvssV31, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV31_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV31_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=NIST_NVD.CvssV31_privilegesRequired, domain=CvssV31, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV31_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV31_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=NIST_NVD.CvssV31_userInteraction, domain=CvssV31, range=Optional[Union[str, "CvssV3UserInteraction"]])

slots.CvssV31_confidentialityImpact = Slot(uri=CVE.confidentialityImpact, name="CvssV31_confidentialityImpact", curie=CVE.curie('confidentialityImpact'),
                   model_uri=NIST_NVD.CvssV31_confidentialityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_integrityImpact = Slot(uri=CVE.integrityImpact, name="CvssV31_integrityImpact", curie=CVE.curie('integrityImpact'),
                   model_uri=NIST_NVD.CvssV31_integrityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_availabilityImpact = Slot(uri=CVE.availabilityImpact, name="CvssV31_availabilityImpact", curie=CVE.curie('availabilityImpact'),
                   model_uri=NIST_NVD.CvssV31_availabilityImpact, domain=CvssV31, range=Optional[Union[str, "CvssImpact"]])

slots.CvssV31_remediationLevel = Slot(uri=CVE.remediationLevel, name="CvssV31_remediationLevel", curie=CVE.curie('remediationLevel'),
                   model_uri=NIST_NVD.CvssV31_remediationLevel, domain=CvssV31, range=Optional[Union[str, "CvssRemediationLevel"]])

slots.CvssV31_reportConfidence = Slot(uri=CVE.reportConfidence, name="CvssV31_reportConfidence", curie=CVE.curie('reportConfidence'),
                   model_uri=NIST_NVD.CvssV31_reportConfidence, domain=CvssV31, range=Optional[Union[str, "CvssV3ReportConfidence"]])

slots.CvssV31_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV31_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=NIST_NVD.CvssV31_confidentialityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV31_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=NIST_NVD.CvssV31_integrityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV31_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=NIST_NVD.CvssV31_availabilityRequirement, domain=CvssV31, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV31_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV31_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=NIST_NVD.CvssV31_modifiedAttackVector, domain=CvssV31, range=Optional[Union[str, "CvssV3ModifiedAttackVector"]])

slots.CvssV31_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV31_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=NIST_NVD.CvssV31_modifiedAttackComplexity, domain=CvssV31, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV31_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV31_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=NIST_NVD.CvssV31_modifiedPrivilegesRequired, domain=CvssV31, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV31_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV31_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=NIST_NVD.CvssV31_modifiedUserInteraction, domain=CvssV31, range=Optional[Union[str, "CvssV3ModifiedUserInteraction"]])

slots.CvssV31_modifiedConfidentialityImpact = Slot(uri=CVE.modifiedConfidentialityImpact, name="CvssV31_modifiedConfidentialityImpact", curie=CVE.curie('modifiedConfidentialityImpact'),
                   model_uri=NIST_NVD.CvssV31_modifiedConfidentialityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_modifiedIntegrityImpact = Slot(uri=CVE.modifiedIntegrityImpact, name="CvssV31_modifiedIntegrityImpact", curie=CVE.curie('modifiedIntegrityImpact'),
                   model_uri=NIST_NVD.CvssV31_modifiedIntegrityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV31_modifiedAvailabilityImpact = Slot(uri=CVE.modifiedAvailabilityImpact, name="CvssV31_modifiedAvailabilityImpact", curie=CVE.curie('modifiedAvailabilityImpact'),
                   model_uri=NIST_NVD.CvssV31_modifiedAvailabilityImpact, domain=CvssV31, range=Optional[Union[str, "CvssModifiedImpact"]])

slots.CvssV40_version = Slot(uri=CVE.version, name="CvssV40_version", curie=CVE.curie('version'),
                   model_uri=NIST_NVD.CvssV40_version, domain=CvssV40, range=str)

slots.CvssV40_vectorString = Slot(uri=CVE.vectorString, name="CvssV40_vectorString", curie=CVE.curie('vectorString'),
                   model_uri=NIST_NVD.CvssV40_vectorString, domain=CvssV40, range=str,
                   pattern=re.compile(r'^CVSS:4[.]0/AV:[NALP]/AC:[LH]/AT:[NP]/PR:[NLH]/UI:[NPA]/VC:[HLN]/VI:[HLN]/VA:[HLN]/SC:[HLN]/SI:[HLN]/SA:[HLN](/E:[XAPU])?(/CR:[XHML])?(/IR:[XHML])?(/AR:[XHML])?(/MAV:[XNALP])?(/MAC:[XLH])?(/MAT:[XNP])?(/MPR:[XNLH])?(/MUI:[XNPA])?(/MVC:[XNLH])?(/MVI:[XNLH])?(/MVA:[XNLH])?(/MSC:[XNLH])?(/MSI:[XNLHS])?(/MSA:[XNLHS])?(/S:[XNP])?(/AU:[XNY])?(/R:[XAUI])?(/V:[XDC])?(/RE:[XLMH])?(/U:(X|Clear|Green|Amber|Red))?$'))

slots.CvssV40_attackVector = Slot(uri=CVE.attackVector, name="CvssV40_attackVector", curie=CVE.curie('attackVector'),
                   model_uri=NIST_NVD.CvssV40_attackVector, domain=CvssV40, range=Optional[Union[str, "CvssV4AttackVector"]])

slots.CvssV40_attackComplexity = Slot(uri=CVE.attackComplexity, name="CvssV40_attackComplexity", curie=CVE.curie('attackComplexity'),
                   model_uri=NIST_NVD.CvssV40_attackComplexity, domain=CvssV40, range=Optional[Union[str, "CvssAttackComplexity"]])

slots.CvssV40_privilegesRequired = Slot(uri=CVE.privilegesRequired, name="CvssV40_privilegesRequired", curie=CVE.curie('privilegesRequired'),
                   model_uri=NIST_NVD.CvssV40_privilegesRequired, domain=CvssV40, range=Optional[Union[str, "CvssPrivilegesRequired"]])

slots.CvssV40_userInteraction = Slot(uri=CVE.userInteraction, name="CvssV40_userInteraction", curie=CVE.curie('userInteraction'),
                   model_uri=NIST_NVD.CvssV40_userInteraction, domain=CvssV40, range=Optional[Union[str, "CvssV4UserInteraction"]])

slots.CvssV40_confidentialityRequirement = Slot(uri=CVE.confidentialityRequirement, name="CvssV40_confidentialityRequirement", curie=CVE.curie('confidentialityRequirement'),
                   model_uri=NIST_NVD.CvssV40_confidentialityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_integrityRequirement = Slot(uri=CVE.integrityRequirement, name="CvssV40_integrityRequirement", curie=CVE.curie('integrityRequirement'),
                   model_uri=NIST_NVD.CvssV40_integrityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_availabilityRequirement = Slot(uri=CVE.availabilityRequirement, name="CvssV40_availabilityRequirement", curie=CVE.curie('availabilityRequirement'),
                   model_uri=NIST_NVD.CvssV40_availabilityRequirement, domain=CvssV40, range=Optional[Union[str, "CvssRequirement"]])

slots.CvssV40_modifiedAttackVector = Slot(uri=CVE.modifiedAttackVector, name="CvssV40_modifiedAttackVector", curie=CVE.curie('modifiedAttackVector'),
                   model_uri=NIST_NVD.CvssV40_modifiedAttackVector, domain=CvssV40, range=Optional[Union[str, "CvssV4ModifiedAttackVector"]])

slots.CvssV40_modifiedAttackComplexity = Slot(uri=CVE.modifiedAttackComplexity, name="CvssV40_modifiedAttackComplexity", curie=CVE.curie('modifiedAttackComplexity'),
                   model_uri=NIST_NVD.CvssV40_modifiedAttackComplexity, domain=CvssV40, range=Optional[Union[str, "CvssModifiedAttackComplexity"]])

slots.CvssV40_modifiedPrivilegesRequired = Slot(uri=CVE.modifiedPrivilegesRequired, name="CvssV40_modifiedPrivilegesRequired", curie=CVE.curie('modifiedPrivilegesRequired'),
                   model_uri=NIST_NVD.CvssV40_modifiedPrivilegesRequired, domain=CvssV40, range=Optional[Union[str, "CvssModifiedPrivilegesRequired"]])

slots.CvssV40_modifiedUserInteraction = Slot(uri=CVE.modifiedUserInteraction, name="CvssV40_modifiedUserInteraction", curie=CVE.curie('modifiedUserInteraction'),
                   model_uri=NIST_NVD.CvssV40_modifiedUserInteraction, domain=CvssV40, range=Optional[Union[str, "CvssV4ModifiedUserInteraction"]])
