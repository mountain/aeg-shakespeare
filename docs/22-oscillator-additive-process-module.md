# Oscillator I: additive process closure before spectrum

**Status:** classical calibration using existing grammar/relation machinery; no new core API.

## 1. Why this example comes after Pendulum III

Pendulum III forced one small structured-construction mechanism: a caller-declared pairing could generate scalar observers while preserving recipes such as `pair(q,e)` separately from the backend coordinate `qy`.

The harmonic oscillator puts pressure on a different part of the system.  Its primitive process

\[
D x=p,\qquad D p=-x
\]

closes immediately under scalar linear combination.  This makes it a useful calibration for the **additive** representation regime without yet asking for spectral or Fourier theory.

The key discipline is to state the prior assumption correctly: Shakespeare's current `GeneratedGrammar` backend already uses finite scalar linear span as its closure policy.  Therefore this example does not "discover addition from nothing."  It asks a narrower and testable question:

> Given additive/scalar span as an allowed presentation operation, does the raw process find a tiny closed grammar before any spectral language is supplied?

## 2. Single-seed discovery

Start from the single seed

\[
x.
\]

Repeated process action gives

\[
x\xrightarrow{D}p\xrightarrow{D}-x.
\]

The first image adds one new independent direction.  The second image lies in the span already generated.  Thus the exact generated grammar is

\[
V=\operatorname{span}\{x,p\}
\]

with process depths

\[
(0,1)
\]

and growth profile

\[
(1,2).
\]

This is the first point in the vignette where an additive module is visible as a compact process presentation.

## 3. Relation before spectrum

Once the grammar has closed, Shakespeare asks for the shortest constant-coefficient process relation valid on the whole grammar.  It finds

\[
\boxed{D^2+1=0.}
\]

Nothing spectral has yet been asserted.

The order of explanation is intentionally

\[
\text{process}
\to
\text{additive closure}
\to
\text{return relation}
\]

rather than

\[
\text{known oscillator}
\to
\text{eigenvalues }\pm i
\to
\text{complex exponentials}.
\]

The latter route is classical and important, but it belongs to Oscillator II.

## 4. Basis accident red team

Now start from a different seed,

\[
x+p.
\]

The generated basis becomes

\[
x+p,\qquad -x+p.
\]

This basis is visibly different from \(x,p\), but it spans the same two-dimensional additive grammar.  More importantly, the discovered grammar-wide relation is still

\[
D^2+1=0.
\]

This is a small but useful separation:

\[
\boxed{\text{basis presentation changes; process relation survives}.}
\]

It prevents the finite additive module from being confused with one preferred coordinate basis.

## 5. Five-line research ledger

**Primitive assumptions.** Scalar assignments `x,p`, process rules `D x=p`, `D p=-x`, and the existing generated-grammar policy that finite scalar linear span is an admissible closure language.

**Forbidden structures.** Caller-supplied ambient basis, matrix representation, eigenvalues/eigenvectors, complex coordinate, sine/cosine, Fourier modes, frequency template.

**Discovered structure.** A two-direction closed additive grammar and the process relation `D^2+1`.

**New reusable abstraction.** None.  Existing `GeneratedGrammar`, exact span coordinates, and relation discovery already suffice.

**Unresolved manual choice.** Additive/scalar span is still a chosen closure policy.  The example demonstrates its economy for the oscillator but does not establish its universality.

## 6. Why we stop before spectrum

Over \(\mathbb C\), one may factor

\[
D^2+1=(D-i)(D+i)
\]

and then interpret the corresponding kernels spectrally.  Doing that in this vignette would hide an important boundary: the current relation factorization is over the existing coefficient domain, and no coefficient-field extension has yet been requested by the process presentation.

Oscillator II should therefore ask a new, sharply delimited question:

> When and why should Shakespeare extend the coefficient language so that a process relation factors further, and what new primitives does that extension force?

That question, rather than a preloaded eigenvalue API, should be the entry point to spectral structure.
