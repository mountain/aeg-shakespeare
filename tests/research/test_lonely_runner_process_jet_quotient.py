"""Lonely Runner Phase 2: exact finite task quotient with ProcessJetSignature.

Question
--------
Can Shakespeare's existing future-signature machinery identify the exact task
quotient of a small Lonely Runner set-cover construction grammar, both rejecting
unsound current-state merges and certifying nontrivial safe merges?

Primitive data
--------------
A prime p, tuple length k, folded speed residues, the bad-time set-cover predicate,
and a canonical nondecreasing construction grammar with first speed fixed to 1.

The grammar is deliberately simpler than the upstream find_cover MRV traversal;
it is an alternative presentation, not a reimplementation of its exact history.

Shakespeare reconstruction
---------------------------
A partial tuple is a process state.  Folded speed residues are continuation tokens.
Appending a smaller residue enters an invalid sink.  The task observation is true
only for a valid length-k history whose bad-time sets cover the whole half-circle.
Because exactly k-d slots remain after a depth-d prefix, ProcessJetSignature at
depth k-d records the complete future task language of that prefix.

Calibration statement
---------------------
Passing this file certifies three statements on finite calibration worlds:

1. equal current cover + equal depth need not imply task equivalence;
2. different current covers can nevertheless have exactly equal future task
   signatures;
3. the exact semantic quotient has substantially fewer classes than literal
   canonical histories on k=4,p=13 and k=5,p=17.

Boundary
--------
The signature is computed by exhaustive continuation enumeration and is therefore
a certificate/oracle, not a scalable k=13 pruning algorithm.  Class-count reduction
is not a runtime speedup.  No morphism to the upstream MRV state space is yet
claimed.
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


def initial_state(prefix: Sequence[int], *, k: int, p: int) -> CoverState:
    values = tuple(prefix)
    if not values or values[0] != 1:
        raise ValueError("canonical calibration prefixes must start with 1")
    if any(left > right for left, right in zip(values, values[1:])):
        raise ValueError("prefix must be nondecreasing")
    if len(values) > k:
        raise ValueError("prefix longer than target tuple")
    return CoverState(values, covered_times(values, k=k, p=p))


def make_transition(*, k: int, p: int):
    def transition(state: CoverState, speed: int) -> CoverState:
        if not state.valid:
            return state
        if len(state.prefix) >= k:
            return CoverState(state.prefix, state.covered, valid=False)
        if state.prefix and speed < state.prefix[-1]:
            return CoverState(state.prefix, state.covered, valid=False)
        new_prefix = state.prefix + (speed,)
        new_cover = state.covered | bad_time_cover(speed, k=k, p=p)
        return CoverState(new_prefix, new_cover)

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


def canonical_prefixes(*, k: int, p: int, depth: int) -> tuple[tuple[int, ...], ...]:
    if not 1 <= depth < k:
        raise ValueError("depth must be in 1..k-1")
    alphabet = range(1, (p - 1) // 2 + 1)
    return tuple(
        (1,) + suffix
        for suffix in combinations_with_replacement(alphabet, depth - 1)
    )


def semantic_class_count(*, k: int, p: int, depth: int) -> int:
    signatures = {
        task_signature(prefix, k=k, p=p).observations
        for prefix in canonical_prefixes(k=k, p=p, depth=depth)
    }
    return len(signatures)


# RED TEAM: present cover equality does not imply future task equivalence.
def test_process_jet_rejects_same_cover_unsound_merge() -> None:
    k = 3
    p = 13
    left = (1, 4)
    right = (1, 6)

    assert covered_times(left, k=k, p=p) == covered_times(right, k=k, p=p)

    left_signature = task_signature(left, k=k, p=p)
    right_signature = task_signature(right, k=k, p=p)

    assert not signatures_equivalent(left_signature, right_signature)

    accepting_left = tuple(
        word.steps
        for word, accepted in left_signature.entries
        if accepted
    )
    accepting_right = tuple(
        word.steps
        for word, accepted in right_signature.entries
        if accepted
    )
    assert accepting_left == ((5,),)
    assert accepting_right == ()


# POSITIVE RESULT: different present cover states may have the same exact future.
def test_process_jet_certifies_nontrivial_safe_merge() -> None:
    k = 5
    p = 17
    left = (1, 1, 4)
    right = (1, 4, 5)

    assert covered_times(left, k=k, p=p) == frozenset({1, 2, 4, 8})
    assert covered_times(right, k=k, p=p) == frozenset({1, 2, 3, 4, 7, 8})
    assert covered_times(left, k=k, p=p) != covered_times(right, k=k, p=p)

    left_signature = task_signature(left, k=k, p=p)
    right_signature = task_signature(right, k=k, p=p)

    assert signatures_equivalent(left_signature, right_signature)

    accepting_left = tuple(
        word.steps
        for word, accepted in left_signature.entries
        if accepted
    )
    accepting_right = tuple(
        word.steps
        for word, accepted in right_signature.entries
        if accepted
    )
    assert accepting_left == accepting_right == ((6, 7),)


# MEASUREMENT: exact task classes are much fewer than literal partial histories.
def test_exact_semantic_class_counts_on_small_worlds() -> None:
    counts_4_13 = tuple(
        (
            len(canonical_prefixes(k=4, p=13, depth=depth)),
            semantic_class_count(k=4, p=13, depth=depth),
        )
        for depth in range(1, 4)
    )
    assert counts_4_13 == ((1, 1), (6, 5), (21, 5))
    assert sum(raw for raw, _classes in counts_4_13) == 28
    assert sum(classes for _raw, classes in counts_4_13) == 11

    counts_5_17 = tuple(
        (
            len(canonical_prefixes(k=5, p=17, depth=depth)),
            semantic_class_count(k=5, p=17, depth=depth),
        )
        for depth in range(1, 5)
    )
    assert counts_5_17 == ((1, 1), (8, 5), (36, 7), (120, 6))
    assert sum(raw for raw, _classes in counts_5_17) == 165
    assert sum(classes for _raw, classes in counts_5_17) == 19
