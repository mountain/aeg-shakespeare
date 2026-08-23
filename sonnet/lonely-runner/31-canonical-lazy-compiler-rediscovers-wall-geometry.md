# Phase 11B1 — canonical lazy compiler rediscovers the global wall geometry

> **Phase-15A certificate correction.**  A unique forced separator between two
> partial terminal regions is not a valid general proof of coordinate
> minimality.  The 27-coordinate numerical conclusion survives a stronger
> check: all 4,343 feasible cells of the complete 33-coordinate sign grammar are
> materialized, the selected projection is task-pure, and every selected
> coordinate has a full-sign deletion witness.  See
> [`40-global-closure-contract-and-theory-audit.md`](40-global-closure-contract-and-theory-audit.md).

**Status:** exact bounded symbolic calibration passed.  
**Implementation:** `sonnet/lonely-runner/python/canonical_lazy_contact_compiler.py`.  
**Executable red team:** `tests/research/test_lonely_runner_canonical_lazy_contact_compiler.py`.  
**Scope:** ordered four-speed domain, `delta=1/5`, `u4/u1 < 8`; `K=13` remains frozen.

## 1. Question

Phase 11A shows that the exact contact process can evolve on the canonical torus carrier

\[
(\mathbf u,\boldsymbol\phi),
\qquad
\phi_i=t u_i\bmod1,
\]

without treating the universal-cover contact center as process state.

Phase 11B0 also shows that canonical event evolution is not itself the cheapest execution program: on the old 55-input usage world it pays total event depth `280`, while the frozen static wall compilation pays `135`.

The missing mechanism is therefore:

> Can the useful static pair-ratio predicates be generated *from* canonical dynamics, rather than supplied through a center-2/3/4 contact hierarchy?

## 2. Horizon-free lazy symbolic compiler

The compiler receives only:

- the canonical next-contact process law;
- exact multiplicative difference-constraint closure;
- ordered positive relative speeds;
- `delta=1/5` and `u4/u1<8`;
- the first-witness observer.

It receives no `max_center`, no `contact_ratios(m)`, no old 21/26/29-wall target, no `19/11` hint, and no Hauffman tree.

For each runner it keeps only the next lifted contact coefficient `alpha_i` as **compiler provenance**.  When two next events can exchange order,

\[
\frac{\alpha_i}{u_i}
=
\frac{\alpha_j}{u_j},
\]

the equality locus is generated automatically as

\[
\boxed{
\frac{u_j}{u_i}=\frac{\alpha_j}{\alpha_i}.
}
\]

Thus pair-ratio walls are derived equality loci of the canonical process, not a primitive alphabet.

At each symbolic region the compiler branches only on the exact set of runners attaining the next minimum contact time.  Equality is imposed inside that set and strict precedence over nonminimal runners; ordering among nonminimal events is left unresolved.  These branches are disjoint and exhaustive.

## 3. Exact closure result

The complete symbolic expansion terminates with:

```text
symbolic nonterminal states     388
terminal exact regions          261
first-witness semantics          81
maximum event index              18
maximum contact center reached    4
```

The last two numbers are outputs, not supplied horizons.  In particular, the compiler independently reproduces the previous finite-tail fact that the first-witness task closes by center 4.

Across the whole expansion it encounters only

\[
\boxed{33}
\]

genuinely unresolved pair-ratio coordinates.

## 4. Exact global task minimum: 33 -> 27

For every pair of terminal regions carrying different first-witness tasks, compute which generated coordinates are forced on both regions with different signs.

There are `33,369` cross-task terminal-region pairs, and every one has at least one such separator.

A particularly strong lower-bound certificate occurs when a cross-task pair has exactly one available separator: that coordinate is mandatory in every task-sufficient subset.  Exactly `27` coordinates receive singleton-separator witnesses, and those same `27` coordinates separate every cross-task pair.

Therefore

\[
\boxed{
33\text{ generated candidates}
\longrightarrow
27\text{ exact cardinality-minimum task coordinates}.
}
\]

No external set-cover solver is needed: each retained coordinate has an exact necessity witness and their union is sufficient.

## 5. Independent identity check against the old programme

Only after the 27-coordinate minimum is frozen is it compared with the staged center-depth results.

The discovered set is exactly

\[
\boxed{21+5+1=27},
\]

namely:

- the 21 old globally relevant center-2 walls;
- the five globally relevant new center-3 walls;
- the shared center-4 wall
  \[
  \frac{u_4}{u_3}\ ?\ \frac{19}{11}.
  \]

The compiler therefore rediscovers `19/11` without receiving center 4 as an input.

It also independently excludes the two Phase-8C coordinates

\[
\frac{u_3}{u_2}\ ?\ \frac{14}{11},
\qquad
\frac{u_3}{u_2}\ ?\ \frac{16}{11},
\]

which were useful in per-parent minimum supports but were already known not to survive global task relevance.

This cleanly separates three optimization levels:

```text
per-parent minimum support
persistent incremental carrier
final global task minimum.
```

## 6. Mechanistic conclusion

The old causal order was approximately

```text
choose contact-center horizon
-> enumerate ratio alphabet
-> quotient / complete
-> obtain task representation.
```

The canonical-first order is now executable:

```text
canonical torus process
-> lazy next-event symbolic competition
-> process-generated equality loci
-> exact global task separation
-> minimum wall representation.
```

So the static wall geometry is not a rival ontology to the canonical process.  It is a task-directed compilation generated from that process.

Phase 11B2 then tests whether these 27 discovered coordinates can recover the old Hauffman execution advantage; see `32-canonical-global-compilation-recovers-hauffman-geometry.md`.

## Claim boundary

No new Lonely Runner theorem is proved.  The `388 / 261 / 81 / 33 / 27` results are exact for the declared bounded four-speed first-witness calibration and for the compiler-generated pair-ratio sign grammar.  No universality across runner dimension or task is claimed.
