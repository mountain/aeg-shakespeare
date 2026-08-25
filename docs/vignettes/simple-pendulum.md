# Simple pendulum — complete vignette family entry

**Status:** canonical knowledge entry for the pendulum vignette family; family-level completeness audit; not a Theory Map promotion record.

This is the stable *start here* page for the simple-pendulum material in Process Geometry. The executable mathematics remains distributed across focused essays, while this page keeps the physical problem, normalization, dependency order, information loss, evidence level, reconstruction status, and open theory boundaries in one place.

The labels `P0`–`P13` are family-local navigation identifiers. They do not rename historical files and do not imply theory maturity.

---

## Retrieval

**Problem:** planar simple pendulum / mathematical pendulum.

**Domains:** classical mechanics; holonomic constraints; first integrals; algebraic curves; elliptic integrals/functions; Riemann surfaces; Abelian differentials; periods; reconstruction.

**Classical search terms:** simple pendulum, nonlinear pendulum, energy integral, elliptic curve, elliptic integral, elliptic function, genus one, Weierstrass form, Abelian differential, period lattice, reflection symmetry, local inverse.

**Process Geometry search terms:** constraint prolongation, invariant discovery, observable algebraic quotient, observer selection, structured observer proposal, A/M presentation change, second-jet transport, universal history lift, unit one, dimensional resource line, fundamental domain, action-period coarea, quotient fiber, local branch decoder, task-visible continuation bit, reconstruction boundary, canonical process differential, period residual, sampled intersection form.

**Primary executable entry:** `tests/classical/test_pendulum_process_geometry.py`.

**Theory boundary:** `docs/52-canonical-completion-hypothesis.md` is a governed T1 foundational candidate. Its stronger completion interpretation is not part of the executable pendulum facts.

**History-planning bridge:** `docs/54-pendulum-canonical-history-cost.md` records the T0 result that the marked clock form supplies a presentation-invariant edge measure only after task quotienting; it does not identify canonicalization with Huffman optimization.

**A/M presentation bridge:** `tests/research/test_pendulum_am_marked_carrier_bridge.py` separates global affine A/M re-presentation from local nonlinear clock covariance, certifies the missing second-jet term for full dynamics, restores the physical time scale, and turns the Cartesian double-cover mark into an exact task-relative `1/0`-bit continuation result.

**Unit-framed history bridge:** `tests/research/test_pendulum_unit_history_fundamental_domain.py` starts again from Cartesian process data and places the unit frame, lifted clock, task-dependent fundamental domain, action-period coarea identity, elliptic quotient/readout, and `2/1/0`-bit two-sheet census in one exact audit.

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

**Current executable boundary:** the normalization is still supplied rather
than discovered, but P13 now executes the resulting time/energy/action unit
transport and its covariant family identity.

---

## 3. One family, fourteen stages

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
| **P12** | A/M effective-presentation audit: global affine marked-carrier transport, local nonlinear clock chart, required second jet, dimensional clock line, task-visible sheet memory | `tests/research/test_pendulum_am_marked_carrier_bridge.py` | exact symbolic + finite exact continuation census |
| **P13** | first-principles unit-framed history audit: universal/developing lift boundary, task-dependent fundamental domains, dimensional scale transport, action-period coarea, elliptic quotient/readout, two-sheet memory | `tests/research/test_pendulum_unit_history_fundamental_domain.py` | exact symbolic + finite exact continuation census |

The historical titles (`Discovery I/II/III`, `Pendulum II/III/IV/V`) arose at different times. `P0`–`P13` is the dependency map going forward; file names remain unchanged.

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

### 4.1 What the A/M bridge now does—and does not—say

P12 makes the relation to Addition/Multiplication precise without placing the
elliptic curve inside the A/M upper half-plane.  For a supplied scalar
presentation

\[
X=h(U),\qquad Z=DX=h'(U)Y,
\]

the marked clock is transported by

\[
\frac{dX}{Z}=\frac{dU}{Y}.
\]

