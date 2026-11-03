# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to change the schema: edit `src/nist_nvd/schema/`, run `just lint`, `just gen-project`, `just gen-doc` and `just lokf-adapt`, then `just test`, and commit the output.
* [Validate an NVD response](validate-an-nvd-response.md) - How to validate a file against the schema with `linkml-validate`, naming the kind of response with `-C NvdCveResponse`, `NvdCpeResponse`, `NvdCpeMatchResponse` or `NvdHistoryResponse`.
* [Move the upstream pins](move-the-upstream-pins.md) - What to do when the watch reports that a file of NIST's differs: compare it with `upstream/`, move the copy, the pin in `scripts/check_upstream_release.py` and the module's header together, and let `tests/test_upstream.py` say what the schema must follow.
* [Release a version](release.md) - How a version is released: changelog entries under `## [Unreleased]`, a releasing commit type, the `v0.0.0` baseline tag before the first release, and `semantic-release.yml`, which tags and publishes on the merge and dispatches the knowledge release.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out with a reason.
