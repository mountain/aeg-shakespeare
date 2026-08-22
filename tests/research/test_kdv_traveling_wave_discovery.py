"""KdV traveling waves: discover the elliptic quotient before naming it.

Question
--------
Can Shakespeare enter an integrable soliton problem without preloading the
traveling-wave energy integral, Jacobi elliptic functions, or the soliton
formula, and still discover the algebraic geometry that separates the generic
periodic wave from its solitary-wave degeneration?

Primitive data
--------------
For the KdV equation

    u_t + 6 u u_x + u_xxx = 0,

a permanent traveling profile ``u(x,t)=U(x-c t)`` satisfies, after one exact
integration in the traveling coordinate,

    D U = V,
    D V = c U - 3 U^2 + a.

The integration constant ``a`` and wave speed ``c`` are retained as parameters.
No first integral for this second-order process is supplied to Shakespeare.

Classical lineage
-----------------
Traveling-wave reduction of KdV produces a cubic effective potential. Generic
bounded waves are cnoidal/elliptic, while the solitary wave occurs when the
cubic degenerates and two roots coalesce. See [Carretero-Frantzeskakis-
Kevrekidis-2024]. More generally, degeneration of finite-gap spectral curves is
a standard route from algebro-geometric KdV solutions toward solitons; see
[Bertola-Jenkins-Tovbis-2023].

Shakespeare reconstruction
---------------------------
Within a degree-three polynomial observer budget, the Discovery layer sees only
the local process generator above. Its exact nullspace search must recover the
nontrivial invariant direction

    I = V^2 - c U^2 + 2 U^3 - 2 a U.

Only after that direction is discovered do we introduce a leaf value ``B`` and
eliminate the source assignments. The first-order quotient must then recover

    Y^2 = B + c X^2 + 2 a X - 2 X^3.

For generic parameters this is a smooth cubic, hence genus one. On the soliton
leaf ``a=B=0`` it becomes

    Y^2 = X^2 (c - 2 X),

whose repeated root makes the cubic singular. Dividing by the repeated factor
on the normalization, ``W=Y/X`` satisfies

    W^2 = c - 2 X,

which is genus zero.

**Shakespeare interpretation.** The named elliptic and hyperbolic function
languages are not inputs. The generic genus-one language and the genus-zero
soliton degeneration are shadows of one discovered process quotient.

Calibration statement
---------------------
Passing this file certifies that:

1. the traveling-wave process has exactly one nontrivial polynomial first
   integral within the declared degree-three budget;
2. that invariant is discovered without an energy template;
3. the invariant leaf eliminates exactly to the expected cubic quotient;
4. the generic quotient has genus one;
5. the solitary-wave parameter leaf is detected as a discriminant-zero
   degeneration; and
6. removing the repeated factor exposes a genus-zero normalized quotient.

This is intentionally a first integrable-systems calibration. It does not yet
claim to reconstruct the full KdV PDE, Lax operator, inverse-scattering data,
N-soliton determinant, or finite-gap theta function from primitive PDE syntax.
Those are the next thresholds if the representation program survives this test.

References
----------
[Carretero-Frantzeskakis-Kevrekidis-2024] R. Carretero-Gonzalez,
D. J. Frantzeskakis, and P. G. Kevrekidis, "Traveling Wave Reduction,
Elliptic Functions, and Connections to KdV," in *Nonlinear Waves & Hamiltonian
Systems*, Oxford University Press, 2024, Chapter 6.
DOI: 10.1093/oso/9780192843234.003.0006.

[Bertola-Jenkins-Tovbis-2023] M. Bertola, R. Jenkins, and A. Tovbis,
"Partial degeneration of finite gap solutions to the Korteweg-de Vries
equation: soliton gas and scattering on elliptic background," arXiv:2210.01350.
"""

import sympy as sp

from aeg_shakespeare.analysis.algebraic import hyperelliptic_profile
from aeg_shakespeare.discovery import (
    discover_first_order_process_quotient,
    discover_polynomial_invariants,
)
from aeg_shakespeare.presentation.constraints import AlgebraicConstraintSet
from aeg_shakespeare.process.local import ProcessSystem


def kdv_traveling_wave_process():
    U, V, c, a = sp.symbols("U V c a")
    system = ProcessSystem(
        (U, V),
        {
            U: V,
            V: c * U - 3 * U**2 + a,
        },
        name="D_xi",
    )
    return U, V, c, a, system


def test_kdv_traveling_wave_discovers_genus_one_and_soliton_degeneration():
    U, V, c, a, system = kdv_traveling_wave_process()

    discovery = discover_polynomial_invariants(system, max_degree=3)
    assert len(discovery.invariants) == 1
    invariant = discovery.invariants[0]
    assert invariant.certified

    expected_invariant = sp.expand(V**2 - c * U**2 + 2 * U**3 - 2 * a * U)
    invariant_ratio = sp.cancel(invariant.expression / expected_invariant)
    assert invariant_ratio != 0
    assert not invariant_ratio.free_symbols

    B, X, Y = sp.symbols("B X Y")
    leaf = AlgebraicConstraintSet(
        (U, V, c, a, B),
        (invariant.expression - B,),
    )
    quotient = discover_first_order_process_quotient(
        system,
        U,
        observable_symbol=X,
        derivative_symbol=Y,
        constraints=leaf,
        parameters=(c, a, B),
    )

    assert quotient.complete_certificates
    assert len(quotient.relations) == 1
    discovered_relation = quotient.relations[0].relation
    expected_polynomial = sp.expand(B + c * X**2 + 2 * a * X - 2 * X**3)
    expected_relation = sp.expand(Y**2 - expected_polynomial)
    relation_ratio = sp.cancel(discovered_relation / expected_relation)
    assert relation_ratio != 0
    assert not relation_ratio.free_symbols

    generic_profile = hyperelliptic_profile(X, Y, expected_polynomial)
    assert generic_profile.degree == 3
    assert generic_profile.generic_genus == 1
    assert generic_profile.generically_smooth
    assert sp.simplify(
        generic_profile.discriminant.subs({a: 0, B: 0})
    ) == 0

    # CLASSICAL SHADOW: the solitary-wave leaf is a singular cubic with a
    # repeated root. Its normalization is rational/genus zero.
    soliton_polynomial = sp.factor(expected_polynomial.subs({a: 0, B: 0}))
    assert soliton_polynomial == X**2 * (c - 2 * X)
    soliton_profile = hyperelliptic_profile(X, Y, soliton_polynomial)
    assert soliton_profile.discriminant == 0
    assert soliton_profile.generic_genus is None

    W = sp.Symbol("W")
    normalized_profile = hyperelliptic_profile(X, W, c - 2 * X)
    assert normalized_profile.degree == 1
    assert normalized_profile.generic_genus == 0
    assert normalized_profile.generically_smooth
