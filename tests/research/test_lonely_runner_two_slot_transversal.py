"""Lonely Runner Phase 5: exact two-slot transversal pruning.

Question
--------
Can the requirement representation discovered in Phases 2--4 be lowered to a
cheap exact certificate that materially reduces the real upstream find_cover
search on primes already present in the solved configurations?

Primitive / upstream data
-------------------------
This file keeps the Phase-4 semantic mirror of vzsky/13-lonely-runners/find_cover:
folded speed residues, bad-time bitsets, AvailableChoice sibling elimination,
MRV next-time selection, the existing optimistic early_return_bound, and the
serialized equivalent of the top-level parallel workers.

Shakespeare reconstruction
---------------------------
With exactly two speed slots remaining, future completion is equivalent to a
2-transversal of the repair-requirement hypergraph, or equivalently to two
currently available speed-cover bitsets whose union contains every uncovered
time bit.  This is the first cost-selected exact shadow of the full future task
language.

Calibration statement
---------------------
Passing this file certifies:

* a reachable k=8,p=79 state that survives the upstream bound but has no two-speed
  completion;
* complete raw-history equality before/after the new prune at k=8,p=79 and
  k=9,p=89;
* deterministic node reductions

      k=8,p=79:   39813 -> 28828   (2276 new prunes)
      k=9,p=89:  161820 -> 112951  (10113 new prunes)

The tested primes occur in the current upstream configured prime lists.

Boundary
--------
This is still a Python semantic mirror, not a benchmark of a patched upstream C++
binary.  Node reductions are exact search metrics; Python timings are intentionally
not asserted.

Reference
---------
[Sungkawichai-Trakulthongchai-code-2026]
https://github.com/vzsky/13-lonely-runners
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class CoverContext:
    k: int
    p: int
    half: int
    full: int
    all_choices: int
    masks: tuple[int, ...]
    position_choices: tuple[int, ...]

    @classmethod
    def build(cls, *, k: int, p: int) -> "CoverContext":
        half = p // 2
        masks: list[int] = []
        for speed in range(1, half + 1):
            mask = 0
            for time_numerator in range(1, half + 1):
                position = half - time_numerator
                remainder = (time_numerator * speed) % p
                if (
                    remainder * (k + 1) < p
                    or (p - remainder) * (k + 1) < p
                ):
                    mask |= 1 << position
            masks.append(mask)

        position_choices = []
        for position in range(half):
            choices = 0
            for choice, mask in enumerate(masks):
                if mask & (1 << position):
                    choices |= 1 << choice
            position_choices.append(choices)

        return cls(
            k=k,
            p=p,
            half=half,
            full=(1 << half) - 1,
            all_choices=(1 << half) - 1,
            masks=tuple(masks),
            position_choices=tuple(position_choices),
        )


@dataclass(frozen=True)
class StateAnalysis:
    prune: bool
    selected_position: int
    available: int


def analyze_upstream_state(
    context: CoverContext,
    *,
    covered: int,
    eliminated: int,
    depth: int,
) -> StateAnalysis:
    """Fuse the repeated reads in the Phase-4 transliteration, preserving semantics."""

    available = context.all_choices ^ eliminated
    selected = -1
    minimum = 1 << 30

    for position, position_choices in enumerate(context.position_choices):
        if covered & (1 << position):
            continue
        count = (position_choices & available).bit_count()
        if count < minimum:
            minimum = count
            selected = position

    if selected != -1 and minimum == 0:
        return StateAnalysis(True, selected, available)

    if depth < context.k - 4 or selected == -1:
        return StateAnalysis(False, selected, available)

    other_uncovered = (context.full ^ covered) & ~(1 << selected)
    total_to_cover = context.half - covered.bit_count()
    best_covering_next = 0
    best_covering = 0

    remaining = available
    while remaining:
        choice_bit = remaining & -remaining
        remaining -= choice_bit
        choice = choice_bit.bit_length() - 1
        mask = context.masks[choice]
        count = (other_uncovered & mask).bit_count()
        best_covering = max(best_covering, count)
        if mask & (1 << selected):
            best_covering_next = max(best_covering_next, count + 1)

    slots = context.k - depth
    prune = total_to_cover > (
        best_covering_next + best_covering * (slots - 1)
    )
    return StateAnalysis(prune, selected, available)


def two_slot_completion_exists(
    context: CoverContext,
    *,
    covered: int,
    available: int,
) -> bool:
    """Exact two-slot set-cover/transversal decision using integer bitsets."""

    uncovered = context.full ^ covered
    if uncovered == 0:
        return True

    selected = -1
    minimum = 1 << 30
    probe = uncovered
    while probe:
        position_bit = probe & -probe
        probe -= position_bit
        position = position_bit.bit_length() - 1
        count = (context.position_choices[position] & available).bit_count()
        if count < minimum:
            minimum = count
            selected = position

    if selected == -1 or minimum == 0:
        return False

    first_choices = context.position_choices[selected] & available
    while first_choices:
        first_bit = first_choices & -first_choices
        first_choices -= first_bit
        first = first_bit.bit_length() - 1
        residual = uncovered & ~context.masks[first]
        if residual == 0:
            return True

        second_choices = available
        while second_choices:
            second_bit = second_choices & -second_choices
            second_choices -= second_bit
            second = second_bit.bit_length() - 1
            if residual & ~context.masks[second] == 0:
                return True

    return False


def brute_two_slot_completion_exists(
    context: CoverContext,
    *,
    covered: int,
    available: int,
) -> bool:
    """Independent pair enumeration used to red-team the optimized certificate."""

    choices = [
        choice
        for choice in range(context.half)
        if available & (1 << choice)
    ]
    for first in choices:
        for second in choices:
            if covered | context.masks[first] | context.masks[second] == context.full:
                return True
    return False


@dataclass(frozen=True)
class SearchResult:
    solutions: frozenset[tuple[int, ...]]
    counters: tuple[tuple[str, int], ...]

    def count(self, key: str) -> int:
        return dict(self.counters).get(key, 0)


def run_find_cover(
    context: CoverContext,
    *,
    use_two_slot_prune: bool,
) -> SearchResult:
    """Complete serialized mirror of the upstream top-level find_cover search."""

    counters: Counter[str] = Counter()
    solutions: set[tuple[int, ...]] = set()

    def run(
        covered: int,
        eliminated: int,
        chosen: tuple[int, ...],
    ) -> None:
        counters["nodes"] += 1
        depth = len(chosen)

        if depth == context.k:
            if covered == context.full:
                solutions.add(chosen)
            return

        analysis = analyze_upstream_state(
            context,
            covered=covered,
            eliminated=eliminated,
            depth=depth,
        )
        if analysis.prune:
            counters["upstream_prune"] += 1
            return

        slots = context.k - depth
        if use_two_slot_prune and slots == 2:
            counters["two_slot_checks"] += 1
            if not two_slot_completion_exists(
                context,
                covered=covered,
                available=analysis.available,
            ):
                counters["two_slot_prune"] += 1
                return

        selected = analysis.selected_position
        for choice, mask in enumerate(context.masks):
            if eliminated & (1 << choice):
                continue
            if selected == -1 or mask & (1 << selected):
                run(
                    covered | mask,
                    eliminated,
                    chosen + (choice + 1,),
                )
                # Match AvailableChoice::eliminate(i) after returning from the
                # child: this only affects later siblings, not the child itself.
                eliminated |= 1 << choice

    first_covered = context.masks[0]
    first_analysis = analyze_upstream_state(
        context,
        covered=first_covered,
        eliminated=0,
        depth=1,
    )
    second_candidates = tuple(
        choice
        for choice, mask in enumerate(context.masks)
        if (
            first_analysis.selected_position == -1
            or mask & (1 << first_analysis.selected_position)
        )
    )

    eliminated = 0
    for choice in second_candidates:
        run(
            first_covered | context.masks[choice],
            eliminated,
            (1, choice + 1),
        )
        eliminated |= 1 << choice

    return SearchResult(
        solutions=frozenset(solutions),
        counters=tuple(sorted(counters.items())),
    )


def replay_history(
    context: CoverContext,
    history: Sequence[int],
) -> int:
    covered = 0
    for speed in history:
        covered |= context.masks[speed - 1]
    return covered


# RED TEAM: the optimized two-slot certificate is exactly pair enumeration.
def test_two_slot_certificate_matches_brute_pairs_on_reachable_small_states() -> None:
    context = CoverContext.build(k=5, p=29)

    # A selection of histories spanning different current cover shapes.
    histories = (
        (1, 2, 7),
        (1, 4, 5),
        (1, 7, 11),
        (1, 2, 7, 5),
        (1, 6, 10, 13),
    )
    elimination_masks = (
        0,
        1 << (3 - 1),
        (1 << (4 - 1)) | (1 << (9 - 1)),
    )

    for history in histories:
        covered = replay_history(context, history)
        for eliminated in elimination_masks:
            available = context.all_choices ^ eliminated
            assert two_slot_completion_exists(
                context,
                covered=covered,
                available=available,
            ) == brute_two_slot_completion_exists(
                context,
                covered=covered,
                available=available,
            )


# STRICTNESS: reachable upstream state survives old bound but fails exact 2-slot task.
def test_two_slot_certificate_strictly_strengthens_upstream_on_k8_p79() -> None:
    context = CoverContext.build(k=8, p=79)
    history = (1, 2, 7, 5, 3, 15)
    eliminated_speeds = (4, 11)
    eliminated = sum(1 << (speed - 1) for speed in eliminated_speeds)
    covered = replay_history(context, history)

    analysis = analyze_upstream_state(
        context,
        covered=covered,
        eliminated=eliminated,
        depth=len(history),
    )
    assert not analysis.prune
    assert context.k - len(history) == 2
    assert not two_slot_completion_exists(
        context,
        covered=covered,
        available=analysis.available,
    )


# TRANSFER: exact raw-history preservation with substantial node reductions.
def test_two_slot_prune_transfers_to_configured_solved_primes() -> None:
    context_8_79 = CoverContext.build(k=8, p=79)
    baseline_8_79 = run_find_cover(context_8_79, use_two_slot_prune=False)
    enhanced_8_79 = run_find_cover(context_8_79, use_two_slot_prune=True)

    assert baseline_8_79.solutions == enhanced_8_79.solutions
    assert len(baseline_8_79.solutions) == 3529
    assert baseline_8_79.count("nodes") == 39813
    assert enhanced_8_79.count("nodes") == 28828
    assert enhanced_8_79.count("two_slot_prune") == 2276

    context_9_89 = CoverContext.build(k=9, p=89)
    baseline_9_89 = run_find_cover(context_9_89, use_two_slot_prune=False)
    enhanced_9_89 = run_find_cover(context_9_89, use_two_slot_prune=True)

    assert baseline_9_89.solutions == enhanced_9_89.solutions
    assert len(baseline_9_89.solutions) == 12436
    assert baseline_9_89.count("nodes") == 161820
    assert enhanced_9_89.count("nodes") == 112951
    assert enhanced_9_89.count("two_slot_prune") == 10113
