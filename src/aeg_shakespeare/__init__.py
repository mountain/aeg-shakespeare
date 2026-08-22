"""AEG Shakespeare: process-representation discovery library."""

from .core import (
    ProcessSystem,
    ProcessWord,
    SearchBudget,
    homogeneous_monomials,
    interpret_history,
)
from .cost import PresentationCost
from .grammar import (
    GeneratedGrammar,
    GeneratedPresentation,
    discover_generated_grammar,
    discover_generated_presentation,
)
from .linear import KrylovReturnRelation, discover_krylov_relation
from .relations import (
    ProcessPolynomialRelation,
    RelationDecomposition,
    RelationKernel,
    ReturnRelation,
    action_matrix,
    coefficient_vector,
    decompose,
    discover_operator_relation,
    discover_relation_decomposition,
    discover_relation_kernel,
    discover_return_relation,
    factor_process_relation,
)
from .rewrite import (
    RewriteResult,
    RewriteStep,
    WordRewriteRule,
    normalize_word,
    rewrite_once,
)

__all__ = [
    "ProcessSystem",
    "ProcessWord",
    "SearchBudget",
    "homogeneous_monomials",
    "interpret_history",
    "PresentationCost",
    "GeneratedGrammar",
    "GeneratedPresentation",
    "discover_generated_grammar",
    "discover_generated_presentation",
    "KrylovReturnRelation",
    "discover_krylov_relation",
    "ProcessPolynomialRelation",
    "RelationDecomposition",
    "RelationKernel",
    "ReturnRelation",
    "action_matrix",
    "coefficient_vector",
    "decompose",
    "discover_operator_relation",
    "discover_relation_decomposition",
    "discover_relation_kernel",
    "discover_return_relation",
    "factor_process_relation",
    "RewriteResult",
    "RewriteStep",
    "WordRewriteRule",
    "normalize_word",
    "rewrite_once",
]

__version__ = "0.0.1"
