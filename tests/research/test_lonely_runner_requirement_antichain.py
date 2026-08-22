"""Lonely Runner Phase 3: requirement antichain as an exact structural quotient.

Question
--------
Can the exact ProcessJet task classes discovered in Phase 2 be approximated by a
cheap state invariant whose soundness follows directly from the set-cover process?

Primitive data
--------------
The canonical nondecreasing folded-speed grammar from Phase 2.  For each uncovered
time position, we record which still-admissible future speeds can cover it, then
retain only distinct inclusion-minimal requirement sets.

Shakespeare reconstruction
---------------------------
The structural state is

    (remaining slots, last speed, minimal future-requirement antichain).

A continuation is accepting exactly when it is canonically admissible and its
support hits every minimal requirement.  Therefore equality of this structural
state implies equality of the complete remaining ProcessJetSignature.

Calibration statement
---------------------
Passing this file computationally red-teams that sufficiency theorem on every
canonical partial prefix in k=4,p=13 and k=5,p=17, exhibits a nontrivial merge of
different current cover states, and records the compression ladder

    literal -> current-cover -> requirement-antichain -> exact task class.

Boundary
--------
The quotient is exact only for the declared canonical grammar.  It is not yet a
morphism or optimization for the upstream MRV/AvailableChoice search, and the
reported class counts are not runtime speedups.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations_with_replacement
from typing import Sequence

from aeg_shakespeare.presentation.history import (
    ProcessJetSignature,
    process_jet_signature,
    signatures_equivalent,
)


@dataclass(frozen=True)
class CoverState:
    prefix: tuple[int, ...]
    covered: frozenset[int]
    valid: bool = True


def distance_to_integer(value: Fraction) -> Fraction:
    residue = value % 1
    return min(residue, 1 - residue)


def bad_time_cover(speed: int, *, k: int, p: int) -> frozenset[int]:
    threshold = Fraction(1, k + 1)
    return frozenset(
        numerator
        for numerator in range(1, (p - 1) // 2 + 1)
        if distance_to_integer(Fraction(numerator * speed, p)) < threshold
    )


def covered_times(speeds: Sequence[int], *, k: int, p: int) -> frozenset[int]:
    covered: set[int] = set()
    for speed in speeds:
        covered.update(bad_time_cover(speed, k=k, p=p))
    return frozenset(covered)


def canonical_prefixes(*, k: int, p: int, depth: int) -> tuple[tuple[int, ...], ...]:
    alphabet = range(1, (p - 1) // 2 + 1)
    return tuple(
        (1,) + suffix
        for suffix in combinations_with_replacement(alphabet, depth - 1)
    )


def initial_state(prefix: Sequence[int], *, k: int, p: int) -> CoverState:
    values = tuple(prefix)
    return CoverState(values, covered_times(values, k=k, p=p))


def make_transition(*, k: int, p: int):
    def transition(state: CoverState, speed: int) -> CoverState:
        if not state.valid:
            return state
        if len(state.prefix) >= k or speed < state.prefix[-1]:
            return CoverState(state.prefix, state.covered, valid=False)
        return CoverState(
            state.prefix + (speed,),
            state.covered | bad_time_cover(speed, k=k, p=p),
        )

    return transition


def make_observer(*, k: int, p: int):
    universe = frozenset(range(1, (p - 1) // 2 + 1))

    def observe(state: CoverState) -> bool:
        return state.valid and len(state.prefix) == k and state.covered == universe

    return observe


def task_signature(
    prefix: Sequence[int],
    *,
    k: int,
    p: int,
) -> ProcessJetSignature[int, bool]:
    state = initial_state(prefix, k=k, p=p)
    alphabet = tuple(range(1, (p - 1) // 2 + 1))
    return process_jet_signature(
        state,
        alphabet,
        make_transition(k=k, p=p),
        make_observer(k=k, p=p),
        depth=k - len(state.prefix),
    )


def requirement_antichain(
    prefix: Sequence[int],
    *,
    k: int,
    p: int,
) -> tuple[tuple[int, ...], ...]:
    """Distinct inclusion-minimal future speed sets for uncovered times."""

    current_cover = covered_times(prefix, k=k, p=p)
    universe = frozenset(range(1, (p - 1) // 2 + 1))
    uncovered = universe - current_cover
    lower = prefix[-1]
    allowed = range(lower, (p - 1) // 2 + 1)

    requirements = {
        frozenset(
            speed
            for speed in allowed
            if time_position in bad_time_cover(speed, k=k, p=p)
        )
        for time_position in uncovered
    }

    minimal = {
        requirement
        for requirement in requirements
        if not any(
            other < requirement
            for other in requirements
        )
    }
    return tuple(
        sorted(
            (tuple(sorted(requirement)) for requirement in minimal),
            key=lambda values: (len(values), values),
        )
    )


def structural_signature(
    prefix: Sequence[int],
    *,
    k: int,
    p: int,
) -> tuple[int, int, tuple[tuple[int, ...], ...]]:
    return (
        k - len(prefix),
        prefix[-1],
        requirement_antichain(prefix, k=k, p=p),
    )


def current_cover_signature(
    prefix: Sequence[int],
    *,
    k: int,
    p: int,
) -> tuple[int, int, frozenset[int]]:
    return (
        k - len(prefix),
        prefix[-1],
        covered_times(prefix, k=k, p=p),
    )


def assert_structural_signature_is_task_safe(*, k: int, p: int) -> None:
    """Exhaustively red-team equal structural states on one finite world."""

    for depth in range(1, k):
        by_structure: dict[
            tuple[int, int, tuple[tuple[int, ...], ...]],
            list[tuple[int, ...]],
        ] = {}
        for prefix in canonical_prefixes(k=k, p=p, depth=depth):
            by_structure.setdefault(
                structural_signature(prefix, k=k, p=p),
                [],
            ).append(prefix)

        for prefixes in by_structure.values():
            reference = task_signature(prefixes[0], k=k, p=p)
            for prefix in prefixes[1:]:
                candidate = task_signature(prefix, k=k, p=p)
                assert signatures_equivalent(reference, candidate)


def representation_counts(*, k: int, p: int) -> tuple[int, int, int, int]:
    """Return literal, current-cover, structural, and exact task class totals."""

    literal_total = 0
    current_total = 0
    structural_total = 0
    semantic_total = 0

    for depth in range(1, k):
        prefixes = canonical_prefixes(k=k, p=p, depth=depth)
        literal_total += len(prefixes)
        current_total += len(
            {
                current_cover_signature(prefix, k=k, p=p)
                for prefix in prefixes
            }
        )
        structural_total += len(
            {
                structural_signature(prefix, k=k, p=p)
                for prefix in prefixes
            }
        )
        semantic_total += len(
            {
                task_signature(prefix, k=k, p=p).observations
                for prefix in prefixes
            }
        )

    return literal_total, current_total, structural_total, semantic_total


# THEOREM RED TEAM: no structural collision may split the exact task language.
def test_requirement_antichain_is_task_safe_on_calibration_worlds() -> None:
    assert_structural_signature_is_task_safe(k=4, p=13)
    assert_structural_signature_is_task_safe(k=5, p=17)


# POSITIVE MERGE: different missing times impose the same future requirement.
def test_requirement_antichain_merges_different_current_covers() -> None:
    k = 5
    p = 17
    left = (1, 3, 4, 6)
    right = (1, 4, 5, 6)

    assert covered_times(left, k=k, p=p) == frozenset({1, 2, 3, 4, 5, 6, 8})
    assert covered_times(right, k=k, p=p) == frozenset({1, 2, 3, 4, 6, 7, 8})
    assert covered_times(left, k=k, p=p) != covered_times(right, k=k, p=p)

    assert structural_signature(left, k=k, p=p) == (
        1,
        6,
        ((7,),),
    )
    assert structural_signature(left, k=k, p=p) == structural_signature(
        right,
        k=k,
        p=p,
    )

    left_task = task_signature(left, k=k, p=p)
    right_task = task_signature(right, k=k, p=p)
    assert signatures_equivalent(left_task, right_task)
    assert tuple(
        word.steps
        for word, accepted in left_task.entries
        if accepted
    ) == ((7,),)


# MEASUREMENT: structural quotient sits strictly between present state and optimum.
def test_representation_compression_ladder() -> None:
    assert representation_counts(k=4, p=13) == (28, 21, 16, 11)
    assert representation_counts(k=5, p=17) == (165, 85, 41, 19)
