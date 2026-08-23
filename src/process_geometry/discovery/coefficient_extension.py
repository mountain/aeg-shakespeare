"""Explicit coefficient-language extensions for process-relation factorization.

A discovered process relation is always meaningful before any root or spectral
interpretation.  Sometimes a caller may nevertheless ask whether the same
relation admits a finer factorization after enlarging the coefficient language.
This module provides exactly that experiment and nothing more.

It deliberately does not define eigenvalues, eigenspaces, a spectral theorem,
or an automatic policy for choosing coefficient fields.  The extension is an
explicit representation proposal supplied by the caller.
"""

from __future__ import annotations

import sympy as sp

from ..relations import ProcessPolynomialRelation


def factor_process_relation_over_extension(
    relation: ProcessPolynomialRelation,
    extension,
) -> tuple[ProcessPolynomialRelation, ...]:
    """Factor ``relation`` after an explicit algebraic coefficient extension.

    Parameters
    ----------
    relation:
        The already-discovered constant-coefficient process relation.
    extension:
        A SymPy algebraic extension accepted by ``factor_list``; for example
        ``sp.I`` for adjoining a square root of ``-1``.

    Notes
    -----
    Multiplicity is retained inside each primary factor, matching the ordinary
    Shakespeare relation-factor convention.  Returned factors are normalized
    to monic process polynomials.  No semantic meaning is attached to their
    roots by this routine.
    """

    if extension is None:
        raise ValueError("an explicit coefficient extension is required")

    symbol = sp.Symbol("_D")
    expression = relation.as_expr(symbol)
    _unit, factors = sp.factor_list(
        expression,
        symbol,
        extension=extension,
    )
    if not factors:
        return (relation,)

    result: list[ProcessPolynomialRelation] = []
    for factor, multiplicity in factors:
        primary = sp.Poly(
            sp.expand(factor**multiplicity),
            symbol,
            extension=extension,
        ).monic()
        coefficients = tuple(
            sp.simplify(value)
            for value in reversed(primary.all_coeffs())
        )
        result.append(ProcessPolynomialRelation(coefficients))

    original = sp.Poly(expression, symbol, extension=extension).monic().as_expr()
    rebuilt = sp.expand(
        sp.prod(factor.as_expr(symbol) for factor in result)
    )
    if sp.simplify(sp.expand(original - rebuilt)) != 0:
        raise AssertionError("coefficient-extension factorization certificate failed")

    return tuple(result)
