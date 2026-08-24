"""A/M-first checkpointing A1--A2: history jets and first-order task germs.

Problem
-------
For a nonlinear time step written only with Addition and Multiplication, what
is the smallest materialized history object sufficient for a declared
first-order reverse/adjoint task?  The classical route starts from a Jacobian.
This calibration starts from a free A/M expression history and derives value,
JVP, and VJP compositionally.

Domains / classical names
-------------------------
Automatic differentiation, tangent/cotangent lift, straight-line programs,
checkpointing, affine group, semidirect product.

Process Geometry roles
----------------------
Free A/M history, analytic rank-lowering pressure, first-order differential
task germ, objectification candidate, and minimal process completion.  Theory
Map relation: research-local pressure on V5, not a closed V5 square.

Primitive firewall
------------------
Discovery receives only named inputs, constants, and binary Add/Mul nodes.
``AMExpression.jvp`` uses the Addition rule and Multiplication Leibniz rule.
``AMExpression.vjp`` dualizes those same rules and explicitly accumulates
cotangents at shared named leaves.  Neither path calls symbolic
differentiation, finite differences, or a supplied Jacobian.  The existing
``AMFunctionTheory`` is used only after the construction to certify that the
finite order red team lowers to the repository's A/M frame.

Claim boundary
--------------
The object below is only a first-order task germ at a declared basepoint and
declared inputs.  It is not a continuation-stable global function quotient.
The endpoint counterexample concerns cross-program/segment objectification; it
does not show that a classical fixed-program checkpoint containing state and
step index is insufficient.  Scalar JVP/VJP duality is standard AD, so this
calibration establishes an A/M-generated classical shadow, not a new adjoint
theory, a Pareto advantage, V5 closure, or A/M universality.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Mapping

import sympy as sp

from process_geometry.analysis.am import AMFunctionTheory, AMState


def _merge_cotangents(*parts: Mapping[str, Fraction]) -> dict[str, Fraction]:
    merged: dict[str, Fraction] = {}
    for part in parts:
        for name, value in part.items():
            merged[name] = merged.get(name, Fraction(0)) + value
    return merged


@dataclass(frozen=True)
class DirectionalJet:
    """One value and one caller-declared tangent direction."""

    value: Fraction
    tangent: Fraction


@dataclass(frozen=True)
class FirstOrderTaskGerm:
    """Task-local objectification candidate at one declared basepoint."""

    basepoint: tuple[tuple[str, Fraction], ...]
    endpoint: Fraction
    pullback: tuple[tuple[str, Fraction], ...]
    primitive_cost: int


@dataclass(frozen=True)
class AMExpression:
    """Free binary A/M expression history; derivatives are not syntax fields."""

    operation: str
    arguments: tuple["AMExpression", ...] = ()
    atom: Fraction | str | None = None

    @classmethod
    def input(cls, name: str) -> "AMExpression":
        return cls("input", atom=name)

    @classmethod
    def constant(cls, value) -> "AMExpression":
        return cls("constant", atom=Fraction(value))

    def __add__(self, other: "AMExpression") -> "AMExpression":
        return AMExpression("add", (self, other))

    def __mul__(self, other: "AMExpression") -> "AMExpression":
        return AMExpression("mul", (self, other))

    @property
    def primitive_cost(self) -> int:
        if not self.arguments:
            return 0
        return 1 + sum(argument.primitive_cost for argument in self.arguments)

    def evaluate(self, inputs: Mapping[str, Fraction]) -> Fraction:
        if self.operation == "input":
            assert isinstance(self.atom, str)
            return Fraction(inputs[self.atom])
        if self.operation == "constant":
            assert isinstance(self.atom, Fraction)
            return self.atom
        left = self.arguments[0].evaluate(inputs)
        right = self.arguments[1].evaluate(inputs)
        if self.operation == "add":
            return left + right
        if self.operation == "mul":
            return left * right
        raise ValueError(f"unknown A/M operation: {self.operation}")

    def jvp(
        self,
        inputs: Mapping[str, Fraction],
        tangents: Mapping[str, Fraction],
    ) -> DirectionalJet:
        """Generate a directional 1-jet using only A/M composition rules."""

        if self.operation == "input":
            assert isinstance(self.atom, str)
            return DirectionalJet(
                Fraction(inputs[self.atom]),
                Fraction(tangents.get(self.atom, 0)),
            )
        if self.operation == "constant":
            assert isinstance(self.atom, Fraction)
            return DirectionalJet(self.atom, Fraction(0))

        left = self.arguments[0].jvp(inputs, tangents)
        right = self.arguments[1].jvp(inputs, tangents)
        if self.operation == "add":
            return DirectionalJet(
                left.value + right.value,
                left.tangent + right.tangent,
            )
        if self.operation == "mul":
            return DirectionalJet(
                left.value * right.value,
                left.tangent * right.value + left.value * right.tangent,
            )
        raise ValueError(f"unknown A/M operation: {self.operation}")

    def vjp(
        self,
        inputs: Mapping[str, Fraction],
        output_covector: Fraction,
    ) -> dict[str, Fraction]:
        """Pull back a cotangent by dual A/M rules, accumulating shared leaves."""

        seed = Fraction(output_covector)
        if self.operation == "input":
            assert isinstance(self.atom, str)
            return {self.atom: seed}
        if self.operation == "constant":
            return {}

        left, right = self.arguments
        if self.operation == "add":
            return _merge_cotangents(
                left.vjp(inputs, seed),
                right.vjp(inputs, seed),
            )
        if self.operation == "mul":
            left_value = left.evaluate(inputs)
            right_value = right.evaluate(inputs)
            return _merge_cotangents(
                left.vjp(inputs, seed * right_value),
                right.vjp(inputs, seed * left_value),
            )
        raise ValueError(f"unknown A/M operation: {self.operation}")

    def substitute(self, replacements: Mapping[str, "AMExpression"]) -> "AMExpression":
        """Compose histories without quotienting their A/M syntax."""

        if self.operation == "input":
            assert isinstance(self.atom, str)
            return replacements.get(self.atom, self)
        if self.operation == "constant":
            return self
        return AMExpression(
            self.operation,
            tuple(argument.substitute(replacements) for argument in self.arguments),
        )


def euler_am_history() -> AMExpression:
    """Build ``x + h*(x*x - 2)`` without supplying any derivative."""

    x = AMExpression.input("x")
    h = AMExpression.input("h")
    return x + h * (x * x + AMExpression.constant(-2))


def first_order_task_germ(
    expression: AMExpression,
    inputs: Mapping[str, Fraction],
    declared_inputs: tuple[str, ...],
) -> FirstOrderTaskGerm:
    unit_pullback = expression.vjp(inputs, Fraction(1))
    return FirstOrderTaskGerm(
        basepoint=tuple((name, Fraction(inputs[name])) for name in declared_inputs),
        endpoint=expression.evaluate(inputs),
        pullback=tuple((name, unit_pullback.get(name, Fraction(0))) for name in declared_inputs),
        primitive_cost=expression.primitive_cost,
    )


def test_am_rules_generate_euler_value_all_jvps_vjp_and_pairing():
    expression = euler_am_history()
    inputs = {"x": Fraction(3, 5), "h": Fraction(1, 10)}
    x, h = inputs["x"], inputs["h"]

    x_direction = expression.jvp(inputs, {"x": 1, "h": 0})
    h_direction = expression.jvp(inputs, {"x": 0, "h": 1})
    assert x_direction.value == x + h * (x**2 - 2)
    assert x_direction.tangent == 1 + 2 * h * x
    assert h_direction.tangent == x**2 - 2

    output_covector = Fraction(7, 3)
    pulled = expression.vjp(inputs, output_covector)
    assert pulled == {
        "x": output_covector * (1 + 2 * h * x),
        "h": output_covector * (x**2 - 2),
    }

    direction = {"x": Fraction(5, 7), "h": Fraction(-2, 9)}
    output_tangent = expression.jvp(inputs, direction).tangent
    assert output_covector * output_tangent == sum(
        pulled[name] * direction[name] for name in ("x", "h")
    )


def test_shared_mul_leaf_accumulates_both_adjoint_contributions():
    x = AMExpression.input("x")
    square = x * x
    assert square.vjp({"x": Fraction(3)}, Fraction(1)) == {"x": Fraction(6)}


def test_two_step_am_history_composition_matches_segment_jvp_and_vjp():
    step = euler_am_history()
    composed = step.substitute({"x": step})
    inputs = {"x": Fraction(1, 2), "h": Fraction(1, 20)}

    first_x = step.jvp(inputs, {"x": 1, "h": 0})
    first_h = step.jvp(inputs, {"x": 0, "h": 1})
    second_inputs = {"x": first_x.value, "h": inputs["h"]}
    second_x = step.jvp(second_inputs, {"x": 1, "h": 0})
    second_h = step.jvp(second_inputs, {"x": 0, "h": 1})

    assert composed.jvp(inputs, {"x": 1, "h": 0}).tangent == (
        second_x.tangent * first_x.tangent
    )
    assert composed.jvp(inputs, {"x": 0, "h": 1}).tangent == (
        second_x.tangent * first_h.tangent + second_h.tangent
    )

    terminal_covector = Fraction(11, 7)
    direct = composed.vjp(inputs, terminal_covector)
    second_pullback = step.vjp(second_inputs, terminal_covector)
    first_pullback = step.vjp(inputs, second_pullback["x"])
    segmented = {
        "x": first_pullback["x"],
        "h": first_pullback["h"] + second_pullback["h"],
    }
    assert direct == segmented


def test_endpoint_only_cross_program_objectification_fails_for_adjoint_task():
    x = AMExpression.input("x")
    square = x * x
    add_zero = x + AMExpression.constant(0)
    inputs = {"x": Fraction(1)}
    left = first_order_task_germ(square, inputs, ("x",))
    right = first_order_task_germ(add_zero, inputs, ("x",))

    assert left.primitive_cost == right.primitive_cost == 1
    assert left.endpoint == right.endpoint == 1
    assert left.pullback == (("x", Fraction(2)),)
    assert right.pullback == (("x", Fraction(1)),)


def test_am_order_is_visible_only_when_translation_parameter_varies():
    x = AMExpression.input("x")
    epsilon = AMExpression.input("epsilon")
    two = AMExpression.constant(2)

    scale_after_translate = two * (x + epsilon)
    translate_after_scale = two * x + epsilon
    corrected = two * x + two * epsilon
    inputs = {"x": Fraction(5, 3), "epsilon": Fraction(0)}

    left = first_order_task_germ(
        scale_after_translate, inputs, ("x", "epsilon")
    )
    wrong = first_order_task_germ(
        translate_after_scale, inputs, ("x", "epsilon")
    )
    right = first_order_task_germ(corrected, inputs, ("x", "epsilon"))

    assert left.endpoint == wrong.endpoint
    assert dict(left.pullback)["x"] == dict(wrong.pullback)["x"] == 2
    assert dict(left.pullback)["epsilon"] == 2
    assert dict(wrong.pullback)["epsilon"] == 1
    assert left.endpoint == right.endpoint
    assert left.pullback == right.pullback


def test_finite_order_red_team_lowers_to_the_existing_am_process_frame():
    a, v = sp.symbols("a v", real=True)
    theory = AMFunctionTheory(a, v)
    state = AMState(a, v)
    residual = theory.finite_relation_residual(
        state,
        amount=1,
        log_scale=sp.log(2),
    )
    assert all(sp.simplify(component) == 0 for component in residual)

    probe = a**3 * sp.exp(v) + a * v
    assert sp.simplify(theory.commutator(probe) - theory.A(probe)) == 0


def test_first_order_germ_has_a_hessian_and_global_completion_boundary():
    x = AMExpression.input("x")
    square = x * x
    tangent_line_at_one = AMExpression.constant(2) * x + AMExpression.constant(-1)
    anchor = {"x": Fraction(1)}

    square_germ = first_order_task_germ(square, anchor, ("x",))
    line_germ = first_order_task_germ(tangent_line_at_one, anchor, ("x",))
    assert square_germ.basepoint == line_germ.basepoint
    assert square_germ.endpoint == line_germ.endpoint == 1
    assert square_germ.pullback == line_germ.pullback == (("x", Fraction(2)),)

    nearby = {"x": Fraction(3, 2)}
    assert square.evaluate(nearby) != tangent_line_at_one.evaluate(nearby)
