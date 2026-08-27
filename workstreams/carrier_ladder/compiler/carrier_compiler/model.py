"""Carrier capability declarations and typed result vocabulary."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Carrier(str, Enum):
    C0 = "C0-rational-newton"
    C1 = "C1f-finite-generalized-polynomial"
    C2 = "C2-finite-height-le"
    C3 = "C3-hyperserial-conditional"
    C4 = "C4-surreal-envelope-conditional"


class DecisionStatus(str, Enum):
    SUFFICIENT = "sufficient"
    UNSUPPORTED = "unsupported"
    INCONCLUSIVE = "inconclusive"
    RESOURCE_EXCEEDED = "resource-exceeded"
    OUTSIDE_GRAMMAR = "outside-implemented-grammar"


class FailureCode(str, Enum):
    SYMBOLIC_HEIGHT = "symbolic-height-not-finite-unrolling"
    ABEL_ASSUMPTIONS = "abel-existence-normalization-unresolved"
    C3_UNSUPPORTED = "hyperserial-backend-unsupported"
    C4_UNSUPPORTED = "surreal-runtime-unsupported"
    NODE_BUDGET = "input-node-budget-exceeded"
    HEIGHT_BUDGET = "construction-height-budget-exceeded"
    CERTIFICATE_BUDGET = "certificate-budget-exceeded"


@dataclass(frozen=True)
class Capability:
    carrier: Carrier
    supports: frozenset[str]
    executable: bool
    note: str


CAPABILITY_MATRIX: tuple[Capability, ...] = (
    Capability(Carrier.C0, frozenset({"rational", "finite-polynomial-germ", "integer-power"}), True, "exact rational Newton weights and finite polynomial germs"),
    Capability(Carrier.C1, frozenset({"rational", "finite-polynomial-germ", "integer-power", "negative-integer-power", "ordered-rational-monomial", "finite-generalized-polynomial-support"}), True, "explicit finite generalized-polynomial support; no series field or infinite-support operations"),
    Capability(Carrier.C2, frozenset({"rational", "finite-polynomial-germ", "integer-power", "negative-integer-power", "ordered-rational-monomial", "finite-generalized-polynomial-support", "finite-exp-log", "finite-construction-height"}), True, "syntax carrier for a finite-height exp/log term; no transseries normalization, domain, or comparison theorem"),
    Capability(Carrier.C3, frozenset(), False, "conditional label only; no hyperserial constructor, comparison, or replay backend"),
    Capability(Carrier.C4, frozenset(), False, "semantic envelope only; no surreal arithmetic or effective-shadow backend"),
)


def capability(carrier: Carrier) -> Capability:
    return next(item for item in CAPABILITY_MATRIX if item.carrier is carrier)
