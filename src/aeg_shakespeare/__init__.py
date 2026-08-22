"""AEG Shakespeare: process-representation discovery library."""

from .core import (
    ProcessSystem,
    ProcessWord,
    SearchBudget,
    homogeneous_monomials,
    interpret_history,
)
from .cost import PresentationCost
from .linear import KrylovReturnRelation, discover_krylov_relation
from .relations import (
    RelationKernel,
    ReturnRelation,
    action_matrix,
    coefficient_vector,
    decompose,
    discover_relation_kernel,
    discover_return_relation,
)

__all__ = [
    "ProcessSystem",
    "ProcessWord",
    "SearchBudget",
    "homogeneous_monomials",
    "interpret_history",
    "PresentationCost",
    "KrylovReturnRelation",
    "discover_krylov_relation",
    "RelationKernel",
    "ReturnRelation",
    "action_matrix",
    "coefficient_vector",
    "decompose",
    "discover_relation_kernel",
    "discover_return_relation",
]

__version__ = "0.0.1"
