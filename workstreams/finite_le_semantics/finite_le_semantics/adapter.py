"""Narrow adapter back to the carrier gate's open C2 task obligations."""

from __future__ import annotations

from typing import Any, Mapping


def c2_semantic_discharge(certificate: Mapping[str, Any]) -> dict[str, Any]:
    evaluated = certificate.get("status") == "evaluated"
    codes = ("le-normal-form", "le-domain-branches", "le-comparison")
    return {
        "schema": "process-geometry/c2-semantic-discharge/v0",
        "source_certificate_digest": certificate.get("certificate_digest"),
        "scope": "real single-exponential rational-rate finite Laurent/Taylor fragment",
        "obligations": [
            {"code": code, "discharged": evaluated and code in certificate.get("discharged_c2_obligations", [])}
            for code in codes
        ],
        "general_le_claim": False,
        "surreal_runtime_used": False,
    }
