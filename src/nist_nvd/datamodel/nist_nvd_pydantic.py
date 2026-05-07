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


metamodel_version = "1.7.0"
version = "None"


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


linkml_meta = LinkMLMeta({'annotations': {'cwe_view': {'tag': 'cwe_view', 'value': 'CWE-1003'},
                     'source_context': {'tag': 'source_context',
                                        'value': 'NVD Vulnerability Detail Pages '
                                                 'and Vulnerability Status pages'},
                     'source_features': {'tag': 'source_features',
                                         'value': 'current_description,analysis_description,cvss_tabs,reference_resource_tags,cpe_configuration_types,kev_banner,weakness_source_table,status_flow'}},
     'default_prefix': 'nvd',
     'default_range': 'string',
     'description': 'NIST National Vulnerability Database (NVD) LinkML Schema.\n'
                    'Captures enriched vulnerability records, CVSS metric views, '
                    'CPE\n'
                    'applicability statements, weakness attributions, reference '
                    'resource tags,\n'
                    'KEV indicator details, and NVD lifecycle status transitions.',
     'id': 'https://w3id.org/lmodel/nist-nvd',
     'imports': ['./vulnerability_core'],
     'license': 'Apache-2.0',
     'name': 'nist-nvd',
     'prefixes': {'WIKIDATA': {'prefix_prefix': 'WIKIDATA',
                               'prefix_reference': 'https://www.wikidata.org/wiki/'},
                  'core': {'prefix_prefix': 'core',
                           'prefix_reference': 'https://w3id.org/lmodel/vulnerability-core/'},
                  'cve': {'prefix_prefix': 'cve',
                          'prefix_reference': 'https://w3id.org/lmodel/cve/'},
                  'dct': {'prefix_prefix': 'dct',
                          'prefix_reference': 'http://purl.org/dc/terms/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nvd': {'prefix_prefix': 'nvd',
                          'prefix_reference': 'https://w3id.org/lmodel/nist-nvd/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/nist-nvd',
                  'https://csrc.nist.gov/schema/nvd/api/2.0/cve_api_json_2.0.schema',
                  'https://nvd.nist.gov/vuln/detail',
                  'https://nvd.nist.gov/general/visualizations/vulnerability-visualizations/cve-status-waterfall'],
     'source': 'https://nvd.nist.gov/vuln/data-feeds',
     'source_file': 'src/nist_nvd/schema/nist_nvd.yaml',
     'subsets': {'detail_page': {'description': 'Fields represented on NVD '
                                                'vulnerability detail pages.',
                                 'from_schema': 'https://w3id.org/lmodel/nist-nvd',
                                 'name': 'detail_page'},
                 'metrics': {'description': 'CVSS and related scoring content.',
                             'from_schema': 'https://w3id.org/lmodel/nist-nvd',
                             'name': 'metrics'},
                 'nvd_feed': {'description': 'Fields published in NVD API and '
                                             'feeds.',
                              'from_schema': 'https://w3id.org/lmodel/nist-nvd',
                              'name': 'nvd_feed'},
                 'status_workflow': {'description': 'Fields representing NVD '
                                                    'status lifecycle and '
                                                    'transition context.',
                                     'from_schema': 'https://w3id.org/lmodel/nist-nvd',
                                     'name': 'status_workflow'}},
     'title': 'nist-nvd'} )

class VulnerabilityStatus(str, Enum):
    """
    Lifecycle state of a vulnerability record.
    """
    ACTIVE = "ACTIVE"
    """
    Vulnerability is actively maintained and published.
    """
    REJECTED = "REJECTED"
    """
    CVE ID was rejected and should not be used.
    """
    DISPUTED = "DISPUTED"
    """
    The vulnerability details are disputed by a party.
    """
    RESERVED = "RESERVED"
    """
    CVE ID is reserved but details are not yet published.
    """
    DEPRECATED = "DEPRECATED"
    """
    Entry has been superseded or withdrawn.
    """


class ImpactSeverity(str, Enum):
    """
    CVSS qualitative severity rating.
    """
    NONE = "NONE"
    """
    No measurable impact.
    """
    LOW = "LOW"
    """
    Limited impact; exploitation requires specific conditions.
    """
    MEDIUM = "MEDIUM"
    """
    Moderate impact; partial compromise of security properties.
    """
    HIGH = "HIGH"
    """
    High impact; significant compromise of security properties.
    """
    CRITICAL = "CRITICAL"
    """
    Critical impact; complete compromise; remote exploitation likely.
    """
    UNKNOWN = "UNKNOWN"
    """
    Severity has not been assessed or is unavailable.
    """


class CVSSVersion(str, Enum):
    """
    Supported CVSS versions displayed in NVD metrics tabs.
    """
    V2_0 = "V2_0"
    V3_0 = "V3_0"
    V3_1 = "V3_1"
    V4_0 = "V4_0"


class NVDTag(str, Enum):
    """
    NVD analysis tags attached to vulnerability records.
    """
    ANALYSIS_PENDING = "ANALYSIS_PENDING"
    ADDITIONAL_INFORMATION = "ADDITIONAL_INFORMATION"


class ScoreSource(str, Enum):
    """
    Provider of CVSS vectors and scores.
    """
    NVD = "NVD"
    CNA = "CNA"
    ADP = "ADP"
    VENDOR = "VENDOR"
    THIRD_PARTY = "THIRD_PARTY"


class ReferenceTag(str, Enum):
    """
    Resource tag labels used by NVD references.
    """
    THIRD_PARTY_ADVISORY = "THIRD_PARTY_ADVISORY"
    VENDOR_ADVISORY = "VENDOR_ADVISORY"
    ISSUE_TRACKING = "ISSUE_TRACKING"
    PATCH = "PATCH"
    TECHNICAL_DESCRIPTION = "TECHNICAL_DESCRIPTION"
    PRESS_MEDIA_COVERAGE = "PRESS_MEDIA_COVERAGE"
    VDB_ENTRY = "VDB_ENTRY"


class ConfigurationType(str, Enum):
    """
    NVD configuration rendering category.
    """
    BASIC = "BASIC"
    RUNNING_ON_WITH = "RUNNING_ON_WITH"
    ADVANCED = "ADVANCED"


class NVDWorkflowStatus(str, Enum):
    """
    Enrichment state labels shown by NVD for CVEs.
    """
    AWAITING_ENRICHMENT = "AWAITING_ENRICHMENT"
    UNDERGOING_ENRICHMENT = "UNDERGOING_ENRICHMENT"
    ENRICHED = "ENRICHED"
    MODIFIED_AFTER_ENRICHMENT = "MODIFIED_AFTER_ENRICHMENT"
    NOT_SCHEDULED = "NOT_SCHEDULED"
    REJECTED = "REJECTED"


class NVDWorkflowEventSource(str, Enum):
    """
    Source of state transition decisions in the status flow.
    """
    NVD_PROCESS = "NVD_PROCESS"
    NVD_STAFF_DECISION = "NVD_STAFF_DECISION"
    CVE_PROGRAM_PROCESS = "CVE_PROGRAM_PROCESS"
    USER_REQUEST = "USER_REQUEST"


class VersionBoundType(str, Enum):
    """
    Boundary type for version-range constraints.
    """
    START_INCLUDING = "START_INCLUDING"
    START_EXCLUDING = "START_EXCLUDING"
    END_INCLUDING = "END_INCLUDING"
    END_EXCLUDING = "END_EXCLUDING"



class Vulnerability(ConfiguredBaseModel):
    """
    Abstract base representation of a security vulnerability. Extended by source-specific schemas (KEV, CVE, NVD).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'broad_mappings': ['nvd:NVDEntry', 'kev_catalog:KevEntry'],
         'exact_mappings': ['WIKIDATA:Q631425'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['schema:SoftwareApplication', 'cwe:Weakness'],
         'slot_usage': {'cve_id': {'name': 'cve_id', 'recommended': True},
                        'description': {'name': 'description', 'recommended': True}}})

    cve_id: str = Field(default=..., description="""The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveId'],
         'domain_of': ['Vulnerability'],
         'exact_mappings': ['schema:identifier',
                            'cve:cve_id',
                            'nvd:cve_id',
                            'kev_catalog:cve_id'],
         'in_subset': ['metadata'],
         'recommended': True,
         'slot_uri': 'dct:identifier'} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title or name for this entity.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:vulnerability_name'],
         'domain_of': ['Vulnerability'],
         'exact_mappings': ['schema:name'],
         'in_subset': ['metadata'],
         'slot_uri': 'dct:title'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    published_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability was first published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'],
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:date_added'],
         'slot_uri': 'dct:created'} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'VendorComment'],
         'in_subset': ['core'],
         'slot_uri': 'dct:modified'} })
    products: Optional[list[Product]] = Field(default=None, description="""Products affected by this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    weaknesses: Optional[list[Weakness]] = Field(default=None, description="""Weakness classifications (e.g. CWE) associated with this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'NVDEntry'],
         'in_subset': ['core'],
         'related_mappings': ['cwe:Weakness']} })
    references: Optional[list[Reference]] = Field(default=None, description="""External references such as advisories and articles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'NVDEntry'], 'in_subset': ['core']} })
    impact: Optional[Impact] = Field(default=None, description="""Impact and severity assessment for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    status: Optional[VulnerabilityStatus] = Field(default=None, description="""Current lifecycle state of the vulnerability record.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:NVDWorkflowStatus'],
         'domain_of': ['Vulnerability'],
         'in_subset': ['core']} })


class Product(ConfiguredBaseModel):
    """
    Software or hardware entity affected by the vulnerability.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['schema:SoftwareApplication'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:KevEntry']})

    vendor: Optional[str] = Field(default=None, description="""Name of the vendor or organization responsible for the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'VendorComment'], 'slot_uri': 'schema:name'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness'],
         'slot_uri': 'rdfs:label'} })
    version: Optional[str] = Field(default=None, description="""Version string of the affected product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'CVSSMetric'], 'slot_uri': 'schema:version'} })
    platforms: Optional[list[str]] = Field(default=None, description="""Platforms or operating environments affected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product']} })


class Reference(ConfiguredBaseModel):
    """
    External reference such as an advisory or article.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:ExternalReference', 'nvd:NVDReference'],
         'exact_mappings': ['schema:CreativeWork'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:notes']})

    url: Optional[str] = Field(default=None, description="""URL pointing to the reference resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference'], 'slot_uri': 'schema:url'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness'],
         'slot_uri': 'rdfs:label'} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference', 'CVSSMetric', 'CVSSScoreNote', 'NVDWeakness'],
         'slot_uri': 'dct:source'} })


class Weakness(ConfiguredBaseModel):
    """
    Weakness classification from CWE or a similar taxonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cwe:Weakness', 'nvd:NVDWeakness'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    cwe_id: Optional[str] = Field(default=None, description="""CWE identifier for the weakness classification (e.g. CWE-79).""", json_schema_extra = { "linkml_meta": {'aliases': ['cweId'],
         'domain_of': ['Weakness'],
         'related_mappings': ['cwe:Weakness'],
         'slot_uri': 'dct:identifier'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'slot_uri': 'dct:description'} })

    @field_validator('cwe_id')
    def pattern_cwe_id(cls, v):
        pattern=re.compile(r"^CWE-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cwe_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cwe_id format: {v}"
            raise ValueError(err_msg)
        return v


class Impact(ConfiguredBaseModel):
    """
    Assessment of the vulnerability's impact and severity.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:CVSSMetric'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    severity: Optional[ImpactSeverity] = Field(default=None, description="""Qualitative severity rating.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:CVSSMetric'], 'domain_of': ['Impact']} })
    vector: Optional[str] = Field(default=None, description="""CVSS vector string or equivalent scoring vector expression.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:CVSSMetric'], 'domain_of': ['Impact']} })
    score: Optional[float] = Field(default=None, description="""Numeric vulnerability score (e.g. CVSS base score).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Impact']} })


class Configuration(ConfiguredBaseModel):
    """
    Logical grouping of CPE match expressions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nvd:CPEConfiguration'],
         'from_schema': 'https://w3id.org/lmodel/vulnerability-core',
         'in_subset': ['core']})

    cpe_uri: Optional[str] = Field(default=None, description="""CPE 2.2 URI identifying an affected product configuration.""", json_schema_extra = { "linkml_meta": {'aliases': ['cpeUri'],
         'domain_of': ['Configuration'],
         'related_mappings': ['nvd:CPEMatch']} })
    operator: Optional[str] = Field(default=None, description="""Logical operator (AND/OR) used in configuration node groupings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Configuration', 'CPEConfiguration']} })


class NVDEntry(Vulnerability):
    """
    Enriched NVD representation of a CVE entry.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cve:CVERecord'],
         'comments': ['Current Description is the currently visible CVE description.',
                      'Analysis Description captures the description present when NVD '
                      'enrichment occurred.'],
         'exact_mappings': ['WIKIDATA:Q631425'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['nvd_feed', 'detail_page'],
         'notes': ['If NVD and CNA CVSS values match, NVD displays only the CNA '
                   'values.',
                   'Rejected CVEs are determined by the CVE Program rather than NVD.'],
         'slot_usage': {'description': {'description': 'Current Description shown on '
                                                       'the NVD detail page.',
                                        'name': 'description',
                                        'required': True},
                        'references': {'name': 'references', 'range': 'NVDReference'},
                        'status': {'name': 'status', 'range': 'NVDWorkflowStatus'},
                        'weaknesses': {'name': 'weaknesses', 'range': 'NVDWeakness'}}})

    description_source: Optional[str] = Field(default=None, description="""Source attribution shown beneath Current Description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry'],
         'examples': [{'value': 'MITRE'}],
         'slot_uri': 'dct:source'} })
    analysis_description: Optional[str] = Field(default=None, description="""Description available at enrichment time and shown under Analysis Description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry'], 'slot_uri': 'dct:description'} })
    metrics: Optional[MetricSet] = Field(default=None, description="""Grouped CVSS displays and notes for this entry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry'], 'in_subset': ['metrics']} })
    configurations: Optional[list[CPEConfiguration]] = Field(default=None, description="""Affected software configuration statements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry'], 'in_subset': ['detail_page']} })
    references: Optional[list[NVDReference]] = Field(default=None, description="""External references such as advisories and articles.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'NVDEntry'], 'in_subset': ['core']} })
    weaknesses: Optional[list[NVDWeakness]] = Field(default=None, description="""Weakness classifications (e.g. CWE) associated with this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'NVDEntry'],
         'in_subset': ['core'],
         'related_mappings': ['cwe:Weakness']} })
    vendor_comments: Optional[list[VendorComment]] = Field(default=None, description="""Vendor comments associated with the vulnerability record.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    nvd_tags: Optional[list[NVDTag]] = Field(default=None, description="""NVD analysis tag values.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    cve_tags: Optional[list[str]] = Field(default=None, description="""CVE tags passed through the CVE List and rendered by NVD.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    workflow_status: Optional[NVDWorkflowStatus] = Field(default=None, description="""Current NVD workflow status for the CVE.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry'], 'exact_mappings': ['skos:notation']} })
    status_transitions: Optional[list[StatusTransition]] = Field(default=None, description="""Timeline of status transitions in NVD workflow.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    known_exploited: Optional[KnownExploitedVulnerability] = Field(default=None, description="""KEV banner details when this CVE is listed by CISA.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    cwe_view: Optional[str] = Field(default=None, description="""CWE view used for weakness mapping, typically CWE-1003.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    date_received: Optional[datetime ] = Field(default=None, description="""Date/time when NVD received the CVE record for processing.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDEntry']} })
    cve_id: str = Field(default=..., description="""The CVE identifier assigned by a CVE Numbering Authority (CNA). Format: CVE-YYYY-NNNNN.""", json_schema_extra = { "linkml_meta": {'aliases': ['cveId'],
         'domain_of': ['Vulnerability'],
         'exact_mappings': ['schema:identifier',
                            'cve:cve_id',
                            'nvd:cve_id',
                            'kev_catalog:cve_id'],
         'in_subset': ['metadata'],
         'recommended': True,
         'slot_uri': 'dct:identifier'} })
    title: Optional[str] = Field(default=None, description="""Short human-readable title or name for this entity.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:vulnerability_name'],
         'domain_of': ['Vulnerability'],
         'exact_mappings': ['schema:name'],
         'in_subset': ['metadata'],
         'slot_uri': 'dct:title'} })
    description: str = Field(default=..., description="""Current Description shown on the NVD detail page.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'recommended': True,
         'slot_uri': 'dct:description'} })
    published_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability was first published.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'],
         'in_subset': ['core'],
         'related_mappings': ['kev_catalog:date_added'],
         'slot_uri': 'dct:created'} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'VendorComment'],
         'in_subset': ['core'],
         'slot_uri': 'dct:modified'} })
    products: Optional[list[Product]] = Field(default=None, description="""Products affected by this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    impact: Optional[Impact] = Field(default=None, description="""Impact and severity assessment for this vulnerability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability'], 'in_subset': ['core']} })
    status: Optional[NVDWorkflowStatus] = Field(default=None, description="""Current lifecycle state of the vulnerability record.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['nvd:NVDWorkflowStatus'],
         'domain_of': ['Vulnerability'],
         'in_subset': ['core']} })


class MetricSet(ConfiguredBaseModel):
    """
    Container for all metric views across CVSS versions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cve:MetricEntry'],
         'comments': ['NVD detail pages expose button toggles for CVSS v4.0, v3.x, and '
                      'v2.0.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['metrics']})

    cvss_v4_metrics: Optional[list[CVSSMetric]] = Field(default=None, description="""CVSS v4.0 metrics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricSet']} })
    cvss_v3_metrics: Optional[list[CVSSMetric]] = Field(default=None, description="""CVSS v3.x metrics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricSet']} })
    cvss_v2_metrics: Optional[list[CVSSMetric]] = Field(default=None, description="""CVSS v2.0 metrics.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricSet']} })
    score_notes: Optional[list[CVSSScoreNote]] = Field(default=None, description="""Notes about CVSS display behavior and data provenance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MetricSet']} })


class CVSSMetric(ConfiguredBaseModel):
    """
    Individual CVSS vector and score attribution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['cve:CvssV4_0', 'cve:CvssV3', 'cve:CvssV2_0'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['metrics'],
         'slot_usage': {'source': {'name': 'source', 'range': 'ScoreSource'}}})

    version: Optional[str] = Field(default=None, description="""Version string of the affected product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'CVSSMetric'], 'slot_uri': 'schema:version'} })
    vector_string: Optional[str] = Field(default=None, description="""Serialized CVSS vector string.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSMetric']} })
    base_score: Optional[float] = Field(default=None, ge=0, le=10, json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSMetric']} })
    base_severity: Optional[ImpactSeverity] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSMetric']} })
    source: Optional[ScoreSource] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference', 'CVSSMetric', 'CVSSScoreNote', 'NVDWeakness'],
         'slot_uri': 'dct:source'} })
    provider_label: Optional[str] = Field(default=None, description="""Display label for score source, such as NIST NVD or CNA Example.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSMetric']} })
    scoring_justification: Optional[str] = Field(default=None, description="""Supplemental rationale or caveat for a CVSS score.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSMetric']} })


class CVSSScoreNote(ConfiguredBaseModel):
    """
    Additional explanatory note for CVSS display conditions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-nvd', 'in_subset': ['metrics']})

    note_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSScoreNote'], 'slot_uri': 'dct:identifier'} })
    message: Optional[str] = Field(default=None, description="""Human-readable explanatory note text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSScoreNote']} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference', 'CVSSMetric', 'CVSSScoreNote', 'NVDWeakness'],
         'slot_uri': 'dct:source'} })
    created: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['CVSSScoreNote'], 'slot_uri': 'dct:created'} })


