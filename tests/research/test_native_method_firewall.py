"""Executable audit of the research-local native-method firewall (issue #156)."""

from __future__ import annotations

from dataclasses import replace
import importlib.util
import json
from pathlib import Path
import sys

import pytest


MODULE_PATH = (
    Path(__file__).parents[2]
    / "workstreams/native_method_firewall/native_method_firewall.py"
)
SPEC = importlib.util.spec_from_file_location("native_method_firewall", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def contract(*, with_lowering: bool = False) -> object:
    task = module.TaskContract(
        task_id="escape-value",
        observer="normalized escape value at one declared state",
        deliverable="value with a retained tail certificate",
        regime="degree >= 2, interaction > 0, inverse state in [0, 1]",
        accuracy="caller tolerance for the analytic tail",
        claim_mode=module.ClaimMode.CERTIFIED_APPROXIMATE,
        failure_semantics=("outside-domain", "budget-exhausted"),
    )
    lowering = ()
    if with_lowering:
        lowering = (
            module.LoweringWitness(
                witness_id="fixed-chart-series",
                mechanism=module.MethodMechanism.POWER_SERIES,
                source_presentation="native inverse-state recurrence",
                target_presentation="finite fixed-chart coefficient vector",
                task_scope=("escape-value",),
                allowed_lanes=(module.MethodLane.NATIVE_EVALUATION,),
                adequacy_grade=module.AdequacyGrade.TASK_APPROXIMATE,
                preserved_information=("escape-value", "first omitted residual"),
                forgotten_information=("full process history",),
                residual="first omitted degree and coefficient",
                decoder="degree-ray Horner evaluation in the frozen chart",
                certificate="replay the finite eigenrelation and residual",
                failure_semantics=("chart-failure", "order-budget-exhausted"),
            ),
        )
    return module.MethodContract(
        contract_id="amp-escape-method",
        problem="evaluate one AMP escape process without changing task semantics",
        primitive_processes=("inverse-state recurrence",),
        tasks=(task,),
        native_charts=("q = exp(-y)",),
        retained_fibres=("tail residual", "domain witness"),
        native_function_family="finite composition of power and log1p atoms",
        native_composition="chronological inverse-state recurrence",
        native_operators=("raise to degree", "divide by 1+t*q^d"),
        claim_boundary="one scalar task; no generic AMP solver or complexity theorem",
        allowed_lowerings=lowering,
        baselines=(
            module.BaselineSpec(
                baseline_id="direct-iterate",
                mechanism=module.MethodMechanism.BLACK_BOX_NUMERICS,
                task_scope=("escape-value",),
                purpose="independent same-information numerical comparison",
                independent_reference="direct normalized log iteration",
            ),
            module.BaselineSpec(
                baseline_id="series-red-team",
                mechanism=module.MethodMechanism.POWER_SERIES,
                task_scope=("escape-value",),
                purpose="detect fixed-chart truncation failure",
                independent_reference="explicit finite coefficient evaluation",
            ),
        ),
    )


def event_kwargs() -> dict[str, object]:
    return {
        "task_id": "escape-value",
        "action": "evaluate the declared recurrence",
        "input_semantics": "inverse state and tolerance",
        "output_semantics": "escape value and tail residual",
    }


def test_incomplete_contract_fails_before_a_trace_exists() -> None:
    incomplete = replace(contract(), primitive_processes=())
    with pytest.raises(module.MethodContractError, match="primitive_processes"):
        module.MethodTrace(incomplete)


@pytest.mark.parametrize(
    "mechanism",
    sorted(module.CLASSICAL_MECHANISMS, key=lambda item: item.value),
)
def test_every_classical_mechanism_fails_in_native_discovery(mechanism: object) -> None:
    trace = module.MethodTrace(contract())
    with pytest.raises(module.PrematureLoweringError, match="lowering witness"):
        trace.record(
            **event_kwargs(),
            lane=module.MethodLane.NATIVE_DISCOVERY,
            mechanism=mechanism,
        )


def test_declared_classical_baseline_remains_legal() -> None:
    trace = module.MethodTrace(contract())
    event = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.BASELINE,
        mechanism=module.MethodMechanism.POWER_SERIES,
        baseline_id="series-red-team",
        cost=module.CostLedger(evaluation_steps=20, stored_history_units=10),
    )
    assert event.lane is module.MethodLane.BASELINE
    assert trace.audit_report()["summary"]["lane_counts"]["baseline"] == 1


@pytest.mark.parametrize(
    "mechanism",
    sorted(module.CLASSICAL_MECHANISMS, key=lambda item: item.value),
)
def test_each_classical_mechanism_is_legal_when_declared_as_baseline(
    mechanism: object,
) -> None:
    declared = tuple(
        module.BaselineSpec(
            baseline_id=f"{item.value}-baseline",
            mechanism=item,
            task_scope=("escape-value",),
            purpose="independent red team",
            independent_reference=f"declared {item.value} implementation",
        )
        for item in sorted(module.CLASSICAL_MECHANISMS, key=lambda item: item.value)
    )
    trace = module.MethodTrace(replace(contract(), baselines=declared))
    event = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.BASELINE,
        mechanism=mechanism,
        baseline_id=f"{mechanism.value}-baseline",
    )
    assert event.mechanism is mechanism


