"""Finite process presentations: histories, grammars, relations, and search.

Exact task quotients and local canonical-observer slices remain under
``process_geometry.experimental`` until their broader semantics mature.
"""

from . import (
    constraints,
    construction,
    grammar,
    history,
    morphism,
    relations,
    search,
)

__all__ = [
    "history",
    "construction",
    "constraints",
    "grammar",
    "relations",
    "search",
    "morphism",
]
