"""Lonely Runner Phase 4: test a requirement certificate on upstream MRV states.

Question
--------
Does the future-requirement representation discovered in the canonical Shakespeare
calibration contain pruning information that is absent from the actual upstream
find_cover early_return_bound?

Primitive / upstream data
-------------------------
This file transliterates the relevant small finite part of
vzsky/13-lonely-runners/src/find_cover.h: the exact cover-bit ordering, available
choice elimination, MRV next-position choice, optimistic early-return bound, DFS
branch order, and serialized equivalent of the parallel top-level initialization.

Shakespeare reconstruction
---------------------------
For every uncovered time position, form the set of currently available speeds that
can cover it.  Delete duplicate requirements and strict supersets.  If more than r
of the remaining minimal requirement sets are pairwise disjoint, then r remaining
speed slots cannot possibly hit all requirements.

Calibration statement
---------------------
Passing this file certifies a reachable k=5,p=29 MRV state that survives the
upstream optimistic bound but has a three-way disjoint-requirement obstruction with
only two slots left.  It also verifies, on complete small searches, that adding the
certificate preserves the exact canonical solution set while reducing DFS calls:

    k=5,p=29: 113 -> 110, 1 new prune, 7 solution classes unchanged
    k=7,p=37: 1752 -> 1743, 3 new prunes, 177 solution classes unchanged

Boundary
--------
This is a semantic mirror for small worlds, not a Python replacement for the C++
solver and not a wall-clock benchmark.  The improvement is deliberately reported
as a strictness result; its magnitude is still small.

Reference
---------
[Sungkawichai-Trakulthongchai-code-2026]
https://github.com/vzsky/13-lonely-runners/blob/main/src/find_cover.h
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import combinations
from typing import Iterable, Sequence


def cover_mask(speed: int, *, k: int, p: int) -> int:
    """Literal upstream bit layout: bit position p//2 - t."""

    half = p // 2
    result = 0
    for time_numerator in range(1, half + 1):
        position = half - time_numerator
        remainder = (time_numerator * speed) % p
        is_bad = (
            remainder * (k + 1) < p
            or (p - remainder) * (k + 1) < p
        )
        if is_bad:
            result |= 1 << position
    return result


def cover_masks(*, k: int, p: int) -> tuple[int, ...]:
    return tuple(
        cover_mask(speed, k=k, p=p)
        for speed in range(1, p // 2 + 1)
    )


def remaining_counts(
    eliminated: int,
    *,
    k: int,
    p: int,
) -> tuple[int, ...]:
    masks = cover_masks(k=k, p=p)
    half = p // 2
    counts = [0] * half
    for choice, mask in enumerate(masks):
        if eliminated & (1 << choice):
            continue
        for position in range(half):
            if mask & (1 << position):
                counts[position] += 1
    return tuple(counts)


def next_to_cover(
    covered: int,
    eliminated: int,
    *,
    k: int,
    p: int,
) -> int:
    """Match upstream tie-breaking: first bit with minimum remaining choices."""

    counts = remaining_counts(eliminated, k=k, p=p)
    best_position = -1
    best_count: int | None = None
    for position, count in enumerate(counts):
        if covered & (1 << position):
            continue
        if best_count is None or count < best_count:
            best_position = position
            best_count = count
    return best_position


@dataclass(frozen=True)
class UpstreamBound:
    prune: bool
    reason: str | None
    uncovered_count: int | None = None
    best_covering_next: int | None = None
    best_covering: int | None = None
    slots: int | None = None


def upstream_early_return_bound(
    covered: int,
    eliminated: int,
    *,
    depth: int,
    k: int,
    p: int,
) -> UpstreamBound:
    """Literal semantic transliteration of Dfs::early_return_bound()."""

    half = p // 2
    masks = cover_masks(k=k, p=p)
    chosen_position = next_to_cover(covered, eliminated, k=k, p=p)
    counts = remaining_counts(eliminated, k=k, p=p)

    if chosen_position != -1 and counts[chosen_position] == 0:
        return UpstreamBound(True, "uncoverable")

    if depth < k - 4 or chosen_position == -1:
        return UpstreamBound(False, None)

    full = (1 << half) - 1
    other_uncovered = full ^ covered
    other_uncovered &= ~(1 << chosen_position)
    total_to_cover = half - covered.bit_count()

    best_covering_next = 0
    best_covering = 0
    for choice, mask in enumerate(masks):
        if eliminated & (1 << choice):
            continue
        count = (other_uncovered & mask).bit_count()
        best_covering = max(best_covering, count)
        if mask & (1 << chosen_position):
            best_covering_next = max(best_covering_next, count + 1)

    slots = k - depth
    prune = total_to_cover > (
        best_covering_next + best_covering * (slots - 1)
    )
    return UpstreamBound(
        prune,
        "optimistic" if prune else None,
        uncovered_count=total_to_cover,
        best_covering_next=best_covering_next,
        best_covering=best_covering,
        slots=slots,
    )


def requirement_antichain(
    covered: int,
    eliminated: int,
    *,
    k: int,
    p: int,
) -> tuple[frozenset[int], ...]:
    """Minimal currently available speed sets for every uncovered time."""

    half = p // 2
    masks = cover_masks(k=k, p=p)
    requirements: set[frozenset[int]] = set()

    for position in range(half):
        if covered & (1 << position):
            continue
        requirement = frozenset(
            choice + 1
            for choice, mask in enumerate(masks)
            if not (eliminated & (1 << choice))
            and (mask & (1 << position))
        )
        requirements.add(requirement)

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
            minimal,
            key=lambda requirement: (len(requirement), tuple(sorted(requirement))),
        )
    )


