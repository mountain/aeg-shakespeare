"""Exact rewriting for ordered process histories.

This module is deliberately independent of SymPy and derivation-style process
systems. It provides a first executable layer for noncommutative finite process
presentations: literal histories are preserved, oriented process relations are
applied explicitly, and every normalization carries a rewrite trace.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Literal, Sequence, TypeVar

from .process.history import ProcessWord

StepT = TypeVar("StepT")
RewriteReason = Literal["normal_form", "cycle", "max_steps"]


@dataclass(frozen=True)
class WordRewriteRule(Generic[StepT]):
    """An oriented exact relation between two finite process words.

    The rule rewrites a contiguous occurrence of ``lhs`` to ``rhs``. An empty
    left-hand side is forbidden because it would permit insertion at every
    history position and destroy the bounded-normalization semantics.
    """

    lhs: ProcessWord[StepT]
    rhs: ProcessWord[StepT]
    name: str = ""

    def __post_init__(self) -> None:
        if not self.lhs.steps:
            raise ValueError("rewrite-rule lhs must be non-empty")


@dataclass(frozen=True)
class RewriteStep(Generic[StepT]):
    """One certified history rewrite."""

    rule: WordRewriteRule[StepT]
    position: int
    before: ProcessWord[StepT]
    after: ProcessWord[StepT]


@dataclass(frozen=True)
class RewriteResult(Generic[StepT]):
    """Result and certificate of a bounded normalization attempt."""

    original: ProcessWord[StepT]
    normal_form: ProcessWord[StepT]
    trace: tuple[RewriteStep[StepT], ...]
    terminated: bool
    reason: RewriteReason

    @property
    def rewrite_steps(self) -> int:
        return len(self.trace)

    @property
    def depth_delta(self) -> int:
        """Final history depth minus original history depth."""

        return self.normal_form.depth - self.original.depth


def rewrite_once(
    history: ProcessWord[StepT],
    rules: Sequence[WordRewriteRule[StepT]],
) -> RewriteStep[StepT] | None:
    """Apply one deterministic leftmost rewrite.

    Positions are searched from left to right. If several rules match at the
    same position, their order in ``rules`` is the tie breaker.
    """

    steps = history.steps
    for position in range(len(steps)):
        for rule in rules:
            width = len(rule.lhs.steps)
            if steps[position : position + width] != rule.lhs.steps:
                continue
            after = ProcessWord(
                steps[:position] + rule.rhs.steps + steps[position + width :]
            )
            return RewriteStep(
                rule=rule,
                position=position,
                before=history,
                after=after,
            )
    return None


def normalize_word(
    history: ProcessWord[StepT],
    rules: Sequence[WordRewriteRule[StepT]],
    *,
    max_steps: int = 1_000,
    detect_cycles: bool = True,
) -> RewriteResult[StepT]:
    """Normalize a process word under explicit oriented relations.

    The function never assumes that the supplied rewrite system terminates or
    is confluent. It returns ``terminated=False`` with an explicit reason when a
    cycle or step bound is encountered. Literal input history and the complete
    sequence of process-relation applications remain available in ``trace``.
    """

    if max_steps < 0:
        raise ValueError("max_steps must be non-negative")

    current = history
    trace: list[RewriteStep[StepT]] = []
    seen: list[ProcessWord[StepT]] = [history]

    for _ in range(max_steps):
        step = rewrite_once(current, rules)
        if step is None:
            return RewriteResult(
                original=history,
                normal_form=current,
                trace=tuple(trace),
                terminated=True,
                reason="normal_form",
            )

        current = step.after
        trace.append(step)

        if detect_cycles and any(current == previous for previous in seen):
            return RewriteResult(
                original=history,
                normal_form=current,
                trace=tuple(trace),
                terminated=False,
                reason="cycle",
            )
        seen.append(current)

    if rewrite_once(current, rules) is None:
        return RewriteResult(
            original=history,
            normal_form=current,
            trace=tuple(trace),
            terminated=True,
            reason="normal_form",
        )
    return RewriteResult(
        original=history,
        normal_form=current,
        trace=tuple(trace),
        terminated=False,
        reason="max_steps",
    )
