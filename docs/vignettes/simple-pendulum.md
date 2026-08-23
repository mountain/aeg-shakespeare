# Simple pendulum — complete vignette family entry

**Status:** canonical knowledge entry for the pendulum vignette family; family-level completeness audit; not a Theory Map promotion record.

This page is the stable *start here* entry for the simple-pendulum material in Process Geometry.  The executable mathematics remains distributed across focused tests, but the mathematical problem, normalization, stage dependencies, information loss, evidence level, and open reconstruction obligations are stated here in one place.

The family-local labels `P0`–`P9` below are navigation identifiers only.  They do not rename historical test files or imply theory maturity.

---

## Retrieval

**Problem:** planar simple pendulum / mathematical pendulum.

**Domains:** classical mechanics; holonomic constraints; first integrals; algebraic curves; elliptic integrals and functions; Riemann surfaces; Abelian differentials; periods and homology.

**Classical search terms:** simple pendulum, nonlinear pendulum, energy integral, elliptic integral, elliptic function, elliptic curve, genus one, Weierstrass form, Abelian differential, period lattice, Riemann surface, homology cycle.

**Process Geometry search terms:** constraint prolongation, invariant discovery, observable algebraic quotient, observer selection, structured observer proposal, quotient fiber, reconstruction boundary, canonical process differential, lifted history, period residual, sampled intersection form.

**Primary executable entry:** `tests/classical/test_pendulum_process_geometry.py`.

**Family theory boundary:** `docs/52-canonical-completion-hypothesis.md` is a governed T1 foundational candidate.  Its stronger completion interpretation is not part of the executable pendulum facts.

---

## 1. The mathematical problem, independently stated

Consider a point mass constrained by a rigid massless rod of length `ell` to move in a vertical plane.  Write its Cartesian position as

\[
Q=(X,Y),\qquad X^2+Y^2=\ell^2,
\]

with the positive `Y` direction upward and gravity `-g e_y`.  A Lagrange-multiplier form of the equation of motion is

\[
\ddot Q=-g e_y+\Lambda(t)Q,
\]

where the multiplier is determined by preservation of the rigid constraint.  Initial data must satisfy

\[
Q\cdot Q=\ell^2,
\qquad
Q\cdot\dot Q=0.
\]

The classical task is to determine the subsequent motion and understand its qualitative and global analytic structure.

A common textbook route introduces an angle `theta`, obtains the nonlinear scalar equation

\[
\ddot\theta+\frac g\ell\sin\theta=0,
\]

integrates the conserved energy, and reaches elliptic integrals/functions.  The Process Geometry vignette deliberately asks a different representation question:

> Starting from Cartesian constrained dynamics, how much of the familiar elliptic/Abelian structure can be reconstructed without taking the angle, trigonometric functions, energy formula, elliptic integral, or elliptic function as primitive input?

That is the question shared by the whole family.

---

## 2. From the physical problem to the executable normalization

The executable tests use dimensionless variables.  Set

\[
q=Q/\ell,
\qquad
\tau=\sqrt{g/\ell}\,t,
\qquad
v=\frac{dq}{d\tau}.
\]

Then

\[
q\cdot q=1,
\qquad
q\cdot v=0,
\]

and, after rescaling the multiplier,

\[
Dq=v,
\qquad
Dv=-e_y+\lambda q,
\qquad
D=\frac d{d\tau}.
\]

The dimensionless energy is

\[
E=\frac12(v_x^2+v_y^2)+q_y.
\]

Physical time is recovered from `tau` by

\[
t=\sqrt{\ell/g}\,\tau.
\]

This bridge matters educationally: the polynomial process used by the tests is a normalized mechanical system, not the original dimensional statement of the problem.

**Current executable boundary.**  The repository certifies the normalized equations and their consequences, but does not yet contain a unit-aware executable derivation of this nondimensionalization.

---

## 3. One family, ten stages

