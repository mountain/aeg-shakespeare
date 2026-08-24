"""Finite Phase-0 contract for the Minimal Hidden A/M Noether Sonnet."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement, product


ATOMS = ("x", "y", "vx", "vy", "-2", "-1", "1", "2")
OPERATIONS = ("add", "mul")
GENERATORS = ("A_x", "M_x", "A_y", "M_y")


@dataclass(frozen=True, order=True)
class Expression:
    operation: str
    arguments: tuple["Expression", ...] = ()

    @classmethod
    def atom(cls, name: str) -> "Expression":
        if name not in ATOMS:
            raise ValueError(f"atom is outside the frozen grammar: {name!r}")
        return cls(name)

    @classmethod
    def binary(cls, operation: str, left: "Expression", right: "Expression"):
        if operation not in OPERATIONS:
            raise ValueError(f"operation is outside the frozen grammar: {operation!r}")
        first, second = sorted((left, right))
        return cls(operation, (first, second))

    @property
    def depth(self) -> int:
        if not self.arguments:
            return 0
        return 1 + max(argument.depth for argument in self.arguments)


def expressions_through_depth_one() -> tuple[Expression, ...]:
    atoms = tuple(Expression.atom(name) for name in ATOMS)
    binary = {
        Expression.binary(operation, left, right)
        for operation in OPERATIONS
        for left, right in combinations_with_replacement(atoms, 2)
    }
    return tuple(sorted(set(atoms) | binary))


def projective_generator_coefficients() -> tuple[tuple[int, ...], ...]:
    """Nonzero {-1,0,1}^4 vectors modulo multiplication by -1."""

    representatives = []
    for coefficients in product((-1, 0, 1), repeat=len(GENERATORS)):
        if not any(coefficients):
            continue
        first_nonzero = next(value for value in coefficients if value)
        if first_nonzero == 1:
            representatives.append(coefficients)
    return tuple(representatives)


def observer_words(max_length: int = 3) -> tuple[tuple[str, ...], ...]:
    if max_length < 0:
        raise ValueError("observer word bound must be non-negative")
    return tuple(
        word
        for length in range(max_length + 1)
        for word in product(GENERATORS, repeat=length)
    )


@dataclass(frozen=True)
class OracleFirewall:
    discovery_inputs: frozenset[str]
    hidden_oracles: frozenset[str]

    def validate(self) -> None:
        leaked = self.discovery_inputs & self.hidden_oracles
        if leaked:
            raise ValueError(f"hidden oracle leaked into discovery inputs: {sorted(leaked)}")


PHASE0_FIREWALL = OracleFirewall(
    discovery_inputs=frozenset(
        {
            "raw_expression",
            "am_generator_grammar",
            "observer_word_grammar",
            "task_equivalence",
            "exact_residual_backend",
        }
    ),
    hidden_oracles=frozenset(
        {
            "hidden_observer",
            "classical_noether_charge",
            "preselected_cyclic_coordinate",
            "lie_solver_output",
            "frontier_witness",
        }
    ),
)

