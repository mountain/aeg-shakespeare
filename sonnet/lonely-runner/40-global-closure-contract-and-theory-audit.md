# Phase 15A — global closure contract and Theory Map audit

**Audit date:** 2026-08-24

**Mathematical target:** `LRC(13)`, meaning 13 relative speeds and 14 total runners

**Executable declaration audit:** `python/lrc13_closure_contract.py`
**Executable red teams:**

- `tests/research/test_lonely_runner_lrc13_closure_contract.py`
- `tests/research/test_lonely_runner_canonical_lazy_contact_compiler.py`
- `tests/research/test_lonely_runner_canonical_contact_state.py`
- `tests/research/test_lonely_runner_clean_separator_theory.py`

## 1. Result first

Sonnet 001 is not one closure problem.  It contains four distinct closure
contracts, and they must not borrow status from one another.

| contract | audited status | strongest justified statement |
| --- | --- | --- |
| `LRC(13)` mathematics | **OPEN** | The first three `K=13,p=199` initial-sieve workers preserve exact output under the Phase-5 prune.  No complete prime proof exists. |
| bounded Sonnet mechanism | **PARTIALLY CLOSED** | Several declared K4/K5 domains have exact canonical dynamics, task presentations, and clean/obstruction certificates.  This is not an arbitrary-K or unbounded-domain theorem. |
| Theory Map evidence | **LOCAL SUPPORT ONLY** | Sonnet strongly calibrates H0/H1, finite H3 coding shadows, and V0/V1.  `Clean` is a T3/local finite obstruction law.  H2 and V2--V5 are not established. |
| engineering/API | **RESEARCH-LOCAL** | Exact tests and manual heavy gates exist; certificate hardening and status authority are improved here.  No Experimental or Public API promotion is justified. |

The previous phrase “contact-depth line closed” meant a bounded representation
claim.  It never meant that `LRC(13)` was proved, that Theory Map V5 closure was
reached, or that a public abstraction had matured.

## 2. Primitive audit: two exact lines that have not rejoined

The repository has developed two rigorous but presently noncommuting lines.

```text
modular proof line

residue speeds -> I(k,p,1) set cover -> lift/project -> J(k,p)=empty
               -> enough certified primes -> finite product contradiction

continuous representation line

torus contact process -> canonical event compiler -> declared stopping task
                      -> pair-ratio query grammar -> task quotient
                      -> selective materialization -> Clean / obstruction
```

They share the Lonely Runner inequality and the discipline of future-relative
semantics.  No theorem currently maps a K4/K5 continuous contact classifier to
a task-preserving prune, lift invariant, or certificate for `I(13,p,1)`.

### 2.1 Native primitives

For the modular line the native objects are:

- folded residue speeds modulo `p`;
- ansatz times `a/(lp)`;
- bad-time cover sets;
- fixed-cardinality partial covers;
- exact lift and backward-projection relations.

For the continuous line the native objects are:

- positive relative speeds modulo global scale;
- torus phases `tu_i mod 1`;
- the next boundary event and simultaneous minimum group;
- exact multiplicative difference constraints;
- a separately declared stopping task.

Pair-ratio walls, decision trees, Huffman histories, and task DAGs are derived
presentations.  They are not physical primitives.

### 2.2 Assumptions and forbidden substitutions

This audit assumes the finite-checking proposition and `B_k` used by the pinned
2026 computation.  It does not assume that the current upstream K13 configuration
is a complete proof plan.

The following substitutions are forbidden:

1. continuous LR feasibility must not be identified with one finite ansatz grid;
2. a task label must not be called a reconstructible witness without a decoder;
3. pairwise or partial-region separation must not be called global minimality;
4. a bounded K4/K5 exact census must not be extrapolated to K13;
5. finite coding cost must not be called intrinsic entropy;
6. a local task quotient must not be called Theory Map objectification;
7. an implementation or green workflow must not be used as evidence of a theorem.

### 2.3 External mathematical landscape

Globally, Lonely Runner is not only a scheduling puzzle.  The same statement
sits in several established languages:

