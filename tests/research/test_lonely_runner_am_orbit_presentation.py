"""Lonely Runner Phase 7: finite A/M orbit presentation.

This calibration deliberately avoids linear/Fourier machinery.  The finite
mod-p problem is reconstructed directly from the arithmetic process pair

    A_p = (F_p, +),
    M_p = (F_p^*, *),
    M_s : a -> s*a.

The sign-folded bad-time window is one primitive observer.  Every speed cover is
its pullback under one M action.  Two-speed completion then has an exact relative
presentation: after quotienting simultaneous multiplication, a pair (s,t) is
represented by one ratio r=t/s.

The second calibration builds a small search directly on M-orbits of speed
multisets.  It verifies exact terminal-cover preservation and measures the state
compression obtained by removing the arbitrary choice of multiplicative anchor.

This is a representation result, not yet an upstream runtime claim.
"""

from __future__ import annotations

from itertools import combinations_with_replacement

from aeg_shakespeare.process.finite import (
    FamilyAction,
    ProcessFamily,
    verify_family_action,
)


def fold_nonzero(value: int, p: int) -> int:
    residue = value % p
    if residue == 0:
        raise ValueError("folded multiplicative states must be nonzero modulo p")
    return min(residue, p - residue)


def folded_mul(left: int, right: int, p: int) -> int:
    return fold_nonzero(left * right, p)


def folded_inverse(value: int, p: int) -> int:
    return fold_nonzero(pow(value, -1, p), p)


def finite_am_families(p: int):
    """Return the finite Addition family, Multiplication family, and M-on-A action."""

    addition = ProcessFamily(
        name=f"A_mod_{p}",
        combine=lambda left, right: (left + right) % p,
        identity=0,
    )
    multiplication = ProcessFamily(
        name=f"M_mod_{p}",
        combine=lambda left, right: (left * right) % p,
        identity=1,
    )
    action = FamilyAction(
        acting=multiplication,
        target=addition,
        apply=lambda scale, amount: (scale * amount) % p,
        name="finite-AM",
    )
    return addition, multiplication, action


