"""Release-level smoke tests for the semantic public API.

The package root is a navigation surface, not a flat symbol catalog. Deeper
mathematical behavior belongs in literate tests; these checks certify the
canonical ``process_geometry`` namespace, foundation-aligned names, and the
temporary historical alias.
"""

import importlib
from importlib.metadata import version

import pytest

import process_geometry as pg


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
    assert hasattr(pg.presentation.history, "TaskContinuationSignature")
    assert hasattr(pg.presentation.history, "task_continuation_signature")
    assert hasattr(pg.presentation.constraints, "AlgebraicConstraintSet")
    assert hasattr(pg.presentation.grammar, "discover_generated_presentation")
    assert hasattr(pg.presentation.relations, "discover_relation_kernel")
    assert hasattr(pg.presentation.search, "PresentationCost")
    assert hasattr(pg.presentation.search, "pareto_frontier")
    assert hasattr(pg.presentation.morphism, "PresentationMorphism")

    assert hasattr(pg.discovery, "discover_polynomial_invariants")
    assert hasattr(pg.discovery, "generate_pairing_observers")
    assert hasattr(pg.discovery, "ObservableAlgebraicQuotient")
    assert hasattr(pg.discovery, "discover_first_order_observable_quotient")
    assert hasattr(pg.discovery, "search_first_order_observer_presentations")

    assert hasattr(pg.analysis.module, "ProcessFunctionModule")
    assert hasattr(pg.analysis.am, "AMFunctionTheory")
    assert hasattr(pg.analysis.algebraic, "hyperelliptic_profile")
    assert hasattr(pg.analysis.abelian, "AbelianPeriodMatrix")
    assert hasattr(pg.analysis.abelian, "normalized_abelian_torus")


def test_unsettled_canonical_observer_slice_does_not_occupy_public_namespaces():
    assert "canonicalization" not in pg.presentation.__all__
    assert "connection" not in pg.analysis.__all__
    assert "decomposition" not in pg.analysis.__all__


def test_experimental_is_the_canonical_owner_of_unsettled_slices():
    import process_geometry.experimental as experimental
    from process_geometry.analysis.connection import ObserverConnection
    from process_geometry.analysis.decomposition import CanonicalDecomposition
    from process_geometry.presentation.canonicalization import (
        ConstraintCanonicalization,
    )

    assert experimental.ConstraintCanonicalization is ConstraintCanonicalization
    assert experimental.ObserverConnection is ObserverConnection
    assert experimental.CanonicalDecomposition is CanonicalDecomposition
    assert ConstraintCanonicalization.__module__ == (
        "process_geometry.experimental.canonical_observer"
    )
    assert ObserverConnection.__module__ == (
        "process_geometry.experimental.canonical_observer"
    )
    assert CanonicalDecomposition.__module__ == (
        "process_geometry.experimental.canonical_observer"
    )


def test_foundation_aligned_names_preserve_historical_backend_identity():
    assert (
        pg.presentation.history.TaskContinuationSignature
        is pg.presentation.history.ProcessJetSignature
    )
    assert (
        pg.presentation.history.task_continuation_signature
        is pg.presentation.history.process_jet_signature
    )
    assert pg.discovery.ObservableAlgebraicQuotient is pg.discovery.ObservableQuotient
    assert (
        pg.discovery.discover_first_order_observable_quotient
        is pg.discovery.discover_first_order_process_quotient
    )
    assert (
        pg.discovery.search_first_order_observer_presentations
        is pg.discovery.search_first_order_process_quotients
    )


def test_legacy_root_symbol_is_lazy_and_warns_during_transition():
    with pytest.warns(DeprecationWarning, match="legacy root-level import"):
        legacy = pg.ProcessWord
    assert legacy is pg.process.history.ProcessWord


def test_aeg_shakespeare_alias_preserves_deep_object_identity():
    import aeg_shakespeare as legacy

    # The compatibility package may already have been imported during test
    # collection. Reload it so this test validates the deprecation signal
    # deterministically rather than depending on import order.
    with pytest.warns(DeprecationWarning, match="deprecated compatibility namespace"):
        importlib.reload(legacy)

    from aeg_shakespeare.analysis.am import AMFunctionTheory as LegacyAMFunctionTheory
    from aeg_shakespeare.presentation.morphism import (
        PresentationMorphism as LegacyPresentationMorphism,
    )
    from aeg_shakespeare.process.history import ProcessWord as LegacyProcessWord

    assert legacy.process is pg.process
    assert legacy.presentation is pg.presentation
    assert legacy.discovery is pg.discovery
    assert legacy.analysis is pg.analysis
    assert LegacyProcessWord is pg.process.history.ProcessWord
    assert LegacyPresentationMorphism is pg.presentation.morphism.PresentationMorphism
    assert LegacyAMFunctionTheory is pg.analysis.am.AMFunctionTheory
