"""Bounded continuation signatures for task-relative distinguishability.

A process presentation should not merge histories merely because their current
symbolic values happen to match. This module provides a bounded calibration of
the distinguishability program in ``docs/42`` and ``docs/43``: two histories
remain equivalent only when their task observations agree under every allowed
continuation up to a declared finite depth.

The historical ``ProcessJetSignature`` name predates the Process Geometry
foundation. ``jet`` is now reserved for genuinely local/differential structure;
``TaskContinuationSignature`` is the canonical name for this discrete object.
Compatibility aliases are retained during the 0.0.x transition.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Generic, Sequence, TypeVar

from .process.history import ProcessWord, interpret_history

StepT = TypeVar("StepT")
StateT = TypeVar("StateT")
ObservationT = TypeVar("ObservationT")


@dataclass(frozen=True)
class TaskContinuationSignature(Generic[StepT, ObservationT]):
    """Task observations under every bounded admissible continuation."""

    depth: int
    entries: tuple[tuple[ProcessWord[StepT], ObservationT], ...]

    @property
    def observations(self) -> tuple[ObservationT, ...]:
        return tuple(observation for _word, observation in self.entries)


def enumerate_process_words(
    steps: Sequence[StepT],
    max_depth: int,
) -> tuple[ProcessWord[StepT], ...]:
    """Enumerate the free ordered continuation tree through ``max_depth``.

    The empty continuation is included first. No commutativity or relation
    quotient is assumed; callers may normalize words separately when that is
    part of the chosen presentation.
    """

    if max_depth < 0:
        raise ValueError("max_depth must be non-negative")
    alphabet = tuple(steps)
    words: list[ProcessWord[StepT]] = [ProcessWord()]
    for depth in range(1, max_depth + 1):
        words.extend(ProcessWord(tuple(items)) for items in product(alphabet, repeat=depth))
    return tuple(words)


def task_continuation_signature(
    state: StateT,
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
    *,
    depth: int,
) -> TaskContinuationSignature[StepT, ObservationT]:
    """Compute a bounded task-continuation signature from a current state."""

    continuations = enumerate_process_words(steps, depth)
    entries = tuple(
        (
            continuation,
            observe(interpret_history(continuation, state, transition)),
        )
        for continuation in continuations
    )
    return TaskContinuationSignature(depth=depth, entries=entries)


def history_task_continuation_signature(
    history: ProcessWord[StepT],
    initial: StateT,
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
    *,
    depth: int,
) -> TaskContinuationSignature[StepT, ObservationT]:
    """Compute the bounded task signature after one literal process history."""

    state = interpret_history(history, initial, transition)
    return task_continuation_signature(
        state,
        steps,
        transition,
        observe,
        depth=depth,
    )


def signatures_equivalent(
    left: TaskContinuationSignature[StepT, ObservationT],
    right: TaskContinuationSignature[StepT, ObservationT],
    *,
    equivalent: Callable[[ObservationT, ObservationT], bool] | None = None,
) -> bool:
    """Compare two bounded task signatures with an optional observation comparator."""

    if left.depth != right.depth or len(left.entries) != len(right.entries):
        return False
    compare = equivalent or (lambda a, b: bool(a == b))
    for (left_word, left_value), (right_word, right_value) in zip(
        left.entries, right.entries
    ):
        if left_word != right_word:
            return False
        if not compare(left_value, right_value):
            return False
    return True


def histories_task_equivalent(
    left: ProcessWord[StepT],
    right: ProcessWord[StepT],
    initial: StateT,
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
    *,
    depth: int,
    equivalent: Callable[[ObservationT, ObservationT], bool] | None = None,
) -> bool:
    """Bounded task-congruence test for two literal histories.

    Equality of current task observations is not enough. The histories are
    merged only when every allowed continuation up to ``depth`` remains
    task-indistinguishable. This is a finite approximation to the exact
    continuation-stable equivalence emphasized by Myhill--Nerode.
    """

    left_signature = history_task_continuation_signature(
        left,
        initial,
        steps,
        transition,
        observe,
        depth=depth,
    )
    right_signature = history_task_continuation_signature(
        right,
        initial,
        steps,
        transition,
        observe,
        depth=depth,
    )
    return signatures_equivalent(
        left_signature,
        right_signature,
        equivalent=equivalent,
    )


# Historical 0.0.x terminology. These aliases intentionally preserve behavior
# while new code uses vocabulary aligned with the Process Geometry foundation.
ProcessJetSignature = TaskContinuationSignature
process_jet_signature = task_continuation_signature
history_process_jet_signature = history_task_continuation_signature
