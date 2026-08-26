# Phase 1G results — selective continuation and time reversal

**Status:** six exact research-local certificates passed.  The phase earns a
calculable stop/continue rule in one finite reversible model and an exact
time-reversal obstruction.  It proves no continuum kinetic or entropy
statement.

**Contract:**
`13-phase1g-selective-continuation-time-reversal-contract.md`.

**Executable:**
`tests/research/test_selective_continuation_time_reversal.py`.

## 1. Main result

The finite calibration turns layer-specific semantic adaptation into the
exact identity

\[
\pi U F
=\underbrace{B_\delta(\pi F)}_{\text{stop at target layer}}
 +\underbrace{\pi U E_\delta(F)}_{\text{continue connected residual}},
\]

where

\[
B_\delta=\pi U\sigma_\delta,
\qquad
E_\delta(F)=F-\sigma_\delta(\pi F).
\]

The connected residual is invisible to the present marginal but can change
the next marginal.  The stopping rule is therefore valid only for the
declared target branch; exact microscopic continuation requires the residual
branch as well.

This directly answers the concern that strict decoding back to the original
dynamics is too strong.  Exact decoding is not imposed.  Instead, the phase
asks for an exact task equation plus an explicit residual for the stronger
continuation task.

## 2. Exact cut values

For

\[
p_0=(3/4,1/4),\qquad \delta=1/16,
\]

the factorized microscopic source evolves to

\[
F_1=
\begin{pmatrix}
45/64 & 1/64\\
15/64 & 3/64
\end{pmatrix},
\qquad
p_1=\pi F_1=(23/32,9/32).
\]

The factorized section at the cut and its residual are

\[
\sigma_\delta(p_1)=
\begin{pmatrix}
345/512 & 23/512\\
135/512 & 9/512
\end{pmatrix},
\]

\[
E_\delta(F_1)=
\begin{pmatrix}
15/512 & -15/512\\
-15/512 & 15/512
\end{pmatrix}.
\]

Both marginals of the residual vanish and

\[
\lVert E_\delta(F_1)\rVert_1=15/128.
\]

Thus $F_1$ and $\sigma_\delta(p_1)$ have the same declared target state,
but are separated by a continuation task.

## 3. Stopped A/M branch and continued correction

The target channel at the middle marginal gives

\[
B_\delta(p_1)=(177/256,79/256).
\]

It has the derived one-step A/M chart

\[
A(p)=(\delta p_1,\delta p_0),
\qquad
M(p)=(-\delta,-\delta),
\]

so componentwise

\[
B_\delta(p)_i=p_i+A_i(p)+p_iM_i(p).
\]

Continuing the connected branch gives

\[
\pi U E_\delta(F_1)=(15/256,-15/256).
\]

The exact sum is

\[
(177/256,79/256)+(15/256,-15/256)
=(3/4,1/4)=p_0.
\]

The A/M chart therefore belongs to the stopped target dynamics selected by
the section.  The exact microscopic observation contains an additional
additive continuation residual.  This is a more precise statement than
either ``A/M rewrites the whole microscopic dynamics'' or ``coarse-graining
destroys all semantics.''

## 4. Time reversal locates the asymmetry

Because $U^{-1}=U$, the correlated middle law returns exactly:

\[
\pi U^{-1}F_1=p_0.
\]

Factorizing first gives

\[
\pi U^{-1}\sigma_\delta(p_1)
=B_\delta(p_1)
\ne p_0.
\]

The failure is exactly

\[
p_0-B_\delta(p_1)
=\pi U E_\delta(F_1)
=(15/256,-15/256).
\]

So microscopic reversibility is not contradicted.  The asymmetric step is the
choice to re-enter the microscopic layer through the factorized section
$\sigma_\delta$.  That section is not equivariant with the microscopic
evolution.  The same stop policy cannot be used forward and backward while
also claiming exact closed-system continuation.

This is the phase's principal negative result:

> A target-semantic adapter can be exact for its declared stopped process and
> still fail the stronger reverse-continuation task.  The failure is measured
> by the continued connected residual, not by a demand for global decoding.

## 5. The autonomous target is a renewed process

Repeated application of the target channel contracts the deviation from the
uniform law by

\[
\lambda=1-2\delta=7/8.
\]

After 16 steps,

\[
B_\delta^{16}p_0
=
\left(
\frac12+\frac14(7/8)^{16},
\frac12-\frac14(7/8)^{16}
\right).
\]

The closed microscopic model has $U^{16}F_0=F_0$.  Hence the exact observed
gap is

\[
\left\lVert
\pi U^{16}F_0-B_\delta^{16}p_0
\right\rVert_1
=\frac12\left(1-(7/8)^{16}\right).
\]

It is already greater than three times the one-cut residual norm $15/128$.
This is not an estimate for hard spheres.  It is an exact warning that a
small local closure residual cannot be reused indefinitely without a
stability or accumulated-tail theorem.

