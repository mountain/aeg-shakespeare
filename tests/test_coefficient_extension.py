import sympy as sp

from aeg_shakespeare.discovery import factor_process_relation_over_extension
from aeg_shakespeare.presentation.relations import (
    ProcessPolynomialRelation,
    factor_process_relation,
)


def test_explicit_complex_extension_refines_irreducible_process_relation():
    relation = ProcessPolynomialRelation((1, 0, 1))
    D = sp.Symbol("D")

    assert [factor.as_expr(D) for factor in factor_process_relation(relation)] == [
        D**2 + 1
    ]

    factors = factor_process_relation_over_extension(relation, sp.I)
    assert {sp.expand(factor.as_expr(D)) for factor in factors} == {
        D - sp.I,
        D + sp.I,
    }
    assert sp.expand(sp.prod(factor.as_expr(D) for factor in factors) - (D**2 + 1)) == 0


def test_extension_factorization_retains_primary_multiplicity():
    relation = ProcessPolynomialRelation((1, 0, 2, 0, 1))  # (D^2+1)^2
    D = sp.Symbol("D")

    factors = factor_process_relation_over_extension(relation, sp.I)
    assert {sp.expand(factor.as_expr(D)) for factor in factors} == {
        sp.expand((D - sp.I) ** 2),
        sp.expand((D + sp.I) ** 2),
    }
