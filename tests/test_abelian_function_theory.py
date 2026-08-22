import sympy as sp

from aeg_shakespeare.analysis.abelian import (
    abelian_integral_profile,
    holomorphic_differential_basis,
)
from aeg_shakespeare.analysis.algebraic import (
    hyperelliptic_profile,
    weierstrass_cubic_profile,
)


def test_holomorphic_differential_basis_tracks_generic_genus():
    x, y, E = sp.symbols("x y E")

    genus_zero = hyperelliptic_profile(x, y, 2 * E - x**2)
    genus_one = hyperelliptic_profile(x, y, 2 * E - x**4 / 2)
    genus_two = hyperelliptic_profile(x, y, 2 * E - x**6 / 3)

    assert holomorphic_differential_basis(genus_zero) == ()
    assert [d.power for d in holomorphic_differential_basis(genus_one)] == [0]
    assert [d.power for d in holomorphic_differential_basis(genus_two)] == [0, 1]


def test_abelian_profile_exposes_dimension_homology_rank_and_process_pullback():
    x, y, E = sp.symbols("x y E")
    curve = hyperelliptic_profile(x, y, 2 * E - x**6 / 3)
    profile = abelian_integral_profile(curve)

    assert profile.abelian_dimension == 2
    assert profile.homology_rank == 4
    assert profile.pullback_coefficients(y) == (1, x)


def test_weierstrass_cubic_profile_certifies_exact_coordinate_change():
    x, y, X, W = sp.symbols("x y X W")
    curve = hyperelliptic_profile(x, y, x**3 - x)
    profile = weierstrass_cubic_profile(curve, X, W)

    assert profile.transformation_residual() == 0
    assert profile.g3 == 0
    assert profile.j_invariant == 1728


def test_weierstrass_profile_rejects_non_cubic_input():
    x, y, X, W = sp.symbols("x y X W")
    curve = hyperelliptic_profile(x, y, x**4 + 1)

    try:
        weierstrass_cubic_profile(curve, X, W)
    except ValueError as exc:
        assert "degree exactly 3" in str(exc)
    else:
        raise AssertionError("quartic input must not be silently treated as a cubic")
