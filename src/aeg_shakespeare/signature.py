"""Finite future signatures for task-sufficient process quotients.

A process representation should not merge histories merely because their
current symbolic values happen to match. This module provides a bounded test:
two histories are indistinguishable for a declared task only when their task
observations agree under every allowed continuation up to a finite depth.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Generic, Sequence, TypeVar

from .core import ProcessWord, interpret_history

StepT = TypeVar("StepT")
StateT = TypeVar("StateT")
ObservationT = TypeVar("ObservationT")


@dataclass(frozen=True)
class ProcessJetSignature(Generic[StepT, ObservationT]):
    """Task observations under all bounded process continuations."""

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


def process_jet_signature(
    state: StateT,
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
    *,
    depth: int,
) -> ProcessJetSignature[StepT, ObservationT]:
    """Compute a finite task signature from a current state."""

    continuations = enumerate_process_words(steps, depth)
    entries = tuple(
        (
            continuation,
            observe(interpret_history(continuation, state, transition)),
        )
        for continuation in continuations
    )
    return ProcessJetSignature(depth=depth, entries=entries)


def history_process_jet_signature(
    history: ProcessWord[StepT],
    initial: StateT,
    steps: Sequence[StepT],
    transition: Callable[[StateT, StepT], StateT],
    observe: Callable[[StateT], ObservationT],
    *,
    depth: int,
) -> ProcessJetSignature[StepT, ObservationT]:
    """Compute the finite task signature after one literal process history."""

    state = interpret_history(history, initial, transition)
    return process_jet_signature(
        state,
        steps,
        transition,
        observe,
        depth=depth,
    )


def signatures_equivalent(
    left: ProcessJetSignature[StepT, ObservationT],
    right: ProcessJetSignature[StepT, ObservationT],
    *,
    equivalent: Callable[[ObservationT, ObservationT], bool] | None = None,
) -> bool:
    """Compare two finite task signatures with an optional observation metric."""

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
    """Bounded task congruence test for two literal histories.

    Equality of current task observations is not enough. The histories are
    merged only when every allowed continuation up to ``depth`` remains
    task-indistinguishable.
    """

    left_signature = history_process_jet_signature(
        left,
        initial,
        steps,
        transition,
        observe,
        depth=depth,
    )
    right_signature = history_process_jet_signature(
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
