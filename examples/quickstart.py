"""Minimal AEG Shakespeare 0.0.1 quickstart.

The example is intentionally small and problem-independent.  It demonstrates
three layers without asking the reader to accept a named classical solver:
ordered history, an explicit history relation, and the Addition/Multiplication
function-theory branch.
"""

import sympy as sp

from aeg_shakespeare import (
    AMFunctionTheory,
    ProcessWord,
    WordRewriteRule,
    normalize_word,
)


# Literal histories come first.  Nothing here says A and M commute.
history = ProcessWord(("A", "M", "A"))
relation = WordRewriteRule(ProcessWord(("A", "M")), ProcessWord(("M", "A", "A")))
normalized = normalize_word(history, (relation,), max_steps=8)
print("literal:", history.steps)
print("rewritten:", normalized.normal_form.steps)


# A/M means Addition/Multiplication.  The arithmetic relation [A, M] = A is
# checked as a consequence of the concrete process frame.
a, v = sp.symbols("a v")
theory = AMFunctionTheory(a, v)
expr = a**2 * v
print("[A,M]f - Af =", sp.simplify(theory.commutator(expr) - theory.A(expr)))


# Resonance creates a new function type instead of being inserted by name.
resonant = theory.A_primitive(theory.power_weight(-1, 0))
print("A-resonant primitive:", resonant.expression)
print("certificate residual:", theory.primitive_residual(resonant))
