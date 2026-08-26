# Phase 1H results — target modes before entropy

**Status:** nine exact research-local certificates passed.  The target
semigroup selects a simple Lyapunov mode and a larger certified cone, but does
not uniquely select the classical H functional.

**Contract:**
`15-phase1h-hidden-lyapunov-mode-contract.md`.

**Executable:**
`tests/research/test_hidden_lyapunov_mode_discovery.py`.

## 1. Main outcome

The discovery path received no logarithm, entropy formula, or supplied H
candidate.  Exact enumeration found:

\[
u=(1/2,1/2),
\qquad m=(1,1),
\qquad z=(1,-1),
\]

with

\[
m^TB_\delta=m^T,
\qquad
z^TB_\delta=\lambda z^T,
\qquad
\lambda=1-2\delta.
\]

For the frozen $\delta=1/16$, $\lambda=7/8$.  Thus the entire nonconserved
target dynamics is the scaling law

\[
z(B_\delta p)=\frac78z(p).
\]

Exchange symmetry and nonnegativity retain the even modes.  The frozen
minimum-degree selector chooses

\[
K_2(p)=(p_0-p_1)^2.
\]

It has the exact one-step decrement

\[
K_2(p)-K_2(B_\delta p)
=\left(1-\lambda^2\right)(p_0-p_1)^2\ge0,
\]

with equality exactly at the invariant law.

## 2. The decisive negative result: monotonicity is not uniqueness

Every even power is also monotone:

\[
K_{2m}(p)=(p_0-p_1)^{2m},
\]

\[
K_{2m}(p)-K_{2m}(B_\delta p)
=\left(1-\lambda^{2m}\right)(p_0-p_1)^{2m}\ge0.
\]

The executable verifies a nontrivial exact combination through degree eight,

\[
K_c(z)
=\frac35z^2+\frac7{11}z^4+\frac29z^6+\frac5{13}z^8,
\]

and its coefficientwise decrement on the whole simplex.  It also verifies
that $z^2$ and $z^4$ are not positive scalar multiples.

Therefore:

> The target dynamics supplies a Lyapunov cone, not a unique entropy.

The minimum-complexity rule selects $K_2$, but that is a choice of grammar and
cost, not a theorem that nature has selected the classical H functional.

The claim is deliberately limited: the positive even-power cone is
certified, not proved to be the complete cone of all target Lyapunov
functions.

## 3. A/M explains the step only with the correct jet depth

For $p=(3/4,1/4)$ and $\delta=1/16$, the target A/M chart gives

\[
A=(1/64,3/64),
\qquad
M=(-1/16,-1/16),
\]

and hence

\[
\Delta p=A+p\odot M=(-1/32,1/32).
\]

For $K_2=(p_0-p_1)^2$, the exact finite-step ledger is

| contribution | exact value |
| --- | ---: |
| full change $K_2(p+\Delta p)-K_2(p)$ | $-15/256$ |
| A/M first-jet pairing $dK_{2,p}(\Delta p)$ | $-1/16$ |
| quadratic/second-jet remainder | $1/256$ |

Thus

\[
-\frac{15}{256}
=-\frac1{16}+\frac1{256}.
\]

The A/M first jet supplies the tangent direction exactly, but it does not by
itself equal a finite-step Lyapunov decrement.  The second jet is part of the
task.  This is a useful correction to any proposal that two A/M quantities
automatically contain every finite-horizon functional statement.

For a continuous-time generator, the first-jet pairing would govern the
instantaneous derivative.  For the discrete renewed channel used here,
discarding the curvature term is a category error.

## 4. The target Lyapunov function does not lift to the micro orbit

Pull $K_2$ back along the observed Phase 1G microscopic fixture.  The exact
values are

\[
K_2(\pi F_0)=\frac14,
\qquad
K_2(\pi UF_0)=\frac{49}{256},
\qquad
K_2(\pi U^2F_0)=\frac14.
\]

The first step decreases and the reversed return increases.  Hence $K_2$ is a
Lyapunov function of the renewed target process, not of the exact reversible
microscopic process.

This is precisely what layer-specific semantic adaptation should predict:
the target theorem is valid at its own layer, while the stronger lifting task
has a witnessed residual and fails.

## 5. Minimum dynamical complexity does not imply entropy composition

On the binary simplex, $K_2$ is the quadratic reference distance to the
uniform law.  For

\[
p=(3/4,1/4),
\qquad q=(2/3,1/3),
\]

the executable obtains

\[
K_2(p)=1/4,
\qquad K_2(q)=1/9,
\]

while its natural four-state product extension gives

\[
K_2(p\otimes q)=7/18.
\]

In fact,

\[
K_2(p\otimes q)
=K_2(p)+K_2(q)+K_2(p)K_2(q),
\]

not an additive law.  Target monotonicity and independent-product additivity
are different tasks.  The minimum candidate for the first need not solve the
second.

This also warns against a premature conclusion: additivity alone will still
not necessarily select classical H, because a multiplicative quantity can be
sent to an additive one by a logarithmic chart.  The collision-local
covector/chain rule remains an additional constraint.

## 6. Post-selection comparison with classical H

Only after $K_2$ and the nonuniqueness result were frozen was the classical
binary relative functional opened.  With

