"""Construction-history-preserving candidate primitive proposals.

These objects preserve how a possible primitive was constructed and let search
compare candidates without erasing provenance. They are deliberately
**pre-objectification**: proposal alone does not establish the semantic
stability, higher-rank free composition, or compositional rank lowering required
by the foundation notion in ``docs/44``.
"""

from ..construction import (
    PrimitiveConstruction,
    PrimitiveProposal,
    PrimitiveProposalResult,
    RejectedPrimitiveProposal,
    SymbolicOperation,
    generate_primitive_proposals,
)

__all__ = [
    "PrimitiveConstruction",
    "PrimitiveProposal",
    "PrimitiveProposalResult",
    "RejectedPrimitiveProposal",
    "SymbolicOperation",
    "generate_primitive_proposals",
]