| Stage | Mathematical role | Primary artifact | Evidence level |
| --- | --- | --- | --- |
| **P0** | physical problem and nondimensional bridge | this guide | explanatory, not executable |
| **P1** | constraint prolongation, multiplier closure, energy verification, supplied-observer cubic | `test_pendulum_process_geometry.py` | exact symbolic |
| **P2** | discover the energy invariant and then the cubic | `test_pendulum_discovery_layer.py` | exact symbolic within declared polynomial budget |
| **P3** | compare `qx` and `qy` first-order quotient presentations | `test_pendulum_observer_selection.py` | exact quotient + declared Pareto cost |
| **P4** | generate scalar observers from `q,v,e` and a supplied pairing | `test_pendulum_structured_observers.py` | exact symbolic within declared construction grammar |
| **P5** | certify quotient fiber / hidden `Z2` state symmetry and reconstruction boundary | `test_pendulum_observable_quotient_fiber.py` | exact symbolic |
| **P6** | obtain `dU/Y`, process clock, `E=0` symmetry, Weierstrass invariants and square-lattice shadow | `test_pendulum_period_history.py` | exact symbolic at the symmetric leaf |
| **P7** | continue one explicit lifted contour and integrate a period | `test_pendulum_period_contour.py` | sampled numerical with refinement check |
| **P8** | measure two explicit periods and normalized genus-one period matrix | `test_pendulum_period_matrix.py` | sampled numerical |
| **P9** | distinguish projected crossings from surface intersections; recover symplectic orientation | `test_pendulum_cycle_intersection.py` | sampled numerical + orientation red team |

The historical module titles (`Discovery I/II/III`, `Pendulum II/III/IV/V`) arose at different times and should not be read as one coherent numbering scheme.  `P0`–`P9` is the family-level dependency map going forward; file names remain unchanged to avoid gratuitous churn.

---

## 4. The executable mechanism chain

After nondimensionalization the constraint is

\[
q_x^2+q_y^2=1.
\]

Differentiating once gives tangency,

\[
q_xv_x+q_yv_y=0,
\]

and preserving tangency determines the multiplier

\[
\lambda=q_y-v_x^2-v_y^2.
\]

The closed constrained process admits the invariant

\[
I=v_x^2+v_y^2+2q_y=2E.
\]

The discovery tests do not need this formula as a supplied invariant: within the declared degree-two polynomial grammar they recover it from the process action.

On an invariant leaf, the selected scalar observable is

\[
U=q_y,
\qquad
Y=DU=v_y.
\]

Exact elimination gives

\[
\boxed{Y^2=2(E-U)(1-U^2).}
\]

For `E != +/-1` the cubic has distinct roots and the smooth projective completion has genus one.  The process relation `DU=Y` then singles out

\[
\omega=\frac{dU}{Y},
\qquad
\omega(D)=1.
\]

Thus the Abelian integral

\[
s=\int\omega
\]

is locally the normalized process clock.  At the symmetric leaf `E=0`, the later tests continue explicit cycles on the two-sheeted curve, measure periods, assemble a normalized period matrix, and use lifted sheet history to distinguish genuine surface intersections from crossings visible only in the base `U`-plane.

This is the family’s central process-first chain:

```text
physical constrained pendulum
  -> dimensionless Cartesian process
  -> constraint closure
  -> discovered invariant leaf
  -> structured observable proposal / selection
  -> first-order algebraic image
  -> marked carrier (C, dU/Y)
  -> lifted cycles and periods
  -> sampled period/intersection data
```

No step in this chain licenses the stronger statement that the final carrier is a unique universal normal form for the original process.

---

## 5. The observable cubic is a quotient, not merely a coordinate change

The map used by the first-order carrier is

\[
\pi(q_x,q_y,v_x,v_y)=(q_y,v_y).
\]

It is invariant under

\[
\iota(q_x,q_y,v_x,v_y)
=(-q_x,q_y,-v_x,v_y).
\]

