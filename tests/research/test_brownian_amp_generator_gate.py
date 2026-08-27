"""Brownian A/M/P generator and competing-chart gate for correction #160."""

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
    / "sonnet/brownian-scale-fibre/phase1_amp_contract.py"
)
SPEC = importlib.util.spec_from_file_location("brownian_phase1_amp_contract", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)
amp = module.amp
firewall = module.firewall


def test_amp_contract_requires_three_generators_and_exposes_closure_escape() -> None:
    grammar = module.AMP_METHOD_CONTRACT.native_grammar
    assert grammar.family is firewall.NativeGrammarFamily.AMP
    assert grammar.generator_ids == {"A", "M", "P"}
    relations = {relation.relation_id: relation for relation in grammar.relations}
    assert relations["A-M"].expression == "[A,M]=A"
    assert relations["M-P"].expression == "[M,P]=M"
    assert relations["A-P"].expression == "[A,P]=(1+log(x))*d/dx"
    assert (
        relations["A-P"].closure_status
        is firewall.ClosureStatus.ESCAPES_DECLARED_SPAN
    )
    assert "infinite family" in grammar.closure_obligations[0]


def test_positive_position_chart_has_a_typed_zero_crossing_obstruction() -> None:
    audit = amp.audit_positive_position_history(
        Fraction(2),
        (Fraction(1), Fraction(-1)),
    )
    assert audit.states == (Fraction(2), Fraction(3), Fraction(2))
    assert audit.generator_ids == ("A", "M", "P")

    with pytest.raises(
        amp.PositionChartDomainError,
        match="positive-position-chart-obstruction",
    ) as error:
        amp.audit_positive_position_history(
            Fraction(1),
            (Fraction(-1), Fraction(1)),
        )
    assert error.value.step_index == 1
    assert error.value.value == 0
    assert error.value.offending_increment == -1


@pytest.mark.parametrize("initial", (Fraction(0), Fraction(-1)))
def test_positive_position_chart_rejects_nonpositive_initial_states(
    initial: Fraction,
) -> None:
    with pytest.raises(amp.PositionChartDomainError) as error:
        amp.audit_positive_position_history(initial, ())
    assert error.value.step_index == 0


def test_exponential_observer_realizes_exact_a_and_m_actions() -> None:
    observer = amp.ExponentialObserver.from_finite_law(
        (-1, 1),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    assert observer.shift_state(Fraction(2)).terms == (
        (Fraction(1), Fraction(1, 2)),
        (Fraction(3), Fraction(1, 2)),
    )
    assert observer.scale_state(Fraction(3)).terms == (
        (Fraction(-3), Fraction(1, 2)),
        (Fraction(3), Fraction(1, 2)),
    )
    assert observer.shift_state(Fraction(2)).shift_state(Fraction(-2)) == observer
    assert observer.scale_state(Fraction(3)).scale_state(Fraction(1, 3)) == observer


def test_integer_p_slice_reproduces_the_endpoint_fibre_law_exactly() -> None:
    observer = amp.ExponentialObserver.from_finite_law(
        (-1, 1),
        (Fraction(1, 2), Fraction(1, 2)),
    )
    replica = observer.replica_power(5)
    assert replica.observer.terms == (
        (Fraction(-5), Fraction(1, 32)),
        (Fraction(-3), Fraction(5, 32)),
        (Fraction(-1), Fraction(5, 16)),
        (Fraction(1), Fraction(5, 16)),
        (Fraction(3), Fraction(5, 32)),
        (Fraction(5), Fraction(1, 32)),
    )
    assert replica.observer.mass == 1
    assert "noninteger P" in replica.residual
    with pytest.raises(amp.BrownianAMPDomainError, match="non-negative integer"):
        observer.replica_power(Fraction(1, 2))


def test_endpoint_observer_preserves_an_explicit_path_residual() -> None:
    residual = amp.expose_path_information_residual(
        (Fraction(1), Fraction(-1)),
        (Fraction(-1), Fraction(1)),
    )
    assert residual.shared_observer == amp.ExponentialObserver.point_mass(Fraction(0))
    assert "running maximum" in residual.lost_observer


def test_amp_gate_is_exact_and_machine_auditable() -> None:
    result = module.run_amp_gate()
    report = json.loads(result.trace.to_json())
    assert result.position_obstruction.step_index == 1
    assert result.ensemble.shift_inverse_certified
    assert result.ensemble.scale_inverse_certified
    assert result.ensemble.endpoint_fibre_certified
    assert report["contract"]["native_grammar"]["family"] == "amp"
    assert report["contract"]["native_grammar"]["required_generators"] == [
        "A",
        "M",
        "P",
    ]
    assert len(report["native_claims"]) == 3
    ensemble_event = next(
        event
        for event in report["events"]
        if event["task_id"] == "ensemble-amp-adapter"
        and event["lane"] == "native-evaluation"
    )
    assert ensemble_event["generator_ids"] == ["A", "M", "P"]
    assert report["summary"]["cost_scalarization"] == "not-authorized"


def test_amp_claim_cannot_drop_p_even_if_the_contract_declares_it() -> None:
    trace = firewall.MethodTrace(module.AMP_METHOD_CONTRACT)
    event = trace.record(
        task_id="ensemble-amp-adapter",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.NATIVE_PROCESS,
        action="incomplete two-generator adapter",
        input_semantics="positive ensemble observer",
        output_semantics="A/M result with no P witness",
        generator_ids=("A", "M"),
    )
    with pytest.raises(firewall.EvidenceLaneError, match="missing.*P"):
        trace.claim_native_result(
            task_id="ensemble-amp-adapter",
            statement="this must not be accepted as an AMP result",
            evidence_event_ids=(event.event_id,),
        )


def test_amp_engine_imports_no_matrix_series_or_transform_package() -> None:
    source_path = MODULE_PATH.with_name("brownian_amp.py")
    tree = ast.parse(source_path.read_text(encoding="utf-8"))
    imported_roots = {
        alias.name.split(".")[0]
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    assert not imported_roots & {"numpy", "scipy", "sympy"}
    source = source_path.read_text(encoding="utf-8")
    assert ".series(" not in source
    assert ".fourier_transform(" not in source
    assert ".as_matrix(" not in source
