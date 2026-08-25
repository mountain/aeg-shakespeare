# Pendulum equal-clock section red team

**Status:** T0 end-to-end executable calibration; no Theory Map or API
promotion.

## 1. Pre-registered failure opportunity

Notes 54 and 56 propose

\[
\text{lifted history}
\to\text{task stopping section}
\to\text{canonical clock cost}
\to\text{Bellman/Huffman optimization}.
\]

The prediction was frozen before execution: equal-clock first-hit sections on
the same pendulum history must produce the same finite policy and value under a
nonlinear observable reparameterization. Equal-coordinate sections should fail
as a negative control. Failure of the first statement rejects the interface or
the alleged ruler.

## 2. Orbit and presentations

On the positive-velocity regular half of the (E=0) libration branch,

\[
Y^2=-2U(1-U^2),\quad U\in[-0.9,-0.1],\quad\omega=\frac{dU}{Y}.
\]

Use (X=U^3), so (Z=DX=3U^2Y) and

\[
\frac{dX}{Z}=\frac{dU}{Y}.
\]

The test integrates both expressions independently and constructs five
equal-clock first-hit sections by monotone inversion.

## 3. Finite stopping task

Four ordered latent task classes have weights ((8,4,2,1)). An admissible query
resets the same orbit, evolves from the root to a selected first-hit boundary,
and observes which side contains the class. Its cost is the root-to-boundary
clock integral. A finite alphabetic Bellman recursion chooses tree and value.

Thus the experiment executes

```text
one lifted orbit -> stopping sections -> task splits
  -> integrated query ruler -> recursive optimization -> value/policy
```

## 4. Result

For equal-clock sections measured independently in (U) and (X):

```text
maximum section-clock discrepancy  < 1e-30
optimized-value discrepancy        < 1e-30
optimal policy                     identical
```

For the control, equal-(U) and equal-(X) grids select different physical
boundaries. Their clock-gap profiles and optimized task values differ by more
than (0.1). Coordinate spacing is therefore presentation baggage.

## 5. Claim boundary

This supports one missing end-to-end arrow, not the full framework. It does not
establish global turning-point transport, mesh convergence, observer/clock
discovery, a continuous-Huffman theorem, task-quotient invariance, or uniqueness
of the clock ruler.

The broader schedule should now return to the frozen Hidden A/M Noether S1
census. A later pendulum pressure would be mesh refinement across a turning
point.

## 6. Governance

```text
Epistemic maturity: T0
Role: pre-registered lift/section/optimization red team
Theory Map Change: supports one candidate arrow; no promotion
Experimental/Public API pressure: none
```
