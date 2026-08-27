# From analytic germs to Newton faces: the Bessel--Airy transition gate

**Target:** next mathematical gate for process-geometry issue #140 / PR #141  
**Status:** research-local, T1/local; no Core, Theory Map, Experimental, or
Public API promotion  
**Claim mode:** exact local symbolic certificate plus explicit unproved global
obligations  
**Compiler constraint:** no modification of the frozen S0/S1 compiler core

## 0. Result first

The bounded monomial-balance solver has a precise extension target.

For an analytic phase germ

\[
\Phi(y)=\sum_{\gamma\in S}c_\gamma y^\gamma,
\qquad c_\gamma\ne0,
\]

and a large factor \(N^\kappa\), a monomial chart

\[
y_j=N^{-w_j}\widehat y_j
\]

has a finite nonzero leading phase exactly when the retained support is an
exposed face of the Newton polyhedron with

\[
\langle\gamma,w\rangle=\kappa
\quad(\gamma\text{ on the face}),
\qquad
\langle\gamma,w\rangle>\kappa
\quad(\gamma\text{ off the face}).
\]

The equalities are the current monomial-balance equations.  The strict
inequalities, coefficient nonvanishing, analytic-tail bound, phase gauge, and
branch/domain conditions are the additional obligations needed to upgrade a
finite polynomial solve to an analytic-germ certificate.

Applied to the raw Bessel phase

\[
\phi(\theta,\delta)=(1+\delta)\sin\theta-\theta,
\qquad z=1+\delta,
\]

the critical support is

\[
\delta\theta,\qquad -\frac{\theta^3}{6}.
\]

The Newton equations recover, without an Airy name or target exponents,

\[
\theta=N^{-1/3}u,
\qquad
\delta=N^{-2/3}\xi.
\]

Moreover,

\[
N\phi(N^{-1/3}u,N^{-2/3}\xi)
=\xi u-\frac{u^3}{6}
+N^{-2/3}\left(\frac{u^5}{120}-\frac{\xi u^3}{6}\right)
+O(N^{-4/3})
\]

uniformly for \((u,\xi)\) in a fixed compact set.  After
\(u=2^{1/3}t\), the leading phase is the standard Airy phase with parameter
\(-2^{1/3}\xi\).

This is a valid **local chart-discovery certificate**.  It is not by itself a
uniform asymptotic theorem for \(J_\nu(\nu z)\): amplitude transport, contour
localization, remote-tail cancellation, the noninteger-order Schlaefli term,
and a quantitative remainder still require separate certificates.

Surreal numbers remain unnecessary in both the theorem and its executable
replay.  They continue to be a useful comparison semantics for scale windows,
but the runtime data here are finite exact integer supports, rational weights,
and analytic remainder bounds.

---

## 1. Primitive problem and task

### 1.1 Primitive data

Let \(y=(x,p)\) collect local integration/state variables
\(x\in\mathbb C^d\) and control parameters \(p\in\mathbb C^m\).  Let
\(\Phi\) be analytic on a polydisc about \(0\), after any declared
state-independent phase has either been retained separately or removed by a
task-approved phase gauge.  Write

\[
\Phi(y)=\sum_{\gamma\in\mathbb N^{D}}c_\gamma y^\gamma,
\qquad D=d+m.
\]

The support is \(S=\{\gamma:c_\gamma\ne0\}\).  Coefficients must first be
collected exactly.  Two syntactic terms with the same exponent do not define
two support points, and a coefficient that vanishes on a parameter stratum
changes the support.

The phase appears as \(N^\kappa\Phi\), with \(N\to+\infty\) and fixed
\(\kappa>0\).  The first gate asks only for a monomial chart producing a
nonconstant \(O(1)\) limiting phase.  It does not yet ask for evaluation of an
integral containing that phase.

### 1.2 Task semantics

The local discovery task is:

```text
input
  analytic phase germ and certified local domain
  large factor N^kappa
  variables permitted to approach the base point
  phase-gauge policy
  requested active monomials or bounded face search
  branch and resource budget

output
  exact rational scale weights when available
  exposed active face and normalized leading phase
  exact equality/inequality replay data
  finite-jet sufficiency and analytic-tail obligation
  typed ambiguity, inconsistency, branch, or outside-domain result
```

