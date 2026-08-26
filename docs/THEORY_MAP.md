# Process Geometry — living theory map

**Status:** evolving research map. This document is a navigation and review aid, **not** a frozen mathematical specification and **not** a public API contract.

**Required prior reading:** [`MATHEMATICAL_CORE.md`](MATHEMATICAL_CORE.md), then
[`ENGINEERING_ARCHITECTURE.md`](ENGINEERING_ARCHITECTURE.md). The first carries
the current objects, constructions, equations, information contracts, and
failure boundaries; the second carries the technical decisions that make
declared problems feasibly computable. This file locates and grades that work;
it must not be read as a substitute for either.

## 0. Why this document exists

Process Geometry is developing through mathematics, executable calibrations, Sonnets, and software at the same time. That creates a specific engineering risk: a useful local implementation can acquire a generic name and API shape before the underlying theory has settled, and compatibility pressure can then freeze an accidental ontology.

This document exists to prevent that failure mode.

It records the **current larger theoretical picture** against which implementation and API changes should be interpreted. It is intentionally revisable. A later experiment may split a node, merge two concepts, reject a proposed layer, or show that the current arrows are wrong.

The governing distinction is:

```text
Research Program  conjectural Arithmetic Generativity synthesis and kill conditions
Mathematical Core objects, constructions, laws, and boundaries
Research Status   dated evidence owners, results, and explicit nonclaims
Engineering Arch. representations, algorithms, evidence, errors, and cost
Theory Map        compact dependency and maturity map
Public API        durable semantic commitments already earned
Experimental      executable candidates testing parts of the map
Sonnets           problem-driven sources of pressure and counterexamples
```

An API should be reviewed **against** the Theory Map, but the API must never be treated as evidence that an unsettled part of the Theory Map has thereby become true.

The current foundation and its conjectural research direction are developed
primarily in:

- `RESEARCH_PROGRAM.md` — Arithmetic Generativity and Universality as a
  conjectural synthesis, decomposed into U1--U5 and cross-cutting E obligations;
  it is not a stable Theory Map node or promotion record;
- `MATHEMATICAL_CORE.md` — current mathematical synthesis and the required
  object/construction/law/boundary reading of this map;
- `ENGINEERING_ARCHITECTURE.md` — problem-to-solver architecture and current
  technical decisions for feasible computation;
- `42-process-geometry-from-distinguishability.md`
- `43-myhill-nerode-and-the-topological-threshold.md`
- `44-objectification-semantic-compression-and-rank-lowering.md`
- `45-lineage-objectification-and-analytic-closure.md`
- `48-foundation-naming-audit.md`
- `49-theory-implementation-structural-alignment.md`
- `50-aeg-translation-objectification-rank-lowering.md`
- `51-aeg-addition-multiplication-rank-transition.md`
- `52-canonical-completion-hypothesis.md` through
  `63-thermodynamic-objectification-and-partition-towers.md` — subsequent
  T0/T1 refinement and obstruction records;
- `64-first-principles-and-api-boundary-audit.md` — current synthesis and
  conservative implementation-boundary review.
- `65-effective-analysis-principle.md` — cross-cutting research and engineering
  requirement that analysis-bearing presentations remain symbolically and/or
  numerically effective, certifiable, and cost-auditable.

Those notes contain the argument and structural audits. This file is the
compact map used for theory location and engineering review.  A map change that
cannot be expanded into the Mathematical Core contract is vocabulary, not yet
mathematical understanding.

---

## 1. Current mother picture

The theory currently has two complementary axes.

```text
                                VERTICAL
                  ontology growth / process rank

Sigma_r
   |
   v
free process histories H_r
   |
   v
semantic compression under declared semantics
   |
   v
stable semantic classes C_r
   |
   v
objectification
   |
   v
Sigma_(r+1)  -----> free higher-rank composition
   ^                         |
   |                         |
   +---- compositional ------+
         rank lowering


HORIZONTAL at each rank

process/history
   |
   v
observer/task distinguishability
   |
   +-------------------------------+
   |                               |
   v                               v
exact continuation-stable          finite-resolution / local
semantic equivalence               distinguishability
   |                               |
   v                               v
task/process quotient              topology / locality
   |                               |
   v                               +--> continuity / boundary / covering
minimal or task-sufficient         +--> entropy / intrinsic complexity
presentation                       +--> metric/uniform structure when justified
                                   +--> differential/connection structure when justified
```

The map is deliberately not a single mandatory pipeline. A finite discrete process may stop at an exact quotient. A symbolic dynamical system may naturally reach entropy. A continuous process may support differential structure. A higher-rank language is not legitimate merely because a new symbol was introduced: its legal compositions must remain grounded by rank-lowering semantics.

The second arithmetic calibration adds an important caution to the schematic `C_r -> objectification` arrow: the thing objectified at the next rank may be a stable **process/action on lower-rank semantic objects**, not only one point or equivalence class of `C_r`. That refinement is currently evidence from AEG, not yet a generic replacement for the mother picture.

### 1.1 Emerging transversal — task-covariant history evaluation

Notes `54–63`, the pendulum P12/P13 calibrations, and the finite local-field
projective phases force a related structure that is not naturally another
stage of either axis:

```text
lifted history
    -> composable transported payload / residual in a unit frame
    -> stopping section or task evaluation
    -> task quotient / fundamental domain / retained decoder data
    -> coding, variational, or analytic structure when justified
```

Examples of payload include additive clock/action, vector-valued resources,
deck or connection holonomy, max-like peak memory, phase, and composable
projective matrix evaluation. A task may discard the payload, evaluate it in a
base frame, observe only a quotient of that evaluation, or turn a declared
frontier into an ordered resource for Bellman/Huffman optimization.
Objectification changes the local primitive ruler and must charge compilation,
dictionary, decoder, and storage effects rather than silently declaring a long
history to be one free step.

This structure cuts across the current map:

- at H1 it decides whether equal visible endpoints remain continuation
  distinguishable;
- at H3 it supplies frontier weights, coding measures, and memory lower bounds;
- at H4 it supplies clock forms, connections, and variational payloads;
- at V2/V3 it records the measure and residual data retained by an objectified
  assembly;
- at V5 it becomes part of the comparison data that lowering must transport.

The Boltzmann--BBGKY finite calibration adds a typed cross-layer refinement.
Exact continuation equivalence remains the H1 anchor, but different semantic
layers may instead be connected by a task-relative adapter carrying a state or
jet map, continuation and result translators, task family, horizon, topology,
and error budget.  When probability is primitive, its target may be a measured
task fibration: the macro base, conditional laws within fibres, transverse
ensemble law, and retained residual are separate data.  This is T0/T1 pressure
on the transversal, not a third stable axis and not a generic adapter API.

The exact finite Bellman/frontier identity, covariant pendulum family identity,
task-visible holonomy bound, same-scale mass-pushforward theorem, twisted
finite-cycle identity, pendulum lift--unit--domain--quotient--decoder chain,
and local-field history--matrix--lattice--cylinder--code separation provide
strong pressure. The pendulum proves locally that the period lattice cuts a
task-relative fundamental domain while the unit frame measures it; it also
separates continuous action coarea from finite deck memory. The projective
calibration independently separates an observer/evaluation tree from literal
history and from a probability-dependent coding tree, and adds the exact
discrete shell identity

\[
|B_d|-|B_{d-1}|=|S_d|.
\]

The same projective line now continues through one exact finite selector-policy
control task: a contact-lift grammar, matrix/lattice payload, complete-quotient
and visited-state residuals, depth-four stopping cylinder, shared decoder, and
Pareto Bellman witnesses.  Changed sources and scalar rulers select different
economies, so the geometry does not select an intrinsic controller.  Its
action syntax subsequently quotients exactly to a Ruban-reference bit, but
equal contact, evaluated next geometry, and local-cost signatures still admit
disjoint optimal-bit sets.  This obstruction transfers to deeper stopping
surfaces, new primes, and held-out inputs: a lossless action alphabet is not a
lossless policy-state quotient.  The shell identity is not identified with
physical coarea or entropy, and neither Bellman result is a preferred
\(p\)-adic section. The candidate generic carrier is still unsettled: resource
bundle, groupoid, cocycle family, enriched history category, and problem-local
alternatives remain live. Consequently this is recorded as an **emerging
T0/T1 transversal**, not a stable Theory Map node and not a generic API
proposal.

The disjoint policy collisions also expose a nontrivial task-relative
continuation-value fibre over the local evaluated signature.  Its finite
residual-bit lower bound is real.  Phase 8 now computes the coarsest stable
finite extension over that signature: 6,044 S2 classes refine to 8,126 scalar
policy/value classes or 8,128 full-decoder classes, with irregular fibres of
size one through seventy.  Lift-bit transport descends but is partial,
terminal, and many-to-one.  This closes one horizontal finite task-state
question while answering the vertical interpretation negatively for this
calibration: stable transport alone does not supply a uniform objectified
dimension or a new process rank.

Phase 9 supplies a problem-local candidate for the previously unsettled source
side of this transversal. A finite marked rational A/M-plus-Weyl history
carrier maps compatibly to real hyperbolic/Farey and p-adic lattice-tree
shadows, while depth-six/depth-eight stopping and scalar/full decoding form
commuting task-refinement triangles. Precision terminals, cross-place invalid
actions, and local many-to-one arrows can therefore be diagnosed as downstream
projections. The same-task policy residual remains because the local observer
forgets rational continuation/frame data. This is positive horizontal
mother-carrier evidence only: the real and p-adic shadows are not identified,
the generic cross-domain carrier remains unsettled, and no new free primitive
or lowering law is introduced.

Phase 10 audits the missing reverse arrows.  A genuine contravariant duality
preserves universal properties only after reversing their variance; the
current history, place, stopping, and decoder maps have not been shown to form
such an equivalence.  On the exact rank-one projective layer,

\[
Jg=(\det g)g^{-T}J
\]

identifies the contragredient action with a conjugate action after a declared
point--covector frame.  The ordered unit frame
\((g(0),g(1),g(\infty))\) reconstructs rational projective matrix semantics on the
frozen image, while bare real points and p-adic vertices retain nontrivial
stabilizer fibres.  A local solver therefore needs a rational-image and
decoder certificate before exact lowering.  This refines the emerging
transversal and its reconstruction boundary; projective self-duality and
restored quotient fibres still create no new free primitive or process rank.

