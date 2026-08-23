"""Physical-layout checks for completed semantic implementation moves."""

from process_geometry.central import ProcessCocycle as LegacyProcessCocycle
from process_geometry.core import (
    ProcessSystem as LegacyProcessSystem,
    ProcessWord as LegacyProcessWord,
    SearchBudget as LegacySearchBudget,
)
from process_geometry.families import ProcessFamily as LegacyProcessFamily
from process_geometry.frame import ProcessFrame as LegacyProcessFrame
from process_geometry.presentation.search import SearchBudget
from process_geometry.process.finite import ProcessCocycle, ProcessFamily
from process_geometry.process.history import ProcessWord
from process_geometry.process.local import ProcessFrame, ProcessSystem


def test_finite_process_implementations_live_under_semantic_namespace():
    assert ProcessFamily.__module__ == "process_geometry.process.finite.families"
    assert ProcessCocycle.__module__ == "process_geometry.process.finite.cocycle"


def test_core_split_objects_live_under_semantic_owners():
    assert ProcessWord.__module__ == "process_geometry.process.history"
    assert ProcessSystem.__module__ == "process_geometry.process.local.system"
    assert ProcessFrame.__module__ == "process_geometry.process.local.frame"
    assert SearchBudget.__module__ == "process_geometry.presentation.budget"


def test_pre_refactor_module_paths_are_identity_preserving_shims():
    assert LegacyProcessFamily is ProcessFamily
    assert LegacyProcessCocycle is ProcessCocycle
    assert LegacyProcessWord is ProcessWord
    assert LegacyProcessSystem is ProcessSystem
    assert LegacyProcessFrame is ProcessFrame
    assert LegacySearchBudget is SearchBudget
