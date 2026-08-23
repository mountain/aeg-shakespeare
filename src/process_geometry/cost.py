"""Cost objects for process-presentation search.

Costs stay multi-axis by default. A caller may scalarize them later, but the
library does not hide trade-offs between grammar size, relation complexity,
history depth, decoder complexity, and task error.

``representation`` is intentionally not used as the formal object name here:
within the Process Geometry foundation a ``Presentation`` is the auditable,
task-sufficient realization being costed, while representation remains a broad
informal umbrella term.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class PresentationCost:
    """Multi-axis operational cost of one concrete process presentation."""

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

        Missing weights default to ``1``. Process Geometry does not prescribe
        one universal scalar objective because different tasks may value
        grammar, history, and decoding differently.
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