Phase 11 opens a different reverse arrow: finite state--predicate duality.
For finite \(X\), state maps act covariantly while inverse-image Boolean
homomorphisms act contravariantly on \(\mathcal P(X)\); structure-preserving
Boolean evaluations recover exactly the points.  A surjective task quotient
dually embeds the fibre-constant predicate algebra, so a residual may first be
a missing discriminator rather than a new coordinate.  The calibration also
separates Archimedean integer cofinality from real completeness and
connectedness, p-adic ultrametric predicates, and the global rational product
formula.  This adds one exact horizontal logical-observer edge, but bounded
behaviors do not establish a cofree history observer, global bidual return, or
new rank.

### 1.2 Cross-cutting admissibility — effective analysis

The two axes and the emerging evaluation transversal are governed by an
additional research constraint:

> When a presentation is claimed to support analysis, the claim must provide
> an effective symbolic and/or numerical calculation path, explicit
> certificates, error or failure semantics, and task-relative cost accounting.

This is not a third ontology axis and not a theorem that every process admits a
calculus-bearing presentation.  A finite task quotient may stop at exact
transition and observation semantics.  A continuous or higher-rank theory that
claims analysis, however, must state more than the existence of an abstract
differential, integral, or comparison object.

The principle constrains the current map in five places:

- **Presentation:** task sufficiency and analytic effectiveness are distinct;
  adequate presentations may differ in symbolic closure, conditioning, and
  cost;
- **canonicalization:** computational advantage supplies a local selection
  pressure but does not create a global canonical representative;
- **lift first:** derivatives, adjoints, phase, branch, error, and holonomy
  payload must not be quotiented away before the task declares them invisible;
- **objectification:** new primitives must charge compilation, dictionary,
  storage, residual, and lowering costs rather than treating abbreviation as a
  free computational gain;
- **V5:** formal comparison of variation is only the first level; certified and
  effective analytic closure must also compare evaluators, units, errors, and
  costs when those are part of the claim.

The operational gates are semantic adequacy, symbolic effectiveness, numerical
effectiveness, computational economy, and certified transport/closure.  They
are recorded in `65-effective-analysis-principle.md`.  This is a stable
research/engineering discipline, while the general existence and cross-rank
closure claims it motivates remain open.

### 1.3 Conjectural overlay — Arithmetic Generativity

The stable axes and transversal above do not assume that arithmetic-generated
presentations are universal.  The separately governed
[`RESEARCH_PROGRAM.md`](RESEARCH_PROGRAM.md) records the stronger possibility
that arithmetic primitives, their free process compositions, and their
objectified higher-rank operations generate a compatible executable system:

```text
arithmetic process grammar
    -> task-sufficient presentation                         U1
    -> effective native analysis                            U2
    -> costed and measured task fibres                      U3
    -> statistical adaptation and macroscopic response     U4
    -> objectification and higher-rank lowering             U5
    -> chart covariance and total computational economy     E.
```

This overlay explains why AEG, AM chart search, canonical history cost,
entropy, partition structure, and Boltzmann--BBGKY pressure appear in one
research programme.  It conjectures a common generative source rather than an
equality of complexity, entropy, action volume, probability, or thermodynamic
state count.

The overlay has no independent maturity grade.  Evidence must still land on a
typed Core construction, law, obstruction, adapter, or explicit boundary, and
the dated result must be recorded in `RESEARCH_STATUS.md`.  A generic Process
Geometry result may leave every arithmetic-specific universality obligation
open.

---

## 2. Horizontal axis — distinguishability geometry

### H0 — Process and history

**Question:** What primitive operations, transitions, histories, and continuations exist before a representation is chosen?

Current software has strong concrete support here through `process.history`, `process.finite`, and `process.local`.

**Maturity:** implemented in several concrete forms; no claim of one universal `Process` protocol.

### H1 — Exact task/future distinguishability

**Question:** Which histories or states are indistinguishable under every declared task-relevant continuation?

The canonical exact calibration is Myhill–Nerode:

\[
\text{future distinguishability}
\to
\text{continuation-stable quotient}
\to
\text{minimal DFA presentation}.
\]

The public `TaskContinuationSignature` machinery remains a **bounded finite witness** for this idea: it compares all continuations only through a declared finite depth.

The Experimental namespace contains a narrower but exact finite slice:

```text
process_geometry.experimental.FiniteTaskQuotient
process_geometry.experimental.minimize_finite_task_process
```

For a finite deterministic state carrier with a finite step alphabet and a total task observation, stable partition refinement computes the coarsest equivalence preserving the task under **all** finite continuations. The quotient carries an induced deterministic transition, and every pair of distinct quotient classes is accompanied by an explicit distinguishing continuation.

This exact finite slice does **not** establish a generic quotient/minimization framework for infinite, nondeterministic, probabilistic, continuous, approximate, or resource-bounded processes.

The Boltzmann--BBGKY Phase 1C result marks the boundary of this node.  A
one-body marginal is exact for a present-state task but fails a
next-derivative task; an A/M first jet repairs that one stronger task.  The
appropriate generalization is therefore a task/horizon/topology/error-relative
adapter, not a weakening of exact equivalence into an untyped approximate
relation.  No generic adapter category or probabilistic quotient is promoted.

