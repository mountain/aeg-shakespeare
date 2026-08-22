# Killer calibrations and the dominance target

**Status:** research direction after `0.0.2`; two Level-1 calibrations are executable on `research/killer-calibrations`.

## 1. The four proposed application lines are ambitious, but not yet ambitious enough

KdV/solitons, collision-singular Hamiltonian systems, non-Abelian Berry transport,
and stiff multiscale dynamics are all legitimate stress tests. They share the right
failure pattern for Shakespeare: a classical local description becomes expensive
because global history, branching, topology, or scale separation is being hidden
inside continuous coordinates.

But "solve four difficult classical systems" is still an application list. It does
not yet state what would make the process-first representation program *strictly
stronger* than importing the classical solution technology problem by problem.

The stronger target is:

> **Given primitive process laws and a bounded proposal grammar, discover a compact
> global presentation in which the evolution closes by finite relations,
> translations, or certified history rewrites; make the presentation complexity
> itself distinguish integrable/regularizable systems from nearby systems for
> which no such closure is found within the same budget.**

This is a falsifiable dominance claim. It can fail because the discovery grammar is
too weak, because the correct presentation is not cheaper, because the rewrite
system is not confluent, or because nonintegrable perturbations compress just as
well as the integrable examples.

## 2. Why the current architecture is finally ready for this test

The semantic pipeline is now

```text
Process -> Presentation -> Discovery -> Analysis
```

and the relevant pieces already exist independently:

- local process generators and finite histories;
- explicit rewriting and costed presentations;
- bounded exact polynomial invariant/quotient discovery;
- A/M process function theory;
- algebraic quotient profiles and genus detection;
- square-root history lifts and branch monodromy;
- real branch-cycle grammars and intersection certificates;
- period matrices and normalized Abelian history quotients.

The missing proof of value is no longer another isolated abstraction. It is a
single problem family that forces several of these layers to compose and produces
an observable advantage.

## 3. Two Level-1 killer calibrations

### 3.1 KdV traveling wave: integrability appears as a discovered genus degeneration

For

\[
u_t+6uu_x+u_{xxx}=0,
\]

a traveling profile gives the local process

\[
D U=V,\qquad D V=cU-3U^2+a.
\]

`tests/research/test_kdv_traveling_wave_discovery.py` asks Discovery to recover,
inside a degree-three polynomial budget,

\[
I=V^2-cU^2+2U^3-2aU.
\]

Only after this first integral has been discovered is the leaf value introduced.
Exact elimination then produces

\[
Y^2=B+cX^2+2aX-2X^3.
\]

The generic quotient is genus one. The solitary-wave leaf `a=B=0` has

\[
Y^2=X^2(c-2X),
\]

so the discriminant vanishes; after normalization `W=Y/X`,

\[
W^2=c-2X,
\]

which is genus zero.

The point is not that KdV has elliptic traveling waves--that is classical. The
calibration is that the named function theory is downstream of a discovered
process quotient, and the soliton appears as a topological/algebraic degeneration
of that quotient rather than as a separately inserted formula.

### 3.2 Kepler collision: a physical singularity becomes a regular branch history

For fixed Kepler energy, Sundman time

\[
dt=r\,d\tau
\]

turns the radial dynamics into

\[
D r=Y,\qquad D Y=2Er+k.
\]

`tests/research/test_kepler_sundman_collision_branch.py` asks Discovery to recover

\[
I=Y^2-2Er^2-2kr,
\]

whose leaf value is `-ell^2`. In the radial collision sector `ell=0`,

\[
Y^2=2r(k+Er).
\]

At `r=0` the regularized algebraic curve is smooth, while physical velocity

\[
\frac{dr}{dt}=\frac{Y}{r}
\]

diverges because `dt/dtau=r` vanishes. The collision radius is nevertheless a
branch point of the projection to `r`: a closed loop around it closes in visible
radius but flips the lifted sign of `Y`.

This is the first executable instance of the proposed principle

```text
physical singularity
    -> change of process presentation
    -> regular global curve
    -> branch history carries the missing continuation data.
```

It is deliberately narrower than Levi-Civita/KS regularization of the full planar
or spatial problem, and far narrower than three-body collision dynamics.

## 4. The flagship should be KdV/finite-gap first, not three-body first