class CPEConfiguration(ConfiguredBaseModel):
    """
    Logical grouping of CPE match criteria for affected software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cve:CpeApplicabilityElement'],
         'comments': ['Supported rendering categories include Basic, Running On/With, '
                      'and Advanced.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['detail_page']})

    configuration_id: Optional[str] = Field(default=None, description="""Display identifier, for example Configuration 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEConfiguration']} })
    configuration_type: Optional[ConfigurationType] = Field(default=None, description="""Simplified configuration rendering type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEConfiguration']} })
    operator: Optional[str] = Field(default=None, description="""Logical operator (AND/OR) used in configuration node groupings.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Configuration', 'CPEConfiguration']} })
    children: Optional[list[CPEConfiguration]] = Field(default=None, description="""Child configuration nodes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEConfiguration']} })
    matches: Optional[list[CPEMatch]] = Field(default=None, description="""Match criteria for this configuration node.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEConfiguration']} })
    summary: Optional[str] = Field(default=None, description="""Human-oriented explanation of configuration logic.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEConfiguration']} })


class CPEMatch(ConfiguredBaseModel):
    """
    Leaf-level CPE match criterion and optional version bounds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'exact_mappings': ['cve:CpeMatch'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['detail_page'],
         'notes': ['Matching CPE names can be exposed in expanded detail-page '
                   'sections.']})

    match_criteria_id: Optional[str] = Field(default=None, description="""Identifier for a match criterion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    criteria: Optional[str] = Field(default=None, description="""CPE 2.3 match criterion expression.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    cpe23_uri: Optional[str] = Field(default=None, description="""Concrete CPE 2.3 URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    vulnerable: Optional[bool] = Field(default=None, description="""Whether the criterion indicates a vulnerable product context.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    version_start_including: Optional[str] = Field(default=None, description="""Inclusive lower version bound.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    version_start_excluding: Optional[str] = Field(default=None, description="""Exclusive lower version bound.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    version_end_including: Optional[str] = Field(default=None, description="""Inclusive upper version bound.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    version_end_excluding: Optional[str] = Field(default=None, description="""Exclusive upper version bound.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })
    matched_cpe_names: Optional[list[str]] = Field(default=None, description="""Expanded list of matching CPE names shown in detail UI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['CPEMatch']} })


class NVDReference(Reference):
    """
    Reference URL with NVD resource tags.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cve:CveReference'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['detail_page'],
         'slot_usage': {'source': {'name': 'source', 'required': False},
                        'url': {'name': 'url', 'required': True}}})

    resource_tags: Optional[list[ReferenceTag]] = Field(default=None, description="""NVD resource categories attached to references.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NVDReference']} })
    url: str = Field(default=..., description="""URL pointing to the reference resource.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference'], 'slot_uri': 'schema:url'} })
    name: Optional[str] = Field(default=None, description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness'],
         'slot_uri': 'rdfs:label'} })
    source: Optional[str] = Field(default=None, description="""Source or origin of the reference or data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference', 'CVSSMetric', 'CVSSScoreNote', 'NVDWeakness'],
         'slot_uri': 'dct:source'} })


class NVDWeakness(Weakness):
    """
    Weakness row as presented on the NVD detail page.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['cve:ProblemType'],
         'comments': ['NVD uses CWE-1003 for simplified mapping of published '
                      'vulnerabilities.'],
         'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['detail_page'],
         'slot_usage': {'cwe_id': {'name': 'cwe_id', 'required': True},
                        'name': {'name': 'name', 'required': True},
                        'source': {'description': 'Source column value, such as NIST '
                                                  'or ASSIGNER.',
                                   'name': 'source',
                                   'required': True}}})

    source: str = Field(default=..., description="""Source column value, such as NIST or ASSIGNER.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Reference', 'CVSSMetric', 'CVSSScoreNote', 'NVDWeakness'],
         'slot_uri': 'dct:source'} })
    cwe_id: str = Field(default=..., description="""CWE identifier for the weakness classification (e.g. CWE-79).""", json_schema_extra = { "linkml_meta": {'aliases': ['cweId'],
         'domain_of': ['Weakness'],
         'related_mappings': ['cwe:Weakness'],
         'slot_uri': 'dct:identifier'} })
    name: str = Field(default=..., description="""Name of the entity (product, weakness, reference, etc.).""", json_schema_extra = { "linkml_meta": {'aliases': ['label', 'product'],
         'domain_of': ['Product', 'Reference', 'Weakness'],
         'slot_uri': 'rdfs:label'} })
    description: Optional[str] = Field(default=None, description="""Narrative description of the vulnerability.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['kev_catalog:short_description'],
         'domain_of': ['Vulnerability', 'Weakness'],
         'exact_mappings': ['schema:description'],
         'in_subset': ['core'],
         'slot_uri': 'dct:description'} })

    @field_validator('cwe_id')
    def pattern_cwe_id(cls, v):
        pattern=re.compile(r"^CWE-[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid cwe_id format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid cwe_id format: {v}"
            raise ValueError(err_msg)
        return v


class VendorComment(ConfiguredBaseModel):
    """
    Comment provided by vendor during NVD analysis.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-nvd', 'in_subset': ['nvd_feed']})

    vendor: Optional[str] = Field(default=None, description="""Name of the vendor or organization responsible for the product.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Product', 'VendorComment'], 'slot_uri': 'schema:name'} })
    comment: Optional[str] = Field(default=None, description="""Vendor-provided comment text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['VendorComment']} })
    last_modified_date: Optional[datetime ] = Field(default=None, description="""Date and time the vulnerability record was last modified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Vulnerability', 'VendorComment'],
         'in_subset': ['core'],
         'slot_uri': 'dct:modified'} })


