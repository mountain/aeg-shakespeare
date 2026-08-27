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
        required_generators=("Q",),
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
        native_grammar=module.NativeGrammarProfile(
            profile_id="inverse-recurrence-grammar",
            family=module.NativeGrammarFamily.DECLARED,
            required_generators=("Q",),
            generators=(
                module.GeneratorWitness(
                    generator_id="Q",
                    finite_action="one inverse-state recurrence update",
                    infinitesimal_action="not-applicable: finite declared recurrence",
                    carrier="inverse state q",
                    domain="q in [0, 1]",
                    task_role="evaluate the escape observer",
                    residual="tail after the finite recurrence budget",
                    certificate="replay the exact recurrence",
                ),
            ),
            legal_compositions=("chronological recurrence composition",),
            relations=(
                module.GeneratorRelationWitness(
                    relation_id="Q-Q",
                    expression="Q after Q is chronological recurrence composition",
                    closure_status=module.ClosureStatus.TASK_SCOPED,
                    residual="the full history is not reconstructed",
                    certificate="direct two-step replay",
                ),
            ),
            closure_obligations=("retain the recurrence tail residual",),
            domain_and_branches=("real inverse-state chart q in [0, 1]",),
            claim_boundary="declared recurrence grammar, not an AMP grammar",
        ),
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
        "generator_ids": ("Q",),
    }


def amp_grammar(*, generator_ids: tuple[str, ...] = ("A", "M", "P")) -> object:
    generators = tuple(
        module.GeneratorWitness(
            generator_id=generator_id,
            finite_action=f"finite {generator_id} flow",
            infinitesimal_action=f"infinitesimal {generator_id} action",
            carrier="positive state chart",
            domain="x > 0 with declared branch",
            task_role=f"{generator_id} process role",
            residual=f"{generator_id} domain residual",
            certificate=f"differentiate the {generator_id} flow at zero",
        )
        for generator_id in generator_ids
    )
    relation_ids = ("A-M", "M-P", "A-P") if "P" in generator_ids else ("A-M",)
    relations = tuple(
        module.GeneratorRelationWitness(
            relation_id=relation_id,
            expression=f"bracket {relation_id}",
            closure_status=(
                module.ClosureStatus.ESCAPES_DECLARED_SPAN
                if relation_id == "A-P"
                else module.ClosureStatus.CLOSES_DECLARED_SPAN
            ),
            residual=f"{relation_id} residual",
            certificate=f"direct coefficient differentiation for {relation_id}",
        )
        for relation_id in relation_ids
    )
    return module.NativeGrammarProfile(
        profile_id="amp-positive-chart",
        family=module.NativeGrammarFamily.AMP,
        required_generators=generator_ids,
        generators=generators,
        legal_compositions=("chronological finite-flow composition",),
        relations=relations,
        closure_obligations=("retain brackets outside the declared span",),
        domain_and_branches=("positive real chart with a fixed real logarithm",),
        claim_boundary="local positive AMP chart only",
    )


def test_incomplete_contract_fails_before_a_trace_exists() -> None:
    incomplete = replace(contract(), primitive_processes=())
    with pytest.raises(module.MethodContractError, match="primitive_processes"):
        module.MethodTrace(incomplete)


def test_amp_contract_fails_when_one_generator_is_missing() -> None:
    incomplete = replace(contract(), native_grammar=amp_grammar(generator_ids=("A", "M")))
    with pytest.raises(module.MethodContractError, match="exactly the A, M, and P"):
        module.MethodTrace(incomplete)


def test_amp_contract_fails_when_ap_escape_is_hidden() -> None:
    grammar = amp_grammar()
    hidden = replace(
        grammar.relations[-1],
        closure_status=module.ClosureStatus.CLOSES_DECLARED_SPAN,
    )
    incomplete = replace(
        contract(),
        native_grammar=replace(
            grammar,
            relations=grammar.relations[:-1] + (hidden,),
        ),
    )
    with pytest.raises(module.MethodContractError, match="must expose escape"):
        module.MethodTrace(incomplete)


def test_amp_contract_fails_when_one_pair_relation_is_missing() -> None:
    grammar = amp_grammar()
    incomplete = replace(
        contract(),
        native_grammar=replace(grammar, relations=grammar.relations[:-1]),
    )
    with pytest.raises(module.MethodContractError, match="requires exactly"):
        module.MethodTrace(incomplete)


def test_amp_native_claim_requires_task_generator_coverage() -> None:
    task = replace(contract().tasks[0], required_generators=("A", "M", "P"))
    trace = module.MethodTrace(
        replace(contract(), tasks=(task,), native_grammar=amp_grammar())
    )
    event = trace.record(
        **{key: value for key, value in event_kwargs().items() if key != "generator_ids"},
        lane=module.MethodLane.NATIVE_EVALUATION,
        mechanism=module.MethodMechanism.NATIVE_PROCESS,
        generator_ids=("A", "M"),
    )
    with pytest.raises(module.EvidenceLaneError, match="missing.*P"):
        trace.claim_native_result(
            task_id="escape-value",
            statement="incomplete AMP result",
            evidence_event_ids=(event.event_id,),
        )


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
