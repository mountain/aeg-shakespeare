"""Executable checks for the frozen static-observer S2 no-go result."""

import importlib
from pathlib import Path
import sys

import pytest


SONNET_PATH = Path(__file__).parents[2] / "sonnet" / "hidden-am-noether"
sys.path.insert(0, str(SONNET_PATH))
phase1 = importlib.import_module("phase1_s1_census")
phase2 = importlib.import_module("phase2_static_observer_no_go")


def test_static_product_affine_observers_preserve_stabilizer_dimension():
    frontier, observers, failures = phase2.frozen_s2_static_observer_census()

    assert len(frontier) == 166
    assert len(observers) == 3
    assert failures == ()
    assert all(phase2.stabilizer_dimension(expression) == 0 for expression in frontier)


def test_no_go_has_visible_symmetry_positive_control():
    x = phase1.X
    observed = phase2.product_affine_observe(
        x, x_scale=2, x_shift=1, y_scale=3, y_shift=-1
    )

    assert phase2.stabilizer_dimension(x) == phase2.stabilizer_dimension(observed)
    assert phase2.stabilizer_dimension(x) > 0


def test_noninvertible_observer_is_rejected_not_used_to_fake_symmetry():
    with pytest.raises(ValueError, match="invertible"):
        phase2.product_affine_observe(
            phase1.X * phase1.Y,
            x_scale=0,
            x_shift=0,
            y_scale=1,
            y_shift=0,
        )

