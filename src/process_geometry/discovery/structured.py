"""Compatibility shim for the incubating structured-observable experiment.

The canonical owner is :mod:`process_geometry.experimental.structured_observables`.
These names preserve executable provenance for 0.0.x callers; they are omitted
from the canonical ``process_geometry.discovery.__all__`` surface.
"""

from ..experimental.structured_observables import (
    PairableAtom,
    PairingConstruction,
    PairingSpec,
    StructuredObservableProposal,
    StructuredObservableProposalResult,
    euclidean_pairing,
    generate_pairing_observables,
    nonstationary_observable_proposals,
)

# Historical 0.0.x names.
StructuredObserverProposal = StructuredObservableProposal
StructuredObserverProposalResult = StructuredObservableProposalResult
generate_pairing_observers = generate_pairing_observables
nonstationary_observer_proposals = nonstationary_observable_proposals

__all__ = [
    "PairableAtom",
    "PairingConstruction",
    "PairingSpec",
    "StructuredObservableProposal",
    "StructuredObservableProposalResult",
    "euclidean_pairing",
    "generate_pairing_observables",
    "nonstationary_observable_proposals",
    "StructuredObserverProposal",
    "StructuredObserverProposalResult",
    "generate_pairing_observers",
    "nonstationary_observer_proposals",
]
