"""Compatibility shim for the pre-refactor central-residual module path.

New code should import finite process cocycles from
``aeg_shakespeare.process.finite``.  The implementation now physically lives
under that semantic namespace.
"""

from .process.finite.cocycle import (
    CocycleVerification,
    ProcessCocycle,
    central_commutator_residual,
    verify_process_cocycle,
)

__all__ = [
    "ProcessCocycle",
    "CocycleVerification",
    "verify_process_cocycle",
    "central_commutator_residual",
]
