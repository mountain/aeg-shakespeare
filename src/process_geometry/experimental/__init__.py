"""Incubating Process Geometry abstractions with no compatibility promise.

Experimental code tests parts of ``docs/THEORY_MAP.md`` that have not earned a
Public API commitment. Symbols in this namespace may be renamed, split, moved,
or rejected as the theory changes.
"""

from .finite_task_quotient import (
    DistinguishingContinuation,
    FiniteTaskQuotient,
    minimize_finite_task_process,
)
from .canonical_observer import (
    CanonicalDecomposition,
    ConstraintCanonicalization,
    ObserverConnection,
)
from .structured_observables import (
    PairableAtom,
    PairingConstruction,
    PairingSpec,
    StructuredObservableProposal,
    StructuredObservableProposalResult,
    euclidean_pairing,
    generate_pairing_observables,
    nonstationary_observable_proposals,
)

__all__ = [
    "DistinguishingContinuation",
    "FiniteTaskQuotient",
    "minimize_finite_task_process",
    "ConstraintCanonicalization",
    "ObserverConnection",
    "CanonicalDecomposition",
    "PairableAtom",
    "PairingConstruction",
    "PairingSpec",
    "StructuredObservableProposal",
    "StructuredObservableProposalResult",
    "euclidean_pairing",
    "generate_pairing_observables",
    "nonstationary_observable_proposals",
]