def find_pairwise_disjoint_requirements(
    requirements: Sequence[frozenset[int]],
    *,
    target: int,
) -> tuple[frozenset[int], ...] | None:
    """Return any target-size disjoint family; existence is a safe lower bound."""

    for candidate in combinations(requirements, target):
        used: set[int] = set()
        valid = True
        for requirement in candidate:
            if not requirement or used.intersection(requirement):
                valid = False
                break
            used.update(requirement)
        if valid:
            return candidate
    return None


def canonical_mod_p(speeds: Sequence[int], p: int) -> tuple[int, ...]:
    """Canonicalize under global units, sign folding, and permutation."""

    candidates = []
    for unit in range(1, p):
        folded = []
        for speed in speeds:
            residue = (unit * speed) % p
            folded.append(min(residue, p - residue))
        candidates.append(tuple(sorted(folded)))
    return min(candidates)


@dataclass(frozen=True)
class ExtraPruneState:
    chosen: tuple[int, ...]
    eliminated: frozenset[int]
    remaining_slots: int
    requirements: tuple[frozenset[int], ...]


@dataclass(frozen=True)
class SearchResult:
    solutions: frozenset[tuple[int, ...]]
    counters: tuple[tuple[str, int], ...]
    extra_prunes: tuple[ExtraPruneState, ...]

    def count(self, key: str) -> int:
        return dict(self.counters).get(key, 0)


def run_find_cover(
    *,
    k: int,
    p: int,
    use_disjoint_requirement_prune: bool,
) -> SearchResult:
    """Serialized exact small-world mirror of upstream find_all_covers_parallel."""

    half = p // 2
    full = (1 << half) - 1
    masks = cover_masks(k=k, p=p)
    counters: Counter[str] = Counter()
    solutions: set[tuple[int, ...]] = set()
    extra_prunes: list[ExtraPruneState] = []

    def run(
        covered: int,
        eliminated: int,
        chosen: tuple[int, ...],
    ) -> None:
        counters["nodes"] += 1
        depth = len(chosen)

        if depth == k:
            if covered == full:
                solutions.add(canonical_mod_p(chosen, p))
            return

        upstream = upstream_early_return_bound(
            covered,
            eliminated,
            depth=depth,
            k=k,
            p=p,
        )
        if upstream.prune:
            counters["upstream_prune"] += 1
            counters[f"upstream_{upstream.reason}"] += 1
            return

        if use_disjoint_requirement_prune:
            requirements = requirement_antichain(
                covered,
                eliminated,
                k=k,
                p=p,
            )
            slots = k - depth
            certificate = find_pairwise_disjoint_requirements(
                requirements,
                target=slots + 1,
            )
            if certificate is not None:
                counters["disjoint_prune"] += 1
                extra_prunes.append(
                    ExtraPruneState(
                        chosen=chosen,
                        eliminated=frozenset(
                            choice + 1
                            for choice in range(half)
                            if eliminated & (1 << choice)
                        ),
                        remaining_slots=slots,
                        requirements=requirements,
                    )
                )
                return

        selected_position = next_to_cover(
            covered,
            eliminated,
            k=k,
            p=p,
        )

        # Integer masks are copied into recursive calls.  Updating `eliminated`
        # after a child therefore matches AvailableChoice::eliminate(i) for the
        # subsequent siblings while automatically restoring on function return.
        for choice, mask in enumerate(masks):
            if eliminated & (1 << choice):
                continue
            if (
                selected_position == -1
                or mask & (1 << selected_position)
            ):
                run(
                    covered | mask,
                    eliminated,
                    chosen + (choice + 1,),
                )
                eliminated |= 1 << choice

    # Match find_all_covers_parallel(): fix first speed to 1, find all admissible
    # second-coordinate workers, and give worker idx the choice state in which
    # only earlier second-coordinate candidates have been eliminated.
    first_covered = masks[0]
    base_eliminated = 0
    first_selected = next_to_cover(
        first_covered,
        base_eliminated,
        k=k,
        p=p,
    )
    second_candidates = tuple(
        choice
        for choice, mask in enumerate(masks)
        if first_selected == -1 or mask & (1 << first_selected)
    )

    eliminated = base_eliminated
    for choice in second_candidates:
        run(
            first_covered | masks[choice],
            eliminated,
            (1, choice + 1),
        )
        eliminated |= 1 << choice

    return SearchResult(
        solutions=frozenset(solutions),
        counters=tuple(sorted(counters.items())),
        extra_prunes=tuple(extra_prunes),
    )


