# Simple pendulum — complete vignette family entry

**Status:** canonical knowledge entry for the pendulum vignette family; family-level completeness audit; not a Theory Map promotion record.

This is the stable *start here* page for the simple-pendulum material in Process Geometry. The executable mathematics remains distributed across focused essays, while this page keeps the physical problem, normalization, dependency order, information loss, evidence level, reconstruction status, and open theory boundaries in one place.

The labels `P0`–`P11` are family-local navigation identifiers. They do not rename historical files and do not imply theory maturity.

---

## Retrieval

**Problem:** planar simple pendulum / mathematical pendulum.

**Domains:** classical mechanics; holonomic constraints; first integrals; algebraic curves; elliptic integrals/functions; Riemann surfaces; Abelian differentials; periods; reconstruction.

**Classical search terms:** simple pendulum, nonlinear pendulum, energy integral, elliptic curve, elliptic integral, elliptic function, genus one, Weierstrass form, Abelian differential, period lattice, reflection symmetry, local inverse.

**Process Geometry search terms:** constraint prolongation, invariant discovery, observable algebraic quotient, observer selection, structured observer proposal, quotient fiber, local branch decoder, reconstruction boundary, canonical process differential, lifted history, period residual, sampled intersection form.

**Primary executable entry:** `tests/classical/test_pendulum_process_geometry.py`.

**Theory boundary:** `docs/52-canonical-completion-hypothesis.md` is a governed T1 foundational candidate. Its stronger completion interpretation is not part of the executable pendulum facts.

**History-planning bridge:** `docs/54-pendulum-canonical-history-cost.md` records the T0 result that the marked clock form supplies a presentation-invariant edge measure only after task quotienting; it does not identify canonicalization with Huffman optimization.

---

## 1. The problem, independently stated

A point mass is constrained by a rigid massless rod of length `ell` to move in a vertical plane. Write

\[
Q=(X,Y),\qquad X^2+Y^2=\ell^2,
\]

with positive `Y` upward and gravity `-g e_y`. A Lagrange-multiplier form is

\[
\ddot Q=-g e_y+\Lambda(t)Q,
\]

with initial data satisfying

\[
Q\cdot Q=\ell^2,
\qquad
Q\cdot\dot Q=0.
\]

The classical task is to determine the motion and its global analytic structure. A textbook route introduces an angle `theta`, obtains

\[
\ddot\theta+\frac g\ell\sin\theta=0,
\]

then uses energy conservation, elliptic integrals, and elliptic functions.

The Process Geometry question is instead:

> Starting from Cartesian constrained dynamics, how much of the familiar elliptic/Abelian structure and how much of the original state can be reconstructed without taking the angle, trigonometric functions, energy formula, elliptic integral, or elliptic function as primitive input?

---

## 2. Physical variables to the executable normalization

The tests use

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
E=\frac12(v_x^2+v_y^2)+q_y,
\]

and physical time is restored by

\[
t=\sqrt{\ell/g}\,\tau.
\]

This bridge is part of the educational contract: the polynomial process in the tests is a normalized mechanical system, not the original dimensional statement.

**Current executable boundary:** nondimensionalization is documented here but is not yet a unit-aware executable derivation.

---

## 3. One family, ten stages

