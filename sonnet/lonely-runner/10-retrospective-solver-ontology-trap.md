# Retrospective — why Sonnet 001 initially missed the strongest Shakespeare language

## Summary

The Lonely Runner problem was a good Sonnet choice.  The first research line was also scientifically useful: it found a new exact future-requirement/transversal certificate and transferred it into real open-case search branches.

But the route exposed a framework/agent failure:

> the research agent inherited the ontology of the mature upstream solver before auditing the problem in Shakespeare's strongest native languages.

As a result, the first successful representation was expressed as bitset cover -> future requirement -> antichain -> transversal, while the more primitive A/M structure `C_s=s^{-1}B` was left unused.

This note treats that as a process failure to fix, not as a reason to discard the earlier result.

## 1. What went right

The problem selection had the properties a Sonnet needs:

- independently recognized open frontier;
- exact finite semantics;
- an identified computational bottleneck;
- a credible upstream baseline;
- abundant symmetries and representation choices;
- solved instances suitable for training/holdout discipline.

The solver-first line then established a legitimate Level-3 result: a task-relative future representation produced a new exact pruning certificate and transferred across the theorem frontier without retuning.

So neither the problem selection nor the Shakespeare task-quotient idea failed.

## 2. What went wrong

The first decomposition was effectively

```text
upstream code
    -> identify state fields
    -> reinterpret I(k,p,1) as set cover
    -> search for a better future state
```

rather than

```text
mathematical statement
    -> identify primitive processes
    -> identify observer/contact geometry
    -> identify native Shakespeare language
    -> discover a presentation
    -> only then bridge to upstream
```

The first route made `covered`, `AvailableChoice`, MRV order, and sibling elimination psychologically primary.  Once that happened, the natural representation search was over refinements/quotients of those objects.

But those objects already erase the fact that every cover is generated from one primitive additive bad window by the multiplicative family:

\[
C_s=s^{-1}B.
\]

The agent optimized a derived combinatorial presentation before asking whether the derivation itself had thrown away the most useful structure.

## 3. Why an agent is likely to make this mistake

### 3.1 Executable code has strong salience

A mature solver supplies named types, control flow, counters, benchmarks, and exact outputs.  Those are easy anchors for an agent.  A process-geometric reconstruction requires an explicit ontology choice before there is code to imitate.

### 3.2 The repository documents capabilities more clearly than routing

Shakespeare already contains A/M calculus, finite process families/actions, history quotients, discovery, and Pareto search.  But knowing that these modules exist is not the same as having a rule saying:

> when a new problem visibly contains Addition/Multiplication actions, test that language before generic linear/combinatorial reductions.

The missing artifact was a *research-routing protocol*.

### 3.3 Baseline comparison can accidentally become baseline ontology

A Sonnet correctly requires a credible baseline.  But if the baseline is introduced too early, `compare against the baseline` can silently become `represent the problem as the baseline does`.

Those are different requirements.

### 3.4 Discovery APIs still have domain-shaped adapters

The generic candidate/Pareto machinery is reusable, but some proposal generators remain specialized toward symbolic/polynomial reconstruction.  When the native finite A/M task does not drop directly into a standard adapter, an agent has an incentive to move to a representation for which tooling already exists.

That is an API pressure signal: discovery should be easier to apply to a new task than abandoning the native language.

## 4. Corrective actions

### 4.1 `sonnet/AGENTS.md`

A scoped agent protocol now requires:

- problem-native primitive audit before solver ontology;
- arithmetic-first testing when A/M is intrinsic;
- discovery before hand-supplied clever invariants;
- staged native-language then unrestricted search;
- explicit bridge back to upstream;
- separation of research benchmarks from routine CI.

### 4.2 AM-first restart

Phase 7 restarts from finite A/M contact geometry and uses contact-task semantics as the oracle.  Known ratio coordinates are hidden calibration targets, not search inputs.

### 4.3 Two-gate representation search

The new protocol is:

```text
Gate A: strongest native language only
Gate B: unrestricted Shakespeare presentation search
```

This prevents a generic representation family from winning merely because its tooling is more mature.

### 4.4 Discovery API pressure

A future reusable adapter should support task-relative finite presentation search with roughly the contract

```text
primitive atoms / process families
constructor grammar
bounded generation
exact task-equivalence oracle
multi-axis presentation cost
Pareto frontier
```

without assuming polynomial targets or linear reconstruction.

Promotion to public API should wait until the same need is confirmed outside Lonely Runner.

## 5. General lesson

For Shakespeare, an existing solver should be treated as

\[
\boxed{\text{benchmark + evidence + implementation target}}
\]

not automatically as

\[
\boxed{\text{the mathematical ontology}}.
\]

The framework's comparative advantage is precisely the possibility that a hard problem is difficult in the presentation inherited by its best current solver.

Therefore the first research question for a Sonnet should be:

> **What is the strongest problem-native process language already available in Shakespeare, and what information is lost before the baseline solver begins?**

Only after answering that should the baseline's state representation become a candidate presentation.
