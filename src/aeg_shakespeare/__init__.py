"""AEG Shakespeare: process-presentation discovery experiments."""

from .affine import Add, AffineNormalForm, Scale, normalize_affine_history
from .core import ProcessSystem, homogeneous_monomials
from .linear import KrylovReturnRelation, discover_krylov_relation
from .relations import (
    ReturnRelation,
    ReturnSector,
    action_matrix,
    decompose,
    discover_quadratic_return_sectors,
    discover_return_relation,
)

__all__ = [
    "Add",
    "AffineNormalForm",
    "Scale",
    "normalize_affine_history",
    "ProcessSystem",
    "homogeneous_monomials",
    "KrylovReturnRelation",
    "discover_krylov_relation",
    "ReturnRelation",
    "ReturnSector",
    "action_matrix",
    "decompose",
    "discover_quadratic_return_sectors",
    "discover_return_relation",
]

__version__ = "0.1.0a1"
