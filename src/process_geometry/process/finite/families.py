"""Finite parameterized process families and their scalar responses.

This module is deliberately smaller than a group-, representation-, or harmonic-
analysis framework.  It records only the structure forced by the Translation,
Dilation, and Addition/Multiplication calibration sequence:

* a named finite process family whose parameters have an explicit composition
  law;
* scalar multiplicative responses to one family;
* an action of one family on the parameter space of another; and
* transport/compatibility checks for those scalar responses.

Topology, measure, inverses, Lie theory, spectra, Fourier transforms, and
operator-valued representations are intentionally absent.  They should enter
only when later mathematical vignettes require them.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, Generic, Sequence, TypeVar

import sympy as sp

ParamT = TypeVar("ParamT")
ActingParamT = TypeVar("ActingParamT")
TargetParamT = TypeVar("TargetParamT")


def _default_parameter_equivalence(left, right) -> bool:
    """Small exact/symbolic equality helper for family parameters.

    Tuples are compared componentwise.  Scalar symbolic values are compared by
    simplifying their difference when possible.  Callers with richer parameter
    objects may supply their own equivalence predicate to ``ProcessFamily``.
    """

    if isinstance(left, tuple) and isinstance(right, tuple):
        return len(left) == len(right) and all(
            _default_parameter_equivalence(a, b) for a, b in zip(left, right)
        )
    try:
        return sp.simplify(sp.sympify(left) - sp.sympify(right)) == 0
    except (TypeError, ValueError, sp.SympifyError):
        return left == right


@dataclass(frozen=True)
class FamilyStep(Generic[ParamT]):
    """One finite step from a named parameterized process family."""

    family_name: str
    parameter: ParamT


@dataclass(frozen=True)
class ProcessFamily(Generic[ParamT]):
    """A finite process family with an explicit parameter-composition law.

    ``ProcessFamily`` intentionally does not assert that the parameters form a
    group.  A family may later turn out to have identities, inverses, topology,
    or measure, but none of those structures are required here.
    """

    name: str
    combine: Callable[[ParamT, ParamT], ParamT] = field(repr=False, compare=False)
    identity: ParamT | None = None
    equivalent: Callable[[ParamT, ParamT], bool] | None = field(
        default=None,
        repr=False,
        compare=False,
    )

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("process-family name must be non-empty")

    def step(self, parameter: ParamT) -> FamilyStep[ParamT]:
        return FamilyStep(self.name, parameter)

    def compose_parameters(self, left: ParamT, right: ParamT) -> ParamT:
        """Parameter of the composed finite process ``F_left F_right``."""

        return self.combine(left, right)

    def parameters_equivalent(self, left: ParamT, right: ParamT) -> bool:
        predicate = self.equivalent or _default_parameter_equivalence
        return bool(predicate(left, right))

    def fold_parameters(self, parameters: Sequence[ParamT]) -> ParamT:
        """Reduce an ordered same-family history to one family parameter."""

        parameters = tuple(parameters)
        if not parameters:
            if self.identity is None:
                raise ValueError("empty family history requires a declared identity")
            return self.identity
        value = parameters[0]
        for parameter in parameters[1:]:
            value = self.compose_parameters(value, parameter)
        return value


@dataclass(frozen=True)
class ProcessCharacter(Generic[ParamT]):
    """A SymPy-valued scalar response candidate for one finite process family.

    The defining mathematical test is multiplicativity with respect to the
    family's own composition law.  Analytic regularity and completeness are not
    part of this object.
    """

    family: ProcessFamily[ParamT]
    response: Callable[[ParamT], sp.Expr] = field(repr=False, compare=False)
    label: object | None = None
    simplify: Callable[[sp.Expr], sp.Expr] = field(
        default=sp.simplify,
        repr=False,
        compare=False,
    )

    def value(self, parameter: ParamT) -> sp.Expr:
        return sp.sympify(self.response(parameter))

    def multiplicativity_residual(self, left: ParamT, right: ParamT) -> sp.Expr:
        combined = self.family.compose_parameters(left, right)
        residual = self.value(combined) - self.value(left) * self.value(right)
        return sp.sympify(self.simplify(residual))

    def normalization_residual(self) -> sp.Expr:
        if self.family.identity is None:
            raise ValueError("character normalization requires a declared family identity")
        return sp.sympify(self.simplify(self.value(self.family.identity) - 1))


@dataclass(frozen=True)
class CharacterVerification:
    """Exact residual certificate for a bounded character check."""

    multiplicativity_residuals: tuple[sp.Expr, ...]
    normalization_residual: sp.Expr | None = None

    @property
    def exact(self) -> bool:
        return all(residual == 0 for residual in self.multiplicativity_residuals) and (
            self.normalization_residual in (None, 0)
        )


def verify_process_character(
    character: ProcessCharacter[ParamT],
    parameter_pairs: Sequence[tuple[ParamT, ParamT]],
    *,
    check_identity: bool = True,
) -> CharacterVerification:
    """Verify multiplicativity on caller-supplied parameter pairs.

    This is a bounded exact certificate, not a proof over an unbounded parameter
    domain unless the supplied symbolic pairs themselves establish such an
    identity through the backend simplifier.
    """

    residuals = tuple(
        character.multiplicativity_residual(left, right)
        for left, right in parameter_pairs
    )
    normalization = None
    if check_identity and character.family.identity is not None:
        normalization = character.normalization_residual()
    return CharacterVerification(residuals, normalization)


@dataclass(frozen=True)
class FamilyAction(Generic[ActingParamT, TargetParamT]):
    """An explicit action of one process family on another family's parameters.

    For a left action ``alpha`` the intended law is

    ``alpha(g*h, b) = alpha(g, alpha(h, b))``

    together with preservation of the target-family composition law.  The
    action itself is primary; no semidirect-product or group object is created.
    """

    acting: ProcessFamily[ActingParamT]
    target: ProcessFamily[TargetParamT]
    apply: Callable[[ActingParamT, TargetParamT], TargetParamT] = field(
        repr=False,
        compare=False,
    )
    name: str = "action"

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("family-action name must be non-empty")

    def transport_parameter(
        self,
        acting_parameter: ActingParamT,
        target_parameter: TargetParamT,
    ) -> TargetParamT:
        return self.apply(acting_parameter, target_parameter)


@dataclass(frozen=True)
class FamilyActionVerification:
    """Bounded law certificate for a ``FamilyAction``."""

    target_homomorphism_checks: tuple[bool, ...]
    acting_composition_checks: tuple[bool, ...]
    identity_checks: tuple[bool, ...] = ()

    @property
    def exact(self) -> bool:
        return all(
            (*self.target_homomorphism_checks, *self.acting_composition_checks, *self.identity_checks)
        )


def verify_family_action(
    action: FamilyAction[ActingParamT, TargetParamT],
    *,
    acting_parameters: Sequence[ActingParamT] = (),
    acting_pairs: Sequence[tuple[ActingParamT, ActingParamT]] = (),
    target_parameters: Sequence[TargetParamT] = (),
    target_pairs: Sequence[tuple[TargetParamT, TargetParamT]] = (),
    check_identities: bool = True,
) -> FamilyActionVerification:
    """Verify the two elementary finite-action laws on supplied samples."""

    target_checks: list[bool] = []
    for acting_parameter in acting_parameters:
        for left, right in target_pairs:
            lhs = action.transport_parameter(
                acting_parameter,
                action.target.compose_parameters(left, right),
            )
            rhs = action.target.compose_parameters(
                action.transport_parameter(acting_parameter, left),
                action.transport_parameter(acting_parameter, right),
            )
            target_checks.append(action.target.parameters_equivalent(lhs, rhs))

    acting_checks: list[bool] = []
    for left, right in acting_pairs:
        combined = action.acting.compose_parameters(left, right)
        for target_parameter in target_parameters:
            lhs = action.transport_parameter(combined, target_parameter)
            rhs = action.transport_parameter(
                left,
                action.transport_parameter(right, target_parameter),
            )
            acting_checks.append(action.target.parameters_equivalent(lhs, rhs))

    identity_checks: list[bool] = []
    if check_identities:
        if action.acting.identity is not None:
            for target_parameter in target_parameters:
                image = action.transport_parameter(action.acting.identity, target_parameter)
                identity_checks.append(
                    action.target.parameters_equivalent(image, target_parameter)
                )
        if action.target.identity is not None:
            for acting_parameter in acting_parameters:
                image = action.transport_parameter(
                    acting_parameter,
                    action.target.identity,
                )
                identity_checks.append(
                    action.target.parameters_equivalent(image, action.target.identity)
                )

    return FamilyActionVerification(
        target_homomorphism_checks=tuple(target_checks),
        acting_composition_checks=tuple(acting_checks),
        identity_checks=tuple(identity_checks),
    )


def transport_process_character(
    character: ProcessCharacter[TargetParamT],
    action: FamilyAction[ActingParamT, TargetParamT],
    acting_parameter: ActingParamT,
    *,
    label: object | None = None,
) -> ProcessCharacter[TargetParamT]:
    """Pull a target-family character along one finite family action."""

    if action.target.name != character.family.name:
        raise ValueError("family action target must match character family")
    transported_label = label
    if transported_label is None:
        transported_label = (action.name, acting_parameter, character.label)
    return ProcessCharacter(
        family=character.family,
        response=lambda parameter: character.value(
            action.transport_parameter(acting_parameter, parameter)
        ),
        label=transported_label,
        simplify=character.simplify,
    )


def character_invariance_residual(
    character: ProcessCharacter[TargetParamT],
    action: FamilyAction[ActingParamT, TargetParamT],
    acting_parameter: ActingParamT,
    target_parameter: TargetParamT,
) -> sp.Expr:
    """Residual for whether a scalar character survives a family action unchanged.

    Nonzero residual is an obstruction to treating the target character as an
    action-invariant scalar response of the combined finite process structure.
    """

    transported = transport_process_character(character, action, acting_parameter)
    residual = transported.value(target_parameter) - character.value(target_parameter)
    return sp.sympify(character.simplify(residual))