| Stage | Mathematical role | Primary artifact | Evidence level |
| --- | --- | --- | --- |
| **P0** | physical problem and nondimensional bridge | this guide | explanatory, not executable |
| **P1** | constraint prolongation, multiplier closure, energy verification, supplied-observer cubic | `test_pendulum_process_geometry.py` | exact symbolic |
| **P2** | discover the energy invariant and then the cubic | `test_pendulum_discovery_layer.py` | exact symbolic within declared polynomial budget |
| **P3** | compare `qx` and `qy` first-order quotient presentations | `test_pendulum_observer_selection.py` | exact quotient + declared Pareto cost |
| **P4** | generate scalar observers from `q,v,e` and a supplied pairing | `test_pendulum_structured_observers.py` | exact symbolic within declared construction grammar |
| **P5** | certify the hidden `Z2` fiber, then locally reconstruct state+flow with one branch bit | `test_pendulum_observable_quotient_fiber.py`; `test_pendulum_local_branch_decoder.py` | exact symbolic on the stated localization |
| **P6** | obtain `dU/Y`, process clock, `E=0` symmetry, Weierstrass invariants and square-lattice shadow | `test_pendulum_period_history.py` | exact symbolic at the symmetric leaf |
| **P7** | continue one explicit lifted contour and integrate a period | `test_pendulum_period_contour.py` | sampled numerical with refinement check |
| **P8** | measure two explicit periods and normalized genus-one period matrix | `test_pendulum_period_matrix.py` | sampled numerical |
| **P9** | distinguish projected crossings from surface intersections; recover symplectic orientation | `test_pendulum_cycle_intersection.py` | sampled numerical + orientation red team |
| **P10** | exact Weierstrass reduction, chord-tangent group law, Euler/Abel-Jacobi additivity, lifted clock -> geometric phase quotient, objectification red teams | `tests/research/test_pendulum_elliptic_group_rank_lowering.py` | exact symbolic on the carrier; sampled numerical for the closed-form flow |
| **P11** | lifted-clock lattice and unramified mark cover: sigma symmetry with tau = i, Jacobi period relations giving the primitive square lattice, sheet transport through q_x = 0, clock-chain kernels | `tests/research/test_pendulum_lifted_clock_global_quotient.py` | exact symbolic for the symmetry/degeneration; theorem-invoked lattice with sampled numerical certification |

The historical titles (`Discovery I/II/III`, `Pendulum II/III/IV/V`) arose at different times. `P0`–`P11` is the dependency map going forward; file names remain unchanged.

---

## 4. Core executable mechanism

Constraint prolongation gives

\[
q_x^2+q_y^2=1
\quad\Longrightarrow\quad
q_xv_x+q_yv_y=0,
\]

and preservation of tangency determines

\[
\lambda=q_y-v_x^2-v_y^2.
\]

The closed process admits

\[
I=v_x^2+v_y^2+2q_y=2E,
\]

which P2 discovers inside its declared degree-two polynomial grammar rather than receiving as a template.

On an invariant leaf the selected first-order observable is

\[
U=q_y,
\qquad
Y=DU=v_y,
\]

and exact elimination gives

\[
\boxed{Y^2=2(E-U)(1-U^2).}
\]

For `E != +/-1` this gives a smooth genus-one projective completion. Because `DU=Y`, the marked differential

\[
\omega=\frac{dU}{Y}
\]

satisfies

\[
\omega(D)=1.
\]

The family therefore follows

```text
physical constrained pendulum
  -> dimensionless Cartesian process
  -> constraint closure
  -> discovered invariant leaf
  -> structured observable proposal / selection
  -> first-order algebraic image
  -> quotient-fiber + local reconstruction audit
  -> marked carrier (C, dU/Y)
  -> lifted cycles and periods
  -> sampled period/intersection data
```

This chain does not imply that the final carrier is a unique universal normal form.

---

## 5. Information loss and local reconstruction

### 5.1 The cubic is a genuine quotient

The observable map

\[
\pi(q_x,q_y,v_x,v_y)=(q_y,v_y)
\]

is invariant under

\[
\iota(q_x,q_y,v_x,v_y)=(-q_x,q_y,-v_x,v_y).
\]

`test_pendulum_observable_quotient_fiber.py` certifies that this involution preserves the fixed-energy constrained process. It also certifies that

\[
q_x^2=1-q_y^2,
\]

\[
v_x^2=2(E-q_y)-v_y^2,
\]

\[
q_xv_x=-q_yv_y
\]

descend exactly. Thus the carrier retains hidden quadratic data but forgets the simultaneous sign of `(qx,vx)` on generic fibers.

### 5.2 One branch bit is locally sufficient

`test_pendulum_local_branch_decoder.py` takes

\[
(U,Y,E,\sigma),\qquad \sigma\in\{-1,+1\},
\]

on the open set

\[
1-U^2\neq0,
\]

and defines

