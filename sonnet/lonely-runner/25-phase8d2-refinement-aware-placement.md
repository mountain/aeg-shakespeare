# Phase 8D.2 — refinement-aware Huffman placement exposes a space-time Pareto frontier

**Status:** exact bounded seven-mixture placement calibration passed.  
**Scope:** reorder only the old 21 center-2 task-relevant walls; keep all Phase-8C.2 completion decoders frozen below their six completion terminals.  
**Predecessor:** [`24-phase8d-persistent-dag-increment.md`](24-phase8d-persistent-dag-increment.md)

## 1. Question

Phase 8D produced a sparse persistent graft with the same total amount of
decision structure as the separately frozen fresh center-3 time-first tree:

```text
both: 376 tree/boundary nodes, 125 internal query nodes.
```

But the structure is placed differently:

```text
persistent graft: peak/worst = 75/12
fresh center-3:   peak/worst = 72/10.
```

The first placement experiment asks whether this gap is merely a consequence of
using the old current-task Huffman weights.

> If the old 21-wall prefix is reoptimized with explicit refinement weights,
> while the six new completion decoders remain frozen at terminal leaves, can
> the persistent architecture recover the fresh tree's space-time geometry?

## 2. Two distributions are kept explicit

The current-task distribution is the same 55 integer quadruples used in the
center-2 Huffman calibration.

The continuation distribution is supported on the six genuine completion
parents and weights each parent by its number of locally realizable center-3
completion children.  These masses sum to

\[
288.
\]

For the **proposal search only**, Phase 8D.2 mixes the normalized distributions:

\[
w_\lambda
=(1-\lambda)\frac{w_{\rm current}}{55}
+\lambda\frac{w_{\rm refine}}{288}.
\]

Seven exact values are sampled:

\[
\lambda\in
\left\{
0,\frac1{16},\frac18,\frac14,\frac12,\frac34,1
\right\}.
\]

The final evaluation is not scalarized: current depth, completion-child depth,
volume, peak, and worst depth are reported separately.

## 3. Exact placement profile

| `lambda` | current total / 55 | completion final total / 288 | old tree nodes | graft nodes | peak | worst |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 135 / 2.4545 | 2933 / 10.1840 | 328 | 376 | 75 | 12 |
| 1/16 | 136 / 2.4727 | 2146 / 7.4514 | 328 | 376 | 93 | 9 |
| 1/8 | 136 / 2.4727 | 2146 / 7.4514 | 328 | 376 | 93 | 9 |
| 1/4 | 143 / 2.6000 | 2027 / 7.0382 | 328 | 376 | 87 | 10 |
| 1/2 | 163 / 2.9636 | 1739 / 6.0382 | 328 | 376 | 90 | 9 |
| 3/4 | 163 / 2.9636 | 1739 / 6.0382 | 328 | 376 | 90 | 9 |
| 1 | 234 / 4.2545 | 1721 / 5.9757 | 379 | 427 | 108 | 9 |

The root wall also changes only after refinement receives substantial weight:

```text
lambda <= 1/4: root u4/u1 ? 4
lambda = 1/2, 3/4: root u3/u1 ? 4
lambda = 1: root u3/u2 ? 3/2.
```

## 4. Small refinement weight gives cheap time improvement — but expensive space

The most striking comparison is

\[
\lambda=0
\quad\text{versus}\quad
\lambda=\frac1{16}.
\]

Current weighted depth changes by only

\[
135\to136,
\]

while completion-child final depth improves dramatically:

\[
2933\to2146,
\]

and worst depth improves

\[
12\to9.
\]

But peak frontier simultaneously jumps

\[
\boxed{75\to93}.
\]

Thus a refinement-aware expected-depth scalar can buy large time improvement at
almost no current-time cost while making the history-space geometry much worse.

This is direct executable evidence that refinement-aware Huffman placement is a
multi-axis problem.

## 5. The fresh `72/10` target is not reached in this restricted architecture

No sampled candidate simultaneously satisfies

\[
\text{peak}\le72,
\qquad
\text{worst}\le10.
\]

