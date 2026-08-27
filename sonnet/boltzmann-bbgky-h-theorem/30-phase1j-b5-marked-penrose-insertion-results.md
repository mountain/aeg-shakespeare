# Phase 1J-B5 results — the one-layer Penrose expansion accepts a collision mark

**Verdict:** the one-layer marked Penrose insertion gate passes for bounded
event tests invariant under non-root relabeling. The collision mark depends
only on C-atoms, while the Penrose argument groups only O-atom overlap
subsets. It is therefore constant on every grouping fiber and commutes with
the inclusion--exclusion proof before absolute values.

This establishes the main one-layer signed current identity and retains the
large-component family as an exact signed remainder. It does not yet identify
the multi-layer B3 formal family with the physical hard-sphere response.

**Contract:**
[29-phase1j-b5-marked-penrose-insertion-contract.md](./29-phase1j-b5-marked-penrose-insertion-contract.md).

**Executable:**
[test_marked_penrose_insertion_identity.py](../../tests/research/test_marked_penrose_insertion_identity.py).

## 1. New proof-level corollary

For a fixed original C-molecule \(M_C\), the observable

\[
Z_\psi(M_C)
=\sum_{n\in\mathcal C_H(M_C)}
\bigl(\psi(e_n^{\rm out})-\psi(e_n^{\rm in})\bigr)
\]

does not depend on the artificial overlap subset \(G\subseteq E\). Multiplying
equations (5.19)--(5.24) by \(Z_\psi(M_C)\) therefore preserves every Penrose
fiber cancellation.

When the proof extracts rooted components, every eligible mark remains in the
rooted molecule and no eligible mark enters the unrooted complement. For
several rooted components the insertion obeys the ordinary additive
derivation rule.

Consequently, the proof of Proposition 5.10 gives

\[
\mathcal D_\psi S_N^{\Lambda,\Gamma}
=
\sum_{M\in F_\Lambda}
\mathcal D_\psi(S\circ1)^{\rm Pen}_M
\circ S_{[N]\setminus p(M)}^{\Lambda,\Gamma}
+\mathcal R_{\psi,\Lambda}^{\rm large}
\]

before the large-component term is replaced by an \(O_1\) majorant.
Proposition 7.5 identifies each C-atom insertion with the corresponding
prescribed collision event.

## 2. Exact certificate ledger

The finite fixture partitions all eight subsets of three potential O-edges
into three interval fibers. For every one of the eight Boolean overlap
assignments:

- the ungrouped expansion equals the direct no-overlap indicator;
- each interval fiber equals its required-edge times allowed-edge product;
- the sum of grouped fibers equals the ungrouped expansion; and
- multiplying by four different bounded C-atom tests preserves every
  identity.

The root-routing fixture contains two root clusters, two unrooted clusters,
two eligible root C-marks and one ineligible non-root C-mark. Every Penrose
representative routes both eligible marks into rooted components exactly
once.

The targeted run is:

    11 passed in 0.04s

## 3. Independent sign axes and exact remainder

An even Penrose coefficient produces gain \(+2/5\) and loss \(-2/5\).
Changing only O-atom parity negates both weights. Thus overlap parity and
gain/loss orientation commute; neither can reconstruct the other.

For the assignment in which only overlap \(b\) is active, the main marked
term is \(+3/4\) and the large-component marked remainder is \(-3/4\). Their
exact cancellation is destroyed if the latter is prematurely replaced by
its absolute majorant \(3/4\). This is the concrete reason to preserve the
signed remainder before estimation.

## 4. Red teams

Two structural violations fail exactly.

1. A mark proportional to the number of selected O-edges varies inside a
   Penrose fiber. Its expanded marked value is one while pulling out the
   representative value gives zero.
2. A collision in a non-root cluster is not an eligible root-current mark,
   even when later artificial overlaps connect its cluster to a root
   component.

The second distinction keeps the observable task-relative: B5 identifies the
declared root current, not every collision in a connected Penrose molecule.

## 5. Relabeling boundary

The result is stated on the event quotient invariant under non-root particle
relabeling. Three relabeled partners contribute three identical
representative pairings, so the orbit sum is exactly the orbit multiplicity
times the representative. A label-sensitive test would require a different
event space and a separate multiplicity proof.

## 6. What has and has not advanced

B5 has earned:

- marked inclusion--exclusion on every Penrose grouping fiber;
- exact root-component routing of eligible C-marks;
- the additive insertion derivation for several rooted components;
- an exact signed one-layer large-component remainder;
- independent preservation of both sign axes; and
- eleven exact certificates and red teams.

B5 has not earned:

- a multi-layer identity for the B3 current;
- actual-versus-truncated current control;
- \(\mathrm{Err}_2\), geometry, or terminal current estimates;
- logarithmic-tail control, entropy or H; or
- a generic Process Geometry object/API.

The next theorem-sized target is a marked version of the exact signed
cumulant recurrence (5.62)--(5.63). The mark must carry a layer index, and the
recurrence must prove that each physical root-visible collision is inserted
once across the full layer sequence. Absolute summability from B3 may be used
only after that signed equality is established.

## 7. Repository effect

### Mathematical Core

Unchanged.

### Engineering Architecture

Refined research-locally: insertion is now explicitly typed as a derivation
before majorization.

### Theory Map

Unchanged.

### API

No pressure.
