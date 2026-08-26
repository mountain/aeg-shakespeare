# Phase 1H contract — hidden target-layer Lyapunov modes

**Status:** frozen research-local discovery contract.  The target process was
earned in Phase 1G; the classical entropy expression remains hidden until the
candidate ranking and nonuniqueness test are complete.

**Executable owner:**
`tests/research/test_hidden_lyapunov_mode_discovery.py`.

**Result owner:**
`16-phase1h-hidden-lyapunov-mode-results.md`.

## 1. Question and dependency boundary

Phase 1G constructed the renewed target channel

\[
B_\delta=
\begin{pmatrix}
1-\delta&\delta\\
\delta&1-\delta
\end{pmatrix},
\qquad 0<\delta<1/2,
\]

while proving that it is not the quotient of repeated evolution on the closed
reversible microscopic fixture.  Phase 1H asks:

> Once a target semigroup has been earned, what monotone state functions can
> be discovered from its process structure alone, and does that structure
> uniquely select the classical H functional?

This is Track A on one finite renewed target.  It does not reopen Track B, the
microscopic-to-kinetic passage, and does not transfer a finite result to
hard spheres.

## 2. Oracle firewall

The discovery path may use only:

- the exact rational transition matrix $B_\delta$;
- preservation of total probability;
- a stationary reference law discovered from the matrix;
- exchange symmetry $p_0\leftrightarrow p_1$;
- exact left eigen-observers of the target evolution;
- monomials of a discovered nonconserved observer up to degree eight;
- nonnegativity, target monotonicity, and syntactic degree/support cost.

The discovery path may not use:

- a logarithm or exponential;
- Shannon entropy, relative entropy, $f\log f$, or a named H formula;
- the Phase 1A supplied functional;
- the Phase 1B continuous-character oracle;
- Maxwellian, partition-function, or detailed-balance formulas;
- floating-point fitting or a numerical entropy target;
- tensor-product additivity as a tie-breaker.

Source inspection must verify that discovery functions do not call the
held-out classical control.

## 3. First-principles observable modes

Treat laws as column vectors and observables as left covectors.  Discovery
enumerates primitive integer covectors in a frozen finite box and tests

\[
c^TB_\delta=\mu c^T
\]

by exact rational equality.  It separately enumerates small nonnegative
stationary vectors and normalizes them to probability one.

For the frozen symmetric channel, the expected result is not supplied to the
search.  If found, it should contain:

\[
u=(1/2,1/2),
\]

the conserved mass observer $m=(1,1)$, and one centered nonconserved observer

\[
z=(1,-1),
\qquad z(u)=0.
\]

Write the value of the latter on a law as

\[
z(p)=p_0-p_1.
\]

If its eigenvalue is $\lambda$, the Koopman action on its powers is

\[
z(B_\delta p)^k=\lambda^kz(p)^k.
\]

No geometric or entropy interpretation is assumed before this calculation.

## 4. Frozen candidate grammar and selector

Generate the degree-bounded grammar

\[
z,z^2,\ldots,z^8.
\]

Each mode records:

- polynomial degree;
- Koopman eigenvalue $\lambda^k$;
- parity under state exchange;
- whether it is nonnegative on the whole binary simplex.

An admissible state functional must:

1. vanish at the discovered reference law;
2. be invariant under state exchange;
3. be nonnegative on the simplex;
4. not increase under one target step.

The frozen selector chooses the lowest degree and then the smallest support.
It does not compare candidates with a classical target.

## 5. Simplex-wide certificate

For $0<\lambda<1$, every even mode satisfies

\[
z^{2m}-(\lambda z)^{2m}
=(1-\lambda^{2m})z^{2m}\ge0.
\]

More generally, for exact coefficients $c_m\ge0$,

\[
K_c(z)=\sum_{m=1}^Mc_mz^{2m}
\]

has the exact decrement

\[
K_c(z)-K_c(\lambda z)
=\sum_{m=1}^M
c_m(1-\lambda^{2m})z^{2m}\ge0.
\]

This coefficientwise cone is a certified Lyapunov cone.  Phase 1H does not
claim that it exhausts every monotone function on the simplex.

If at least two nonproportional members pass, uniqueness of a target
Lyapunov function is rejected even though the minimum-complexity selector may
still return one representative.

## 6. A/M and jet-depth test

Phase 1G derived the one-step target A/M quantities

\[
A(p)=(\delta p_1,\delta p_0),
\qquad
M(p)=(-\delta,-\delta),
\]

so

\[
\Delta p=A(p)+p\odot M(p).
\]

