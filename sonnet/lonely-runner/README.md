# Lonely Runner — Sonnet 001

**Status:** Phase 0 — audited frontier, exact oracles, baseline reconstruction.  
**Target open case:** `LRC(13)`, i.e. **14 runners**.

## 1. Statement and notation

Following the convention used by Sungkawichai–Trakulthongchai, `LRC(k)` asks whether every positive integer speed tuple

\[
\mathbf u=(u_1,\ldots,u_k)
\]

has a witness time \(t\in\mathbb R\) satisfying

\[
\|t u_i\|\ge \frac1{k+1}\qquad(i=1,\ldots,k),
\]

where \(\|x\|\) denotes distance to the nearest integer.  In this notation `LRC(k)` is the Lonely Runner Conjecture for `k+1` total runners after passing to speeds relative to one runner.

The current published/preprint computational frontier is

\[
\boxed{LRC(k)\text{ holds for }k\le 12.}
\]

Thus the next fixed-dimensional open case is

\[
\boxed{LRC(13)\quad\text{(14 runners)}.}
\]

## 2. Why this belongs in `sonnet/`

This problem already contains an explicit representation bottleneck rather than merely a large numerical workload.

The 2026 proof strategy converts the global conjecture into finite modular verification.  For a prime \(p\) and lifting denominator \(l\), one studies the set \(I(k,p,l)\) of speed tuples that are *improper*: they have neither the relevant gcd certificate nor a witness in the rational time grid \(\frac1{lp}\mathbb Z\).  Lifting and backward projection then progressively shrink supersets of the genuinely difficult residue classes.

The implementation also quotients speed tuples by three exact symmetries modulo \(p\):

1. coordinate permutation;
2. independent sign flips;
3. multiplication by a unit in \(\mathbb Z_p^\times\).

This reduces the initial search from roughly \(p^k\) tuples to about

\[
\binom{p/2}{k-1}\approx\frac{p^k}{2^k(k-1)!}.
\]

But the authors explicitly identify the next barrier:

> for `k = 13`, the primary bottleneck is the efficient computation of `I(k,p,1)`; progress likely requires a better understanding of speed tuples without an ansatz witness, yielding stronger pruning conditions.

That is almost exactly a Shakespeare question:

\[
\boxed{
\text{Can the initial modular search be replaced by a cheaper task-sufficient presentation?}
}
\]

The goal is **not** to rename the existing sieve.  The goal is to discover additional exact quotients, signatures, relations, or morphisms that preserve the only semantics that matter: whether a residue class can still contain a non-eventually-proper tuple after allowed refinements.

## 3. Phase 0 contract

Phase 0 deliberately stops before attacking `k=13` at scale.

It establishes four things:

1. **exact continuous oracle** for small integer speed tuples, using rational arithmetic only;
2. **exact ansatz-grid oracle** matching the finite witness semantics used by the current computational proof;
3. **symmetry reconstruction** for the known modulo-\(p\) quotient;
4. **red-team calibration** on the tight tuple \((1,2,\ldots,k)\), which passes exactly at \(1/(k+1)\) and fails under any strengthened threshold.

The executable Phase 0 calibration lives in:

```text
tests/research/test_lonely_runner_phase0.py
```

The mathematical and literature audit lives in:

```text
sonnet/lonely-runner/00-problem-frontier.md
```

## 4. Shakespeare research hypothesis

Let a modular search state encode partial information about a candidate speed tuple.  A future refinement may consist of a larger denominator, a lift, a projection, or another admissible sieve step.  Two states should be merged only if no allowed future refinement can distinguish them with respect to the target predicate

```text
can this state still contain a non-eventually-proper tuple?
```

This suggests a task-relative congruence analogous in spirit to the existing bounded future signatures:

\[
h_1\sim_{\mathrm{LRC}} h_2
\iff
Q(h_1c)=Q(h_2c)
\quad\text{for all allowed continuations }c,
\]

where \(Q\) is the LRC survival/properness semantics.

The first serious discovery experiment will therefore search for **coarser-than-labelled but certificate-preserving states** on already solved values of \(k\), before attempting `k=13`.

## 5. Success ladder

We will keep four claim levels separate:

1. **re-expression:** reproduce the known ansatz/lifting argument;
2. **compression:** reduce state count or runtime under identical exact semantics;
3. **structural discovery:** discover a new exact pruning signature or presentation quotient;
4. **new mathematics:** use the discovered structure to prove `LRC(13)` or another previously open statement.

Only level 4 is a solution of the open problem.

## 6. Immediate next phases

### Phase 0 — exact ground truth

- finish and test exact small-instance oracles;
- reproduce the known symmetry quotient;
- encode the paper's `(k,p,l)` proper/improper predicate exactly.

### Phase 1 — baseline reconstruction

- reproduce `I(k,p,1)` for small solved `k,p` pairs;
- record tuple counts before and after each known quotient/pruning rule;
- compare with the upstream `find_cover` implementation.

### Phase 2 — representation search

- define candidate state signatures from residue occupancy, pair differences, arc-cover profiles, witness-deficit patterns, and bounded refinement behavior;
- merge only with exact task certificates;
- measure Pareto tradeoffs among state count, branching, certificate cost, and decoder/reconstruction cost.

### Phase 3 — transfer

- train nothing and assume nothing from `k=13` initially;
- freeze the best quotient on solved cases;
- then apply the same representation grammar and budgets to `LRC(13)`.

## Claim boundary

Nothing in this directory currently proves `LRC(13)`, improves the best published finite-checking bound, or establishes that Shakespeare will outperform the current C++ implementation.  Phase 0 only creates an auditable bridge from the accepted problem formulation to Shakespeare's representation-search machinery.
