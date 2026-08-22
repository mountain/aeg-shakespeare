"""Minimal AEG Shakespeare quickstart using the semantic public namespaces.

The example is intentionally small and problem-independent. It demonstrates
three layers without asking the reader to accept a named classical solver:
literal process history, an explicitly declared presentation relation, and the
Addition/Multiplication analysis branch.
"""

import sympy as sp

from aeg_shakespeare.analysis.am import AMFunctionTheory
from aeg_shakespeare.presentation.history import WordRewriteRule, normalize_word
from aeg_shakespeare.process.history import ProcessWord


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
