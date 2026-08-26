# Phase 1G contract — selective continuation and time reversal

**Status:** frozen finite exact calibration.  This phase tests the logic of
stopping a leading branch while continuing a connected branch.  It is not a
hard-sphere discretization, a derivation of molecular chaos, a
Boltzmann--Grad theorem, or an H theorem.

**Executable owner:**
`tests/research/test_selective_continuation_time_reversal.py`.

**Result owner:**
`14-phase1g-selective-continuation-time-reversal-results.md`.

## 1. Research question

Phase 1F left a calculability test:

> Can layer-specific semantic adaptation decide which component may stop at a
> target description and which component must retain microscopic continuation,
> while exposing the exact defect of that decision under time reversal?

The test must not begin with entropy.  It must first construct:

1. a reversible microscopic evolution;
2. a lowering to a target state;
3. a declared closure section;
4. a leading branch that stops at the target layer;
5. a connected residual that continues through the microscopic evolution;
6. a cut identity and a time-reversal obstruction;
7. an autonomous target semigroup whose relation to the closed microscopic
   system is stated without semantic overclaim.

This is the finite structural shadow of the Deng--Hani--Ma policy that stops
leading $f_A$ factors and continues earlier cumulants.  The paper's
continuum estimates remain external.

## 2. Frozen carrier and reversible evolution

Let

\[
\Gamma=\{0,1\}_x\times\{0,1\}_h,
\]

where $x$ is observed and $h$ is a hidden/environment bit.  A microscopic
state is a probability law $F(x,h)$.  The exact microscopic map is

\[
U(x,h)=(x\mathbin{\mathtt{xor}}h,h).
\]

It is an involution:

\[
U^{-1}=U,\qquad U^2=I.
\]

The target observation is the $x$-marginal

\[
\pi F(x)=\sum_h F(x,h).
\]

Fix a declared environment law

\[
q_\delta=(1-\delta,\delta),\qquad 0<\delta<1/2,
\]

and the factorized section

\[
\sigma_\delta(p)=p\otimes q_\delta.
\]

The section is a semantic choice: it attaches a fresh, uncorrelated hidden
bit to a target law.  It is not an inverse to the microscopic history.

## 3. The cut and its two branches

For a microscopic law whose hidden marginal remains $q_\delta$, define the
signed connected residual

\[
E_\delta(F)=F-\sigma_\delta(\pi F).
\]

At the cut,

\[
F=\underbrace{\sigma_\delta(\pi F)}_{\text{leading/factorized}}
 +\underbrace{E_\delta(F)}_{\text{connected residual}}.
\]

Both marginals of $E_\delta(F)$ vanish.  It is therefore invisible to the
present target state, but it need not be invisible after continuation.

Define the stopped target channel

\[
B_\delta=\pi U\sigma_\delta.
\]

Linearity gives the exact selective-continuation identity

\[
\boxed{
\pi U F
=B_\delta(\pi F)+\pi U E_\delta(F).
}
\]

The first term is evaluated entirely at the target layer and stops.  The
second remains microscopic long enough to pass through $U$, then lowers.
The omission defect of the stopped branch is therefore not a verbal
``information loss'' but the exact task-relative quantity

\[
\rho_U(F)=\pi U E_\delta(F).
\]

This earns a one-cut observation identity.  It does not assert that all
future histories have been controlled.

## 4. Target A/M chart is derived after closure

For $p=(p_0,p_1)$, the stopped channel is the binary symmetric channel

\[
B_\delta(p)_0=(1-\delta)p_0+\delta p_1,
\qquad
B_\delta(p)_1=\delta p_0+(1-\delta)p_1.
\]

Its one-step increment has the componentwise A/M presentation

\[
B_\delta(p)_i-p_i=A_i(p)+p_iM_i,
\]

with

\[
A_0=\delta p_1,\quad A_1=\delta p_0,
\qquad M_0=M_1=-\delta.
\]

Thus the target A/M quantities are derived from the lowered dynamics and the
chosen section.  They are not assigned to the exact closed microscopic
future.  For a correlated $F$, the observed next increment additionally
contains $\rho_U(F)$.

## 5. Time-reversal red team

Starting with a factorized source $F_0=\sigma_\delta(p_0)$, let

\[
F_1=UF_0,\qquad p_1=\pi F_1.
\]

Microscopic reversal gives

\[
\pi U^{-1}F_1=\pi UF_1=p_0.
\]

If the cut first replaces $F_1$ by its factorized section, it gives instead

