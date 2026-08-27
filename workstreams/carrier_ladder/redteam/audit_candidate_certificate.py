"""Independent red-team checks for carrier-decision certificates.

The checks are intentionally schema-light so they can be run before the
compiler stabilizes.  They audit forbidden evidence patterns rather than
reimplementing the compiler's positive decision logic.
"""

from __future__ import annotations

from typing import Any


ORDER = {"C0": 0, "C1": 1, "C2": 2, "C3": 3, "C4": 4}


def audit(certificate: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    selected = certificate.get("selected_carrier")
    passed = certificate.get("passed_carriers", [])

    if selected not in ORDER:
        failures.append("unknown-selected-carrier")
    if passed:
        unknown = [item for item in passed if item not in ORDER]
        if unknown:
            failures.append("unknown-passed-carrier")
        elif selected in ORDER:
            least = min(passed, key=ORDER.__getitem__)
            if ORDER[selected] > ORDER[least]:
                failures.append("overpromotion-smaller-carrier-already-passed")

    evidence = certificate.get("evidence", {})
    if certificate.get("symbolic_height_credit"):
        if evidence.get("mode") in {"fixed_unrolling", "bounded_samples"}:
            failures.append("fixed-height-masquerades-as-symbolic-height")
        if evidence.get("unrolled_height") is not None:
            failures.append("symbolic-height-certificate-contains-unrolling-bound")

    if selected in {"C3", "C4"}:
        if evidence.get("kind") in {"embedding", "membership", "existence_only"}:
            failures.append("embedding-or-existence-masquerades-as-algorithm")
        if not certificate.get("smaller_carrier_obstruction"):
            failures.append("missing-smaller-carrier-obstruction")

    forbidden_keys = {"full_trace", "source_expr", "heldout_expected_answer"}
    if forbidden_keys.intersection(certificate):
        failures.append("certificate-stores-forbidden-trace-or-answer")

    if certificate.get("compression_claim"):
        cert_bytes = certificate.get("certificate_bytes")
        source_trace_bytes = certificate.get("source_plus_full_trace_bytes")
        if not isinstance(cert_bytes, int) or not isinstance(source_trace_bytes, int):
            failures.append("compression-cost-missing")
        elif cert_bytes >= 0.95 * source_trace_bytes:
            failures.append("certificate-does-not-compress-source-plus-trace")

    return failures