After the two Level-1 calibrations, the higher-risk flagship should be the
integrable-systems line. The reason is architectural, not historical.

KdV offers a ladder on which almost every Shakespeare layer can be forced to
participate:

```text
traveling-wave cubic
    -> genus-one quotient
    -> finite-gap spectral curve of genus g
    -> branch/cycle grammar
    -> period lattice / Abelian torus
    -> translation of the integrable flow
    -> pinched-cycle degeneration
    -> soliton sector
    -> factorized multi-soliton scattering
    -> rewrite confluence / Yang-Baxter-type consistency test.
```

The singular-Hamiltonian line is equally important, but if attacked immediately
at full three-body strength it risks spending most of the research budget on
regularization, coordinates, and numerical celestial mechanics before the
Shakespeare-specific advantage has been isolated.

KdV therefore gives the cleaner first attempt at a *system-level unification* of
process discovery, genus, branch topology, Abelian history, and rewriting.

## 5. The more aggressive target: presentation-complexity as an integrability detector

The flagship experiment should not stop at reproducing known KdV solutions. It
should include matched red teams.

For a family `P_epsilon`, compare an integrable member `epsilon=0` with nearby
nonintegrable or non-isospectral perturbations under the same proposal grammar and
budgets. Record at least:

1. invariant-discovery degree and nullity;
2. minimal closed quotient degree/genus;
3. number and complexity of branch/cycle generators;
4. rewrite length and confluence defects;
5. decoder complexity back to requested observables;
6. numerical/symbolic residual of the proposed closure;
7. total presentation cost on the existing Pareto axes.

The desired signal is not "integrable gets a smaller number" by construction.
The desired signal is a reproducible phase separation:

\[
\text{integrable / regularizable}
\longrightarrow
\text{bounded compact global presentation},
\]

while

\[
\text{matched perturbation}
\longrightarrow
\text{closure failure, genus growth, rewrite nonconfluence, or cost explosion}.
\]

If this separation survives several unrelated families, Shakespeare has something
substantially stronger than a new solver: it has an operational notion of
**representation-theoretic integrability**.

## 6. Research ladder

### Level 1 -- now executable

- KdV traveling-wave invariant discovery and genus-one/soliton degeneration.
- Sundman Kepler collision branch and physical-time singular reconstruction.

### Level 2 -- next

- KdV two- and three-soliton histories from Baecklund/Darboux/Hirota data.
- Require alternative collision/order histories to normalize to the same result.
- Extract pairwise phase shifts as history residuals rather than inserting the
  final multi-soliton formula as an atomic object.
- Add a deliberately broken interaction rule as a rewrite-confluence red team.

### Level 3 -- the first real dominance test

- Build a finite-gap genus-`g` KdV calibration from branch data through the
  existing cycle/period/Abel-Jacobi machinery.
- Represent the flow as translation on the normalized Abelian history quotient.
- Pinch selected cycles and verify that the presentation degenerates toward the
  soliton sector without changing ontology.
- Compare representation cost against a matched nonintegrable perturbation.

### Level 4 -- singular Hamiltonian generalization

- Planar Kepler with Levi-Civita presentation.
- Spatial Kepler / restricted three-body binary collision with KS-type
  regularization.
- Long-return Poincare histories across repeated near-collision passages.
- Compare topological/invariant drift against standard high-order and symplectic
  integrators, while keeping the claim boundary between exact topology and
  numerical realization explicit.

### Level 5 -- only after the common machinery survives

- non-Abelian Berry/Wilson transport near degeneracies;
- stiff reaction networks and slow-manifold presentation search.

These later lines should not force premature public abstractions. In particular,
non-Abelian gauge transport needs more than the present scalar-character/cocycle
API, and stiff multiscale reduction needs a credible discovery objective before a
slow-manifold API is justified.

## 7. Success criterion

A convincing Shakespeare result is not

> "we can express the classical answer in process language."

It is

> **"from substantially weaker prior structure, the system discovers a compact
> global representation, certifies the rewrite/topological invariants needed for
> that representation, and either computes something materially cheaper or
> exposes structure that the local continuous description hides."**

The KdV finite-gap -> soliton -> factorized-scattering ladder is currently the
best candidate for that claim. The Kepler collision test is the complementary
red team showing that the same history/branch ontology also survives a true
physical singularity.
