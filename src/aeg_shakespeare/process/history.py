"""Literal ordered process histories and caller-supplied semantics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, TypeVar

StepT = TypeVar("StepT")
StateT = TypeVar("StateT")


@dataclass(frozen=True)
class ProcessWord(Generic[StepT]):
    """An ordered finite process history.

    ``ProcessWord`` deliberately stores steps without interpreting them. The
    same history can therefore be given different semantics by different
    presentations or observers.
    """

    steps: tuple[StepT, ...] = ()

    def __iter__(self) -> Iterator[StepT]:
        return iter(self.steps)

    def __len__(self) -> int:
        return len(self.steps)

    @property
    def depth(self) -> int:
        return len(self.steps)

    def then(self, step: StepT) -> "ProcessWord[StepT]":
        return ProcessWord(self.steps + (step,))

    def compose(self, other: "ProcessWord[StepT]") -> "ProcessWord[StepT]":
        return ProcessWord(self.steps + other.steps)


def interpret_history(
    history: ProcessWord[StepT],
    initial: StateT,
    transition,
) -> StateT:
    """Interpret an ordered history under a caller-supplied transition rule."""

    state = initial
    for step in history:
        state = transition(state, step)
    return state


__all__ = ["ProcessWord", "interpret_history"]
