"""Research-local scale and chart compiler prototype.

This package deliberately exposes a small surface.  It is not a public API.
"""

from .balance import (
    BalanceError,
    BalanceBudget,
    BalanceResult,
    infer_distinguished_scaling,
)
from .compiler import CompilationReport, compile_expression
from .ir import Add, Const, Exp, Expr, Log, Mul, Pow, Var, exp, log
from .reporting import balance_summary, compilation_summary
from .scale import Obligation, Observer, Residual, Scale, Series, VisibilityEvent

__all__ = [
    "Add",
    "BalanceError",
    "BalanceBudget",
    "BalanceResult",
    "CompilationReport",
    "Const",
    "Exp",
    "Expr",
    "Log",
    "Mul",
    "Obligation",
    "Observer",
    "Pow",
    "Residual",
    "Scale",
    "Series",
    "Var",
    "VisibilityEvent",
    "compile_expression",
    "compilation_summary",
    "exp",
    "infer_distinguished_scaling",
    "log",
    "balance_summary",
]
