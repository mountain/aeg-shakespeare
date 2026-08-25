"""Compatibility path for experimental canonical decomposition.

Use ``process_geometry.experimental.CanonicalDecomposition`` for new code.
"""

from ..experimental.canonical_observer import CanonicalDecomposition


__all__ = ["CanonicalDecomposition"]