def time_numerators_from_uncovered(covered: int, p: int) -> frozenset[int]:
    """Decode upstream bit positions back to t numerators."""

    half = p // 2
    return frozenset(
        half - position
        for position in range(half)
        if not (covered & (1 << position))
    )


# STRICTNESS: a reachable state survives upstream but has a 3>2 obstruction.
def test_disjoint_requirement_certificate_strictly_strengthens_upstream_bound() -> None:
    k = 5
    p = 29

    enhanced = run_find_cover(
        k=k,
        p=p,
        use_disjoint_requirement_prune=True,
    )
    assert enhanced.count("disjoint_prune") == 1

    state = enhanced.extra_prunes[0]
    assert state.chosen == (1, 2, 7)
    assert state.eliminated == frozenset({5})
    assert state.remaining_slots == 2

    required_triple = (
        frozenset({6, 11, 12}),
        frozenset({3, 8, 13}),
        frozenset({9, 10, 14}),
    )
    for requirement in required_triple:
        assert requirement in state.requirements
    assert find_pairwise_disjoint_requirements(
        state.requirements,
        target=3,
    ) is not None

    # Reconstruct the same reachable state to inspect the upstream bound terms.
    # The enhanced search identifies it uniquely, so replay the literal chosen
    # history and elimination state through set union.
    masks = cover_masks(k=k, p=p)
    covered = masks[0] | masks[1] | masks[6]
    eliminated_mask = 1 << (5 - 1)

    assert time_numerators_from_uncovered(covered, p) == frozenset(
        {5, 6, 7, 9, 10, 11}
    )

    upstream = upstream_early_return_bound(
        covered,
        eliminated_mask,
        depth=3,
        k=k,
        p=p,
    )
    assert not upstream.prune
    assert (
        upstream.uncovered_count,
        upstream.best_covering_next,
        upstream.best_covering,
        upstream.slots,
    ) == (6, 3, 3, 2)


# WHOLE SEARCH: stronger certificate must preserve exact canonical outputs.
def test_disjoint_requirement_prune_preserves_solution_sets() -> None:
    baseline_5_29 = run_find_cover(
        k=5,
        p=29,
        use_disjoint_requirement_prune=False,
    )
    enhanced_5_29 = run_find_cover(
        k=5,
        p=29,
        use_disjoint_requirement_prune=True,
    )

    assert baseline_5_29.solutions == enhanced_5_29.solutions
    assert len(baseline_5_29.solutions) == 7
    assert baseline_5_29.count("nodes") == 113
    assert enhanced_5_29.count("nodes") == 110
    assert enhanced_5_29.count("disjoint_prune") == 1

    baseline_7_37 = run_find_cover(
        k=7,
        p=37,
        use_disjoint_requirement_prune=False,
    )
    enhanced_7_37 = run_find_cover(
        k=7,
        p=37,
        use_disjoint_requirement_prune=True,
    )

    assert baseline_7_37.solutions == enhanced_7_37.solutions
    assert len(baseline_7_37.solutions) == 177
    assert baseline_7_37.count("nodes") == 1752
    assert enhanced_7_37.count("nodes") == 1743
    assert enhanced_7_37.count("disjoint_prune") == 3
