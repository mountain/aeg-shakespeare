# Phase 13B — the first new causal boundary still admits zero-completion separation

**Status:** exact five-speed critical-boundary probe passed.  
**Adapter:** `sonnet/lonely-runner/python/five_speed_clean_certificate.py`.  
**Executable calibration:** `tests/research/test_lonely_runner_five_speed_clean_certificate.py`.  
**Scope:** five ordered relative speeds, `delta=1/6`; `K=13` remains frozen.

## 1. Do not widen the domain by arbitrary increments

Phase 12 established clean-separator recursion through

\[
\frac{u_5}{u_1}<\frac{25}{4}=6.25.
\]

The next question is where the canonical contact process itself acquires a genuinely new possible event ordering.

Contact coefficients have the exact form

\[
\alpha=n\pm\frac16.
\]

The first outer-runner equality ratio strictly above `25/4`, including the next contact layer, is

\[
\boxed{
R_*=
\frac{8-\frac16}{1+\frac16}
=
\frac{47/6}{7/6}
=
\frac{47}{7}.
}
\]

At this value the fastest runner's center-8 enter can tie the slowest runner's center-1 exit.

So Phase 13B probes the open domain

\[
\boxed{
\frac{u_5}{u_1}<\frac{48}{7}
}
\]

just beyond the first native causal threshold rather than choosing an arbitrary decimal width.

---

## 2. Independent recertification of the Phase-12 endpoint

Before crossing the threshold, translate the exact terminal closures at

\[
R<25/4
\]

into the generic Phase-13 partial-sign system and run the new exact recursive criterion instead of reusing the Phase-12 greedy constructor.

The result is clean:

```text
symbolic states          14,773
terminal regions          5,379
generated coordinates       111
canonical tasks               48
minimum coordinates           46
clean tree nodes             349
clean max depth               15
root                      u5/u1 ? 5
max event / center          47 / 7
```

Thus the generic criterion independently recovers the Phase-12 zero-completion conclusion at the widest frozen baseline.

---

## 3. Crossing 47/7 produces new dynamics

At

\[
R<48/7
\]

the horizon-free symbolic process grows to

```text
symbolic states          16,747
terminal regions          6,203
generated coordinates       111
canonical tasks               50
minimum coordinates           48
max event index               49
maximum contact center         8
```

The important change is not merely a larger census.  The previous emergent contact ceiling

\[
7
\]

has genuinely moved to

\[
\boxed{8}.
\]

So the probe has crossed a real causal boundary of the canonical process rather than staying within one stable combinatorial chamber.

---

## 4. Yet the exact clean criterion still passes

Despite the new center-8 histories, the generic exact recursion returns

```text
pairwise task separable      yes
clean separable              yes
clean states visited         745
clean tree nodes             745
clean max depth               16
completion obstruction       none
```

No current exact region needs to be split by an unresolved coordinate.

Therefore

\[
\boxed{
\text{new causal layer}
\not\Rightarrow
\text{representation completion}.
}

This is now established after both:

1. process canonicalization; and
2. task/certificate objectification.

It is a stronger negative result than the old observation that a particular deeper contact center happened not to affect the task.

---

## 5. A subtle tree change should not be overinterpreted

Under the deterministic candidate ordering of the generic exact solver, the returned root changes from

\[
\frac{u_5}{u_1}\ ?\ 5
\]

at `25/4` to

\[
\frac{u_4}{u_1}\ ?\ 5
\]

at `48/7`.

This shows that the clean decision geometry has changed, but the selected root is not currently proved unique or optimal.  It should therefore be treated as a property of the returned witness tree, not yet as a new intrinsic phase boundary.

The invariant result is the existence of a verified clean tree and the absence of a completion obstruction.

---

## 6. What clean obstruction is actually measuring

The generic red teams reveal the right geometric interpretation.

Each canonical terminal region has a **partial** sign vector.  A coordinate cut is clean on a family precisely when it does not cut through any region in that family.

Thus clean-separability asks whether the task partition can be realized by a recursive hierarchy of coordinate cuts that are compatible with the existing region partition.

This is stronger than ordinary pairwise separability.

The three-region red team from Phase 13A can be read as an `argmin` pattern:

- every pair of possible minima can be distinguished by one pairwise comparison;
- when the third event is minimum, that comparison is irrelevant and can remain unresolved;
- consequently no single pairwise comparison is defined on all three task regions.

A conventional comparison algorithm can still classify the argmin by asking a pairwise question and thereby splitting the third region unnecessarily.  A **clean** decision program forbids that over-refinement.

So a future obstruction means:

> the current task partition is not recursively compatible with the current primitive coordinate cuts without manufacturing distinctions inside an already exact canonical task region.

This is a much more precise meaning of representation-completion pressure.

---

## 7. Two possible repairs when obstruction eventually occurs

When `Clean(S)` first fails, there are conceptually different responses.

### A. Region completion

Choose an unresolved existing coordinate and split one or more current regions by its feasible signs.

This enlarges the representation by making a previously latent distinction explicit.

### B. Primitive objectification

Introduce a compound process primitive whose value is already constant on the obstructed canonical regions but separates their task roles directly.

For an argmin-style obstruction, this could be a multiway `which event is minimal?` primitive rather than a sequence of pairwise comparisons that cuts irrelevant regions.

These two repairs should not be conflated.  One refines the region geometry; the other changes the predicate grammar.

This suggests the next version of the Minimal Process Completion principle:

\[
\boxed{
\text{when clean separation fails, compare minimum region refinement}
\quad\text{against}\quad
\text{minimum compound primitive objectification}.
}
\]

---

## 8. Why the full generated grammar may behave differently from the minimum basis

The current Phase-13 probe tests the **globally cardinality-minimum task coordinate basis**.

That is intentionally stringent.  A richer process-generated coordinate set may admit a clean tree even when a minimum task-separating subset does not.

Therefore future failure should be classified at two levels:

```text
minimum task basis not clean
    -> content minimization conflicts with zero-refinement placement

full generated process grammar not clean
    -> even all currently generated primitive cuts cannot avoid region refinement
```

Only the second is strong evidence for genuinely missing primitive geometry.  The first may be repaired simply by adding back a globally redundant but placement-useful coordinate.

This distinction mirrors the earlier difference between the 29-predicate persistent carrier and the 27-predicate global minimum at four speeds.

---

## 9. Next gate

The next critical outer ratio after `47/7` is `7`.  But the better Phase-13C experiment is now two-dimensional:

1. continue across exact process-generated critical ratios;
2. at every probe test clean-separability both for
   - the exact minimum task basis, and
   - the full process-generated coordinate grammar.

The first point where the minimum basis fails but the full grammar succeeds identifies a **basis-completion** transition.

The first point where even the full grammar fails identifies a stronger **region/primitive-completion** transition.

At either failure, preserve the recursive `CleanObstruction` certificate rather than only a scalar count.

`K=13` remains frozen.

## Claim boundary

No new Lonely Runner theorem is proved.  The `16,747 / 6,203 / 50 / 48`, center-8, and 745-node clean-certificate results are exact bounded representation statements for the declared domain `u5/u1 < 48/7`.  The returned tree is a valid clean witness but is not claimed globally optimal or root-unique.