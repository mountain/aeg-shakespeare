"""Compatibility path for the experimental observer-connection record.

Use ``process_geometry.experimental.ObserverConnection`` for new code.
"""

from ..experimental.canonical_observer import ObserverConnection


__all__ = ["ObserverConnection"]
