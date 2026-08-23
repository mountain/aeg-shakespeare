"""Executable checks for Sonnet 001 Phase 13C."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_BASIS_VS_FULL_PROBE") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_basis_vs_full_probe.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_basis_vs_full_probe",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_second_probe_crosses_next_native_threshold():
    module = _load()
    assert module.PREVIOUS_PROBE == Fraction(48, 7)
    assert module.next_outer_threshold_after_previous_probe() == Fraction(7)
    assert module.PROBE_RMAX == Fraction(36, 5)
    assert module.PREVIOUS_PROBE < module.CRITICAL_RMAX < module.PROBE_RMAX


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 minimum-basis/full-grammar frontier probe",
)
def test_second_critical_probe_minimum_basis_remains_clean():
    module = _load()
    result = module.analyze_probe()

    assert result.rmax == Fraction(36, 5)
    assert result.symbolic_states == 20_031
    assert result.terminal_regions == 8_247
    assert result.generated_coordinates == 123
    assert result.canonical_tasks == 55
    assert result.minimum_coordinates == 54

    # The cardinality-minimum task basis itself remains clean.  Therefore the
    # richer full generated grammar is clean by containment and no fallback
    # analysis is required.
    assert result.minimum_clean
    assert result.minimum_tree_nodes == 802
    assert result.minimum_max_depth == 17
    assert result.minimum_root_coordinate == (0, 3, Fraction(5))
    assert result.minimum_obstruction_atomic is None
    assert result.full_clean
    assert not result.full_analysis_required
    assert result.full_tree_nodes == 802
    assert result.full_max_depth == 17
    assert result.full_obstruction_atomic is None
    assert result.max_event_index == 49
    assert result.max_contact_center == 8