def folded_universe(p: int) -> tuple[int, ...]:
    return tuple(range(1, p // 2 + 1))


def bad_window(*, k: int, p: int) -> frozenset[int]:
    """The primitive sign-folded additive window around zero."""

    return frozenset(
        value
        for value in folded_universe(p)
        if value * (k + 1) < p
    )


def act_folded(scale: int, values: frozenset[int], p: int) -> frozenset[int]:
    return frozenset(folded_mul(scale, value, p) for value in values)


def direct_cover(speed: int, *, k: int, p: int) -> frozenset[int]:
    bad = bad_window(k=k, p=p)
    return frozenset(
        time
        for time in folded_universe(p)
        if folded_mul(time, speed, p) in bad
    )


def am_cover(speed: int, *, k: int, p: int) -> frozenset[int]:
    """C_s = s^{-1} B, reconstructed from one bad-window primitive."""

    return act_folded(
        folded_inverse(speed, p),
        bad_window(k=k, p=p),
        p,
    )


def am_pair_union(first: int, second: int, *, k: int, p: int) -> frozenset[int]:
    """Reconstruct C_s union C_t from a base M action and ratio t/s."""

    bad = bad_window(k=k, p=p)
    first_inverse = folded_inverse(first, p)
    ratio = folded_mul(second, first_inverse, p)
    relative_template = bad | act_folded(folded_inverse(ratio, p), bad, p)
    return act_folded(first_inverse, relative_template, p)


def ratio_shape(ratio: int, p: int) -> int:
    """Unordered two-speed shape modulo simultaneous M action."""

    return min(ratio, folded_inverse(ratio, p))


def canonical_speed_multiset(speeds: tuple[int, ...], p: int) -> tuple[int, ...]:
    """Canonicalize a nonempty folded speed multiset under global M action."""

    if not speeds:
        raise ValueError("an M-orbit representative needs at least one speed")
    return min(
        tuple(sorted(folded_mul(unit, speed, p) for speed in speeds))
        for unit in folded_universe(p)
    )


def covers_all(speeds: tuple[int, ...], *, k: int, p: int) -> bool:
    covered: set[int] = set()
    for speed in speeds:
        covered.update(am_cover(speed, k=k, p=p))
    return len(covered) == p // 2


def fixed_one_multisets(depth: int, p: int) -> tuple[tuple[int, ...], ...]:
    """Literal canonical grammar used in the earlier Sonnet calibration."""

    universe = folded_universe(p)
    return tuple(
        (1,) + tail
        for tail in combinations_with_replacement(universe, depth - 1)
    )


def orbit_bfs_counts(*, max_depth: int, p: int) -> tuple[int, ...]:
    """State counts for the search grammar whose states are M-orbits."""

    universe = folded_universe(p)
    states = {canonical_speed_multiset((speed,), p) for speed in universe}
    counts = [len(states)]
    for _depth in range(2, max_depth + 1):
        states = {
            canonical_speed_multiset(state + (speed,), p)
            for state in states
            for speed in universe
        }
        counts.append(len(states))
    return tuple(counts)


def test_finite_am_action_is_exact_without_linearization() -> None:
    addition, multiplication, action = finite_am_families(29)

    verification = verify_family_action(
        action,
        acting_parameters=(1, 2, 7, 11),
        acting_pairs=((2, 7), (7, 11), (11, 3)),
        target_parameters=(0, 1, 5, 13),
        target_pairs=((1, 2), (5, 9), (13, 17)),
    )
    assert verification.exact
    assert addition.compose_parameters(17, 19) == 7
    assert multiplication.compose_parameters(7, 11) == 19
    assert action.transport_parameter(7, 5) == 6


def test_every_cover_is_one_multiplicative_translate_of_one_bad_window() -> None:
    # Include the actual solved-frontier parameter sets.  This is only O(p^2)
    # integer arithmetic and stays a cheap semantic regression test.
    for k, p in ((8, 79), (9, 89), (10, 127), (11, 131), (12, 139)):
        for speed in folded_universe(p):
            assert am_cover(speed, k=k, p=p) == direct_cover(speed, k=k, p=p)


def test_two_slot_family_has_an_exact_relative_m_presentation() -> None:
    k = 5
    p = 29
    universe = folded_universe(p)

    for first in universe:
        for second in universe:
            assert am_pair_union(first, second, k=k, p=p) == (
                direct_cover(first, k=k, p=p)
                | direct_cover(second, k=k, p=p)
            )

    # Unordered pairs modulo simultaneous multiplication are classified by the
    # relative ratio r=t/s up to r <-> r^{-1}.  At the open p=199 frontier this
    # turns 4,950 literal unordered speed pairs into only 50 relative shapes.
    p_open = 199
    open_universe = folded_universe(p_open)
    shapes = {
        ratio_shape(ratio, p_open)
        for ratio in open_universe
    }
    assert len(open_universe) == 99
    assert len(shapes) == 50
    assert len(open_universe) * (len(open_universe) + 1) // 2 == 4950


def test_m_orbit_search_preserves_cover_task_and_compresses_small_worlds() -> None:
    k = 5
    p = 17

    # Fixed-first literal states versus direct M-orbit states by depth.
    literal_counts = tuple(
        len(fixed_one_multisets(depth, p))
        for depth in range(1, k + 1)
    )
    orbit_counts = orbit_bfs_counts(max_depth=k, p=p)

    assert literal_counts == (1, 8, 36, 120, 330)
    assert orbit_counts == (1, 5, 15, 43, 99)
    assert sum(literal_counts[:-1]) == 165
    assert sum(orbit_counts[:-1]) == 64

    # The terminal predicate is constant on every M orbit, so quotienting is
    # exact for the solution-class task rather than a heuristic compression.
    terminals = fixed_one_multisets(k, p)
    for state in terminals:
        canonical = canonical_speed_multiset(state, p)
        assert covers_all(state, k=k, p=p) == covers_all(canonical, k=k, p=p)

    literal_solutions = tuple(
        state for state in terminals if covers_all(state, k=k, p=p)
    )
    orbit_solutions = {
        canonical_speed_multiset(state, p)
        for state in literal_solutions
    }
    assert len(literal_solutions) == 18
    assert len(orbit_solutions) == 4


def test_m_orbit_transition_is_well_defined_under_reanchoring() -> None:
    p = 17
    universe = folded_universe(p)
    state = (1, 3, 6)

    for unit in universe:
        transported_state = tuple(
            sorted(folded_mul(unit, speed, p) for speed in state)
        )
        for next_speed in universe:
            transported_next = folded_mul(unit, next_speed, p)
            assert canonical_speed_multiset(state + (next_speed,), p) == (
                canonical_speed_multiset(
                    transported_state + (transported_next,),
                    p,
                )
            )
