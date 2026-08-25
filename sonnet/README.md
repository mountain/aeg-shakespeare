# Sonnet

`sonnet/` is Shakespeare's problem-centered research workspace for classical and open mathematical problems.

The name is intentional: a sonnet is a constrained form in which a difficult idea is forced into a compact structure. Here the constraint is mathematical rather than literary. Each study asks whether a hard problem admits a substantially better **process presentation** than the representation in which it is usually attacked.

## Role in the repository

The repository now has three complementary entry levels:

```text
examples/         small runnable API entry points
tests/research/   executable mathematical calibrations
sonnet/           problem-centered investigations of classical/open problems
```

A `sonnet` is therefore not a quickstart and not, by itself, a proof. It is a sustained research line organized around one named problem, with explicit primitive assumptions, task semantics, representation hypotheses, certificates, red teams, and claim boundaries.

## Selection criterion

A problem belongs here when most of the following are true:

1. **Classical or independently recognized.** The problem should have a clear mathematical lineage and a stable statement independent of Shakespeare.
2. **Genuinely unresolved or structurally difficult.** Prefer open cases, sharp computational frontiers, or classical problems whose accepted methods expose a real representation bottleneck.
3. **Exact task semantics.** There should be a precise criterion for what counts as solving, refuting, reducing, or certifying the target instance.
4. **Process-first formulation.** The primitive dynamics, operations, histories, or local moves can be stated without importing the expected advanced solution language as ontology.
5. **Competing presentations matter.** The known difficulty should plausibly depend on branching, quotient choice, hidden history, reconstruction cost, topology, singularity, or some other representation issue.
6. **There is a falsifiable comparison.** Shakespeare should be compared against a credible baseline under matched information and computational budgets.

Fame alone is not a selection criterion. A famous problem is a poor `sonnet` if the current framework has no principled way to engage its actual bottleneck.

## Expected structure of a problem study

A problem directory should normally make the following chain explicit:

```text
classical statement
    -> primitive process
    -> exact task semantics
    -> known representation bottleneck
    -> candidate presentations / quotients
    -> discovery or transformation search
    -> certificates and red teams
    -> baseline comparison
    -> claim boundary
```

Useful artifacts may include:

- a concise mathematical statement and literature map;
- exact small-instance or finite-instance oracles;
- baseline implementations or reproducible reference results;
- candidate `Presentation` objects and `PresentationMorphism` witnesses;
- bounded task signatures used to justify history quotients;
- search budgets and Pareto cost comparisons;
- adversarial examples that break over-aggressive quotients;
- links to substantial executable arguments under `tests/research/` when they mature.

## Research discipline

A `sonnet` should distinguish four levels of result:

1. **re-expression** — Shakespeare can encode a known argument or solution;
2. **compression** — a task-equivalent presentation is measurably cheaper;
3. **structural discovery** — the framework discovers a useful quotient, relation, invariant, or morphism not supplied in advance;
4. **new mathematics** — the resulting presentation resolves a previously open case or proves a new theorem.

These levels should not be conflated. In particular, reproducing a classical solution in process language is calibration, not evidence that Shakespeare has solved the underlying representation problem.

## Study ledger

The ledger records repository state, not mathematical prestige. A line may be
closed after a useful negative result, active without any theorem claim, or
deferred until its next oracle/evidence gate is affordable.

| Study | Current state | Highest responsible claim | Authoritative entry / next gate |
| --- | --- | --- | --- |
| [`local-field-projective-process-geometry/`](local-field-projective-process-geometry/) | Phase 3 matched Ruban/Browkin rational comparison | level-1 cross-place re-expression with exact projective contact, matrix/lattice-prefix, outcome, continuation, and cost red teams; no task-free \(p\)-adic selector is preferred | [matched-selector ledger](local-field-projective-process-geometry/04-phase3-padic-selector-matched-task.md); next audit pairwise tree travel, backtracking, and net displacement |
| [`lonely-runner/`](lonely-runner/) | active pivot after Phase 15A | level-3 structural discovery in exact bounded K4/K5 settings; `LRC(13)` remains open | [global closure audit](lonely-runner/40-global-closure-contract-and-theory-audit.md); next develop lift-aware initial search on solved cases, then freeze before K13 |
| [`hidden-am-noether/`](hidden-am-noether/) | static branch closed negatively | a frozen observer in the same product-affine group cannot reveal a missing stabilizer dimension | [static-observer no-go](hidden-am-noether/03-static-observer-no-go-and-schedule-split.md); continuation moved to `moving-am-observer/` |
| [`moving-am-observer/`](moving-am-observer/) | affine deterministic phase closed | bounded blind observer discovery, task-equivalent minimum slice, and dimensionful Bellman covariance on the declared family | [study ledger](moving-am-observer/README.md); stochastic continuation moved to its own Sonnet |
| [`stochastic-feedback-trap-first-passage/`](stochastic-feedback-trap-first-passage/) | current calibration closed | exact Itô task quotient plus independent first-passage and reset-Bellman covariance across 242 monotone charts | [Phase-4 results](stochastic-feedback-trap-first-passage/09-phase4-reset-bellman-results.md); further work requires a new Sonnet or governed extraction proposal |
| [`pcr3bp-history-cost/`](pcr3bp-history-cost/) | Phases 0–1 complete; Phase 2 frozen | lifted topology and scale-jet reconstruction separate word, clock, deck, and hyperbolic costs; no Bellman/Huffman source is yet justified | [Phase-2 contract](pcr3bp-history-cost/02-return-partition-holonomy-contract.md); next run the frozen two-gate covariance and convergence gates |
| [`s6-complex-arithmetic-tower/`](s6-complex-arithmetic-tower/) | T0 initialization | auditable two-question research contract only; neither the manuscript nor an arithmetic interface is verified | [problem frontier](s6-complex-arithmetic-tower/00-problem-frontier.md); next archive/checksum the source and reproduce its matrix/topology certificate |