The local-field Phase 8 calibration adds an exact base-preserving variant.
Starting from a declared local interface and task output, finite refinement
computes the coarsest extension stable under the binary lift actions and emits
distinguishing suffixes.  If one interface refines another, its stable quotient
also refines the former quotient, so total stable class count and the
\(\lceil\log_2N\rceil\) lower bound are monotone.  Conditional fibre size over
one base point is a separate quantity.  This implementation remains
research-local because policy-only, value, and full decoder semantics are
problem-specific and do not define a new generic API contract.

**Maturity:** theorem-level classical anchor; bounded public witness; exact finite Experimental implementation.

### H2 — Topological threshold

**Question:** When do finite-resolution distinctions form stable local neighborhoods, and when is process evolution compatible with them?

Topology is not assumed for every process. It becomes justified only when observer neighborhoods satisfy suitable refinement/locality conditions. Stronger structures such as uniformity, quasi-uniformity, metric structure, or separation axioms may or may not be present.

The exact finite H1 quotient does not by itself provide locality or topology.

The local-field finite-ball calibration gives one exact H2 model: projective
cylinders refine by parent reduction in a rooted metric tree. That observer
geometry is not promoted to the history unfolding or to a generic topology
object.

**Maturity:** foundational research program; no generic topology API.

### H3 — Entropy and intrinsic complexity

**Question:** How quickly do task-relevant or robust distinctions grow under process continuation, and what lower bounds does that impose on any adequate presentation?

This layer connects topological/metric entropy, coding, history growth, and the proposed distinction between intrinsic complexity and implementation overhead.

Current `BoundaryProfile`/Huffman machinery provides useful finite growth and coding calibrations, but no generic Process Geometry entropy object or intrinsic-complexity lower-bound contract exists.

The finite projective-cylinder task adds an exact source/coding calibration:
one fixed geometry supports different optimal Huffman trees when the source law
changes. Hence refinement growth can supply an alphabet and memory lower bound
without supplying probabilities, a coding objective, or an entropy-rate
theorem.

Its subsequent finite selector-policy task supplies a distinct control
calibration.  Exact reachable-graph exhaustion and Pareto Bellman recursion
produce replayable task-local controllers, while changing the source reverses
a conditional baseline cost ranking and changing the scalar ruler changes
twelve \(p=3\) controllers.  This supports finite H3 optimization only after
state, actions, stopping, decoder, source, and costs are declared; it does not
make the observer tree itself a policy or an intrinsic objective.

The Phase 7 transfer audit sharpens the negative boundary.  The action grammar
has an exact binary normal form, but the digit- and decoder-optimal first-bit
relations do not descend through contact, evaluated geometry, or locally
visible costs.  Exact disjoint collisions persist under greater depth, new
primes, and held-out inputs.  Thus alphabet growth can be compressed without
compressing future distinguishability or Bellman value.

Phase 8 computes the missing finite residual rather than adding more local
features.  Above S2, the coarsest transported scalar relation retains 8,126 of
8,336 possible tagged-state classes and has a maximum seventy-class fibre.
Forgetting S2 yields only 435 digit-policy or 395 decoder-policy behaviour
types, but those compact automata are task/ruler dependent and omit full
decoder semantics.  Hence local geometry, task-minimal policy state, and full
reconstruction state carry different H1/H3 complexity ledgers.

**Maturity:** classical anchors plus concrete finite coding and control shadows
exist; the general Process Geometry correspondence remains a research
question.

### H4 — Analysis of variation

**Question:** Once locality and suitable regularity exist, how should variation, derivatives, flows, observer paths, connections, and global analytic structure be expressed in the process-native presentation?

AEG is the first major model organism because its arithmetic process structure naturally developed into function theory and analysis rather than remaining a discrete hierarchy.

Current `analysis.*` modules implement important concrete languages.  The
`ConstraintCanonicalization`, `ObserverConnection`, and
`CanonicalDecomposition` records now live under `process_geometry.experimental`;
they are local executable slices, not a universal theory.

**Maturity:** strong domain-specific implementation plus developing general theory.

---

## 3. Vertical axis — semantic compression and ontology growth

### V0 — Free generation

Given primitive vocabulary \(\Sigma_r\), legal histories/composites are generated with as little accidental quotienting as the domain permits.

Current history, grammar, rewrite, and construction machinery provide several concrete realizations.

**Maturity:** implemented in multiple bounded/concrete forms.

### V1 — Semantic compression

Histories or states may be identified only relative to declared semantics. This is stronger than syntactic simplification, common-subexpression elimination, or short coding.

`FiniteTaskQuotient` fully realizes this idea in the finite deterministic class. The signed-translation calibration adds a complementary infinite algebraic example: free `S/P` histories are identified by exact net displacement, and this equivalence is stable under every continuation because

\[
q(hk)=q(h)+q(k).
\]

Other repository mechanisms—rewrite normalization, observable elimination, finite coding, and ordinary primitive proposals—remain distinct and should not be called semantic compression unless their declared semantics justify the identification.

**Maturity:** exact finite Experimental implementation plus concrete arithmetic research calibration; no generic semantic-compression abstraction across process classes.

### V2 — Objectification

A stable lower-rank semantic process becomes a new reusable primitive.

This is **not** satisfied by `PrimitiveProposal` alone. A proposal is only a candidate. Objectification matters when the new object participates in a new compositional language.

