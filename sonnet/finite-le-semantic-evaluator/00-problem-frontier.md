# Finite LE semantic evaluator

## Question

Can the carrier compiler's syntax-level C2 decision be upgraded to an exact
semantic result for a useful finite log--exp fragment, without introducing a
general transseries or surreal runtime?

The frozen regime is real `N -> +infinity`.  Rational linear exponential rates
derive one chart

\[
t=\exp(-N/q)\longrightarrow 0^+,
\]

where `q` is the least common denominator forced by the source.  Admissible
expressions are rewritten into a finite Laurent/Taylor band in `t`; exact
valuation comparison, branch witnesses, cancellation depth, residual order,
and replay are mandatory.

## Why this is the next gate

Issue #142 classified the held-out L1 source as finite-height C2, but the
compiler did not compute its requested limit.  This workstream succeeds only
if the compiler itself returns exact semantic readouts such as

\[
\exp\!\left(\exp(N+2e^{-N})-\exp(N)\right)\to e^2
\]

and

\[
e^{3N}\!\left(\log(1+e^{-N})-e^{-N}+\frac12e^{-2N}\right)\to\frac13.
\]

It complements #140's chart-discovery work.  It does not yet attempt symbolic
height or distinguish hyperseries from surreal numbers.

## Evidence discipline

- grammar, domains, chart rule, order propagation, budgets, controls, and
  held-out commitment freeze before code;
- no `sympy.limit` is allowed in compiler or replay;
- the certificate cannot store the expected answer or full expansion trace;
- the same-information SymPy result is a baseline, not an oracle;
- a self-committed held-out receives no independent-agent discovery credit;
- Core, Theory Map, Experimental, and Public API remain unchanged.

The machine-readable contract and corpus live in
[`workstreams/finite_le_semantics/`](../../workstreams/finite_le_semantics/).
