"""Process-first presentation and observer discovery backends."""

from .coefficient_extension import factor_process_relation_over_extension
from .polynomial import (
    ObservableAlgebraicQuotient,
    ObservableQuotient,
    ObservableRelation,
    PolynomialInvariant,
    PolynomialInvariantDiscovery,
    PolynomialObserverBasis,
    discover_first_order_observable_quotient,
    discover_first_order_process_quotient,
    discover_observable_relations,
    discover_polynomial_invariants,
    generate_polynomial_observer_basis,
)
from .selection import (
    FirstOrderObservablePresentation,
    search_first_order_observer_presentations,
    search_first_order_process_quotients,
    structural_first_order_observer_presentation_cost,
    structural_first_order_quotient_cost,
)
from .structured import (
    PairableAtom,
    PairingConstruction,
    PairingSpec,
    StructuredObserverProposal,
    StructuredObserverProposalResult,
    euclidean_pairing,
    generate_pairing_observers,
    nonstationary_observer_proposals,
)

__all__ = [
    "factor_process_relation_over_extension",
    "ObservableAlgebraicQuotient",
    "ObservableRelation",
    "PolynomialInvariant",
    "PolynomialInvariantDiscovery",
    "PolynomialObserverBasis",
    "discover_first_order_observable_quotient",
    "discover_observable_relations",
    "discover_polynomial_invariants",
    "generate_polynomial_observer_basis",
    "FirstOrderObservablePresentation",
    "search_first_order_observer_presentations",
    "structural_first_order_observer_presentation_cost",
    "PairableAtom",
    "PairingConstruction",
    "PairingSpec",
    "StructuredObserverProposal",
    "StructuredObserverProposalResult",
    "euclidean_pairing",
    "generate_pairing_observers",
    "nonstationary_observer_proposals",
    # Historical 0.0.x backend names retained for compatibility.
    "ObservableQuotient",
    "discover_first_order_process_quotient",
    "search_first_order_process_quotients",
    "structural_first_order_quotient_cost",
]