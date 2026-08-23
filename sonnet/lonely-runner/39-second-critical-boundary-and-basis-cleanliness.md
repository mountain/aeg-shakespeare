# Phase 13C — the minimum task basis remains clean across the second native threshold

**Status:** exact five-speed basis-versus-full probe passed.  
**Implementation:** `sonnet/lonely-runner/python/five_speed_basis_vs_full_probe.py`.  
**Executable calibration:** `tests/research/test_lonely_runner_five_speed_basis_vs_full_probe.py`.  
**Scope:** five ordered relative speeds, `delta=1/6`; `K=13` remains frozen.

## 1. Two different failure levels

Phase 13B established an exact clean tree just beyond the first new causal boundary `47/7`.

But a future failure of clean separation can mean two different things.

### Minimum-basis obstruction

The globally cardinality-minimum task coordinate basis is pairwise sufficient but cannot be arranged into a clean tree.

A richer subset of already generated process coordinates might restore clean placement without splitting any region.

This is **basis-completion pressure**: content minimization and zero-refinement placement are in tension.

### Full-grammar obstruction

Even the complete set of currently process-generated coordinates has no clean tree.

Then every classifier over the current primitive grammar must either refine a canonical region or introduce a richer compound primitive.

This is a stronger **primitive/region-completion pressure**.

Phase 13C begins separating these two notions experimentally.

---

## 2. The next native outer threshold is 7

After the first probe domain

\[
R<\frac{48}{7},
\]

the next raw contact equality ratio is

\[
\boxed{R_*=7.}
\]

This includes the comparison

\[
\frac{1+\frac16}{\frac16}=7,
\]

so it is again a process-generated event-order boundary rather than an arbitrary parameter increment.

Probe just above it at

\[
\boxed{R<\frac{36}{5}=7.2.}
\]

---

## 3. Exact process growth

The canonical symbolic process now contains

```text
symbolic states          20,031
terminal regions          8,247
generated coordinates       123
canonical tasks               55
minimum task coordinates      54
max witness event index       49
maximum contact center          8
```

Compared with the previous `48/7` probe:

```text
states       16,747 -> 20,031
regions       6,203 -> 8,247
tasks            50 -> 55
minimum walls    48 -> 54
```

So the domain has again acquired nontrivial new exact geometry and task distinctions.

---

## 4. The minimum basis itself is still clean

Run the exact Phase-13 clean-separability solver on the **54-coordinate cardinality-minimum task basis**.

Result:

```text
pairwise task separable      yes
minimum-basis clean          yes
clean tree nodes             802
clean max depth               17
completion obstruction       none
```

Because this clean witness uses only the minimum basis, the full 123-coordinate generated grammar is automatically clean by containment.  A second full-grammar search is unnecessary.

Thus the failure hierarchy remains

```text
minimum task basis      CLEAN
full generated grammar  CLEAN
```

through the second native threshold.

No basis-completion or primitive/region-completion transition has appeared yet.

---

## 5. Why this is more informative than another zero-refinement count

Phase 12B originally found one greedy zero-refinement tree.  Phase 13 now supplies three stronger ingredients:

1. an exact recursive existence criterion rather than one successful heuristic;
2. a recursive obstruction certificate for the negative case;
3. an explicit distinction between minimum-basis failure and full-grammar failure.

Therefore every new critical probe is no longer merely asking whether one constructor happens to work.  It classifies the representation layer at which a mathematically unavoidable obstruction first appears.

The two first critical crossings have both remained on the strongest side:

\[
\boxed{
\text{minimum cardinality task basis itself admits a clean tree}.}
\]

---

## 6. A useful geometric interpretation: compatibility, not just separability

The task partition is a partition of exact canonical regions.

Each primitive coordinate induces a ternary cut, but that cut may be undefined on some current regions because the region crosses the coordinate wall.

A clean decision tree requires every selected cut to be a union of whole regions at the moment it is used.

Thus the property being observed is a recursive compatibility between

\[
\text{canonical task partition}
\quad\text{and}\quad
\text{process-generated coordinate cuts}.
\]

This resembles a laminarity condition more than ordinary pointwise distinguishability: cuts may be individually useful but globally unusable if they slice through task-relevant region blocks at the wrong stage.

The Phase-13A three-region counterexample demonstrates exactly that failure mode.

---

## 7. Why blind frontier scanning should now stop

The next raw outer threshold after `7` is `37/5`, and one could continue probing indefinitely.

But two genuine causal crossings have already shown the same qualitative phenomenon while the exact theory now tells us what must fail.

The higher-value question is therefore no longer

> at which arbitrary numerical width does the first obstruction happen?

but

> what structural property of the canonical first-witness regions makes the minimum task basis recursively compatible with whole-region coordinate cuts?

A proof or counterexample mechanism for that property would tell us whether clean separation should persist far beyond the tested domains and what kind of process motif can destroy it.

---

## 8. Next theory target

The emerging candidate is a **task-compatible partial-sign hierarchy**.

Given a family `S` of canonical regions, define its currently total coordinates

\[
A(S)=\{c:\sigma_R(c)\ne\bot\text{ for every }R\in S\}.
\]

Clean-separability requires a coordinate

\[
c\in A(S)
\]

whose sign partition reduces task ambiguity and recursively preserves the same property.

The next research step should inspect how the canonical event compiler generates the partial-sign domains `A(S)` and ask whether first-witness causality imposes a structural ordering on them.

Two possibilities are especially important:

1. **positive theorem direction:** a causal-prefix / first-witness property guarantees a clean coordinate at every mixed-task family produced by the canonical compiler;
2. **minimal counterexample direction:** identify the smallest contact interleaving motif whose task quotient has the three-way `argmin` obstruction pattern from Phase 13A.

Either outcome would be more valuable than another raw census.

## Claim boundary

No new Lonely Runner theorem is proved.  The `20,031 / 8,247 / 55 / 54` and 802-node clean-tree results are exact bounded representation statements for `u5/u1 < 36/5`.  Clean-separability is proved only for the finite task systems explicitly constructed here; no arbitrary-domain theorem is claimed.