\[
r=\sqrt{1-U^2},
\qquad
q_x=\sigma r,
\qquad
q_y=U,
\]

\[
v_y=Y,
\qquad
v_x=-\sigma\frac{UY}{r}.
\]

Modulo the reduced cubic these formulas satisfy rod, tangency, and energy exactly. More importantly, differentiating the cubic gives the reduced vector field

\[
DU=Y,
\qquad
DY=3U^2-2EU-1,
\]

and the decoder intertwines this flow with

\[
Dq=v,
\qquad
Dv=-e_y+\lambda q,
\qquad
\lambda=3U-2E.
\]

So away from `U=+/-1`, the missing state information is precisely one branch choice; there is no second independent velocity sign after tangency is imposed.

At `U=+/-1`, however, `q_x=0`, `Y=0` on the reduced curve, and the formula for `v_x` is `0/0`. This is an explicit chart/continuation boundary rather than an implementation accident.

The reconstruction contract is now:

```text
(U,Y,E)
  -> hidden quadratic data exactly
(U,Y,E,sigma), 1-U^2 != 0
  -> full Cartesian state and vector field exactly
vertical fibers U=+/-1
  -> require continuation / another chart / history data
```

---

## 6. Exact versus sampled evidence

### 6.1 Exact symbolic layer

The family now has exact certificates for:

- rod -> tangency;
- multiplier closure;
- energy invariance;
- bounded discovery of the energy invariant;
- Gröbner elimination to the cubic;
- generic genus one and `E=+/-1` degenerations;
- observer selection under a declared cost;
- structured proposal `pair(q,e)` under a supplied Euclidean pairing;
- hidden `Z2` quotient fiber;
- local branch decoder and reduced/Cartesian flow intertwining away from `U=+/-1`;
- at `E=0`, `dU/Y`, its pullback to the process clock, the chosen curve automorphism, and Weierstrass invariants.

### 6.2 Sampled numerical layer

The global layer demonstrates:

- square-root sheet continuation around supplied contours;
- numerical period convergence and beta-integral cross-check;
- two explicit non-collinear periods;
- normalized period ratio near `i`;
- sampled lifted intersection number `A.B=+1`;
- orientation reversal as a red team.

These are sampled numerical certificates, not rigorous interval-certified general homology/period algorithms.

---

## 7. Completeness audit

| Dimension | Current state | Remaining gap |
| --- | --- | --- |
| **Problem completeness** | dimensional problem and normalization are explicit | nondimensionalization not unit-aware/executable |
| **Exposition** | coherent family entry plus standalone proof essays | historical file numbering remains but is harmless |
| **Executability** | strong exact local/algebraic layer; sampled global layer | no rigorous general cycle/period engine |
| **Retrieval** | central index + this page + classical/Process Geometry aliases | future additions must keep the family guide synchronized |
| **Reconstruction** | locally complete with one branch bit away from `U=+/-1` | no certified branch transport through vertical fibers; no A/M-history decoder |
| **Theory relation** | executable facts separated from T1 completion hypothesis | representation-invariance / completion still open |

The key change from the first audit is that reconstruction is no longer merely “known to lose a `Z2` bit”: a local decoder and its exact domain are now executable.

---

## 8. What is deliberately not yet claimed

### 8.1 A/M lift canonicalization

The Cartesian equation admits an Addition/Multiplication reading, but the repository has not constructed canonical A/M process-space lifts, synchronized their multiplication gauge, or defined the second-order A/M jet needed to make mechanical acceleration intrinsic to that calculus.

### 8.2 Observer canonicality independent of supplied grammar

P3 chooses between `qx` and `qy`; P4 proposes `pair(q,e)`. But the Euclidean pairing, common sort, structured atoms, and presentation cost remain declared inputs. “Height is canonical” therefore requires those qualifiers.

### 8.3 Representation-invariant elliptic object

The repository has an exact observable cubic, but it does not yet prove that an independent admissible reduction produces the same marked curve, a birational model, an isogenous curve, or another declared equivalence class while preserving the process differential.

### 8.4 General-energy global analysis

