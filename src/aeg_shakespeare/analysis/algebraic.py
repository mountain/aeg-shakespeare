"""Algebraic quotient profiles used to select richer function languages."""

from ..function_theory.algebraic import HyperellipticProfile, hyperelliptic_profile
from ..function_theory.weierstrass import WeierstrassCubicProfile, weierstrass_cubic_profile

__all__ = [
    "HyperellipticProfile",
    "hyperelliptic_profile",
    "WeierstrassCubicProfile",
    "weierstrass_cubic_profile",
]
