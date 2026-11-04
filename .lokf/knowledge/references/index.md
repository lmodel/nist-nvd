# References

* [NIST's NVD API JSON schemas](nvd-json-schemas.md) - The JSON schemas NIST publishes at `https://csrc.nist.gov/schema/nvd/api/2.0/`: the vulnerability schema at edition 2.2.4, products and match strings at 2.0, change history at 2.0.1. NIST changes them in place, so they are pinned by SHA-256.
* [The NVD API and data feeds](nvd-api.md) - NVD's vulnerability, product and match-string APIs at `services.nvd.nist.gov/rest/json/`, and the modified feed at `nvd.nist.gov/feeds/json/cve/2.0/`, whose `.meta` file gives its size and SHA-256. NVD's `nvd.nist.gov` web pages refuse an automated client.
* [FIRST's CVSS schemas](first-cvss-schemas.md) - The CVSS JSON schemas of the Forum of Incident Response and Security Teams (FIRST), versions 2.0, 3.0, 3.1 and 4.0, of which NIST publishes copies under `external/`. Each carries FIRST's copyright notice and BSD-style licence inside the file.
