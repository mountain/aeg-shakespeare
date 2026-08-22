import pytest
import sympy as sp

from aeg_shakespeare.analysis.abelian import GenusOneLattice, lift_square_root_path
from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile


def test_lift_requires_numeric_parameters_and_avoids_branch_points():
    x, y, a = sp.symbols("x y a")
    curve = hyperelliptic_profile(x, y, x**2 - a)

    with pytest.raises(ValueError, match="parameters fixed"):
        lift_square_root_path(curve, (2 + 0j, 2 + 1j))

    numeric = hyperelliptic_profile(x, y, x**2 - 1)
    with pytest.raises(ValueError, match="branch point"):
        lift_square_root_path(numeric, (1 + 0j, 1 + 1j))


def test_genus_one_lattice_rejects_collinear_periods():
    with pytest.raises(ValueError, match="non-collinear"):
        GenusOneLattice(omega_a=1 + 0j, omega_b=2 + 0j)
