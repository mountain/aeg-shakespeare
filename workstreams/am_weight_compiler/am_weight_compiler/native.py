from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import prod
from typing import Mapping

from .model import ExpQCoefficient, EvaluationFailure, fraction_text, parse_fraction


@dataclass(frozen=True)
class AMTerm:
    nu: int
    weight: Fraction
    coefficient: Fraction

    @classmethod
    def decode(cls, value: Mapping[str, object], *, max_abs_power: int) -> "AMTerm":
        nu_value = value.get("nu")
        if isinstance(nu_value, bool) or not isinstance(nu_value, int):
            raise ValueError("nu must be an integer")
        if abs(nu_value) > max_abs_power:
            raise EvaluationFailure("resource_exceeded", "power-budget-exceeded")
        basis = value.get("basis")
        if basis == "power-weight":
            weight = parse_fraction(value.get("weight"), field="weight")
        elif basis == "power-character":
            character = parse_fraction(value.get("character"), field="character")
            weight = Fraction(nu_value) + character
        else:
            raise EvaluationFailure("unsupported", "unknown-am-basis")
        return cls(
            nu=nu_value,
            weight=weight,
            coefficient=parse_fraction(value.get("coefficient"), field="coefficient"),
        )

    @property
    def character(self) -> Fraction:
        return self.weight - self.nu

    def multiply(self, other: "AMTerm") -> "AMTerm":
        return AMTerm(
            nu=self.nu + other.nu,
            weight=self.weight + other.weight,
            coefficient=self.coefficient * other.coefficient,
        )

    def apply_A(self) -> "AMTerm":
        return AMTerm(
            nu=self.nu - 1,
            weight=self.weight - 1,
            coefficient=self.coefficient * self.nu,
        )

    def apply_M(self) -> "AMTerm":
        return AMTerm(
            nu=self.nu,
            weight=self.weight,
            coefficient=self.coefficient * self.weight,
        )

    def as_dict(self) -> dict[str, object]:
        return {
            "nu": self.nu,
            "weight": fraction_text(self.weight),
            "coefficient": fraction_text(self.coefficient),
        }


def falling(value: Fraction | int, length: int) -> Fraction:
    return prod((Fraction(value) - offset for offset in range(length)), start=Fraction(1))


def pbw_identity(term: AMTerm, a_power: int, m_power: int) -> bool:
    """Check A^m M^n = (M+m)^n A^m on one exact weight vector."""

    left = falling(term.nu, a_power) * term.weight**m_power
    lowered_weight = term.weight - a_power
    right = falling(term.nu, a_power) * (lowered_weight + a_power) ** m_power
    return left == right


def finite_affine_relation(translation: Fraction, scale: Fraction) -> bool:
    """Check normal forms for S_s T_t = T_(exp(s)t) S_s."""

    left_translation = ExpQCoefficient.exp_atom(scale).scale_rational(translation)
    right_translation = ExpQCoefficient.rational(translation) * ExpQCoefficient.exp_atom(scale)
    return left_translation == right_translation


def primitive(term: AMTerm, generator: str, extension_policy: str) -> dict[str, object]:
    allow_typed = extension_policy == "allow-typed"
    if generator == "A":
        if term.nu == -1:
            if not allow_typed:
                raise EvaluationFailure("unsupported", "resonance-extension-required")
            return {"extension": "log-a", "domain_witness": "a>0"}
        return {
            "extension": "ordinary-power-weight",
            "term": AMTerm(
                nu=term.nu + 1,
                weight=term.weight + 1,
                coefficient=term.coefficient / (term.nu + 1),
            ).as_dict(),
        }
    if generator == "M":
        if term.weight == 0:
            if not allow_typed:
                raise EvaluationFailure("unsupported", "resonance-extension-required")
            return {"extension": "v-jordan"}
        return {
            "extension": "ordinary-power-weight",
            "term": AMTerm(
                nu=term.nu,
                weight=term.weight,
                coefficient=term.coefficient / term.weight,
            ).as_dict(),
        }
    raise EvaluationFailure("unsupported", "unknown-primitive-generator")
