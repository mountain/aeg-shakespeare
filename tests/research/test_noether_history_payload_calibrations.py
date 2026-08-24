"""Noether-guided canonicalization probes with nontrivial history payloads.

The three calibrations deliberately play different roles:

* anisotropic optics is a positive variational/optimization example;
* a magnetic connection supplies genuine curvature and path holonomy;
* Berry phase shows that composable history data need not be an ordered cost.

They remain research-local and do not define a package API.
"""

from fractions import Fraction
from math import cos, hypot, isclose, pi


def _anisotropic_norm(dx, dy, horizontal_scale):
    return hypot(horizontal_scale * dx, dy)


def _anisotropic_optical_length(crossing_x):
    # Endpoints (0,4), (6,-8), interface y=0.  The lower medium has
    # F_2(v)=sqrt(4 vx^2+vy^2) and index 1/2.
    upper = _anisotropic_norm(crossing_x, 4, 1)
    lower = Fraction(1, 2) * _anisotropic_norm(6 - crossing_x, 8, 2)
    return upper + lower


def test_anisotropic_fermat_stationarity_is_conservation_of_noether_momentum():
    crossing_x = 3

    # For F_i(v)=n_i sqrt(alpha_i^2 vx^2+vy^2), translation along
    # the interface gives p_x=dF/dvx.  Both exact momenta equal 3/5.
    upper_momentum = Fraction(1) * Fraction(1**2 * 3, 5)
    lower_momentum = Fraction(1, 2) * Fraction(2**2 * 3, 10)
    assert upper_momentum == lower_momentum == Fraction(3, 5)

    # The stationary crossing is a strict minimum in this positive convex
    # Finsler example, not just an equality of momenta.
    assert _anisotropic_optical_length(3) == 10
    assert _anisotropic_optical_length(3) < _anisotropic_optical_length(2)
    assert _anisotropic_optical_length(3) < _anisotropic_optical_length(4)

    # Uniformly changing the length unit scales path velocities and c alike;
    # the arrival time and minimizing crossing are unchanged.
    length_unit_scale = 100
    light_speed = 7
    scaled_time = (
        length_unit_scale * _anisotropic_optical_length(crossing_x)
        / (length_unit_scale * light_speed)
    )
    assert scaled_time == _anisotropic_optical_length(crossing_x) / light_speed


def _line_integral_symmetric_gauge(start, end, magnetic_field):
    """Integral of A=(-By/2,Bx/2) on a straight segment."""

    x0, y0 = start
    x1, y1 = end
    return Fraction(magnetic_field, 2) * (x0 * y1 - y0 * x1)


def _chi(point, gauge_strength):
    x, y = point
    return gauge_strength * x * y


def _connection_integral(path, magnetic_field, gauge_strength=0):
    total = Fraction(0)
    for start, end in zip(path, path[1:]):
        total += _line_integral_symmetric_gauge(start, end, magnetic_field)
        total += _chi(end, gauge_strength) - _chi(start, gauge_strength)
    return total


def test_magnetic_connection_has_gauge_invariant_nontrivial_holonomy():
    square = ((0, 0), (2, 0), (2, 3), (0, 3), (0, 0))

    # Stokes: the loop integral is B times oriented area = 5*6=30.
    base_holonomy = _connection_integral(square, magnetic_field=5)
    transformed_holonomy = _connection_integral(
        square, magnetic_field=5, gauge_strength=7
    )
    assert base_holonomy == transformed_holonomy == 30

    # Open-path connection integrals are gauge dependent, but two histories
    # with the same endpoints differ by the enclosed flux in every gauge.
    upper = ((0, 0), (0, 3), (2, 3))
    lower = ((0, 0), (2, 0), (2, 3))
    base_difference = _connection_integral(upper, 5) - _connection_integral(lower, 5)
    gauge_difference = _connection_integral(upper, 5, 7) - _connection_integral(
        lower, 5, 7
    )
    assert base_difference == gauge_difference == -30

    # Reversing history reverses holonomy.  This signed action contribution is
    # composable, but is not by itself a positive Bellman cost.
    reversed_square = tuple(reversed(square))
    assert _connection_integral(reversed_square, 5) == -base_holonomy


def _phase_mod_one(turns):
    return turns % 1


def test_berry_phase_is_composable_history_data_but_not_an_ordered_resource():
    # For a spin-1/2 eigenline at fixed polar angle, a once-wound loop has
    # Berry phase / 2pi = (1-cos(theta))/2.  Choose cos(theta)=3/5.
    berry_turns = (Fraction(1) - Fraction(3, 5)) / 2
    assert berry_turns == Fraction(1, 5)

    # A single-valued gauge change shifts the representative by an integer;
    # the U(1) holonomy is unchanged modulo one turn.
    assert _phase_mod_one(berry_turns + 3) == berry_turns

    # Winding composes by addition modulo one and a reversed loop is the
    # inverse.  A nonzero element plus its inverse being zero rules out reading
    # the phase itself as a nonnegative additive complexity.
    inverse = _phase_mod_one(-berry_turns)
    assert inverse == Fraction(4, 5)
    assert _phase_mod_one(berry_turns + inverse) == 0

    # A task/measurement can turn phase into a scalar interference observable,
    # but that scalarization is not additive along histories.
    interference = cos(2 * pi * float(berry_turns))
    twice_interference = cos(2 * pi * float(_phase_mod_one(2 * berry_turns)))
    assert isclose(interference, cos(2 * pi / 5))
    assert not isclose(twice_interference, 2 * interference)