The stronger integral task additionally needs a contour, amplitude, endpoint
and saddle inventory, deformation semantics, and a uniform error norm.  These
two tasks must not share one unqualified `success` status.

### 1.3 Phase gauge

A monomial depending only on parameters may multiply an oscillatory integral
by a global phase.  It may be removed only if:

1. the output task is invariant under that phase; or
2. the phase is retained as a separately decoded residual.

Otherwise it participates in the scale task.  “Drop the constant term” is not
a coordinate-free rule without this task declaration.

---

## 2. Newton-face criterion

Put \(\varepsilon=N^{-1}\) and consider a positive weight vector
\(w=(w_1,\ldots,w_D)\), initially with every \(w_j>0\).  Under

\[
y_j=\varepsilon^{w_j}\widehat y_j,
\]

one has

\[
N^\kappa\Phi(y)
=\sum_{\gamma\in S}
c_\gamma\varepsilon^{\langle\gamma,w\rangle-\kappa}
\widehat y^\gamma.
\]

Define the Newton polyhedron

\[
\mathcal N(\Phi)
=\operatorname{conv}\left(
\bigcup_{\gamma\in S}(\gamma+\mathbb R_{\ge0}^{D})
\right).
\]

### Theorem 1 — exact local scale criterion

Let \(F\subset S\) be finite and nonempty.  The chart \(w>0\) makes exactly
the monomials in \(F\) survive at order \(N^0\), while every other monomial
vanishes coefficientwise on compact \(\widehat y\)-sets, if and only if

\[
\langle\gamma,w\rangle=\kappa
\quad(\gamma\in F),
\]

and

\[
\langle\gamma,w\rangle>\kappa
\quad(\gamma\in S\setminus F).
\]

Equivalently, \(F\) is the support on the compact exposed face

\[
\mathcal F_w
=\{\gamma\in\mathcal N(\Phi):
\langle\gamma,w\rangle=\kappa\},
\]

and the leading phase is

\[
\Phi_F(\widehat y)
=\sum_{\gamma\in F}c_\gamma\widehat y^\gamma.
\]

#### Proof

Each monomial carries the exact exponent
\(\langle\gamma,w\rangle-\kappa\).  A finite nonzero limit requires exponent
zero for retained terms, while a term is asymptotically absent precisely when
its exponent is positive.  A negative exponent produces a divergent phase
term and violates this particular \(O(1)\)-face task.  The equality and strict
inequality set is exactly the definition of an exposed face with normal
\(w\).  Analytic convergence on compact rescaled sets follows from the
finite-jet argument in Theorem 3 below.  ∎

### Important qualification

The theorem is task-relative.  A negative exponent may be appropriate for a
different steepest-descent task, and a term independent of state may be
factored under a declared phase gauge.  The theorem characterizes the current
compiler target: all task-active phase terms are \(O(1)\).

### Corollary 2 — monomial balance is the equality half

For a proposed face \(F=\{\gamma_1,\ldots,\gamma_r\}\), the current solver's
linear system is

\[
\Gamma_F w=\kappa\mathbf 1,
\]

where row \(i\) of \(\Gamma_F\) is \(\gamma_i\).  Solving this system proves
only the face equalities.  An analytic-germ adapter must additionally certify:

- \(w_j>0\) for every variable declared to approach the base point;
- every off-face support exponent has larger weight;
- the active coefficients are nonzero on the declared stratum;
- the unseen analytic tail cannot meet or cross the face;
- domain, phase-gauge, and branch obligations.

Thus Newton-face extraction is a strict semantic extension of bare monomial
balance, not a different numerical trick.

---

## 3. Existence, uniqueness, and finite determinacy

### 3.1 Fixed face, fixed large exponent

Let \(D=d+m\).  For a fixed proposed face and fixed \(\kappa\):

- a solution exists iff \(\Gamma_F w=\kappa\mathbf1\) is consistent and has a
  solution satisfying positivity and all off-face inequalities;
- it is unique iff \(\operatorname{rank}\Gamma_F=D\);
- if the rank is smaller, the chart is underdetermined and the result is a
  feasible polyhedron of weights, not one canonical scale;
- if the equations are inconsistent or every solution violates an inequality,
  that face is impossible.

If \(\kappa\) is not fixed, only a normal ray is meaningful.  Uniqueness up to
positive scale then requires the differences of face exponents to span a
codimension-one subspace and the corresponding positive normal cone to be one
dimensional.  The external factor \(N^\kappa\) fixes the normalization.

