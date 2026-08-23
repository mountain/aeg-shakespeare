"""Cost red team for the Sonnet-001 canonical torus contact carrier.

Canonicalization removes the universal-cover contact-center coordinate from the
process state.  This test checks the corresponding negative result: exact
center-free event evolution is not automatically faster than the already-frozen
static wall compilation.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations


def _bad(phase: Fraction, delta: Fraction) -> bool:
    return phase < delta or phase >= 1 - delta


def _next_distance(phase: Fraction, delta: Fraction) -> Fraction:
    if phase < delta:
        return delta - phase
    if phase < 1 - delta:
        return 1 - delta - phase
    return 1 + delta - phase


def canonical_event_depth(speeds: tuple[int, ...], *, final_k: int) -> int:
    """Exact first-witness event depth using only phases modulo one."""

    delta = Fraction(1, final_k + 1)
    phases = tuple(Fraction(0) for _ in speeds)

    for event_index in range(1, 512):
        bad_before = {
            runner for runner, phase in enumerate(phases) if _bad(phase, delta)
        }
        candidates = tuple(
            (_next_distance(phase, delta) / speed, runner)
            for runner, (phase, speed) in enumerate(zip(phases, speeds))
        )
        dt = min(item[0] for item in candidates)
        boundary_runners = {
            runner for candidate_dt, runner in candidates if candidate_dt == dt
        }

        if not (bad_before - boundary_runners):
            return event_index

        phases = tuple(
            (phase + speed * dt) % 1
            for phase, speed in zip(phases, speeds)
        )

    raise AssertionError("event limit did not reach a witness")


def test_canonicalization_removes_state_growth_but_not_execution_depth() -> None:
    usage = tuple(
        speeds
        for speeds in combinations(range(1, 9), 4)
        if Fraction(speeds[-1], speeds[0]) < 8
    )
    assert len(usage) == 55

    canonical_depth = sum(
        canonical_event_depth(speeds, final_k=4)
        for speeds in usage
    )
    assert canonical_depth == 280

    # Frozen Phase 7f result on exactly this usage world: the exact time-first
    # 21-wall compilation has weighted depth 135.  Hence the canonical carrier
    # is a semantic/generative baseline from which useful predicates may be
    # materialized; it is not itself an execution-speed dominance result.
    frozen_time_first_wall_depth = 135
    assert frozen_time_first_wall_depth < canonical_depth
