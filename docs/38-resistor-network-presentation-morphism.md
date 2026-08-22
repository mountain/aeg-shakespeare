# Resistor networks as a non-KdV presentation-morphism calibration

**Status:** orthogonal research calibration; executable, not a public API contract.

## 1. Why leave the integrable-systems neighborhood

The KdV sequence has now produced two representations of the same structure:

```text
Hirota tau combinatorics <-> parametric scattering rewrite.
```

That is evidence for a generic `presentation morphism`, but it is still evidence
from one mathematical ecology.  Solitons, factorized scattering, tau functions,
and spectral geometry are closely related historically and structurally.

A stronger test should remove all of those ingredients while retaining the same
abstract pressure:

```text
source presentation
    -> local representation change
    -> target presentation
    -> exact task-semantics certificate.
```

Finite resistor networks provide a particularly clean test because the task
quotient is explicit finite-dimensional linear algebra.

## 2. The task quotient is the boundary response

Let a finite conductance network have boundary nodes `B` and internal nodes `I`.
Its Kirchhoff matrix is block-decomposed as

\[
L=\begin{pmatrix}
L_{BB}&L_{BI}\\
L_{IB}&L_{II}
\end{pmatrix}.
\]

After internal voltages are eliminated, the boundary voltage-current law is

\[
I_B=\Lambda V_B,
\]

with

\[
\boxed{\Lambda=L_{BB}-L_{BI}L_{II}^{-1}L_{IB}.}
\]

For this calibration, `Lambda` is the declared task semantics.  Two network
presentations are therefore task-equivalent when

\[
\boxed{\Lambda(\Pi_1)=\Lambda(\Pi_2).}
\]

This is stronger than checking selected currents, effective resistances, or power
values and weaker than requiring the internal graphs themselves to be identical.

Classically, Curtis--Ingerman--Morrow study exactly this response matrix for
circular planar resistor networks.  In particular, critical networks are tightly
controlled by Y--Delta equivalence and their conductances are recoverable from the
response matrix.  See `[Curtis-Ingerman-Morrow-1998]` in `REFERENCES.md`.

## 3. E1: discover Y--Delta from semantic equality

Take a three-leg star with conductances `a,b,c` from boundary nodes `A,B,C` to
one internal node.  Do **not** supply the corresponding triangle conductances.
Instead write a triangle with unknowns

\[
x_{AB},x_{BC},x_{CA}
\]

and solve

\[
\Lambda_Y=\Lambda_\Delta.
\]

The unique symbolic solution is

\[
\boxed{
 x_{AB}=\frac{ab}{a+b+c},\qquad
 x_{BC}=\frac{bc}{a+b+c},\qquad
 x_{CA}=\frac{ca}{a+b+c}.
}
\]

Thus the familiar Y--Delta rule enters Shakespeare as a **morphism forced by a
declared task quotient**, not as a named circuit identity inserted in advance.

This is structurally parallel to the previous KdV step:

```text
Hirota equation                 boundary response equality
      |                                  |
      v                                  v
pair coefficient A_ij            Y--Delta conductances
      |                                  |
      v                                  v
rewrite presentation             graph presentation morphism
```

The mathematical contents are unrelated; the representation pattern is the
common object under test.

## 4. E2: confluence should be task-relative, not syntactic

Consider a network with four boundary nodes `A,B,C,D` and two adjacent internal
nodes `U,V`.  There are two overlapping local elimination histories:

```text
Pi --eliminate U--> Pi_U
 |
 eliminate V
 |
 v
Pi_V
```

`Pi_U` and `Pi_V` are different graphs: one still contains `V`, the other still
contains `U`.  Nevertheless exact Schur complement gives

\[
\Lambda(\Pi_U)=\Lambda(\Pi)=\Lambda(\Pi_V).
\]

Completing the two histories gives

\[
\Pi_{UV}=\Pi_{VU},
\]

and the same boundary response.

The important point is already visible **before** reaching the common final graph:

\[
\boxed{
\text{syntactically different intermediate presentations}
\quad\text{can already be semantically joined.}
}
\]

