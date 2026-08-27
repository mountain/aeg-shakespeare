# Observer-driven scale and chart compiler

This directory is a research-local prototype.  It tests one claim: a task
observer can control scale retention and chart discovery before Process
Geometry commits to a larger compiler architecture.  It is not an
Experimental or Public API.

## Problem contract

Inputs are:

1. a finite expression built from constants, variables, addition,
   multiplication, integer/general powers, `exp`, and `log`;
2. scale bindings in the convention `N -> +infinity`, with `Scale(p) = N^p`;
3. an `Observer` declaring the visible order, required residual order, and a
   finite expansion budget;
4. for chart discovery, the unknown scale variables and any fixed scales.

The exact S0 grammar, regimes, budgets, output states, and hidden-answer rules
are machine-readably frozen in `FROZEN_CONTRACT.json`.  Inputs are declared
dimensionless in this prototype; dimensional lowering is outside the grammar.

Outputs are a result or an explicit failure, a residual ledger, visibility
events, compiler decisions, and simple operation/term counts.

## Representation

`ir.py` supplies the finite log-exp/power expression IR.  `scale.py` separates:

- `Scale`: exact rational polynomial orders;
- `Observer`: task precision and finite budget;
- `Series`: finite exact generalized-power terms plus a big-O remainder;
- `Residual`: what remains after propagation;
- `VisibilityEvent`: a locally hidden term that later becomes visible.

The IR can state larger log-exp expressions.  The evaluator currently computes
the polynomial-scale germ around bounded `exp` arguments and `log(1+u)`.
Positive-order exponential growth is intentionally a typed unsupported case.

## Algorithm

The evaluator does **delayed truncation**.  It carries intermediate terms
through the complete expression and lowers a non-integer power as

```text
pow(base, exponent) -> exp(exponent * log(base)).
```

Only then does it compare output terms with the observer contract.  Taylor
depth is doubled until the residual target is met or the finite budget is
exhausted.  Thus the input perturbation in

```text
(1 + N^-1)^N
```

is not discarded at local visible order `N^0`: multiplication by the exponent
raises its effect from `N^-1` to `N^0`, and the result has constant term `e`.

Forward values and backward obligations are different records.  The backward
pass derives that a `N^0` output observation of this power needs the near-unit
base down to `N^-1`; it does not infer that obligation by first truncating the
base.  Addition conservatively retains tied/cancelling children, multiplication
subtracts the other factors' orders, and bounded local `exp`/`log` transport the
requested band.  These are finite rules under test, not a general calculus.

For an exponential phase, `balance.py` distributes polynomial terms and writes
one exact rational scale equation per active monomial.  The default task is to
make every exponent-driving term `O(1)`.  Applied to

```text
exp(-N * (t^3/3 - z*t))
```

it derives, rather than receives, the equations

```text
1 + 3 scale(t) = 0
1 + scale(t) + scale(z) = 0
```

and hence `scale(t) = -1/3`, `scale(z) = -2/3`.

The certificate also returns the normalized phase
`-t_hat^3/3 + t_hat*z_hat`, exact equation replays, the target-order checks,
and a scope statement.  The solver contains no case name, expected exponent,
or normal-form dispatch.

## Evaluator and certificate

`compile_expression` returns a `CompilationReport`.  `certified` means only:

- evaluation completed in the implemented fragment;
- the analytic/truncation remainder is below the observer's visible boundary;
- no failure was suppressed.

It is a machine-checkable research certificate, not a formal proof.  Exact
rational powers and SymPy coefficients keep cancellation and the Airy balance
auditable.

## Failure semantics

The compiler refuses to guess:

- a missing variable binding returns `missing-binding`;
- unsupported exponential growth returns `unsupported-scale`;
- an invalid local `log` form returns `domain-error`;
- insufficient Taylor depth returns `unsafe` with `budget-exhausted`;
- inconsistent or underdetermined chart equations raise typed balance errors.

An underdetermined balance means that the task contract lacks an anchor; it is
not resolved by selecting an arbitrary chart.

## Baseline

The immediate baseline is a hand-provided asymptotic scaling.  The Airy test
provides no expected powers to the solver: only the source phase, the large
parameter scale, and the names whose scales are unknown.  A later integration
should also compare against SymPy/Sage/Wolfram on held-out phases and record
human hints, expression growth, runtime, residual quality, and coverage.

## Budget and cost

`CostStats` reports input nodes, evaluation retries, coefficient additions,
term-pair multiplications, Taylor terms, and peak live series terms.  These are
transparent structural counters, not wall-clock performance claims.  It also
separates backward-obligation count, retained storage, residual records, branch
cases, and decoder operations.  The last two are zero in the frozen fragment;
they are present so a later benchmark cannot hide those costs.

`compilation_summary` and `balance_summary` emit JSON-compatible, replayable
result ledgers.  `demo.py` prints those ledgers rather than a presentation-only
answer.

Run everything from this directory:

```bash
python -m unittest discover -s tests -v
python demo.py
```

## Current limits

- one asymptotic generator `N` and exact rational polynomial orders;
- local finite expansions only, not a general Hahn/transseries engine;
- no contour deformation, Airy integral evaluation, or uniform error theorem;
- phase balancing assumes every extracted monomial must remain `O(1)`;
- no automatic selection among competing subsets of active terms;
- no Process Geometry repository integration or stable API promise.

The next honest step is a held-out benchmark with competing balances and a
chart candidate ranking rule.  Only after that should the representation be
promoted into a shared compiler IR.

## FFI-ready kernel boundary

The sprint remains Python-only.  If later benchmarks justify a lower-level
kernel, the following components have deliberately pure boundaries suitable
for Rust:

- exact rational scale weights and linear balance constraints;
- an immutable expression-DAG arena with stable node identifiers;
- backward-obligation propagation over typed node edges;
- certificate replay, resource limits, and structural cost counters.

The research grammar, workload orchestration, SymPy coefficient adapter,
symbolic simplification, and rapid calibration fixtures should remain in
Python while the semantics is changing.  A Rust migration is justified only
if a frozen cross-domain benchmark shows that these pure kernel components are
a material wall-clock or memory bottleneck after compilation cost, FFI copies,
residual storage, and repeated evaluation are all charged.  Language choice is
not credited as a research result.
