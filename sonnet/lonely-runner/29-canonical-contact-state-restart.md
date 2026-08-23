# Phase 11A — restart Sonnet 001 from the canonical contact state

**Status:** active reconstruction after the C1–C4 canonicalization closure.  
**Branch:** `research/sonnet001-canonical-contact-state`.  
**Open-frontier policy:** `K=13` remains frozen.  
**Executable red team:** `tests/research/test_lonely_runner_canonical_contact_state.py`.

## 1. Why Sonnet 001 must now be reordered

The earlier Sonnet sequence learned a great deal from the finite pair-difference / wall presentation:

```text
A/M contact calculus
-> pair-difference sign geometry
-> task quotient
-> local completion pressure
-> minimum generated walls
-> task objectification
-> controlled interleaving / persistent Hauffman DAG
-> finite closure of the infinite contact tail.
```

Those results remain valid **relative to that chosen presentation**.  In particular, the center-2 -> center-3 and center-3 -> center-4 experiments correctly identified which old wall/task states split and what extra wall information was sufficient to separate them.

The C1–C4 canonicalization programme changes the causal order, however.  Its central methodological rule is

\[
\boxed{\text{canonicalize first; classify residuals second; complete representation last}.}
\]

Therefore the existing `6` and `7` completion states cannot be treated as evidence that the physical/contact process intrinsically requires those new coordinates.  They show only that the **finite static wall carrier** requires them.

The restart question is consequently:

> Which coordinates in the lifted contact-center description are physical/task state, and which are only representation lift or certificate provenance?

The first answer is unexpectedly strong: the contact-center index itself is a universal-cover sheet coordinate.

---

## 2. Raw process: the lifted contact train lives on a universal cover

For positive relative speeds `u_i`, write the lifted phase

\[
s_i(t)=t u_i\in\mathbb R.
\]

The physical runner phase is

\[
\phi_i(t)=s_i(t)\pmod 1\in \mathbb R/\mathbb Z.
\]

The usual lifted bad-interval boundaries are

\[
s_i=n\pm\delta,
\qquad n\in\mathbb Z,
\]

or, in time coordinates,

\[
\tau_{i,n,\pm}=\frac{n\pm\delta}{u_i}.
\]

The integer `n` is therefore a sheet coordinate of the lift

\[
\mathbb R\longrightarrow\mathbb R/\mathbb Z.
\]

The LRC observer itself depends on the torus phase, not on which integer lift represents that phase.  Deck transformations

\[
s_i\mapsto s_i+m_i,
\qquad m_i\in\mathbb Z,
\]

leave

\[
\phi_i=s_i\bmod 1
\]

unchanged.

This distinction was hidden by the earlier center-depth programme because the static wall presentation precompiled progressively larger pieces of the universal cover.

---

## 3. First canonicalization: quotient the deck lift before wall completion

Choose the fundamental-domain representative

\[
\boxed{\phi_i=s_i\bmod1\in[0,1).}
\]

For the exact first-witness process the canonical dynamic carrier is then

\[
\boxed{(\mathbf u,\boldsymbol\phi)}
\]

modulo the already-known global M-scale freedom.  Absolute elapsed time may be accumulated as certificate provenance, but it is not needed to decide the next contact event.

For one runner define the phase distance to the next contact by

\[
d(\phi)=
\begin{cases}
\delta-\phi, & 0\le \phi<\delta,\\
1-\delta-\phi, & \delta\le\phi<1-\delta,\\
1+\delta-\phi, & 1-\delta\le\phi<1.
\end{cases}
\]

The corresponding event kinds are respectively

```text
exit, enter, exit-after-wrap.
```

For several runners,

\[
\boxed{
\Delta t=\min_i \frac{d(\phi_i)}{u_i},
\qquad
\phi_i'=(\phi_i+u_i\Delta t)\bmod1.
}
\]

Ties give simultaneous contact strata.  At a contact boundary equality is safe, exactly as in the previous `before / on / after` semantics.

Crucially, this event map contains **no contact center `n` and no maximum center horizon**.  The same finite local rule crosses center 2, 3, 4, or arbitrarily later sheets.

---

## 4. Contact center becomes decoder/provenance, not process state

If an old lifted certificate is desired, the integer center can be reconstructed from accumulated time after the event has occurred:

\[
\begin{aligned}
\text{exit:}\quad n &= t u_i-\delta,\\
\text{enter:}\quad n &= t u_i+\delta.
\end{aligned}
\]

At an exact contact these quantities are integers by construction.

Thus there are now two distinct objects that the old presentation combined:

```text
canonical task dynamics     (u, phi mod 1)
certificate provenance      elapsed t + decoded lift sheet n
```

This is the same methodological distinction already exposed elsewhere in Sonnet 001:

\[
\text{solver / certificate trace}
\neq
\text{task-minimal representation ontology}.
\]

The new point is that the distinction appears **before** completion, at the level of the contact lift itself.

---

## 5. Immediate reinterpretation of the old center-3 / center-4 completions

In the static pair-difference carrier, adding a deeper contact layer introduces new collision ratios.  Some old sign cells then need a new wall coordinate, giving the previously verified

\[
843F_{\rm ren}\oplus0F_{\rm res}\oplus6F_{\rm comp}
\]

and later

\[
2746F_{\rm ren}\oplus0F_{\rm res}\oplus7F_{\rm comp}.
\]

Those decompositions remain correct **for that carrier**.

But the canonical torus event carrier does not enlarge when those same examples cross center 3 or center 4.  The phase update rule is unchanged.  Therefore the old completion pressure has a plausible new interpretation:

\[
\boxed{
\text{static compilation completion}
\quad\text{rather than necessarily}\quad
\text{process-state completion}.
}
\]

The executable red team includes the two previous horizon counterexamples:

```text
(2, 6, 9, 14)   -> witness uses a center-3 contact
(3, 9, 13, 23)  -> witness uses a center-4 contact
```

Both are recovered by the same center-free canonical event rule.  This does **not** yet prove that `F_comp=0` for every useful Sonnet task carrier, but it is enough to reject contact-center depth as an intrinsic state-growth axis.

This is exactly the representation relativity highlighted by the C4 Kepler calibration: a residual that forces completion in one carrier can be absorbed by a better carrier.

---

## 6. Second canonicalization already present implicitly: global M scale

The contact task is invariant under

\[
\mathbf u\mapsto c\mathbf u,
\qquad
t\mapsto t/c,
\qquad c>0.
\]

The canonical phase/event sequence is unchanged; only reconstructed physical time rescales.

The executable calibration verifies this directly.  In logarithmic speed coordinates

\[
x_i=\log u_i,
\]

this is the translation gauge

\[
x_i\mapsto x_i+a.
\]

After quotienting it, the natural local coordinates are the adjacent gaps

\[
q_a=x_{a+1}-x_a,
\]

so every pair difference is a positive-root sum

\[
x_j-x_i=q_i+\cdots+q_{j-1}.
\]

For four ordered speeds the six pair-edge coordinates are therefore an overcomplete lift of only three independent relative M coordinates.  The old exact cycle closure was already enforcing this compatibility indirectly.

This suggests a second reconstruction step: derive wall comparisons from a canonical `A_{k-1}` simple-root carrier rather than treating the complete gain graph as primitive.  That step is not yet implemented in Phase 11A because the deck quotient is the more consequential correction.

---

## 7. What happens to Hauffman geometry

Hauffman is not discarded.  Its position changes.

The old order effectively became

```text
choose finite wall language
-> complete wall language as contact depth grows
-> optimize history placement / Hauffman DAG.
```

The new order should be

```text
canonical torus process state
-> exact center-free event evolution
-> task-relative quotient / objectification
-> choose what part of the canonical dynamics should be compiled
-> Hauffman / persistent DAG placement downstream.
```

This makes the existing 29-wall center-4 representation easier to interpret: it is a successful **compiled finite sufficient statistic** for the declared four-runner first-witness task, not necessarily the ontology from which the process should be derived.

The infinite-tail closure remains valuable.  It says that one particular static compilation eventually stops growing.  Phase 11 asks a different question: whether starting from the canonical dynamic state gives a cheaper or more transferable compilation path in the first place.

---

## 8. The main red team: canonicalization may move cost rather than remove it

The torus carrier is not automatically better.

It removes an artificial sheet/contact-center axis, but it replaces a finite precompiled wall lookup by exact event evolution on a continuous/rational phase state.  Therefore the relevant comparison is not state count alone.

We must compare at least

