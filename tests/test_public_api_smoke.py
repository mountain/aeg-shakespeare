"""Release-level smoke tests for the semantic public API.

The package root is a navigation surface, not a flat symbol catalog. Deeper
mathematical behavior belongs in literate tests; these checks certify namespace
shape, representative imports, and the temporary 0.0.x compatibility bridge.
"""

from importlib.metadata import version

import pytest

import aeg_shakespeare as pg


def test_public_version_matches_distribution_metadata():
    assert pg.__version__ == version("process-geometry")


def test_root_public_surface_is_only_the_semantic_router():
    assert pg.__all__ == [
        "process",
        "presentation",
        "discovery",
        "analysis",
        "__version__",
    ]
    assert "ProcessWord" not in dir(pg)
    assert "AbelianPeriodMatrix" not in dir(pg)


def test_representative_namespaced_entry_points_are_importable():
    assert hasattr(pg.process.history, "ProcessWord")
    assert hasattr(pg.process.finite, "ProcessFamily")
    assert hasattr(pg.process.finite, "ProcessCharacter")
    assert hasattr(pg.process.finite, "FamilyAction")
    assert hasattr(pg.process.finite, "ProcessCocycle")
    assert hasattr(pg.process.local, "ProcessSystem")
    assert hasattr(pg.process.local, "ProcessFrame")

    assert hasattr(pg.presentation.history, "normalize_word")
    assert hasattr(pg.presentation.constraints, "AlgebraicConstraintSet")
    assert hasattr(pg.presentation.grammar, "discover_generated_presentation")
    assert hasattr(pg.presentation.relations, "discover_relation_kernel")
    assert hasattr(pg.presentation.search, "PresentationCost")
    assert hasattr(pg.presentation.search, "pareto_frontier")
    assert hasattr(pg.presentation.morphism, "PresentationMorphism")

    assert hasattr(pg.discovery, "discover_polynomial_invariants")
    assert hasattr(pg.discovery, "generate_pairing_observers")
    assert hasattr(pg.discovery, "search_first_order_process_quotients")

    assert hasattr(pg.analysis.module, "ProcessFunctionModule")
    assert hasattr(pg.analysis.am, "AMFunctionTheory")
    assert hasattr(pg.analysis.algebraic, "hyperelliptic_profile")
    assert hasattr(pg.analysis.abelian, "AbelianPeriodMatrix")
    assert hasattr(pg.analysis.abelian, "normalized_abelian_torus")


def test_legacy_root_symbol_is_lazy_and_warns_during_transition():
    with pytest.warns(DeprecationWarning, match="legacy root-level import"):
        legacy = pg.ProcessWord
    assert legacy is pg.process.history.ProcessWord
