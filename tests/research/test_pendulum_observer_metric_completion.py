"""Pendulum observer-metric completion: declared A/M metric -> double covers.

Question
--------
The simple-pendulum family already certifies the observable carrier

    C_E: Y^2 = 2 (E-U) (1-U^2),
    Y = D U,

with ``U=q_y``.  Separately, the A/M observer demo uses the assignment
``a=U`` and an equal-weight A/M metric to draw a metric-horizontal lift in the
upper half-plane.

This essay asks a narrower, auditable question:

    If an A/M metric is *declared*, what algebraic structure is induced when
    the observer arc-length sheet is retained together with the physical
    velocity sheet?

The metric is kept as a one-parameter family.  This is deliberate: the test must
not smuggle the equal-weight choice into a claim of canonicality.

Primitive data
--------------
Use the A/M frame

    A = d/da,
    M = d/dv + a d/da,

with dual coframe

    theta_A = da - a dv,
    theta_M = dv.

Declare

    g_c = theta_A^2 + c theta_M^2,
    c > 0.

For the assignment fiber ``a=U`` the metric-horizontal direction normalized by
``H(U)=1`` is derived below.  The existing pendulum carrier supplies the second
square-root sheet.

Classical lineage
-----------------
The algebra used here is classical: two quadratic extensions of ``C(U)`` give a
biquadratic/V_4 extension, and the three nontrivial involution quotients are the
three quadratic subextensions.  A smooth hyperelliptic model ``w^2=P_d(U)``
with squarefree ``d=5`` has genus two.  At the special equal-weight/symmetric
point ``c=1, E=0`` the third quotient reduces to the Bolza model

    w^2 = U^5 - U.

The Process Geometry content of the experiment is not that these algebraic facts
are new.  It is the provenance of the two sheets: one comes from the physical
observable carrier and one from the declared observer metric.

Calibration statement
---------------------
Passing this file certifies:

1. the ``g_c``-horizontal lift has pullback line element
   ``ds_c^2 = c dU^2/(c+U^2)``;
2. the metric line element has orientation double-cover model
   ``Z^2=c+U^2``;
3. adjoining the physical sheet ``Y^2=2(E-U)(1-U^2)`` gives a biquadratic
   extension with third quadratic quotient
   ``W^2=2(E-U)(1-U^2)(c+U^2)``;
4. for generic parameters that quotient is genus two;
5. at ``E=0,c=1`` it is exactly the Bolza model after constant rescaling;
6. changing ``c`` moves the observer branch points and destroys the literal
   Bolza polynomial, so this essay provides no metric-naturality or canonical
   completion theorem.

Theory-map effect
-----------------
None.  This is problem-local evidence and a red team for stronger completion
language.  In particular it does not promote a generic observer metric,
``CanonicalCompletion``, or genus-two API.
"""

import sympy as sp

from process_geometry.analysis.algebraic import hyperelliptic_profile


def test_declared_am_metric_forces_the_horizontal_lift_and_line_element():
    U, c = sp.symbols("U c", positive=True)
    alpha, beta = sp.symbols("alpha beta")

    # In the (A,M) frame, H = alpha A + beta M has H(U)=alpha+U*beta.
    # A tangent vector to the assignment fiber has theta_A=0 and may be taken
    # as F=M-U*A, whose frame coefficients are (-U,1).
    # Orthogonality in diag(1,c) gives -U*alpha + c*beta = 0.
    solution = sp.solve(
        [sp.Eq(alpha + U * beta, 1), sp.Eq(-U * alpha + c * beta, 0)],
        (alpha, beta),
        dict=True,
    )
    assert len(solution) == 1
    alpha_u = sp.factor(solution[0][alpha])
    beta_u = sp.factor(solution[0][beta])

    assert sp.simplify(alpha_u - c / (c + U**2)) == 0
    assert sp.simplify(beta_u - U / (c + U**2)) == 0

    # Since d/dU along the horizontal lift is H, the metric coefficient is
    # g_c(H,H)=alpha^2+c*beta^2.
    metric_coefficient = sp.factor(alpha_u**2 + c * beta_u**2)
    assert sp.simplify(metric_coefficient - c / (c + U**2)) == 0


def test_observer_metric_and_physical_velocity_form_two_quadratic_sheets():
    U, E, c, Y, Z, W = sp.symbols("U E c Y Z W")

    physical = sp.expand(2 * (E - U) * (1 - U**2))
    observer = c + U**2
    third = sp.expand(physical * observer)

    # The two declared quadratic extensions are Y^2=physical and
    # Z^2=observer.  Their product W=YZ lies in the third quadratic
    # subextension.
    relation = sp.expand(W**2 - third)
    substituted = sp.expand(relation.subs(W**2, Y**2 * Z**2))
    substituted = sp.expand(
        substituted.subs({Y**2: physical, Z**2: observer}, simultaneous=True)
    )
    assert substituted == 0


def test_generic_observer_metric_completion_is_genus_two():
    U, E, c, W = sp.symbols("U E c W")
    polynomial = sp.expand(2 * (E - U) * (1 - U**2) * (c + U**2))
    profile = hyperelliptic_profile(U, W, polynomial)

    assert profile.degree == 5
    assert profile.generic_genus == 2
    assert profile.generically_smooth

    # The discriminant must vanish at obvious branch collisions.  We avoid
    # asserting a large closed form and instead certify representative
    # degenerations directly.
    disc = sp.factor(profile.discriminant)
    assert sp.simplify(disc.subs(E, 1)) == 0
    assert sp.simplify(disc.subs(E, -1)) == 0
    assert sp.simplify(disc.subs({E: 0, c: 0})) == 0


def test_equal_weight_symmetric_leaf_is_exactly_the_bolza_model():
    U, W, w = sp.symbols("U W w")

    polynomial = sp.expand(2 * (0 - U) * (1 - U**2) * (1 + U**2))
    assert sp.expand(polynomial - 2 * (U**5 - U)) == 0

    # W^2=2(U^5-U); w=W/sqrt(2) gives w^2=U^5-U.
    residual = sp.expand(
        (W**2 - polynomial).subs(W, sp.sqrt(2) * w) / 2
        - (w**2 - (U**5 - U))
    )
    assert residual == 0


def test_metric_weight_is_a_real_red_team_for_bolza_literal_symmetry():
    U, W, c = sp.symbols("U W c")
    e0_family = sp.expand(2 * (0 - U) * (1 - U**2) * (c + U**2))

    # At c=1 the finite branch set is {0,+/-1,+/-i}; for c!=1 the observer
    # pair moves to +/- i*sqrt(c).  Algebraically the literal Bolza polynomial
    # is recovered only at c=1 (up to the fixed overall factor used here).
    bolza_scaled = 2 * (U**5 - U)
    difference = sp.factor(e0_family - bolza_scaled)
    assert difference == 2 * U * (c - 1) * (U - 1) * (U + 1)
