"""Executable checks for Sonnet 001 Phase 11C canonical task objectification."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_HUFFMAN = os.environ.get("AEG_RUN_LR_CANONICAL_TASK_HUFFMAN") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "canonical_task_objectification.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_canonical_task_objectification",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_canonical_task_projection_removes_history_only_wall_pressure():
    module = _load()
    result = module.analyze_task_objectification(include_huffman=False)

    assert result.generated_coordinates == 33
    assert result.full_certificate.task_count == 81
    assert len(result.full_certificate.minimum_coordinates) == 27

    assert result.history_free_certificate.task_count == 36
    assert len(result.history_free_certificate.minimum_coordinates) == 19

    assert result.canonical_witness.task_count == 25
    assert len(result.canonical_witness.minimum_coordinates) == 19
    assert (
        result.history_free_certificate.minimum_coordinates
        == result.canonical_witness.minimum_coordinates
    )

    assert result.mode_only.task_count == 2
    assert len(result.mode_only.minimum_coordinates) == 12

    for projection in (
        result.full_certificate,
        result.history_free_certificate,
        result.canonical_witness,
        result.mode_only,
    ):
        assert projection.full_sign_cells == 4_343
        assert len(projection.deletion_witnesses) == len(
            projection.minimum_coordinates
        )
        for witness in projection.deletion_witnesses:
            index = witness.coordinate_index
            assert witness.left_task != witness.right_task
            assert (
                witness.left_signature[:index]
                + witness.left_signature[index + 1 :]
                == witness.right_signature[:index]
                + witness.right_signature[index + 1 :]
            )

    assert result.canonical_sign_cells == 1_431
    assert result.removed_history_coordinates == (
        (1, 2, Fraction(4)),
        (1, 2, Fraction(6)),
        (1, 3, Fraction(9, 4)),
        (1, 3, Fraction(4)),
        (1, 3, Fraction(6)),
        (2, 3, Fraction(14, 9)),
        (2, 3, Fraction(4)),
        (2, 3, Fraction(6)),
    )


@pytest.mark.skipif(
    not RUN_HUFFMAN,
    reason="opt-in Sonnet 001 canonical-task Huffman calibration",
)
def test_canonical_witness_huffman_geometry_is_strictly_smaller():
    module = _load()
    result = module.analyze_task_objectification(include_huffman=True)
    huffman = result.canonical_huffman
    assert huffman is not None

    assert huffman.sign_cells == 1_431
    assert huffman.tasks == 25
    assert huffman.weighted_depth == 113
    assert huffman.tree_nodes == 94
    assert huffman.worst_depth == 7
    assert huffman.internal_nodes == 31
    assert huffman.dag_nodes == 56
    assert huffman.peak_frontier == 24
    assert huffman.widths == (1, 3, 3, 9, 18, 24, 21, 15)
    assert huffman.root_coordinate == (0, 3, Fraction(4))
