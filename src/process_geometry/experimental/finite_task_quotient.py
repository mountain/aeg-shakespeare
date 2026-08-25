"""Exact finite deterministic task quotients.

Theory position
---------------
This module is the first executable slice that intentionally uses the strong
``TaskQuotient`` vocabulary from ``docs/THEORY_MAP.md``.  For a finite,
deterministic process with a finite step alphabet and a hashable task
observation, it computes the coarsest continuation-stable equivalence

    x ~ y  iff  Q(delta(x, w)) == Q(delta(y, w)) for every finite word w.

This is the Moore-machine / Myhill--Nerode finite calibration.  It is exact in
this declared class: unlike ``TaskContinuationSignature``, no continuation-depth
cutoff is used.

Boundary
--------
The implementation is Experimental. It does not claim to cover infinite,
nondeterministic, probabilistic, continuous, approximate, or resource-bounded
processes, and it does not introduce topology.  Its purpose is to make H1/V1 of
the Theory Map executable before any broader quotient abstraction is designed.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from types import MappingProxyType
from typing import Callable, Generic, Hashable, Mapping, Sequence, TypeVar

StateT = TypeVar("StateT", bound=Hashable)
StepT = TypeVar("StepT", bound=Hashable)
ObservationT = TypeVar("ObservationT", bound=Hashable)


@dataclass(frozen=True)
class DistinguishingContinuation(Generic[StepT]):
    """Exact future witness separating two quotient classes."""

    left_class: int
    right_class: int
    continuation: tuple[StepT, ...]


@dataclass(frozen=True)
class FiniteTaskQuotient(Generic[StateT, StepT, ObservationT]):
    """Coarsest finite continuation-stable quotient preserving a task output.

    ``classes`` are equivalence classes of original states. ``class_transitions``
    stores the induced deterministic transition table, indexed by class and then
    by the order of ``steps``. ``distinguishing_witnesses`` contains one exact
    continuation for every unordered pair of distinct classes, certifying that
    no two quotient states can be merged while preserving all future task
    observations.
    """

    states: tuple[StateT, ...]
    steps: tuple[StepT, ...]
    classes: tuple[tuple[StateT, ...], ...]
    state_to_class: Mapping[StateT, int]
    class_observations: tuple[ObservationT, ...]
    class_transitions: tuple[tuple[int, ...], ...]
    refinement_rounds: int
    distinguishing_witnesses: tuple[DistinguishingContinuation[StepT], ...]

    def __post_init__(self) -> None:
        # A frozen certificate must not retain a caller-mutable dictionary.
        object.__setattr__(
            self,
            "state_to_class",
            MappingProxyType(dict(self.state_to_class)),
        )

    @property
    def class_count(self) -> int:
        return len(self.classes)

    def class_of(self, state: StateT) -> int:
        try:
            return int(self.state_to_class[state])
        except KeyError as exc:
            raise KeyError(f"state is outside the quotient carrier: {state!r}") from exc

    def observation_of_class(self, class_index: int) -> ObservationT:
        """Return the task observation attached to one quotient class."""

        if class_index < 0 or class_index >= self.class_count:
            raise IndexError("quotient class index out of range")
        return self.class_observations[class_index]

    def transition_class(self, class_index: int, step: StepT) -> int:
        if class_index < 0 or class_index >= self.class_count:
            raise IndexError("quotient class index out of range")
        try:
            step_index = self.steps.index(step)
        except ValueError as exc:
            raise KeyError(f"unknown process step: {step!r}") from exc
        return self.class_transitions[class_index][step_index]

    def run_class(
        self,
        class_index: int,
        continuation: Sequence[StepT],
    ) -> int:
        """Run a finite continuation on the induced quotient process."""

        current = class_index
        # Validate even when ``continuation`` is empty.
        self.observation_of_class(current)
        for step in continuation:
            current = self.transition_class(current, step)
        return current

    def observe_after(
        self,
        class_index: int,
        continuation: Sequence[StepT],
    ) -> ObservationT:
        """Observe the quotient task after a finite continuation."""

        return self.observation_of_class(
            self.run_class(class_index, continuation)
        )

    def witness_between(
        self,
        left_class: int,
        right_class: int,
    ) -> tuple[StepT, ...]:
        """Return an exact continuation distinguishing two different classes."""

        if left_class == right_class:
            raise ValueError("one quotient class is not distinguishable from itself")
        left, right = sorted((left_class, right_class))
        for witness in self.distinguishing_witnesses:
            if witness.left_class == left and witness.right_class == right:
                return witness.continuation
        raise KeyError(f"no distinguishing witness for classes {left} and {right}")


def _require_distinct(items: tuple[Hashable, ...], *, name: str) -> None:
    try:
        unique = set(items)
    except TypeError as exc:
        raise TypeError(f"{name} must be hashable") from exc
    if len(unique) != len(items):
        raise ValueError(f"{name} must be distinct")


def _find_distinguishing_word(
    left: int,
    right: int,
    *,
    steps: tuple[StepT, ...],
    observations: tuple[ObservationT, ...],
    transitions: tuple[tuple[int, ...], ...],
) -> tuple[StepT, ...]:
    """Breadth-first exact witness on the minimized quotient machine."""

    queue: deque[tuple[int, int, tuple[StepT, ...]]] = deque(
        [(left, right, ())]
    )
    seen: set[tuple[int, int]] = {(left, right)}

    while queue:
        current_left, current_right, word = queue.popleft()
        if observations[current_left] != observations[current_right]:
            return word

        for step_index, step in enumerate(steps):
            next_left = transitions[current_left][step_index]
            next_right = transitions[current_right][step_index]
            pair = (next_left, next_right)
            if pair in seen:
                continue
            seen.add(pair)
            queue.append((next_left, next_right, word + (step,)))

    raise AssertionError(
        "distinct stable quotient classes have no distinguishing continuation"
    )


def minimize_finite_task_process(
    states: Sequence[StateT],
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
) -> FiniteTaskQuotient[StateT, StepT, ObservationT]:
    """Compute the exact finite task quotient by stable partition refinement.

    The initial partition groups states by current task observation. Repeated
    refinement then separates states whenever some one-step continuation enters
    different current partition blocks. At the fixed point, equality of blocks
    is equivalent to equality of task observations under every finite
    continuation.

    The returned quotient includes explicit distinguishing continuations for all
    pairs of different classes. Those witnesses certify minimality: each pair of
    quotient states has a future experiment that would be destroyed by merging
    them.
    """

    state_tuple = tuple(states)
    step_tuple = tuple(steps)
    if not state_tuple:
        raise ValueError("finite task quotient requires at least one state")
    _require_distinct(state_tuple, name="states")
    _require_distinct(step_tuple, name="steps")

    state_set = set(state_tuple)

    observations: dict[StateT, ObservationT] = {}
    transition_table: dict[tuple[StateT, StepT], StateT] = {}

    for state in state_tuple:
        observation = observe(state)
        try:
            hash(observation)
        except TypeError as exc:
            raise TypeError("task observations must be hashable") from exc
        observations[state] = observation

        for step in step_tuple:
            target = transition(state, step)
            if target not in state_set:
                raise ValueError(
                    "finite process transition leaves declared state carrier: "
                    f"delta({state!r}, {step!r}) = {target!r}"
                )
            transition_table[(state, step)] = target

    # Initial task partition. IDs are deterministic from caller state order and
    # require no ordering relation on the generic observation type.
    observation_blocks: dict[ObservationT, int] = {}
    state_class: dict[StateT, int] = {}
    for state in state_tuple:
        observation = observations[state]
        block = observation_blocks.setdefault(observation, len(observation_blocks))
        state_class[state] = block

    refinement_rounds = 0
    while True:
        signature_blocks: dict[tuple[ObservationT, tuple[int, ...]], int] = {}
        refined: dict[StateT, int] = {}

        for state in state_tuple:
            signature = (
                observations[state],
                tuple(
                    state_class[transition_table[(state, step)]]
                    for step in step_tuple
                ),
            )
            block = signature_blocks.setdefault(signature, len(signature_blocks))
            refined[state] = block

        if all(refined[state] == state_class[state] for state in state_tuple):
            break
        state_class = refined
        refinement_rounds += 1

    class_count = max(state_class.values(), default=-1) + 1
    class_lists: list[list[StateT]] = [[] for _ in range(class_count)]
    for state in state_tuple:
        class_lists[state_class[state]].append(state)
    classes = tuple(tuple(items) for items in class_lists)

    class_observations: list[ObservationT] = []
    class_transitions: list[tuple[int, ...]] = []

    for class_index, members in enumerate(classes):
        if not members:
            raise AssertionError("partition refinement created an empty class")
        representative = members[0]
        observation = observations[representative]

        if any(observations[state] != observation for state in members):
            raise AssertionError("task observation is not well-defined on quotient class")

        transition_row = tuple(
            state_class[transition_table[(representative, step)]]
            for step in step_tuple
        )
        for state in members[1:]:
            candidate_row = tuple(
                state_class[transition_table[(state, step)]]
                for step in step_tuple
            )
            if candidate_row != transition_row:
                raise AssertionError(
                    "process continuation is not well-defined on quotient class"
                )

        class_observations.append(observation)
        class_transitions.append(transition_row)

    observation_tuple = tuple(class_observations)
    transition_tuple = tuple(class_transitions)

    witnesses: list[DistinguishingContinuation[StepT]] = []
    for left in range(class_count):
        for right in range(left + 1, class_count):
            continuation = _find_distinguishing_word(
                left,
                right,
                steps=step_tuple,
                observations=observation_tuple,
                transitions=transition_tuple,
            )
            witnesses.append(
                DistinguishingContinuation(
                    left_class=left,
                    right_class=right,
                    continuation=continuation,
                )
            )

    return FiniteTaskQuotient(
        states=state_tuple,
        steps=step_tuple,
        classes=classes,
        state_to_class=dict(state_class),
        class_observations=observation_tuple,
        class_transitions=transition_tuple,
        refinement_rounds=refinement_rounds,
        distinguishing_witnesses=tuple(witnesses),
    )


__all__ = [
    "DistinguishingContinuation",
    "FiniteTaskQuotient",
    "minimize_finite_task_process",
]
