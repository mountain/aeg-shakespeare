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

## First candidate

The first candidate under consideration is the next open fixed-dimensional case of the **Lonely Runner Conjecture**. It is attractive because its known computational frontier already exhibits an explicit tradeoff between symmetry reduction, label reconstruction, CRT lifting, and combinatorial branching — exactly the kind of presentation problem Shakespeare is designed to make explicit.

The concrete formulation, literature status, baselines, and experiment design should live in its own subdirectory once frozen; this index deliberately does not commit to a particular attack before that work is audited.