class KnownExploitedVulnerability(ConfiguredBaseModel):
    """
    CISA KEV information rendered on the NVD detail page.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['detail_page'],
         'notes': ['Present only when the CVE appears in the CISA Known Exploited '
                   'Vulnerabilities catalog.']})

    date_added: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['KnownExploitedVulnerability'], 'slot_uri': 'dct:created'} })
    due_date: Optional[date] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['KnownExploitedVulnerability'], 'slot_uri': 'dct:date'} })
    required_action: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['KnownExploitedVulnerability'], 'slot_uri': 'dct:description'} })
    kev_reference: Optional[str] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['KnownExploitedVulnerability'], 'slot_uri': 'schema:url'} })


class StatusTransition(ConfiguredBaseModel):
    """
    State transition event in NVD enrichment workflow.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-nvd',
         'in_subset': ['status_workflow']})

    transition_id: str = Field(default=..., json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition'], 'slot_uri': 'dct:identifier'} })
    from_status: Optional[NVDWorkflowStatus] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition']} })
    to_status: Optional[NVDWorkflowStatus] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition']} })
    event_source: Optional[NVDWorkflowEventSource] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition']} })
    transition_time: Optional[datetime ] = Field(default=None, json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition'], 'slot_uri': 'dct:modified'} })
    rationale: Optional[str] = Field(default=None, description="""Optional reason for transition.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StatusTransition']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Vulnerability.model_rebuild()
Product.model_rebuild()
Reference.model_rebuild()
Weakness.model_rebuild()
Impact.model_rebuild()
Configuration.model_rebuild()
NVDEntry.model_rebuild()
MetricSet.model_rebuild()
CVSSMetric.model_rebuild()
CVSSScoreNote.model_rebuild()
CPEConfiguration.model_rebuild()
CPEMatch.model_rebuild()
NVDReference.model_rebuild()
NVDWeakness.model_rebuild()
VendorComment.model_rebuild()
KnownExploitedVulnerability.model_rebuild()
StatusTransition.model_rebuild()