For a candidate $K$, test whether the finite-step change equals the first-jet
pairing $dK_p(\Delta p)$.  For a quadratic candidate, Taylor's identity gives

\[
K(p+\Delta p)-K(p)
=dK_p(\Delta p)+R_2(p,\Delta p).
\]

The executable must retain $R_2$ rather than silently identifying a finite
step with an infinitesimal derivative.  This tests whether an A/M first jet is
sufficient for the declared monotonicity task or whether a higher jet is
required.

## 7. Two red teams beyond target monotonicity

### 7.1 Closed microscopic orbit

Pull the selected target function back along the Phase 1G observed microscopic
orbit.  Since $U^2=I$, any strict decrease on the first observed step must be
followed by an increase on the return step.  A target Lyapunov certificate may
not be promoted to a microscopic Lyapunov theorem.

### 7.2 Independent-product composition

Extend the minimum candidate to a product law relative to the product
reference using its natural quadratic reference distance.  For two
independent laws, test whether

\[
K(p\otimes q)=K(p)+K(q).
\]

Failure is not failure of target monotonicity.  It shows that the minimum
dynamical candidate does not automatically satisfy the composition law often
expected of an entropy-like quantity.

## 8. Held-out classical control

Only after the following are frozen may the classical binary reference
functional be opened:

1. discovered reference and linear modes;
2. selected minimum polynomial candidate;
3. exact positive modal cone;
4. nonuniqueness result;
5. A/M jet-depth result;
6. microscopic and product-composition red teams.

With $p=((1+z)/2,(1-z)/2)$ and reference $u=(1/2,1/2)$, the held-out control
may then use

\[
H_u(z)
=\frac12\left[(1+z)\log(1+z)+(1-z)\log(1-z)\right].
\]

Its even Taylor coefficients are compared with the discovered mode family:

\[
H_u(z)
=\sum_{m\ge1}
\frac{z^{2m}}{(2m)(2m-1)}.
\]

The derivative control is

\[
H_u'(z)
=\sum_{m\ge1}\frac{z^{2m-1}}{2m-1}
=\frac12\log\frac{1+z}{1-z}.
\]

Since $(1+z)/(1-z)=p_0/p_1$, this is the point where an analytic completion
of target modes may be compared with the Phase 1B logarithmic collision
covector.  The comparison remains outside discovery.

This is a post-selection interpretation, not an input to candidate discovery.

## 9. Frozen fixture and certificates

Freeze

\[
\delta=1/16,
\qquad \lambda=1-2\delta=7/8,
\qquad p=(3/4,1/4).
\]

The executable must certify:

1. exact discovery of the invariant law, conserved mass, and contrast mode;
2. source-level separation between discovery and classical control;
3. minimum selection of the quadratic contrast mode;
4. simplex-wide monotonicity of a nontrivial positive even-mode combination;
5. nonuniqueness and failure of quadratic tensor additivity;
6. exact A/M first-jet plus second-jet finite-step ledger;
7. failure of the target candidate to lift to the reversible micro orbit;
8. positive held-out classical coefficients after selection;
9. separate typing of all earned, rejected, and external claims.

## 10. Claim boundary and next decision

Phase 1H may earn a target-local Lyapunov family and a minimum candidate.  It
may not claim uniqueness merely from monotonicity.  It may not rename every
member entropy, lift it to the microscopic system, or transfer it to the
Boltzmann equation.

If the classical H control is a positive resummation of discovered modes but
is not uniquely selected, the next gate must test which additional
composition law selects its coefficients.  Candidate laws include the
collision-product character constraint already isolated by Phase 1B and
independent-product/chain rules.  These must be compared rather than assumed
equivalent.

This was the frozen prospective gate at the start of Phase 1H.  The later
[Phase 1I contract](./17-phase1i-charted-fibre-calculus-contract.md) retains
the selection question but inserts two prior obligations: the observable
change must first be split into exact target and fibre responses, and the
candidate cost must be audited across the dynamical contrast chart and the
compositional odds chart.

## 11. Cost and repository effect

- exact standard-library rational arithmetic only;
- one research-local test module;
- deterministic bounded enumeration;
- sub-second target;
- no Core, Theory Map, Experimental API, or Public API change.

### Mathematical Core

Unchanged.  This phase tests whether a target process selects a Lyapunov
covector; it does not add a general entropy object.

### Engineering Architecture

Research-local refinement.  Candidate generation, selection, monotonicity,
jet depth, lifting, product composition, and held-out evaluation remain
separate stages.

### Theory Map

Unchanged.  No rank or cross-domain law is promoted.
