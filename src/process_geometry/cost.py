"""Cost objects for process-representation search.

Costs stay multi-axis by default.  A caller may scalarize them later, but the
library does not hide trade-offs between grammar size, relation complexity,
history depth, decoder complexity, and task error.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class PresentationCost:
    """Multi-axis cost of a process presentation."""

    grammar: float = 0.0
    relations: float = 0.0
    history: float = 0.0
    decoder: float = 0.0
    task_error: float = 0.0

    def components(self) -> Mapping[str, float]:
        return {
            "grammar": self.grammar,
            "relations": self.relations,
            "history": self.history,
            "decoder": self.decoder,
            "task_error": self.task_error,
        }

    def scalarize(self, weights: Mapping[str, float] | None = None) -> float:
        """Return a caller-controlled weighted sum.

        Missing weights default to ``1``.  Shakespeare does not prescribe one
        universal scalar objective because different tasks may value grammar,
        history, and decoding differently.
        """

        weights = weights or {}
        return sum(weights.get(name, 1.0) * value for name, value in self.components().items())

    def dominates(self, other: "PresentationCost") -> bool:
        """Whether this cost Pareto-dominates ``other``."""

        mine = tuple(self.components().values())
        theirs = tuple(other.components().values())
        return all(a <= b for a, b in zip(mine, theirs)) and any(
            a < b for a, b in zip(mine, theirs)
        )
