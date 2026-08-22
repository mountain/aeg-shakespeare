"""Square-root monodromy: a closed base loop can leave a history open upstairs.

Question
--------
Can Shakespeare make the distinction ``state return != history return``
executable in the simplest nontrivial branched covering, before any elliptic or
higher-genus machinery is invoked?

Primitive data
--------------
We use only the algebraic relation

    y^2 = x^2 - 1,

whose branch points in the x-plane are x=+1 and x=-1, together with sampled
closed loops in the punctured x-plane.  No monodromy permutation is supplied as
input.  The lift is chosen incrementally by continuity of the square root.

Classical lineage
-----------------
The square root over the punctured plane is the elementary prototype of analytic
continuation and monodromy.  Encircling one simple branch point exchanges the
two sheets; encircling both branch points has even branch parity and returns to
the original sheet.  This is standard covering/Riemann-surface material; see
[Forster-1981] and [Farkas-Kra-1992].

Shakespeare reconstruction
---------------------------
The base path records only x.  ``lift_square_root_path`` carries the additional
history needed to choose y continuously.  The endpoint of the base loop may
therefore equal its start while the lifted endpoint differs by the deck
transformation y -> -y.

**Shakespeare interpretation.**  The sign change is read as a residual of
process history after the visible state x has returned.  The classical theorem
is monodromy of the square-root cover; the 'history residual' terminology is the
project's reinterpretation.

Calibration statement
---------------------
This file certifies numerically, with increasingly fine sampled loops, that:

1. one turn around exactly one branch point has sheet multiplier -1;
2. one turn around both branch points has sheet multiplier +1;
3. two turns around one branch point have sheet multiplier +1.

Thus a closed base history need not be a closed lifted history.

Proof map
---------
``test_one_branch_point_flips_the_sheet`` checks item 1.
``test_two_branch_points_cancel_the_sheet_flip`` checks item 2.
``test_two_turns_close_the_lift`` checks item 3.

Boundary
--------
These tests do not compute a homology basis or a period.  They also do not give
rigorous a-posteriori error bounds for the discrete continuation algorithm.  The
loops are chosen far from branch points and sampled densely enough that the two
candidate square roots remain well separated.

References
----------
[Forster-1981] O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981,
chapters on analytic continuation and covering surfaces.
DOI: 10.1007/978-1-4612-5961-9.

[Farkas-Kra-1992] H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed.,
Springer, 1992, chapters on branched coverings and algebraic functions.
DOI: 10.1007/978-1-4612-2034-3.
"""

import cmath
import math

import sympy as sp

from aeg_shakespeare.analysis.abelian import lift_square_root_path
from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile


def sampled_circle(center: complex, radius: float, *, turns: int, samples: int):
    return tuple(
        center + radius * cmath.exp(2j * math.pi * turns * index / samples)
        for index in range(samples + 1)
    )


def square_root_cover():
    x, y = sp.symbols("x y")
    return hyperelliptic_profile(x, y, x**2 - 1)


def test_one_branch_point_flips_the_sheet():
    curve = square_root_cover()
    loop = sampled_circle(1.0 + 0j, 0.25, turns=1, samples=512)

    lifted = lift_square_root_path(curve, loop)

    assert lifted.base_closed
    assert not lifted.lifted_closed
    assert lifted.sheet_multiplier == -1
    assert abs(lifted.y_values[-1] + lifted.y_values[0]) < 1e-10


def test_two_branch_points_cancel_the_sheet_flip():
    curve = square_root_cover()
    loop = sampled_circle(0j, 2.0, turns=1, samples=768)

    lifted = lift_square_root_path(curve, loop)

    assert lifted.base_closed
    assert lifted.lifted_closed
    assert lifted.sheet_multiplier == 1
    assert abs(lifted.y_values[-1] - lifted.y_values[0]) < 1e-10


def test_two_turns_close_the_lift():
    curve = square_root_cover()
    loop = sampled_circle(1.0 + 0j, 0.25, turns=2, samples=1024)

    lifted = lift_square_root_path(curve, loop)

    assert lifted.base_closed
    assert lifted.lifted_closed
    assert lifted.sheet_multiplier == 1
    assert abs(lifted.y_values[-1] - lifted.y_values[0]) < 1e-10
