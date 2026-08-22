"""Physical-layout checks for completed semantic implementation moves."""

from aeg_shakespeare.central import ProcessCocycle as LegacyProcessCocycle
from aeg_shakespeare.families import ProcessFamily as LegacyProcessFamily
from aeg_shakespeare.process.finite import ProcessCocycle, ProcessFamily


def test_finite_process_implementations_live_under_semantic_namespace():
    assert ProcessFamily.__module__ == "aeg_shakespeare.process.finite.families"
    assert ProcessCocycle.__module__ == "aeg_shakespeare.process.finite.cocycle"


def test_pre_refactor_module_paths_are_identity_preserving_shims():
    assert LegacyProcessFamily is ProcessFamily
    assert LegacyProcessCocycle is ProcessCocycle
