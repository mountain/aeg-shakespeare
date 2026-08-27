"""Research-local lane and lowering audit for Process Geometry calculations.

This module is deliberately outside ``src/process_geometry``.  It records and
checks a research method; it is not a generic solver or a package API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import json
from typing import Iterable


class MethodContractError(ValueError):
    """A method contract or trace violates its declared semantics."""


class PrematureLoweringError(MethodContractError):
    """A classical mechanism entered a native lane without a scoped witness."""


class EvidenceLaneError(MethodContractError):
    """Evidence from one lane was claimed as evidence from another lane."""


class MethodLane(str, Enum):
    NATIVE_DISCOVERY = "native-discovery"
    NATIVE_EVALUATION = "native-evaluation"
    CERTIFICATE = "certificate"
    BASELINE = "baseline"


class MethodMechanism(str, Enum):
    """Mechanisms are typed so renaming cannot evade the lane audit."""

    NATIVE_PROCESS = "native-process"
    TASK_FIBRE = "task-fibre"
    NATIVE_FUNCTION_FAMILY = "native-function-family"
    EXACT_FINITE_ENUMERATION = "exact-finite-enumeration"
    ORDINARY_POLYNOMIAL = "ordinary-polynomial"
    POWER_SERIES = "power-series"
    MATRIX_LINEARIZATION = "matrix-linearization"
    FOURIER_SPECTRAL = "fourier-spectral"
    KOOPMAN_CARLEMAN = "koopman-carleman"
    GENERIC_CAS = "generic-cas"
    BLACK_BOX_NUMERICS = "black-box-numerics"


CLASSICAL_MECHANISMS = frozenset(
    {
        MethodMechanism.ORDINARY_POLYNOMIAL,
        MethodMechanism.POWER_SERIES,
        MethodMechanism.MATRIX_LINEARIZATION,
        MethodMechanism.FOURIER_SPECTRAL,
        MethodMechanism.KOOPMAN_CARLEMAN,
        MethodMechanism.GENERIC_CAS,
        MethodMechanism.BLACK_BOX_NUMERICS,
    }
)


class AdequacyGrade(str, Enum):
    TASK_EXACT = "task-exact"
    TASK_APPROXIMATE = "task-approximate"


class ClaimMode(str, Enum):
    EXACT_SYMBOLIC = "exact-symbolic"
    EXACT_FINITE = "exact-finite"
    CERTIFIED_APPROXIMATE = "certified-approximate"
    NUMERICAL = "numerical"
    STOCHASTIC = "stochastic"
    SEARCH_ONLY = "search-only"


class NativeGrammarFamily(str, Enum):
    """The process grammar whose generators make a result native."""

    DECLARED = "declared"
    AMP = "amp"


class ClosureStatus(str, Enum):
    CLOSES_DECLARED_SPAN = "closes-declared-span"
    ESCAPES_DECLARED_SPAN = "escapes-declared-span"
    TASK_SCOPED = "task-scoped"


AMP_GENERATOR_IDS = frozenset({"A", "M", "P"})
AMP_RELATION_IDS = frozenset({"A-M", "M-P", "A-P"})


def _require_text(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise MethodContractError(f"{field_name} must be non-empty text")


def _require_texts(values: Iterable[str], field_name: str) -> None:
    values = tuple(values)
    if not values:
        raise MethodContractError(f"{field_name} must not be empty")
    for value in values:
        _require_text(value, field_name)


def _enum_value(value: object, enum_type: type[Enum], field_name: str) -> Enum:
    try:
        return enum_type(value)
    except (TypeError, ValueError) as exc:
        raise MethodContractError(f"unknown {field_name}: {value!r}") from exc


@dataclass(frozen=True)
class TaskContract:
    task_id: str
    observer: str
    deliverable: str
    regime: str
    accuracy: str
    claim_mode: ClaimMode
    failure_semantics: tuple[str, ...]
    required_generators: tuple[str, ...] = ()

    def validate(self) -> None:
        for name in ("task_id", "observer", "deliverable", "regime", "accuracy"):
            _require_text(getattr(self, name), f"task.{name}")
        _enum_value(self.claim_mode, ClaimMode, "claim mode")
        _require_texts(self.failure_semantics, "task.failure_semantics")
        if self.required_generators:
            _require_texts(self.required_generators, "task.required_generators")
            if len(set(self.required_generators)) != len(self.required_generators):
                raise MethodContractError("task required generator ids must be unique")

    def as_dict(self) -> dict[str, object]:
        return {
            "task_id": self.task_id,
            "observer": self.observer,
            "deliverable": self.deliverable,
            "regime": self.regime,
            "accuracy": self.accuracy,
            "claim_mode": ClaimMode(self.claim_mode).value,
            "failure_semantics": list(self.failure_semantics),
            "required_generators": list(self.required_generators),
        }


@dataclass(frozen=True)
class GeneratorWitness:
    generator_id: str
    finite_action: str
    infinitesimal_action: str
    carrier: str
    domain: str
    task_role: str
    residual: str
    certificate: str

    def validate(self) -> None:
        for name in self.__dataclass_fields__:
            _require_text(getattr(self, name), f"generator.{name}")

    def as_dict(self) -> dict[str, str]:
        return {name: getattr(self, name) for name in self.__dataclass_fields__}


@dataclass(frozen=True)
class GeneratorRelationWitness:
    relation_id: str
    expression: str
    closure_status: ClosureStatus
    residual: str
    certificate: str

    def validate(self) -> None:
        for name in ("relation_id", "expression", "residual", "certificate"):
            _require_text(getattr(self, name), f"relation.{name}")
        _enum_value(self.closure_status, ClosureStatus, "closure status")

    def as_dict(self) -> dict[str, str]:
        return {
            "relation_id": self.relation_id,
            "expression": self.expression,
            "closure_status": ClosureStatus(self.closure_status).value,
            "residual": self.residual,
            "certificate": self.certificate,
        }


@dataclass(frozen=True)
class NativeGrammarProfile:
    profile_id: str
    family: NativeGrammarFamily
    required_generators: tuple[str, ...]
    generators: tuple[GeneratorWitness, ...]
    legal_compositions: tuple[str, ...]
    relations: tuple[GeneratorRelationWitness, ...]
    closure_obligations: tuple[str, ...]
    domain_and_branches: tuple[str, ...]
    claim_boundary: str

    def validate(self) -> None:
        _require_text(self.profile_id, "grammar.profile_id")
        family = _enum_value(self.family, NativeGrammarFamily, "grammar family")
        _require_texts(self.required_generators, "grammar.required_generators")
        _require_texts(self.legal_compositions, "grammar.legal_compositions")
        _require_texts(self.closure_obligations, "grammar.closure_obligations")
        _require_texts(self.domain_and_branches, "grammar.domain_and_branches")
        _require_text(self.claim_boundary, "grammar.claim_boundary")

        if len(set(self.required_generators)) != len(self.required_generators):
            raise MethodContractError("grammar required generator ids must be unique")
        if not self.generators:
            raise MethodContractError("grammar.generators must not be empty")
        for generator in self.generators:
            generator.validate()
        generator_ids = tuple(item.generator_id for item in self.generators)
        if len(set(generator_ids)) != len(generator_ids):
            raise MethodContractError("generator witness ids must be unique")
        if set(generator_ids) != set(self.required_generators):
            raise MethodContractError(
                "generator witnesses must exactly cover required_generators"
            )

        if not self.relations:
            raise MethodContractError("grammar.relations must not be empty")
        for relation in self.relations:
            relation.validate()
        relation_ids = tuple(item.relation_id for item in self.relations)
        if len(set(relation_ids)) != len(relation_ids):
            raise MethodContractError("generator relation ids must be unique")

        if family is NativeGrammarFamily.AMP:
            if set(self.required_generators) != AMP_GENERATOR_IDS:
                raise MethodContractError(
                    "AMP grammar requires exactly the A, M, and P generators"
                )
            if set(relation_ids) != AMP_RELATION_IDS:
                raise MethodContractError(
                    "AMP grammar requires exactly A-M, M-P, and A-P relations"
                )
            relation_map = {item.relation_id: item for item in self.relations}
            for relation_id in ("A-M", "M-P"):
                if (
                    ClosureStatus(relation_map[relation_id].closure_status)
                    is not ClosureStatus.CLOSES_DECLARED_SPAN
                ):
                    raise MethodContractError(
                        f"AMP {relation_id} relation must close the declared span"
                    )
            if (
                ClosureStatus(relation_map["A-P"].closure_status)
                is not ClosureStatus.ESCAPES_DECLARED_SPAN
            ):
                raise MethodContractError(
                    "AMP A-P relation must expose escape from the three-generator span"
                )

    @property
    def generator_ids(self) -> frozenset[str]:
        return frozenset(self.required_generators)

    def as_dict(self) -> dict[str, object]:
        self.validate()
        return {
            "profile_id": self.profile_id,
            "family": NativeGrammarFamily(self.family).value,
            "required_generators": list(self.required_generators),
            "generators": [item.as_dict() for item in self.generators],
            "legal_compositions": list(self.legal_compositions),
            "relations": [item.as_dict() for item in self.relations],
            "closure_obligations": list(self.closure_obligations),
            "domain_and_branches": list(self.domain_and_branches),
            "claim_boundary": self.claim_boundary,
        }


@dataclass(frozen=True)
class LoweringWitness:
    witness_id: str
    mechanism: MethodMechanism
    source_presentation: str
    target_presentation: str
    task_scope: tuple[str, ...]
    allowed_lanes: tuple[MethodLane, ...]
    adequacy_grade: AdequacyGrade
    preserved_information: tuple[str, ...]
    forgotten_information: tuple[str, ...]
    residual: str
    decoder: str
    certificate: str
    failure_semantics: tuple[str, ...]

    def validate(self, task_ids: frozenset[str]) -> None:
        for name in (
            "witness_id",
            "source_presentation",
            "target_presentation",
            "residual",
            "decoder",
            "certificate",
        ):
            _require_text(getattr(self, name), f"lowering.{name}")
        mechanism = _enum_value(self.mechanism, MethodMechanism, "mechanism")
        if mechanism not in CLASSICAL_MECHANISMS:
            raise MethodContractError(
                "a lowering witness must name a classical/lowered mechanism"
            )
        _enum_value(self.adequacy_grade, AdequacyGrade, "adequacy grade")
        _require_texts(self.task_scope, "lowering.task_scope")
        unknown_tasks = set(self.task_scope) - task_ids
        if unknown_tasks:
            raise MethodContractError(
                f"lowering {self.witness_id!r} has unknown tasks: "
                f"{sorted(unknown_tasks)!r}"
            )
        if not self.allowed_lanes:
            raise MethodContractError("lowering.allowed_lanes must not be empty")
        lanes = {
            _enum_value(lane, MethodLane, "method lane") for lane in self.allowed_lanes
        }
        native_lanes = {
            MethodLane.NATIVE_DISCOVERY,
            MethodLane.NATIVE_EVALUATION,
        }
        if not lanes <= native_lanes:
            raise MethodContractError(
                "lowering witnesses apply only inside declared native lanes"
            )
        _require_texts(self.preserved_information, "lowering.preserved_information")
        _require_texts(self.forgotten_information, "lowering.forgotten_information")
        _require_texts(self.failure_semantics, "lowering.failure_semantics")

    def as_dict(self) -> dict[str, object]:
        return {
            "witness_id": self.witness_id,
            "mechanism": MethodMechanism(self.mechanism).value,
            "source_presentation": self.source_presentation,
            "target_presentation": self.target_presentation,
            "task_scope": list(self.task_scope),
            "allowed_lanes": [MethodLane(lane).value for lane in self.allowed_lanes],
            "adequacy_grade": AdequacyGrade(self.adequacy_grade).value,
            "preserved_information": list(self.preserved_information),
            "forgotten_information": list(self.forgotten_information),
            "residual": self.residual,
            "decoder": self.decoder,
            "certificate": self.certificate,
            "failure_semantics": list(self.failure_semantics),
        }


@dataclass(frozen=True)
class BaselineSpec:
    baseline_id: str
    mechanism: MethodMechanism
    task_scope: tuple[str, ...]
    purpose: str
    independent_reference: str

    def validate(self, task_ids: frozenset[str]) -> None:
        for name in ("baseline_id", "purpose", "independent_reference"):
            _require_text(getattr(self, name), f"baseline.{name}")
        _enum_value(self.mechanism, MethodMechanism, "mechanism")
        _require_texts(self.task_scope, "baseline.task_scope")
        unknown_tasks = set(self.task_scope) - task_ids
        if unknown_tasks:
            raise MethodContractError(
                f"baseline {self.baseline_id!r} has unknown tasks: "
                f"{sorted(unknown_tasks)!r}"
            )

    def as_dict(self) -> dict[str, object]:
        return {
            "baseline_id": self.baseline_id,
            "mechanism": MethodMechanism(self.mechanism).value,
            "task_scope": list(self.task_scope),
            "purpose": self.purpose,
            "independent_reference": self.independent_reference,
        }


@dataclass(frozen=True)
class CostLedger:
    """Non-scalarized, unit-free operation counts for one trace event."""

    discovery_steps: int = 0
    compilation_steps: int = 0
    evaluation_steps: int = 0
    live_state_units: int = 0
    stored_history_units: int = 0
    residual_units: int = 0
    decoder_steps: int = 0

    def validate(self) -> None:
        for name in self.__dataclass_fields__:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise MethodContractError(f"cost.{name} must be a non-negative integer")

    def as_dict(self) -> dict[str, int]:
        return {name: getattr(self, name) for name in self.__dataclass_fields__}

    def __add__(self, other: "CostLedger") -> "CostLedger":
        return CostLedger(
            **{
                name: getattr(self, name) + getattr(other, name)
                for name in self.__dataclass_fields__
            }
        )


@dataclass(frozen=True)
class MethodContract:
    contract_id: str
    problem: str
    primitive_processes: tuple[str, ...]
    tasks: tuple[TaskContract, ...]
    native_charts: tuple[str, ...]
    retained_fibres: tuple[str, ...]
    native_function_family: str
    native_composition: str
    native_operators: tuple[str, ...]
    claim_boundary: str
    native_grammar: NativeGrammarProfile
    forbidden_premature_lowerings: frozenset[MethodMechanism] = field(
        default_factory=lambda: CLASSICAL_MECHANISMS
    )
    allowed_lowerings: tuple[LoweringWitness, ...] = ()
    baselines: tuple[BaselineSpec, ...] = ()

    def validate(self) -> "MethodContract":
        for name in (
            "contract_id",
            "problem",
            "native_function_family",
            "native_composition",
            "claim_boundary",
        ):
            _require_text(getattr(self, name), name)
        _require_texts(self.primitive_processes, "primitive_processes")
        _require_texts(self.native_charts, "native_charts")
        _require_texts(self.retained_fibres, "retained_fibres")
        _require_texts(self.native_operators, "native_operators")
        self.native_grammar.validate()
        if not self.tasks:
            raise MethodContractError("tasks must not be empty")
        for task in self.tasks:
            task.validate()
        task_ids = tuple(task.task_id for task in self.tasks)
        if len(set(task_ids)) != len(task_ids):
            raise MethodContractError("task ids must be unique")
        known_tasks = frozenset(task_ids)
        grammar_generators = self.native_grammar.generator_ids
        for task in self.tasks:
            unknown_generators = set(task.required_generators) - grammar_generators
            if unknown_generators:
                raise MethodContractError(
                    f"task {task.task_id!r} has unknown required generators: "
                    f"{sorted(unknown_generators)!r}"
                )

        forbidden = {
            _enum_value(mechanism, MethodMechanism, "mechanism")
            for mechanism in self.forbidden_premature_lowerings
        }
        if not forbidden <= CLASSICAL_MECHANISMS:
            raise MethodContractError(
                "forbidden_premature_lowerings may contain only classical mechanisms"
            )
        if forbidden != CLASSICAL_MECHANISMS:
            missing = sorted(
                mechanism.value for mechanism in CLASSICAL_MECHANISMS - forbidden
            )
            raise MethodContractError(
                "the research firewall must enumerate every classical mechanism; "
                f"missing {missing!r}"
            )

        lowering_ids = tuple(witness.witness_id for witness in self.allowed_lowerings)
        if len(set(lowering_ids)) != len(lowering_ids):
            raise MethodContractError("lowering witness ids must be unique")
        for witness in self.allowed_lowerings:
            witness.validate(known_tasks)

        baseline_ids = tuple(baseline.baseline_id for baseline in self.baselines)
        if len(set(baseline_ids)) != len(baseline_ids):
            raise MethodContractError("baseline ids must be unique")
        for baseline in self.baselines:
            baseline.validate(known_tasks)
        return self

    @property
    def task_ids(self) -> frozenset[str]:
        return frozenset(task.task_id for task in self.tasks)

    def lowering(self, witness_id: str) -> LoweringWitness:
        for witness in self.allowed_lowerings:
            if witness.witness_id == witness_id:
                return witness
        raise PrematureLoweringError(f"undeclared lowering witness: {witness_id!r}")

    def task(self, task_id: str) -> TaskContract:
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise MethodContractError(f"unknown task: {task_id!r}")

    def baseline_for(
        self, task_id: str, mechanism: MethodMechanism, baseline_id: str
    ) -> BaselineSpec:
        for baseline in self.baselines:
            if baseline.baseline_id == baseline_id:
                if task_id not in baseline.task_scope:
                    raise MethodContractError(
                        f"baseline {baseline_id!r} is outside task {task_id!r}"
                    )
                if MethodMechanism(baseline.mechanism) != mechanism:
                    raise MethodContractError(
                        f"baseline {baseline_id!r} does not certify {mechanism.value!r}"
                    )
                return baseline
        raise MethodContractError(f"undeclared baseline: {baseline_id!r}")

    def as_dict(self) -> dict[str, object]:
        self.validate()
        return {
            "contract_id": self.contract_id,
            "problem": self.problem,
            "primitive_processes": list(self.primitive_processes),
            "tasks": [task.as_dict() for task in self.tasks],
            "native_charts": list(self.native_charts),
            "retained_fibres": list(self.retained_fibres),
            "native_function_family": self.native_function_family,
            "native_composition": self.native_composition,
            "native_operators": list(self.native_operators),
            "claim_boundary": self.claim_boundary,
            "native_grammar": self.native_grammar.as_dict(),
            "forbidden_premature_lowerings": sorted(
                MethodMechanism(mechanism).value
                for mechanism in self.forbidden_premature_lowerings
            ),
            "allowed_lowerings": [
                witness.as_dict() for witness in self.allowed_lowerings
            ],
            "baselines": [baseline.as_dict() for baseline in self.baselines],
        }


@dataclass(frozen=True)
class MethodEvent:
    event_id: int
    task_id: str
    lane: MethodLane
    mechanism: MethodMechanism
    action: str
    input_semantics: str
    output_semantics: str
    cost: CostLedger
    generator_ids: tuple[str, ...] = ()
    lowering_id: str | None = None
    baseline_id: str | None = None

    def as_dict(self) -> dict[str, object]:
        return {
            "event_id": self.event_id,
            "task_id": self.task_id,
            "lane": self.lane.value,
            "mechanism": self.mechanism.value,
            "action": self.action,
            "input_semantics": self.input_semantics,
            "output_semantics": self.output_semantics,
            "cost": self.cost.as_dict(),
            "generator_ids": list(self.generator_ids),
            "lowering_id": self.lowering_id,
            "baseline_id": self.baseline_id,
        }


@dataclass(frozen=True)
class NativeClaim:
    claim_id: int
    task_id: str
    statement: str
    evidence_event_ids: tuple[int, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "claim_id": self.claim_id,
            "task_id": self.task_id,
            "statement": self.statement,
            "evidence_event_ids": list(self.evidence_event_ids),
        }


class MethodTrace:
    """Fail-closed audit trail for one validated method contract."""

    def __init__(self, contract: MethodContract):
        self.contract = contract.validate()
        self._events: list[MethodEvent] = []
        self._claims: list[NativeClaim] = []

    @property
    def events(self) -> tuple[MethodEvent, ...]:
        return tuple(self._events)

    @property
    def claims(self) -> tuple[NativeClaim, ...]:
        return tuple(self._claims)

    def record(
        self,
        *,
        task_id: str,
        lane: MethodLane,
        mechanism: MethodMechanism,
        action: str,
        input_semantics: str,
        output_semantics: str,
        cost: CostLedger = CostLedger(),
        generator_ids: tuple[str, ...] = (),
        lowering_id: str | None = None,
        baseline_id: str | None = None,
    ) -> MethodEvent:
        if task_id not in self.contract.task_ids:
            raise MethodContractError(f"unknown task: {task_id!r}")
        lane = _enum_value(lane, MethodLane, "method lane")  # type: ignore[assignment]
        mechanism = _enum_value(  # type: ignore[assignment]
            mechanism, MethodMechanism, "mechanism"
        )
        _require_text(action, "event.action")
        _require_text(input_semantics, "event.input_semantics")
        _require_text(output_semantics, "event.output_semantics")
        cost.validate()

        native_lanes = {
            MethodLane.NATIVE_DISCOVERY,
            MethodLane.NATIVE_EVALUATION,
        }
        if lane in native_lanes:
            _require_texts(generator_ids, "event.generator_ids")
            if len(set(generator_ids)) != len(generator_ids):
                raise MethodContractError("event generator ids must be unique")
            unknown_generators = (
                set(generator_ids) - self.contract.native_grammar.generator_ids
            )
            if unknown_generators:
                raise MethodContractError(
                    f"event has unknown generators: {sorted(unknown_generators)!r}"
                )
        elif generator_ids:
            _require_texts(generator_ids, "event.generator_ids")
            unknown_generators = (
                set(generator_ids) - self.contract.native_grammar.generator_ids
            )
            if unknown_generators:
                raise MethodContractError(
                    f"event has unknown generators: {sorted(unknown_generators)!r}"
                )
        if lane in native_lanes and mechanism in CLASSICAL_MECHANISMS:
            if lowering_id is None:
                raise PrematureLoweringError(
                    f"{mechanism.value} cannot enter {lane.value} without a "
                    "task-scoped lowering witness"
                )
            witness = self.contract.lowering(lowering_id)
            if MethodMechanism(witness.mechanism) != mechanism:
                raise PrematureLoweringError(
                    f"lowering {lowering_id!r} does not certify {mechanism.value!r}"
                )
            if task_id not in witness.task_scope:
                raise PrematureLoweringError(
                    f"lowering {lowering_id!r} is outside task {task_id!r}"
                )
            if lane not in {MethodLane(value) for value in witness.allowed_lanes}:
                raise PrematureLoweringError(
                    f"lowering {lowering_id!r} is outside lane {lane.value!r}"
                )
        elif lowering_id is not None:
            raise MethodContractError(
                "a lowering witness may be attached only to a classical mechanism "
                "inside a native lane"
            )

        if lane is MethodLane.BASELINE:
            if baseline_id is None:
                raise MethodContractError(
                    "baseline events require a declared baseline_id"
                )
            self.contract.baseline_for(task_id, mechanism, baseline_id)
        elif baseline_id is not None:
            raise EvidenceLaneError(
                "baseline evidence cannot be attached outside the baseline lane"
            )

        event = MethodEvent(
            event_id=len(self._events),
            task_id=task_id,
            lane=lane,
            mechanism=mechanism,
            action=action,
            input_semantics=input_semantics,
            output_semantics=output_semantics,
            cost=cost,
            generator_ids=tuple(generator_ids),
            lowering_id=lowering_id,
            baseline_id=baseline_id,
        )
        self._events.append(event)
        return event

    def claim_native_result(
        self,
        *,
        task_id: str,
        statement: str,
        evidence_event_ids: Iterable[int],
    ) -> NativeClaim:
        if task_id not in self.contract.task_ids:
            raise MethodContractError(f"unknown task: {task_id!r}")
        _require_text(statement, "claim.statement")
        event_ids = tuple(evidence_event_ids)
        if not event_ids:
            raise EvidenceLaneError("a native claim requires evidence")
        selected: list[MethodEvent] = []
        for event_id in event_ids:
            if isinstance(event_id, bool) or not isinstance(event_id, int):
                raise EvidenceLaneError("evidence ids must be integer event ids")
            try:
                event = self._events[event_id]
            except IndexError as exc:
                raise EvidenceLaneError(f"unknown evidence event: {event_id}") from exc
            if event.event_id != event_id:
                raise EvidenceLaneError(f"unknown evidence event: {event_id}")
            if event.task_id != task_id:
                raise EvidenceLaneError(
                    f"event {event_id} belongs to task {event.task_id!r}"
                )
            if event.lane is MethodLane.BASELINE:
                raise EvidenceLaneError(
                    f"baseline event {event_id} cannot be relabelled as native evidence"
                )
            selected.append(event)
        if not any(
            event.lane
            in {MethodLane.NATIVE_DISCOVERY, MethodLane.NATIVE_EVALUATION}
            for event in selected
        ):
            raise EvidenceLaneError(
                "certificate-only evidence cannot establish a native result"
            )

        required_generators = set(self.contract.task(task_id).required_generators)
        witnessed_generators = {
            generator_id
            for event in selected
            if event.lane
            in {MethodLane.NATIVE_DISCOVERY, MethodLane.NATIVE_EVALUATION}
            for generator_id in event.generator_ids
        }
        missing_generators = required_generators - witnessed_generators
        if missing_generators:
            raise EvidenceLaneError(
                "native claim is missing required generator evidence: "
                f"{sorted(missing_generators)!r}"
            )

        claim = NativeClaim(
            claim_id=len(self._claims),
            task_id=task_id,
            statement=statement,
            evidence_event_ids=event_ids,
        )
        self._claims.append(claim)
        return claim

    def total_cost(self) -> CostLedger:
        total = CostLedger()
        for event in self._events:
            total = total + event.cost
        return total

    def audit_report(self) -> dict[str, object]:
        lane_counts = {
            lane.value: sum(event.lane is lane for event in self._events)
            for lane in MethodLane
        }
        mechanism_counts = {
            mechanism.value: sum(
                event.mechanism is mechanism for event in self._events
            )
            for mechanism in MethodMechanism
            if any(event.mechanism is mechanism for event in self._events)
        }
        return {
            "contract": self.contract.as_dict(),
            "events": [event.as_dict() for event in self._events],
            "native_claims": [claim.as_dict() for claim in self._claims],
            "summary": {
                "lane_counts": lane_counts,
                "mechanism_counts": mechanism_counts,
                "total_cost": self.total_cost().as_dict(),
                "cost_scalarization": "not-authorized",
            },
        }

    def to_json(self, *, indent: int | None = 2) -> str:
        return json.dumps(
            self.audit_report(),
            ensure_ascii=False,
            indent=indent,
            sort_keys=True,
        )


def contract_json(contract: MethodContract, *, indent: int | None = 2) -> str:
    """Return a deterministic, machine-readable validated contract."""

    return json.dumps(
        contract.as_dict(),
        ensure_ascii=False,
        indent=indent,
        sort_keys=True,
    )