def test_undeclared_baseline_fails_closed() -> None:
    trace = module.MethodTrace(contract())
    with pytest.raises(module.MethodContractError, match="undeclared baseline"):
        trace.record(
            **event_kwargs(),
            lane=module.MethodLane.BASELINE,
            mechanism=module.MethodMechanism.POWER_SERIES,
            baseline_id="friendly-name-only",
        )


def test_task_scoped_lowering_enters_only_its_declared_native_lane() -> None:
    trace = module.MethodTrace(contract(with_lowering=True))
    accepted = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.NATIVE_EVALUATION,
        mechanism=module.MethodMechanism.POWER_SERIES,
        lowering_id="fixed-chart-series",
    )
    assert accepted.lowering_id == "fixed-chart-series"

    with pytest.raises(module.PrematureLoweringError, match="outside lane"):
        trace.record(
            **event_kwargs(),
            lane=module.MethodLane.NATIVE_DISCOVERY,
            mechanism=module.MethodMechanism.POWER_SERIES,
            lowering_id="fixed-chart-series",
        )


def test_wrong_mechanism_cannot_borrow_a_lowering_witness() -> None:
    trace = module.MethodTrace(contract(with_lowering=True))
    with pytest.raises(module.PrematureLoweringError, match="does not certify"):
        trace.record(
            **event_kwargs(),
            lane=module.MethodLane.NATIVE_EVALUATION,
            mechanism=module.MethodMechanism.MATRIX_LINEARIZATION,
            lowering_id="fixed-chart-series",
        )


def test_alias_string_cannot_evade_the_typed_mechanism_vocabulary() -> None:
    trace = module.MethodTrace(contract())
    with pytest.raises(module.MethodContractError, match="unknown mechanism"):
        trace.record(
            **event_kwargs(),
            lane=module.MethodLane.NATIVE_DISCOVERY,
            mechanism="spectral-diagonalization",
        )


def test_baseline_event_cannot_be_relabelled_as_native_evidence() -> None:
    trace = module.MethodTrace(contract())
    native = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.NATIVE_EVALUATION,
        mechanism=module.MethodMechanism.NATIVE_PROCESS,
    )
    baseline = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.BASELINE,
        mechanism=module.MethodMechanism.BLACK_BOX_NUMERICS,
        baseline_id="direct-iterate",
    )
    with pytest.raises(module.EvidenceLaneError, match="cannot be relabelled"):
        trace.claim_native_result(
            task_id="escape-value",
            statement="native recurrence evaluates the task",
            evidence_event_ids=(native.event_id, baseline.event_id),
        )


def test_certificate_may_support_but_not_replace_native_evidence() -> None:
    trace = module.MethodTrace(contract())
    certificate = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.CERTIFICATE,
        mechanism=module.MethodMechanism.GENERIC_CAS,
    )
    with pytest.raises(module.EvidenceLaneError, match="certificate-only"):
        trace.claim_native_result(
            task_id="escape-value",
            statement="a CAS output is not a native derivation",
            evidence_event_ids=(certificate.event_id,),
        )

    native = trace.record(
        **event_kwargs(),
        lane=module.MethodLane.NATIVE_EVALUATION,
        mechanism=module.MethodMechanism.NATIVE_PROCESS,
    )
    claim = trace.claim_native_result(
        task_id="escape-value",
        statement="native recurrence with an independent symbolic certificate",
        evidence_event_ids=(native.event_id, certificate.event_id),
    )
    assert claim.evidence_event_ids == (native.event_id, certificate.event_id)


def test_json_audit_preserves_lane_and_multi_axis_cost() -> None:
    trace = module.MethodTrace(contract())
    trace.record(
        **event_kwargs(),
        lane=module.MethodLane.NATIVE_DISCOVERY,
        mechanism=module.MethodMechanism.TASK_FIBRE,
        cost=module.CostLedger(
            discovery_steps=3,
            live_state_units=2,
            residual_units=1,
        ),
    )
    trace.record(
        **event_kwargs(),
        lane=module.MethodLane.NATIVE_EVALUATION,
        mechanism=module.MethodMechanism.NATIVE_PROCESS,
        cost=module.CostLedger(evaluation_steps=5, decoder_steps=1),
    )
    report = json.loads(trace.to_json())
    assert report["summary"] == {
        "cost_scalarization": "not-authorized",
        "lane_counts": {
            "baseline": 0,
            "certificate": 0,
            "native-discovery": 1,
            "native-evaluation": 1,
        },
        "mechanism_counts": {"native-process": 1, "task-fibre": 1},
        "total_cost": {
            "compilation_steps": 0,
            "decoder_steps": 1,
            "discovery_steps": 3,
            "evaluation_steps": 5,
            "live_state_units": 2,
            "residual_units": 1,
            "stored_history_units": 0,
        },
    }
