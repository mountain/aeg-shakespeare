# Phase 1D synthesis — measured semantic fibres and objectification

**Status:** T0/T1 structural synthesis after the exact finite Phase 1C
calibration.  This note records a refined contract and red teams.  It proves no
continuum Boltzmann--Grad theorem, no equivalence of ensembles, no generic
objectification theorem, and no arithmetic universality theorem.

**Evidence owner:**
`07-phase1c-chart-first-adaptation-results.md` and
`tests/research/test_chart_first_collision_adapters.py`.

## 1. Outcome

The current mother picture is no longer a choice between strict equality and
unstructured approximation.  It is a typed ladder:

```text
literal equality
    -> exact continuation equivalence for a declared task
    -> task-relative semantic adaptation between different layers
    -> measured/filtered fibre interface when probability or scale is primitive
    -> objectification only after stable interaction, new composition, and lowering
```

Phase 1C certifies the third line in one exact finite fixture.  The present
phase explains how probability, thermodynamic ensembles, and asymptotic
correlation data can enter without being confused with equality or with a new
arithmetic rank.

The central refinement is:

> A macro-object need not be a bare point.  It may be a fibre together with a
> conditional law, admissible couplings, response data, and a residual.  But a
> rich fibre interface is still only horizontal semantic completion until it
> supports a new free composition and compositional lowering.

## 2. Three fibre constructions that must remain distinct

### 2.1 Exact task quotient

For one history layer and one exact task \(Q\),

