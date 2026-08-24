"""Pre-execution invariants for the frozen depth-three enlargement."""

import importlib.util
from pathlib import Path
import sys


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet/stochastic-feedback-trap-first-passage/phase1_presentation_census.py"
)
SPEC = importlib.util.spec_from_file_location("stochastic_trap_phase1b", MODULE_PATH)
assert SPEC and SPEC.loader
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


def test_depth_three_literal_bound_is_frozen_without_materialization():
    counts = module.literal_depth_counts(3)

    assert counts == (4, 20, 580, 364_820)
    assert sum(counts) == 365_424


def test_semantic_closure_reproduces_the_frozen_depth_two_baseline():
    semantic = module.semantic_am_grammar(2)
    census = module.depth_two_presentation_census()

    assert semantic == census.semantic_presentations
    assert len(semantic) == 60
