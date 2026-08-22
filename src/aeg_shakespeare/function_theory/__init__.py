"""Optional process-generated function-theory layers.

Addition/Multiplication (A/M) is the first concrete arithmetic theory.
Algebraic quotient profiles provide a second route for processes whose reduced
geometry forces elliptic/Abelian or higher-genus function languages. The
Abelian layer then exposes canonical holomorphic differentials, history lifts,
cycle intersections, branch-cut cycle constructions, period data, and finally
normalized history coordinates modulo the measured period lattice.
"""

from .abel_jacobi import (
    AbelJacobiHistoryIncrement,
    NormalizedAbelianTorus,
    abel_jacobi_history_increment,
    normalized_abelian_torus,
)
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
from .intersection import (
    LiftedCycleIntersection,
    SampledIntersectionForm,
    SampledRiemannProfile,
    canonical_symplectic_form,
    lifted_path_intersections,
    sampled_intersection_form,
    sampled_intersection_number,
    sampled_riemann_profile,
)
from .module import ProcessFunctionModule, polynomial_am_module
from .period_matrix import AbelianCycleSystem, AbelianPeriodMatrix, compute_period_matrix
from .periods import (
    GenusOneLattice,
    LiftedSquareRootPath,
    integrate_lifted_differential,
    lift_square_root_path,
)
from .real_branch_cycles import (
    ConstructedRealBranchCycles,
    RealBranchCutPresentation,
    RealBranchCycleSpec,
    construct_real_branch_cycles,
    real_branch_cut_presentation,
)
from .weierstrass import WeierstrassCubicProfile, weierstrass_cubic_profile

__all__ = [
    "AbelJacobiHistoryIncrement",
    "NormalizedAbelianTorus",
    "abel_jacobi_history_increment",
    "normalized_abelian_torus",
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
    "LiftedCycleIntersection",
    "SampledIntersectionForm",
    "SampledRiemannProfile",
    "canonical_symplectic_form",
    "lifted_path_intersections",
    "sampled_intersection_form",
    "sampled_intersection_number",
    "sampled_riemann_profile",
    "ProcessFunctionModule",
    "polynomial_am_module",
    "AbelianCycleSystem",
    "AbelianPeriodMatrix",
    "compute_period_matrix",
    "GenusOneLattice",
    "LiftedSquareRootPath",
    "integrate_lifted_differential",
    "lift_square_root_path",
    "ConstructedRealBranchCycles",
    "RealBranchCutPresentation",
    "RealBranchCycleSpec",
    "construct_real_branch_cycles",
    "real_branch_cut_presentation",
    "WeierstrassCubicProfile",
    "weierstrass_cubic_profile",
]
