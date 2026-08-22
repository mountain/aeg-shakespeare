"""Release-level smoke tests for the semantic public API.

The package root is a navigation surface, not a flat symbol catalog. Deeper
mathematical behavior belongs in literate tests; these checks certify namespace
shape, representative imports, and the temporary 0.0.x compatibility bridge.
"""

from importlib.metadata import version

import pytest

import aeg_shakespeare as shakespeare


def test_public_version_matches_distribution_metadata():
    assert shakespeare.__version__ == version("aeg-shakespeare")


def test_root_public_surface_is_only_the_semantic_router():
    assert shakespeare.__all__ == [
        "process",
        "presentation",
        "discovery",
        "analysis",
        "__version__",
    ]
    assert "ProcessWord" not in dir(shakespeare)
    assert "AbelianPeriodMatrix" not in dir(shakespeare)


def test_representative_namespaced_entry_points_are_importable():
    assert hasattr(shakespeare.process.history, "ProcessWord")
    assert hasattr(shakespeare.process.finite, "ProcessFamily")
    assert hasattr(shakespeare.process.finite, "ProcessCharacter")
    assert hasattr(shakespeare.process.finite, "FamilyAction")
    assert hasattr(shakespeare.process.finite, "ProcessCocycle")
    assert hasattr(shakespeare.process.local, "ProcessSystem")
    assert hasattr(shakespeare.process.local, "ProcessFrame")

    assert hasattr(shakespeare.presentation.history, "normalize_word")
    assert hasattr(shakespeare.presentation.constraints, "AlgebraicConstraintSet")
    assert hasattr(shakespeare.presentation.grammar, "discover_generated_presentation")
    assert hasattr(shakespeare.presentation.relations, "discover_relation_kernel")
    assert hasattr(shakespeare.presentation.search, "PresentationCost")
    assert hasattr(shakespeare.presentation.search, "pareto_frontier")

    assert hasattr(shakespeare.discovery, "discover_polynomial_invariants")
    assert hasattr(shakespeare.discovery, "generate_pairing_observers")
    assert hasattr(shakespeare.discovery, "search_first_order_process_quotients")

    assert hasattr(shakespeare.analysis.module, "ProcessFunctionModule")
    assert hasattr(shakespeare.analysis.am, "AMFunctionTheory")
    assert hasattr(shakespeare.analysis.algebraic, "hyperelliptic_profile")
    assert hasattr(shakespeare.analysis.abelian, "AbelianPeriodMatrix")
    assert hasattr(shakespeare.analysis.abelian, "normalized_abelian_torus")


def test_legacy_root_symbol_is_lazy_and_warns_during_transition():
    with pytest.warns(DeprecationWarning, match="legacy root-level import"):
        legacy = shakespeare.ProcessWord
    assert legacy is shakespeare.process.history.ProcessWord