The first concrete calibration exists in the Addition/translation model organism. A signed unit-history class with net displacement \(n\) is promoted to a research-local translation primitive

\[
T_n:x\mapsto x+n.
\]

The primitive denotes the lower semantic class, not one particular `S/P` history.

The second arithmetic calibration sharpens V2. Multiplication by a positive integer \(k\) is not obtained by objectifying one fixed repeated sum such as \(T_2^3=T_6\). The same output can arise from a different process, for example \(T_3^2=T_6\). What remains stable is the **uniform repeated-Addition action**

\[
R_k(T_a)=T_a^k=T_{ka}
\qquad\forall a,
\]

which is an endomorphism of the Translation process. The research-local Multiplication primitive \(D_k\) objectifies this action schema.

This creates explicit refinement pressure: the domain of objectification may need to include stable lower-rank processes/actions such as elements of `End(C_r)` or another process carrier, not only semantic points/classes in `C_r`. One arithmetic example is not enough to choose the generic abstraction.

The finite thermodynamic calibration in
`63-thermodynamic-objectification-and-partition-towers.md` adds a different
boundary.  Any finite fibre map pushes Boltzmann mass forward, but it is
task-objectification only when the fibre semantics is continuation-stable and
the resulting object has grounded composition/lowering.  At one fixed scale,
nested free-energy pushforwards flatten exactly when the outer measure is
pulled back to the microscopic histories.  Therefore repeated log-sum-exp or
coarse-graining alone is not evidence for a new process rank.  The measure,
cost scale, and any retained holonomy are explicit objectification payloads,
not intrinsic properties silently created by the quotient.

The measured-fibration synthesis sharpens the same boundary.  A thermodynamic
macro-object may need to retain an interface

\[
(b,F_b,\nu_b,\text{couplings},\text{response},\text{residual})
\]

rather than only one base point \(b\).  Microcanonical, canonical, and
grand-canonical descriptions can correspond respectively to selecting a
fibre, reweighting fibres, or enlarging the total space.  None is a dynamic
closure, and equivalence of ensembles is only task- and limit-relative under
declared concentration/convexity hypotheses.  Such a measured interface is
still not objectified until its interaction/response semantics are
continuation-stable and it gains new free composition plus all-composite
lowering.  Likewise, an exact tower of asymptotic quotients may retain higher
order residuals without raising arithmetic rank.

The p-adic continuation-fibre audit supplies a second V2 boundary.  Its finite
stable quotient has exact composition under already admitted bit words, but
the fibres are nonuniform, transport is partial and many-to-one, and no new
free grammar or lowering theorem exists.  A transported residual may therefore
complete horizontal task state without becoming a vertical primitive.  This
also rules out treating every nonzero residual bit as one new process
dimension. Phase 9 strengthens that boundary: even when the finite task
quotients descend from one marked rational carrier with compatible place
shadows, source universality remains orthogonal to new-object generation.
Phase 10 adds the reverse red team: rank-one dualization is projectively
conjugate to the existing action, and an ordered frame restores matrix data
lost by local quotients.  Neither a dual presentation nor restoration of a
stabilizer fibre is new free generation.  New compositional syntax and
all-composite lowering remain separate obligations.  Phase 11 adds the logical
red team: a quotient embeds only its fibre-constant predicate algebra, and a
new predicate may merely restore a discriminator.  Finite Boolean biduality
and bounded response languages do not supply a task-independent cogenerator,
cofree universal property, or global biduality.

**Maturity:** two concrete AEG rank-objectification calibrations plus exact
finite thermodynamic, continuation-fibre, and semantic-adapter boundaries;
measured and filtered fibre interfaces remain T0/T1 synthesis.  Generic V2
theory remains a research program and has no Experimental/Public abstraction.

### V3 — Higher-rank free composition

The objectified primitive opens legal combinations not merely enumerated in the discovery examples.

In the signed-translation calibration, retained primitives such as \(T_2\) and \(T_{-1}\) are placed in a new free `ProcessWord` language. Composites such as

\[
T_2T_2T_{-1}
\]

produce translation by \(+3\) without requiring \(T_3\) to have been supplied as a retained seed.

The second calibration supplies the genuinely multiplicative next step. Retained primitives such as

\[
D_2,\quad D_3
\]

freely generate an unseen multiplicative composite whose lower action is multiplication by six. More importantly, the research essay admits mixed Translation/Dilation words, so the higher-rank language can express how Multiplication acts on Addition objects rather than merely forming a second isolated commutative monoid.

The thermodynamic calibration also tests free **symmetric** assembly through
the plethystic exponential.  It separates that construction from Boltzmann
weighting: nested assemblies retain bracket type and degeneracy until a
declared semantic quotient forgets them.  This is candidate V3 pressure, not a
promotion.  If the task forgets brackets, the lowering map must still push
their multiplicities forward rather than silently resetting every flat object
to unit weight.

**Maturity:** two-step arithmetic research calibration from unit histories ->
Translation -> Multiplication/action, plus a finite formal-series assembly
boundary; no generic higher-rank grammar API.

### V4 — Compositional rank lowering

Every legal higher-rank composite must admit coherent interpretation in an explicitly declared lower-rank semantic domain:

\[
\llbracket A\circ_{r+1}B\rrbracket
\simeq
\llbracket A\rrbracket\star_r\llbracket B\rrbracket.
\]

Generator-by-generator expansion is insufficient. Relations must lower soundly as well.

The signed-translation calibration provides the first concrete executable instance. Each \(T_n\) lowers to a canonical `S/P` word; lowering extends by concatenation to every legal higher-rank word; arbitrary generated terms preserve exact translation semantics; and relations such as

\[
T_mT_n\equiv T_{m+n}
\]

remain valid after lowering to the lower semantic quotient.

A red team using only absolute displacement shows why terminal compression is insufficient: \(S\) and \(P\) appear equal under \(|q|\), but continuation by \(S\) separates them.

The Addition -> Multiplication calibration forces a richer target. A nontrivial dilation \(D_k(x)=kx\) cannot lower to any fixed Translation object \(T_b(x)=x+b\). Pure multiplicative words therefore lower to endomorphisms of the Translation process,

\[
\phi_k(T_a)=T_{ka},
\]

while arbitrary mixed Translation/Dilation words lower to the positive affine monoid

\[
\operatorname{Aff}_+(\mathbb Z)
\cong
\mathbb Z\rtimes\mathbb N_{>0}.
\]

This lowering preserves all three exact relation families:

\[
T_aT_b=T_{a+b},
\qquad
D_kD_\ell=D_{k\ell},
\qquad
\boxed{D_kT_a=T_{ka}D_k}.
\]

The cross relation is the first calibrated V4 law that is genuinely noncommutative across two arithmetic process ranks.

**Maturity:** two consecutive concrete arithmetic V4 calibrations, including an action/endomorphism semantic completion and mixed cross-rank relation soundness; no generic Experimental/Public rank-lowering interpretation object.

### V5 — Cross-rank closure

When additional horizontal structure exists, stronger compatibility can be asked:

- **semantic closure** — compositional lowering;
- **topological closure** — continuous lowering between induced geometries;
- **analytic closure** — coherent comparison of local variation across ranks.

The second arithmetic calibration now supplies the explicit rank pair that the earlier theory was missing. Its finite relation

\[
D_kT_a=T_{ka}D_k
\]

is the positive-integer slice of the existing A/M finite law

\[
S_sT_t=T_{e^s t}S_s,
\]

whose infinitesimal shadow in the current analysis layer is

\[
[A,M]=A.
\]

This alignment makes the first V5 analytic-closure experiment well posed, but it does **not** prove analytic closure. No higher-rank differential/variation object and no canonical comparison transport \(\Lambda\) have yet been defined for a diagram such as

\[
D_{\mathrm{low}}\circ L
\stackrel{?}{=}
\Lambda\circ D_{\mathrm{high}}.
\]

**Maturity:** explicit semantic rank pair plus exact finite/infinitesimal AEG bridge; analytic closure remains a research hypothesis and the next vertical executable target.

Under the Effective Analysis Principle, a formal differential square is
necessary but not sufficient for the strongest V5 claim.  The research program
distinguishes:

1. formal closure of variation objects;
2. certified closure with exact residual or controlled error and a red team;
3. effective closure in which symbolic/numerical evaluation, units, failure
   semantics, and accounted cost lower coherently.

No generic V5 result currently reaches the third level.

---

## 4. Cross-axis roles of the current software layers

The existing public pipeline remains useful, but it should be read as an engineering decomposition rather than the entire ontology:

```text
Process -> Presentation -> Discovery -> Analysis
```

### Process

Carries concrete primitive dynamics, histories, finite actions, and local realizations.

### Presentation

Carries explicit, auditable realizations: rewriting, constraints, generated grammars, relations, task-sufficiency evidence, morphisms, and costs.

A presentation may realize an exact quotient, a local geometry, an algebraic observable image, a code, or another task-sufficient structure. The word does not imply that all Process Geometry has already been reconstructed.

### Discovery

Searches candidate observables, presentations, languages, quotients, or structures. Discovery algorithms are proposal mechanisms, not ontology.

### Analysis

Provides mathematical languages for variation and global structure supported by successful presentations.

The word `Analysis` carries an operational obligation.  A concrete family
should state its function/observable language, process operators, closure or
controlled extension, evaluator, certificates, and numerical domain/error
semantics when numerical behavior is claimed.  Current A/M, algebraic, and
Abelian families satisfy different local slices; none is a universal calculus.

### Experimental

Hosts explicitly unstable theory-to-code probes. Experimental is not a fifth stable ontology layer and is never re-exported from the package root merely because an experiment works.

The exact finite task quotient is the first Experimental probe added specifically to close a Theory Map implementation gap rather than to support one named classical problem. Both current AEG V2–V4 rank-transition calibrations remain research-local rather than entering Experimental before independent domains establish the right abstraction.

The local canonical-observer records are also owned by Experimental.  Their
historical `presentation.canonicalization`, `analysis.connection`, and
`analysis.decomposition` paths are 0.0.x compatibility shims and are not part of
the declared namespace surfaces.

---

## 5. AEG and Arithmetic Universality

AEG has two roles that must remain distinct.

First, it is the current **model organism** for Process Geometry:

