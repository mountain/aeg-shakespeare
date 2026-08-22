# From quotient curves to Abelian history coordinates

This note records the next layer after the genus hierarchy.  The central point is
that `genus = g` is not merely a label for a curve: it controls the dimension of
the holomorphic differential space and the rank of the first homology, hence the
shape of the global period data available to a lifted process history.

## 1. Local quotient first

Suppose a process reduction has already produced a generically smooth
hyperelliptic curve

\[
C:\qquad y^2=P(x),
\]

with genus \(g\).  Shakespeare deliberately does **not** choose a named special
function at this stage.

The first canonical analytic structure emitted by the curve is the holomorphic
differential basis

\[
\omega_k = x^k\frac{dx}{y},\qquad k=0,\dots,g-1.
\]

`holomorphic_differential_basis()` and `abelian_integral_profile()` expose this
finite structure.  They also record

\[
\dim H^0(C,K_C)=g,
\qquad
\operatorname{rank}H_1(C,\mathbb Z)=2g.
\]

These are classical invariants, not Shakespeare-specific complexity measures.

## 2. Pulling the differential back to the process

A process law gives the differential an operational meaning.  If

\[
\frac{dx}{dt}=y,
\]

then

\[
\frac{dx}{y}=dt.
\]

Thus the first Abelian integral is literally the lifted process clock.  For
higher genus the remaining canonical differentials pull back to

\[
\left(1,x,\dots,x^{g-1}\right)dt.
\]

**Shakespeare interpretation.**  The quotient geometry determines how many
natural integrated history channels become available.  This is a concrete
instance of representation dimension being forced by process geometry, but it
does not yet prove that all those channels are useful or optimal for a chosen
task.

## 3. State return versus history return

For a closed cycle \(\gamma\) on the quotient curve,

\[
P\longrightarrow P,
\]

the Abelian integral changes by

\[
\Omega_\gamma=\oint_\gamma\omega.
\]

The algebraic state has returned, while the lifted integral coordinate retains
\(\Omega_\gamma\).

**Shakespeare interpretation.**  A period can therefore be read as a history
residual left after state return.

The code does not identify this interpretation with the classical terminology;
classical mathematics supplies periods, homology, and Jacobians, while the
history-residual reading is the project's process-first viewpoint.

## 4. The symmetric pendulum as the first exact period calibration

The first pendulum vignette produces

\[
Y^2=2(E-U)(1-U^2).
\]

At \(E=0\),

\[
Y^2=2U(U^2-1).
\]

The canonical differential is

\[
\omega=\frac{dU}{Y},
\]

and the exact automorphism

\[
\sigma(U,Y)=(-U,iY)
\]

satisfies

\[
\sigma^*\omega=i\omega.
\]

A cut cycle around \([-1,0]\) has nonzero period

\[
\Omega_1 = 2\int_0^1\frac{dt}{\sqrt{2t(1-t^2)}}
=\frac{1}{\sqrt2}B\!\left(\frac14,\frac12\right),
\]

and the image cycle has

\[
\Omega_2=i\Omega_1.
\]

Hence this symmetric energy leaf has a square period lattice.  Independently,
`weierstrass_cubic_profile()` converts the cubic exactly to

\[
W^2=4X^3-g_2X-g_3
\]

with

\[
g_2=1,\qquad g_3=0,\qquad j=1728,
\]

matching the classical lemniscatic case.

This is the first executable bridge in Shakespeare from

\[
\text{process quotient}
\to
\text{holomorphic differential}
\to
\text{period history}
\to
\text{complex-torus shadow}.
\]

## 5. Higher genus and the Jacobian threshold

For the sextic oscillator quotient

\[
y^2=2E-\frac{x^6}{3},
\]

the generic genus is two.  The common Abelian layer therefore emits

\[
\frac{dx}{y},\qquad x\frac{dx}{y},
\]

and first-homology rank four.

This is the correct point to begin a later Jacobian implementation, but the
current library intentionally stops before pretending to have one.  A genuine
next stage must introduce:

1. explicit homology-cycle data;
2. analytic continuation / branch control;
3. a period matrix with numerical and/or exact certificates;
4. Riemann bilinear consistency checks;
5. an Abel--Jacobi map or Jacobian object only after those prerequisites exist.

The separation is important.  Returning `(dimension=2, homology_rank=4)` is a
classical structural fact; returning a trustworthy genus-two period matrix is a
substantially harder computational problem.

## References

- NIST DLMF §5.12, Beta Function: https://dlmf.nist.gov/5.12
- NIST DLMF §23.2, Definitions and Periodic Properties: https://dlmf.nist.gov/23.2
- NIST DLMF §23.3, Weierstrass invariants and differential equation: https://dlmf.nist.gov/23.3
- NIST DLMF §23.5, Special Lattices: https://dlmf.nist.gov/23.5
- NIST DLMF §23.19, modular invariants: https://dlmf.nist.gov/23.19
- O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981.
- H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed., Springer, 1992.
- C. McMullen, *Riemann Surfaces* course notes, hyperelliptic canonical forms:
  https://abel.math.harvard.edu/~ctm/math213b/home/course/course.pdf
- D. Mumford, *Tata Lectures on Theta I*, Birkhaeuser, 1983.
