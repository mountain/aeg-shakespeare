"""Versioned raw special-function representation registry.

Registry knowledge is deliberately isolated from the generic germ adapter and
receives no discovery credit.  Entries may contain a classical representation,
its domain, provenance, and proof obligations, but never expected scales or a
named local normal form.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256

import sympy as sp

from scale_compiler import Scale

from .adapter import (
    GermBudget,
    GermReport,
    LocalCoordinate,
    adapt_phase_to_germ,
)


@dataclass(frozen=True)
class BridgeFailure:
    code: str
    message: str


@dataclass(frozen=True)
class RepresentationObligation:
    name: str
    statement: str
    required_for: str
    discharged: bool


@dataclass(frozen=True)
class BridgeCertificate:
    registry_id: str
    registry_version: int
    source_digest: str
    provenance: str
    applicability: str
    phase: sp.Expr
    state_coordinate: LocalCoordinate
    parameter_coordinate: LocalCoordinate
    obligations: tuple[RepresentationObligation, ...]
    contains_scale_hint: bool = False
    contains_normal_form_hint: bool = False

    @property
    def local_representation_certified(self) -> bool:
        return (
            not self.contains_scale_hint
            and not self.contains_normal_form_hint
            and all(
                obligation.discharged
                for obligation in self.obligations
                if obligation.required_for == "local-chart"
            )
        )

    @property
    def uniform_integral_certified(self) -> bool:
        return all(obligation.discharged for obligation in self.obligations)


@dataclass(frozen=True)
class BridgeReport:
    status: str
    certificate: BridgeCertificate | None
    failures: tuple[BridgeFailure, ...]

    @property
    def local_representation_certified(self) -> bool:
        return (
            self.status == "ok"
            and self.certificate is not None
            and self.certificate.local_representation_certified
        )

    @property
    def uniform_integral_certified(self) -> bool:
        return (
            self.status == "ok"
            and self.certificate is not None
            and self.certificate.uniform_integral_certified
        )


@dataclass(frozen=True)
class RawGermReport:
    status: str
    bridge: BridgeReport
    germ: GermReport | None

    @property
    def local_chart_certified(self) -> bool:
        return (
            self.status == "local-chart-ok"
            and self.bridge.local_representation_certified
            and self.germ is not None
            and self.germ.certified
        )

    @property
    def uniform_integral_certified(self) -> bool:
        return self.local_chart_certified and self.bridge.uniform_integral_certified


def lower_registered_special_function(
    expression: sp.Expr,
    *,
    large_parameter: sp.Symbol,
    local_parameter: sp.Symbol,
    state_name: str = "theta",
    detuning_name: str = "delta",
) -> BridgeReport:
    """Lower one exact registered shape to its classical oscillatory phase.

    Registered shape: ``besselj(N, N*z)`` with ``N`` explicitly positive and
    integer and ``z`` explicitly real.  The entry is the integer-order cosine
    integral representation recorded at DLMF 10.9.2.  Only its phase is sent to
    germ discovery; evaluation and uniform-error obligations stay visible.
    """

    source = sp.sympify(expression)
    if source.func != sp.besselj or len(source.args) != 2:
        return _bridge_failed(
            "unsupported-special-function",
            "no representation registry entry matches the raw expression",
        )
    if large_parameter.is_integer is not True or large_parameter.is_positive is not True:
        return _bridge_failed(
            "registry-domain-mismatch",
            "the integer-order Bessel registry requires a positive integer large parameter",
        )
    if local_parameter.is_real is not True:
        return _bridge_failed(
            "registry-domain-mismatch",
            "the current turning-point registry requires a declared real local parameter",
        )
    order, argument = source.args
    if order != large_parameter or sp.simplify(argument - large_parameter * local_parameter) != 0:
        return _bridge_failed(
            "registry-shape-mismatch",
            "the registered shape is exactly besselj(N, N*z)",
        )

    theta = sp.Symbol(state_name, real=True)
    canonical_N = sp.Symbol(str(large_parameter))
    canonical_z = sp.Symbol(str(local_parameter), real=True)
    phase = canonical_N * (canonical_z * sp.sin(theta) - theta)
    obligations = (
        RepresentationObligation(
            "registry-shape",
            "source is exactly J_N(N z), with N positive integer and z real",
            "local-chart",
            True,
        ),
        RepresentationObligation(
            "full-reconstruction",
            "full function evaluation still requires the cosine integral, prefactor, and integration interval",
            "uniform-integral",
            False,
        ),
        RepresentationObligation(
            "uniform-error",
            "the local phase germ does not prove a uniform asymptotic error bound",
            "uniform-integral",
            False,
        ),
    )
    certificate = BridgeCertificate(
        registry_id="dlmf-10.9.2-integer-bessel-cosine-phase",
        registry_version=1,
        source_digest=sha256(sp.srepr(source).encode("utf-8")).hexdigest(),
        provenance="NIST DLMF 10.9.2, integer-order Bessel cosine integral",
        applicability="J_N(N*z), N positive integer, z real in a declared neighborhood of 1",
        phase=phase,
        state_coordinate=LocalCoordinate(theta, 0, state_name, "state"),
        parameter_coordinate=LocalCoordinate(canonical_z, 1, detuning_name, "parameter"),
        obligations=obligations,
    )
    return BridgeReport("ok", certificate, ())


def adapt_registered_special_function(
    expression: sp.Expr,
    *,
    large_parameter: sp.Symbol,
    local_parameter: sp.Symbol,
    large_parameter_scale: Scale,
    budget: GermBudget | None = None,
    require_degenerate: bool = True,
) -> RawGermReport:
    """Execute raw expression -> registered representation -> formal germ."""

    bridge = lower_registered_special_function(
        expression,
        large_parameter=large_parameter,
        local_parameter=local_parameter,
    )
    if not bridge.local_representation_certified or bridge.certificate is None:
        return RawGermReport("failed", bridge, None)
    certificate = bridge.certificate
    germ = adapt_phase_to_germ(
        certificate.phase,
        coordinates=(certificate.state_coordinate, certificate.parameter_coordinate),
        fixed_scales={str(large_parameter): large_parameter_scale},
        budget=budget,
        require_degenerate=require_degenerate,
    )
    return RawGermReport("local-chart-ok" if germ.certified else "failed", bridge, germ)


def raw_germ_summary(report: RawGermReport) -> dict[str, object]:
    """Expose local and uniform claims separately in a JSON-compatible ledger."""

    certificate = report.bridge.certificate
    return {
        "status": report.status,
        "local_chart_certified": report.local_chart_certified,
        "uniform_integral_certified": report.uniform_integral_certified,
        "bridge": None
        if certificate is None
        else {
            "registry_id": certificate.registry_id,
            "registry_version": certificate.registry_version,
            "source_digest": certificate.source_digest,
            "provenance": certificate.provenance,
            "applicability": certificate.applicability,
            "contains_scale_hint": certificate.contains_scale_hint,
            "contains_normal_form_hint": certificate.contains_normal_form_hint,
            "obligations": [asdict(obligation) for obligation in certificate.obligations],
        },
        "bridge_failures": [asdict(failure) for failure in report.bridge.failures],
        "germ_failures": [] if report.germ is None else [asdict(failure) for failure in report.germ.failures],
        "scales": {}
        if report.germ is None or report.germ.certificate is None
        else {name: str(scale) for name, scale in report.germ.certificate.balance.scales.items()},
    }


def _bridge_failed(code: str, message: str) -> BridgeReport:
    return BridgeReport("failed", None, (BridgeFailure(code, message),))
