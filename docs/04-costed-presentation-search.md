# Costed presentation search

**Status:** first reusable search loop; proposal generation is still external.

## 1. Why a search layer is separate

Shakespeare now has several reusable mechanisms that answer different questions:

- literal ordered history and exact rewriting;
- bounded task-sufficient future signatures;
- finite history geometry and prefix-depth strategies;
- generated symbolic grammar closure;
- template-free process-relation discovery and factorization.

None of those mechanisms should silently decide that one representation is globally "best".  Different tasks may trade grammar width against history depth, decoder size, or relation complexity differently.

The search layer therefore consumes explicit multi-axis `PresentationCost` values and returns Pareto candidates by default.

## 2. Generic candidates

`PresentationCandidate[payload]` attaches three things to an arbitrary representation payload:

1. a multi-axis `PresentationCost`;
2. an explicit task-sufficiency flag;
3. an optional certificate.

`pareto_frontier` rejects task-insufficient candidates by default and removes any candidate dominated on every cost axis by another admissible candidate.

No universal scalarization is imposed.

## 3. First symbolic adapter: exact reconstruction

The first concrete adapter treats exact decoding of declared target expressions as the task.

For each caller-proposed seed grammar:

1. `discover_generated_presentation` grows the process span from the seeds;
2. failure to close remains an explicit incomplete presentation;
3. if closure succeeds, process relations and relation factors are discovered;
4. each target must be exactly decomposable in the discovered primitive grammar;
5. a transparent structural baseline cost is computed;
6. all sufficient candidates are Pareto-filtered.

The baseline cost uses five already-public axes:

\[
C=(C_{grammar},C_{relations},C_{history},C_{decoder},C_{task}).
\]

The default structural proxy is deliberately simple:

- grammar cost counts symbolic construction size of proposed seeds and returned primitives;
- relation cost counts nonzero coefficients in discovered global/component relations;
- history cost sums the process depths at which independent grammar directions first appear;
- decoder cost counts nonzero target-coordinate coefficients;
- task error is zero for exact reconstruction and infinity otherwise.

Callers may replace this model entirely.

## 4. A useful trade-off appears immediately

A recurrent two-assignment calibration can be represented from one seed or from two seeds.

With one seed, the initial grammar dictionary is narrower, but the second independent process direction must be discovered at depth one.  With two seeds, grammar description is wider but process-discovery depth is lower.

Neither candidate dominates the other.  A third proposal containing a redundant composite seed is dominated and disappears from the Pareto frontier.

This is the intended behavior: Shakespeare should expose representation trade-offs instead of hiding them in one hand-chosen score.

## 5. Current boundary

The current search routine evaluates **caller-proposed** seed sets.  It does not yet generate candidate primitives from allowed arithmetic/process operations.

That separation is intentional for this checkpoint.  The next research problem is proposal generation with explicit construction histories, because collapsing equal symbolic expressions too early would lose exactly the process information Shakespeare is designed to preserve.

A future proposal engine should therefore return both:

- the candidate object/expression;
- a construction-history certificate and its cost.

Those proposals can then flow through the search API introduced here without changing the task-sufficiency or Pareto machinery.
