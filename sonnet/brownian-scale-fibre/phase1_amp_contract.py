"""Executable Brownian AMP generator/chart gate for correction issue #160."""

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
discrete = _load("brownian_native", Path(__file__).with_name("brownian_native.py"))
amp = _load("brownian_amp", Path(__file__).with_name("brownian_amp.py"))


AMP_GRAMMAR = firewall.NativeGrammarProfile(
    profile_id="brownian-positive-real-amp",
    family=firewall.NativeGrammarFamily.AMP,
    required_generators=("A", "M", "P"),
    generators=(
        firewall.GeneratorWitness(
            generator_id="A",
            finite_action="A_t(x)=x+t",
            infinitesimal_action="A=d/dx",
            carrier="positive real state or positive ensemble observer",
            domain="translation must retain the chosen carrier domain",
            task_role="state translation and chronological increment accumulation",
            residual="a symmetric position history can hit zero or the negative half-line",
            certificate="differentiate A_t at t=0 and replay additive composition",
        ),
        firewall.GeneratorWitness(
            generator_id="M",
            finite_action="M_s(x)=exp(s)*x",
            infinitesimal_action="M=x*d/dx",
            carrier="positive real state or exponential-observer exponents",
            domain="positive multiplicative scale",
            task_role="change physical or observer scale",
            residual="zero is a fixed boundary not contained in the positive chart",
            certificate="differentiate M_s at s=0 and replay positive-scale composition",
        ),
        firewall.GeneratorWitness(
            generator_id="P",
            finite_action="P_r(x)=exp(exp(r)*Log(x))",
            infinitesimal_action="P=x*log(x)*d/dx",
            carrier="positive real state or pointwise-positive ensemble observer",
            domain="x>0 with a declared real Log branch",
            task_role="replica power and scale-of-scale transport",
            residual=(
                "noninteger powers generally exit the finite exponential-atom carrier"
            ),
            certificate="differentiate P_r at r=0; integer replicas use exact products",
        ),
    ),
    legal_compositions=(
        "chronological composition of finite A/M/P flows on their common domain",
        "M/P affine subgroup in Log coordinate",
        "integer replica composition of independent ensemble observers",
    ),
    relations=(
        firewall.GeneratorRelationWitness(
            relation_id="A-M",
            expression="[A,M]=A",
            closure_status=firewall.ClosureStatus.CLOSES_DECLARED_SPAN,
            residual="none inside the A/M subsystem",
            certificate="differentiate vector-field coefficients directly",
        ),
        firewall.GeneratorRelationWitness(
            relation_id="M-P",
            expression="[M,P]=M",
            closure_status=firewall.ClosureStatus.CLOSES_DECLARED_SPAN,
            residual="none inside the M/P subsystem",
            certificate="differentiate vector-field coefficients directly",
        ),
        firewall.GeneratorRelationWitness(
            relation_id="A-P",
            expression="[A,P]=(1+log(x))*d/dx",
            closure_status=firewall.ClosureStatus.ESCAPES_DECLARED_SPAN,
            residual="new log-weighted vector fields beyond span{A,M,P}",
            certificate="compare the coefficient with constants times 1,x,x*log(x)",
        ),
    ),
    closure_obligations=(
        "retain the infinite family V_(m,n)=x^m*(log(x))^n*d/dx as a residual",
        "do not describe full A/M/P as one three-dimensional Lie group",
    ),
    domain_and_branches=(
        "position chart requires x>0 and fails at zero or negative states",
        "ensemble observer Z(s)>0 for real s, but finite atoms are not closed under noninteger P",
    ),
    claim_boundary=(
        "Brownian AMP chart gate only; no continuum Brownian law, recurrence, heat kernel, "
        "or complexity advantage is certified"
    ),
)


