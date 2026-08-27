"""Deterministic carrier certificate and a fail-closed replay checker."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
from typing import Any, Mapping

from .features import infer_features
from .ir import ScaleExpr, expr_from_data
from .model import Carrier, DecisionStatus, capability


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class CostLedger:
    input_nodes: int
    feature_visits: int
    construction_height: int | None
    compilation_steps: int
    certificate_bytes: int
    replay_steps: int
    residual_items: int
    decoder_steps: int


@dataclass(frozen=True)
class Obligation:
    code: str
    statement: str
    discharged: bool
    witness: str | None = None


@dataclass(frozen=True)
class CarrierDecisionCertificate:
    schema: str
    status: DecisionStatus
    input_digest: str
    minimum_declared_carrier: Carrier | None
    requested_carrier: Carrier | None
    construction_height: int | None
    features: tuple[str, ...]
    feature_witnesses: tuple[dict[str, str], ...]
    syntax_capability: str
    normal_form_capability: str
    comparison_capability: str
    lowering_obligations: tuple[Obligation, ...]
    upgrade_obligations: tuple[Obligation, ...]
    task_obligations: tuple[Obligation, ...]
    eliminability: str | None
    claim_scope: str
    failures: tuple[dict[str, str], ...]
    cost: CostLedger
    certificate_digest: str

    def payload(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data["minimum_declared_carrier"] = self.minimum_declared_carrier.value if self.minimum_declared_carrier else None
        data["requested_carrier"] = self.requested_carrier.value if self.requested_carrier else None
        data.pop("certificate_digest", None)
        return data

    def to_data(self) -> dict[str, Any]:
        return {**self.payload(), "certificate_digest": self.certificate_digest}


@dataclass(frozen=True)
class ReplayResult:
    valid: bool
    steps: int
    failures: tuple[str, ...]


def replay_certificate(expr_data: Mapping[str, Any], certificate_data: Mapping[str, Any]) -> ReplayResult:
    """Recompute all positive finite-carrier claims without compiler state."""

    failures: list[str] = []
    steps = 0
    steps += 1
    if digest(expr_data) != certificate_data.get("input_digest"):
        failures.append("input-digest-mismatch")
    stored_digest = certificate_data.get("certificate_digest")
    payload = dict(certificate_data)
    payload.pop("certificate_digest", None)
    steps += 1
    if digest(payload) != stored_digest:
        failures.append("certificate-digest-mismatch")
    expr = expr_from_data(expr_data)
    report = infer_features(expr)
    steps += report.node_count
    if sorted(report.features) != list(certificate_data.get("features", [])):
        failures.append("feature-set-mismatch")
    if report.construction_height != certificate_data.get("construction_height"):
        failures.append("construction-height-mismatch")

    minimum = certificate_data.get("minimum_declared_carrier")
    status = certificate_data.get("status")
    independently_minimal = next(
        (
            candidate
            for candidate in (Carrier.C0, Carrier.C1, Carrier.C2)
            if report.features <= capability(candidate).supports
        ),
        None,
    ) if not report.symbolic_height else None
    if minimum:
        carrier = Carrier(minimum)
        cap = capability(carrier)
        steps += len(report.features)
        if not report.features <= cap.supports:
            failures.append("carrier-lacks-feature-closure")
        if carrier in {Carrier.C3, Carrier.C4} or not cap.executable:
            failures.append("conditional-carrier-reported-as-executable")
        if independently_minimal is not carrier:
            failures.append("carrier-not-minimum-in-frozen-matrix")
    if status == DecisionStatus.SUFFICIENT.value:
        if not minimum:
            failures.append("positive-certificate-missing-carrier")
        if certificate_data.get("eliminability") != "surreal-runtime-eliminable-for-frozen-syntax-decision":
            failures.append("positive-finite-certificate-missing-eliminability")
    if minimum and certificate_data.get("eliminability") != "surreal-runtime-eliminable-for-frozen-syntax-decision":
        failures.append("finite-shadow-missing-eliminability")
    if minimum == Carrier.C2.value:
        if certificate_data.get("normal_form_capability") != "not-implemented":
            failures.append("c2-overclaims-normal-form")
        if certificate_data.get("comparison_capability") != "not-implemented":
            failures.append("c2-overclaims-comparison")
        task_obligations = certificate_data.get("task_obligations", [])
        expected_codes = {"le-normal-form", "le-domain-branches", "le-comparison"}
        actual_codes = {item.get("code") for item in task_obligations}
        all_open = all(item.get("discharged") is False for item in task_obligations)
        if actual_codes != expected_codes or len(task_obligations) != 3 or not all_open:
            failures.append("c2-task-obligations-invalid")
    return ReplayResult(not failures, steps, tuple(failures))
