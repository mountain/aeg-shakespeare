"""Lonely Runner Phase 1: reconstruct the initial modular sieve as set cover.

Question
--------
What process is the upstream I(k,p,1) search actually executing, and which pieces
of its search state are semantically necessary?

Primitive data
--------------
A prime p, a tuple length k, folded nonzero speed residues 1,...,(p-1)/2, and
the threshold 1/(k+1).

Classical / upstream lineage
----------------------------
The companion implementation for Sungkawichai--Trakulthongchai precomputes, for
each folded speed residue, a bitset of rational time positions at which that speed
fails the loneliness inequality.  Its find_cover DFS searches for k speeds whose
union covers all half-circle time positions.  The DFS state includes the covered
bitset, chosen speeds, and remaining allowed choices.

Shakespeare reconstruction
---------------------------
We reconstruct that computation independently in two presentations:

1. direct rational-grid witness semantics;
2. fixed-cardinality set-cover semantics.

They are cross-checked exhaustively on k=3,p=13.  We then red-team an apparently
smaller state presentation, `covered set + depth`, and show that it loses future
completion information.

Calibration statement
---------------------
Passing this file certifies that the initial l=1 improper predicate is exactly a
set-cover predicate on the half-circle for the calibration world; it reproduces
56 folded candidates -> 14 improper tuples -> 3 unit-orbit canonical classes;
and it shows that the available-choice frontier cannot in general be discarded.

Boundary
--------
This is a tiny exact reconstruction, not a competitive implementation of
find_cover and not a proof of any new Lonely Runner case.

References
----------
[Sungkawichai-Trakulthongchai-2026] T. Sungkawichai, T. Trakulthongchai,
Eleven, twelve, and thirteen lonely runners, arXiv:2604.23906 (2026), Sections 5
and 7; companion code https://github.com/vzsky/13-lonely-runners.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations_with_replacement
from math import gcd
from typing import Iterable, Sequence


def distance_to_integer(value: Fraction) -> Fraction:
    residue = value % 1
    return min(residue, 1 - residue)


def direct_grid_improper(speeds: Sequence[int], p: int) -> bool:
    """No witness exists on (1/p) Z / Z."""

    k = len(speeds)
    threshold = Fraction(1, k + 1)
    for numerator in range(p):
        time = Fraction(numerator, p)
        if all(
            distance_to_integer(speed * time) >= threshold
            for speed in speeds
        ):
            return False
    return True


def bad_time_cover(speed: int, *, k: int, p: int) -> frozenset[int]:
    """Half-circle time positions made bad by one folded speed residue."""

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


def set_cover_improper(speeds: Sequence[int], p: int) -> bool:
    """The tuple is improper iff its bad-time subsets cover the half-circle."""

    k = len(speeds)
    universe = frozenset(range(1, (p - 1) // 2 + 1))
    return covered_times(speeds, k=k, p=p) == universe


def canonical_mod_p(speeds: Sequence[int], p: int) -> tuple[int, ...]:
    """Canonical representative under global units, signs, and permutation."""

    candidates = []
    for unit in range(1, p):
        if gcd(unit, p) != 1:
            continue
        folded = []
        for speed in speeds:
            residue = unit * speed % p
            folded.append(min(residue, (-residue) % p))
        candidates.append(tuple(sorted(folded)))
    return min(candidates)


def nondecreasing_completions(
    prefix: Sequence[int],
    *,
    k: int,
    p: int,
) -> Iterable[tuple[int, ...]]:
    """Upstream-style ordered continuations, allowing repeated residues."""

    slots = k - len(prefix)
    if slots < 0:
        return ()
    lower = prefix[-1] if prefix else 1
    upper = (p - 1) // 2
    return combinations_with_replacement(range(lower, upper + 1), slots)


def can_complete_cover(prefix: Sequence[int], *, k: int, p: int) -> bool:
    """Exact future task semantics for one ordered partial history."""

    universe = frozenset(range(1, (p - 1) // 2 + 1))
    current = covered_times(prefix, k=k, p=p)
    for suffix in nondecreasing_completions(prefix, k=k, p=p):
        future = set(current)
        for speed in suffix:
            future.update(bad_time_cover(speed, k=k, p=p))
        if frozenset(future) == universe:
            return True
    return False


# CROSS-PRESENTATION: rational-grid semantics == set-cover semantics.
def test_small_initial_sieve_cross_calibration() -> None:
    k = 3
    p = 13
    folded_speeds = range(1, (p - 1) // 2 + 1)
    candidates = tuple(combinations_with_replacement(folded_speeds, k))

    assert len(candidates) == 56

    for speeds in candidates:
        assert set_cover_improper(speeds, p) == direct_grid_improper(speeds, p)

    improper = tuple(speeds for speeds in candidates if set_cover_improper(speeds, p))
    assert len(improper) == 14

    canonical = {canonical_mod_p(speeds, p) for speeds in improper}
    assert canonical == {
        (1, 2, 3),
        (1, 2, 4),
        (1, 3, 4),
    }


# RED TEAM: covered-bitset + depth is not enough under ordered continuation.
def test_same_cover_and_depth_can_have_different_completion_semantics() -> None:
    k = 3
    p = 13
    left = (1, 4)
    right = (1, 6)

    left_cover = covered_times(left, k=k, p=p)
    right_cover = covered_times(right, k=k, p=p)

    assert len(left) == len(right) == 2
    assert left_cover == right_cover == frozenset({1, 2, 3, 4, 6})

    # The histories differ only in their remaining admissible-choice frontier.
    # From (1,4), speed 5 is still available and completes the cover.
    assert set_cover_improper((1, 4, 5), p)
    assert can_complete_cover(left, k=k, p=p)

    # From (1,6), ordered enumeration permits only another 6; no completion exists.
    assert not set_cover_improper((1, 6, 6), p)
    assert not can_complete_cover(right, k=k, p=p)
