"""Physical-layout checks for completed semantic implementation moves."""

from aeg_shakespeare.central import ProcessCocycle as LegacyProcessCocycle
from aeg_shakespeare.core import (
    ProcessSystem as LegacyProcessSystem,
    ProcessWord as LegacyProcessWord,
    SearchBudget as LegacySearchBudget,
)
from aeg_shakespeare.families import ProcessFamily as LegacyProcessFamily
from aeg_shakespeare.frame import ProcessFrame as LegacyProcessFrame
from aeg_shakespeare.presentation.search import SearchBudget
from aeg_shakespeare.process.finite import ProcessCocycle, ProcessFamily
from aeg_shakespeare.process.history import ProcessWord
from aeg_shakespeare.process.local import ProcessFrame, ProcessSystem


def test_finite_process_implementations_live_under_semantic_namespace():
    assert ProcessFamily.__module__ == "aeg_shakespeare.process.finite.families"
    assert ProcessCocycle.__module__ == "aeg_shakespeare.process.finite.cocycle"


def test_core_split_objects_live_under_semantic_owners():
    assert ProcessWord.__module__ == "aeg_shakespeare.process.history"
    assert ProcessSystem.__module__ == "aeg_shakespeare.process.local.system"
    assert ProcessFrame.__module__ == "aeg_shakespeare.process.local.frame"
    assert SearchBudget.__module__ == "aeg_shakespeare.presentation.budget"


def test_pre_refactor_module_paths_are_identity_preserving_shims():
    assert LegacyProcessFamily is ProcessFamily
    assert LegacyProcessCocycle is ProcessCocycle
    assert LegacyProcessWord is ProcessWord
    assert LegacyProcessSystem is ProcessSystem
    assert LegacyProcessFrame is ProcessFrame
    assert LegacySearchBudget is SearchBudget