The new P5 vignette certifies that this involution preserves the closed process and the fixed-energy constraint ideal.  Consequently `pi` identifies these two states.

At the same time, the following hidden quadratic data descend exactly:

\[
q_x^2=1-q_y^2,
\]

\[
v_x^2=2(E-q_y)-v_y^2,
\]

\[
q_xv_x=-q_yv_y.
\]

So the observable carrier retains substantial hidden information but forgets the simultaneous sign of `(qx,vx)` on generic fibers.

This gives the first explicit reconstruction contract for the family:

```text
(U,Y,E)
  -> hidden quadratic data exactly
  -X-> unique full Cartesian state
```

A full decoder needs an additional branch choice or equivalent initial/history information.  Turning points and branch fibers require separate treatment.

---

## 6. What the family currently certifies

### 6.1 Exact symbolic certificates

The current exact layer covers:

- rod constraint -> tangency by prolongation;
- uniqueness of the radial multiplier in the normalized representation;
- energy invariance after constraint closure;
- bounded discovery of the degree-two invariant;
- exact Gröbner elimination to the first-order cubic;
- generic genus-one classification and detection of `E=+/-1` degenerations;
- costed selection of `qy` from `(qx,qy)` under the declared presentation cost;
- proposal of `pair(q,e)` from the declared `q,v,e` atoms and Euclidean pairing;
- the hidden `Z2` symmetry and the quadratic information that survives the observable quotient;
- at `E=0`, the differential `dU/Y`, its pullback to the process clock, the exact curve automorphism used by the square-lattice calibration, and the chosen Weierstrass invariants.

### 6.2 Sampled / numerical certificates

The later global layer additionally demonstrates:

- sheet continuation around supplied base contours;
- convergence of one period under contour refinement and agreement with an independent beta-integral value;
- two measured non-collinear periods for explicit A/B contours;
- the normalized genus-one period ratio near `i`;
- sampled lifted intersection number `A.B=+1` for the chosen contours;
- orientation reversal as a red team that flips both intersection and period orientation.

These are intentionally labelled sampled/numerical.  They are not rigorous interval-certified homology or period algorithms.

---

## 7. Completeness audit

| Dimension | Current state | Main evidence | Remaining gap |
| --- | --- | --- | --- |
| **Problem completeness** | substantially complete at family level | §1–2 plus P1 | nondimensionalization is documented but not unit-aware/executable |
| **Exposition** | strong per-file and now coherent as a family | eight historical essays + this guide | historical numbering remains visible but is neutralized by P0–P9 navigation |
| **Executability** | strong through local/algebraic layers; partial globally | P1–P6 exact, P7–P9 sampled | no rigorous general cycle/period engine |
| **Retrieval** | strong | `docs/VIGNETTES.md`, this page, classical and Process Geometry aliases | future additions must keep this entry synchronized |
| **Reconstruction** | explicitly partial | P5 quotient-fiber certificate | no branch-aware full-state decoder or A/M-history decoder |
| **Theory relation** | explicit and conservative | Theory Map + `52-canonical-completion-hypothesis.md` | representation-invariance / completion claims remain T1 research |

The important outcome is that “pendulum completeness” is no longer synonymous with “the cubic and period tests pass.”  The family has separate obligations for problem statement, information loss, reconstruction, global analytic evidence, and theory status.

---

## 8. What is deliberately *not* yet claimed

The family does **not** currently establish any of the following.

### 8.1 A/M lift canonicalization

The normalized Cartesian equation can be read in Addition/Multiplication language, but the repository has not yet constructed two canonical curves in the underlying A/M process space, synchronized their multiplication gauge, or defined a second-order A/M jet that intrinsically produces mechanical acceleration.

Therefore the current pendulum computation is still, at executable level, polynomial constrained mechanics interpreted through Process Geometry; it is not yet a complete derivation of the pendulum from A/M process curves.

### 8.2 Unique/canonical observer independent of declared structure