\[
h\sim_Q h'
\quad\Longleftrightarrow\quad
Q(hk)=Q(h'k)
\]

for every continuation in the declared common interface.  The quotient map

\[
\pi_Q:\mathcal H\longrightarrow \mathcal H/{\sim_Q}
\]

has fibres that are exact continuation-equivalence classes.  Equality in the
quotient is exact, even though literal histories have been forgotten.

### 2.2 Cross-layer adapter fibre

For different semantic layers, Phase 1C uses

\[
\mathfrak A_{\ell\to m}
=
(a,\kappa,\eta,\mathcal Q,T,\varepsilon).
\]

Here \(\eta\) is the Phase 1C result translator, renamed from that note's
\(\rho\) so that \(\rho\) can denote the transverse ensemble law below.
The source fibre \(a^{-1}(y)\) contains states, germs, or jets represented by
one target datum.  It need not be a continuation-equivalence class.  Two
members may agree for the present task and separate at the next derivative,
at a longer horizon, or in a stronger topology.  In approximate settings the
adapter may not induce a transitive relation at all.

The Phase 1C fixture is exactly of this kind:

\[
L:\mathcal P(\{0,1,2\}^2)
\longrightarrow
\mathcal P(\{0,1,2\}),
\qquad
P^{(2)}\longmapsto f^{(1)}.
\]

The diagonal and off-diagonal two-body laws occupy one fibre of \(L\), but
their next one-body derivatives differ.  Refining the target to

\[
J_\chi(P^{(2)})=(f^{(1)},A^{(1)},M^{(1)})
\]

splits the witnessed ambiguity enough to evaluate one next derivative.  It
does not collapse the fibre to a point and does not reconstruct the complete
two-body future.

### 2.3 Measured task fibration

For a macro-observable \(J:\Gamma\to B\), write \(F_b=J^{-1}(b)\).  In a
finite setting, or a standard Borel setting with a declared disintegration,
a probability law may be expressed as

\[
\mathbb P(A)
=
\int_B \nu_b(A)\,\rho(db),
\qquad
\rho=J_*\mathbb P,
\qquad
\nu_b(F_b)=1
\quad \rho\text{-a.e.}
\]

The data have different meanings:

| datum | role |
| --- | --- |
| \(\Gamma\) | microscopic or source carrier |
| \(B\) | macro/task base |
| \(F_b\) | source distinctions hidden over \(b\) |
| \(\lambda\) | declared reference measure |
| \(\mathbb P\) | normalized source law |
| \(\rho\) | transverse law across macrostates |
| \(\nu_b\) | conditional law within one fibre |

This note uses *fibration* as typed fibre language.  It does not assert that
\(J\) is a topological Hurewicz or Serre fibration.  Outside the finite or
suitable measurable setting, the existence and uniqueness of \(\nu_b\) are
additional hypotheses.

The adapter fibre in Section 2.2 and the conditional-probability fibre here
can coexist, but they are not identical.  In particular, putting a probability
law on the space of two-body laws in the Phase 1C example would create a
second-order ensemble not used by its finite certificate.

## 3. Probability is more than a weight attached to a quotient

A probabilistic layer must distinguish:

1. a reference measure \(\lambda\);
2. a dimensionless density \(d\mathbb P/d\lambda\), where it exists;
3. an unnormalized positive weight and its partition normalizer;
4. the pushed-forward base law \(J_*\mathbb P\);
5. conditional fibre laws \(\nu_b\);
6. any stochastic kernel used for reconstruction or closure.

These data transform differently.  Changing the reference measure changes a
density even when \(\mathbb P\) is unchanged.  Changing transverse weights can
change \(J_*\mathbb P\) while preserving the conditional laws.  Changing the
macro-observable changes the fibres themselves.  A logarithm must act on a
dimensionless ratio relative to the declared reference.

The finite thermodynamic pushforward in
`docs/63-thermodynamic-objectification-and-partition-towers.md` is the exact
finite base case.  Any finite map pushes mass forward.  That fact alone does
not make the target a semantic quotient, a dynamic closure, or an objectified
primitive.

## 4. Ensembles as choices of fibre geometry and transverse law

Let \(E:\Gamma\to\mathbb R\) be energy and let
\(\Omega=E_*\lambda\) be the density-of-states measure induced by the declared
reference measure.

### 4.1 Microcanonical

A microcanonical model selects an energy fibre \(F_E\), or a declared shell
when the exact level set is singular or has zero ambient measure.  Its law is
the conditional law \(\nu_E\), not a bare equation \(E(x)=E\).

### 4.2 Canonical

A canonical law keeps the energy map and mixes its fibres with

\[
\rho_\beta(dE)
=
Z_\beta^{-1}e^{-\beta E}\,\Omega(dE),
\]

so that

\[
\mathbb P_\beta(A)
=
\int \nu_E(A)\,\rho_\beta(dE).
\]

In the cleanest finite model, the conditional law within a fixed energy fibre
is inherited from \(\lambda\), while \(\beta\) changes the transverse weights.
More general canonical constructions must state when that statement remains
true.

### 4.3 Grand canonical

A grand-canonical model can enlarge the total space to

\[
\Gamma_{\mathrm{gc}}=\bigsqcup_{N\ge0}\Gamma_N
\]

and use base coordinates \((N,E)\) with weight

\[
e^{-\beta(E-\mu_{\mathrm{chem}}N)}
\]

relative to a declared counting/reference measure.  This is not merely a new
weight on the original fixed-\(N\) fibration; the total space and base have
changed.

### 4.4 Ensemble equivalence is an adapter claim

Two ensembles are equivalent only after declaring:

- the observable/task family being compared;
- the thermodynamic or scaling limit;
- the topology, divergence, or rate function;
- uniformity in parameters and the continuation horizon;
- concentration, concavity, locality, or other hypotheses;
- phase coexistence, long-range interaction, and noncommuting-limit red teams.

Thus ensemble equivalence is naturally an asymptotic semantic adapter, not
literal equality of probability measures and not automatic identity of fibre
geometries.

## 5. Observation, ensemble, and closure are separate arrows

The kinetic seam contains at least four maps:

\[
P^{(2)}\xrightarrow{L}f^{(1)},
\qquad
P^{(2)}\xrightarrow{J_\chi}(f^{(1)},A^{(1)},M^{(1)}),
\]

\[
f^{(1)}\xrightarrow{\sigma}P^{(2)},
\qquad
\mathbb P\longmapsto L_*\mathbb P.
\]

They mean respectively observation, process-jet adaptation, a deterministic
closure section, and probability pushforward.  A closure could instead be a
kernel \(K_f(dP^{(2)})\) on the fibre over \(f\).  An ensemble supplies a law;
it does not by itself prove that either \(\sigma\) or \(K_f\) makes the target
dynamics autonomous.

Molecular chaos belongs at this closure/limit seam.  Formally writing

\[
f^{(2)}=f\otimes f+g^{(2)}
\]

places the connected correlation \(g^{(2)}\) in a candidate residual fibre.
But \(g^{(2)}\) is generally signed rather than a probability law, hard-core
exclusion changes the reference carrier, and the relevant incoming trace may
not be determined by a bulk marginal.  No generic identification of
correlation, conditional measure, A/M component, or information has been
earned.

## 6. Higher fibres can contain asymptotic adaptation

Let \(x_\epsilon,y_\epsilon\) be scale-indexed source families.  For a frozen
task family and continuation horizon, define provisionally

\[
x_\epsilon\sim_k y_\epsilon
\quad\Longleftrightarrow\quad
d_q\bigl(q(x_\epsilon c),q(y_\epsilon c)\bigr)
=o(\epsilon^k)
\]

for every declared \(q,c\).  If continuation stability and transitivity are
proved, this produces exact quotient projections

\[
\cdots\to X/{\sim_{k+1}}\to X/{\sim_k}.
\]

The apparently approximate lower-order object is then an exact projection of
a richer filtered object.  Higher cumulants, recollision histories, boundary
traces, or error coefficients may inhabit successive fibres.  This realizes
the intuition that gradual approximation can be contained by a higher fibre
without pretending that the lower layer was strictly equal to the source.

Three cautions remain:

1. continuation depth \(k\), BBGKY observer order \(s\), and arithmetic rank
   \(r\) are independent indices;
2. ordinary power jets miss exponentially small effects such as
   \(e^{-1/\epsilon}\), so the asymptotic scale is part of the contract;
3. singular limits may require boundary layers, stratified fibres,
   large-deviation rates, or full history carriers rather than a finite jet.

The Deng--Hani--Ma collision-history/cumulant construction remains a decisive
red team against assuming that one finite jet controls a long kinetic horizon.

## 7. Refined objectification statement

The earlier shorthand

```text
semantic class -> objectified point -> higher-rank composition
```

is too narrow if it suggests that all lower-rank internal structure must be
erased.  The conservative replacement is

```text
task-relative fibre or adapter
    -> stable interaction/response interface
    -> objectified primitive
    -> new free composition
    -> compositional lowering plus residual
```

A candidate thermodynamic primitive may therefore carry

\[
\mathcal O_b
=
(b,F_b,\nu_b,\mathcal K_b,R_b,\mathcal R_b),
\]

where \(\mathcal K_b\) declares admissible couplings, \(R_b\) declares response
under those couplings, and \(\mathcal R_b\) retains task-visible residuals.
This tuple is a research grammar, not a canonical mother object.

The objectification gate requires all of the following:

1. continuation-stable semantics for the declared interface;
2. a reusable identity/type, not one ad hoc macrostate;
3. a new free composition law on those objects;
4. lowering defined on every legal composite;
5. relation soundness and explicit information loss;
6. cost for compilation, fibre data, residuals, and decoding;
7. a negative control where a rich measured fibre fails to objectify.

Measured coarse-graining, entropy increase, nonzero correlation, or a
nontrivial fibre does not pass this gate by itself.

## 8. Arithmetic-tower universality remains a sharpened conjecture

The strong conjecture suggested by these fibres is that arithmetic-generated
geometries may provide a universal and effectively calculable presentation
language in which other structures occur as typed subobjects, quotients,
fibrations, completions, or gluings.

For this to be mathematically nontrivial, a future statement must specify:

- an independently defined target class of process geometries;
- the arithmetic-generated source category or tower;
- the comparison functor and the universal property it satisfies;
- which tasks, continuations, measures, residuals, and compositions are
  preserved or reflected;
- compilation, differentiation/integration, decoding, certification, and
  complexity bounds;
- a reconstruction boundary and counterexamples.

Arbitrary Gödel coding is the first kill condition.  If all target structure
is hidden in relations, residual fields, or the decoder, the arithmetic
carrier has not explained or simplified anything.  Likewise, the existence of
a formal embedding without an effective calculus does not establish the
computational part of the conjecture.

Nothing in Phase 1C proves this conjecture.  The measured-fibration language
only makes one possible statement of it sharper and more falsifiable.

## 9. Claim ledger

| statement | maturity |
| --- | --- |
| Phase 1C marginal/first-jet adequacy ladder | exact finite executed result |
| finite probability disintegration | exact finite classical fact |
| standard-Borel disintegration under its hypotheses | classical anchor |
| microcanonical/canonical/grand-canonical fibre ledger | classical reorganization with explicit measure conventions |
| measured task fibration as a common Process Geometry carrier | T0/T1 candidate |
| filtered asymptotic quotient tower | T0 candidate requiring task-specific proofs |
| fibre interface as possible objectified primitive | refinement pressure on V2 |
| equivalence of ensembles in general | unclaimed; theorem-specific only |
| arithmetic-tower universality and universal calculus | open conjecture |

## 10. Repository effect

### Mathematical Core

Refined.  Exact task equivalence remains the anchor.  The core now records
task-relative adapters, measured task fibres, ensemble data, filtered
asymptotic quotients, and the stronger objectification gate.  No generic
mother object is selected.

### Engineering Architecture

Refined.  Cross-layer calculations must declare task, translated
continuations, horizon, topology/error, residual, decoder, closure, reference
measure, base pushforward, conditional fibre laws, and ensemble parameters.
No package interface follows.

### Theory Map

Refined without adding an axis.  Semantic adaptation and measured fibres enter
the emerging transversal and sharpen the V2 boundary.  Arithmetic Geometric
Universality remains an open conjecture with an explicit anti-encoding and
effective-calculus test.

## 11. Next gate

Return to the continuum adapter contract with this ledger frozen:

1. define the hard-sphere admissible carrier and reference measure;
2. write the \(s+1\to s\) collision-boundary observation and its fibres;
3. separate bulk marginal, incoming trace, cumulant residual, and A/M jet;
4. state the source and target task families, horizon, topology, and error;
5. locate the propagated ensemble, factorized section or kernel, and closure;
6. test whether the retained collision-history carrier behaves like a filtered
   fibre rather than presupposing a finite jet;
7. only after autonomous target dynamics is certified, reopen H/Lyapunov
   discovery.
