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

No generic ODE solver, integrating factor, or closed-form trajectory is supplied
to ``ProcessDirection``.

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

This separates three layers that were previously easy to conflate:

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
5. no observer connection is required for this calibration -- this is a useful
   negative control separating process direction from observer transport.

Boundary
--------
This test does not claim that ``ProcessDirection`` is itself a trajectory object
or that arbitrary directions admit closed-form integration.  It also does not
identify proportional directions: time reparameterization remains task-sensitive.
"""

import sympy as sp

from aeg_shakespeare.analysis.am import AMFunctionTheory
from aeg_shakespeare.process.local import ProcessDirection


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