For an affine A/M chart \(h(U)=sU+b\), \(s\ne0\), this is a global invertible
re-presentation of the marked cubic.  For the nonlinear A/M expression
\(h(U)=U^3\) used in the equal-clock red team, it is only a regular local chart
on the frozen negative libration interval: \(h'(0)=0\), and
\((U,Y)=(0,0)\) lies on the \(E=0\) carrier. Thus local clock/Bellman
covariance does not by itself prove global birational equivalence of elliptic
presentations.

The full reduced dynamics carry one further obligation.  Since

\[
DU=Y,\qquad DY=3U^2-2EU-1,
\]

the transformed acceleration is

\[
DZ=h''(U)Y^2+h'(U)(3U^2-2EU-1).
\]

The \(h''Y^2\) term is generically nonzero for \(h(U)=U^3\). P12 therefore
separates two facts that earlier notes left adjacent: the first-order marked
clock already transports exactly, while an intrinsic mechanical A/M lift must
also reproduce the second prolongation.  This is the concrete certificate a
future second-order `AMJet` must match.

Dimensions supply the multiplication/scale interpretation:

\[
dt=\sqrt{\ell/g}\,\omega
  =\sqrt{\ell/g}\,\frac{dX}{Z}.
\]

The dimensionless marked carrier describes shape; the physical time unit is a
scale line transported multiplicatively. Coordinate distance in either
\(U\) or \(X\) is not the physical ruler.

Finally, `U=q_y` is a selected scalar observable, not an observer-group
parameter with its own canonical ODE. A genuine moving observer would require
a task/state normalization \(N(x,g)=0\) and an induced equation from
\(DN=0\). No such normalization is discovered for the pendulum here. The
older declared A/M metric-horizontal arc remains a separate mechanism probe,
not the canonical pendulum observer.

### 4.2 Why the Bolza surface appears

The Bolza surface enters through that *separate declared metric probe*, not
through a translation between pendulum presentations.  The physical carrier
already has one square-root sheet

\[
Y^2=2(E-U)(1-U^2).
\]

Declaring the weighted A/M metric
`g_c=theta_A^2+c theta_M^2` supplies an independent oriented arc-length sheet

\[
Z_m^2=c+U^2.
\]

The two quadratic extensions form a biquadratic fiber product. Its third
quadratic quotient, with \(W=YZ_m\), is

\[
W^2=2(E-U)(1-U^2)(c+U^2).
\]

This curve is generically genus two. At the symmetric point \(E=0,c=1\), the
rescaling \(w=W/\sqrt{2}\) gives

\[
w^2=U^5-U,
\]

the affine Bolza model. Changing \(c\) moves the extra branch pair and destroys
the literal Bolza polynomial.  Its entry is therefore explained but
noncanonical: it is a special quotient of **physical sheet** \(\times\) **declared metric
sheet**, not the pendulum's state space, not an A/M chart \(X=h(U)\), and not a
mechanically forced completion.  The exact construction and its metric-weight
red team live in
`tests/research/test_pendulum_observer_metric_completion.py`; P12 records the
boundary between this construction and ordinary presentation covariance.

### 4.3 The first-principles map: lift, unit, domain, quotient, readout

P13 reverses the usual explanatory order.  The elliptic curve is not the
starting space; it is a quotient shadow downstream of measured history:

```text
Cartesian constrained process
  -> lifted history / Abel developing clock
  -> transported time and transverse-resource units
  -> stopping section and process volume
  -> task quotient, deck residual, fundamental domain
  -> marked elliptic carrier
  -> elliptic-function readout.
```

The analytic universal cover of the certified marked carrier is an exact
downstream model of this lifted clock.  It is not yet an intrinsically
discovered canonical A/M history lift.

| Concept | Pendulum expression | Role |
| --- | --- | --- |
| primitive process | `q·q=1`, `q·v=0`, `Dq=v`, `Dv=-e_y+lambda q` | physical history before the observer quotient |
| observable history jet | `U=q_y`, `Y=DU=v_y` | selected task-visible state |
| marked carrier | `Y^2=2(E-U)(1-U^2)`, `omega=dU/Y` | quotient state plus local process clock |
| lifted clock | `z=integral omega` | additive developing/history coordinate |
| period kernel | `Lambda=omega_A Z + i omega_A Z` at `E=0` | histories erased by elliptic readout |
| elliptic curve | `C_0=C_z/Lambda` | complex completed quotient geometry |
| elliptic function | `U(z)=-sn^2(z/sqrt(2),i)` | periodic decoder from lifted clock to visible state |
| natural unit one | `t0=sqrt(ell/g)`, `E0=mg ell`, `A0=E0 t0` | time, transverse energy, and action frames |
| Cartesian residual | one nontrivial `Z2` sheet | `1` bit for full continuation, `0` for carrier-only tasks |

Unit and fundamental domain are related but not identical.  The lattice cuts
the domain; the unit measures it:

\[
\Lambda_{\rm phys}=t_0\Lambda.
\]

On the real symmetric leaf the reduced carrier closes after
(`omega_A t0`), whereas the full Cartesian state closes after
(`2 omega_A t0`).  The difference is the task-visible sheet, not a change in
the local clock.

The exact continuous time/space statement is the action-period coarea identity.
With bottom-referenced (`epsilon=E+1`) and (`m=epsilon/2`),

\[
\frac{\Omega}{\mathcal A_0}
=16\left[\mathbf E(m)-(1-m)\mathbf K(m)\right],
\qquad
\frac{T}{t_0}=4\mathbf K(m),
\]

and

\[
d\Omega=T\,dH.
\]

Thus a thin action shell is one **full physical history fundamental-domain
length** times a transverse energy thickness.  The reference action unit
(`A0`) makes this dimensionless but is not a universal quantum or information
cell.  Under moving scales the correct family relation is covariant:

\[
\nabla^{\mathcal A}\Omega=T\,\nabla^E H.
\]

This is sharper than writing an unqualified (`T*S`).  The integral
(`integral S_Q(t)dt`) is the candidate general process volume; here its
continuous calibration is action/coarea, while deck-signature bits remain a
separate exact memory statement.

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

### 5.3 The branch mark is task-relative memory

P11 proves that on the real \(E=0\) loop one carrier period flips the
Cartesian sheet and two periods close the full physical state.  P12 combines
that cover with continuation equivalence. If a task observes only the carrier
\((U,Y)\), the two sheet histories have one continuation signature and require
no residual state.  If the task must reconstruct the Cartesian continuation,
the two signatures remain distinct and any exact state representation needs

\[
\left\lceil\log_2 2\right\rceil=1\ \text{bit}.
\]

This is not an entropy or runtime claim.  It is the exact finite
distinguishability lower bound for two declared tasks on the certified
nontrivial double cover.

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
- global affine A/M transport of the marked cubic and clock;
- local nonlinear clock transport together with the required second-jet correction for full dynamics;
- physical time-line scaling and the task-relative `1/0`-bit Cartesian-sheet memory result.
- the provenance of the Bolza special point as a declared-metric fiber-product quotient, together with its metric-weight dependence.
- the separation of period lattice from unit ruler, the task-dependent real fundamental domains, the covariant action-period identity, and the `2/1/0`-bit two-sheet task census.

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
| **Problem completeness** | dimensional problem, normalization, declared unit frames, their scale transport, and the action-period coarea identity are executable | discovering the normalization and a canonical flat ruler from raw A/M histories remains open |
| **Exposition** | coherent family entry plus standalone proof essays | historical file numbering remains but is harmless |
| **Executability** | strong exact local/algebraic layer; sampled global layer | no rigorous general cycle/period engine |
| **Retrieval** | central index + this page + classical/Process Geometry aliases | future additions must keep the family guide synchronized |
| **Reconstruction** | local decoder plus exact `E=0` sheet transport; the residual is `1` bit for full-state tasks and `0` bits for carrier-only tasks | generic-energy/global complex cover and an A/M-history decoder remain open |
| **Theory relation** | supplied chart covariance and the downstream lift/unit/domain/quotient/readout chain are exact and separated from the T1 completion hypothesis | canonical A/M history-lift discovery, global nonlinear equivalence, and canonical completion remain open |

The key changes from the first audit are that the `Z2` residual is now evaluated
relative to continuation tasks, and the physical ruler is no longer an
afterthought: P13 separates the lattice that cuts a fundamental domain from the
unit frame that measures it.

---

## 8. What is deliberately not yet claimed

### 8.1 A/M lift canonicalization

The Cartesian equation admits an Addition/Multiplication reading, but the repository has not constructed canonical A/M process-space lifts, synchronized their multiplication gauge, or defined the second-order A/M jet needed to make mechanical acceleration intrinsic to that calculus.

### 8.2 Observer canonicality independent of supplied grammar

P3 chooses between `qx` and `qy`; P4 proposes `pair(q,e)`. But the Euclidean pairing, common sort, structured atoms, and presentation cost remain declared inputs. “Height is canonical” therefore requires those qualifiers.

### 8.3 Representation-invariant elliptic object

The repository has an exact observable cubic.  P12 additionally proves that a
*supplied* invertible affine A/M chart gives the same marked carrier globally,
and that a supplied nonlinear chart preserves its clock on a regular local
task interval.  It still does not prove that an independently selected
observer or raw A/M history produces the same marked curve, a birational
model, an isogenous curve, or another declared equivalence class.  In
particular, local covariance under `X=U^3` is not a global-equivalence proof.

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

1. **Intrinsic history lift and ruler.** Discover, rather than supply, the pendulum history lift, unit frame, cost cocycle, and stopping semantics from a bounded A/M grammar; the Abel cover is currently a downstream calibration target.
2. **Generic-energy continuation.** Extend the certified sheet transport, fundamental-domain, and task-memory results away from `E=0`, through oscillatory/rotational regimes and controlled degenerations.
3. **Intrinsic A/M second jet.** Define second-order A/M process data and prove that it reproduces the exact `h''(U)Y^2` correction, instead of importing classical prolongation after the fact.
4. **Pendulum moving-observer discovery.** Search A/M histories for a task/state normalization `N(x,g)=0`, derive its motion from `DN=0`, and compare it with the presently selected scalar observable `U=q_y`.
5. **Independent cross-presentation and full inversion.** Derive another admissible reduction with a declared equivalence notion, then close the branch-aware map back to Cartesian history before claiming a complete process solution.

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

### A/M presentation, clock, and task memory

1. `tests/research/test_pendulum_am_marked_carrier_bridge.py`;
2. `tests/research/test_pendulum_observer_metric_completion.py` (declared
   metric/Bolza red team);
3. `docs/56-am-universal-history-recalibration.md`;
4. `docs/61-pendulum-section-reparameterization-redteam.md`.

### Unit-framed history, fundamental domain, and coarea

1. `tests/research/test_pendulum_unit_history_fundamental_domain.py`;
2. `docs/53-process-volume-frontier-coarea-hypothesis.md`;
3. `docs/56-am-universal-history-recalibration.md`;
4. `docs/62-task-covariant-complexity-coarea.md`.

### Foundational hypothesis

Read the executable family first, then `docs/52-canonical-completion-hypothesis.md`. The T1 theory record is intentionally downstream of the calibrated facts.

---

## References

- V. I. Arnold, *Mathematical Methods of Classical Mechanics*, 2nd ed., Springer, 1989. DOI: 10.1007/978-1-4757-2063-1.
- D. Cox, J. Little, D. O'Shea, *Ideals, Varieties, and Algorithms*, 4th ed., Springer, 2015. DOI: 10.1007/978-3-319-16721-3.
- O. Forster, *Lectures on Riemann Surfaces*, Springer, 1981. DOI: 10.1007/978-1-4612-5961-9.
- H. M. Farkas and I. Kra, *Riemann Surfaces*, 2nd ed., Springer, 1992. DOI: 10.1007/978-1-4612-2034-3.
- NIST Digital Library of Mathematical Functions, Chapters 19, 22, and 23.
