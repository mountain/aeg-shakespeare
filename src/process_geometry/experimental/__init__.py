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

__all__ = [
    "DistinguishingContinuation",
    "FiniteTaskQuotient",
    "minimize_finite_task_process",
]