### 3.2 Competing faces

Several exposed faces can satisfy the declared grammar.  They may describe:

- distinct parameter regimes;
- different coalescing subsets of saddles;
- boundary versus interior scaling;
- charts related by an admitted monomial reparameterization;
- genuinely incomparable adequate presentations.

The correct result is then a finite candidate set with regime predicates and
Pareto costs, or `ambiguous_within_budget`.  Enumeration order cannot supply
canonicality.

### Theorem 3 — finite-jet sufficiency for a proposed positive chart

Assume \(\Phi\) is analytic on a polydisc and \(w_{\min}=\min_j w_j>0\).
Suppose a candidate \(w\) has been obtained from exact coefficients through
total degree \(K\), and

\[
(K+1)w_{\min}>\kappa.
\]

Then no monomial of total degree greater than \(K\) can lie on or below the
target face, because

\[
\langle\gamma,w\rangle
\ge |\gamma|w_{\min}
\ge(K+1)w_{\min}>\kappa.
\]

Consequently the degree-\(K\) jet decides all Newton equalities and
inequalities relevant to this chart.  On every compact rescaled polydisc, the
remaining analytic tail is \(o(1)\) after multiplication by \(N^\kappa\).

This gives an adaptive certification rule: propose \(w\) from a bounded jet,
then expand until \((K+1)w_{\min}>\kappa\).  If no positive lower bound on the
weights exists, finite-jet certification may fail.

### 3.3 Rationality

When \(\kappa\) and all support exponents are rational/integer and a unique
solution exists, \(w\) is rational.  Exact rational arithmetic is therefore
sufficient for the present finite Newton solve.  Irrational or logarithmic
scales arise only after the grammar or coefficient asymptotics are enlarged;
they are not forced by analytic power-series support alone.

---

## 4. Fold normal form as a Newton consequence

Let \(x\) be one state variable and \(\lambda\) one control parameter.  After
a declared phase gauge, suppose the first nonzero state term at the critical
point is \(c_mx^m\), and the first unfolding term is
\(d\lambda x^q\), with

\[
m>q\ge0,
\qquad c_m d\ne0.
\]

The two active support points are \((m,0)\) and \((q,1)\).  For a large factor
\(N\), their equations are

\[
mw_x=1,
\qquad
qw_x+w_\lambda=1.
\]

Hence

\[
w_x=\frac1m,
\qquad
w_\lambda=1-\frac qm=\frac{m-q}{m}.
\]

The ordinary fold/coalescing-saddle case has \(m=3,q=1\), giving

\[
x=N^{-1/3}u,
\qquad
\lambda=N^{-2/3}\xi.
\]

This calculation explains why the Airy exponents are structural: they are the
unique normalized positive normal to the Newton edge joining the cubic
critical term to its linear unfolding.  It does not imply that every cubic
Taylor coefficient produces an Airy **integral**; the contour and amplitude
must realize the same fold.

### Negative control — regular saddle

If the quadratic coefficient is nonzero, the active phase begins with
\(cx^2\).  The local state scale is \(x=N^{-1/2}u\).  A system that returns the
Airy \(N^{-1/3}\) scale merely because a cubic term also occurs has failed the
off-face inequality/task test.  At Bessel \(z\) bounded away from \(1\), the
relevant saddles are nondegenerate and the regular stationary-phase scale is
the correct local regime.

---

## 5. Raw Bessel calibration

### 5.1 Exact integral identity and its domain

For integer \(n\), Bessel's integral is

\[
J_n(nz)
=\frac1\pi\int_0^\pi
\cos\!\left(n(z\sin\theta-\theta)\right)d\theta.
\]

For noninteger \(\nu\) and \(|\arg z|<\pi/2\), Schlaefli's formula is

\[
J_\nu(\nu z)
=\frac1\pi\int_0^\pi
\cos\!\left(\nu(z\sin\theta-\theta)\right)d\theta
-\frac{\sin\pi\nu}{\pi}\int_0^\infty
e^{-\nu(z\sinh t+t)}dt.
\]

