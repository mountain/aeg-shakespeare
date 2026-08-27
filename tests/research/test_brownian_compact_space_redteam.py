"""Exact cycle/circle and frozen sphere red teams for issue #162."""

from __future__ import annotations

import ast
from fractions import Fraction
import importlib.util
import json
from pathlib import Path
import sys

import pytest


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/brownian-scale-fibre/phase_compact_contract.py"
)
SPEC = importlib.util.spec_from_file_location("brownian_compact_contract", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)
compact = module.compact
line = module.line
firewall = module.firewall


@pytest.mark.parametrize(
    "modulus,horizon",
    ((2, 0), (2, 5), (3, 7), (4, 6), (5, 9), (11, 4)),
)
def test_cycle_counts_are_the_exact_deck_pushforward_of_line_counts(
    modulus: int,
    horizon: int,
) -> None:
    line_distribution = line.endpoint_fibres(1, horizon)
    folded = compact.fold_integer_endpoint_counts(
        ((point[0], count) for point, count in line_distribution.counts),
        modulus=modulus,
        horizon=horizon,
    )
    direct = compact.direct_cycle_endpoint_counts(modulus, horizon)
    assert folded.cycle.counts == direct.counts
    assert folded.cycle.total_histories == 2**horizon
    assert all(
        lift % modulus == residue
        for residue, fibre in enumerate(folded.deck_fibres)
        for lift, _ in fibre
    )


def test_deck_fibres_retain_lifts_that_the_cycle_endpoint_forgets() -> None:
    line_distribution = line.endpoint_fibres(1, 8)
    folded = compact.fold_integer_endpoint_counts(
        ((point[0], count) for point, count in line_distribution.counts),
        modulus=4,
        horizon=8,
    )
    zero_fibre = folded.deck_fibres[0]
    assert tuple(lift for lift, _ in zero_fibre) == (-8, -4, 0, 4, 8)
    assert sum(count for _, count in zero_fibre) == folded.cycle.counts[0]


def test_even_cycle_period_two_is_a_typed_terminal_limit_obstruction() -> None:
    assert compact.nearest_neighbour_period(
        6,
        stay_probability=Fraction(0),
    ) == 2
    with pytest.raises(
        compact.PeriodicClockObstruction,
        match="periodic-clock-obstruction",
    ) as error:
        compact.require_terminal_mixing_clock(
            6,
            stay_probability=Fraction(0),
        )
    assert error.value.modulus == 6
    assert error.value.period == 2


def test_odd_or_lazy_cycle_has_no_period_two_obstruction() -> None:
    assert compact.nearest_neighbour_period(
        5,
        stay_probability=Fraction(0),
    ) == 1
    assert compact.nearest_neighbour_period(
        6,
        stay_probability=Fraction(1, 2),
    ) == 1
    compact.require_terminal_mixing_clock(5, stay_probability=Fraction(0))
    compact.require_terminal_mixing_clock(6, stay_probability=Fraction(1, 2))


def test_stationary_uniform_does_not_imply_mixing_for_a_frozen_clock() -> None:
    uniform = compact.CycleLaw.uniform(5)
    assert compact.cycle_step(uniform, stay_probability=Fraction(1)) == uniform
    with pytest.raises(
        compact.ReducibleClockObstruction,
        match="reducible-clock-obstruction",
    ):
        compact.require_terminal_mixing_clock(
            5,
            stay_probability=Fraction(1),
        )


def test_even_nonlazy_cycle_stays_far_from_uniform_at_every_bounded_time() -> None:
    modulus = 6
    uniform = compact.CycleLaw.uniform(modulus)
    for horizon in range(10):
        counts = compact.direct_cycle_endpoint_counts(modulus, horizon)
        law = compact.CycleLaw(
            tuple(Fraction(count, counts.total_histories) for count in counts.counts)
        )
        assert compact.total_variation(law, uniform) >= Fraction(1, 2)


@pytest.mark.parametrize("modulus", (2, 3, 5, 8))
def test_uniform_cycle_law_is_an_exact_fixed_point(modulus: int) -> None:
    uniform = compact.CycleLaw.uniform(modulus)
    for stay_probability in (Fraction(0), Fraction(1, 2), Fraction(1)):
        assert (
            compact.cycle_step(uniform, stay_probability=stay_probability)
            == uniform
        )


def test_bounded_lazy_audit_records_a_trend_without_claiming_a_limit() -> None:
    audit = compact.bounded_lazy_mixing_audit(
        5,
        horizon=12,
        stay_probability=Fraction(1, 2),
    )
    assert audit.nonincreasing
    assert audit.distances_to_uniform[-1] < audit.distances_to_uniform[0]
    assert "no asymptotic mixing theorem" in audit.claim_boundary


def test_cycle_endpoint_quotient_exposes_winding_loss() -> None:
    residual = compact.expose_winding_residual(
        4,
        (1, 1, 1, 1),
        (1, -1, 1, -1),
    )
    assert residual.left_lift == 4
    assert residual.right_lift == 0
    assert residual.shared_residue == 0
    assert "winding" in residual.lost_observer


def test_circle_and_sphere_use_time_stationarity_not_line_scale_stability() -> None:
    assert (
        compact.CIRCLE_GATE.stability_mechanism
        is compact.StabilityMechanism.TIME_STATIONARY
    )
    assert (
        compact.SPHERE_GATE.stability_mechanism
        is compact.StabilityMechanism.TIME_STATIONARY
    )
    assert (
        compact.CIRCLE_GATE.stability_mechanism
        is not compact.StabilityMechanism.SCALE_RENORMALIZED
    )
    assert compact.CIRCLE_GATE.quotient_or_homogeneous_space == "R / (2*pi*Z)"
    assert compact.SPHERE_GATE.quotient_or_homogeneous_space == "SO(3) / SO(2)"
    assert "curvature" in compact.SPHERE_GATE.retained_residuals
    assert "no executable continuum" in compact.SPHERE_GATE.claim_boundary


def test_compact_gate_is_machine_auditable_and_lane_separated() -> None:
    result = module.run_compact_gate()
    report = json.loads(result.trace.to_json())
    assert result.deck_pushforward_certified
    assert result.periodic_obstruction.period == 2
    assert result.uniform_stationary_certified
    assert result.bounded_mixing.nonincreasing
    assert report["summary"]["lane_counts"] == {
        "baseline": 0,
        "certificate": 1,
        "native-discovery": 1,
        "native-evaluation": 2,
    }
    assert len(report["native_claims"]) == 2
    assert report["summary"]["cost_scalarization"] == "not-authorized"


def test_compact_engine_imports_no_classical_discovery_backend() -> None:
    source_path = MODULE_PATH.with_name("compact_space_redteam.py")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_roots = {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert not imported_roots & {"numpy", "scipy", "sympy"}
    assert ".series(" not in source
    assert ".fourier_transform(" not in source
    assert ".as_matrix(" not in source


def test_classical_cycle_or_sphere_oracle_cannot_enter_native_discovery() -> None:
    trace = firewall.MethodTrace(module.COMPACT_REDTEAM_CONTRACT)
    with pytest.raises(firewall.PrematureLoweringError):
        trace.record(
            task_id="compact-stability-kind",
            lane=firewall.MethodLane.NATIVE_DISCOVERY,
            mechanism=firewall.MethodMechanism.FOURIER_SPECTRAL,
            action="supply a stationary law from a spectral oracle",
            input_semantics="undeveloped compact process",
            output_semantics="answer-shaped uniform law",
        )
