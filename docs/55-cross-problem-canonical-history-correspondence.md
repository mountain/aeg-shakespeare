# Canonicalization and Hauffman history geometry across heterogeneous problems

**Status:** T0 cross-problem synthesis backed by exact research-local tests; no
Theory Map or API promotion.

**Subsequent correction:** `docs/56-am-universal-history-recalibration.md`
retains the quotient-carrier split below but rejects using that split to
separate canonicalization from Hauffman/Bellman optimization on a common
universal history lift.

## 1. Question

The pendulum produced a clean bridge:

\[
\text{canonical observable quotient}
+\text{marked clock form}
\longrightarrow
\text{costed task-history planning}.
\]

Is this an accident of a one-degree-of-freedom integrable system, or one view of
a wider mechanism?  We compare three heterogeneous calibrations already present
in the repository and deliberately include cases whose natural history carrier
is not a tree.

## 2. Common audit contract

Each problem is inspected in the same order:

1. primitive process and free histories (H);
2. declared task/observer semantics (T);
3. continuation-stable canonical quotient (q_T:H\to C_T);
4. invisible but potentially compositional history residual (R_T);
5. additive or declared history cost (c);
6. stopping/cutset semantics, if the task actually has one;
7. only then, Hauffman/Bellman optimization.

This order implements the established constraint

```text
canonicalization
  -> canonical history/path
  -> ren / res / comp
  -> completion / objectification
  -> Hauffman planning.
```

It expressly forbids beginning with a convenient wall tree or fixed Lie
vocabulary and treating its nodes as the problem's ontology.

## 3. Case A — hard particles: the genuine stopping-tree case

For ordered particles in free flight, adjacent candidate contact times are

\[
\tau_i=\frac{x_{i+1}-x_i}{v_i-v_{i+1}}.
\]

The task asks for the nonempty set attaining (min_i\tau_i).  Translating and
scaling positions together with scaling velocities, and adding a Galilean
boost to every velocity, leave every (	au_i) unchanged.  Thus candidate-time
space is already a canonical quotient of substantial presentation freedom.

The task regions are argmin strata.  Pair comparisons of (	au_i) supply
admissible walls, simultaneous minima supply tie residuals, and the task stops
at the first event.  Here the history carrier is naturally a decision tree and
the physical waiting time (min_i\tau_i) supplies an invariant first-hit clock.

This is the strongest positive analogue of the pendulum bridge, despite the
absence of an elliptic carrier.

## 4. Case B — signed translation: canonicalization forces reconvergence

Let free histories be words in successor/predecessor steps `S/P`.  The exact
continuation-stable quotient is

\[
q(h)=\#S(h)-\#P(h)\in\mathbb Z,
\qquad q(hk)=q(h)+q(k).
\]

Distinct prefixes such as `SSP` and `PSS` have the same quotient and remain
equivalent after every continuation.  The free prefix tree therefore maps to a
reconvergent Cayley graph.  Objectification promotes the stable class to a
translation primitive (T_n).

This case separates canonical state from canonical cost.  `S` and `SSP` denote
the same quotient state but have different raw lengths.  Minimal word length is
relative to the declared primitive grammar, and objectification changes that
grammar.  Hence no representation-independent edge cost follows merely from
the quotient.

Huffman coding remains meaningful for a declared finite distribution over
translation tasks, but it is not the intrinsic history ontology.  The tree is
the free unfolding; the canonical carrier is the quotient graph/DAG.

## 5. Case C — Abelian periods: the residual cannot be terminally erased

On a genus-(g) algebraic carrier, lifted path integration gives a normalized
history increment in (mathbb C^g).  Closed lifted histories generate

\[
\Lambda=\mathbb Z^g+\tau\mathbb Z^g.
\]

Several histories may return to the same visible base state while differing by
an integer period residual ((m,n)\in\mathbb Z^{2g}).  These residuals compose
under path concatenation and invert under path reversal.  If the task asks only
for the endpoint modulo periods, they are quotiented; if it asks for winding,
monodromy, or accumulated action, they must survive.

The natural global carrier is therefore a covering space with a deck group or
groupoid, not a terminal decision tree.  A Hauffman tree can be introduced only
after declaring a finite observation/stopping task on this carrier.  Treating
the tree as primary would erase precisely the global history that Abelian
continuation was built to retain.

## 6. Comparative result

| Problem | Canonical quotient | History carrier | Residual | Cost | Hauffman role |
| --- | --- | --- | --- | --- | --- |
| Pendulum | ((U,Y)) on (C_E) | lifted orbit/period cover | branch and winding | (int dU/Y) | costed stopping after task choice |
| Hard particles | argmin strata of ((\tau_i)) | first-hit decision tree | tie set | first-hit time/query cost | native |
| Signed translation | net displacement (n) | Cayley graph / shared DAG | discarded word representative | grammar-relative | optional finite code |
| Abelian periods | normalized coordinate mod (Lambda) | cover/deck groupoid | ((m,n)\in\mathbb Z^{2g}) | differential integral | task-dependent only |

All four cases support a canonicalization/history correspondence.  They reject
the stronger claim that the correspondence always produces a Hauffman tree.

## 7. The extracted essential structure

The smallest common candidate is not a class named `CanonicalHistoryTree`, but
a diagram:

\[
\begin{array}{ccc}
\widetilde H_T & \xrightarrow{\;q_T\;} & C_T\\
\downarrow c && \circlearrowleft R_T
\end{array}
\]

where:

- (widetilde H_T) is a free or lifted history unfolding;
- (q_T) is a task-relative, continuation-compatible canonical projection;
- (C_T) is the compressed state/process carrier;
- (R_T) records invisible history transformations that still compose;
- (c) is an additive cost cocycle when the problem supplies one, otherwise a
  declared representation cost;
- a stopping cut (Sigma_T) is additional task structure, not automatic.

This gives the sharper relationship:

\[
\boxed{
\text{Hauffman geometry optimizes a stopping section of a canonicalized
history unfolding; it is not canonicalization itself.}
}
\]

Objectification has a precise place in this diagram.  Repeated stable quotient
motions or residual actions can become shortcut generators, changing the
presentation cost and turning portions of the free tree into shared graph/DAG
structure.  It does not license forgetting residual composition.

## 8. Three genuinely different canonicalization outputs

The examples suggest that `canonicalization` should not prematurely denote one
normal-form algorithm.  It may output at least three different kinds of data:

1. **canonical state coordinates** — pendulum carrier, collision-time ratios;
2. **canonical semantic classes/actions** — net translation and objectified
   operations;
3. **canonical lift plus residual grammar** — Abelian periods, monodromy,
   holonomy.

The shared invariant is not coordinate shape but compatibility with future
composition and declared task distinctions.

## 9. Kill conditions and next pressure

The proposed diagram should be narrowed or rejected if:

1. a claimed quotient fails continuation stability;
2. residual composition depends on arbitrary representatives;
3. the alleged cost fails additivity or presentation invariance without being
   explicitly marked as grammar-relative;
4. a stopping cut cannot be defined independently of the optimizer;
5. objectification changes exact task semantics rather than only the available
   planning language/cost.

The next useful pressure test is a stochastic/non-deterministic process.  It
should determine whether (q_T) must become a probabilistic bisimulation and
whether cost becomes an additive functional in expectation.  Only after that
should this diagram exert pressure on Experimental API design.

## 10. Governance

```text
Epistemic maturity: T0
Role: cross-problem synthesis / extraction candidate
Theory Map Change: none
Experimental/Public API pressure: none
```

