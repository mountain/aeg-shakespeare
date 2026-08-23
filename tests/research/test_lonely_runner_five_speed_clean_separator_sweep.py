"""Executable checks for Sonnet 001 Phase 12C."""

from __future__ import annotations

from fractions import Fraction
import importlib.util
import os
from pathlib import Path
import sys

import pytest


RUN_FULL = os.environ.get("AEG_RUN_LR_FIVE_SPEED_CLEAN_SWEEP") == "1"


def _load():
    root = Path(__file__).parents[2]
    script_dir = root / "sonnet" / "lonely-runner" / "python"
    script_path = script_dir / "five_speed_clean_separator_sweep.py"
    sys.path.insert(0, str(script_dir))
    try:
        spec = importlib.util.spec_from_file_location(
            "sonnet_five_speed_clean_separator_sweep",
            script_path,
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(str(script_dir))


def test_clean_separator_sweep_module_smoke():
    module = _load()
    assert module.SWEEP == (
        Fraction(21, 4),
        Fraction(11, 2),
        Fraction(23, 4),
        Fraction(6),
        Fraction(25, 4),
    )


@pytest.mark.skipif(
    not RUN_FULL,
    reason="opt-in Sonnet 001 five-speed clean-separator domain sweep",
)
def test_clean_separator_recursion_survives_domain_widening_through_25_over_4():
    module = _load()
    results = module.analyze_sweep()

    observed = tuple(
        (
            result.rmax,
            result.symbolic_states,
            result.terminal_regions,
            result.generated_coordinates,
            result.canonical_tasks,
            result.minimum_coordinates,
            result.tree_nodes,
            result.internal_nodes,
            result.leaves,
            result.worst_depth,
            result.peak_frontier,
            result.dag_nodes,
            result.root_coordinate,
            result.max_event_index,
            result.max_contact_center,
        )
        for result in results
    )

    assert observed == (
        (
            Fraction(21, 4),
            3_397,
            1_117,
            98,
            33,
            36,
            235,
            78,
            157,
            15,
            36,
            99,
            (0, 4, Fraction(5)),
            47,
            7,
        ),
        (
            Fraction(11, 2),
            5_603,
            1_909,
            104,
            41,
            42,
            304,
            101,
            203,
            15,
            48,
            119,
            (0, 4, Fraction(5)),
            47,
            7,
        ),
        (
            Fraction(23, 4),
            7_112,
            2_491,
            105,
            41,
            42,
            304,
            101,
            203,
            15,
            48,
            122,
            (0, 4, Fraction(5)),
            47,
            7,
        ),
        (
            Fraction(6),
            12_256,
            4_405,
            107,
            42,
            43,
            316,
            105,
            211,
            15,
            48,
            122,
            (0, 4, Fraction(5)),
            47,
            7,
        ),
        (
            Fraction(25, 4),
            14_773,
            5_379,
            111,
            48,
            46,
            349,
            116,
            233,
            15,
            63,
            137,
            (0, 4, Fraction(5)),
            47,
            7,
        ),
    )
