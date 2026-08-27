# Finite LE semantic evaluator: T1 results

## Disposition: EXPAND

The frozen evaluator completes the declared real, rational-rate,
single-exponential-chart task family with replayable semantic evidence. This
is an expansion relative to the carrier compiler: admissible C2 sources now
receive exact limits, chart derivations, finite normal forms, branch witnesses,
residuals, costs, and independently recomputed replay decisions.

The word **EXPAND** is local to this frozen task family. It is not evidence for
a general LE field, transseries, hyperseries, surreal arithmetic, symbolic
height, arbitrary nesting, or a new complexity class.

## Commit--reveal result

The preimplementation commitment was
`eedef97f8071ea3da687a805b7ea3e8385aa49c0829f2c962a3c6bc8ec181655`.
The evaluator source was remotely frozen at commit
`5df657d450233e14fa6d77a1efb5be36d6bc02e6` before the payload was revealed.
Canonical serialization of the reveal reproduces the commitment.

The held-out source

\[
e^{5N/3}\left(\log(1+e^{-N/3})-e^{-N/3}
+\frac12e^{-2N/3}-\frac13e^{-N}+\frac14e^{-4N/3}\right)
\]

was evaluated without a grammar, budget, or scoring change. The compiler
derived

\[
t=e^{-N/3}\to0^+,
\qquad
\frac15-\frac16t+O(t^2),
\qquad
\lim_{N\to\infty}=\frac15.
\]

It recorded cancellation jump 4, one real-positive logarithm witness, an
1182-byte certificate, and a valid 69-step replay. This is a self-committed
held-out, so it supplies generalization evidence but no independent-discovery
credit.

## Frozen controls

| Gate | Result |
| --- | --- |
| mixed exponential nesting | exact `exp(2)`, replayed |
| third-order log cancellation | exact `1/3`, cancellation jump 2, replayed |
| mixed rational rates | derived `q=6`, exact `1`, replayed |
| missing log positivity | typed fail-closed rejection |
| irrational rate | typed fail-closed rejection |
| nested unbounded exponential scale | typed fail-closed rejection |
| symbolic height | typed fail-closed rejection |
| order and denominator budgets | typed resource failures in unit tests |
| tampered chart/result/residual/domain/cost/digest | replay rejection |

The same-information SymPy baseline computes every expected numerical value,
including the held-out `1/5`. Therefore this stage does **not** establish a raw
computability or speed advantage over a mature computer-algebra system. The
added capability is an explicit semantic boundary and a compact,
deterministically replayed evidence object that can discharge exactly three
C2 obligations inside that boundary.

## What changed in the larger programme

The result supports a layered architecture:

1. the carrier compiler decides whether a finite source needs this chart;
2. this evaluator supplies exact semantics for the bounded C2 fragment;
3. unsupported symbolic-height or higher-scale inputs remain explicit research
   obligations rather than being routed to surreal numbers by default.

Surreal numbers played no substantive computational role in this result. The
experiment instead identifies a sharper possible role for them: only after a
future frozen task defeats finite chart derivation or requires genuinely
symbolic height should a larger carrier be charged to the computation.

## Next gate

Do not generalize the runtime yet. The next responsible benchmark should test
whether the evaluator can *discover* a chart from observer equivalence and
transport the resulting certificate across two independently encoded source
forms. Freeze those paired sources and the transport criterion before code.
That would test reusable representation change rather than another curated
limit identity.
