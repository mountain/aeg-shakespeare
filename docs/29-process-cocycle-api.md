# ProcessCocycle: the first common central-residual API

**Status:** minimal public abstraction forced independently by Galilean mechanics and magnetic translations.

## 1. Why this abstraction enters now

The finite-family API was deliberately frozen at

\[
\texttt{ProcessFamily}
\to
\texttt{ProcessCharacter}
\to
\texttt{FamilyAction}.
\]

Galilean mechanics then exposed information that disappears under bare family
actions: the mass residual

\[
\{K,P\}=m
\]

has zero Hamiltonian vector field, while the finite response law contains a
mass-dependent affine correction.

Magnetic translations reproduced the same structural pressure in an independent
organism.  Visible planar translations still compose by ordinary addition, but
a lifted realization has an area/flux-dependent central residual and the
magnetic-translation generators satisfy

\[
\{K_x,K_y\}=-qB,
\]

again with zero Hamiltonian vector field for the central constant.

The magnetic example additionally exposed the finite composition residual
explicitly as a 2-cocycle.  Re-examining the Galilean organism shows that mass
also admits a finite Bargmann cocycle realization.  Two independent examples
therefore now require the same finite mathematical object.

## 2. The minimal object

`ProcessCocycle` attaches an additive SymPy-valued residual to one visible
`ProcessFamily`:

\[
\omega(g,h).
\]

The lifted composition represented by the object is

\[
(g,z)(h,w)
=
\bigl(gh,\;z+w+\omega(g,h)\bigr).
\]

Associativity is exactly the additive 2-cocycle identity

\[
\boxed{
\omega(g,h)+\omega(gh,k)
=
\omega(h,k)+\omega(g,hk).
}
\]

The API therefore contains only:

```text
ProcessCocycle
CocycleVerification
verify_process_cocycle(...)
central_commutator_residual(...)
```

and the `compose_lifted` method on the cocycle object.

It deliberately does **not** introduce:

- `CentralExtension`;
- cohomology classes or coboundary quotients;
- U(1) or Hilbert-space semantics;
- projective representations;
- a public Poisson/Lie algebra hierarchy;
- an automatic finite-to-infinitesimal differentiation protocol.

The central coordinate is simply additive and symbolic.  A caller may interpret
it as an action-like quantity, a phase exponent, or another residual coordinate.

## 3. Galilean calibration

Use one-dimensional Galilei parameters

\[
g=(x,v,t)
\]

with the fixed composition convention

\[
(x_1,v_1,t_1)(x_2,v_2,t_2)
=
(x_1+x_2+v_1t_2,\;v_1+v_2,\;t_1+t_2).
\]

A standard representative of the mass extension is

\[
\boxed{
\omega_m(g_1,g_2)
=
m\left(v_1x_2+\frac12 t_2v_1^2\right).
}
\]

The executable calibration verifies the cocycle identity exactly.

For a pure boost

\[
B_u=(0,u,0)
\]

and a pure spatial translation

\[
T_a=(a,0,0),
\]

the visible parameters commute, while

\[
\boxed{
\omega_m(B_u,T_a)-\omega_m(T_a,B_u)=mua.
}
\]

The mixed infinitesimal derivative is

\[
\frac{\partial^2}{\partial u\,\partial a}(mua)=m,
\]

matching the independently measured generator residual

\[
\{K,P\}=m.
\]

The particular finite cocycle representative is convention-dependent up to
coboundary; `ProcessCocycle` does not attempt to classify such equivalences.

## 4. Magnetic calibration

For planar visible translations

\[
a,b\in\mathbb R^2,
\qquad
a*b=a+b,
\]

a fixed symmetric-gauge lifted phase convention gives

\[
\boxed{
\omega_B(a,b)
=
\frac{qB}{2\hbar}(a\wedge b).
}
\]

The same generic cocycle verifier checks the exact 2-cocycle identity.  Because
visible planar translations commute,

\[
\boxed{
\omega_B(a,b)-\omega_B(b,a)
=
\frac{qB}{\hbar}(a\wedge b).
}
\]

The explicit lifted-state calculation independently verifies that this API
quantity is precisely the central phase/history discrepancy between the two
translation orders.

At generator level the calibrated symmetric-gauge realization has

\[
\{K_x,K_y\}=-qB,
\]

with zero Hamiltonian vector field for the constant residual.  The difference
of sign and the factor of \(\hbar\) between a phase-exponent convention and a
Hamiltonian-generator convention are realization choices; the public cocycle
object intentionally does not normalize them away.

## 5. What is common and what is not

The common structure is now sharply stated:

\[
\boxed{
\text{visible family composition}
+
\text{additive lifted residual satisfying the cocycle law}.
}
\]

Both examples also show a second pattern:

\[
\boxed{
\text{finite central commutator residual}
\longrightarrow
\text{infinitesimal central generator residual}.
}
\]

But the second arrow is **not yet** a public API.  Galilean and magnetic
realizations use different coordinates, dimensions, and normalization
conventions.  For now the finite cocycle is the shared public object, while the
infinitesimal bracket remains an independently certified derived realization in
each mathematical vignette.

This separation prevents the implementation from silently equating a phase
exponent with a Hamiltonian generator or from assuming that every future central
residual has a differentiable Lie-group realization.

## 6. Claim boundary

This API does not claim that every hidden process residual is cohomological, nor
that every `ProcessFamily` is a group.  It provides one small construction for a
specific repeated phenomenon: an additive central term required to retain
composition information erased by visible semantics.

Further abstraction should wait for another independent pressure.  In
particular, `CentralExtension`, cohomology classes, projective representations,
and a generic finite-to-infinitesimal bridge remain outside the current public
surface.

## References

- V. Bargmann, "On Unitary Ray Representations of Continuous Groups",
  *Annals of Mathematics* 59 (1954), 1-46.
- E. Brown, "Bloch Electrons in a Uniform Magnetic Field", *Physical Review*
  133, A1038 (1964).
- J. Zak, "Magnetic Translation Group", *Physical Review* 134, A1602-A1606
  (1964).
