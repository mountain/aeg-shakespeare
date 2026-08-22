"""P0-P3 research benchmarks for AEG Shakespeare."""

import sympy as sp

from aeg_shakespeare import (
    Add,
    ProcessSystem,
    Scale,
    decompose,
    discover_krylov_relation,
    discover_quadratic_return_sectors,
    discover_return_relation,
    homogeneous_monomials,
    normalize_affine_history,
)


def p0_add_multiply():
    a, b, s = sp.symbols("a b s")
    normal = normalize_affine_history([Add(a), Scale(s), Add(b)])
    print("P0 affine normal form:", normal)


def p1_krylov():
    X = sp.Matrix([[0, -1], [1, 0]])
    v = sp.Matrix([1, 0])
    relation = discover_krylov_relation(X, v)
    print("P1 Krylov return relation:", relation.as_polynomial() if relation else None)


def oscillator_system():
    x, p = sp.symbols("x p")
    return x, p, ProcessSystem((x, p), {x: p, p: -x}, name="R")


def p2_oscillator():
    x, p, R = oscillator_system()
    relation = discover_return_relation(R, x, max_order=6)
    print("P2 return relation:", relation.as_expr() if relation else None)


def p3_duffing_cubic_grammar():
    x, p, R = oscillator_system()
    basis = homogeneous_monomials((x, p), 3)
    sectors = discover_quadratic_return_sectors(R, basis, max_rate=4)
    print("P3 degree-3 return sectors:")
    for sector in sectors:
        print(f"  rate={sector.rate}: {sector.primitives}")

    primitives = [expr for sector in sectors for expr in sector.primitives]
    coeffs = decompose(x**3, primitives, (x, p))
    print("  x^3 decomposition:")
    for coefficient, primitive in zip(coeffs, primitives):
        if coefficient:
            print("   ", coefficient, "*", primitive)


if __name__ == "__main__":
    p0_add_multiply()
    p1_krylov()
    p2_oscillator()
    p3_duffing_cubic_grammar()
