"""Experimental evidence record for canonical process decomposition.

The AEG Analysis working principle separates a local process correction into
three roles before any representation is enlarged:

    renormalizable + resonant/transport + completion.

This module deliberately does not prescribe how those parts are discovered.
Riccati Lie directions, Kepler function modes, and future discrete/history
calibrations need different decomposition backends.  The reusable object only
records the three claimed parts together with caller-defined evidence, following
the same evidence-bearing discipline as ``PresentationMorphism``.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

SourceT = TypeVar("SourceT")
PartT = TypeVar("PartT")
CertificateT = TypeVar("CertificateT")


@dataclass(frozen=True)
class CanonicalDecomposition(Generic[SourceT, PartT, CertificateT]):
    """A claimed local split into renormalize / transport / complete sectors."""

    source: SourceT
    renormalizable: PartT
    resonant: PartT
    completion: PartT
    certificate: CertificateT
    label: str = ""


__all__ = ["CanonicalDecomposition"]
