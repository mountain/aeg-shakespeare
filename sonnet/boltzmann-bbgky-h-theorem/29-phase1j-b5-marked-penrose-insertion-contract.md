# Phase 1J-B5 contract — one-layer marked Penrose insertion

**Status:** frozen and executed as a proof-level one-layer corollary of the
Penrose argument.

**Parent question:** B4 showed that an endpoint identity cannot by itself
identify a collision current. B5 asks whether the proof of Proposition 5.10
can be replayed with a root-visible collision observable before any absolute
value is taken.

**Executable owner:**
[test_marked_penrose_insertion_identity.py](../../tests/research/test_marked_penrose_insertion_identity.py).

**Result owner:**
[30-phase1j-b5-marked-penrose-insertion-results.md](./30-phase1j-b5-marked-penrose-insertion-results.md).

## 0. Dependency firewall

B5 uses B2's pre-cut C-atom event map, B3's bounded formal summability, and
B4's endpoint/path/current distinction. It uses no result from Phase 1J-A.

The result is one-layer and truncated. It does not iterate across layers,
compare truncated with actual dynamics, or identify the full B3 multi-layer
formal family with the physical response.

## 1. Source proof seam

The source is Deng--Hani--Ma,
[*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://arxiv.org/abs/2408.07818),
version 3.

The proof of Proposition 5.10 starts at equation (5.18) with the exact
C-molecule decomposition of the truncated dynamics. It then:

1. expands only the non-overlap indicators as
   \(1_{A_o^c}=1-1_{A_o}\) in (5.19);
2. groups overlap subsets \(G\subseteq E\) by the Penrose map
   \(\pi:G\mapsto F\);
3. identifies each fiber as
   \(F\subseteq G\subseteq F\cup AL(F)\) with forbidden edges absent;
4. factors the fiber sum in (5.23)--(5.24);
5. creates O-atoms from the required overlap set \(F\);
6. extracts the components containing root clusters from the complementary
   unrooted C-molecule; and
7. replaces the large-component signed contribution by an \(O_1\) positive
   majorant only at the end of (5.30).

No step before the last replacement modifies a C-atom. A root-visible
collision mark is therefore constant on every \(\pi\)-fiber.

## 2. Admitted event tests and the generating mark

Fix a bounded event test \(\psi\) on the one-layer oriented quotient event
space. The test records collision time, the root label, incoming/outgoing
states and gain/loss side, but is invariant under relabeling non-root
particles. This symmetry matches the equivalence-class and factorial
relabeling used after Proposition 5.10.

For a C-molecule \(M_C\), define

\[
Z_\psi(M_C)
=\sum_{n\in\mathcal C_H(M_C)}
\bigl(\psi(e_n^{\rm out})-\psi(e_n^{\rm in})\bigr).
\]

The Penrose sign \((-1)^{|F|}\) counts artificial O-atoms. The gain/loss sign
inside \(Z_\psi\) orients a physical C-atom. These are independent sign axes.

Equivalently, introduce a scalar generating parameter \(u\) and weight the
path by

\[
\prod_{n\in\mathcal C_H(M_C)}
\bigl(1+u(\psi(e_n^{\rm out})-\psi(e_n^{\rm in}))\bigr).
\]

The coefficient of \(u\) is \(Z_\psi(M_C)\). B5 uses this first variation
only; higher marked correlations are outside the gate.

## 3. Marked Penrose fiber lemma

For a fixed original C-molecule and a Penrose fiber with required set \(F\)
and allowed set \(AL(F)\),

\[
\begin{aligned}
&\sum_{G:\,\pi(G)=F}
(-1)^{|G|}1_G\,Z_\psi(M_C)\\
&\quad=
Z_\psi(M_C)(-1)^{|F|}
\prod_{o\in F}1_{A_o}
\prod_{o\in AL(F)}(1-1_{A_o}).
\end{aligned}
\]

The proof is the same binomial factorization as (5.23): the mark is constant
with respect to \(G\) and can be pulled outside the fiber sum. This is the
precise commutation that B4 left open.

The lemma fails for an O-atom-dependent mark. Such a quantity varies with
\(G\) and produces an additional derivative/covariance term.

## 4. Root extraction and component derivation

Let \(M_F\) be the molecule after required O-atoms have been inserted, and
write

\[
M_F=M\sqcup M',
\]

where \(M\) is the union of components containing root clusters and \(M'\) is
the complementary unrooted C-molecule, as in the proof of Proposition 5.10.

Every root-visible C-atom lies in a C-cluster containing its root particle
line. Hence it belongs to \(M\), never to \(M'\), and

\[
Z_\psi(M_F)=Z_\psi(M).
\]

If \(M\) has several rooted components, insertion is additive. For a product
of component transports,

\[
\mathcal D_\psi\Bigl(\prod_j S_{M_j}\Bigr)
=\sum_j
\bigl(\mathcal D_\psi S_{M_j}\bigr)
\prod_{i\ne j}S_{M_i}.
\]

This is an observable derivation rule, not a new physical composition law
after the estimating cuts of Sections 8--9.

## 5. One-layer theorem

Let \(\mathcal D_\psi S_N^{\Lambda,\Gamma}(\tau)\) denote the truncated
transport paired with the sum of root-visible oriented collision events in
the layer. Define

\[
\bigl(\mathcal D_\psi(S\circ1)^{\rm Pen}_M\bigr)
\]

by inserting \(Z_\psi\) into the corresponding prescribed-dynamics term.
Then the proof of (5.17), stopped before the \(O_1\) replacement, gives the
exact signed identity

\[
\boxed{
\begin{aligned}
\mathcal D_\psi S_N^{\Lambda,\Gamma}(\tau)
&=
\sum_{\substack{M\in F_\Lambda\\r(M)=[s]}}
\mathcal D_\psi(S\circ1)^{\rm Pen}_M
\circ S_{[N]\setminus p(M)}^{\Lambda,\Gamma}\\
&\quad+
\mathcal R_{\psi,\Lambda}^{\rm large}.
\end{aligned}
}
\]

The remainder \(\mathcal R_{\psi,\Lambda}^{\rm large}\) is the exact signed
sum of the \(F_\Lambda^{\rm err}\) terms occurring in (5.26), with the same
mark inserted. It is not the later \(O_1\) majorant.

After applying a symmetric density and integrating non-root variables, this
is equality of bounded weak pairings on the declared one-layer event space.
Proposition 7.5, equations (7.13)--(7.15), supplies the term-level
identification of each marked C-atom with its prescribed collision event.

## 6. Large-component remainder

The source proof bounds the large-component endpoint term by taking absolute
values in (5.30). B5 records the exact signed term first:

\[
\mathcal R_{\psi,\Lambda}^{\rm large}
=
\sum_{M\in F_\Lambda^{\rm err}}
\mathcal D_\psi\mathcal A_M^{\rm signed}.
\]

For bounded \(\psi\), the same early erasure as B3 gives a conditional
majorant with one additional factor
\(|\mathcal C_H(M)|\le |M|\). The B3 absorption argument shows that this
linear cost is harmless under the source hierarchy. Equality and estimation
remain separate records.

## 7. Exact executable obligations

The rational certificate verifies:

1. interval fibers partition the full overlap-subset expansion;
2. grouped and ungrouped inclusion--exclusion agree for every Boolean overlap
   assignment;
3. a C-atom mark is constant on each O-atom grouping fiber;
4. marking before expansion equals marking every grouped term;
5. root extraction routes every eligible C-mark exactly once;
6. several rooted components obey the additive insertion derivation;
7. Penrose parity and gain/loss orientation are independent sign axes;
8. the large-component signed remainder cancels the main term before
   positive domination;
9. symmetric event quotienting preserves non-root relabeling multiplicity;
10. an O-atom-dependent mark is a counterexample to fiber constancy;
11. a non-root collision is not silently promoted to a root current mark.

All calculations are exact rationals and Boolean identities.

## 8. Kill conditions

B5 fails or must be narrowed if:

- the event test distinguishes arbitrary non-root labels without an orbit
  multiplicity ledger;
- the mark depends on artificial O-atoms or the Penrose grouping choice;
- a root-visible C-atom is routed into the unrooted complement;
- insertion is treated multiplicatively instead of as a derivation over
  rooted components;
- the \(F_\Lambda^{\rm err}\) term is replaced by its positive majorant before
  the signed identity is stated;
- gain/loss and Penrose signs are merged; or
- the result is iterated across layers without a new proof.

## 9. Claim ceiling and next gate

B5 earns a one-layer marked Penrose insertion identity for bounded,
non-root-relabeling-invariant event tests, with an exact signed
large-component remainder.

It does not earn:

- a multi-layer marked current identity for the B3 family;
- comparison of truncated and actual hard-sphere currents;
- current-valued geometry, \(\mathrm{Err}_2\), or terminal estimates;
- an unbounded logarithmic test, entropy chain rule or H theorem;
- Core/Map/rank/API promotion.

The next gate is to iterate the one-layer derivation through the exact signed
cumulant recurrence (5.62)--(5.63) while keeping the layer of the unique mark
explicit. Only then can the resulting multi-layer current be compared with
the B3 absolutely summable formal family.

## 10. Repository boundary

### Mathematical Core

Unchanged. The result remains problem-local.

### Engineering Architecture

Refined research-locally. Event insertion is a derivation on rooted transport
products and must precede majorization.

### Theory Map

Unchanged. B5 is U4/E proof evidence, not a new objectification.

### API

No pressure.
