"""A/M-first checkpointing A1--A2: history jets and differential task quotient.

Problem
-------
For a nonlinear time step written only with Addition and Multiplication, what
is the smallest materialized history object sufficient for a first-order
reverse/adjoint task?  The classical answer starts from a Jacobian.  This
calibration instead starts from a free A/M expression history and derives its
value and variation compositionally.

Domains / classical names
-------------------------
Automatic differentiation, tangent and cotangent lift, straight-line program,
checkpointing, affine group, semidirect product.

Process Geometry roles
----------------------
Free A/M history, analytic rank lowering, differential task quotient,
objectified segment jet, minimal process completion, Bellman checkpoint
payload.  Theory Map relation: first research-local V5 pressure; no API and no
claim of A/M universality.

Primitive firewall
------------------
Discovery receives only constants, one state atom, and binary Add/Mul nodes.
``AMExpression.jet`` implements the Addition rule and Multiplication Leibniz
rule directly.  It does not call symbolic differentiation, finite differences,
or a supplied Jacobian.  The dual pullback is obtained from that generated
variation.  Closed-form derivatives appear only as post-hoc assertions.

Claim boundary
--------------
The first jet is sufficient only for the frozen scalar first-order adjoint
task at a declared anchor.  It is not a global function quotient and is not
sufficient for Hessian tasks.  The affine A/M order test is a finite
semidirect-product calibration, not a general noncommutative AD theorem.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from process_geometry.process.history import ProcessWord


@dataclass(frozen=True)
class AMJet:
    """Research-local value/first-variation object."""

    value: Fraction
    tangent: Fraction

    def pullback(self, covector: Fraction) -> Fraction:
        return self.tangent * covector


@dataclass(frozen=True)
class AMExpression:
    """Free binary A/M expression history; no derivative is stored in syntax."""

    operation: str
    arguments: tuple["AMExpression", ...] = ()
    atom: Fraction | None = None

    @classmethod
    def state(cls) -> "AMExpression":
        return cls("state")

    @classmethod
    def constant(cls, value) -> "AMExpression":
        return cls("constant", atom=Fraction(value))

    def __add__(self, other: "AMExpression") -> "AMExpression":
        return AMExpression("add", (self, other))

    def __mul__(self, other: "AMExpression") -> "AMExpression":
        return AMExpression("mul", (self, other))

    def jet(self, anchor: Fraction) -> AMJet:
        if self.operation == "state":
            return AMJet(anchor, Fraction(1))
        if self.operation == "constant":
            assert self.atom is not None
            return AMJet(self.atom, Fraction(0))

        left = self.arguments[0].jet(anchor)
        right = self.arguments[1].jet(anchor)
        if self.operation == "add":
            return AMJet(left.value + right.value, left.tangent + right.tangent)
        if self.operation == "mul":
            return AMJet(
                left.value * right.value,
                left.tangent * right.value + left.value * right.tangent,
            )
        raise ValueError(f"unknown A/M operation: {self.operation}")


def euler_am_history(step: Fraction) -> AMExpression:
    """Build ``x + step*(x*x - 2)`` without supplying its derivative."""

    x = AMExpression.state()
    return x + AMExpression.constant(step) * (
        x * x + AMExpression.constant(-2)
    )


def compose_local_jets(jets: tuple[AMJet, ...]) -> Fraction:
    """Objectified rank-lowering law for a scalar first-order pullback."""

    tangent = Fraction(1)
    for jet in jets:
        tangent *= jet.tangent
    return tangent


def iterate_am_history(
    expression: AMExpression,
    initial: Fraction,
    count: int,
) -> tuple[Fraction, tuple[AMJet, ...]]:
    state = initial
    jets = []
    for _ in range(count):
        jet = expression.jet(state)
        jets.append(jet)
        state = jet.value
    return state, tuple(jets)


@dataclass(frozen=True)
class Translation:
    amount: Fraction


@dataclass(frozen=True)
class Dilation:
    scale: Fraction

    def __post_init__(self) -> None:
        if self.scale == 0:
            raise ValueError("dilation scale must be nonzero")


AMStep = Translation | Dilation


@dataclass(frozen=True)
class AffineDifferentialPrimitive:
    """Objectified finite A/M history and its cotangent action."""

    scale: Fraction = Fraction(1)
    shift: Fraction = Fraction(0)

    def apply(self, value: Fraction) -> Fraction:
        return self.scale * value + self.shift

    def pullback(self, covector: Fraction) -> Fraction:
        return self.scale * covector

    def then(
        self, later: "AffineDifferentialPrimitive"
    ) -> "AffineDifferentialPrimitive":
        return AffineDifferentialPrimitive(
            scale=later.scale * self.scale,
            shift=later.scale * self.shift + later.shift,
        )


def objectify_am_history(
    history: ProcessWord[AMStep],
) -> AffineDifferentialPrimitive:
    primitive = AffineDifferentialPrimitive()
    for step in history:
        if isinstance(step, Translation):
            lowered = AffineDifferentialPrimitive(shift=step.amount)
        elif isinstance(step, Dilation):
            lowered = AffineDifferentialPrimitive(scale=step.scale)
        else:  # pragma: no cover - protects the local grammar boundary.
            raise TypeError(f"unsupported A/M step: {step!r}")
        primitive = primitive.then(lowered)
    return primitive


def test_am_history_rules_generate_the_euler_value_tangent_and_pullback():
    dt = Fraction(1, 10)
    anchor = Fraction(3, 5)
    history = euler_am_history(dt)
    jet = history.jet(anchor)

    assert jet.value == anchor + dt * (anchor**2 - 2)
    assert jet.tangent == 1 + 2 * dt * anchor
    assert jet.pullback(Fraction(7, 3)) == (1 + 2 * dt * anchor) * Fraction(7, 3)


def test_objectified_local_jets_reconstruct_a_multistep_adjoint_exactly():
    history = euler_am_history(Fraction(1, 20))
    _terminal, jets = iterate_am_history(history, Fraction(1, 2), 5)
    terminal_covector = Fraction(11, 7)

    explicit = terminal_covector
    for jet in reversed(jets):
        explicit = jet.pullback(explicit)

    objectified = compose_local_jets(jets) * terminal_covector
    assert objectified == explicit


def test_differential_task_quotient_is_finer_than_endpoint_at_one_anchor():
    anchor = Fraction(2)
    endpoint_only_left = ProcessWord((Translation(Fraction(1)),))
    endpoint_only_right = ProcessWord(
        (Dilation(Fraction(2)), Translation(Fraction(-1)))
    )
    left = objectify_am_history(endpoint_only_left)
    right = objectify_am_history(endpoint_only_right)

    # Both histories reach 3 from the declared checkpoint anchor.
    assert left.apply(anchor) == right.apply(anchor) == 3

    # The first-order adjoint task separates them: their cotangent actions are
    # different.  Endpoint canonicalization would be an invalid checkpoint
    # quotient for this task.
    assert left.pullback(Fraction(1)) == 1
    assert right.pullback(Fraction(1)) == 2


def test_finite_am_order_requires_the_semidirect_correction():
    translate_then_dilate = ProcessWord(
        (Translation(Fraction(1)), Dilation(Fraction(2)))
    )
    dilate_then_translate = ProcessWord(
        (Dilation(Fraction(2)), Translation(Fraction(1)))
    )
    corrected = ProcessWord(
        (Dilation(Fraction(2)), Translation(Fraction(2)))
    )

    left = objectify_am_history(translate_then_dilate)
    wrong_commutation = objectify_am_history(dilate_then_translate)
    right = objectify_am_history(corrected)

    assert left != wrong_commutation
    assert left == right
    assert left == AffineDifferentialPrimitive(scale=2, shift=2)


def test_first_jet_objectification_has_a_hessian_completion_boundary():
    x = AMExpression.state()
    square = x * x
    tangent_line_at_one = AMExpression.constant(2) * x + AMExpression.constant(-1)

    # A frozen first-order task at x=1 identifies these histories.
    assert square.jet(Fraction(1)) == tangent_line_at_one.jet(Fraction(1)) == AMJet(1, 2)

    # A nearby continuation separates them, witnessing the missing second-order
    # residual.  First-jet objectification must not be promoted to a Hessian or
    # global-function quotient.
    nearby = Fraction(3, 2)
    assert square.jet(nearby).value != tangent_line_at_one.jet(nearby).value