Most period/intersection work specializes to `E=0`. Generic oscillatory/rotational regimes and controlled degeneration toward `E=+/-1` remain open.

### 8.5 Global reconstruction / full inversion

The family does not yet close

```text
(qx,qy,vx,vy)
  -> (U,Y)
  -> Abel clock / periods
  -> inverse process functions
  -> branch-aware global Cartesian history
```

through the vertical decoder boundary, with physical-time restoration and initial/history semantics.

### 8.6 Canonical completion theory

The larger marked-carrier -> global-completion proposal remains T1 in `docs/52-canonical-completion-hypothesis.md`. Pendulum supplies calibration evidence and explicit information-loss boundaries, not a universality theorem. The group/completion layer of that chain is now partially executable: `tests/research/test_pendulum_elliptic_group_rank_lowering.py` certifies the elliptic group law and Abel-Jacobi additivity on the carrier, while separating a lifted real clock from the geometric phase modulo its period. This is a concrete history-to-action quotient, not a canonicity claim; see `docs/54-pendulum-elliptic-group-rank-lowering.md`.

---

## 9. Next priorities

1. **Branch transport through the decoder boundary.** Specify how the local sign/chart data continue through `U=+/-1`, and distinguish state continuation from history continuation. *Partially delivered on the `E=0` leaf:* `tests/research/test_pendulum_lifted_clock_global_quotient.py` certifies the decoder degeneration at `U=+/-1` as a chart artifact (the energy identity keeps two distinct states there), the sheet transport of the Z2 mark through `q_x = 0` on the nontrivial unramified double cover, and the lifted-clock/geometric-phase quotient with the primitive period `sqrt(2) varpi`; other energy leaves and the complex global cover remain open.
2. **Cross-presentation calibration.** Compare the observable cubic with an independently derived classical reduction while tracking the differential/process clock and the exact equivalence notion.
3. **Generic-energy continuation.** Repeat cycle/period analysis away from `E=0` and through controlled degenerations.
4. **A/M mechanical bridge.** Define the second-order A/M process data needed for mechanics to arise from the calculus rather than from a post hoc reading.
5. **Full inversion.** Only after these steps should the family claim a complete process solution rather than a reduced observable function theory.

None of these priorities, by itself, requires a new Public API abstraction.

---

## 10. Reading paths

### Classical problem

1. this page §§1–4;
2. `test_pendulum_process_geometry.py`;
3. `test_pendulum_period_history.py`;
4. `test_pendulum_period_contour.py`.

### Discovery and reconstruction

1. `test_pendulum_discovery_layer.py`;
2. `test_pendulum_observer_selection.py`;
3. `test_pendulum_structured_observers.py`;
4. `test_pendulum_observable_quotient_fiber.py`;
5. `test_pendulum_local_branch_decoder.py`.

### Global topology and periods

1. `test_pendulum_period_history.py`;
2. `test_pendulum_period_contour.py`;
3. `test_pendulum_period_matrix.py`;
4. `test_pendulum_cycle_intersection.py`;
5. `docs/13-abelian-history-periods.md` through `docs/16-lifted-cycle-intersection.md`.

### Vertical axis / group law

1. `tests/research/test_pendulum_elliptic_group_rank_lowering.py`;
2. `docs/54-pendulum-elliptic-group-rank-lowering.md`;
3. the AEG analogues `docs/50-aeg-translation-objectification-rank-lowering.md` and `docs/51-aeg-addition-multiplication-rank-transition.md`.

### Lifted clock and branch locus

1. `tests/research/test_pendulum_lifted_clock_global_quotient.py`;
2. `docs/55-pendulum-lifted-clock-global-quotient.md`.

### Foundational hypothesis

Read the executable family first, then `docs/52-canonical-completion-hypothesis.md`. The T1 theory record is intentionally downstream of the calibrated facts.

---

## References

- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.
- D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and Algorithms*, 4th ed., Springer, 2015. DOI: 10.1007/978-3-319-16721-3.
- O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981. DOI: 10.1007/978-1-4612-5961-9.
- H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed., Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.
- NIST Digital Library of Mathematical Functions, Chapters 19, 22, and 23.
