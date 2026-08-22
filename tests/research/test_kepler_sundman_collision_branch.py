"""Kepler collision: a physical singularity becomes a regular branch history.

Question
--------
Can Shakespeare represent a genuine mechanical collision singularity by a
process presentation whose local evolution remains regular, while the hidden
incoming/outgoing information is carried by branch history rather than by an
infinitesimal physical-time step?

Primitive data
--------------
For the planar Kepler problem with gravitational parameter ``k`` and fixed
energy ``E``, introduce Sundman time by

    dt = r d tau.

Writing ``Y = dr/dtau``, the fixed-energy radial equation becomes the regular
linear process

    D r = Y,
    D Y = 2 E r + k.

No Kepler conic, eccentric anomaly, collision-reflection rule, or square-root
branch convention is supplied to invariant discovery.

Classical lineage
-----------------
The Sundman transformation was introduced to regularize collision singularities
and, for fixed Kepler energy, converts the radial equation to a linear equation
with constant coefficients. In the notation used here its first integral is

    Y^2 - 2 E r^2 - 2 k r = -ell^2,

where ``ell`` is angular momentum. See [Carinena-Martinez-MunozLecanda-2022],
Section 2, especially equations (2.1)--(2.8).

For the radial collision sector ``ell=0`` and negative energy, the regularized
curve has the form

    Y^2 = 2 r (k + E r).

The collision ``r=0`` is a simple branch point of the projection to visible
radius. The algebraic curve itself is smooth there; the two signs of ``Y`` are
the incoming and outgoing histories. Physical velocity is reconstructed as

    dr/dt = Y/r,

which diverges at collision because ``dt/dtau=r`` vanishes.

Shakespeare reconstruction
---------------------------
The Discovery layer receives only the regularized process generator and a
degree-two polynomial budget. It must discover the first-integral direction
before the angular-momentum leaf is named. After adjoining the leaf value, the
same first-order quotient machinery emits the branch curve.

A sampled loop around the collision branch point then tests the existing
square-root history lift. The visible radius loop closes, but the lifted sign of
``Y`` changes. A second traversal would close the lift, exactly as in the basic
monodromy calibration.

**Shakespeare interpretation.** In this restricted Kepler sector, collision is
not a singular point of the regularized process curve. The singularity belongs
to the physical-time reconstruction, while the incoming/outgoing distinction is
a residual of lifted process history over the radius projection.

Calibration statement
---------------------
Passing this file certifies that:

1. bounded polynomial discovery recovers the Sundman first integral without an
   invariant template;
2. the angular-momentum leaf eliminates to the exact radial branch curve;
3. in the zero-angular-momentum bound sector the collision point is smooth on
   the regularized algebraic curve;
4. physical radial velocity nevertheless diverges there under reconstruction;
5. one loop around the collision radius flips the lifted sheet.

This is not yet a three-body collision integrator and it does not prove a global
symplectic regularization theorem. It is the smallest singular-Hamiltonian test
in which exact discovery, time re-presentation, branch geometry, and history
monodromy all meet in one executable argument.

References
----------
[Carinena-Martinez-MunozLecanda-2022] J. F. Carinena, E. Martinez, and
M. C. Munoz-Lecanda, "Infinitesimal Time Reparametrisation and Its
Applications," *Journal of Nonlinear Mathematical Physics* 29 (2022), 523--555.
DOI: 10.1007/s44198-022-00037-w.
"""

import cmath
import math

import sympy as sp

from aeg_shakespeare.analysis.abelian import lift_square_root_path
from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile
from aeg_shakespeare.discovery import (
    discover_first_order_process_quotient,
    discover_polynomial_invariants,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def sampled_circle(center: complex, radius: float, *, samples: int):
    return tuple(
        center + radius * cmath.exp(2j * math.pi * index / samples)
        for index in range(samples + 1)
    )


def sundman_kepler_process():
    r, y, E, k = sp.symbols("r y E k")
    system = ProcessSystem(
        (r, y),
        {
            r: y,
            y: 2 * E * r + k,
        },
        name="D_tau",
    )
    return r, y, E, k, system


def test_kepler_collision_becomes_regular_branch_history():
    r, y, E, k, system = sundman_kepler_process()

    discovery = discover_polynomial_invariants(system, max_degree=2)
    assert len(discovery.invariants) == 1
    invariant = discovery.invariants[0]
    assert invariant.certified

    expected_invariant = sp.expand(y**2 - 2 * E * r**2 - 2 * k * r)
    invariant_ratio = sp.cancel(invariant.expression / expected_invariant)
    assert invariant_ratio != 0
    assert not invariant_ratio.free_symbols

    L2, R, Y = sp.symbols("L2 R Y")
    leaf = AlgebraicConstraintSet(
        (r, y, E, k, L2),
        (invariant.expression + L2,),
    )
    quotient = discover_first_order_process_quotient(
        system,
        r,
        observable_symbol=R,
        derivative_symbol=Y,
        constraints=leaf,
        parameters=(E, k, L2),
    )

    assert quotient.complete_certificates
    assert len(quotient.relations) == 1
    discovered_relation = quotient.relations[0].relation
    expected_polynomial = sp.expand(2 * E * R**2 + 2 * k * R - L2)
    expected_relation = sp.expand(Y**2 - expected_polynomial)
    relation_ratio = sp.cancel(discovered_relation / expected_relation)
    assert relation_ratio != 0
    assert not relation_ratio.free_symbols

    generic_profile = hyperelliptic_profile(R, Y, expected_polynomial)
    assert generic_profile.degree == 2
    assert generic_profile.generic_genus == 0

    # Radial bound collision calibration: E=-1, k=1, ell=0.
    collision_polynomial = 2 * R * (1 - R)
    collision_curve = hyperelliptic_profile(R, Y, collision_polynomial)
    assert collision_curve.discriminant != 0

    # The regularized curve F(R,Y)=0 is smooth at the collision point (0,0).
    F = sp.expand(Y**2 - collision_polynomial)
    gradient_at_collision = (
        sp.diff(F, R).subs({R: 0, Y: 0}),
        sp.diff(F, Y).subs({R: 0, Y: 0}),
    )
    assert gradient_at_collision != (0, 0)

    # Physical-time reconstruction is singular even though D_tau is regular.
    physical_speed_outgoing = sp.sqrt(collision_polynomial) / R
    assert sp.limit(physical_speed_outgoing, R, 0, dir="+") == sp.oo
    assert system.rules[y].subs({r: 0, E: -1, k: 1}) == 1

    # The collision radius is a branch point of the visible-radius projection.
    loop = sampled_circle(0j, 0.2, samples=512)
    lifted = lift_square_root_path(collision_curve, loop)
    assert lifted.base_closed
    assert not lifted.lifted_closed
    assert lifted.sheet_multiplier == -1
    assert abs(lifted.y_values[-1] + lifted.y_values[0]) < 1e-10
