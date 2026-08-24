"""Executable freeze for the Minimal Hidden A/M Noether Sonnet Phase 0."""

import importlib.util
from pathlib import Path
import sys

import pytest


MODULE_PATH = (
    Path(__file__).parents[2]
    / "sonnet"
    / "hidden-am-noether"
    / "phase0_contract.py"
)
SPEC = importlib.util.spec_from_file_location("hidden_am_noether_phase0", MODULE_PATH)
phase0 = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = phase0
SPEC.loader.exec_module(phase0)


def test_frozen_phase0_grammars_have_exact_auditable_sizes():
    expressions = phase0.expressions_through_depth_one()
    generators = phase0.projective_generator_coefficients()
    observers = phase0.observer_words(max_length=3)

    assert len(expressions) == 80
    assert sum(expression.depth == 0 for expression in expressions) == 8
    assert sum(expression.depth == 1 for expression in expressions) == 72
    assert len(generators) == 40
    assert len(observers) == 1 + 4 + 16 + 64 == 85
    assert len(set(expressions)) == len(expressions)
    assert len(set(generators)) == len(generators)
    assert len(set(observers)) == len(observers)


def test_commutative_syntax_and_projective_sign_are_canonicalized():
    x = phase0.Expression.atom("x")
    y = phase0.Expression.atom("y")
    assert phase0.Expression.binary("add", x, y) == phase0.Expression.binary(
        "add", y, x
    )

    for coefficients in phase0.projective_generator_coefficients():
        assert next(value for value in coefficients if value) == 1
        assert tuple(-value for value in coefficients) not in (
            phase0.projective_generator_coefficients()
        )


def test_oracle_firewall_rejects_answer_leakage():
    phase0.PHASE0_FIREWALL.validate()

    leaked = phase0.OracleFirewall(
        discovery_inputs=frozenset({"raw_expression", "hidden_observer"}),
        hidden_oracles=frozenset({"hidden_observer"}),
    )
    with pytest.raises(ValueError, match="hidden oracle leaked"):
        leaked.validate()


def test_bounds_reject_silent_grammar_expansion():
    x = phase0.Expression.atom("x")
    with pytest.raises(ValueError, match="outside the frozen grammar"):
        phase0.Expression.atom("sin(x)")
    with pytest.raises(ValueError, match="outside the frozen grammar"):
        phase0.Expression.binary("sqrt", x, x)
    with pytest.raises(ValueError, match="non-negative"):
        phase0.observer_words(max_length=-1)
