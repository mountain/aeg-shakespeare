"""Exact stopped-process quotient over the depth-three presentation slice."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys

import sympy as sp


_PHASE1_PATH = Path(__file__).with_name("phase1_presentation_census.py")
_SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase1_for_quotient", _PHASE1_PATH)
assert _SPEC and _SPEC.loader
_phase1 = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = _phase1
_SPEC.loader.exec_module(_phase1)


@dataclass(frozen=True)
class TransportCertificate:
    presentation: sp.Expr
    degree: int
    transformed_drift: sp.Expr
    transformed_variance: sp.Expr
    generator_residual: sp.Expr
    naive_residual: sp.Expr
    sections: tuple[sp.Expr, sp.Expr]
    section_labels: tuple[str, str]
    initial_point: sp.Expr
    clock: str

    @property
    def full_task_certified(self) -> bool:
        return (
            self.generator_residual == 0
            and self.sections[0] < self.sections[1]
            and self.section_labels == ("left", "right")
            and self.clock == "theta=Vt/L"
        )


@dataclass(frozen=True)
class TaskQuotientCensus:
    certificates: tuple[TransportCertificate, ...]

    @property
    def equivalence_class_count(self) -> int:
        # Every certificate retains the same labelled source task and differs
        # only by a certified invertible forward presentation.
        return 1 if self.certificates and all(c.full_task_certified for c in self.certificates) else 0


def transport_certificate(h: sp.Expr) -> TransportCertificate:
    u, epsilon = sp.symbols("u epsilon", real=True)
    alpha, beta, gamma = sp.symbols("alpha beta gamma")
    h = sp.expand(h)
    drift = u**2 - 2
    first = sp.diff(h, u)
    second = sp.diff(h, u, 2)
    transformed_drift = sp.expand(first * drift + epsilon * second)
    transformed_variance = sp.expand(2 * epsilon * first**2)

    observable = alpha + beta * h + gamma * h**2
    source = sp.expand(drift * sp.diff(observable, u) + epsilon * sp.diff(observable, u, 2))
    target_first = beta + 2 * gamma * h
    target_second = 2 * gamma
    target = sp.expand(transformed_drift * target_first + transformed_variance * target_second / 2)
    naive = sp.expand(first * drift * target_first + transformed_variance * target_second / 2)

    return TransportCertificate(
        presentation=h,
        degree=int(sp.Poly(h, u).degree()),
        transformed_drift=transformed_drift,
        transformed_variance=transformed_variance,
        generator_residual=sp.expand(source - target),
        naive_residual=sp.expand(source - naive),
        sections=(sp.expand(h.subs(u, -1)), sp.expand(h.subs(u, 1))),
        section_labels=("left", "right"),
        initial_point=sp.expand(h.subs(u, 0)),
        clock="theta=Vt/L",
    )


def depth_three_task_quotient() -> TaskQuotientCensus:
    census = _phase1.depth_three_presentation_census()
    return TaskQuotientCensus(tuple(
        transport_certificate(certificate.presentation)
        for certificate in census.monotone_certificates
    ))


__all__ = [
    "TaskQuotientCensus",
    "TransportCertificate",
    "depth_three_task_quotient",
    "transport_certificate",
]
