"""Lonely Runner: continuous A/M contact calculus plus history-geometry cost.

This calibration is the first Sonnet-001 experiment in which the A/M *calculus*
itself, rather than only the finite multiplicative action, generates the task
history.

For one runner, contact boundaries have the lifted form

    tau(v) = exp(-v) * alpha,

so the multiplicative generator satisfies d tau / d v = -tau.  For several
runners, contact-order changes occur only on walls where two such times agree.
Those wall crossings generate a finite contact history.  We then evaluate
representations of that history using Shakespeare's history geometry:

* depth / stopping depth is the time-like axis;
* boundary width is the space-like axis;
* Huffman expected code depth is the optimal finite prefix-depth allocation for
  the observed task classes.

The important red team is that a fixed contact-jet depth selected on a smaller
finite world does not transfer.  A variable stopping tree does transfer as an
exact process representation: follow contacts until the first lonely witness.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
import math

import sympy as sp

from aeg_shakespeare.history_geometry import boundary_profile, huffman_prefix_code
from aeg_shakespeare.process.history import ProcessWord


@dataclass(frozen=True)
class ContactTransition:
    time: Fraction
    boundary: tuple[tuple[int, int, str], ...]
    bad_before: tuple[int, ...]
    bad_on: tuple[int, ...]
    bad_after: tuple[int, ...]

    @property
    def shape(self) -> tuple[object, ...]:
        """Scale-free process token; the absolute contact time is deliberately dropped."""

        return (self.boundary, self.bad_on, self.bad_after)


@dataclass(frozen=True)
class Witness:
    event_index: int
    boundary: tuple[tuple[int, int, str], ...]
    mode: str
    time: Fraction

    @property
    def task_key(self) -> tuple[object, ...]:
        """Scale-free certificate; input speeds decode the actual witness time."""

        return (self.event_index, self.boundary, self.mode)


def contact_transitions(
    speeds: tuple[int, ...],
    *,
    final_k: int,
    event_limit: int = 64,
) -> tuple[ContactTransition, ...]:
    """Exact lifted contact process for positive integral relative speeds."""

    if not speeds:
        return ()
    if any(speed <= 0 for speed in speeds):
        raise ValueError("relative speeds must be positive")

    delta = Fraction(1, final_k + 1)
    events: dict[Fraction, list[tuple[int, int, str]]] = defaultdict(list)

    # The first event_limit contacts of any single runner use at most roughly
    # event_limit/2 integer centers.  The generous bound below stays tiny for
    # these semantic calibrations and avoids floating-point event ordering.
    for runner, speed in enumerate(speeds):
        for center in range(event_limit + 4):
            exit_time = (Fraction(center) + delta) / speed
            if exit_time > 0:
                events[exit_time].append((runner, center, "exit"))
            if center >= 1:
                enter_time = (Fraction(center) - delta) / speed
                if enter_time > 0:
                    events[enter_time].append((runner, center, "enter"))

    bad = set(range(len(speeds)))
    transitions: list[ContactTransition] = []

    for time in sorted(events):
        group = tuple(sorted(events[time]))
        bad_before = tuple(sorted(bad))
        boundary_runners = {runner for runner, _center, _kind in group}
        # At the contact instant itself equality is allowed in LRC, so every
        # runner participating in the boundary event is safe at that instant.
        bad_on = tuple(sorted(bad - boundary_runners))

        after = set(bad)
        for runner, _center, kind in group:
            if kind == "exit":
                after.discard(runner)
            elif kind == "enter":
                after.add(runner)
            else:  # pragma: no cover - construction is closed above
                raise AssertionError(kind)

        transition = ContactTransition(
            time=time,
            boundary=group,
            bad_before=bad_before,
            bad_on=bad_on,
            bad_after=tuple(sorted(after)),
        )
        transitions.append(transition)
        bad = after
        if len(transitions) >= event_limit:
            break

    return tuple(transitions)


def first_witness(
    speeds: tuple[int, ...],
    *,
    final_k: int,
) -> Witness:
    """Return the first exact point/interval at which all current runners are safe."""

    for index, transition in enumerate(
        contact_transitions(speeds, final_k=final_k, event_limit=96),
        start=1,
    ):
        if transition.bad_on:
            continue
        mode = "interval" if not transition.bad_after else "point"
        return Witness(
            event_index=index,
            boundary=transition.boundary,
            mode=mode,
            time=transition.time,
        )
    raise AssertionError("finite calibration did not find a witness")


def stopping_history(
    speeds: tuple[int, ...],
    *,
    final_k: int,
) -> ProcessWord[tuple[object, ...]]:
    """AM-contact history stopped at the first exact lonely witness."""

    steps: list[tuple[object, ...]] = []
    for transition in contact_transitions(speeds, final_k=final_k, event_limit=96):
        steps.append(transition.shape)
        if not transition.bad_on:
            return ProcessWord(tuple(steps))
    raise AssertionError("finite calibration did not find a witness")


def contact_jet(
    speeds: tuple[int, ...],
    *,
    final_k: int,
    depth: int,
) -> tuple[tuple[object, ...], ...]:
    """Fixed-depth contact jet used only as a transfer red team."""

    return tuple(
        transition.shape
        for transition in contact_transitions(
            speeds,
            final_k=final_k,
            event_limit=max(depth, 1),
        )[:depth]
    )


def distinct_pairs(limit: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(1, limit + 1), 2))


def relative_m_key(pair: tuple[int, int]) -> Fraction:
    return Fraction(pair[1], pair[0])


def partition_is_task_sufficient(keys, tasks) -> bool:
    seen = {}
    for key, task in zip(keys, tasks):
        old = seen.get(key)
        if old is not None and old != task:
            return False
        seen[key] = task
    return True


def fixed_jet_is_sufficient(*, limit: int, depth: int) -> bool:
    pairs = distinct_pairs(limit)
    return partition_is_task_sufficient(
        [contact_jet(pair, final_k=2, depth=depth) for pair in pairs],
        [first_witness(pair, final_k=2).task_key for pair in pairs],
    )


def terminal_huffman_metrics(keys):
    weights = Counter(keys)
    return huffman_prefix_code(weights).metrics()


def test_contact_time_is_an_m_flow_and_walls_are_relative_m_equations() -> None:
    v = sp.symbols("v", real=True)
    alpha = sp.symbols("alpha", positive=True)
    tau = sp.exp(-v) * alpha
    assert sp.simplify(sp.diff(tau, v) + tau) == 0

    # alpha*exp(-v1) = beta*exp(-v2) is exactly a wall in relative M position.
    v1 = sp.symbols("v1", real=True)
    beta = sp.symbols("beta", positive=True)
    v2 = v1 + sp.log(beta / alpha)
    assert sp.simplify(alpha * sp.exp(-v1) - beta * sp.exp(-v2)) == 0

    # Global M scaling changes physical contact times but not the contact history.
    base = (2, 5)
    scaled = (6, 15)
    base_history = stopping_history(base, final_k=2)
    scaled_history = stopping_history(scaled, final_k=2)
    assert base_history == scaled_history

    base_witness = first_witness(base, final_k=2)
    scaled_witness = first_witness(scaled, final_k=2)
    assert base_witness.task_key == scaled_witness.task_key
    assert base_witness.time == 3 * scaled_witness.time


def test_contact_calculus_keeps_isolated_boundary_witnesses() -> None:
    # For (1,2) at delta=1/3, t=1/3 is a genuine lonely point: runner 1 is
    # leaving its bad interval exactly when runner 2 enters another one.  There
    # is no open safe interval after the event, so an interval-only combinatorial
    # model would miss the witness.
    witness = first_witness((1, 2), final_k=2)
    assert witness.time == Fraction(1, 3)
    assert witness.mode == "point"
    assert witness.event_index == 2

    transition = contact_transitions((1, 2), final_k=2, event_limit=2)[1]
    assert transition.bad_on == ()
    assert transition.bad_after == (1,)
    assert transition.boundary == (
        (0, 0, "exit"),
        (1, 1, "enter"),
    )


def test_fixed_contact_jet_overfits_but_variable_stopping_tree_transfers() -> None:
    # A bounded jet selected on a smaller solved world appears sufficient...
    assert not fixed_jet_is_sufficient(limit=12, depth=7)
    assert fixed_jet_is_sufficient(limit=12, depth=8)
    # ...but the same frozen depth fails immediately on the larger holdout.
    assert not fixed_jet_is_sufficient(limit=16, depth=8)

    # The process-native alternative is not a universal fixed jet: stop exactly
    # when the task observer fires.  This remains exact without choosing a depth.
    for limit in (12, 16, 20):
        for pair in distinct_pairs(limit):
            history = stopping_history(pair, final_k=2)
            witness = first_witness(pair, final_k=2)
            assert len(history.steps) == witness.event_index


def test_huffman_history_geometry_scores_space_and_time_together() -> None:
    pairs = distinct_pairs(12)
    selection_histories = tuple(ProcessWord(pair) for pair in pairs)
    tasks = tuple(first_witness(pair, final_k=2).task_key for pair in pairs)

    def literal_prefix(word: ProcessWord[int]):
        return word.steps

    def relative_prefix(word: ProcessWord[int]):
        if word.depth == 0:
            return ()
        if word.depth == 1:
            return ("M-orbit",)
        return relative_m_key((word.steps[0], word.steps[1]))

    def witness_prefix(word: ProcessWord[int]):
        if word.depth == 0:
            return ()
        if word.depth == 1:
            return ("contact-process",)
        return first_witness((word.steps[0], word.steps[1]), final_k=2).task_key

    literal_profile = boundary_profile(
        selection_histories,
        max_depth=2,
        quotient_key=literal_prefix,
    )
    relative_profile = boundary_profile(
        selection_histories,
        max_depth=2,
        quotient_key=relative_prefix,
    )
    witness_profile = boundary_profile(
        selection_histories,
        max_depth=2,
        quotient_key=witness_prefix,
    )

    assert literal_profile.widths == (1, 11, 66)
    assert relative_profile.widths == (1, 1, 45)
    assert witness_profile.widths == (1, 1, 13)

    literal_keys = tuple(pair for pair in pairs)
    relative_keys = tuple(relative_m_key(pair) for pair in pairs)
    witness_keys = tasks

    assert partition_is_task_sufficient(literal_keys, tasks)
    assert partition_is_task_sufficient(relative_keys, tasks)
    assert partition_is_task_sufficient(witness_keys, tasks)

    literal_huffman = terminal_huffman_metrics(literal_keys)
    relative_huffman = terminal_huffman_metrics(relative_keys)
    witness_huffman = terminal_huffman_metrics(witness_keys)

    # The calculus-derived task quotient strictly improves both history-geometry
    # axes over the absolute and relative-coordinate presentations.
    assert (
        witness_profile.peak_information_width
        < relative_profile.peak_information_width
        < literal_profile.peak_information_width
    )
    assert (
        witness_huffman.expected_depth
        < relative_huffman.expected_depth
        < literal_huffman.expected_depth
    )

    assert math.isclose(witness_huffman.expected_depth, 2.5454545454545454)
    assert math.isclose(relative_huffman.expected_depth, 5.257575757575758)
    assert math.isclose(literal_huffman.expected_depth, 6.0606060606060606)


def test_contact_stopping_tree_is_narrow_and_exposes_a_huffman_shortcut_gap() -> None:
    pairs = distinct_pairs(12)
    histories = tuple(stopping_history(pair, final_k=2) for pair in pairs)
    profile = boundary_profile(histories)

    # This is the striking geometry: as the speed-pair input set grows to 66
    # literal instances, the continuous contact process needs at most four
    # distinguishable prefix states at any stopping depth in this calibration.
    assert profile.widths == (1, 1, 3, 3, 4, 3, 3, 3, 3, 1, 1)
    assert profile.peak_width == 4
    assert math.isclose(profile.peak_information_width, 2.0)

    average_process_depth = sum(history.depth for history in histories) / len(histories)
    assert math.isclose(average_process_depth, 215 / 66)

    task_weights = Counter(first_witness(pair, final_k=2).task_key for pair in pairs)
    optimal_prefix = huffman_prefix_code(task_weights).metrics()
    assert optimal_prefix.leaf_count == 13
    assert math.isclose(optimal_prefix.expected_depth, 2.5454545454545454)

    # The difference is actionable: contact calculus already collapses the
    # space-like frontier, while Huffman says there is still average depth that
    # could in principle be removed by discovering reusable contact shortcuts.
    assert optimal_prefix.expected_depth < average_process_depth
    assert average_process_depth - optimal_prefix.expected_depth > 0.7
