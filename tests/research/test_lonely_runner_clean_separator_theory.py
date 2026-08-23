"""Executable red teams for Sonnet 001 Phase 13A clean-separator theory."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "clean_separator_theory.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_clean_separator_theory",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_pairwise_task_separation_does_not_imply_clean_separability():
    m = _load()

    # Every pair of different tasks has a jointly-defined opposite sign:
    #   A/B separated by c0
    #   B/C separated by c1
    #   A/C separated by c2
    # but every coordinate is undefined on the third region.  Therefore the
    # mixed three-region family has no legal clean root query.
    regions = (
        m.PartialRegion("A", "A", (0, None, 0)),
        m.PartialRegion("B", "B", (1, 0, None)),
        m.PartialRegion("C", "C", (None, 1, 1)),
    )

    assert m.pairwise_task_separable(regions)
    assert m.clean_coordinates(regions, frozenset(range(3))) == ()

    result = m.analyze_clean_separability(regions)
    assert not result.clean
    assert result.tree is None
    assert result.obstruction is not None
    assert result.obstruction.atomic
    assert m.verify_obstruction(regions, result.obstruction)


def test_clean_separability_can_hold_with_partial_signatures():
    m = _load()

    # c0 is clean at the root.  Its negative branch is already task A; its
    # positive branch is cleanly resolved by c1 even though c1 was deliberately
    # left undefined on the root's A regions.
    regions = (
        m.PartialRegion("A0", "A", (-1, None)),
        m.PartialRegion("A1", "A", (-1, None)),
        m.PartialRegion("B", "B", (1, -1)),
        m.PartialRegion("C", "C", (1, 1)),
    )

    result = m.analyze_clean_separability(regions)
    assert result.clean
    assert result.tree is not None
    assert result.obstruction is None
    assert result.max_depth == 2
    assert result.tree_nodes == 5
    assert m.verify_tree(regions, result.tree)


def test_recursive_obstruction_covers_every_possible_clean_root():
    m = _load()

    # c0 and c1 are both legal root queries.  Each choice sends one branch into
    # a mixed-task pair that has no clean coordinate left.  The resulting
    # obstruction is therefore genuinely recursive rather than merely atomic at
    # the original root.
    regions = (
        m.PartialRegion("A", "A", (-1, -1, None, 0)),
        m.PartialRegion("B", "B", (-1, 1, 0, None)),
        m.PartialRegion("C", "C", (1, -1, 1, None)),
        m.PartialRegion("D", "D", (1, 1, None, 1)),
    )

    # Pairwise separability is intentionally stronger than needed for the red
    # team: failure is caused by incompatibility of clean recursive placement,
    # not by an inseparable task pair.
    assert m.pairwise_task_separable(regions)
    assert set(m.clean_coordinates(regions, frozenset(range(4)))) == {0, 1}

    result = m.analyze_clean_separability(regions)
    assert not result.clean
    assert result.obstruction is not None
    assert not result.obstruction.atomic
    assert {
        failure.coordinate
        for failure in result.obstruction.candidate_failures
    } == {0, 1}
    assert m.verify_obstruction(regions, result.obstruction)
