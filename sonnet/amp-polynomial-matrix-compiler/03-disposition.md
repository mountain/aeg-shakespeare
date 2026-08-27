# Disposition: selective algorithmic simplification

Status: issue #152 result.

## 1. Verdict by layer

| Layer | Disposition | Reason |
|---|---|---|
| AMP polynomial-like basis | **EXPAND** | compresses degree-`d^N` expanded support into a fixed observer ray and exposes the correct asymptotic coordinate |
| AMP matrix-like transport | **EXPAND** | composition becomes an exact sparse nilpotent matrix and the conjugacy becomes a triangular linear solve |
| Exact certificate/replay | **EXPAND** | rational coefficients, finite eigenrelation, and first omitted residual replay independently |
| Single-query floating-point speed | **NARROW** | strong logarithmic recurrence stops early and can equal or beat compiled evaluation |
| Global numerical method | **STOP outside chart** | higher truncation can diverge near the non-asymptotic region |
| Generic interacting dynamics | **OPEN** | one power-dominant scalar family is not a general AMP solver |

The overall disposition is

\[
\boxed{\texttt{EXPAND-NARROW}}.
\]

Both proposed layers earned real algorithmic roles, but only for specified
observers and charts.

## 2. What was actually simplified

The representation changes the algorithmic structure:

\[
\text{nonlinear repeated state map}
\longrightarrow
\text{sparse linear composition operator}
\longrightarrow
\text{finite eigen-coordinate}
\longrightarrow
\text{one long-horizon observer evaluation}.
\]

The polynomial-like side supplies the task-adapted dictionary.  The
matrix-like side supplies the reusable action and solve.  Neither layer earns
the result alone:

- without the exponential ray, a generic ordinary polynomial/Taylor basis
  misses the sparse scale transport;
- without the matrix, the basis remains only a vocabulary and does not compile
  iteration into an eigenproblem.

This is the first exact example in the AMP line where the two sides form one
algorithm rather than two analogies.

## 3. What remains classical and what is programme-specific

The Böttcher conjugacy, escape-rate function, and Koopman composition operator
are classical.  No priority or replacement claim is earned.

The Process Geometry contribution under test is the selection principle:

> start from arithmetic process ranks, choose the chart in which the dominant
> rank is affine, complete the lower-rank residual along its generated support,
> and compile the resulting observer transport.

In this example that principle independently selects the classical useful
coordinate and produces an exact sparse implementation.  More examples are
needed before calling the selection principle general.

## 4. Next gate

Do not enlarge the runtime generically.  The next discriminating tasks are:

1. add a mixed logarithmic degree `q^k y^n` so that genuine P/A bracket terms,
   not only the `n=0` ray, are required;
2. test a two-variable coupled map where the anchor kernel and cross-variable
   support become task-visible;
3. compare automatic AMP dictionary generation against a generic monomial
   Carleman dictionary under the same residual and storage budget;
4. require a chart-switch certificate when the asymptotic expansion fails.

Only transfer to a coupled or mixed-log workload would justify extracting a
reusable engineering abstraction.

```text
Mathematical Core: unchanged
Research Programme: one T1 positive AMP algorithm calibration
Engineering Architecture: Sonnet-local sparse compiler; no extraction yet
Theory Map: no promoted node
Experimental/Public API: none
```
