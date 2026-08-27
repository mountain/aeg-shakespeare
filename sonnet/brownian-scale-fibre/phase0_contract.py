"""Frozen S0/S1 method contract and executable audit for issue #158."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, path: Path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    loaded = importlib.util.module_from_spec(spec)
    sys.modules[name] = loaded
    spec.loader.exec_module(loaded)
    return loaded


firewall = _load(
    "native_method_firewall",
    ROOT / "workstreams/native_method_firewall/native_method_firewall.py",
)
native = _load("brownian_native", Path(__file__).with_name("brownian_native.py"))


METHOD_CONTRACT = firewall.MethodContract(
    contract_id="brownian-scale-fibre-s0-s1",
    problem=(
        "derive the first fluctuation scale and endpoint-fibre composition "
        "from raw finite increment histories"
    ),
    primitive_processes=(
        "chronological independent finite-increment histories",
        "nearest-neighbour histories on the integer lattice",
    ),
    tasks=(
        firewall.TaskContract(
            task_id="blind-scale",
            observer=(
                "nonzero finite response of the centered aggregate under an "
                "unknown power scale"
            ),
            deliverable=(
                "active centered response order, balance equation, and solved exponent"
            ),
            regime="centered nondegenerate finite-support increment laws",
            accuracy="exact rational scale balance",
            claim_mode=firewall.ClaimMode.EXACT_SYMBOLIC,
            failure_semantics=(
                "centering-required",
                "degenerate-second-response",
                "outside-finite-law-grammar",
            ),
        ),
        firewall.TaskContract(
            task_id="endpoint-fibre",
            observer="endpoint after a declared finite horizon",
            deliverable=(
                "exact fibre counts, pushforward probabilities, and concatenation certificate"
            ),
            regime="bounded nearest-neighbour histories on the integer lattice",
            accuracy="exact integer counts and rational probabilities",
            claim_mode=firewall.ClaimMode.EXACT_FINITE,
            failure_semantics=("invalid-history", "transition-budget-exhausted"),
        ),
    ),
    native_charts=(
        "aggregate probe scale s=N^(-a)*xi with a solved rather than supplied",
        "integer-lattice endpoint chart",
    ),
    retained_fibres=(
        "increment law and exact centering witness",
        "endpoint fibre multiplicity",
        "literal history remains residual for path-sensitive tasks",
    ),
    native_function_family=(
        "finite-law cumulant atom under independent composition, with exact "
        "integral response identity"
    ),
    native_composition=(
        "chronological history concatenation; endpoint addition and exact mass pushforward"
    ),
    native_operators=(
        "exact centering and centered response",
        "scale-balance solve",
        "endpoint pushforward",
        "history concatenation",
    ),
    claim_boundary=(
        "S0/S1 only: no continuum limit law, path-space limit, recurrence theorem, "
        "physical decoder, efficiency theorem, or new stochastic calculus"
    ),
    allowed_lowerings=(),
    baselines=(
        firewall.BaselineSpec(
            baseline_id="spectral-endpoint-check",
            mechanism=firewall.MethodMechanism.FOURIER_SPECTRAL,
            task_scope=("blind-scale", "endpoint-fibre"),
            purpose="independent classical transform check after native discovery",
            independent_reference="finite characteristic function or continuum limit",
        ),
        firewall.BaselineSpec(
            baseline_id="local-response-check",
            mechanism=firewall.MethodMechanism.POWER_SERIES,
            task_scope=("blind-scale",),
            purpose="post-discovery coefficient red team",
            independent_reference="classical local cumulant calculation",
        ),
        firewall.BaselineSpec(
            baseline_id="simulation-check",
            mechanism=firewall.MethodMechanism.BLACK_BOX_NUMERICS,
            task_scope=("endpoint-fibre",),
            purpose="independent sampling comparison for later large workloads",
            independent_reference="seeded random-walk simulation",
        ),
    ),
).validate()


@dataclass(frozen=True)
class Phase0Result:
    scale: object
    endpoint_distribution: object
    concatenation_certified: bool
    trace: object


def run_phase0() -> Phase0Result:
    law = native.FiniteIncrementLaw.symmetric_unit()
    scale = native.discover_diffusive_scale(law)
    left = native.endpoint_fibres(1, 2)
    right = native.endpoint_fibres(1, 3)
    endpoint = native.endpoint_fibres(1, 5)
    composed = native.concatenate_endpoint_fibres(left, right)
    concatenation_certified = composed.counts == endpoint.counts
    if not concatenation_certified:  # pragma: no cover - fail closed
        raise AssertionError("endpoint pushforward did not preserve concatenation")

    trace = firewall.MethodTrace(METHOD_CONTRACT)
    scale_event = trace.record(
        task_id="blind-scale",
        lane=firewall.MethodLane.NATIVE_DISCOVERY,
        mechanism=firewall.MethodMechanism.NATIVE_FUNCTION_FAMILY,
        action="derive centered response order and solve population/scale balance",
        input_semantics="raw symmetric unit increment law; no target exponent",
        output_semantics="exact scale-balance certificate",
        cost=firewall.CostLedger(
            discovery_steps=scale.cost.exact_weighted_additions,
            live_state_units=scale.cost.law_atoms,
        ),
    )
    fibre_event = trace.record(
        task_id="endpoint-fibre",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.TASK_FIBRE,
        action="push chronological histories to exact endpoint fibres",
        input_semantics="nearest-neighbour step grammar and finite horizon",
        output_semantics="endpoint counts and rational pushforward law",
        cost=firewall.CostLedger(
            evaluation_steps=endpoint.cost.transition_updates,
            live_state_units=endpoint.cost.peak_live_fibres,
            stored_history_units=endpoint.cost.stored_endpoint_fibres,
        ),
    )
    certificate_event = trace.record(
        task_id="endpoint-fibre",
        lane=firewall.MethodLane.CERTIFICATE,
        mechanism=firewall.MethodMechanism.EXACT_FINITE_ENUMERATION,
        action="compare direct horizon-five fibres with the two-plus-three pushforward",
        input_semantics="two independently constructed exact endpoint tables",
        output_semantics="zero count residual at every endpoint",
        cost=firewall.CostLedger(
            evaluation_steps=composed.cost.transition_updates,
            stored_history_units=composed.cost.stored_endpoint_fibres,
        ),
    )
    trace.claim_native_result(
        task_id="blind-scale",
        statement="the centered finite law forces the declared scale balance",
        evidence_event_ids=(scale_event.event_id,),
    )
    trace.claim_native_result(
        task_id="endpoint-fibre",
        statement="endpoint pushforward descends history concatenation exactly",
        evidence_event_ids=(fibre_event.event_id, certificate_event.event_id),
    )
    return Phase0Result(scale, endpoint, concatenation_certified, trace)
