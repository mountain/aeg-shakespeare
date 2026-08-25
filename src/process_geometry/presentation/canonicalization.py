"""Compatibility path for experimental constraint canonicalization.

Use ``process_geometry.experimental.ConstraintCanonicalization`` for new code.
The implementation moved so a local H4 research slice no longer occupies the
declared Presentation namespace merely because it predates theory governance.
"""

from ..experimental.canonical_observer import ConstraintCanonicalization


__all__ = ["ConstraintCanonicalization"]