In fact the lowest sampled peak remains the original graft's 75, while every
refinement-weighted candidate that improves worst depth increases peak frontier.

After duplicate metric profiles are collapsed (`1/16=1/8`, `1/2=3/4`), all five
sampled profiles are Pareto-nondominated across

```text
current weighted depth
completion-child final depth
updated tree volume
peak frontier
worst depth.
```

This rules out the naive hope that one scalar current/refinement mixture will
select an unambiguous better presentation inside the old-prefix-first
architecture.

## 6. Architectural interpretation

Phase 8D already showed that local completion found the correct **amount** of
decision structure.  Phase 8D.2 now shows that reweighting the old prefix alone
cannot recover the fresh tree's placement quality in the sampled family.

The remaining gap therefore points to a stronger architectural operation:

> some newly generated completion walls must be allowed to participate before a
> complete old persistent parent has been identified, or equivalent new
> completion structure must be shared across old-parent contexts.

In other words, the next search space must relax

```text
old persistent tree
    -> identify one old terminal
    -> local completion decoder
```

into a more general interleaved persistent DAG.

This does **not** mean importing the fresh center-3 tree as an answer.  The
challenge is to derive admissible early activation/sharing rules from old
process geometry plus the already-discovered completion walls.

## 7. Cost-API consequence

Phase 8D.2 strengthens, but does not yet freeze, a cost-design requirement:

\[
\boxed{
C(P)\text{ must preserve current time, refinement time, and frontier geometry as
separate axes.}
}

Expected depth under a mixture distribution is useful as a proposal mechanism,
but it cannot replace space-time Pareto comparison.

This is consistent with the existing `PresentationCost` philosophy of avoiding
mandatory scalarization.  No new public cost field is added yet because the
correct representation of continuation/refinement mass has only one bounded
calibration so far.

## 8. Executable evidence

Implementation:

```text
sonnet/lonely-runner/python/refinement_aware_huffman.py
```

Executable mathematical essay:

```text
tests/research/test_lonely_runner_refinement_aware_huffman.py
```

Recorded exact run:

```text
workflow: Sonnet Lonely Runner Refinement Placement
run id:   32586811587
Python:   3.12.14
essay:    1 passed in 29.03 s
```

The workflow is restored to manual `workflow_dispatch`; routine CI audits the
essay structure and references without repeating the seven exact tree searches.

## 9. Next experiment — controlled interleaving

Freeze all seven mixture results as a negative/positive placement calibration.

The next representation experiment should allow the seven newly discovered
center-3 completion walls to become queryable **before** full old-parent
resolution, but only where old process constraints make that activation
semantically admissible.

Required guardrails:

1. no full center-3 tree is supplied;
2. completion walls remain exactly those generated by Phase 8C;
3. stable old states may branch on an early new wall only if branches can be
   certified to reconverge to the same task semantics;
4. every early activation must have an exact old-state/local-contact certificate;
5. compare resulting history geometry to both the `75/12` graft and the frozen
   `72/10` fresh-tree oracle only after the interleaved representation is built.

This is the first plausible route for discovering cross-parent completion
sharing without surrendering the process-first methodology.

## 10. Claim boundary

This is a seven-point exact placement sweep, not an optimization over every
scalar mixing coefficient and not a theorem that all old-prefix reweightings
fail.

The bounded claim is narrower:

\[
\boxed{
\text{within the sampled old-prefix-first family, refinement-time gains and
frontier-space cost form a genuine Pareto tradeoff, and no candidate recovers the
fresh }72/10\text{ placement.}
}
\]

## 11. References

[Huffman-1952] David A. Huffman, "A Method for the Construction of
Minimum-Redundancy Codes," *Proceedings of the IRE* 40(9) (1952), 1098--1101;
DOI 10.1109/JRPROC.1952.273898.

[Sungkawichai-Trakulthongchai-2026] Touch Sungkawichai, Tanupat
Trakulthongchai, "Eleven, twelve, and thirteen lonely runners,"
arXiv:2604.23906 (2026), https://arxiv.org/abs/2604.23906 .
