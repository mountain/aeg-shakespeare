# Phase 1E results — continuum collision-adapter seam

**Status:** exact research-local algebra and obstruction passed.  The
hard-sphere continuum statements remain external theorem records.  This phase
does not prove a trace estimate, the Boltzmann--Grad limit, propagation of
chaos, or an H theorem.

**Contract:**
`09-phase1e-continuum-collision-adapter-contract.md`.

**Executable:**
`tests/research/test_hard_sphere_continuum_adapter_seam.py`.

## 1. Outcome

Phase 1E resolves the first continuum typing question in four parts.

1. The exact \(s+1\to s\) process observation is an oriented
   collision-boundary flux, not a function of the bulk \(s\)-particle state.
2. Its primitive two-process presentation is the positive gain/loss cone
   \((A,L)\).  The A/M presentation \((A,M)\), with \(M=-L/F_s\), is a derived
   division chart only where the target density \(F_s\) is positive.
3. The instantaneous finite-to-limit generator defect splits exactly into
   scaling, contact-geometry, and correlation-trace terms.  A long-time
   comparison additionally needs collision-history/recollision control.
4. Bulk \(L^1\) adaptation and collision-boundary adaptation are different
   tasks.  The former does not imply the latter without a trace theorem,
   flux topology, weak/mild formulation, or direct history estimate.

This is the continuum counterpart of the finite Phase 1C observation: an
exact present-state readout need not determine the next process jet.  It is
also a refinement of the user's proposed chart-first route.  The chart is
indeed introduced before entropy, but only after the physical collision
boundary has supplied the two positive process amounts.

## 2. Exact rational boundary shadow

The executable freezes one two-dimensional positive-flux quadrature node:

\[
v=(1,0),\qquad
u=(-1,0),\qquad
\omega=(-3/5,-4/5),\qquad
w=5/6.
\]

The raw flux is \(6/5\), so \(w(\omega\cdot(u-v))_+=1\).  The one-body
section is

\[
f(x,v)=10+x_0+2x_1+v_0^2.
\]

All evaluation uses `fractions.Fraction`; there is no floating-point tolerance
and no entropy candidate in the fixture.

### 2.1 Collision and process-jet certificates

The equal-mass collision involution gives

\[
v^*=(7/25,-24/25),\qquad
u^*=(-7/25,24/25).
\]

The executable verifies exact restoration under a second reflection and exact
conservation of pair momentum and kinetic energy.  At zero contact
displacement it then obtains

| quantity | exact value |
| --- | ---: |
| target state \(f(0,v)\) | \(11\) |
| gain \(A\) | \(39\,677\,401/390\,625=(6299/625)^2\) |
| loss \(L\) | \(121\) |
| material tangent \(A-L\) | \(-7\,588\,224/390\,625\) |
| A/M multiplicative coordinate \(M=-L/f\) | \(-11\) |

Thus \(A+fM=A-L\) exactly on the positive chart.  A separate certificate
keeps a perfectly valid gain/loss jet at \(f=0\) and rejects the A/M division.
The zero is a chart boundary, not a failure of the underlying collision flux.

### 2.2 Generator-defect certificate

For the frozen choices

\[
\epsilon=1/10,\qquad
\alpha=7/6,\qquad
(g^+_{\mathrm{tr}},g^-_{\mathrm{tr}})=(3/7,1/5),
\]

the limit section, displaced finite section, and finite source tangents are

| quantity | exact value |
| --- | ---: |
| \(K_0\sigma_0^{\mathrm{tr}}(f)\) | \(-7\,588\,224/390\,625\) |
| \(K_\epsilon\sigma_\epsilon^{\mathrm{tr}}(f)\) | \(-9\,399\,649/390\,625\) |
| \(\alpha K_\epsilon(\sigma_\epsilon^{\mathrm{tr}}(f)+g^{\mathrm{tr}})\) | \(-21\,724\,181/781\,250\) |

Every residual channel is nonzero:

| residual | exact value |
| --- | ---: |
| scaling | \(-1\,264\,704/390\,625\) |
| contact/geometric | \(-507\,199/93\,750\) |
| correlation trace | \(4/15\) |
| total finite-to-limit defect | \(-6\,547\,733/781\,250\) |

The executable certifies that the three residuals sum exactly to the total
defect.  This proves the algebra and typing of the ledger for the frozen
quadrature shadow; it proves no asymptotic bound on the continuum terms.

## 3. Exact no-go: bulk \(L^1\) is not a trace budget

For

\[
g_n(r)=\max(1-nr,0),\qquad r\ge0,
\]

