"""NVD's statements that the generated JSON Schema does not check.

LinkML states `list_elements_unique`, but no generator writes it (linkml issue
4194), so `uniqueItems` in NVD's files is checked here. LinkML has no way to
state `multipleOf`. Each function takes a plain record and yields a problem as
(rule, where, what).
"""

from decimal import Decimal


def _dumps_key(item):
    """A value in a form that compares equal when two JSON values are equal."""
    if isinstance(item, dict):
        return tuple(sorted((k, _dumps_key(v)) for k, v in item.items()))
    if isinstance(item, list):
        return tuple(_dumps_key(v) for v in item)
    return item


def _repeated(items):
    seen = set()
    for item in items:
        key = _dumps_key(item)
        if key in seen:
            return item
        seen.add(key)
    return None


def _unique(where, holder, keys):
    for key in keys:
        found = _repeated(holder.get(key) or [])
        if found is not None:
            yield ("unique-items", f"{where}/{key}", found)


def product_problems(product, where=""):
    """`uniqueItems` on an affected product's lists and a version's changes."""
    yield from _unique(
        where,
        product,
        ("cpes", "modules", "programFiles", "programRoutines", "platforms", "versions"),
    )
    for n, version in enumerate(product.get("versions") or []):
        yield from _unique(f"{where}/versions/{n}", version, ("changes",))


def ssvc_problems(data, where=""):
    """`uniqueItems` on an SSVC decision's options."""
    yield from _unique(where, data, ("options",))


def cvss_v40_problems(data, where=""):
    """`multipleOf: 0.1` on the scores of NVD's copy of CVSS 4.0, in decimal
    arithmetic, since 7.1 is not a multiple of 0.1 in binary floating point."""
    for key in ("baseScore", "threatScore", "environmentalScore"):
        if key in data and Decimal(str(data[key])) % Decimal("0.1") != 0:
            yield ("score-step", f"{where}/{key}", data[key])


def cve_problems(cve, where=""):
    """Every rule above, over one vulnerability."""
    metrics = cve.get("metrics") or {}
    for n, metric in enumerate(metrics.get("ssvcV203") or []):
        yield from ssvc_problems(metric["ssvcData"], f"{where}/metrics/ssvcV203/{n}/ssvcData")
    for n, metric in enumerate(metrics.get("cvssMetricV40") or []):
        yield from cvss_v40_problems(
            metric["cvssData"], f"{where}/metrics/cvssMetricV40/{n}/cvssData"
        )
    for a, affected in enumerate(cve.get("affected") or []):
        for p, product in enumerate(affected.get("affectedData") or []):
            yield from product_problems(product, f"{where}/affected/{a}/affectedData/{p}")
