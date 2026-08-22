"""Release-level smoke tests for the installable public API.

This file is deliberately shallow. Deeper mathematical behavior belongs in the
literate unit/classical/research tests; release smoke tests answer a narrower
question: does the package expose a small coherent toolkit that an external user
can import without relying on repository internals?
"""

from importlib.metadata import version

import aeg_shakespeare as shakespeare


def test_public_version_matches_distribution_metadata():
    assert shakespeare.__version__ == version("aeg-shakespeare")


def test_representative_public_entry_points_are_importable():
    required = (
        "ProcessWord",
        "ProcessSystem",
        "ProcessFrame",
        "SearchBudget",
        "AlgebraicConstraintSet",
        "PresentationCost",
        "PolynomialObserverBasis",
        "discover_polynomial_invariants",
        "discover_first_order_process_quotient",
        "search_first_order_process_quotients",
        "PairableAtom",
        "PairingSpec",
        "generate_pairing_observers",
        "factor_process_relation_over_extension",
        "AMFunctionTheory",
        "hyperelliptic_profile",
        "AbelianIntegralProfile",
        "LiftedSquareRootPath",
        "AbelianPeriodMatrix",
        "compute_period_matrix",
        "generate_primitive_proposals",
        "discover_generated_presentation",
        "pareto_frontier",
    )
    for name in required:
        assert hasattr(shakespeare, name), name