\[
p=((1+z)/2,(1-z)/2),
\qquad u=(1/2,1/2),
\]

it is

\[
H_u(z)
=\frac12\left[(1+z)\log(1+z)+(1-z)\log(1-z)\right].
\]

Its expansion is

\[
\boxed{
H_u(z)
=\sum_{m\ge1}
\frac{z^{2m}}{(2m)(2m-1)}.
}
\]

The first four exact coefficients are

\[
\frac12,
\quad\frac1{12},
\quad\frac1{30},
\quad\frac1{56}.
\]

All are positive.  Consequently the classical binary relative H is a
positive analytic resummation of the discovered even Koopman modes.  Its
monotonicity under $B_\delta$ follows mode by mode.

Differentiating the resummation gives

\[
H_u'(z)
=z+\frac{z^3}{3}+\frac{z^5}{5}+\cdots
=\frac12\log\frac{1+z}{1-z}
=\frac12\log\frac{p_0}{p_1}.
\]

Thus the logarithmic odds covector is not present in any one finite mode.  It
appears when the full analytic tower is completed and differentiated.  This
is the precise bridge from target spectral contraction to the logarithmic
chart, but the coefficients of that completion still require an additional
selection law.

This supplies a new structural reading:

- the target semigroup explains why a broad family of deviations from the
  invariant law decreases;
- it does not determine the coefficients of the classical H resummation;
- the logarithmic covector must be selected by additional composition and
  locality structure.

Phase 1B identifies one such structure: collision pair products are formed by
Multiplication while one-site covectors add.  The resulting
Multiplication-to-Addition character is logarithmic after the ordered
continuous regularity assumptions are supplied.  Phase 1H and Phase 1B are
therefore complementary rather than competing derivations.

## 7. What the result says about the original H question

The friend's original observation was that an H function may be only one
representation of a more abstract entropy-like quantity.  The finite result
supports the first half and sharpens the second:

1. a semigroup determines a cone of monotone observables, not generally one
   scalar;
2. the state chart and process spectrum expose that cone before entropy is
   named;
3. a particular H is selected only after further requirements—reference
   measure, locality, collision composition, separability, chain rule, or
   another task—are imposed;
4. the selected target H need not be monotone on the reversible microscopic
   layer;
5. different semantic layers may therefore carry different adapted
   Lyapunov functionals without requiring a global decoder or one universal
   formula.

What has not yet been proved is that this entire pattern transfers from the
renewed binary target to the Boltzmann collision semigroup.  That remains a
continuum and collision-geometry problem.

## 8. Executed certificates

Nine exact tests pass:

1. invariant law, conserved mass, and contrast mode are discovered exactly;
2. discovery source is separated from the held-out classical control;
3. the minimum admissible polynomial mode is quadratic contrast;
4. a positive even-mode cone has an exact simplex-wide decrement;
5. target Lyapunov uniqueness and quadratic tensor additivity are rejected;
6. the finite-step change splits into A/M first jet plus second jet;
7. the target candidate fails to lift to the reversible microscopic orbit;
8. the held-out classical coefficients form a positive modal resummation;
9. all target, microscopic, composition, and continuum claims remain typed.

Together with Phases 1C, 1E, 1F, and 1G, the focused dependency-free run now
contains 38 exact certificates.

## 9. Claim boundary

Phase 1H has earned:

- an oracle-free invariant/reference and Koopman-mode discovery;
- a minimum-complexity quadratic target Lyapunov candidate;
- a certified positive cone of exact target Lyapunov polynomials;
- an exact nonuniqueness result;
- an exact A/M/second-jet ledger;
- microscopic lifting and product-additivity counterexamples;
- a post-selection modal interpretation of classical binary relative H.

It has not earned:

- uniqueness of entropy from target monotonicity;
- a complete classification of all target Lyapunov functions;
- a microscopic H theorem;
- a Boltzmann or BBGKY H theorem from first principles;
- a collision-history tail estimate or continuum closure;
- a generic entropy/process API or arithmetic-rank promotion.

## 10. Next gate

The next gate should not enumerate more polynomial modes.  It should test an
**intersection of selection laws**:

\[
\text{target Lyapunov cone}
\cap
\text{collision-product covector law}
\cap
\text{declared composition/chain rule}.
\]

The key question is whether finite polynomial modes are all rejected by the
collision-product character law, while an analytic completion/resummation
produces the logarithmic covector and relative H.  This would explain why the
logarithm is not selected by contraction alone, yet becomes forced when
Multiplication of collision activities must lower to Addition of local
covectors.

Independent-product additivity must be included as a red team rather than
treated as sufficient: quadratic distance composes multiplicatively after a
shift, so a logarithmic chart can make another additive quantity.  The
collision-local chain rule is the sharper selector.

## 11. Repository effect

### Mathematical Core

Unchanged.  The result supplies a finite selection/no-uniqueness certificate,
not a general entropy axiom.

### Engineering Architecture

Research-local refinement.  The solver stages are now target-mode discovery,
candidate selection, exact monotonicity, jet-depth analysis, lifting and
composition red teams, then held-out classical comparison.

### Theory Map

Unchanged.  The modal cone and analytic resummation remain Sonnet evidence;
no node, edge, or rank is promoted.
