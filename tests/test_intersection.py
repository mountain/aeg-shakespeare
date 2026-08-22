import pytest

from aeg_shakespeare.analysis.abelian import canonical_symplectic_form


def test_canonical_symplectic_form_uses_a_then_b_order():
    assert canonical_symplectic_form(1) == ((0, 1), (-1, 0))
    assert canonical_symplectic_form(2) == (
        (0, 0, 1, 0),
        (0, 0, 0, 1),
        (-1, 0, 0, 0),
        (0, -1, 0, 0),
    )


def test_canonical_symplectic_form_requires_positive_genus():
    with pytest.raises(ValueError, match="positive"):
        canonical_symplectic_form(0)
