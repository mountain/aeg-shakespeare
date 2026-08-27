"""Typed records for the frozen finite-LE semantic gate."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum
from hashlib import sha256
import json
from typing import Any


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def digest(value: Any) -> str:
    return sha256(canonical_json(value).encode("utf-8")).hexdigest()


class Status(str, Enum):
    EVALUATED = "evaluated"
    UNSUPPORTED = "unsupported"
    RESOURCE_EXCEEDED = "resource-exceeded"


class FailureCode(str, Enum):
    INVALID_RATIONAL = "invalid-rational-constant"
    LOG_DOMAIN = "log-domain-not-certified-positive"
    IRRATIONAL_RATE = "irrational-exponential-rate"
    FREE_PARAMETER = "free-parameter-outside-exponential-scale"
    NESTED_SCALE = "nested-unbounded-exponential-scale"
    SYMBOLIC_HEIGHT = "symbolic-height-outside-finite-le-fragment"
    OUTSIDE_GRAMMAR = "outside-frozen-expression-grammar"
    NODE_BUDGET = "source-node-budget-exceeded"
    Q_BUDGET = "exponential-chart-denominator-budget-exceeded"
    ORDER_BUDGET = "series-order-budget-exceeded"
    NONFINITE_LIMIT = "observer-does-not-have-a-finite-limit"
    NORMAL_FORM = "finite-laurent-taylor-normalization-failed"
    CERTIFICATE_BUDGET = "certificate-budget-exceeded"


@dataclass(frozen=True)
class EvaluatorBudget:
    max_nodes: int = 256
    max_q: int = 24
    max_series_order: int = 12
    max_certificate_bytes: int = 65536


@dataclass(frozen=True)
class DomainWitness:
    path: str
    statement: str


@dataclass(frozen=True)
class CostLedger:
    source_nodes: int
    rate_visits: int
    rewrite_visits: int
    series_order: int
    normal_form_terms: int
    comparison_steps: int
    certificate_bytes: int
    replay_steps: int
    residual_items: int


@dataclass(frozen=True)
class LESemanticCertificate:
    schema: str
    status: Status
    source_digest: str
    context_digest: str
    observer_digest: str
    q: int | None
    rates: tuple[str, ...]
    chart: str | None
    normal_form: str | None
    limit: str | None
    retained_order: int | None
    cancellation_jump: int | None
    residual: str | None
    domain_witnesses: tuple[DomainWitness, ...]
    discharged_c2_obligations: tuple[str, ...]
    claim_scope: str
    failures: tuple[dict[str, str], ...]
    cost: CostLedger
    certificate_digest: str

    def payload(self) -> dict[str, Any]:
        data = asdict(self)
        data["status"] = self.status.value
        data.pop("certificate_digest")
        return data

    def to_data(self) -> dict[str, Any]:
        return {**self.payload(), "certificate_digest": self.certificate_digest}


@dataclass(frozen=True)
class ReplayResult:
    valid: bool
    failures: tuple[str, ...]
    steps: int


class SemanticFailure(Exception):
    def __init__(self, code: FailureCode, message: str, *, resource: bool = False):
        super().__init__(message)
        self.code = code
        self.message = message
        self.resource = resource
