import sympy as sp

from aeg_shakespeare import (
    Add,
    ProcessSystem,
    Scale,
    decompose,
    discover_quadratic_return_sectors,
    discover_return_relation,
    homogeneous_monomials,
    normalize_affine_history,
)


def test_p0_affine_normalization():
    a, b, s = sp.symbols("a b s")
    nf = normalize_affine_history([Add(a), Scale(s), Add(b)])
    assert sp.simplify(nf.scale - s) == 0
    assert sp.simplify(nf.shift - (s * a + b)) == 0


def oscillator():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="R")


def test_p2_oscillator_return_relation():
    x, _, R = oscillator()
    relation = discover_return_relation(R, x, max_order=4)
    assert relation is not None
    assert relation.order == 2
    D = sp.Symbol("D")
    assert sp.expand(relation.as_expr(D) - (1 + D**2)) == 0


def test_p3_discovers_degree_three_return_sectors():
    x, p, R = oscillator()
    basis = homogeneous_monomials((x, p), 3)
    sectors = discover_quadratic_return_sectors(R, basis, max_rate=4)
    rates = {sector.rate for sector in sectors}
    assert rates == {1, 3}

    for sector in sectors:
        for primitive in sector.primitives:
            assert sp.expand(R.derive(R.derive(primitive)) + sector.rate**2 * primitive) == 0


def test_p3_duffing_forcing_decomposes_into_return_sectors():
    x, p, R = oscillator()
    basis = homogeneous_monomials((x, p), 3)
    sectors = discover_quadratic_return_sectors(R, basis, max_rate=4)
    primitives = [expr for sector in sectors for expr in sector.primitives]
    coeffs = decompose(x**3, primitives, (x, p))
    reconstructed = sp.expand(sum(c * q for c, q in zip(coeffs, primitives)))
    assert sp.expand(reconstructed - x**3) == 0


def test_p1_krylov_recovers_return_relation_before_spectrum():
    from aeg_shakespeare import discover_krylov_relation

    X = sp.Matrix([[0, -1], [1, 0]])
    v = sp.Matrix([1, 0])
    relation = discover_krylov_relation(X, v)
    assert relation is not None
    z = sp.Symbol("X")
    assert sp.expand(relation.as_polynomial(z) - (1 + z**2)) == 0
