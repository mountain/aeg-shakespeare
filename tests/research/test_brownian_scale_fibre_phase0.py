"""S0/S1 Brownian scale and endpoint-fibre certificates for issue #158."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys

import pytest


MODULE_PATH = (
    Path(__file__).parents[2] / "sonnet/brownian-scale-fibre/phase0_contract.py"
)
SPEC = importlib.util.spec_from_file_location("brownian_phase0_contract", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)
native = module.native
firewall = module.firewall


def test_method_contract_has_no_s0_s1_lowering_escape_hatch() -> None:
    contract = module.METHOD_CONTRACT
    assert contract.contract_id == "brownian-scale-fibre-s0-s1"
    assert contract.allowed_lowerings == ()
    assert {task.task_id for task in contract.tasks} == {
        "blind-scale",
        "endpoint-fibre",
    }
    assert contract.forbidden_premature_lowerings == firewall.CLASSICAL_MECHANISMS


def test_blind_scale_is_derived_from_the_raw_law() -> None:
    law = native.FiniteIncrementLaw.symmetric_unit()
    certificate = native.discover_diffusive_scale(law)

    assert certificate.increment_mean == 0
    assert certificate.centered_variance == 1
    assert certificate.active_response_order == 2
    assert certificate.population_power == 1
    assert certificate.scale_exponent == Fraction(1, 2)
    assert certificate.balance_residual == 0
    assert certificate.balanced_response_coefficient == Fraction(1, 2)
    assert "no limit law" in certificate.claim_boundary


def test_biased_law_requires_explicit_centering() -> None:
    biased = native.FiniteIncrementLaw(
        (-1, 1),
        (Fraction(1, 4), Fraction(3, 4)),
    )
    with pytest.raises(native.CenteringRequired, match="centering-required") as error:
        native.discover_diffusive_scale(biased)
    assert error.value.mean == Fraction(1, 2)


def test_finite_law_requires_exact_weights_and_nondegenerate_response() -> None:
    with pytest.raises(native.NativeBrownianDomainError, match="exact fractions"):
        native.FiniteIncrementLaw((-1, 1), (0.5, 0.5))

    point_mass = native.FiniteIncrementLaw((0,), (Fraction(1),))
    with pytest.raises(
        native.NativeBrownianDomainError, match="nondegenerate centered second"
    ):
        native.discover_diffusive_scale(point_mass)


def test_exact_one_dimensional_endpoint_fibres() -> None:
    distribution = native.endpoint_fibres(1, 4)
    assert distribution.counts == (
        ((-4,), 1),
        ((-2,), 4),
        ((0,), 6),
        ((2,), 4),
        ((4,), 1),
    )
    assert distribution.probability((0,)) == Fraction(3, 8)
    assert distribution.total_histories == 16


def test_two_dimensional_return_mass_is_an_exact_fibre() -> None:
    distribution = native.endpoint_fibres(2, 2)
    assert distribution.count((0, 0)) == 4
    assert distribution.probability((0, 0)) == Fraction(1, 4)
    assert distribution.total_histories == 16


def test_endpoint_fibre_budget_exhaustion_is_typed() -> None:
    with pytest.raises(native.EndpointFibreBudgetError, match="budget exhausted"):
        native.endpoint_fibres(2, 4, max_transition_updates=3)


@pytest.mark.parametrize("dimension,horizon", ((1, 0), (1, 5), (2, 3)))
def test_endpoint_pushforward_matches_literal_history_enumeration(
    dimension: int, horizon: int
) -> None:
    pushed = native.endpoint_fibres(dimension, horizon)
    exhaustive = native.exhaustive_endpoint_counts(dimension, horizon)
    assert pushed.counts == exhaustive


@pytest.mark.parametrize(
    "dimension,left_horizon,right_horizon",
    ((1, 2, 5), (2, 2, 2), (3, 1, 2)),
)
def test_history_concatenation_descends_exactly_to_endpoint_fibres(
    dimension: int, left_horizon: int, right_horizon: int
) -> None:
    assert native.certify_history_concatenation(
        dimension, left_horizon, right_horizon
    )


def test_endpoint_fibre_is_not_a_path_task_quotient() -> None:
    positive = (1,)
    negative = (-1,)
    first = (positive, negative)
    second = (negative, positive)

    def running_maximum(history):
        value = 0
        maximum = 0
        for (increment,) in history:
            value += increment
            maximum = max(maximum, value)
        return maximum

    assert native.literal_endpoint(first, 1) == native.literal_endpoint(second, 1)
    assert running_maximum(first) == 1
    assert running_maximum(second) == 0


def test_native_source_has_no_classical_lowering_calls() -> None:
    source = (
        MODULE_PATH.with_name("brownian_native.py")
        .read_text(encoding="utf-8")
        .casefold()
    )
    forbidden = (
        ".series(",
        "fourier",
        "matrix",
        "koopman",
        "carleman",
        "gaussian",
        "heat kernel",
    )
    assert not {token for token in forbidden if token in source}


def test_phase0_trace_is_machine_readable_and_lane_separated() -> None:
    result = module.run_phase0()
    report = json.loads(result.trace.to_json())

    assert result.scale.scale_exponent == Fraction(1, 2)
    assert result.concatenation_certified
    assert report["summary"]["lane_counts"] == {
        "baseline": 0,
        "certificate": 1,
        "native-discovery": 1,
        "native-evaluation": 1,
    }
    assert len(report["native_claims"]) == 2
    assert report["summary"]["cost_scalarization"] == "not-authorized"


def test_phase0_firewall_rejects_a_classical_discovery_oracle() -> None:
    trace = firewall.MethodTrace(module.METHOD_CONTRACT)
    with pytest.raises(firewall.PrematureLoweringError):
        trace.record(
            task_id="blind-scale",
            lane=firewall.MethodLane.NATIVE_DISCOVERY,
            mechanism=firewall.MethodMechanism.FOURIER_SPECTRAL,
            action="supply a target scale from a classical transform",
            input_semantics="raw increment law",
            output_semantics="answer-shaped exponent",
        )
