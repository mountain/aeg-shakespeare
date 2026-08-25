"""A/M-first checkpointing A1--A3: history jets and materialized task germs.

Problem
-------
For a nonlinear time step written only with Addition and Multiplication, can a
declared first-order reverse/adjoint payload be generated from the history
itself, and when is caching that payload preferable to replay?  The classical
route starts from a Jacobian.  This calibration starts from a free A/M
expression history and derives value, JVP, and VJP compositionally.

Domains / classical names
-------------------------
Automatic differentiation, tangent/cotangent lift, straight-line programs,
checkpointing, affine group, semidirect product.

Process Geometry roles
----------------------
Free A/M history, analytic rank-lowering pressure, first-order differential
task germ, explicit abstract materialization contract, and Bellman-selected
local cache.  Theory Map relation: research-local pressure on V5, not a closed
V5 square.

Primitive firewall
------------------
The evaluator receives only named inputs, constants, and binary Add/Mul nodes.
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
theory, a single-query Pareto advantage, V5 closure, or A/M universality.  The
A3 Bellman gate compares payload representations for repeated reverse queries
at the same declared basepoints under a frozen segmentation and representation
grammar; it is not a global Pareto frontier or a checkpoint scheduler.  Its
costs are normalized algebraic-RAM work and persistent scalar storage; peak
scratch space, scalar bit complexity, and the common physical forward pass are
outside this gate.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
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
class SegmentExecution:
    """One forward segment and its task-local A/M germ."""

    expression: "AMExpression"
    inputs: tuple[tuple[str, Fraction], ...]
    germ: FirstOrderTaskGerm


@dataclass(frozen=True)
class ReversePullbackPayload:
    """Compact persistent cache used by this declared local reverse task."""

    pullback: tuple[tuple[str, Fraction], ...]


@dataclass(frozen=True)
class MaterializationOption:
    """Normalized persistent-storage/work contract for one segment cache."""

    mode: str
    persistent_scalar_storage: int
    normalized_build_work: int
    normalized_per_reverse_work: int


@dataclass(frozen=True)
class MaterializationPlan:
    normalized_total_work: int
    persistent_scalar_storage: int
    modes: tuple[str, ...]


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


def execute_segments(
    expressions: tuple[AMExpression, ...],
    *,
    initial: Fraction,
    step: Fraction,
) -> tuple[SegmentExecution, ...]:
    """Run the physical history and materialize exact candidate germs."""

    state = Fraction(initial)
    executions = []
    for expression in expressions:
        inputs = {"x": state, "h": Fraction(step)}
        germ = first_order_task_germ(expression, inputs, ("x", "h"))
        executions.append(
            SegmentExecution(expression, tuple(inputs.items()), germ)
        )
        state = germ.endpoint
    return tuple(executions)


def reverse_pullback_payload(
    germ: FirstOrderTaskGerm,
) -> ReversePullbackPayload:
    """Project the semantic germ to the components used by local reverse."""

    return ReversePullbackPayload(germ.pullback)


def materialization_options(
    execution: SegmentExecution,
) -> tuple[MaterializationOption, MaterializationOption]:
    """Compare raw replay with a cached pullback in a normalized cost model.

    Both options use the same task convention: the shared step parameter,
    fixed program identity, and segmentation are task metadata.  A raw cache
    persistently stores one scalar input state.  Reconstructing a local
    pullback performs one normalized forward and one reverse A/M rule per
    primitive, plus one scalar application per declared input.

    The semantic germ remains the auditable object containing basepoint and
    endpoint.  Its materialized reverse cache stores only the unit pullback
    components actually read by ``reverse_materialized_segments``.  It pays a
    fresh normalized forward/reverse construction once, then only applies the
    stored pullback for each same-basepoint query.  These numbers specify an
    algebraic-RAM contract; they do not measure the recursive Python methods.
    """

    payload = reverse_pullback_payload(execution.germ)
    input_count = len(payload.pullback)
    primitive_cost = execution.germ.primitive_cost
    raw = MaterializationOption(
        mode="raw",
        persistent_scalar_storage=1,
        normalized_build_work=0,
        normalized_per_reverse_work=2 * primitive_cost + input_count,
    )
    pullback = MaterializationOption(
        mode="pullback",
        persistent_scalar_storage=len(payload.pullback),
        normalized_build_work=2 * primitive_cost,
        normalized_per_reverse_work=input_count,
    )
    return raw, pullback


def static_materialization_bellman(
    executions: tuple[SegmentExecution, ...],
    *,
    scalar_budget: int,
    reverse_queries: int,
) -> MaterializationPlan:
    """Multiple-choice Bellman gate for payload representation only.

    This is deliberately not a complete checkpoint scheduler or a global
    cache optimizer: segmentation is frozen and every segment receives either
    a raw-state or pullback payload.  C0 owns the classical
    save/restore/recompute schedule.  A future gate may combine the two state
    spaces only after the query family is rich enough to survive the
    whole-chain-germ red team.
    """

    if scalar_budget < 0 or reverse_queries < 1:
        raise ValueError("budget must be nonnegative and queries positive")

    @lru_cache(maxsize=None)
    def solve(index: int, remaining: int):
        if index == len(executions):
            return 0, 0, ()
        candidates = []
        for option in materialization_options(executions[index]):
            if option.persistent_scalar_storage > remaining:
                continue
            suffix = solve(
                index + 1,
                remaining - option.persistent_scalar_storage,
            )
            if suffix is None:
                continue
            suffix_work, suffix_storage, suffix_modes = suffix
            local_work = (
                option.normalized_build_work
                + reverse_queries * option.normalized_per_reverse_work
            )
            candidates.append(
                (
                    local_work + suffix_work,
                    option.persistent_scalar_storage + suffix_storage,
                    (option.mode,) + suffix_modes,
                )
            )
        if not candidates:
            return None
        return min(candidates, key=lambda item: (item[0], item[1], item[2]))

    result = solve(0, scalar_budget)
    if result is None:
        raise ValueError("scalar budget cannot materialize one payload per segment")
    return MaterializationPlan(*result)


def reverse_materialized_segments(
    executions: tuple[SegmentExecution, ...],
    modes: tuple[str, ...],
    terminal_covector: Fraction,
) -> tuple[Fraction, Fraction]:
    """Return pullbacks for initial state and the shared step parameter."""

    if len(executions) != len(modes):
        raise ValueError("one materialization mode is required per segment")
    state_covector = Fraction(terminal_covector)
    step_covector = Fraction(0)
    for execution, mode in zip(reversed(executions), reversed(modes), strict=True):
        if mode == "raw":
            pulled = execution.expression.vjp(dict(execution.inputs), state_covector)
        elif mode == "pullback":
            unit = dict(execution.germ.pullback)
            pulled = {name: value * state_covector for name, value in unit.items()}
        else:
            raise ValueError(f"unknown materialization mode: {mode}")
        state_covector = pulled["x"]
        step_covector += pulled["h"]
    return state_covector, step_covector


def whole_chain_pullback_payload(
    executions: tuple[SegmentExecution, ...],
) -> ReversePullbackPayload:
    """Collapse a terminal-only scalar task to its global unit pullback."""

    state, step = reverse_materialized_segments(
        executions,
        ("raw",) * len(executions),
        Fraction(1),
    )
    return ReversePullbackPayload((
        ("x", state),
        ("h", step),
    ))


def power_euler_am_history(power: int) -> AMExpression:
    """A heterogeneous polynomial step built in the same A/M grammar."""

    if power < 1:
        raise ValueError("power must be positive")
    x = AMExpression.input("x")
    h = AMExpression.input("h")
    power_history = x
    for _ in range(power - 1):
        power_history = power_history * x
    return x + h * (power_history + AMExpression.constant(-2))


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


def test_a3_all_raw_pullback_mixtures_reconstruct_the_same_adjoint():
    expressions = tuple(power_euler_am_history(power) for power in (1, 2, 4))
    initial = Fraction(1, 2)
    step = Fraction(1, 20)
    executions = execute_segments(
        expressions,
        initial=initial,
        step=step,
    )
    terminal_covector = Fraction(13, 11)
    expected = reverse_materialized_segments(
        executions,
        ("raw",) * len(executions),
        terminal_covector,
    )

    composed = expressions[0]
    for expression in expressions[1:]:
        composed = expression.substitute({"x": composed})
    composed_inputs = {"x": initial, "h": step}
    forward_pairing_oracle = (
        terminal_covector
        * composed.jvp(composed_inputs, {"x": 1, "h": 0}).tangent,
        terminal_covector
        * composed.jvp(composed_inputs, {"x": 0, "h": 1}).tangent,
    )
    assert expected == forward_pairing_oracle

    for modes in product(("raw", "pullback"), repeat=len(executions)):
        assert reverse_materialized_segments(
            executions, modes, terminal_covector
        ) == expected


def test_a3_materialization_contract_charges_only_persistent_payload_components():
    execution = execute_segments(
        (power_euler_am_history(2),),
        initial=Fraction(1, 2),
        step=Fraction(1, 20),
    )[0]
    raw, pullback = materialization_options(execution)

    assert raw.persistent_scalar_storage == 1
    assert pullback.persistent_scalar_storage == 2  # dx and dh only.
    assert (
        pullback.normalized_build_work
        == 2 * execution.expression.primitive_cost
    )
    assert (
        raw.normalized_per_reverse_work
        - pullback.normalized_per_reverse_work
        == pullback.normalized_build_work
    )


def test_a3_static_bellman_has_query_dependent_transition_in_frozen_grammar():
    expressions = tuple(power_euler_am_history(power) for power in (1, 2, 4))
    executions = execute_segments(
        expressions,
        initial=Fraction(1, 2),
        step=Fraction(1, 20),
    )
    raw_budget = len(executions)
    one_pullback_budget = raw_budget + 1

    # For one reverse query, building a pullback merely prepays exactly the
    # replay work and consumes more storage, so all-raw is uniquely non-dominated
    # inside the frozen option set.
    once = static_materialization_bellman(
        executions,
        scalar_budget=one_pullback_budget,
        reverse_queries=1,
    )
    assert once.modes == ("raw", "raw", "raw")
    assert once.normalized_total_work == 32
    assert once.persistent_scalar_storage == 3

    # Reusing the same physical trajectory for three adjoint queries makes one
    # cached pullback worthwhile in the normalized table.  With room for
    # exactly one, the DP recovers the optimizer implied by the declared costs.
    repeated = static_materialization_bellman(
        executions,
        scalar_budget=one_pullback_budget,
        reverse_queries=3,
    )
    assert repeated.modes == ("raw", "raw", "pullback")
    assert repeated.normalized_total_work == 72
    assert repeated.persistent_scalar_storage == one_pullback_budget

    all_pullback = static_materialization_bellman(
        executions,
        scalar_budget=2 * len(executions),
        reverse_queries=3,
    )
    assert all_pullback.modes == ("pullback", "pullback", "pullback")
    assert all_pullback.normalized_total_work == 44
    assert all_pullback.normalized_total_work < repeated.normalized_total_work

    try:
        static_materialization_bellman(
            executions,
            scalar_budget=raw_budget - 1,
            reverse_queries=3,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("budget below one raw state per segment must fail")


def test_a3_terminal_only_whole_chain_germ_defeats_the_local_bellman_grammar():
    expressions = tuple(power_euler_am_history(power) for power in (1, 2, 4))
    executions = execute_segments(
        expressions,
        initial=Fraction(1, 2),
        step=Fraction(1, 20),
    )
    queries = 3
    local = static_materialization_bellman(
        executions,
        scalar_budget=2 * len(executions),
        reverse_queries=queries,
    )
    global_payload = whole_chain_pullback_payload(executions)

    # The current task asks only for the pullback of the final scalar endpoint
    # on one fixed trajectory.  A global unit pullback therefore answers every
    # query, but cannot answer future intermediate-stop or local-injection
    # tasks.  This option lies outside the deliberately frozen local grammar.
    global_storage = len(global_payload.pullback)
    global_build_work = sum(
        materialization_options(execution)[0].normalized_per_reverse_work
        for execution in executions
    )
    global_work = global_build_work + queries * global_storage
    seed = Fraction(13, 11)
    unit = dict(global_payload.pullback)
    assert (unit["x"] * seed, unit["h"] * seed) == (
        reverse_materialized_segments(
            executions,
            ("raw",) * len(executions),
            seed,
        )
    )
    assert global_storage == 2
    assert global_storage < local.persistent_scalar_storage
    assert global_build_work == 32
    assert global_work == 38
    assert global_work < local.normalized_total_work