\[
\pi U^{-1}\sigma_\delta(p_1)=B_\delta(p_1).
\]

The exact noncommutation defect is

\[
\pi U^{-1}F_1-
\pi U^{-1}\sigma_\delta(\pi F_1)
=\pi U E_\delta(F_1).
\]

The square

```text
F_1 ------------------U^{-1}------------------> F_0
 |                                              |
 | pi, then sigma_delta                         | pi
 v                                              v
sigma_delta(p_1) --------U^{-1}, then pi------> p_closed
```

does not commute.  Exact microscopic reversibility is intact.  What fails is
equivariance of the selected closure section under $U$.  Hence the
stop/continue policy is intrinsically oriented: applying the stopped policy
symmetrically erases the correlation that carries the return path.

## 6. Re-sectioned process versus closed microscopic process

Repeated target evolution means

\[
p_{n+1}=B_\delta p_n
=\pi U\sigma_\delta(p_n).
\]

Each step reattaches the reference environment $q_\delta$.  It is a valid
autonomous finite semigroup on target states, but it is not the quotient of
repeatedly applying $U$ to one closed microscopic state:

\[
B_\delta^n\pi F_0
\ne
\pi U^nF_0
\quad\text{in general}.
\]

For the frozen fixture $U^2=I$, so the closed microscopic trajectory
returns every two steps.  By contrast, $B_\delta$ contracts the deviation
from the uniform law by

\[
\lambda=1-2\delta.
\]

This isolates the source of the arrow in the finite calibration: not
marginalization alone and not a failure of microscopic reversibility, but the
oriented renewal/closure operation that discards the connected residual at
each step.

There is one further precision.  For $\delta\ne1/2$, $B_\delta$ is
algebraically invertible as a linear map.  Its inverse is not a stochastic map
on the whole probability simplex: for example, $B_\delta^{-1}(1,0)$ has a
negative second component.  The earned arrow is therefore failure of a
positivity-preserving Markov-group inverse and failure of compatibility with
the closed microscopic return, not literal noninjectivity of $B_\delta$.

## 7. Frozen exact fixture and certificates

The executable freezes

\[
p_0=(3/4,1/4),\qquad \delta=1/16,
\qquad F_0=\sigma_\delta(p_0).
\]

It must certify with exact rational equality:

1. $U$ preserves probability and is an involution;
2. the cut $F_1=\sigma_\delta(p_1)+E_\delta(F_1)$ and both zero marginals;
3. stopped target A/M plus continued residual reconstructs the next
   observation;
4. re-factorization at the cut loses the exact reversed return;
5. a declared long-horizon gap separates renewed target dynamics from the
   closed microscopic orbit, while the algebraic inverse fails positivity;
6. exact finite claims, rejected equivalences, and external continuum claims
   remain separately graded.

## 8. Forbidden conclusions

This phase must not claim:

- that XOR dynamics models hard-sphere geometry;
- that $E_\delta$ is a BBGKY cumulant beyond the structural analogy;
- that one finite cut controls a Duhamel tail or recollisions;
- that the factorized section is derived from Newtonian mechanics;
- that $B_\delta$ is the exact quotient of the closed $U$-dynamics;
- that contraction alone discovers or proves an H theorem;
- that hidden-state depth or correlation order is arithmetic rank;
- that this one domain justifies a generic adapter or public API.

## 9. Gate for reopening the H question

Phase 1G may reopen only a **post-closure finite Lyapunov diagnostic** if all
six certificates pass.  The next search must keep three objects distinct:

1. the closed reversible microscopic group $U^n$;
2. the re-sectioned target semigroup $B_\delta^n$;
3. the connected continuation residual that measures their mismatch.

Any candidate $H$ belongs to item 2 unless a separately proved lifting law
relates it to items 1 and 3.  The first-principles question is then whether
the target process geometry and its invariant/reference law select a
monotone covector without importing Shannon or Boltzmann entropy into the
candidate grammar.

## 10. Repository effect

### Mathematical Core

No change.  The phase supplies pressure for an oriented closure-section
defect and a selective continuation identity, but only in one finite model.

### Engineering Architecture

Research-local refinement.  A continuation adapter may expose a stopped
target branch, a continued signed residual, a cut, and a noncommutation
certificate.  No generic interface is introduced.

### Theory Map

Unchanged.  The result may support the semantic-adaptation transversal only
after transfer to a second non-isomorphic domain; it does not promote a node,
edge, or arithmetic rank.
