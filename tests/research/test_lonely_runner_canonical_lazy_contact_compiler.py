"""Sonnet 001 Phase 11B1: compile task predicates from canonical dynamics.

The discovery implementation receives no contact-center horizon, no frozen
contact-ratio alphabet, and no old 21/26/29-wall target.  This test uses the old
results only *after* discovery as a red-team identity check.
"""

from __future__ import annotations

from fractions import Fraction
import importlib.util
from pathlib import Path
import sys


def _load_compiler():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    path = script_dir / "canonical_lazy_contact_compiler.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_canonical_lazy_contact_compiler",
            path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def _frozen_global_task_coordinates():
    """Old result used only as a post-discovery red team.

    The set is the 21 globally relevant center<=2 coordinates, the five new
    globally relevant center<=3 coordinates, and the shared center-4 19/11
    coordinate.  The two extra Phase-8C local-minimum walls are intentionally
    absent because they did not survive the earlier global relevance analysis.
    """

    return {
        (0, 1, Fraction(4)),
        (0, 1, Fraction(6)),
        (0, 2, Fraction(4)),
        (0, 2, Fraction(6)),
        (0, 3, Fraction(4)),
        (0, 3, Fraction(6)),
        (1, 2, Fraction(3, 2)),
        (1, 2, Fraction(11, 6)),
        (1, 2, Fraction(4)),
        (1, 2, Fraction(6)),
        (1, 3, Fraction(3, 2)),
        (1, 3, Fraction(11, 6)),
        (1, 3, Fraction(9, 4)),
        (1, 3, Fraction(7, 3)),
        (1, 3, Fraction(8, 3)),
        (1, 3, Fraction(11, 4)),
        (1, 3, Fraction(4)),
        (1, 3, Fraction(6)),
        (2, 3, Fraction(11, 9)),
        (2, 3, Fraction(14, 11)),
        (2, 3, Fraction(3, 2)),
        (2, 3, Fraction(14, 9)),
        (2, 3, Fraction(19, 11)),
        (2, 3, Fraction(16, 9)),
        (2, 3, Fraction(11, 6)),
        (2, 3, Fraction(4)),
        (2, 3, Fraction(6)),
    }


def test_partial_singleton_separator_is_not_a_generic_minimality_proof() -> None:
    """Freeze the smallest joint-refinement counterexample to the old argument."""

    # Partial task regions A=(-, ?, ?) and B=(+, ?, ?) make coordinate 0 look
    # like their unique forced separator.  Their feasible completions show that
    # coordinates 1 and 2 jointly separate the tasks without coordinate 0.
    completions = {
        "A": {(-1, -1, -1), (-1, 1, 1)},
        "B": {(1, -1, 1), (1, 1, -1)},
    }
    partial = {"A": (-1, None, None), "B": (1, None, None)}
    forced_separator_indices = {
        index
        for index, (left, right) in enumerate(zip(partial["A"], partial["B"]))
        if left is not None and right is not None and left != right
    }
    assert forced_separator_indices == {0}

    projected = {
        task: {(signature[1], signature[2]) for signature in signatures}
        for task, signatures in completions.items()
    }
    assert projected["A"].isdisjoint(projected["B"])


def test_lazy_compiler_closes_without_a_supplied_contact_horizon() -> None:
    compiler = _load_compiler()
    result = compiler.analyze_lazy_compiler()

    assert result.symbolic_states == 388
    assert result.terminal_regions == 261
    assert result.task_count == 81
    assert result.max_event_index == 18
    assert result.max_contact_center == 4

    # The compiler encounters 33 genuinely unresolved equality loci, then exact
    # task separation proves that only 27 are cardinality-minimum necessities.
    assert len(result.generated_coordinates) == 33
    assert len(result.minimum_task_coordinates) == 27
    assert result.unique_separator_witnesses == 27
    assert result.full_sign_cells == 4_343
    assert result.exact_deletion_witnesses == 27

    # The old singleton test on partial terminal regions is only a discovery
    # heuristic.  Exact minimality now has a stronger, independently replayable
    # shape: each selected coordinate has two complete generated-sign cells of
    # different tasks that agree after deleting exactly that coordinate.
    assert {
        witness.coordinate_index
        for witness in result.deletion_witnesses
    } == {
        result.generated_coordinates.index(coordinate)
        for coordinate in result.minimum_task_coordinates
    }
    for witness in result.deletion_witnesses:
        index = witness.coordinate_index
        assert witness.left_task != witness.right_task
        assert witness.left_signature[index] != witness.right_signature[index]
        assert (
            witness.left_signature[:index]
            + witness.left_signature[index + 1 :]
            == witness.right_signature[:index]
            + witness.right_signature[index + 1 :]
        )


def test_lazy_minimum_is_exactly_the_old_global_task_wall_set() -> None:
    compiler = _load_compiler()
    result = compiler.analyze_lazy_compiler()

    discovered = set(result.minimum_task_coordinates)
    frozen = _frozen_global_task_coordinates()
    assert discovered == frozen

    # The canonical compiler therefore rediscovers the earlier global task
    # geometry without receiving its staged center-2/3/4 construction.
    assert (2, 3, Fraction(19, 11)) in discovered

    # These two walls were useful in per-parent Phase-8C minimum signatures but
    # were already known not to survive global relevance.  The new compiler
    # independently leaves them out of its global minimum.
    assert (1, 2, Fraction(14, 11)) not in discovered
    assert (1, 2, Fraction(16, 11)) not in discovered
