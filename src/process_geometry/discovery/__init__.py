"""Process-first presentation and observer discovery backends."""

from .coefficient_extension import factor_process_relation_over_extension
from .polynomial import (
    ObservableQuotient,
    ObservableRelation,
    PolynomialInvariant,
    PolynomialInvariantDiscovery,
    PolynomialObserverBasis,
    discover_first_order_process_quotient,
    discover_observable_relations,
    discover_polynomial_invariants,
    generate_polynomial_observer_basis,
)
from .selection import (
    FirstOrderObservablePresentation,
    search_first_order_process_quotients,
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

# Foundation-aligned canonical vocabulary.  The polynomial backend computes an
# algebraic image/closure of chosen observables; it is not the history/task
# quotient H(P)/~_Q of docs/42--43.  Retain historical backend names as aliases
# during the 0.0.x transition rather than conflating those two quotient notions.
ObservableAlgebraicQuotient = ObservableQuotient
discover_first_order_observable_quotient = discover_first_order_process_quotient
search_first_order_observer_presentations = search_first_order_process_quotients
structural_first_order_observer_presentation_cost = structural_first_order_quotient_cost

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
    # Historical backend names retained for compatibility.
    "ObservableQuotient",
    "discover_first_order_process_quotient",
    "search_first_order_process_quotients",
    "structural_first_order_quotient_cost",
]