These are DLMF 10.9.2 and 10.9.6.  The distinction matters: the real
oscillatory integral alone is exact for integer order, while general order has
an additional endpoint-Laplace term.  DLMF 10.20 gives the established uniform
large-order Airy expansion and its turning-point coordinate \(\zeta(z)\); it
is the independent target, not a discovery input.

References:

- https://dlmf.nist.gov/10.9.E2
- https://dlmf.nist.gov/10.9.E6
- https://dlmf.nist.gov/10.20

### 5.2 Critical jet

Set

\[
z=1+\delta,
\qquad
\phi(\theta,\delta)=(1+\delta)\sin\theta-\theta.
\]

At \((\theta,\delta)=(0,0)\),

\[
\phi_\theta=0,
\qquad
\phi_{\theta\theta}=0,
\qquad
\phi_{\theta\theta\theta}=-1\ne0,
\]

and the unfolding is transverse because

\[
\phi_{\theta\delta}(0,0)=1\ne0.
\]

Thus the two stationary points born from
\((1+\delta)\cos\theta=1\) coalesce at the endpoint \(\theta=0\) when
\(\delta=0\).  The exact analytic germ is

\[
\phi(\theta,\delta)
=\delta\theta
-\frac{(1+\delta)\theta^3}{6}
+\frac{(1+\delta)\theta^5}{120}
-\cdots.
\]

The lowest relevant support points are

\[
(\theta\text{-degree},\delta\text{-degree})
=(3,0),(1,1).
\]

### 5.3 Exact scale solve

Let

\[
\theta=N^{-a}u,
\qquad
\delta=N^{-b}\xi.
\]

The cubic and unfolding terms have orders

\[
N^{1-3a},
\qquad
N^{1-a-b}.
\]

Requiring both to be \(O(1)\) gives

\[
3a=1,
\qquad
a+b=1.
\]

The exponent matrix

\[
\begin{pmatrix}3&0\\1&1\end{pmatrix}
\]

has determinant \(3\), so the normalized chart is unique:

\[
a=\frac13,
\qquad
b=\frac23.
\]

The next support points \((3,1)\) and \((5,0)\) both have weighted degree
\(5/3>1\), giving the first residual order \(N^{-2/3}\).  All later support
points lie strictly above the same Newton edge.

### 5.4 Normalized phase and replayable residual

Substitution gives, on fixed compact \((u,\xi)\)-sets,

\[
\begin{aligned}
N\phi(N^{-1/3}u,N^{-2/3}\xi)
={}&\xi u-\frac{u^3}{6}\\
&+N^{-2/3}
\left(\frac{u^5}{120}-\frac{\xi u^3}{6}\right)\\
&+O(N^{-4/3}).
\end{aligned}
\]

The order-\(N^{-4/3}\) ledger begins with

\[
-\frac{u^7}{5040}+\frac{\xi u^5}{120}.
\]

No special-function identity is needed to replay this local statement.

Using \(u=2^{1/3}t\) and the evenness of cosine, the leading phase becomes

\[
\frac{t^3}{3}-2^{1/3}\xi t.
\]

Since

\[
\operatorname{Ai}(x)
=\frac1\pi\int_0^\infty
\cos\left(\frac{t^3}{3}+xt\right)dt,
\]

the expected leading transition is

\[
J_\nu\!\left(\nu(1+\nu^{-2/3}\xi)\right)
\sim
2^{1/3}\nu^{-1/3}
\operatorname{Ai}(-2^{1/3}\xi).
\]

This last line is a calibration target supported by classical uniform
asymptotics.  The exact certificate produced here earns the chart and local
normal form, not yet the global `sim` symbol.

### 5.5 Noninteger-order residual

For real \(z>0\) and \(\nu>0\), \(\sinh t\ge t\) gives

\[
\left|
\frac{\sin\pi\nu}{\pi}
\int_0^\infty e^{-\nu(z\sinh t+t)}dt
\right|
\le
\frac1{\pi\nu(z+1)}.
\]

In the transition window \(z=1+O(\nu^{-2/3})\), this is \(O(\nu^{-1})\),
smaller than the leading \(O(\nu^{-1/3})\) Airy term.  The certificate should
retain this term rather than silently applying the integer-order formula to
general \(\nu\).

### 5.6 Relation to the established turning-point coordinate

DLMF defines \(\zeta(z)\) by

\[
\left(\frac{d\zeta}{dz}\right)^2
=\frac{1-z^2}{\zeta z^2},
\]