AMP_METHOD_CONTRACT = firewall.MethodContract(
    contract_id="brownian-amp-generator-chart-gate",
    problem=(
        "test whether Brownian processes admit an A/M/P-native chart without hiding "
        "domain, closure, or path-information residuals"
    ),
    primitive_processes=(
        "finite A/M/P flows on a positive carrier",
        "independent composition of finite exponential observers",
    ),
    tasks=(
        firewall.TaskContract(
            task_id="position-chart-domain",
            observer="common real domain of the A/M/P position flows along a history",
            deliverable="positive-chart witness or typed first-exit obstruction",
            regime="finite exact rational position histories",
            accuracy="exact order and sign comparison",
            claim_mode=firewall.ClaimMode.EXACT_FINITE,
            failure_semantics=("zero-crossing", "negative-state", "inexact-input"),
            required_generators=("A", "M", "P"),
        ),
        firewall.TaskContract(
            task_id="ensemble-amp-adapter",
            observer="finite exact exponential observer Z(s)=E[exp(sX)]",
            deliverable="exact A shift, M scale, integer-P replica, and endpoint-fibre certificate",
            regime="finite integer laws, rational shifts/scales, integer replicas",
            accuracy="exact rational atom coefficients",
            claim_mode=firewall.ClaimMode.EXACT_SYMBOLIC,
            failure_semantics=(
                "nonpositive-scale",
                "noninteger-replica",
                "finite-carrier-closure-failure",
            ),
            required_generators=("A", "M", "P"),
        ),
        firewall.TaskContract(
            task_id="path-information-residual",
            observer="collision of distinct histories under the endpoint observer",
            deliverable="explicit lost path observable",
            regime="finite rational increment histories with a shared endpoint",
            accuracy="exact history and endpoint equality",
            claim_mode=firewall.ClaimMode.EXACT_FINITE,
            failure_semantics=("different-endpoints", "identical-histories"),
            required_generators=("A",),
        ),
    ),
    native_charts=(
        "positive position chart x>0 with real Log",
        "positive ensemble observer Z(s) with finite exponential atoms E_q",
    ),
    retained_fibres=(
        "first position-chart exit",
        "noninteger-P finite-carrier closure residual",
        "literal path information lost by the endpoint observer",
    ),
    native_function_family=(
        "finite exact rational sums of exponential atoms E_q with E_p*E_q=E_(p+q)"
    ),
    native_composition=(
        "finite A/M/P action plus exact independent-law product in the ensemble chart"
    ),
    native_operators=(
        "state translation",
        "positive state scaling",
        "integer replica power",
        "typed common-domain audit",
    ),
    claim_boundary=(
        "chart admissibility and exact finite adapter identities only; the PRE-AMP "
        "scale result is not promoted to an AMP Brownian theorem"
    ),
    native_grammar=AMP_GRAMMAR,
    allowed_lowerings=(),
    baselines=(),
).validate()


@dataclass(frozen=True)
class PositionObstructionCertificate:
    step_index: int
    value: Fraction
    offending_increment: Fraction | None
    typed_reason: str


@dataclass(frozen=True)
class EnsembleAMPCertificate:
    base: object
    shifted: object
    scaled: object
    replica: object
    shift_inverse_certified: bool
    scale_inverse_certified: bool
    endpoint_fibre_certified: bool
    noninteger_power_residual: str


@dataclass(frozen=True)
class AMPGateResult:
    positive_history: object
    position_obstruction: PositionObstructionCertificate
    ensemble: EnsembleAMPCertificate
    path_residual: object
    trace: object


