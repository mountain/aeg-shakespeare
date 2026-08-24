# Phase 1a — exact visible-symmetry census

**Status:** S1a depth-0/1 complete; observer grammar remains sealed; no S2
candidate survives at this depth.

## 1. Purpose

Before searching for a hidden symmetry, enumerate every visible symmetry in the
first frozen grammar slice. This prevents S2 from relabelling an ordinary
presentation symmetry as an observer discovery.

The run evaluates all 80 literal depth-0/1 expressions against all 40
projectivized nonzero generators. Literal expressions are first mapped to exact
SymPy semantics and quotiented by exact expanded equality. For every semantic
expression (F) and generator coefficients (c), the certificate is

\[
R(F,c)=\sum_i \frac{\partial F}{\partial q_i}X_c(q_i).
\]

The derivative is only the exact representation backend for the already
declared A/M generator action; no classical Noether charge, cyclic-coordinate
label, observer word, or hidden transformation enters the census.

## 2. Generator action

For (c=(a_x,m_x,a_y,m_y)), the declared product A/M shadow is

\[
X_c(x)=a_x+m_xx,\quad X_c(v_x)=m_xv_x,
\]

\[
X_c(y)=a_y+m_yy,\quad X_c(v_y)=m_yv_y.
\]

A visible witness is retained only when the expanded residual is exactly zero.
An expression is S1-asymmetric only after all 40 residuals are nonzero.

## 3. Certificate boundary

This census is complete only for the depth-0/1 slice. It records:

- raw literal count;
- exact semantic quotient count;
- tested semantic-expression/generator pairs;
- every zero-residual witness;
- every expression with no visible witness.

The executed snapshot is:

```text
raw literal expressions       80
semantic quotient             57
projective generators         40
exact tested pairs          2280
zero-residual witnesses      711
S1-asymmetric expressions      0
```

Thus S1a yields a complete negative certificate for the existence of a legal
S2 input at depth one: every semantic expression has at least one visible
stabilizer. This is structurally plausible because a depth-one binary
expression uses at most two atoms while the declared generator space has four
directions. It was not inserted as an assumption and is now an executable
result.

Depth two is the required Phase 1b gate. Observer histories remain forbidden
until that census is frozen or an explicit cost/soundness argument narrows it.

## 4. Failure opportunity

The absence of asymmetric expressions blocks S2 at this depth but does not
invalidate the census: exact semantic quotienting and exhaustive residuals
turn it into a negative certificate. A framework failure would instead be a
sample-dependent equality, incomplete pair count, oracle leakage, or inability
to distinguish an explicit perturbation.
