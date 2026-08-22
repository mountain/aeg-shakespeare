"""Optional process-generated function-theory layers.

Addition/Multiplication (A/M) is the first concrete arithmetic theory.
Algebraic quotient profiles provide a second route for processes whose reduced
geometry forces elliptic/Abelian or higher-genus function languages.  The
Abelian layer then exposes canonical holomorphic differentials, history lifts,
and the global cycle data from which period/Jacobian structures can grow.
"""

from .abelian import (
    AbelianIntegralProfile,
    HyperellipticDifferential,
    abelian_integral_profile,
    holomorphic_differential_basis,
)
from .algebraic import HyperellipticProfile, hyperelliptic_profile
from .am import (
    AMFunctionTheory,
    AMPathFlow,
    AMPowerWeight,
    AMPrimitive,
    AMState,
    affine_am_frame,
)
from .module import ProcessFunctionModule, polynomial_am_module
from .periods import (
    GenusOneLattice,
    LiftedSquareRootPath,
    integrate_lifted_differential,
    lift_square_root_path,
)
from .weierstrass import WeierstrassCubicProfile, weierstrass_cubic_profile

__all__ = [
    "AbelianIntegralProfile",
    "HyperellipticDifferential",
    "abelian_integral_profile",
    "holomorphic_differential_basis",
    "HyperellipticProfile",
    "hyperelliptic_profile",
    "AMFunctionTheory",
    "AMPathFlow",
    "AMPowerWeight",
    "AMPrimitive",
    "AMState",
    "affine_am_frame",
    "ProcessFunctionModule",
    "polynomial_am_module",
    "GenusOneLattice",
    "LiftedSquareRootPath",
    "integrate_lifted_differential",
    "lift_square_root_path",
    "WeierstrassCubicProfile",
    "weierstrass_cubic_profile",
]