def run_amp_gate() -> AMPGateResult:
    positive_history = amp.audit_positive_position_history(
        Fraction(2),
        (Fraction(1), Fraction(-1)),
    )
    try:
        amp.audit_positive_position_history(
            Fraction(1),
            (Fraction(-1), Fraction(1)),
        )
    except amp.PositionChartDomainError as error:
        obstruction = PositionObstructionCertificate(
            step_index=error.step_index,
            value=error.value,
            offending_increment=error.offending_increment,
            typed_reason=str(error),
        )
    else:  # pragma: no cover - the exact zero crossing must fail closed
        raise AssertionError("symmetric history unexpectedly stayed in x > 0")

    law = discrete.FiniteIncrementLaw.symmetric_unit()
    base = amp.ExponentialObserver.from_finite_law(law.support, law.weights)
    translation = Fraction(2)
    scale = Fraction(3)
    shifted = base.shift_state(translation)
    scaled = base.scale_state(scale)
    replica = base.replica_power(5)
    shift_inverse = shifted.shift_state(-translation) == base
    scale_inverse = scaled.scale_state(Fraction(1, 3)) == base

    endpoint = discrete.endpoint_fibres(1, 5)
    endpoints = {Fraction(point[0]) for point, _ in endpoint.counts}
    observer_endpoints = {exponent for exponent, _ in replica.observer.terms}
    endpoint_certified = endpoints == observer_endpoints and all(
        replica.observer.coefficient(Fraction(point[0]))
        == endpoint.probability(point)
        for point, _ in endpoint.counts
    )
    if not endpoint_certified:  # pragma: no cover - exact identity must fail closed
        raise AssertionError("replica power did not reproduce endpoint fibres")
    ensemble = EnsembleAMPCertificate(
        base=base,
        shifted=shifted,
        scaled=scaled,
        replica=replica,
        shift_inverse_certified=shift_inverse,
        scale_inverse_certified=scale_inverse,
        endpoint_fibre_certified=endpoint_certified,
        noninteger_power_residual=replica.residual,
    )

    path_residual = amp.expose_path_information_residual(
        (Fraction(1), Fraction(-1)),
        (Fraction(-1), Fraction(1)),
    )

    trace = firewall.MethodTrace(AMP_METHOD_CONTRACT)
    position_event = trace.record(
        task_id="position-chart-domain",
        lane=firewall.MethodLane.NATIVE_DISCOVERY,
        mechanism=firewall.MethodMechanism.TASK_FIBRE,
        action="audit the common positive domain along additive histories",
        input_semantics="exact rational initial state and chronological A increments",
        output_semantics="positive witness plus typed zero-crossing obstruction",
        generator_ids=("A", "M", "P"),
        cost=firewall.CostLedger(
            discovery_steps=len(positive_history.increments) + obstruction.step_index,
            live_state_units=1,
            residual_units=1,
        ),
    )
    ensemble_event = trace.record(
        task_id="ensemble-amp-adapter",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.NATIVE_FUNCTION_FAMILY,
        action="apply exact A shift, M scale, and integer P replica composition",
        input_semantics="finite exact exponential observer with rational atoms",
        output_semantics="exact transformed atoms and explicit noninteger-P residual",
        generator_ids=("A", "M", "P"),
        cost=firewall.CostLedger(
            evaluation_steps=replica.atom_products,
            live_state_units=len(replica.observer.terms),
            residual_units=1,
        ),
    )
    certificate_event = trace.record(
        task_id="ensemble-amp-adapter",
        lane=firewall.MethodLane.CERTIFICATE,
        mechanism=firewall.MethodMechanism.EXACT_FINITE_ENUMERATION,
        action="compare replica atom coefficients with PRE-AMP endpoint fibres",
        input_semantics="two independently constructed exact rational laws",
        output_semantics="zero coefficient residual at every endpoint",
        cost=firewall.CostLedger(
            evaluation_steps=len(endpoint.counts),
            stored_history_units=endpoint.support_size,
        ),
    )
    path_event = trace.record(
        task_id="path-information-residual",
        lane=firewall.MethodLane.NATIVE_EVALUATION,
        mechanism=firewall.MethodMechanism.TASK_FIBRE,
        action="compare two chronological histories under the endpoint observer",
        input_semantics="distinct A histories with an equal aggregate",
        output_semantics="shared observer and named lost path information",
        generator_ids=("A",),
        cost=firewall.CostLedger(
            evaluation_steps=len(path_residual.left_history)
            + len(path_residual.right_history),
            residual_units=1,
        ),
    )
    trace.claim_native_result(
        task_id="position-chart-domain",
        statement="the real positive position AMP chart is not global for symmetric histories",
        evidence_event_ids=(position_event.event_id,),
    )
    trace.claim_native_result(
        task_id="ensemble-amp-adapter",
        statement=(
            "A shift, M scale, and integer-P replicas are exact in the finite "
            "ensemble carrier within its declared closure boundary"
        ),
        evidence_event_ids=(ensemble_event.event_id, certificate_event.event_id),
    )
    trace.claim_native_result(
        task_id="path-information-residual",
        statement="the endpoint ensemble observer does not retain chronological paths",
        evidence_event_ids=(path_event.event_id,),
    )
    return AMPGateResult(
        positive_history=positive_history,
        position_obstruction=obstruction,
        ensemble=ensemble,
        path_residual=path_residual,
        trace=trace,
    )