the exact values are

\[
\|g_n\|_{L^1(\mathbb R_+)}=\frac1{2n}\longrightarrow0,
\qquad g_n(0)=1.
\]

The test instantiates \(n=2,4,8,16\), producing bulk masses
\(1/4,1/8,1/16,1/32\) while every boundary value remains one.  In the normal
coordinate to a hard-sphere contact surface this rejects the inference

\[
\text{bulk }L^1\text{ convergence}
\Longrightarrow
\text{collision-boundary or generator convergence}.
\]

This no-go is task-specific.  It does not contradict an \(L^1\) convergence
theorem for bulk correlations.

## 4. Calibrated reading of Deng--Hani--Ma

Theorem 1 of Deng--Hani--Ma supplies, under its hypotheses and over the
regular Boltzmann lifespan, a uniform bulk \(L^1\) comparison between the
rescaled hard-sphere correlations and the excluded factorized Boltzmann
family, for \(s\le|\log\epsilon|\).  Phase 1E records this as an **external
state-adapter theorem**.  It does not silently promote it to a pointwise
collision-boundary estimate.

The proof's partial time expansions, cumulants, layered collision histories,
molecules, cutting, and truncation estimates address the continuation task at
a richer semantic level than one bulk norm.  The process-geometry reading is:

| proof content | adapter role | claim grade |
| --- | --- | --- |
| bulk correlation estimate | state/readout adequacy | external theorem |
| BBGKY contact operator | boundary process observation | exact classical contract |
| cumulants and molecules | retained connected/history structure | typed interpretation |
| cutting identity | compositional proof/cost certificate | external proof device |
| one fixed-order A/M jet | complete long-horizon decoder | rejected/unclaimed |

In particular, a molecule is not promoted to a higher arithmetic-rank object:
it retains collision graph, order, and layer information, but its lowering,
free grammar, and all-composite semantics have not been established.

## 5. Executed certificates

Six exact tests pass:

1. elastic reflection is an involution and preserves the collision rulers;
2. the oriented boundary flux gives a nonnegative gain/loss cone;
3. the A/M chart is exact on positive states and singular at zero;
4. the three generator-defect terms sum to the total defect;
5. vanishing bulk \(L^1\) mass can retain a fixed boundary trace;
6. bulk state, boundary jet, positive chart, and history tasks remain
   separately graded.

The focused direct run retains all 11 finite Phase 1C chart-first certificates
alongside the six new Phase 1E certificates.  The complete repository suite is
left to CI because the local runtime lacks its declared `pytest` and `sympy`
dependencies.  No new dependency or public interface is introduced.

## 6. Claim boundary

The phase has earned:

- an exact formula-level contract for the collision-boundary observation;
- an exact positive \((A,L)\) process cone and conditional A/M chart;
- an exact algebraic defect decomposition;
- an exact obstruction to a bulk-only trace claim;
- a theorem-scoped, task-typed reading of the modern long-time derivation.

It has not earned:

- existence or boundedness of continuum traces for arbitrary \(L^1\) data;
- convergence of the BBGKY generator to the Boltzmann generator;
- an independent proof of the Deng--Hani--Ma theorem;
- a microscopic decoder, semantic equivalence, or full-future A/M state;
- a new H theorem or a higher arithmetic rank.

## 7. Next gate

The next research step is deliberately narrower than “prove H again.”

1. Replace the unsafe pointwise-generator target by a weak observable or
   mild time-integrated flux target whose topology is explicit.
2. Freeze one collision-history continuation cell from the Deng--Hani--Ma
   expansion and type its source payload, cut/composition law, target
   observable, error budget, and forgotten data.
3. Show on that cell how a boundary flux is recovered from history without
   pretending that bulk \(L^1\) convergence supplied a trace.
4. Reopen the H/Lyapunov search only after the autonomous Boltzmann target,
   its time orientation, and validity horizon have been fixed.

This will test the proposed replacement of strict semantic equivalence by
layer-wise semantic adaptation at the hardest current seam: not state
readout, but continuation through collisions.

## 8. Repository effect

### Mathematical Core

Refinement pressure only.  The existing task-relative adapter language can
express the new three-way split.  No stable Core change follows from one
kinetic calibration.

### Engineering Architecture

Research-local refinement.  Boundary flux is recorded separately from bulk
state norms, and gain/loss precedes division-based A/M coordinates.  No API or
backend is promoted.

### Theory Map

Unchanged.  The result strengthens the emerging adaptation transversal and
sharpens its failure semantics, without adding a new edge, axis, or rank.
