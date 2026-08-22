"""Generated-grammar quickstart for AEG Shakespeare 0.0.1.

The process rule is supplied first.  Shakespeare grows the finite grammar from a
seed, discovers a grammar-wide return relation, factors it, and returns a
presentation.  The example deliberately avoids naming the classical spectral
interpretation of the recurrence.
"""

import sympy as sp

from aeg_shakespeare import ProcessSystem, SearchBudget, discover_generated_presentation

x, p = sp.symbols("x p")
system = ProcessSystem((x, p), {x: p, p: -x}, name="R")
budget = SearchBudget(max_history_depth=6, max_expression_degree=3, max_relation_order=8)

presentation = discover_generated_presentation(system, (x**3,), budget=budget)
print("closed:", presentation.grammar.closed)
print("grammar dimension:", presentation.grammar.dimension)
if presentation.relations is not None:
    D = sp.Symbol("D")
    print("process relation:", presentation.relations.global_relation.as_expr(D))