The autonomous target semigroup has nevertheless been earned on its own
declared process: at every step it applies $U$ after attaching a fresh
factorized environment.  Its one-sided Markov arrow comes from repeated
renewal, not from the marginal map $\pi$ alone.

The executable also prevents a stronger overstatement.  Since
$\delta\ne1/2$, $B_\delta$ has an algebraic linear inverse.  But

\[
B_\delta^{-1}(1,0)
=\left(\frac{1-\delta}{1-2\delta},
-\frac{\delta}{1-2\delta}\right)
\]

is not a probability law.  Thus the target dynamics is not a reversible
group of Markov maps on the whole simplex, even though its linear action is
injective.  Contraction should not be confused with literal loss of every
recoverable distinction.

## 6. Relation to Deng--Hani--Ma

The exact model calibrates three structural features of the partial expansion
without claiming to reproduce its analysis.

| Partial-expansion feature | Finite calibration | Missing continuum work |
| --- | --- | --- |
| stop leading $f_A$ | evaluate $B_\delta(\pi F)$ at target layer | Boltzmann comparison and its norm |
| continue cumulant | propagate $E_\delta(F)$ through $U$ before lowering | cumulant hierarchy and long-time bounds |
| cut and estimate remainder | expose $\pi U E_\delta(F)$ exactly | molecule geometry, recollisions, and tail summation |

The key shared logic is orientation.  The leading and connected pieces do not
have the same continuation duty.  In the continuum proof that distinction is
backed by partial time expansion and molecule estimates; here it is backed
only by finite exact algebra.

## 7. Executed certificates

Six exact tests pass:

1. XOR microscopic evolution preserves probability and is an involution;
2. the cut separates a factorized leading law and a signed zero-marginal
   connected residual;
3. the stopped A/M branch plus continued residual reconstructs the exact next
   observation;
4. factorizing at the cut erases the reversed return path by exactly the
   continued residual;
5. sixteen renewed target steps separate from the reversible closed orbit by
   a closed rational formula, while the algebraic inverse fails positivity;
6. one-cut exactness, target autonomy, rejected microscopic quotient, external
   continuum transfer, and untested H claims remain separately graded.

Together with Phases 1C, 1E, and 1F, the focused dependency-free run contains
29 exact certificates.

## 8. What has and has not been earned

Phase 1G has earned:

- a finite exact two-branch selective-continuation identity;
- a derived A/M chart for the stopped target channel;
- a signed residual that is invisible now but continuation-effective later;
- an exact time-reversal/noncommutation certificate;
- a distinction between a renewed autonomous target process and a quotient of
  one closed microscopic process;
- an exact long-horizon amplification red team.

It has not earned:

- a hard-sphere or BBGKY selective-continuation theorem;
- a bound on collision-history tails, recollisions, or cumulants;
- derivation of the closure section from microscopic mechanics;
- a general semantic-adapter law or public interface;
- an entropy, H theorem, or arithmetic-rank promotion.

## 9. Next gate

This gate has now been executed by Phase 1H on the finite renewed process.  Its
frozen target was a **hidden-candidate Lyapunov diagnostic** on $B_\delta$:

1. freeze an observer/covector grammar without Shannon entropy, logarithms, or
   the answer visible to the discovery path;
2. require exact monotonicity over the whole positive binary simplex and a
   strictness/equality-set certificate;
3. test whether the selected functional depends on the invariant reference
   law and how its one-step decrement pairs with the derived A/M jet;
4. keep the microscopic orbit and connected residual as red teams;
5. consult the supplied entropy identity only after candidate selection.

The exact result is recorded in
`15-phase1h-hidden-lyapunov-mode-contract.md` and
`16-phase1h-hidden-lyapunov-mode-results.md`.  Quadratic contrast is the
minimum candidate, but an exact positive modal cone rejects uniqueness.  The
classical binary relative H is a post-selection positive analytic resummation.
This addresses Track A only for the renewed target; Track B and transfer to
hard spheres remain open.

The subsequent
[Phase 1I charted-fibre result](./18-phase1i-charted-fibre-calculus-results.md)
returns to this same cut and evaluates its effect on target observables.  It
shows exactly how the continued residual can outweigh target Lyapunov
dissipation, so the Phase 1G adaptation defect and the Phase 1H target theorem
are joined by a finite response ledger rather than by a global decoder.

## 10. Repository effect

### Mathematical Core

Unchanged.  The exact noncommutation residual is evidence for, not promotion
of, a general oriented-adaptation law.

### Engineering Architecture

Research-local refinement.  The executable separates reversible source
evolution, target lowering, closure section, stopped A/M branch, continued
residual, and horizon amplification.

### Theory Map

Unchanged.  No new node, edge, rank, or public abstraction is introduced.
