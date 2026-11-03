# nist-nvd

This project is a LinkML model of the JSON responses of the National Vulnerability Database (NVD) API 2.0, from the JSON schemas that the National Institute of Standards and Technology (NIST) publishes. It covers the vulnerability response, which NVD's data feeds share, and the product, match-string and change-history responses. NVD's own keys and values are the schema's, so a real response validates unchanged.

This product uses data from the NVD API but is not endorsed or certified by the NVD.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the model is named, where it departs from NIST's files and what it leaves out
- [`nist_nvd.yaml`](schema/nist_nvd.yaml): the schema

## Validating data

NVD has four kinds of response and no document that holds them, so name the kind:

```bash
linkml-validate -s src/nist_nvd/schema/nist_nvd.yaml -C NvdCveResponse response.json
linkml-validate -s src/nist_nvd/schema/nist_nvd.yaml -C NvdCpeResponse response.json
linkml-validate -s src/nist_nvd/schema/nist_nvd.yaml -C NvdCpeMatchResponse response.json
linkml-validate -s src/nist_nvd/schema/nist_nvd.yaml -C NvdHistoryResponse response.json
```

A whole feed works, though the validator's messages make it slow and large; `tests/test_nvd_feed.py` validates a feed one record at a time, as the class `NvdCve`. `tests/test_data.py` holds every example to the same checks. The validator checks:

- each key, value list, pattern, cardinality and bound of NIST's files, and refuses a key they do not name;
- that a `NvdAffectedVersion` is a single version or a range, as NIST's `oneOf` has it: a limit needs a numbering scheme, a range has one upper limit, and status changes need one;
- each CVSS score against the CVSS module of [lmodel/cve](https://github.com/lmodel/cve), including its severity bands.

LinkML does not write two of NIST's statements into the JSON Schema, so `tests/nvd_rules.py` checks them over the examples and the feed: that a list NIST marks unique has no repeats, and that a CVSS 4.0 score is a multiple of 0.1.

The generated Python models check less. The dataclasses refuse an empty list for a required key, as a rejected record's `references` has, and neither model checks a pattern from a type or applies a rule. The dataclasses turn a change's list value into a string, and the Pydantic model refuses a change's list or object value and any SSVC decision point beyond the three the data holds.
