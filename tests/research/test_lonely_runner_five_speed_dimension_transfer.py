"""Executable checks for Sonnet 001 Phase 12A."""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_FIVE_SPEED_TRANSFER") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_dimension_transfer.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_dimension_transfer",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_five_speed_transfer_module_and_nontrivial_threshold_smoke():
    module = _load()
    assert module.K == 5
    assert module.DELTA.numerator == 1 and module.DELTA.denominator == 6
    assert module.RMAX > 5
    assert module.RMAX < 6


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 five-speed dimension-transfer calibration",
)
def test_five_speed_canonical_transfer_and_static_materialization_red_team():
    module = _load()
    result = module.analyze_five_speed_transfer(include_static_cells=True)

    assert result.symbolic_states == 3_397
    assert result.terminal_regions == 1_117
    assert result.max_event_index == 47
    assert result.max_contact_center == 7
    assert result.generated_coordinates == 98

    assert result.full_certificate.task_count == 154
    assert len(result.full_certificate.minimum_coordinates) == 86

    assert result.history_free_certificate.task_count == 63
    assert len(result.history_free_certificate.minimum_coordinates) == 36

    assert result.canonical_witness.task_count == 33
    assert len(result.canonical_witness.minimum_coordinates) == 36
    assert (
        result.history_free_certificate.minimum_coordinates
        == result.canonical_witness.minimum_coordinates
    )

    assert result.mode_only.task_count == 2
    assert len(result.mode_only.minimum_coordinates) == 27

    assert result.canonical_sign_cells == 69_683
