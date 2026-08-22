# Addition/Multiplication Function Theory

**Status:** first concrete process-generated function theory; executable but deliberately incomplete.

## 1. Meaning of A/M

In this note **A means Addition** and **M means Multiplication**.  They are the two arithmetic process directions inherited from the one-variable AEG construction.  The function theory is built *after* those operations are fixed:

\[
\text{arithmetic processes}
\longrightarrow
\text{ordered differential algebra}
\longrightarrow
\text{process-adapted functions}.
\]

This order matters.  The module is not an attempt to rename the ordinary derivative and then rebuild familiar analysis around it.

Shakespeare also does **not** assume that A/M is the only possible function theory.  The public `ProcessFrame` and `ProcessFunctionModule` interfaces are intentionally generic so that projective, elliptic/Abelian, hyperelliptic, Lie-algebroid, or other process-generated theories can coexist.

## 2. Finite arithmetic process

Use an assignment `a` and logarithmic multiplicative coordinate `v`.  The finite Addition and Multiplication flows are

\[
T_t:(a,v)\mapsto(a+t,v),
\]

\[
S_s:(a,v)\mapsto(e^s a,v+s).
\]

They obey

\[
\boxed{S_sT_t=T_{e^s t}S_s}.
\]

Thus order is already visible before any differential language is introduced.  `AMFunctionTheory.finite_relation_residual` provides an exact symbolic certificate for this relation.

## 3. Infinitesimal A/M frame

The corresponding process frame is

\[
A=\partial_a,
\qquad
M=\partial_v+a\partial_a,
\]

with

\[
\boxed{[A,M]=A}.
\]

Shakespeare retains literal `ProcessWord` order separately from this symbolic representation.  The commutator is therefore a relation *between* ordered histories, not permission to erase history.

The dual coframe is

\[
\theta_A=da-a\,dv,
\qquad
\theta_M=dv,
\]

and its structure equation is

\[
d\theta_A=-\theta_A\wedge\theta_M,
\qquad
d\theta_M=0.
\]

The current executable layer represents the process frame; explicit differential-form objects can be added later if they become useful to downstream computation.

## 4. Power-weight lattice

A first process-adapted family is

\[
\boxed{\Phi_{\nu,w}=a^\nu e^{(w-\nu)v}}.
\]

Its labels are adapted to Addition and Multiplication:

\[
M\Phi_{\nu,w}=w\Phi_{\nu,w},
\]

\[
A\Phi_{\nu,w}=\nu\Phi_{\nu-1,w-1}.
\]

Multiplication of functions adds the labels:

\[
\Phi_{\nu,w}\Phi_{\mu,z}
=
\Phi_{\nu+\mu,w+z}.
\]

This is implemented by `AMPowerWeight`.  The labels should be read as process coordinates of this family, not as a claim that every relevant function belongs to it.

The ordered algebra also gives the PBW-type relation

\[
\boxed{M^nA^m=A^m(M-m)^n}.
\]

`AMFunctionTheory.pbw_residual` verifies this relation on supplied expressions while preserving literal process histories elsewhere in the library.

## 5. Process primitives and resonance

The A/M lattice gives a particularly concrete way to see where new function classes appear.

For Addition,

\[
A^{-1}\Phi_{\nu,w}
=
\frac{1}{\nu+1}\Phi_{\nu+1,w+1},
\qquad \nu\ne-1.
\]

At the resonance locus `nu = -1`, the lattice step is singular and one needs the logarithmic extension

\[
\boxed{
A^{-1}\Phi_{-1,w}
=
e^{(w+1)v}\log a.
}
\]

Likewise, for Multiplication,

\[
M^{-1}\Phi_{\nu,w}
=
\frac{1}{w}\Phi_{\nu,w},
\qquad w\ne0,
\]

while at zero multiplicative weight,

\[
\boxed{
M^{-1}\Phi_{\nu,0}
=
v\Phi_{\nu,0}.
}
\]

The latter is a generalized/Jordan-like process extension: `M` annihilates the base weight-zero element but maps the added `v`-extension back to it.

`AMPrimitive` records both ordinary and resonant primitives, and `primitive_residual` provides the exact certificate.

The intended interpretation is structural:

\[
\text{operation hierarchy}
\rightarrow
\text{differential-algebra singularities/resonances}
\rightarrow
\text{new function families}.
\]

Logarithms are therefore a first example of a function that can be *forced* by failure of an A/M process inversion, rather than merely inserted as a named classical function.

## 6. Ordered A/M path flow

For an ordered process path

\[
\mathscr D=\alpha(t)A+\beta(t)M,
\]

the assignments obey

\[
\dot a=\alpha+\beta a,
\qquad
\dot v=\beta.
\]

Let

\[
B(T)=\int_0^T\beta(t)\,dt.
\]

Then

\[
\boxed{
a(T)=e^{B(T)}a_0+
\int_0^T e^{B(T)-B(t)}\alpha(t)\,dt.
}
\]

The second term is retained as a process-history term: Multiplication occurring later in the path reweights earlier Addition history.  `AMFunctionTheory.path_flow` exposes this decomposition rather than returning only the final simplified value.

## 7. Low-complexity process-function modules

A broader function-theory object is a finite basis whose process action closes in a small table.  `ProcessFunctionModule` is generic: it stores a basis and explicit generator action coordinates, with an optional `ProcessFrame` certificate.

For example,

\[
V_n=\operatorname{span}\{1,a,a^2,\ldots,a^n\}
\]

is a finite A/M module because

\[
A(a^k)=k a^{k-1},
\qquad
M(a^k)=k a^k.
\]

`polynomial_am_module` constructs this calibration family.

This suggests a function-theory criterion that Shakespeare can test computationally:

> a distinguished function or function family may be characterized by a small reusable process module/action table, rather than by its name in an existing special-function catalogue.

The current code only verifies declared finite modules.  Discovering low-cost modules directly from process histories is a later search problem.

## 8. Relation to other function theories

A/M should be treated as the first nontrivial concrete branch, not as the final universal answer.  Classical calibration problems are expected to force other geometries.  For example, a constrained mechanical process may reduce to

\[
y^2=P_3(x)
\]

and naturally demand a genus-one/Abelian function theory rather than an A/M weight lattice.

The long-term architecture is therefore closer to

\[
\text{process presentation}
\longrightarrow
\begin{cases}
\text{A/M function theory},\\
\text{projective function theory},\\
\text{elliptic/Abelian function theory},\\
\text{hyperelliptic function theory},\\
\cdots
\end{cases}
\]

with closure, task sufficiency, history geometry, and presentation cost deciding which language is useful for a given process.

## 9. Next tests

The next calibration sequence should separate three questions:

1. **A/M internal laws:** finite relation, commutator, PBW order, weight lattice, resonance, path history.
2. **Classical shadows:** recover logarithmic/exponential/power families as consequences of A/M process structure, without using their traditional classification as input.
3. **Competing function theories:** use pendulum, quartic oscillator, Euler top, and related examples to test whether Shakespeare discovers a different quotient geometry when A/M is not the cheapest adequate language.

That third group is especially important: failure of A/M to be optimal in a problem is useful evidence for the broader Shakespeare program, not a failure of the library.
