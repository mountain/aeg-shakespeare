"""Phase-0 firewall and Ito covariance for stochastic feedback-trap work."""

import importlib.util
from pathlib import Path
import sys

import pytest
import sympy as sp


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/stochastic-feedback-trap-first-passage/phase0_contract.py"
)
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase0", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_noise_strength_and_clock_scale_are_dimensionally_forced():
    length, speed, diffusion = sp.symbols("L V D", positive=True)
    clock_scale = length / speed
    epsilon = diffusion / (length * speed)

    # Exponent pairs are (length, time).  D/(L V) is dimensionless and L/V
    # has time dimension.
    dimensions = {
        length: (1, 0),
        speed: (1, -1),
        diffusion: (2, -1),
    }

    def dimension_of_monomial(expression):
        powers = expression.as_powers_dict()
        return tuple(
            sum(powers.get(symbol, 0) * dimensions[symbol][axis] for symbol in dimensions)
            for axis in range(2)
        )

    assert dimension_of_monomial(clock_scale) == (0, 1)
    assert dimension_of_monomial(epsilon) == (0, 0)


def test_task_signature_requires_stopped_process_semantics_and_labels():
    length, speed, epsilon = sp.symbols("L V epsilon", positive=True)
    task = module.StochasticTaskSignature(
        absorbing_sections=(-1, 1),
        section_labels=("left", "right"),
        initial_law="delta(u=0)",
        reset_semantics="reset to initial law after every query",
        clock_scale=length / speed,
        noise_strength=epsilon,
        cost_functional="expected physical first-passage time",
    )
    assert task.section_labels == ("left", "right")

    with pytest.raises(ValueError, match="retained label"):
        module.StochasticTaskSignature(
            absorbing_sections=(-1, 1),
            section_labels=("unlabelled",),
            initial_law="delta(u=0)",
            reset_semantics="reset",
            clock_scale=length / speed,
            noise_strength=epsilon,
            cost_functional="expectation",
        )


def test_oracle_firewall_is_disjoint():
    assert module.DISCOVERY_INPUTS.isdisjoint(module.HIDDEN_ORACLES)
    assert "labelled_nonlinear_chart" not in module.DISCOVERY_INPUTS
    assert "target_chart_bellman_value" not in module.DISCOVERY_INPUTS


def test_ito_generator_covariance_passes_and_naive_chain_rule_fails():
    u, epsilon = sp.symbols("u epsilon", real=True)
    alpha, beta, gamma = sp.symbols("alpha beta gamma")
    certificate = module.nonlinear_control_covariance_certificate()

    assert certificate.certified
    assert certificate.generator_residual == 0
    assert sp.simplify(
        certificate.naive_residual
        - 6 * epsilon * u * (beta + 2 * gamma * (u**3 + u))
    ) == 0
    assert sp.simplify(certificate.naive_residual.subs(epsilon, 0)) == 0
    assert sp.simplify(
        certificate.transformed_diffusion_variance
        - 2 * epsilon * (3 * u**2 + 1) ** 2
    ) == 0