\[
\boxed{
(
\text{state description cost},
\text{event arithmetic cost},
\text{expected event depth},
\text{worst event depth},
\text{compiled decision depth},
\text{incremental refinement cost},
\text{certificate reconstruction cost}
).
}
\]

This is precisely where the previous Hauffman space-time viewpoint remains essential.  Canonicalization removes representation freedom first; Hauffman then decides how aggressively to materialize / compile the resulting process.

---

## 9. Executable Phase 11A evidence

`tests/research/test_lonely_runner_canonical_contact_state.py` currently checks five things:

1. **deck invariance** — integer lift shifts have the same fundamental-domain phase;
2. **point witness preservation** — the `(1,2)`, `delta=1/3`, `t=1/3` simultaneous-contact red team is preserved exactly;
3. **old horizon failures** — the speed-14 center-3 and speed-23 center-4 examples are reached without a center horizon in the canonical transition rule;
4. **independent lifted-oracle agreement** — all `C(9,4)=126` four-speed tuples from `1..9` agree exactly in event rank, decoded lifted boundary, point/interval mode, and witness time;
5. **global M-scale invariance** — multiplying all speeds by a common factor preserves the canonical event/certificate sequence and rescales only physical time.

The lifted center indices are used only by the red-team decoder.  They never enter the canonical transition.

---

## 10. ObserverConnection judgment: do not overclaim

The map

\[
\phi=s\bmod1
\]

is a quotient by a discrete deck group and the event evolution is piecewise/hybrid.  It is **not** the same mathematical object as the smooth observer ODE calibrated in C1–C4.

Therefore Phase 11A should not reverse the previous API caution by simply renaming deck resets `ObserverConnection`.

A genuine Sonnet observer/connection claim would require an actual moving canonical frame—for example, a locally derived event-adapted chart whose transition law is forced by a normalization and whose reconstruction preserves the task.  That is a later experiment.

For now the supported statement is narrower:

\[
\boxed{
\text{canonical quotient before completion changes the Sonnet decomposition problem.}
}
\]

---

## 11. Revised Sonnet 001 programme

The research dependency graph should now be

```text
Phase 11A  universal-cover/deck audit
    -> canonical torus contact state
    -> exact event-map red team against old lifted semantics

Phase 11B  representation audit
    -> quotient global M scale explicitly
    -> test simple-root / adjacent-ratio carrier
    -> identify remaining genuine representation freedom

Phase 11C  canonical task objectification
    -> quotient canonical event states by future first-witness semantics
    -> determine what finite predicates/primitives are actually worth materializing

Phase 11D  compilation comparison
    -> compile canonical dynamics into decision DAGs
    -> compare against frozen 21/26/29-wall presentations
    -> measure full space-time Pareto geometry

Phase 11E  decomposition after canonicalization
    -> only now recompute F_ren / F_res / F_comp
    -> ask whether any genuine completion residual remains

Phase 11F  observer-connection red team
    -> only if an actually moving locally normalized chart emerges

then, and only then,
    -> reconsider transfer toward larger runner dimension / K=13.
```

`K=13` stays frozen throughout this reconstruction.

---

## 12. Current interpretation

The most important conceptual change is this:

> Sonnet 001 was previously learning how to grow and compress a finite presentation of an open-ended lifted history.  After the canonicalization closure, the first question is whether part of that apparent growth came from representing the same torus process on more and more sheets of its universal cover.

Phase 11A gives a concrete positive answer for the contact-center coordinate: the physical first-witness dynamics can be evolved by a fixed local torus rule, while the center index can be reconstructed afterward as certificate provenance.

If the later cost red team also succeeds, the old hierarchy

\[
\text{center depth}\to\text{new walls}\to\text{completion}\to\text{Hauffman}
\]

should be replaced by

\[
\boxed{
\text{canonical process}
\to
\text{task quotient}
\to
\text{selective compilation}
\to
\text{Hauffman history geometry}.
}
\]

That would be a substantially different reading of Sonnet 001, not a small optimization of the existing Phase 8–10 machinery.

## Claim boundary

No new Lonely Runner case is proved here.  The current executable evidence is a bounded exact semantic calibration plus two previously known calculus-horizon counterexamples.  The claim is about representation order: contact-center sheet growth is not required by the canonical torus process state, and therefore old wall completion must be re-evaluated only after this quotient is applied.
