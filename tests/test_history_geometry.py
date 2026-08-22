import math

import pytest

from aeg_shakespeare.presentation.history import (
    boundary_profile,
    history_depth,
    huffman_prefix_code,
)
from aeg_shakespeare.process.history import ProcessWord


def test_history_depth_is_process_depth_and_can_be_weighted():
    history = ProcessWord(("A", "B", "A"))
    assert history_depth(history) == 3.0
    assert history_depth(history, {"A": 2.0, "B": 3.0}) == 7.0


def test_boundary_profile_counts_prefix_frontiers_without_assuming_quotients():
    histories = (
        ProcessWord(("A", "A")),
        ProcessWord(("A", "B")),
        ProcessWord(("B", "A")),
    )
    profile = boundary_profile(histories)
    assert profile.widths == (1, 2, 3)
    assert profile.information_widths == (0.0, 1.0, math.log2(3))
    assert profile.peak_width == 3


def test_boundary_profile_accepts_external_relation_or_task_quotient_keys():
    histories = (
        ProcessWord(("A", "A")),
        ProcessWord(("A", "B")),
        ProcessWord(("B", "A")),
    )

    def quotient_key(word):
        if not word.steps:
            return "root"
        # Calibration only: suppose the chosen task distinguishes a prefix only
        # by its most recent process step.
        return word.steps[-1]

    profile = boundary_profile(histories, quotient_key=quotient_key)
    assert profile.widths == (1, 2, 2)


def test_huffman_strategy_turns_boundary_weight_into_depth_geometry():
    weights = {"a": 0.5, "b": 0.25, "c": 0.125, "d": 0.125}
    code = huffman_prefix_code(weights)
    metrics = code.metrics()

    assert code.is_prefix_free()
    assert sorted(len(code.codes[symbol]) for symbol in weights) == [1, 2, 3, 3]
    assert metrics.expected_depth == pytest.approx(1.75)
    assert metrics.worst_depth == 3
    assert metrics.kraft_sum == pytest.approx(1.0)
    assert metrics.entropy == pytest.approx(1.75)
    assert metrics.redundancy == pytest.approx(0.0)


def test_huffman_symbols_can_be_literal_process_histories():
    h1 = ProcessWord(("A",))
    h2 = ProcessWord(("B", "A"))
    h3 = ProcessWord(("B", "B"))
    code = huffman_prefix_code({h1: 4.0, h2: 2.0, h3: 1.0})

    message = (h1, h3, h2, h1)
    encoded = code.encode(message)
    assert code.decode(encoded) == message


def test_huffman_does_not_accept_invalid_measures():
    with pytest.raises(ValueError):
        huffman_prefix_code({})
    with pytest.raises(ValueError):
        huffman_prefix_code({"a": 0.0, "b": 0.0})
    with pytest.raises(ValueError):
        huffman_prefix_code({"a": -1.0, "b": 2.0})