P3 removes the manual choice between `qx` and `qy`.  P4 goes further and proposes `pair(q,e)` from structured atoms.  But the Euclidean pairing, the common sort, and the decomposition into `q`, `v`, and `e` are still supplied.

Accordingly “the pendulum canonically chooses height” is too strong without qualifying the supplied construction grammar and cost.

### 8.3 Representation-invariant elliptic object

The repository has an exact observable cubic and classical elliptic shadows, but it does not yet certify that every admissible pendulum canonicalization produces the same marked curve, a birationally equivalent model, an isogenous curve, or some other declared equivalence class.

The object that should be compared across presentations is likely stronger than bare genus and weaker than literal polynomial equality; this remains research work.

### 8.4 General-energy global analysis

Most global cycle/period calibrations specialize to the highly symmetric `E=0` leaf.  The repository does not yet automatically construct canonical cycles or period data across generic oscillatory/rotational regimes and their degenerations.

### 8.5 Full inversion / original-state solution

The family does not yet close the loop

```text
(qx,qy,vx,vy)
  -> (U,Y)
  -> Abel clock / periods
  -> inverse process functions
  -> (qx,qy,vx,vy)
```

with branch continuation, initial-condition semantics, physical-time restoration, and a declared reconstruction guarantee.

### 8.6 Canonical completion theory

The larger proposal

```text
process quotient
  -> marked differential carrier
  -> global period data
  -> canonical group/completion layer
  -> uniformizing process functions
```

is tracked separately as T1 in `docs/52-canonical-completion-hypothesis.md`.  The pendulum supplies important evidence and boundaries, not a universality theorem.

---

## 9. Priority order for completing the family

The next work should remain conservative and should improve the mathematical object before introducing generic APIs.

1. **Branch-aware reconstruction certificate.**  Extend P5 from “one branch bit is missing” to a local decoder with explicit domain, turning-point behavior, and initial/history dependence.
2. **Cross-presentation calibration.**  Compare the observable cubic with at least one independent classical reduction while explicitly tracking the differential/process clock and the exact equivalence notion.
3. **Generic-energy continuation.**  Repeat lifted-cycle/period analysis away from the symmetric `E=0` leaf and through controlled degeneration toward `E=+/-1`.
4. **A/M mechanical bridge.**  Define the second-order A/M process data needed to make the primitive mechanical equation genuinely arise from the process calculus rather than from a post hoc reading.
5. **Full reconstruction/inversion.**  Only after the preceding steps should the family claim a complete process solution rather than a reduced observable function theory.

None of these items, by itself, requires a new Public API abstraction.

---

## 10. Reading paths

### Reader interested in the classical pendulum problem

Read:

1. this page §§1–4;
2. `test_pendulum_process_geometry.py`;
3. `test_pendulum_period_history.py`;
4. `test_pendulum_period_contour.py`.

### Reader interested in discovery / representation search

Read:

1. `test_pendulum_discovery_layer.py`;
2. `test_pendulum_observer_selection.py`;
3. `test_pendulum_structured_observers.py`;
4. `test_pendulum_observable_quotient_fiber.py`.

### Reader interested in global topology and periods

Read:

1. `test_pendulum_period_history.py`;
2. `test_pendulum_period_contour.py`;
3. `test_pendulum_period_matrix.py`;
4. `test_pendulum_cycle_intersection.py`;
5. `docs/13-abelian-history-periods.md` through `docs/16-lifted-cycle-intersection.md`.

### Reader interested in the new foundational hypothesis

Read the executable family first, then `docs/52-canonical-completion-hypothesis.md`.  Do not reverse that order: the T1 theory record is intentionally downstream of the calibrated facts.

---

## References

- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.
- D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and Algorithms*, 4th ed., Springer, 2015. DOI: 10.1007/978-3-319-16721-3.
- O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981. DOI: 10.1007/978-1-4612-5961-9.
- H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed., Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.
- NIST Digital Library of Mathematical Functions, Chapters 19, 22, and 23.
