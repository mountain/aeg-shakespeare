# Braid and Markov moves as a third presentation-morphism calibration

**Status:** third-domain research calibration; executable, not a public API contract.

## 1. Why topology is the decisive third test

The emerging pattern now has two independent sources:

```text
KdV:
    tau <-> scattering history

resistor networks:
    weighted graph -> Schur/Y-Delta equivalent graph
```

The preserved semantics in those two cases is, respectively, analytic/integrable
structure and a finite-dimensional boundary response matrix.  A third test should
change the semantic category itself.

Braids and links do exactly this.  Here a presentation morphism should preserve a
**topological closure class**, and Markov stabilization can even change the braid
index.  Thus source and target presentations need not inhabit the same state space.

## 2. Three nested representation levels

A braid word in `B_n` admits at least three relevant levels of observation:

```text
literal Artin word
    -> braid-group element
    -> isotopy class of the standard closure.
```

These levels have different equivalence laws.

The Artin braid relation

\[
\sigma_1\sigma_2\sigma_1
=
\sigma_2\sigma_1\sigma_2
\]

changes the literal word while preserving the braid element.

Markov conjugation

\[
\beta\longmapsto\gamma\beta\gamma^{-1}
\]

need not preserve a chosen linear representation matrix literally, but preserves
the isotopy class of the closure.

Markov stabilization

\[
\beta\in B_n
\longmapsto
\beta\sigma_n^{\pm1}\in B_{n+1}
\]

is stronger still: it changes the presentation space itself while preserving the
closed oriented link type.  Markov's theorem says braid isotopy together with
conjugation and stabilization/destabilization is complete for closed-braid link
isotopy.  See `[Birman-1974]` in `REFERENCES.md`.

## 3. Executable observer: Burau and Alexander

The research test uses the unreduced Burau generator

\[
\begin{pmatrix}
1-t&t\\
1&0
\end{pmatrix}
\]

inside the identity matrix, then explicitly passes to the quotient by the invariant
all-ones vector to obtain the reduced Burau representation

\[
\rho_n:B_n\to GL_{n-1}(\mathbb Z[t,t^{-1}]).
\]

For a braid `beta` whose standard closure is `L`, the executable closure observer is

\[
\boxed{
\Delta_L(t)
=
\frac{1-t}{1-t^n}
\det(I-\rho_n(\beta)),
}
\]

up to the usual Laurent unit ambiguity.

The test examples are chosen so that the displayed representatives agree exactly,
so no normalization machinery is required yet.

## 4. E1: braid relation as an internal presentation morphism

For `B_3`, the two literal histories

\[
(1,2,1),\qquad(2,1,2)
\]

are different words, but their reduced Burau matrices agree exactly.

This is the most familiar kind of morphism:

```text
same presentation space
same represented object
alternative syntax.
```

It resembles the first KdV rewrite calibration but does not yet test the broader
hypothesis.

## 5. E2: conjugation preserves a coarser task quotient

Take a three-strand trefoil presentation `beta` and a conjugate

\[
\gamma\beta\gamma^{-1}.
\]

The executable test finds

\[
\rho_3(\beta)
\ne
\rho_3(\gamma\beta\gamma^{-1})
\]

as literal matrices in the chosen basis, while

\[
\Delta_{\widehat\beta}(t)
=
\Delta_{\widehat{\gamma\beta\gamma^{-1}}}(t)
=t^2-t+1.
\]

Thus the morphism is not certified at the matrix-syntax level; it is certified only
after passing to the declared closure semantics.

This reinforces the resistor-network lesson:

\[
\boxed{
\text{morphism validity is relative to }Q,
\text{ not to representation syntax.}
}
\]

## 6. E3: stabilization crosses state-space dimension

The two-strand trefoil braid

\[
\beta=\sigma_1^3\in B_2
\]

is positively stabilized to

\[
\beta\sigma_2\in B_3.
\]

Their reduced Burau matrices have sizes

\[
1\times1
\qquad\text{and}\qquad
2\times2.
\]

Matrix equality is therefore not even type-correct.  Nevertheless both closure
presentations give

\[
\Delta(t)=t^2-t+1.
\]

This is the strongest API pressure so far.  A generic `PresentationMorphism` cannot
assume

- one fixed carrier type,
- one fixed alphabet,
- one fixed coordinate dimension, or
- equality inside a single representation backend.

Instead it must allow

\[
\boxed{
M:\Pi_A\to\Pi_B
}
\]

where `Pi_A` and `Pi_B` may be genuinely different presentation categories and only
a declared task semantics connects them.

## 7. Red team: topological observation can still be too weak

The number of components of a closed braid is the number of cycles in its induced
strand permutation.  This is a genuine closure invariant, but it is far from
complete.

The closures of

\[
\sigma_1
\qquad\text{and}\qquad
\sigma_1^3
\]

in `B_2` both have one component.  The first is an unknot and the second a trefoil;
the executable Alexander observers are

\[
1
\qquad\text{and}\qquad
t^2-t+1.
\]

So the same warning has now appeared in three unrelated forms:

```text
KdV:       pairwise confluence can miss irreducible tau data
resistors: two exact power probes can miss the full DtN map
braids:    component count can miss closure topology seen by Alexander
```

The abstraction should therefore never speak of "preserving the object" without
recording which quotient/observer makes that statement meaningful.

## 8. Three-domain synthesis

The common pattern is now:

| domain | source/target presentations | local/global morphism | declared semantics |
| --- | --- | --- | --- |
| KdV | tau / scattering histories | pair rewrite / factorization | Hirota/tau structure |
| resistor networks | weighted graphs | Schur/Y-Delta elimination | DtN response |
| braids/links | braid words, even different `B_n` | braid/Markov moves | closure topology observer |

Across all three, the useful generic data has the same shape:

```text
source presentation
target presentation
construction/history of the transformation
declared task semantics
preservation certificate
possibly a decoder/reconstruction map
cost change
```

This is now substantial evidence that `PresentationMorphism` is not domain-specific
terminology.

## 9. What should be promoted now

Three domains are enough to justify promoting a **minimal** generic morphism object,
but not enough to bake in any domain-specific equality engine.

The first public version should therefore be structurally weak:

```text
PresentationMorphism[source, target, certificate]
    source
    target
    certificate
    label / provenance
```

with semantics supplied externally by the caller or discovery layer.  It should not
yet require a groupoid, category, inverse, composition law, normal form, or universal
`equivalent()` method.

A separate later abstraction may represent composable morphism histories once a
fourth calibration establishes what composition certificates actually need to retain.

## Claim boundary

The executable tests do not solve braid equivalence or knot isotopy.  Alexander
polynomials are incomplete link invariants.  Markov and Burau theory are classical.
The Shakespeare claim is narrower: this third domain demonstrates that a useful
presentation morphism may preserve semantics only after quotienting to a different
mathematical category, and may connect source and target presentations with different
carrier dimensions.
