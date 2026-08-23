# Canonicalization mechanism closure — C1–C4

**Status:** closed calibration sequence.  
**Scope:** local canonicalization, induced observer motion, canonical decomposition, and representation-relative completion.  
**Next research line:** apply the validated mechanism to Sonnet 001.  
**API policy:** no new public abstractions are promoted by this closure.

## 1. The question this sequence answered

The working AEG Analysis hypothesis was that an original process should not be studied in an arbitrary representation path. Given primitive differential/process operations, the same physical or base solution can admit many lifts into a larger representation space. A local canonicalization should select a distinguished lift, and maintaining that local normalization should *derive* an observer ODE.

The core proposed order was

\[
\boxed{
\text{primitive process}
\to
\text{many lifts}
\to
\text{local canonicalization}
\to
\text{observer ODE}
\to
\text{canonical lift}
\to
\text{decomposition}
\to
\text{completion only if necessary}.
}
\]

C1–C4 were designed to test this order rather than to build a general API first.

---

## 2. C1 — nonautonomous Riccati

Executable essay:

```text
tests/classical/test_riccati_canonical_horizontal_lift.py
```

Merged through PR #50, squash commit `29cb2803da1aa2557f323a91a2fa0903a57abd41`.

Model:

\[
\dot x=(x-t)(x-t-1).
\]

Observer: affine chart `x=r+d y`.

Canonicalization: map the two instantaneous roots to `0` and `1`.

Differentiating the normalization gives

\[
r'=1,
\qquad d'=0.
\]

The canonical lift is

\[
\dot y=y^2-y-1.
\]

Thus explicit time dependence disappears. A simple first-order coefficient-jet count is `2` in fixed/noncanonical controls and `0` on the canonical lift.

**Evidence gained:** local canonicalization can derive a distinguished representation path with an exact representation-complexity advantage.

Routine CI evidence: run `32617310202`.

---

## 3. C2 — coupled two-register system

Executable essay:

```text
tests/classical/test_coupled_diagonal_canonical_horizontal_lift.py
```

Merged through PR #51, squash commit `270c0d55bec06645a7765d9de70df6e40b08cc45`.

Model:

\[
\dot x=e^{-2t}y,
\qquad
\dot y=e^{2t}x.
\]

Observer:

\[
u=p x,
\qquad
v=q y,
\qquad
pq=1.
\]

Canonicalization balances the two transformed cross couplings while the determinant-one condition fixes common scale gauge.

The induced observer motion is

\[
p'=p,
\qquad q'=-q.
\]

The canonical lift is

\[
\dot u=u+v,
\qquad
\dot v=u-v.
\]

Again the coefficient-jet count is `2 -> 0`.

**Evidence gained:** the C1 mechanism is not a scalar/root accident. It survives a genuine multivariable moving frame and a two-parameter normalization.

Routine CI evidence: run `32617508984`.

---

## 4. C3 — physical Kepler radial frame

Executable essay:

```text
tests/classical/test_kepler_radial_canonical_horizontal_lift.py
```

Merged through PR #52, squash commit `6ce0bb41467880b4b3bb9153c44c44ccaf0bd52b`.

Start from the planar Cartesian Kepler process and an arbitrary rotating observer. The only local normalization is radial alignment

\[
Y=0,
\qquad X>0.
\]

Maintaining it gives

\[
\dot\theta=\frac{V}{X}=\frac{h}{X^2}.
\]

The canonical frame exposes

\[
\dot X=U,
\qquad
\dot U=-\frac{\mu}{X^2}+\frac{V^2}{X},
\qquad
\dot V=-\frac{UV}{X}.
\]

Since

\[
h=XV,
\qquad
\dot h=0,
\]

the physical flow separates as

\[
\dot X=U,
\qquad
\dot U=\frac{h^2}{X^3}-\frac{\mu}{X^2},
\qquad
\dot\theta=\frac{h}{X^2},
\qquad
\dot h=0.
\]

**Evidence gained:** canonicalization can act as a genuine physical moving-frame reduction: it fixes representation freedom and separates shape dynamics from observer reconstruction without deleting physical solutions.

The first C3 CI red team found only a structural SymPy equality assertion; after replacing structural equality by an algebraic zero certificate, the unchanged mathematics passed Python 3.10–3.14.

Routine CI evidence: final run `32617857482`.

---

## 5. C4 — perturbed Kepler eccentricity frame

Executable essay:

```text
tests/classical/test_perturbed_kepler_eccentricity_canonicalization.py
```

For

\[
\dot{\mathbf r}=\mathbf v,
\qquad
\dot{\mathbf v}
=-\frac{\mu}{r^3}\mathbf r+\mathbf f,
\]

define

\[
\mathbf e
=
\frac{\mathbf v\times\mathbf h}{\mu}
-
\frac{\mathbf r}{r}.
\]

Direct differentiation gives the exact perturbation-only rate

\[
\boxed{
\dot{\mathbf e}
=
\frac{
\mathbf f\times\mathbf h
+
\mathbf v\times(\mathbf r\times\mathbf f)
}{\mu}.
}
\]

The inverse-square Kepler part cancels exactly; setting `f=0` gives `e_dot=0`.

Choose an observer whose first axis is aligned with `e`:

