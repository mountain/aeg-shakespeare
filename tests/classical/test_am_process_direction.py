"""A/M process direction: ordinary ODE as an assignment shadow.

Question
--------
Can the Addition/Multiplication calculus express its local process trajectory
through the generic ``ProcessDirection`` API rather than treating the familiar
ODE

    a_dot = alpha + beta*a,
    v_dot = beta

as primitive A/M-specific ontology?

Primitive data
--------------
The A/M frame is

    A = d/da,
    M = d/dv + a*d/da,

with ``[A,M]=A``.  A local process direction is declared only as

    D_Gamma = alpha(t)*A + beta(t)*M.

No generic ODE solver, integrating factor, observer connection, or closed-form
trajectory is supplied to ``ProcessDirection``.

Classical lineage
-----------------
The relation ``[A,M]=A`` is the infinitesimal relation of the one-dimensional
affine/``ax+b`` group, a standard solvable matrix Lie group; see [Hall-2015] for
matrix Lie groups and Lie algebras.  After projection to assignments,
``a_dot=alpha+beta*a`` is an ordinary first-order linear differential equation,
whose integrating-factor solution belongs to standard ODE theory; see
[Coddington-Levinson-1955].

The classical sources do not motivate the AEG/Shakespeare ontology.  The
**Shakespeare interpretation** is that Addition and Multiplication are primitive
ordered process directions, while the affine group and linear ODE are later
representations/shadows of their process relation.

Shakespeare reconstruction
---------------------------
``ProcessDirection`` acts first on the assignment algebra.  Only after that
projection do the ordinary equations appear:

    D_Gamma(a) = alpha + beta*a,
    D_Gamma(v) = beta.

The existing ``AMFunctionTheory.path_flow`` remains a concrete analytic solver
for this particular process direction.  Its history term keeps the key ordered
A/M effect explicit: additive increments injected earlier are reweighted by
later multiplication history.

This separates four layers that were previously easy to conflate:

```text
A/M process frame
    -> generic local ProcessDirection
    -> assignment ODE shadow
    -> A/M-specific exact integration formula.
```

Calibration statement
---------------------
Passing this file certifies that:

1. the generic direction API produces the standard A/M assignment ODE exactly;
2. lowering that direction to ``ProcessSystem`` preserves the same local rules;
3. the existing exact A/M path flow solves the constant-coefficient instance;
4. the additive history term is still reweighted by subsequent multiplication;
5. no observer connection is required for this calibration -- this is a negative
   control separating process direction from observer transport.

Proof map
---------
1. ``test_am_process_direction_has_the_expected_assignment_shadow`` constructs
   only ``alpha*A+beta*M`` and checks both assignment derivatives before lowering
   to ``ProcessSystem``.
2. ``test_existing_am_path_flow_integrates_the_generic_direction_shadow`` uses
   the constant direction ``A+2M``, verifies its local assignment shadow, and
   then checks the existing exact path-flow endpoint and explicit history term.

Boundary
--------
This test does not claim that ``ProcessDirection`` is itself a trajectory object,
that arbitrary directions admit closed-form integration, or that the A/M
calculus is the unique natural calculus for every problem.  It does not identify
proportional directions: time reparameterization remains task-sensitive.  The
interpretation of the history-weighted integral as an AEG process integral is a
project-specific reading of the implemented formula, not a claim made by the
classical references.

References
----------
[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations: An
Elementary Introduction*, 2nd ed., Graduate Texts in Mathematics 222, Springer,
2015, Chapters 2--3; DOI 10.1007/978-3-319-13467-3.

[Coddington-Levinson-1955] Earl A. Coddington, Norman Levinson, *Theory of
Ordinary Differential Equations*, McGraw-Hill, New York, 1955; see the treatment
of linear differential equations (beginning p. 62 in the standard edition),
ISBN 978-0-07-099256-6.
"""

import sympy as sp

from process_geometry.analysis.am import AMFunctionTheory
from process_geometry.process.local import ProcessDirection


def test_am_process_direction_has_the_expected_assignment_shadow():
    a, v, t = sp.symbols("a v t")
    alpha = sp.Function("alpha")(t)
    beta = sp.Function("beta")(t)
    theory = AMFunctionTheory(a, v)

    direction = ProcessDirection(
        theory.frame,
        {"A": alpha, "M": beta},
        label="A/M process trajectory direction",
    )

    assert sp.expand(direction.apply(a) - (alpha + beta * a)) == 0
    assert sp.expand(direction.apply(v) - beta) == 0

    system = direction.as_system(name="D_Gamma")
    assert sp.expand(system.rules[a] - (alpha + beta * a)) == 0
    assert sp.expand(system.rules[v] - beta) == 0


def test_existing_am_path_flow_integrates_the_generic_direction_shadow():
    a, v, t, T, a0, v0 = sp.symbols("a v t T a0 v0", positive=True)
    theory = AMFunctionTheory(a, v)
    direction = ProcessDirection(
        theory.frame,
        {"A": sp.S.One, "M": sp.Integer(2)},
    )

    assert direction.apply(a) == 1 + 2 * a
    assert direction.apply(v) == 2

    flow = theory.path_flow(
        alpha=1,
        beta=2,
        time=t,
        start=0,
        end=T,
        a0=a0,
        v0=v0,
    )

    expected_history = (sp.exp(2 * T) - 1) / 2
    assert sp.simplify(flow.history_term - expected_history) == 0
    assert sp.simplify(
        flow.a_end - (sp.exp(2 * T) * a0 + expected_history)
    ) == 0
    assert sp.simplify(flow.v_end - (v0 + 2 * T)) == 0
