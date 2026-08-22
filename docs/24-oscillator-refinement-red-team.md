# Oscillator III red team: finer splitting is not automatically cheaper

**Status:** red-team calibration only; no new core API.

## 1. Why this test is needed

Oscillator II established a controlled bridge

\[
D^2+1
\longrightarrow
(D-i)(D+i)
\]

when the caller explicitly enlarges the coefficient language.  The resulting
one-dimensional relation kernels are mathematically useful, but they create an
immediate danger of over-generalization:

> if a process relation can be split more finely, should Shakespeare always
> prefer the finest splitting?

This note constructs a small counter-pressure before any `Spectrum`,
`EigenMode`, or coefficient-language cost hierarchy is introduced.

## 2. Two-frequency process

Take two independent oscillators

\[
D x_1=p_1,\qquad Dp_1=-x_1,
\]

\[
D x_2=p_2,\qquad Dp_2=-2x_2,
\]

and begin from the mixed seed

\[
f=x_1+x_2.
\]

The existing additive-span grammar search grows four independent process
directions and discovers

\[
\boxed{D^4+3D^2+2=0}
\]

or equivalently

\[
\boxed{(D^2+1)(D^2+2)=0.}
\]

No frequency list or spectral basis is supplied.

## 3. Two exact presentations

In the base coefficient language the relation has two quadratic factors,

\[
D^2+1,\qquad D^2+2,
\]

and the corresponding relation kernels are both two-dimensional.  Together
they exactly span the four-dimensional process grammar.

Now make a separate representation proposal: adjoin

\[
i,\qquad \sqrt2.
\]

The same already-discovered relation refines to

\[
(D-i)(D+i)(D-i\sqrt2)(D+i\sqrt2).
\]

The four corresponding relation kernels are one-dimensional and again exactly
span the same original process grammar.

Thus both presentations are exact and sufficient.

## 4. Refinement improves one quantity and worsens another

The base presentation has

\[
\text{component count}=2,
\qquad
\max(\text{component relation order})=2.
\]

The refined presentation has

\[
\text{component count}=4,
\qquad
\max(\text{component relation order})=1.
\]

Therefore refinement does not monotonically reduce representation structure:

- the refined presentation wins on maximum relation order;
- the base presentation wins on component count.

This conflict exists **before** we price the additional coefficient language.
The refined factors also genuinely contain non-rational coefficients involving
\(i\) and \(\sqrt2\), while the base quadratic factors use rational
coefficients only.

## 5. A red-team use of the existing Pareto machinery

The executable vignette deliberately does not propose a canonical cost model.
For one transparent witness only, it maps

- component count -> `PresentationCost.grammar`;
- maximum component relation order -> `PresentationCost.relations`.

Then

\[
(2,2)
\quad\text{and}\quad
(4,1)
\]

are Pareto-incomparable.

Equal scalar weights prefer the two-component quadratic presentation, whereas a
relation-order-heavy weighting prefers the four-component linear presentation.
The purpose is not to endorse either weighting.  It is to certify that no
weight-free rule of the form

\[
\text{finer splitting}\Rightarrow\text{better presentation}
\]

survives even this elementary test.

## 6. Five-line research ledger

**Primitive assumptions.** Two uncoupled oscillator processes, one mixed seed,
and the existing additive-span closure policy.

**Forbidden structures.** Predeclared frequencies/eigenvalues, eigenvectors,
Fourier basis, automatic algebraic closure, or a universal spectral objective.

**Discovered structure.** A four-dimensional grammar, the relation
`D^4+3D^2+2`, its two quadratic base components, and—under an explicit extension
proposal—four linear components; both decompositions exactly span the same
grammar.

**New reusable abstraction.** None.  Existing grammar, relation, coefficient-
extension, kernel, cost, and Pareto machinery suffice.

**Unresolved manual choice.** Which structural reduction matters for the task:
fewer components, lower relation order, simpler coefficient language, cheaper
decoding, or something else?

## 7. What this changes in the roadmap

The next step should **not** be to add a coefficient-language cost merely to
force a universal winner.  This red team says something more basic: even with
language complexity temporarily ignored, exact decompositions can make
different structural trade-offs.

A coefficient-language cost may still become necessary, but it should be
introduced only inside a task where extending the language carries a measurable
benefit or burden.  Likewise, the later translation/character/Fourier
calibration should not inherit an assumption that maximal one-dimensional
splitting is the universal endpoint of representation search.

The protected principle is therefore

\[
\boxed{\text{spectral refinement is a representation option, not a universal normal form.}}
\]
