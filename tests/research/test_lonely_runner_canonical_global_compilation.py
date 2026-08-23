"""Sonnet 001 Phase 11B2: global compilation of canonical lazy predicates."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    path = script_dir / "canonical_global_compilation.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_canonical_global_compilation",
            path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_canonical_27_wall_objectification_is_smaller_than_old_persistent_carrier() -> None:
    compilation = _load()
    coordinates, task_by_signature = compilation.build_global_sign_cells()

    assert len(coordinates) == 27
    assert len(task_by_signature) == 2_211
    assert len(set(task_by_signature.values())) == 81

    # The shared center-4 wall is generated and retained, but the two extra
    # locally useful Phase-8C coordinates are absent from the global minimum.
    assert (2, 3, Fraction(19, 11)) in coordinates
    assert (1, 2, Fraction(14, 11)) not in coordinates
    assert (1, 2, Fraction(16, 11)) not in coordinates


def test_full_sign_deletion_certificates_replay_through_independent_refiner() -> None:
    compilation = _load()
    compiler = compilation.lazy.analyze_lazy_compiler()
    task_by_signature = {}
    for region in compilation._terminal_regions():
        for signature, _closure in compilation._refine_signature(
            region.closure,
            compiler.generated_coordinates,
        ):
            previous = task_by_signature.setdefault(signature, region.task)
            assert previous == region.task

    assert len(task_by_signature) == 4_343
    for witness in compiler.deletion_witnesses:
        assert task_by_signature[witness.left_signature] == witness.left_task
        assert task_by_signature[witness.right_signature] == witness.right_task
        index = witness.coordinate_index
        assert (
            witness.left_signature[:index]
            + witness.left_signature[index + 1 :]
            == witness.right_signature[:index]
            + witness.right_signature[index + 1 :]
        )


@pytest.mark.skipif(
    os.environ.get("AEG_RUN_LR_CANONICAL_GLOBAL_COMPILATION") != "1",
    reason="opt-in exact 2,211-cell Hauffman dynamic program",
)
def test_canonical_27_wall_tree_recovers_frozen_phase9d_execution_geometry() -> None:
    compilation = _load()
    result = compilation.analyze_global_compilation()

    assert result.sign_cells == 2_211
    assert result.tasks == 81
    assert result.weighted_depth == 135
    assert result.tree_nodes == 391
    assert result.worst_depth == 10
    assert result.internal_nodes == 130
    assert result.dag_nodes == 211
    assert result.peak_frontier == 75
    assert result.widths == (1, 3, 3, 9, 27, 48, 63, 75, 66, 48, 48)
    assert result.root_coordinate == (0, 3, Fraction(4))
