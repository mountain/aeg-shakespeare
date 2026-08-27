"""Deterministic fail-closed replay for finite-LE semantic certificates."""

from __future__ import annotations

from typing import Any, Mapping

from .evaluator import evaluate
from .model import EvaluatorBudget, ReplayResult, canonical_json, digest


def replay_certificate(
    source: Mapping[str, Any],
    context: Mapping[str, Any],
    observer: Mapping[str, Any],
    certificate: Mapping[str, Any],
    budget: EvaluatorBudget | None = None,
) -> ReplayResult:
    failures: list[str] = []
    steps = 3
    if certificate.get("source_digest") != digest(source):
        failures.append("source-digest-mismatch")
    if certificate.get("context_digest") != digest(context):
        failures.append("context-digest-mismatch")
    if certificate.get("observer_digest") != digest(observer):
        failures.append("observer-digest-mismatch")
    payload = dict(certificate)
    stored_digest = payload.pop("certificate_digest", None)
    if digest(payload) != stored_digest:
        failures.append("certificate-digest-mismatch")

    derived = evaluate(source, context, observer, budget).to_data()
    steps += int(derived["cost"]["replay_steps"])
    for field in (
        "schema", "status", "q", "rates", "chart", "normal_form", "limit", "retained_order",
        "cancellation_jump", "residual", "domain_witnesses",
        "discharged_c2_obligations", "failures", "claim_scope", "cost",
    ):
        if canonical_json(certificate.get(field)) != canonical_json(derived.get(field)):
            failures.append(f"{field}-mismatch")
    obligations = tuple(certificate.get("discharged_c2_obligations", ()))
    if certificate.get("status") == "evaluated" and obligations != (
        "le-normal-form", "le-domain-branches", "le-comparison"
    ):
        failures.append("c2-obligation-overclaim-or-omission")
    return ReplayResult(not failures, tuple(failures), steps)