This sharpens the KdV lesson.  A future confluence notion should not be defined as
"both histories print the same normal form".  It should be relative to a task
quotient or task signature:

\[
\boxed{Q(\Pi_1)=Q(\Pi_2).}
\]

The existing `ProcessJetSignature` machinery already embodies the analogous idea
for histories inside one process presentation: equality of current observations is
not enough; future task observations matter.  The resistor experiment adds a new
pressure: the two compared objects may live in **different presentations with
different internal state spaces**.

## 5. E3: a weak observer can certify the wrong morphism

For a three-boundary network, the full response matrix contains more information
than a few scalar Dirichlet-energy tests

\[
P(V)=V^T\Lambda V.
\]

The red team starts from the exact Y--Delta triangle corresponding to star
conductances `(3,5,7)`, namely

\[
(1,7/3,7/5).
\]

It then perturbs the triangle conductances in the direction

\[
(\delta x_{AB},\delta x_{BC},\delta x_{CA})
=(\varepsilon,-5\varepsilon,\varepsilon).
\]

For `epsilon=1/10`, two natural voltage probes have **exactly the same power** as
the true network, while a third probe differs and

\[
\Lambda_{\rm fake}\ne\Lambda_{\rm true}.
\]

So even exact agreement is not enough if the observation language is too weak.
This reproduces, in a completely different domain, the hierarchy exposed by the
KdV three-body red team:

\[
\boxed{
\text{partial/local agreement}
<
\text{declared task equivalence}
<
\text{cross-presentation completeness}.
}
\]

## 6. What this does to the API hypothesis

After KdV alone, a candidate abstraction could still have been interpreted as a
special wrapper around integrable rewrites.  The resistor calibration supplies a
second source with different mathematics:

| feature | KdV | resistor network |
| --- | --- | --- |
| presentation | tau / soliton history | weighted graph |
| local morphism | pair scattering rewrite | node elimination / Y--Delta |
| task semantics | Hirota/tau structure | DtN response matrix |
| alternative histories | braid rewrite orders | elimination orders |
| weak-certificate red team | irreducible three-body tau factor | incomplete power probes |
| completeness question | pair data reconstruct tau? | selected probes reconstruct Lambda? |

The common structure is now harder to dismiss as domain terminology:

\[
\boxed{
M:\Pi\to\Pi',
\qquad
Q(\Pi)=Q(\Pi'),
}
\]

where the certificate must state **which** `Q` is preserved.

A plausible future `PresentationMorphism` therefore needs at least conceptual
slots for:

```text
source presentation
target presentation
transformation / construction history
declared task semantics
semantic preservation certificate
cost change / reconstruction cost
```

But this note still does not promote that API.  Two positive domains are strong
pressure, not yet enough to determine the correct generic type system.

## 7. A stronger emerging distinction

The resistor experiment suggests that three notions should remain separate:

1. **syntactic confluence** -- histories reach the same representation;
2. **task-semantic confluence** -- histories reach representations with the same
   declared task quotient;
3. **presentation completeness** -- the quotient retained by one representation
   is sufficient to reconstruct the task-relevant information required by another.

KdV already separated (1)/(2) from (3).  Resistor networks now separate (1) from
(2) in an especially elementary way.

This is likely a more stable foundation for the eventual abstraction than the
word `rewrite` alone.

## 8. Next red team before API promotion

The next independent domain should change the semantics again.  Knot/braid
presentations are attractive because Reidemeister/braid/Markov moves preserve a
*topological equivalence class* rather than a linear response or an analytic
solution.

If knot presentations again force

```text
local morphism + task-relative equivalence + cross-presentation completeness
```

then promoting a generic `PresentationMorphism` would have evidence from three
substantially orthogonal mathematical settings.

## Claim boundary

The current executable test does not implement general circular-planar network
recovery, criticality, circular minors, positivity, arbitrary graph rewrite
search, or optimal electrical-network reduction.  Schur complement and Y--Delta
are classical mathematics.  The research contribution being tested is the
cross-domain interpretation: a local representation change is useful to
Shakespeare insofar as it carries an explicit certificate of preservation for a
declared task quotient.