- the signed-translation calibration makes the first objectification/rank-lowering step executable;
- the Addition -> Multiplication calibration makes the second rank transition executable and shows that a higher primitive may objectify an endomorphism/action on lower-rank semantic objects;
- the second transition forces the mixed semidirect relation `D_k T_a = T_(ka) D_k`, which is the discrete slice of the existing A/M finite relation;
- A/M and related work display a native language of variation and analysis, so analytic closure can now be asked across an explicit rank boundary;
- A/M finite relations, action tables, resonant extensions, residuals, and path
  flow also make it the first model organism for the Effective Analysis
  Principle;
- the same lineage therefore pressures both the vertical and horizontal axes.

Second, a stronger conjecture asks whether arithmetic-generated geometries provide universal covers or standard models for a much broader class of process geometries.

A nontrivial working formulation would require more than encoding arbitrary
data into integers.  For an independently specified class of process
geometries, the arithmetic tower would have to provide a free or otherwise
universal presentation language from which the target structures arise by
typed subobjects, quotients, fibrations, completions, or gluing, while
preserving declared continuation, measure, residual, and lowering semantics.
It would also need an effective calculus: compilation and decoding algorithms,
certificates, failure modes, and complexity bounds.  A construction that hides
the original structure wholesale in relations, residuals, or a decoder is a
Gödel-style encoding control, not evidence for the conjecture.

That second claim is **not** part of the definition of Process Geometry and is not assumed by the software.

```text
Process Geometry                    general evolving framework
AEG                                 first major model organism
Arithmetic Geometric Universality   stronger open conjecture
```

---

## 6. Maturity vocabulary for theory-to-code review

Every substantial proposed abstraction should be located using one of these states:

| State | Meaning |
| --- | --- |
| **classical anchor** | established external mathematics used as calibration |
| **implemented concrete** | executable structure with deliberately local semantics |
| **calibrated candidate** | implementation has survived meaningful examples/red teams but is not generic |
| **experimental abstraction** | explicitly generalized candidate under repository governance |
| **public commitment** | promoted semantic API contract |
| **research hypothesis** | plausible theoretical structure not yet earned by implementation/evidence |
| **open conjecture** | stronger claim whose truth is not assumed by the framework |

A code symbol and a theory node need not have the same maturity. For example, a concrete Experimental `ObserverConnection` record can exist while the general observer-connection theory remains unsettled. Likewise `FiniteTaskQuotient` can be exact in its finite deterministic class while the general theory of task quotients remains broader and unsettled. The two current AEG V2–V4 examples can form a consecutive arithmetic rank calibration while `Objectification`, `ProcessRank`, and `RankLowering` remain intentionally absent as package abstractions.

---

## 7. Mandatory theory-impact questions for API review

Any change that adds, renames, generalizes, promotes, or materially changes an Experimental or Public API should include a short **Theory Impact** section in its PR/AEP/promotion note.

It must answer:

1. **Theory position** — Which node or arrow in this map does the API represent or test?
2. **Maturity** — Is that theory element a classical anchor, concrete implementation, calibrated candidate, experimental abstraction, public commitment, hypothesis, or open conjecture?
3. **Semantic claim** — What mathematical meaning does the API name/signature commit to?
4. **Non-claim** — Which nearby stronger interpretation is explicitly *not* being claimed?
5. **Evidence** — Which independent domains, certificates, or red teams justify this level of generality?
6. **Map effect** — Does the result support, refine, split, contradict, or leave unchanged the current Theory Map?
7. **Migration risk** — If the Theory Map changes later, can this API evolve without forcing the repository to preserve a known-wrong ontology?
8. **Effective-analysis impact** — If the API claims analysis, calculation, or
   computational advantage, what are its symbolic/numerical mode, certificates,
   error/failure semantics, baseline, units, and cost boundary?
9. **Mathematical Core effect** — Which primitive data, construction,
   law/obstruction, information contract, covariance/unit rule, or boundary in
   `MATHEMATICAL_CORE.md` does the result implement, refine, contradict, or
   leave unchanged?
10. **Engineering Architecture effect** — If calculation, search, stability,
    or efficiency is claimed, which algorithm, evaluator, certificate,
    error/failure semantics, units, decoder, baseline, dependency, budget, or
    cost decision in `ENGINEERING_ARCHITECTURE.md` changes?

For a purely mechanical change, the answer may be one sentence: “No theory position changes; this preserves the existing semantic contract.”

For a new foundational abstraction, absence of a meaningful Theory Impact section is itself evidence that the API is premature.

---

## 8. Review rule: theory may evolve; API claims must stay narrower

The Theory Map is expected to change. Therefore engineering review should enforce the asymmetry

```text
API semantic commitment  <=  evidence-backed portion of the evolving theory
```

and never the reverse.

A useful implementation may be merged without promoting its most ambitious theoretical interpretation. Conversely, a compelling theoretical note does not justify a public class until executable cross-domain evidence and governance gates are satisfied.

When theory and code disagree, record the disagreement explicitly. Do not silently rename one side until the mismatch disappears on paper.

---

## 9. Current high-value structural questions

The following narrow implementation questions have now been answered:

1. bounded `TaskContinuationSignature` can be complemented by an exact/minimized task quotient in the finite deterministic class;
2. a complete V1 -> V4 cycle can be realized concretely for signed unit histories objectified as Addition/translation primitives, including continuation congruence, new free composition, compositional lowering, relation soundness, and a negative control;
3. the next Multiplication object should not objectify one fixed repeated sum but the uniform repeated-Addition endomorphism `R_k(T_a) = T_(ka)`;
4. pure multiplicative free composition lowers naturally to endomorphisms of the Translation process, while mixed Addition/Multiplication composition requires the richer affine semantic completion `Z ⋊ N_{>0}`;
5. the noncommutative AEG cross relation `D_k T_a = T_(ka) D_k` lowers soundly for arbitrary generated mixed histories, and the same finite law already underlies the existing A/M calculus;
6. a finite marked rational projective-history carrier can precede compatible
   real and p-adic place evaluations and multiple stopping/decoder quotients;
7. in the finite rank-one calibration, the ordered frame
   `(g(0), g(1), g(infinity))` reconstructs rational projective matrix
   semantics, while bare hyperbolic points and p-adic lattice vertices do not;
8. projective contragredience preserves exact incidence after an explicit
   point--covector identification, but a genuine categorical duality would
   reverse universal-property variance and has not been established for the
   full history/task/decoder chain;
9. finite state maps dualize exactly to inverse-image Boolean homomorphisms,
   finite points are recovered by structure-preserving truth evaluations, and
   task quotients dualize to fibre-constant predicate subalgebras, without
   producing an infinite cofree observer or new process rank.

The next high-value questions are therefore:

1. what is the smallest correct **higher-rank variation object** for a smooth Multiplication/Dilation rank, and what exactly is the lower variation object it should map into?
2. can one construct a canonical comparison map `Lambda` so that a first V5 diagram `D_low ∘ L ≃ Lambda ∘ D_high` commutes, or does the semidirect/noncommutative relation force an adjoint or connection correction term?
3. what is the first clean red team where naive derivative commutation across ranks fails while a corrected analytic-closure law survives?
4. independently, what concrete observer-neighborhood object is the smallest legitimate H2 topological-threshold experiment?
5. can exact task quotients plus `BoundaryProfile`/Huffman separate intrinsic distinguishability complexity from realization overhead in a calibration where both are independently known?
6. which current `PresentationMorphism` semantics survive when used between ranks rather than only between presentations at one level?
7. when does a thermodynamic or plethystic objectification retain a genuinely
   non-flattenable boundary—distinct scale, assembly type, relation,
   reference measure, or task-visible holonomy—rather than merely regrouping
   one finite mass pushforward?
8. can the frozen PCR3BP return--partition--holonomy contract make those
   obstruction coordinates presentation-covariant under its two gate systems,
   or does the proposed classification language remain presentation-relative?
9. across one exact discrete, one independently checkable continuous, and one
   nonintegrable/singular red-team process, which parts of the Effective
   Analysis Principle survive without forcing a single universal calculus?
10. what is the smallest task-sufficient lift between full history unfolding
    and visible state, and when—if ever—is it forced to agree with a
    topological or analytic universal cover?
11. beyond the finite projective frame calibration, can unit frames, stopping
    sections, task kernels, and fundamental domains be related functorially
    without making a unit choose a quotient or a lattice choose a scalar cost?
12. is there a typed theorem connecting continuous coarea volume and finite
    task-visible residual memory, or do red teams force them to remain
    separate resource components?
13. across the p-adic irregular continuation fibre, the pendulum's finite
    sheet transport, and a nonintegrable return-map residual, which additional
    laws distinguish horizontal task-state completion from genuine vertical
    objectification with free composition and lowering?
14. do real and p-adic continued-fraction sections transform covariantly when
    their ordered frame, cusp, unit, residue section, and stopping data are
    transported together?
15. can a local geometric solver preserve or certify return to the common
    rational frame image, with explicit outside-image and approximation
    semantics when it cannot?
16. beyond the finite Stone and bounded-behavior calibration, does a free
    marked-history carrier have a precise dual cofree/decoder universal
    property, or do the information-losing place and stopping maps obstruct
    such an adjunction?
17. can finitely supported real/p-adic place data satisfying the rational
    product formula form a certified restricted-product carrier with explicit
    frame-image, topology, solver-closure, and lowering semantics before an
    adelic abstraction is proposed?
18. which task-relative semantic adapters compose, and how do their horizons,
    topologies, error budgets, residuals, and closure sections transform?
19. when does a macro-observable admit a useful measured task fibration whose
    conditional fibre laws and transverse ensemble law are computationally
    accessible rather than merely existential?
20. can a filtered tower of continuation-stable asymptotic quotients capture
    correlations or closure defects without confusing jet depth, observer
    order, and arithmetic rank?
21. is there a nontrivial universality theorem for an effectively calculable
    arithmetic presentation class that survives the relation/residual/decoder
    encoding red team?

These are research questions, not a backlog of API classes to create.

---

## 10. Standing interpretation

The current compact statement is:

> **Process Geometry studies how process histories are generated, distinguished, semantically compressed, presented, and—when justified—objectified into new compositional ranks, together with the topological, complexity, and analytic structures induced within and between those ranks; when analysis is claimed, the induced language must remain effectively calculable, certifiable, and cost-auditable.**

This sentence is a working research orientation. Its purpose is to keep engineering choices legible inside the larger mathematical program while leaving the mathematics free to improve.
