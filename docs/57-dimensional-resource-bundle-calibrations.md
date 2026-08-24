# Dimensional resource bundles — five-problem calibration

**Status:** T0 executable research note; follows the AM universal-history
recalibration; no Theory Map or API promotion.

## 1. Target

The current candidate structure is

\[
\mathfrak P_T=
(\widetilde{\mathcal H},C,\mathcal R,\nabla,\rho,O_T,\lambda_T,\Sigma_T),
\]

where the universal history lift carries a dimensional resource bundle
(\mathcal R\), observer/unit transport (\nabla), an additive resource
cocycle (\rho), a task dual (\lambda_T), and a stopping section
(\Sigma_T).

This note asks whether the components do real work in the existing examples or
merely rename familiar quantities.  Four previous examples are recalculated,
then an independent state-local-clock problem tests the covariant Bellman
equation directly.

## 2. Pendulum — exact shape/scale typing

For mass (m), length (\ell), and gravity (g),

\[
E_0=mg\ell,
\qquad
t_0=\sqrt{\ell/g},
\qquad
\mathcal A_0=E_0t_0.
\]

The test verifies the dimensional identities

\[
[E_0]=ML^2T^{-2},
\qquad
[t_0]=T,
\qquad
[\mathcal A_0]=ML^2T^{-1}.
\]

The reduced variables and marked differential are dimensionless:

\[
U,\ Y,\ \epsilon,\ \omega=\frac{dU}{Y}.
\]

Physical quantities are sections of scale lines:

\[
dt=t_0\omega,
\qquad
d\mathcal A=\mathcal A_0\,dV.
\]

This supports the shape/scale split.  It does not yet derive (t_0) or
(\omega) from unrestricted AM discovery.

## 3. Hard particles — two resource dimensions, not one clock

First-hit time and comparison depth are different resource types:

\[
\rho(\gamma)=
(T_{\mathrm{physical}},N_{\mathrm{query}}).
\]

One policy may produce an earlier physical answer using more comparisons;
another may use fewer comparisons but wait longer.  Neither dominates.

A scalar objective requires a dimensional exchange rate

\[
J_T=T_{\mathrm{physical}}+lambda_qN_{\mathrm{query}},
\qquad
[\lambda_q]=T/\mathrm{query}.
\]

The exact calibration gives task weights for which each policy wins.  The
canonical output is therefore the resource frontier; scalar Bellman value is
observer/task relative.

## 4. Translation objectification — ruler renormalization

Objectifying a repeated translation changes runtime depth but incurs compilation
and storage:

\[
C_{\mathrm{new}}(N)
=C_{\mathrm{compile}}
+N C_{\mathrm{run}}
+\lambda_s C_{\mathrm{store}}.
\]

The executable example has raw runtime three, objectified runtime one,
compilation cost eight, and two storage units.  With the declared storage/time
exchange rate, objectification loses for one use and wins only from five uses.

Thus objectification is not free shortening of the history tree.  It changes
the primitive ruler under a workload-dependent amortization law.

## 5. Abelian periods — dual pairing resolves the basis obstruction

The previous note showed that the same lattice displacement has coordinate
vectors

\[
c=(0,1),
\qquad
c'=(-1,1)
\]

in standard and sheared bases, with naive word lengths one and two.

The new calculation retains a resource vector and transports the task dual
contragrediently.  For basis matrix

