"""Explicit finite search budgets for process-presentation discovery."""

from dataclasses import dataclass


@dataclass(frozen=True)
class SearchBudget:
    """Finite search limits for local representation discovery.

    Bounded search is part of the presentation contract: general word/relation
    problems need not be decidable, so search limits remain explicit data.
    """

    max_history_depth: int = 8
    max_expression_degree: int = 4
    max_relation_order: int = 8
    max_new_primitives: int = 8

    def __post_init__(self) -> None:
        values = (
            self.max_history_depth,
            self.max_expression_degree,
            self.max_relation_order,
            self.max_new_primitives,
        )
        if any(value < 0 for value in values):
            raise ValueError("search-budget values must be non-negative")