## Sonnet 001 — Lonely Runner

The founding numbered study is [`lonely-runner/`](lonely-runner/), targeting the next open fixed-dimensional case `LRC(13)` (14 total runners).

The literature audit sharpens the reason for choosing it. The 2026 computer-assisted proof through `LRC(12)` explicitly identifies the primary obstacle to `k=13` as efficient computation of the initial improper set `I(k,p,1)`, with stronger pruning of no-witness residue tuples as the needed direction.

The study now contains two exact research lines:

```text
modular proof line
    I(k,p,1) set cover -> future requirements -> exact two-slot prune
    -> pinned upstream K=8..12 transfer -> three K=13,p=199 workers

continuous representation line
    canonical torus contact process -> generated pair-ratio grammar
    -> task-relative compilation -> lazy DAG -> Clean / obstruction
```

The modular line found an exact two-slot transversal certificate that preserves
complete canonical outputs and yields net speedups on the pinned upstream solver.
The continuous line subsequently developed exact K4/K5 bounded-domain models of
canonicalization, task quotienting, selective materialization, and grammar-relative
clean separability.

These lines have not yet rejoined.  In particular, the K4/K5 contact results do
not currently induce a new prune or lift certificate for `I(13,p,1)`.  The global
closure audit also shows that the current upstream K13 prime manifest, even if
fully certified, would not meet the final finite-product threshold.

The authoritative current audit is
[`lonely-runner/40-global-closure-contract-and-theory-audit.md`](lonely-runner/40-global-closure-contract-and-theory-audit.md).
Sonnet 001 has reached level 3 **structural discovery** in several exact bounded
settings, but not level 4: `LRC(13)` remains open and no public API promotion is
proposed.

## Research-local calibration — the \(S^6\) complex structure claim

[`s6-complex-arithmetic-tower/`](s6-complex-arithmetic-tower/) studies a
new author-hosted construction of a compact complex threefold diffeomorphic to
\(S^6\) under two independent questions:

1. whether the construction provides a lossless external calibration of
   history lift, task-visible holonomy, canonicalization, and singular
   completion in Process Geometry;
2. whether the complex Addition/Multiplication/Power closure has a
   task-sufficient finite integral shadow strictly comparable with the
   construction's rank-four monodromy representation.

The study begins at source-verification and research-contract level.  It does
not treat the manuscript as independently verified, does not claim an
arithmetic origin for \(S^6\), and proposes no API extraction.

## Research-local calibration — local-field projective process geometry

[`local-field-projective-process-geometry/`](local-field-projective-process-geometry/)
starts from the bilateral AEG history language rather than importing a local-
field solver ontology. Its Phase 0 executable certificates show that one
rational Multiplication history has opposite Archimedean and \(p\)-adic scale
behavior; residue observations form nested exact quotients; Addition,
Multiplication, and Möbius histories transport the valuation ruler by explicit
laws; and finite right-reciprocal histories lower to continued-fraction matrix
products.

The first red team compares standard and balanced digit sections. Both
reconstruct the same finite residue, while different declared cost rulers
prefer different histories. The result supports task-relative
canonicalization but rejects an observer-free preferred digit system.
Phase 1 then constructs the complete finite standard-root Bruhat--Tits ball
from normalized lattice kernels. It proves that the earlier residue tower is
exactly the affine contact chart, not the whole sphere, and that right
inversion forces the missing infinity chart.

Phase 2 supplies the deliberately separate real positive control. Canonical
regular continued fractions compile exactly into convergent matrices,
Stern--Brocot left/right runs, Farey frames, and ordered real cylinders. The
terminal split \([1;2]=[1;1,1]\) reaches the same rational endpoint and the
same canonical tree path but retains different previous convergents,
one-sided cylinders, and future continuation under an appended suffix. This
rejects endpoint-only state and separates digit cost from materialized-turn
cost. It does not identify the ordered Farey/Stern--Brocot tree with the
residue-branching Bruhat--Tits tree. The infinite \(p\)-adic boundary and a
comparison of competing \(p\)-adic continued-fraction algorithms remain
unselected, and no API extraction is proposed.

Phase 3 performs that comparison without pretending that the algorithm name
defines the task. Ruban's standard section and Browkin I's balanced section
choose different rational lifts of the same finite projective contact. Exact
reciprocal continuation then separates them: \(-1\) terminates under Browkin
but enters a Ruban fixed complete quotient, whereas at \(p=5\) the positive
integer \(3\) has a shorter and cheaper Ruban history. Both lower through the
same projective matrices, and every tested prefix is certified in the finite
lattice-ball oracle. The result rejects a task-free selector while leaving
general convergence, periodicity, and infinite completion open.