\[
B'=\begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

and physical dual (\lambda=(2,3)),

\[
\lambda'=B'^T\lambda=(2,5).
\]

Then

\[
\lambda^Tc=(\lambda')^Tc'=3.
\]

The scalar task value is basis invariant even though naive coordinate length
is not.  This is positive evidence for

\[
\text{canonical resource vector}
+
\text{transported task dual}
\]

rather than a universal scalar metric.

## 6. State-local clocks — direct Bellman red team

Consider a shortest-arrival problem with root and intermediate states using
different local clock units.  The physical alternatives cost

```text
direct       5 time units
via middle   1 + 2 = 3 time units.
```

If one root numeric unit represents two physical units while one middle numeric
unit represents one half physical unit, the naive recursion compares

```text
direct       5/2
via middle   1/2 + 4 = 9/2
```

and chooses the wrong route because the summands live in different fibers.

Let (P_{y\to x}:\mathcal R_y\to\mathcal R_x) transport clock values.  The
covariant recursion is

\[
V(x)=\inf_a\left[
c_x(a)+\sum_y p(y\mid x,a)P_{y\to x}V(y)
\right].
\]

It compares

```text
direct       5/2 root units
via middle   1/2 + 1 = 3/2 root units
```

and recovers the physical optimum.  Independently changing both local gauges
changes the numeric values but preserves the chosen path and reconstructed
physical arrival times.

This is the first executable case in which observer/unit transport is required
for Bellman correctness rather than added as an interpretation afterward.

## 7. Independent physical calibration — discrete optical arrival

A short path through a slow medium competes with a longer path through a fast
medium.  Geometric length chooses the short path, while optical time

\[
T=\sum_e\frac{n_eL_e}{c}
\]

chooses the longer path.  Changing meters to centimeters scales (L) and
(c) together and leaves travel time and the optimal policy unchanged.

This separates curved/nonuniform state geometry from the transported process
ruler.  Bellman requires the latter, not a flat physical coordinate space.

### 7.1 Fermat calibration: from path comparison to variation

The discrete comparison alone does not verify Fermat's principle.  For two
homogeneous layers, parameterize a broken ray by its interface crossing (x):

\[
\mathcal L(x)=n_1\sqrt{x^2+a^2}
 +n_2\sqrt{(D-x)^2+b^2}.
\]

The executable choice (a=4), (b=12), (D=8), (n_1=25), (n_2=39) has the exact
stationary crossing (x=3), since

\[
n_1\sin\theta_1=25\frac35=15
=39\frac5{13}=n_2\sin\theta_2.
\]

Thus Fermat stationarity gives Snell's law.  Moreover,

\[
\mathcal L''(x)=
\frac{n_1a^2}{(x^2+a^2)^{3/2}}
+\frac{n_2b^2}{((D-x)^2+b^2)^{3/2}}>0,
\]

so in this positive, single-interface setting the stationary ray is the unique
global minimum.  This convexity clause matters: Fermat's general principle is
stationary optical length, and caustics or conjugate points can produce maxima
or saddle rays.

For a smooth refractive index, varying

\[
\mathcal L[\gamma]=\int n(\gamma)\lVert\dot\gamma\rVert\,du
\]

gives, in Euclidean arclength,

\[
\frac{d}{ds}(nT)=\nabla n.
\]

The test verifies this equation with an exact rational local jet in a graded
medium.  Equivalently, rays are geodesics of the optical metric
(g_{\mathrm{opt}}=n^2g), while physical travel time is
(T=\mathcal L/c).  Positive reparameterization leaves (\mathcal L) invariant;
changing length units scales both optical length and (c), leaving travel time
unchanged.

This sharpens the resource-bundle interpretation: the canonical path cost is
not bare geometric length but the additive optical cocycle (n\,ds), paired with
the clock conversion (1/c).  Bellman composition and Fermat variation are the
discrete and continuous optimization faces of the same transported ruler.

## 8. Cross-problem verdict

| Problem | Carrier | Resource bundle | Transport/scalarization result |
| --- | --- | --- | --- |
| pendulum | elliptic observable quotient | time and action scale lines | shape/scale typing succeeds |
| hard particles | collision-time/argmin carrier | physical time × query count | Pareto frontier precedes scalarization |
| translation | net-displacement quotient | compile × run × storage | objectification is amortized ruler change |
| Abelian periods | additive lift / period quotient | lattice resource vector | transported task dual restores covariance |
| local-clock/optics | arrival graph / optical metric | local time fibers / optical-length cocycle | transport repairs Bellman; Fermat gives its continuous variation |

The examples coordinate with the proposed framework at distinct interfaces.
Together they support a stronger statement than analogy:

\[
\boxed{
\text{Bellman values are naturally sections of a resource bundle; ordinary
scalar Bellman assumes a chosen global trivialization.}
}
\]

## 9. Remaining gaps

The calibration does not yet establish:

1. that AM discovery can construct the resource bundle and transport rather
   than receive them as declared data;
2. that the observer connection already in the repository is the same
   connection needed for resource transport;
3. a generic rule for choosing task duals or preserving Pareto structure;
4. treatment of nontrivial curvature/holonomy in the resource connection;
5. continuous convergence from finite Hauffman trees to the covariant Bellman
   equation;
6. a representation-invariant accounting law for learned/objectified
   primitives across changing workloads.

The next decisive example should therefore contain nontrivial resource
holonomy, not merely different local units related by a flat gauge.  Until such
an example is calibrated, connection covariance is supported but curvature
remains interpretive.

That next probe is carried out in
`58-noether-canonicalization-and-history-payloads.md`.  Magnetic and Berry
examples show that nontrivial holonomy exists but need not itself be an ordered
cost; this refines the primitive object from a resource bundle to a more general
bundle of task-evaluated history payloads.

## 10. Governance

```text
Epistemic maturity: T0
Role: cross-problem dimensional calibration
Theory Map Change: none
Experimental/Public API pressure: none
```