\[
E_\perp=0,
\qquad E_\parallel>0.
\]

If the perturbation-induced eccentricity-vector rate in this frame is

\[
G_\parallel,
\qquad G_\perp,
\]

then preserving the alignment derives

\[
\boxed{
\dot\varpi=\frac{G_\perp}{E_\parallel}.
}
\]

Therefore the same canonicalization geometry produces the local split

\[
\boxed{
F_{\rm ren}=G_\parallel,
\qquad
F_{\rm res}=G_\perp,
\qquad
F_{\rm comp}=0
}
\]

for the eccentricity-vector carrier.

At the exact calibration state

\[
\mu=1,
\quad
\mathbf r=(1,0),
\quad
\mathbf v=(0,\sqrt{3/2}),
\quad
\mathbf e=(1/2,0),
\]

with local perturbation `f=(f_r,f_t)`, the executable result is

\[
\dot e=\sqrt6\,f_t,
\qquad
\dot\varpi=-\sqrt6\,f_r.
\]

Routine CI evidence: run `32618121736`, all Python 3.10–3.14 test/build/wheel jobs passed.

**Evidence gained:** canonicalization does not only select the representation path; it can generate the distinction between shape renormalization and observer transport before completion is considered.

---

## 6. The important C4 red team: completion is relative

The C4 eccentricity-vector carrier has

\[
F_{\rm comp}=0.
\]

The earlier restricted Kepler function-module calibration, however, has a genuine second-harmonic completion:

\[
n=2\longrightarrow F_{\rm comp}\neq0.
\]

These are not contradictory. They imply the stronger methodological rule

\[
\boxed{
\text{completion is relative to the chosen representation and task.}
}
\]

A physical perturbation is not intrinsically labelled `renormalizable`, `transport`, or `completion`. Those roles are determined *after* a representation path has been canonicalized and a task/carrier has been declared.

This is also consistent with Sonnet 001, where raw solver/certificate distinctions can be strictly richer than the minimum task representation.

---

## 7. Mechanism now supported

Across C1–C4 the following sequence has independent executable support:

```text
1. Declare primitive process structure.
2. Expose representation freedom / many lifts.
3. Impose a local canonicalization using only current finite process data.
4. Differentiate the normalization to derive observer motion.
5. Evolve on the resulting canonical lift.
6. Separate shape/modulus change from observer transport.
7. Ask what residual still lies outside the chosen representation.
8. Only that residual may force representation completion.
9. Organize any resulting discrete history/completion decisions downstream.
```

The compact formula is

\[
\boxed{
\text{canonicalize}
\to
\text{transport}
\to
\text{decompose}
\to
\text{complete only the genuine residual}.
}
\]

---

## 8. What this closure does not claim

The sequence does not prove:

- a universal global optimality theorem for the canonical path;
- a universal scalar representation-complexity functional;
- existence/uniqueness of canonicalization on singular strata;
- that every useful canonicalization is an exact algebraic constraint;
- finite closure of every self-growing representation;
- representation independence of `F_ren/F_res/F_comp`;
- a universal automatic completion algorithm.

C1–C4 all remain local/bounded calibrations with explicit chart and carrier boundaries.

---

## 9. API decision

The mechanism closure validates the semantic roles of the existing narrow research surface:

```text
ProcessDirection
ConstraintCanonicalization
ObserverConnection
CanonicalDecomposition
```

It does not yet force promotion of:

```text
generic Canonicalization
CanonicalLift / HorizontalPath
Completion / ResidualQuotient
RepresentationComplexity
principal bundle / curvature / holonomy
automatic canonicalization discovery.
```

No additional public API should be created merely to summarize C1–C4.

---

## 10. Handoff to Sonnet 001

The previous Sonnet 001 sequence already established downstream mechanisms:

```text
local completion pressure
-> minimum process-generated completion
-> task objectification
-> controlled interleaving/reconvergence
-> Hauffman/history geometry
-> finite first-witness closure of the infinite contact tail
```

The canonicalization closure changes the order in which Sonnet should now be attacked. The next line must begin with

```text
A/M/contact primitive calculus
-> identify the representation/lift freedom
-> derive a local canonicalization without using the known completion/Hauffman oracle
-> derive the canonical observer/history evolution
-> compute F_ren / F_res / F_comp on that canonical path
-> only then reuse completion, objectification, interleaving and Hauffman downstream.
```

The critical question is:

> Are some of the walls/history distinctions previously managed by completion and Hauffman actually representation freedom that canonicalization should quotient first?

Existing Phase 8–10 Sonnet results are to be used as downstream truth data and red teams, not as inputs that define the new canonicalization.

`K=13` remains frozen during this representation investigation.

---

## 11. Final research status

The canonicalization mechanism-exploration line is complete enough for its intended purpose:

\[
\boxed{
\text{many lifts}
\to
\text{local canonicalization}
\to
\text{derived observer ODE}
\to
\text{canonical path}
\to
F_{\rm ren}\oplus F_{\rm res}\oplus F_{\rm comp}
}
\]

has now been calibrated across one-dimensional algebraic, multivariable algebraic, unperturbed physical, and perturbed physical examples.

Further work should resume in a new Sonnet 001 thread rather than extend the C-series.
