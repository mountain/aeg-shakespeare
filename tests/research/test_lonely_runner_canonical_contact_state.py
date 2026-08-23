"""Sonnet 001: canonical torus contact state before completion/Hauffman analysis.

This research calibration revisits the lifted A/M contact process after the
canonicalization C1--C4 closure.  The lifted coordinates

    s_i(t) = t u_i in R

contain a deck/sheet coordinate that is not part of the physical torus phase.
The canonical carrier used here is

    phi_i = s_i mod 1 in [0, 1),

with exact boundary semantics.  Integer contact centers are reconstructed only
for certificate comparison; they are not inputs to the state transition.

This is intentionally a bounded semantic red team, not a new Lonely Runner
theorem and not evidence for a public discrete ObserverConnection API.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations


@dataclass(frozen=True)
class CanonicalWitness:
    event_index: int
    boundary: tuple[tuple[int, str], ...]
    mode: str
    time: Fraction
    decoded_lift_boundary: tuple[tuple[int, int, str], ...]


def fundamental_phase(value: Fraction) -> Fraction:
    """Canonical representative of one universal-cover phase modulo Z."""

    return value % 1


def bad_after_phase(phase: Fraction, delta: Fraction) -> bool:
    """Whether a positive-speed runner is bad immediately after this phase."""

    return phase < delta or phase >= 1 - delta


def next_boundary_from_phase(
    phase: Fraction,
    delta: Fraction,
) -> tuple[Fraction, str]:
    """Return phase distance and kind of the next contact boundary.

    The rule is center-free.  At phase=delta the previous exit has already
    happened, so the next event is an enter at 1-delta.  At phase=1-delta the
    previous enter has already happened, so the next event is the exit after
    wrap, at 1+delta.
    """

    if not (0 <= phase < 1):
        raise ValueError("phase must use the canonical [0,1) representative")
    if phase < delta:
        return delta - phase, "exit"
    if phase < 1 - delta:
        return 1 - delta - phase, "enter"
    return 1 + delta - phase, "exit"


def decode_contact_center(
    *,
    time: Fraction,
    speed: Fraction,
    delta: Fraction,
    kind: str,
) -> int:
    """Recover the universal-cover sheet index from certificate provenance."""

    lifted = time * speed
    center = lifted - delta if kind == "exit" else lifted + delta
    assert center.denominator == 1
    return int(center)


def canonical_first_witness(
    speeds: tuple[int | Fraction, ...],
    *,
    final_k: int,
    event_limit: int = 512,
) -> CanonicalWitness:
    """First witness using only torus phase plus positive relative speeds."""

    if not speeds or any(Fraction(speed) <= 0 for speed in speeds):
        raise ValueError("relative speeds must be positive")

    speeds_q = tuple(Fraction(speed) for speed in speeds)
    delta = Fraction(1, final_k + 1)
    phases = tuple(Fraction(0) for _ in speeds_q)
    time = Fraction(0)

    for event_index in range(1, event_limit + 1):
        bad_before = {
            runner
            for runner, phase in enumerate(phases)
            if bad_after_phase(phase, delta)
        }
        candidates = []
        for runner, (phase, speed) in enumerate(zip(phases, speeds_q)):
            phase_distance, kind = next_boundary_from_phase(phase, delta)
            candidates.append((phase_distance / speed, runner, kind))

        dt = min(item[0] for item in candidates)
        group = tuple(
            sorted(
                (runner, kind)
                for candidate_dt, runner, kind in candidates
                if candidate_dt == dt
            )
        )
        boundary_runners = {runner for runner, _kind in group}
        bad_on = bad_before - boundary_runners

        time += dt
        phases = tuple(
            fundamental_phase(phase + speed * dt)
            for phase, speed in zip(phases, speeds_q)
        )

        bad_after = set(bad_before)
        for runner, kind in group:
            if kind == "exit":
                bad_after.discard(runner)
            elif kind == "enter":
                bad_after.add(runner)
            else:  # pragma: no cover
                raise AssertionError(kind)

        # The canonical torus state itself agrees with the explicit transition
        # update, including exact equality strata.
        assert bad_after == {
            runner
            for runner, phase in enumerate(phases)
            if bad_after_phase(phase, delta)
        }

        if not bad_on:
            decoded = tuple(
                sorted(
                    (
                        runner,
                        decode_contact_center(
                            time=time,
                            speed=speeds_q[runner],
                            delta=delta,
                            kind=kind,
                        ),
                        kind,
                    )
                    for runner, kind in group
                )
            )
            return CanonicalWitness(
                event_index=event_index,
                boundary=group,
                mode="interval" if not bad_after else "point",
                time=time,
                decoded_lift_boundary=decoded,
            )

    raise AssertionError("event limit did not reach a witness")


def lifted_first_witness(
    speeds: tuple[int, ...],
    *,
    final_k: int,
    max_center: int = 32,
) -> tuple[int, tuple[tuple[int, int, str], ...], str, Fraction]:
    """Independent finite universal-cover oracle used only as a red team."""

    delta = Fraction(1, final_k + 1)
    events: dict[Fraction, list[tuple[int, int, str]]] = defaultdict(list)
    for runner, speed in enumerate(speeds):
        for center in range(max_center + 1):
            exit_time = (Fraction(center) + delta) / speed
            if exit_time > 0:
                events[exit_time].append((runner, center, "exit"))
            if center >= 1:
                enter_time = (Fraction(center) - delta) / speed
                if enter_time > 0:
                    events[enter_time].append((runner, center, "enter"))

    bad = set(range(len(speeds)))
    event_index = 0
    for time in sorted(events):
        event_index += 1
        group = tuple(sorted(events[time]))
        boundary_runners = {runner for runner, _center, _kind in group}
        bad_on = bad - boundary_runners

        after = set(bad)
        for runner, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            else:
                after.add(runner)

        if not bad_on:
            return (
                event_index,
                group,
                "interval" if not after else "point",
                time,
            )
        bad = after

    raise AssertionError("finite lifted oracle did not reach a witness")


def test_fundamental_domain_quotients_deck_lifts_exactly() -> None:
    base = (Fraction(2, 7), Fraction(5, 11), Fraction(13, 17), Fraction(0))
    shifts = (3, -4, 19, 8)
    assert tuple(
        fundamental_phase(value + shift)
        for value, shift in zip(base, shifts)
    ) == base


def test_point_witness_semantics_survive_canonicalization() -> None:
    witness = canonical_first_witness((1, 2), final_k=2)
    assert witness.event_index == 2
    assert witness.time == Fraction(1, 3)
    assert witness.mode == "point"
    assert witness.decoded_lift_boundary == (
        (0, 0, "exit"),
        (1, 1, "enter"),
    )


def test_canonical_event_map_crosses_old_center_horizons_without_new_state_axes() -> None:
    center3 = canonical_first_witness((2, 6, 9, 14), final_k=4)
    assert center3.decoded_lift_boundary == (
        (1, 1, "exit"),
        (2, 2, "enter"),
        (3, 3, "enter"),
    )

    center4 = canonical_first_witness((3, 9, 13, 23), final_k=4)
    assert center4.decoded_lift_boundary == ((3, 4, "exit"),)

    # Both are produced by exactly the same phase-local rule.  No contact-center
    # horizon or center-specific wall alphabet is an input to the transition.
    assert center3.mode == "point"
    assert center4.mode == "interval"


def test_canonical_process_matches_lifted_oracle_on_small_four_speed_world() -> None:
    for speeds in combinations(range(1, 10), 4):
        canonical = canonical_first_witness(speeds, final_k=4)
        lifted = lifted_first_witness(speeds, final_k=4)
        assert (
            canonical.event_index,
            canonical.decoded_lift_boundary,
            canonical.mode,
            canonical.time,
        ) == lifted


def test_global_m_scale_changes_only_reconstruction_time() -> None:
    speeds = (3, 9, 13, 23)
    scale = 7
    base = canonical_first_witness(speeds, final_k=4)
    scaled = canonical_first_witness(
        tuple(scale * speed for speed in speeds),
        final_k=4,
    )

    assert scaled.event_index == base.event_index
    assert scaled.boundary == base.boundary
    assert scaled.mode == base.mode
    assert scaled.decoded_lift_boundary == base.decoded_lift_boundary
    assert scaled.time == base.time / scale


def test_boundary_mode_task_label_is_not_a_self_contained_witness() -> None:
    """Dropping event rank and deck sheet also drops witness reconstruction."""

    first = canonical_first_witness((1, 2, 3, 5), final_k=4)
    second = canonical_first_witness((1, 3, 4, 5), final_k=4)

    first_label = (first.boundary, first.mode)
    second_label = (second.boundary, second.mode)
    assert first_label == second_label == (((3, "exit"),), "interval")

    assert (first.event_index, first.time, first.decoded_lift_boundary) == (
        6,
        Fraction(6, 25),
        ((3, 1, "exit"),),
    )
    assert (second.event_index, second.time, second.decoded_lift_boundary) == (
        11,
        Fraction(11, 25),
        ((3, 2, "exit"),),
    )