with \(\zeta(1)=0\).  Its local behavior is

\[
\zeta(z)=2^{1/3}(1-z)+O((1-z)^2).
\]

Therefore, for \(z=1+\nu^{-2/3}\xi\),

\[
\nu^{2/3}\zeta(z)
=-2^{1/3}\xi+O(\nu^{-2/3}),
\]

which agrees with the Airy parameter recovered from the raw phase.  This is
an independent consistency check.  It must not be embedded as a lookup rule
inside discovery.

---

## 6. Certificate boundary: chart versus integral

The local Newton/Bessel certificate proves:

1. exact critical-jet degeneracy and transverse unfolding;
2. exact support extraction through the certified jet;
3. unique rational scale weights;
4. all off-face terms lie above the active Newton edge;
5. normalized phase through a declared residual order on compact rescaled
   sets;
6. the general-order Schlaefli correction is separately bounded.

It does **not** yet prove:

1. the original contour localizes uniformly to the critical chart;
2. no other endpoint, saddle, or deformed-contour segment contributes at the
   same order;
3. the finite local interval may be replaced by the full Airy contour with a
   quantitative error;
4. amplitude zeros, poles, or branches do not change the canonical function;
5. a complex-\(z\) Stokes sector and branch convention;
6. a uniform remainder over a declared \(\xi\)-range;
7. numerical stability or net end-to-end economy.

Accordingly, the next system should expose two result types even if their
names remain research-local:

```text
local_chart_certificate
  Newton face, scales, normalized finite jet, compact residual

uniform_integral_certificate
  local certificate plus contour, amplitude, tail, sector, error, decoder
```

Passing the first must never be reported as passing the second.

---

## 7. Failure and ambiguity boundaries

An analytic-germ adapter must fail closed or stratify when any of the
following occurs.

### 7.1 Coefficient cancellation

If an active coefficient can vanish on the declared parameter set, the Newton
polyhedron changes.  Split into exact strata or return an unresolved
coefficient predicate.  Generic nonzero and identically nonzero are different
claims.

### 7.2 Zero weights and unbounded faces

If some \(w_j=0\), infinitely many powers in that variable may survive.  A
finite polynomial face is no longer justified unless the corresponding whole
analytic subgerm can be summed or retained.  Theorem 3 deliberately assumes
strictly positive weights.

### 7.3 Negative or complex weights

A negative weight moves a variable away from the local base point; the input
germ no longer certifies that chart.  Complex powers require branch data and
are outside the finite rational Newton carrier.

### 7.4 Multiple Newton faces

Multiple feasible faces are not a solver defect.  They represent multiple
regimes or an underdeclared task.  Return regimes/Pareto candidates or request
more observer information.

### 7.5 Nonanalytic and beyond-all-orders terms

Terms such as \(e^{-1/x}\), logarithmic powers, fractional branches, and
resurgent exponentials are invisible to an ordinary analytic Newton support.
They require an enlarged transseries or stratified carrier.  An analytic-germ
success has no authority over them.

### 7.6 Coordinate dependence

Newton support is covariant under declared monomial/toric changes with
transported weights.  A general analytic coordinate change can alter the
diagram and the cost of its presentation.  The singularity type may remain
equivalent while the discovered face representation changes.  No
`canonical chart` claim is earned without a specified transformation class
and uniqueness/cost theorem.

### 7.7 Integral geometry

A correct local fold can be absent from the chosen contour, canceled by
amplitude symmetry, or dominated by another saddle.  Local phase geometry
does not decide global contribution without contour/contact semantics.

---

## 8. Backend-neutral certificate semantics

A minimal analytic-germ certificate can be recorded as:

```text
AnalyticGermCertificate
  variables and base point
  parameter regime and phase gauge
  exact collected jet and coefficient predicates
  analytic domain / tail majorant or finite-jet cutoff proof
  support exponents
  proposed active face
  exact rational weights
  face equalities
  off-face strict inequalities
  rank / uniqueness result
  normalized leading germ
  residual orders and provenance
  branch/domain obligations

IntegralTransitionCertificate
  local analytic-germ certificate
  integral identity and parameter domain
  amplitude and Jacobian transport
  saddle/endpoint inventory
  contour deformation or real-tail argument
  canonical comparison integral
  uniform error norm and parameter window
  decoder and numerical evaluation contract
```

