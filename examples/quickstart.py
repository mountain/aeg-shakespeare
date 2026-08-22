"""Minimal AEG Shakespeare 0.0.1 quickstart.

The example is intentionally small and problem-independent. It demonstrates
three layers without asking the reader to accept a named classical solver:
literal history, an explicitly declared history relation, and the
Addition/Multiplication function-theory branch.
"""

import sympy as sp

from aeg_shakespeare import (
    AMFunctionTheory,
    ProcessWord,
    WordRewriteRule,
    normalize_word,
)


# Literal histories come first. This example relation is merely caller-declared;
# it is not the A/M arithmetic relation used below.
history = ProcessWord(("P", "Q", "P"))
relation = WordRewriteRule(
    ProcessWord(("P", "Q")),
    ProcessWord(("R",)),
    name="objectify-PQ",
)
normalized = normalize_word(history, (relation,), max_steps=8)
print("literal:", history.steps)
print("rewritten:", normalized.normal_form.steps)
print("rewrite trace length:", normalized.rewrite_steps)


# A/M means Addition/Multiplication. The arithmetic relation [A, M] = A is
# checked as a consequence of the concrete process frame.
a, v = sp.symbols("a v")
theory = AMFunctionTheory(a, v)
expr = a**2 * v
print("[A,M]f - Af =", sp.simplify(theory.commutator(expr) - theory.A(expr)))


# Resonance creates a new function type instead of being inserted by name.
resonant = theory.A_primitive(theory.power_weight(-1, 0))
print("A-resonant primitive:", resonant.expression)
print("certificate residual:", theory.primitive_residual(resonant))