1. **Simultaneous Diophantine approximation and torus dynamics.**  An integer
   speed vector generates a one-dimensional subtorus of
   `(R/Z)^k`; loneliness is a hitting/avoidance statement in the `L-infinity`
   geometry of that orbit.  The modern spectrum programme studies not only the
   extremal conjectured threshold but the set and accumulation structure of
   distances realized by subtori.  See
   [Relative Lonely Runner spectra](https://arxiv.org/abs/2411.12684).
2. **View obstruction, billiards, and geometry of numbers.**  Classical
   reformulations connect rays and billiard trajectories to covering radii of
   lattice zonotopes.  This is the geometric source of the finite product bound
   used by the computational proof architecture.  See
   [Henze--Malikiosis](https://arxiv.org/abs/1609.01939).
3. **Finite checking.**  Tao proved that a finite velocity check suffices, and
   the zonotopal route reduced the bound to linearly exponential scale.  See
   [Tao](https://arxiv.org/abs/1701.02048) and
   [Malikiosis--Santos--Schymura](https://arxiv.org/abs/2411.06903).
4. **Combinatorics.**  Distance graphs, chromatic formulations, nowhere-zero
   flows, additive/probabilistic estimates, and tight-instance structure give
   other projections of the same extremal threshold.  The recent overview in
   [Mixed thresholds in the Lonely Runner Conjecture](https://arxiv.org/abs/2605.27941)
   records this wider neighbourhood.
5. **Computer-assisted proof.**  The current fixed-dimensional frontier turns
   the finite theorem into modular obstruction sets, symmetry quotienting,
   set-cover enumeration, lifting, and backward projection.  See
   [Sungkawichai--Trakulthongchai](https://arxiv.org/abs/2604.23906).

Sonnet 001 currently contributes at the interface between the third and fifth
languages: exact task-relative representations of a finite proof search, plus a
bounded continuous model organism.  It has not produced a new theorem about
zonotope covering radii, Lonely Runner spectra, chromatic numbers, or flows.

## 3. Exact mathematical closure contract

The finite-checking proposition requires a set `P` of distinct primes such that

1. `LRC(12)` is established;
2. `J(13,p)` is certified empty for every `p in P`; and
3. the exact product threshold is met:

\[
\prod_{p\in P}p \ge B_{13},
\qquad
B_{13}
=\left(\frac{\binom{14}{2}^{12}}{13}\right)^{13}
=7^{156}13^{143}.
\]

The new declaration auditor represents these as separate machine-audited
hypotheses.  It rejects duplicate or composite entries and decides the product
inequality by integer cross multiplication; logarithms are diagnostics only.
It does **not** inspect the contents of a J-empty certificate, predecessor proof,
generator output, or aggregate artifact, so its `declared_complete` fields are
not theorem verdicts.  A terminal campaign still requires the independent
artifact verifier listed below.

### 3.1 Frozen upstream K13 snapshot

At pinned upstream commit
`755b116b2e6090cd4a83187a696f863388b7d746`:

| audit item | result |
| --- | ---: |
| K13 `PrimeList` entries | 45 |
| distinct primes | 44 |
| duplicate | `293` |
| natural log of distinct-prime product | approximately `254.231` |
| natural log of `B_13` | approximately `670.350` |
| natural-log deficit | approximately `416.119` |
| executable target selected by `main()` | `K=9` |
| expected aggregate `results/result_14` | absent |
| complete `J(13,p)=empty` certificates | none |

Thus even a hypothetical successful completion of every prime currently listed
would not meet the final product threshold.  Repeating `293` cannot increase a
set-of-primes product.  The prime campaign itself must be designed and frozen
before a terminal computation is described as a proof campaign.

### 3.2 Required proof bundle

`LRC(13)` may be marked closed only when one immutable bundle contains:

1. the exact theorem statement and runner-count convention;
2. the external finite bound and predecessor theorem versions;
3. a duplicate-free prime manifest whose exact product meets `B_13`;
4. complete coverage of every initial-sieve worker for every declared prime;
5. all lift/project stages and a final `J(13,p)=empty` certificate per prime;
6. hashes and provenance for the generator outputs;
7. a small checker independent of the high-performance generator;
8. a final exact product verification.

Missing one worker, prime, lift stage, artifact, or checker leaves the mathematical
status `OPEN` or `PARTIAL`.

## 4. Certificate hardening for the bounded mechanism

### 4.1 Why the former partial-singleton proof template was insufficient

Suppose two task regions have these partial signatures:

| region/task | `c0` | feasible joint values of `(c1,c2)` |
| --- | ---: | --- |
| A | `-` | `(--), (++)` |
| B | `+` | `(-+), (+-)` |

At partial-region level `c0` is the only coordinate forced to opposite signs.
Nevertheless `(c1,c2)` jointly separates the two tasks, because the two sets of
complete values are disjoint.  Therefore:

> “unique forced separator of two partial regions” does not generally imply
> “mandatory coordinate in every complete task presentation.”

This three-coordinate construction is now frozen as an executable red team.

### 4.2 Strong replacement certificate

For a declared complete coordinate grammar `C`, a selected coordinate `c` is
certified mandatory by two feasible complete sign cells satisfying

\[
T(s_L)\ne T(s_R),\qquad
s_L|_{C\setminus\{c\}}=s_R|_{C\setminus\{c\}},\qquad
s_L(c)\ne s_R(c).
\]

Deleting `c` therefore creates an unavoidable cross-task collision even when
all other coordinates are used jointly.  Exact minimality needs both:

- one such deletion witness for every selected coordinate; and
- a sufficiency check that the selected projection is task-pure on every
  feasible complete sign cell.

The K4 compiler now materializes all 4,343 feasible cells of its complete
33-coordinate generated grammar.  It re-certifies:

| K4 task projection | selected coordinates | strong deletion witnesses |
| --- | ---: | ---: |
| full first-event certificate | 27 | 27 |
| event-rank-free boundary task | 19 | 19 |
| boundary/mode task | 19 | 19 |
| mode only | 12 | 12 |

For the base K5 domain `delta=1/6`, `u5/u1<21/4`, synchronized exact completion
of paired terminal closures provides the analogous full-98-coordinate witnesses:

| K5 task projection | selected coordinates | strong deletion witnesses |
| --- | ---: | ---: |
| full first-event certificate | 86 | 86 |
| event-rank-free boundary task | 36 | 36 |
| boundary/mode task | 36 | 36 |
| mode only | 27 | 27 |

These are minimum results only inside the stated generated coordinate grammar.
They do not establish representation-independent intrinsic complexity.  Wider
Phase-12/13 sweep counts remain bounded-domain claims and require the same strong
certificate before their minimum language is reused.

### 4.3 Boundary/mode is a task label, not a self-contained witness

The historical function name `canonical_witness` drops event rank and universal-
cover contact center.  The collision below makes the information loss explicit:

| speeds | event index | witness time | lifted boundary | retained label |
| --- | ---: | ---: | --- | --- |
| `(1,2,3,5)` | 6 | `6/25` | `((3,1,exit),)` | `((3,exit), interval)` |
| `(1,3,4,5)` | 11 | `11/25` | `((3,2,exit),)` | `((3,exit), interval)` |

The quotient is exact for the declared boundary/mode task.  It is not a lossless
compression of the full witness.  A full cost comparison must include the input,
provenance, replay decoder, and reconstruction cost when actual time is required.

## 5. Global Theory Map placement

The audit uses the Theory Map nodes and T0--T4 governance literally.

| node or edge | Sonnet 001 evidence | audited maturity and role | prohibited promotion |
| --- | --- | --- | --- |
| H0 process/history | exact modular cover process; exact bounded torus contact process; deck/scale separated from physical state | T2/local | one universal `Process` protocol |
| H1 future/task distinguishability | finite future signatures, task projections, exact terminal task presentations | T2/local | arbitrary-process Myhill--Nerode quotient |
| H1 -> presentation | `Clean` exactly characterizes zero-completion decision trees for finite partial-sign systems | T3/local | generic `CompletionObstruction` API |
| H2 topology | no observer-neighborhood or continuity theorem | unchanged | `ObserverTopology` |
| H3 coding shadow | exact finite tree/DAG/frontier and weighted-depth measurements | T2/local calibration | intrinsic/process/topological entropy |
| H4 variation | exact contact laws and canonical torus evolution in declared domains | T2/local | HJB, global analysis, or discrete `ObserverConnection` |
| V0 free generation | contact histories and compiler-generated event comparisons | T2/local | universal higher-rank process language |
| V1 semantic compression | requirement antichains and task-relative projections | T2/local | task-independent compression |
| V2 objectification | minimum-group outcome is only a candidate new task vocabulary | T0/local candidate | Theory Map `Objectification` or `ArgminPrimitive` |
| V3--V5 | no higher-rank grammar, compositional lowering, or cross-rank closure | unchanged | any promotion |

### 5.1 Canonicalization splits rather than forces one connection concept

The continuous programme contains two different mechanisms:

1. smooth maintained normalization may induce an observer ODE;
2. discrete deck/scale quotient removes representation provenance and yields a
   center-free event map.

The second is not an `ObserverConnection`.  Sonnet therefore provides a useful
negative calibration against the claim that every canonicalization induces a
nontrivial observer motion.

### 5.2 Huffman and continuous planning boundaries

The finite Huffman objects are exact coding/decision geometries for a declared
task distribution.  DAG reconvergence already shows that a real-tree carrier can
forget structural sharing.  These results are finite H3 shadows, not entropy.

The continuous history-planning extraction remains T0.  No controlled scaling
limit, HJB convergence, or identification of the canonical observer path with an
optimizer has been proved.  The H3-to-H4 coarea proposal remains T1; Sonnet does
not supply its missing discrete-to-continuous bridge.

### 5.3 Five meanings of “closure” that must remain distinct

1. multiplicative constraint closure;
2. bounded contact-tail sufficiency for one task and domain;
3. completion of a canonicalization calibration sequence;
4. exact bounded compiler/task closure;
5. Theory Map V5 closure or proof of `LRC(13)`.

Only the first four occur locally in existing Sonnet work.  The fifth does not.

## 6. The missing bridge and the next exact task

The continuous K4/K5 line should now be frozen as a model organism rather than
extended by blind ratio-window scans.  The next problem-native task is resolution
survival in the modular proof line.

For fixed `(k,p)`, define the projected obstruction carrier

\[
S_l(k,p)=\pi_{lp\to p}I(k,p,l).
\]

The paper's definition is exactly

\[
J(k,p)=\bigcap_{l\ge1}S_l(k,p).
\]

When `l` divides `m`, properness at level `l` persists to compatible level-`m`
lifts, so the obstruction carriers refine along divisibility.  This gives a
divisibility-indexed resolution filtration.  It is the most natural global
Process Geometry object in the proof: an H1 future-distinguishability problem
across resolution, not a V5 analytic closure.  Calling it a profinite or inverse-
limit object would require an additional coherent-lift theorem; the intersection
identity alone does not license that stronger ontology.

A `Squeeze<2>` or `Squeeze<3>` run explores selected arrows in this filtration.
Nonempty stabilization under those selected arrows is not by itself a proof that
a tuple belongs to `J(k,p)`, while an actually empty certified level is sufficient
for the prime proof.

For a partial `I(k,p,1)` search state `h`, define a bounded lift-survival task:

\[
Q_{c}(h)=1
\iff
\text{some legal completion of }h\text{ has an improper lift to level }c.
\]

This is a future task, not a new ontology.  Any safe prune derived from it must
prove `Q_c(h)=0`.  It directly composes the two operations that the current solver
separates: completion of the initial cover and survival under the first lift.

The pinned harness now supports a reproducible lexicographic seed sample via

```text
worker-lift-sample 199 0 2000
```

The experiment sorts canonical seeds before sampling; it does not depend on the
iteration order of the upstream `unordered_set`.  It reports both the first
2,000 lexicographic seeds and 2,000 equidistant indices across the complete
sorted worker set.  This dual protocol is necessary because lift survival is
strongly nonuniform across the canonical ordering.

One local pinned run produced:

| worker-0 item | result |
| --- | ---: |
| complete canonical seeds | 1,235,622 |
| lexicographic-prefix survivors at first `l=2` lift | 1,159 / 2,000 |
| equidistant-stratified survivors at first `l=2` lift | 28 / 2,000 |
| lifted classes from the stratified sample | 37 |
| full initial enumeration time on that machine | approximately 159 s |
| both 2,000-seed lift samples together | approximately 0.43 s |

The large protocol difference is itself a red team: neither hash-container order
nor one lexicographic prefix is a defensible population estimate.  The stratified
result suggests strong lift information across the carrier, while the prefix
shows that survivors are structurally clustered.  Both results are directional
only.  Leaf-level filtering cannot accelerate the expensive initial enumeration.
The research question is whether exact lift viability can be lowered to partial
DFS states cheaply enough to prune before leaves.

### 6.1 Pre-registered next hypotheses

**H-LIFT-1 — partial lift viability.**  A solved-case-derived bounded certificate
for `Q_2(h)=0` removes enough nodes to pay for itself in the pinned upstream C++
search.

- positive gate: exact output equality plus net paired speedup on frozen K8--K12
  cases without K-specific retuning;
- kill condition: no matched-cost gain, or certificate cost grows faster than
  the saved subtree work;
- safety gate: an independent exhaustive small-world oracle agrees on every
  partial state.

**H-LIFT-2 — direct level-2 search.**  Searching lift choices jointly at modulus
`2p`, then projecting survivors, is cheaper than enumerating all of `I(k,p,1)`
and lifting at leaves.

- positive gate: exact equality with `Project(I(k,p,2))` on solved cases;
- kill condition: symmetry loss or duplicate generation erases the stronger
  cover constraint;
- forbidden shortcut: no prefix canonicalization unless continuation legality
  under MRV sibling elimination is proved.

Only after one hypothesis is selected and frozen on solved cases may untouched
K13 workers be used as validation.  Workers 0--2 are no longer holdouts.

## 7. Cost and engineering discipline

Correctness and performance evidence are separate.

- The K13 worker byte-equality hashes are strong correctness evidence.
- One baseline/patched timing pair per worker, always in the same order, is not a
  robust performance estimate; the 4.5% result especially needs repetition.
- Future reports must include interleaved paired runs, search-node and prune-hit
  counts, hardware/toolchain provenance, and uncertainty.

CI is divided into four gates:

1. fast multi-version semantic regression;
2. single-version research-exact workflows with complete dependency paths;
3. manual pinned frontier experiments with immutable artifacts;
4. build/release validation independent of the research campaigns.

This phase adds missing Phase-11 exact compilation coverage, repairs Phase-13/14
dependency triggers, and makes Phase-9/10 manual jobs execute their full tests
rather than only printing scripts.

### 7.1 Document authority and historical numbering

The duplicated numeric filename prefixes `31`, `38`, and `39` are historical
identifiers, not a reliable total order.  Renaming them in place would break
existing links and review provenance.  Authority is therefore explicit:

1. this Phase-15A note and the top of `lonely-runner/README.md` own current status;
2. older phase notes own their frozen bounded observations;
3. Phase-15A correction callouts supersede older terminology or proof templates;
4. executable tests own exact counts at the referenced commit;
5. the declaration audit enumerates the final gate; mathematical closure must
   be owned jointly by exact manifest checking and an independent verifier of
   every referenced proof artifact.

Future notes must use a unique filename and state which prior claim they refine,
supersede, or merely calibrate.

The repository now uses the standard spelling `Huffman` throughout filenames,
metrics, and executable symbols.  The spelling correction does not promote every
local decision tree to classical Huffman optimality: uses outside the classical
fixed-alphabet prefix-code setting must state their alphabet, weights, allowed
query arities, admissible geometry, and optimization objective.  Historical
numerical evidence is unchanged; only the erroneous spelling and corresponding
internal identifiers were migrated.

## 8. Claim ledger

### Claims admitted

1. The current K13 upstream prime manifest is not a mathematically sufficient
   terminal prime campaign, independent of runtime.
2. The K4 and base K5 minimum-coordinate counts listed above have strong deletion
   certificates in their declared complete generated grammars.
3. Boundary/mode projection is exact for that task and loses full-witness data.
4. Finite `Clean` is an exact grammar-relative obstruction theorem.
5. The continuous and modular lines do not yet have a task-preserving bridge.

### Claims rejected

1. `LRC(13)` is solved or computationally close to solved.
2. Completing the currently listed K13 primes would by itself prove `LRC(13)`.
3. The Phase-11 boundary/mode label is a reconstructible witness without replay.
4. Partial singleton separators prove global coordinate minimality in general.
5. K4/K5 contact geometry transfers to K13 without a theorem.
6. Sonnet establishes H2, intrinsic entropy, HJB, Theory Map objectification,
   rank lowering, or V5 closure.
7. Any new Public API follows from this audit.

## 9. Completion decision

Phase 14 completes a valuable bounded representation study: canonical process,
task-relative compilation, and a genuine clean obstruction are all now sharply
understood.  Phase 15A closes the ambiguity about what that work means globally
and hardens two certificate classes.

It does not close the original mathematical target.  Sonnet 001 remains active,
but its mainline is now the exact modular resolution bridge and the full
finite-checking contract.  Further local contact-window scans require a new
pre-registered structural hypothesis; they are no longer the default path.

No Experimental or Public API promotion is proposed.