SymPy may generate or replay the polynomial identities.  The certificate
meaning is the exact support/rank/inequality/remainder data, not the return
value of `series()` or `simplify()`.

---

## 9. Surreal-number judgment

### Current result

Surreal numbers are **not runtime-necessary** for this gate.

The exact data needed are:

- integer exponent support;
- rational weight solutions;
- ordered comparisons of weighted degrees;
- analytic coefficient and tail bounds;
- explicit branch and contour data for the stronger integral task.

All of these live in ordinary exact algebra plus classical complex analysis.
The Bessel turning-point chart is recovered from a two-point Newton edge; no
surreal arithmetic appears in the proof or replay.

### Continuing semantic value

Surreal/Hahn/transseries structures remain valuable as a comparison domain
for:

- nested and incomparable asymptotic scales;
- exponentiation opening the kernel of a coarser observer;
- normal forms extending beyond analytic power-series support;
- future hyperexponential/hyperseries pressure.

The criterion for revisiting runtime necessity remains unchanged: a surreal
or hyperseries carrier must enable a theorem, certificate, or workload that a
smaller effective Hahn/transseries fragment cannot express with comparable
cost.  Vocabulary unification alone is not enough.

---

## 10. Governance disposition

### Mathematical Core

**Unchanged.**  This work refines the research-local realization of filtered
asymptotic fibres and backward task visibility.  Newton-face existence and
finite-jet sufficiency are classical local analytic facts and do not require
Core promotion.

### Research Programme

**Pressure on U1, U2, and E.**  The result gives a better-specified route from
an analytic phase to a task-visible monomial chart.  It does not establish
Arithmetic Universality, a universal calculus, or surreal necessity.

### Research Status

**Unchanged until execution.**  The Bessel derivation is the contract for an
independent-domain test.  Repository-wide status should change only after the
analytic-germ adapter discovers this chart from the frozen raw phase and the
negative/ambiguity cases behave correctly.

### Engineering Architecture

**Refine, research-local.**  Candidate generation must add collected analytic
jets, Newton inequalities, a finite-jet cutoff, coefficient strata, and typed
separation between local-chart and uniform-integral certificates.  SymPy
remains a replaceable exact backend.  No compiler core or dependency change is
made here.

### Theory Map

**Unchanged; T1/local pressure on H4 and the task-covariant evaluation
transversal.**  The scale chart is a local analytic presentation, not V2
objectification, a new process rank, or general post-manifold geometry.

### API

**No pressure.**  Even a successful Bessel execution would first support a
Sonnet extraction candidate.  It would not justify public names such as
`NewtonCompiler`, `CanonicalChart`, `SurrealScale`, or `UniformAsymptotics`.

---

## 11. Acceptance gate for the next implementation phase

The next implementation phase counts as an independent positive only if it:

1. receives the raw phase `(1 + delta) * sin(theta) - theta`, not a supplied
   cubic polynomial;
2. derives a sufficient exact jet without the words Bessel or Airy in the
   solver path;
3. collects support and proves the finite-jet cutoff;
4. returns \((1/3,2/3)\) with face equalities, inequalities, rank, and
   normalized residual;
5. rejects or changes regime for a regular Gaussian saddle;
6. reports ambiguity on a frozen competing-face case rather than selecting by
   enumeration order;
7. keeps local-chart success distinct from a uniform-integral claim;
8. compares the result against the DLMF turning-point coordinate only after
   discovery;
9. records compilation, certificate replay, residual, and repeated evaluation
   costs separately.

Until these gates pass, the S4 disposition remains **NARROW**.

---

## 12. Short retrospective

- **Does the result support the original intuition?**  Yes, narrowly.  A
  distinguished chart can be forced by the geometry of an analytic support
  face selected by the output phase task.
- **What is the real key?**  Not the Airy name and not surreal arithmetic, but
  the conjunction of exact active-face equalities, off-face inequalities, and
  a finite-jet/tail certificate.
- **What remains hard?**  Promoting local scale discovery into a uniform
  special-function evaluator requires global contour and error semantics; the
  Newton polygon does not supply them.
- **Next action:** freeze the raw analytic-germ adapter and three cases
  (Bessel fold, Gaussian negative, competing-face ambiguity) before any code
  change, then execute without altering the S0/S1 compiler core.

