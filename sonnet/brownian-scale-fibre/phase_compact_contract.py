"""Executable compact-space Brownian red-team contract for issue #162."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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
line = _load("brownian_native", Path(__file__).with_name("brownian_native.py"))
compact = _load(
    "compact_space_redteam",
    Path(__file__).with_name("compact_space_redteam.py"),
)


COMPACT_REDTEAM_CONTRACT = firewall.MethodContract(
    contract_id="brownian-compact-space-redteam-c0-s0",
    problem=(
        "separate scale-stable line laws from time-stationary compact-space laws "
        "using exact history-fibre pushforwards"
    ),
    primitive_processes=(
        "chronological nearest-neighbour histories on the integer lattice",
        "deck quotient x -> x mod q",
        "exact rational lazy-clock pushforward on a finite cycle",
    ),
    tasks=(
        firewall.TaskContract(
            task_id="cycle-deck-fibre",
            observer="cycle endpoint after forgetting the integer lift",
            deliverable=(
                "exact residue counts, retained deck fibres, and an independent "
                "direct-cycle certificate"
            ),
            regime="finite nearest-neighbour histories and cycle modulus q >= 2",
            accuracy="exact integer counts",
            claim_mode=firewall.ClaimMode.EXACT_FINITE,
            failure_semantics=("invalid-modulus", "history-mass-mismatch"),
        ),
        firewall.TaskContract(
            task_id="compact-stability-kind",
            observer="terminal cycle law under a declared discrete clock",
            deliverable=(
                "typed periodic obstruction or exact stationary-law certificate"
            ),
            regime="finite cycles with exact rational stay probability",
            accuracy="exact rational mass and period classification",
            claim_mode=firewall.ClaimMode.EXACT_FINITE,
            failure_semantics=(
                "periodic-clock-obstruction",
                "reducible-clock-obstruction",
                "bounded-audit-not-a-limit-theorem",
            ),
        ),
        firewall.TaskContract(
            task_id="sphere-claim-boundary",
            observer="global chart and stability mechanism declared for S^2",
            deliverable="frozen obstruction/residual contract for the next phase",
            regime="semantic gate only; no continuum implementation",
            accuracy="claim-boundary audit",
            claim_mode=firewall.ClaimMode.SEARCH_ONLY,
            failure_semantics=(
                "global-additive-chart-assumption",
                "local-gaussian-promoted-globally",
            ),
        ),
    ),
    native_charts=(
        "integer lift with exact endpoint counts",
        "finite cycle residue chart with retained deck fibre",
        "SO(3)/SO(2) sphere gate with curvature and holonomy residuals",
    ),
    retained_fibres=(
        "integer lift and winding",
        "chronological path",
        "clock period",
        "curvature/chart-transition/holonomy for the sphere phase",
    ),
    native_function_family=(
        "finite counting measures and exact rational laws on additive history fibres"
    ),
    native_composition=(
        "chronological step composition followed by deck-fibre pushforward"
    ),
    native_operators=(
        "integer endpoint addition",
        "residue quotient",
        "finite fibre counting integral",
        "exact lazy-clock pushforward",
    ),
    claim_boundary=(
        "bounded cycle calibration plus circle/sphere semantic gates only; no "
        "continuum heat kernel, mixing theorem, or arithmetic universality claim"
    ),
    allowed_lowerings=(),
    baselines=(
        firewall.BaselineSpec(
            baseline_id="cycle-matrix-baseline",
            mechanism=firewall.MethodMechanism.MATRIX_LINEARIZATION,
            task_scope=("cycle-deck-fibre", "compact-stability-kind"),
            purpose="independent finite transition comparison after native discovery",
            independent_reference="finite cycle transition matrix",
        ),
        firewall.BaselineSpec(
            baseline_id="compact-spectral-baseline",
            mechanism=firewall.MethodMechanism.FOURIER_SPECTRAL,
            task_scope=(
                "cycle-deck-fibre",
                "compact-stability-kind",
                "sphere-claim-boundary",
            ),
            purpose="later independent circle/sphere spectral certificate",
            independent_reference="Fourier or spherical-harmonic heat kernel",
        ),
    ),
).validate()


@dataclass(frozen=True)
class CompactGateResult:
    line_distribution: object
    folded: object
    direct: object
    deck_pushforward_certified: bool
    periodic_obstruction: object
    uniform_stationary_certified: bool
    bounded_mixing: object
    winding_residual: object
    circle_gate: object
    sphere_gate: object
    trace: object


def run_compact_gate() -> CompactGateResult:
    horizon = 7
    modulus = 5
    line_distribution = line.endpoint_fibres(1, horizon)
    folded = compact.fold_integer_endpoint_counts(
        ((point[0], count) for point, count in line_distribution.counts),
        modulus=modulus,
        horizon=horizon,
    )
    direct = compact.direct_cycle_endpoint_counts(modulus, horizon)
    deck_certified = folded.cycle.counts == direct.counts
    if not deck_certified:  # pragma: no cover - exact certificate must fail closed
        raise AssertionError("deck pushforward and direct cycle update disagree")

    try:
        compact.require_terminal_mixing_clock(
            6,
            stay_probability=Fraction(0),
        )
    except compact.PeriodicClockObstruction as error:
        periodic_obstruction = error
    else:  # pragma: no cover - the even cycle must expose period two
        raise AssertionError("even nearest-neighbour cycle hid its period")

    uniform = compact.CycleLaw.uniform(modulus)
    uniform_stationary = (
        compact.cycle_step(uniform, stay_probability=Fraction(1, 2)) == uniform
    )
    if not uniform_stationary:  # pragma: no cover - exact fixed point
        raise AssertionError("uniform cycle law was not stationary")
    bounded_mixing = compact.bounded_lazy_mixing_audit(
        modulus,
        horizon=8,
        stay_probability=Fraction(1, 2),
    )
    winding_residual = compact.expose_winding_residual(
        4,
        (1, 1, 1, 1),
        (1, -1, 1, -1),
    )

    trace = firewall.MethodTrace(COMPACT_REDTEAM_CONTRACT)
    fibre_event = trace.record(
        task_id="cycle-deck-fibre",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.TASK_FIBRE,
        action="push exact integer endpoint counts through the deck quotient",
        input_semantics="finite integer lifts with exact history multiplicities",
        output_semantics="cycle counts plus every retained deck lift",
        cost=firewall.CostLedger(
            evaluation_steps=line_distribution.support_size,
            live_state_units=modulus,
            stored_history_units=sum(len(fibre) for fibre in folded.deck_fibres),
            residual_units=1,
        ),
    )
    direct_certificate = trace.record(
        task_id="cycle-deck-fibre",
        lane=firewall.MethodLane.CERTIFICATE,
        mechanism=firewall.MethodMechanism.EXACT_FINITE_ENUMERATION,
        action="compare folded counts with an independent direct cycle update",
        input_semantics="two exact constructions with one horizon and modulus",
        output_semantics="zero residue-count mismatch",
        cost=firewall.CostLedger(
            evaluation_steps=2 * modulus * horizon,
            stored_history_units=modulus,
        ),
    )
    stability_event = trace.record(
        task_id="compact-stability-kind",
        lane=firewall.MethodLane.NATIVE_DISCOVERY,
        mechanism=firewall.MethodMechanism.NATIVE_PROCESS,
        action="classify the discrete clock before making a terminal mixing claim",
        input_semantics="cycle modulus and exact stay probability",
        output_semantics="typed period-two obstruction or an aperiodic clock witness",
        cost=firewall.CostLedger(discovery_steps=2, residual_units=1),
    )
    stationary_event = trace.record(
        task_id="compact-stability-kind",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.NATIVE_FUNCTION_FAMILY,
        action="apply one lazy cycle step to the exact uniform law",
        input_semantics="rational cycle law and declared lazy clock",
        output_semantics="exact stationary uniform law and bounded distance audit",
        cost=firewall.CostLedger(
            evaluation_steps=modulus * 3 * 9,
            live_state_units=modulus,
            residual_units=1,
        ),
    )
    trace.claim_native_result(
        task_id="cycle-deck-fibre",
        statement="cycle endpoint counts are the exact deck-fibre pushforward of line counts",
        evidence_event_ids=(fibre_event.event_id, direct_certificate.event_id),
    )
    trace.claim_native_result(
        task_id="compact-stability-kind",
        statement=(
            "compact time-stationarity requires a clock classification and is not "
            "the line's scale-renormalized stability"
        ),
        evidence_event_ids=(stability_event.event_id, stationary_event.event_id),
    )
    return CompactGateResult(
        line_distribution=line_distribution,
        folded=folded,
        direct=direct,
        deck_pushforward_certified=deck_certified,
        periodic_obstruction=periodic_obstruction,
        uniform_stationary_certified=uniform_stationary,
        bounded_mixing=bounded_mixing,
        winding_residual=winding_residual,
        circle_gate=compact.CIRCLE_GATE,
        sphere_gate=compact.SPHERE_GATE,
        trace=trace,
    )
