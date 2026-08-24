"""Executable Phase-0 contract for stochastic feedback-trap first passage."""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class StochasticTaskSignature:
    absorbing_sections: tuple[sp.Expr, ...]
    section_labels: tuple[str, ...]
    initial_law: str
    reset_semantics: str
    clock_scale: sp.Expr
    noise_strength: sp.Expr
    cost_functional: str

    def __post_init__(self) -> None:
        if len(self.absorbing_sections) != len(self.section_labels):
            raise ValueError("every absorbing section requires a retained label")
        if len(self.absorbing_sections) < 2:
            raise ValueError("first-passage task requires at least two sections")
        if not self.initial_law or not self.reset_semantics or not self.cost_functional:
            raise ValueError("stochastic task semantics must be explicit")


@dataclass(frozen=True)
class ItoCovarianceCertificate:
    transformed_drift: sp.Expr
    transformed_diffusion_variance: sp.Expr
    generator_residual: sp.Expr
    naive_residual: sp.Expr

    @property
    def certified(self) -> bool:
        return (
            sp.simplify(self.generator_residual) == 0
            and sp.simplify(self.naive_residual) != 0
        )


DISCOVERY_INPUTS = frozenset({
    "physical_sde",
    "task_signature",
    "bounded_am_grammar",
    "exact_monotonicity_contract",
})
HIDDEN_ORACLES = frozenset({
    "labelled_nonlinear_chart",
    "inverse_chart",
    "closed_form_first_passage_solution",
    "target_chart_bellman_value",
    "optimal_policy_labels",
})


def nonlinear_control_covariance_certificate() -> ItoCovarianceCertificate:
    """Post-hoc Ito control for ``h(u)=u+u^3``."""

    u, epsilon = sp.symbols("u epsilon", real=True)
    h = u + u**3
    drift = u**2 - 2
    h_prime = sp.diff(h, u)
    h_second = sp.diff(h, u, 2)
    transformed_drift = sp.expand(h_prime * drift + epsilon * h_second)
    transformed_variance = sp.expand(2 * epsilon * h_prime**2)

    # Test generator covariance on a generic quadratic target observable.  Its
    # symbolic coefficients keep the certificate independent of one test value.
    alpha, beta, gamma = sp.symbols("alpha beta gamma")
    target_observable = alpha + beta * h + gamma * h**2
    source_generator = sp.expand(
        drift * sp.diff(target_observable, u)
        + epsilon * sp.diff(target_observable, u, 2)
    )
    target_first = beta + 2 * gamma * h
    target_second = 2 * gamma
    target_generator_pullback = sp.expand(
        transformed_drift * target_first
        + transformed_variance * target_second / 2
    )
    generator_residual = sp.expand(
        source_generator - target_generator_pullback
    )

    naive_pullback = sp.expand(
        h_prime * drift * target_first
        + transformed_variance * target_second / 2
    )
    naive_residual = sp.expand(source_generator - naive_pullback)
    return ItoCovarianceCertificate(
        transformed_drift=transformed_drift,
        transformed_diffusion_variance=transformed_variance,
        generator_residual=generator_residual,
        naive_residual=naive_residual,
    )


__all__ = [
    "DISCOVERY_INPUTS",
    "HIDDEN_ORACLES",
    "ItoCovarianceCertificate",
    "StochasticTaskSignature",
    "nonlinear_control_covariance_certificate",
]
