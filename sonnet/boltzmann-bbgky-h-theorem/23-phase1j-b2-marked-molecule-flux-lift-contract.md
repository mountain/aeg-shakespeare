# Phase 1J-B2 contract — fixed-molecule marked collision-flux lift

**Status:** frozen and executed as a local operator contract.

**Parent question:** Phase 1J-B asks whether the Deng--Hani--Ma molecule
expansion can be lifted from bulk cumulant control to a collision-event
response measure.  This B2 gate isolates the first operation in that lift:
insert one root-visible collision mark into one pre-cut molecule integral.

**Dependency firewall:** Phase 1J-B2 is independent of Phase 1J-A.  It uses no
finite collision-response conclusion from that branch.  The only inputs are
elementary signed-measure facts and explicitly cited structure from the
continuum molecule paper.

## 1. Primary-source seam

The source is Y. Deng, Z. Hani and X. Ma,
[*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://arxiv.org/abs/2408.07818).
The following pieces are used, with no stronger interpretation:

| Source object | Use in this contract | Excluded interpretation |
| --- | --- | --- |
| Definitions 3.1 and 3.17 | a pre-cut molecule contains typed collision (C) and overlap (O) atoms; C-atoms prescribe collisions | every atom is a physical current event |
| Definitions 3.22--3.23 | prescribed dynamics and its integral retain the variables on which an event observable can depend | an already integrated bulk quantity determines the event history |
| Equation (7.6) | \(I_M(Q)\) is an integral against positive collision kernels and a possibly signed amplitude \(Q\) | the signed amplitude is itself a probability density |
| Equations (7.7)--(7.8) | \(I_M(|Q|)\) is the natural absolute-integral majorant | it already estimates a marked flux sum |
| Proposition 8.14 | a cut is an exact iterated-integral identity | cut pieces are independent physical histories |
| Propositions 7.2 and 8.18 | molecule/operation counts are explicit and polylogarithmic on the admitted class | their unmarked estimates automatically survive marking |

The mark must be attached before cutting, while the pre-cut prescribed
dynamics still identifies the collision variables.  After a cut, the mark is
only a multiplicative observable in the relevant iterated integral.

## 2. Objects and eligibility

Fix one pre-cut molecule \(M\), signed amplitude \(Q\), and a root particle
line.  Let

\[
\mathcal C_{\rm root}(M)
=\{n:\ n\text{ is a C-atom incident to the root line}\}.
\]

O-atoms and C-atoms joining only non-root particle lines are ineligible.  For
each \(n\in\mathcal C_{\rm root}(M)\), the prescribed collision variables
define a measurable event map

\[
e_n:\Omega_M\longrightarrow\Sigma_T^\epsilon,
\]

where the target records the declared time/layer, root line, collision
channel, state cell and orientation.  Let the signed molecule measure be

\[
d\lambda_M^Q=Q\,d\mu_M,
\]

where \(d\mu_M\) contains the nonnegative kernel and integration factors from
\(I_M\).  The one-mark current is the pushforward

\[
\kappa_{M,n}:=(e_n)_\#\lambda_M^Q.
\]

This is a research-local object.  It is not yet identified with a hard-sphere
boundary trace or the full current \(J_T^\epsilon\) of Phase 1F.

## 3. The fixed-molecule theorem target

### 3.1 One-mark contraction

For every bounded measurable test \(\psi\), require

\[
\langle\kappa_{M,n},\psi\rangle
=I_M(Q\,\psi\circ e_n)
\]

and

\[
|\langle\kappa_{M,n},\psi\rangle|
\le \|\psi\|_\infty I_M(|Q|),
\qquad
\|\kappa_{M,n}\|_{\rm TV}\le I_M(|Q|).
\]

This follows only from pushforward duality and contraction of total variation.
It does not use a new molecule estimate.

### 3.2 Aggregate local mark cost

For a fixed molecule,

\[
\left\|\sum_{n\in\mathcal C_{\rm root}(M)}\kappa_{M,n}\right\|_{\rm TV}
\le |\mathcal C_{\rm root}(M)|I_M(|Q|)
\le |M|I_M(|Q|).
\]

The mark therefore adds at most a linear atom-count factor before the global
molecule sum.  This statement is sharp at the level of available information:
if the unmarked gain is only reciprocal in the eligible mark count, the
marked budget need not vanish.

### 3.3 Covariance under a cut

If Proposition 8.14 writes \(I_M=I_{M_1}\circ I_{M_2}\), apply it to the
already marked amplitude \(Q\psi\circ e_n\).  The observable remains in the
component containing \(n\), and exact Fubini equality must hold.  No claim of
physical composition, independence, or post-cut reconstruction is admitted.

## 4. Test-class ladder

The B2 contract distinguishes three targets that must not be conflated.

| Test class | Norm or topology | Role |
| --- | --- | --- |
| all \(\|\psi\|_\infty\le K\) | \(K\) times total variation | strongest bounded mark target |
| declared H-adapted family \(\Psi_K\) | family-specific dual seminorm | sufficient candidate for clipped entropy transfer |
| smooth/cylinder weak-flux tests | Phase 1F weak topology | event-measure convergence target |

The first implies the latter two when the tests are included; the converse is
false.  In particular, stating a supremum over the full bounded ball silently
asks for total-variation convergence, not merely weak collision-flux control.

## 5. Conditional absorption and kill condition

On the admitted molecule class, the source paper bounds molecule sizes and
operation sequences by fixed polylogarithmic factors.  A positive power gain
can asymptotically absorb a fixed polylogarithmic mark cost.  B2 records this
only as the conditional arithmetic pattern

\[
|\log\epsilon|^a\epsilon^b\to0\qquad(b>0).
\]

It does not assert that every molecule and error category retains a uniform
positive power \(b\) after marking.

The next analytic gate fails if any required subcase has only a reciprocal
atom-count gain, loses the source paper's positive \(\epsilon\)-margin, or
cannot retain the pre-cut event map through its operation sequence.  Such a
failure must be stored explicitly rather than hidden in a formal H identity.

## 6. Executable obligations

The exact rational certificate must check:

1. only root-visible C-atoms are eligible;
2. pushforward pairing equals direct observable insertion;
3. one-mark total variation is bounded by \(I_M(|Q|)\);
4. pre-cut marking commutes with outer and inner Fubini cuts;
5. aggregate local cost is at most linear in the eligible atom count;
6. an unmarked cut value cannot reconstruct the collision-event pairing;
7. the full bounded test ball detects total variation while a smaller cylinder
   algebra may not;
8. a fixed polylogarithmic mark count is absorbable only conditionally on a
   positive power margin;
9. reciprocal unmarked mass is a red-team obstruction; and
10. the global molecule sum, flux identification, log tail, chain rule, H
    theorem and generic API remain unearned.

The executable is
[test_marked_molecule_flux_lift.py](../../tests/research/test_marked_molecule_flux_lift.py).

## 7. Claim ceiling

Passing B2 earns a **fixed-molecule one-mark operator lemma** and a precise
location for the next missing theorem.  It does not earn:

- a marked analogue of the global cumulant/molecule estimates;
- summability over molecules, cuts, deletions or splitting cases;
- identification with the actual hard-sphere collision current;
- removal of clipping or logarithmic tail control;
- an entropy chain rule or continuum/microscopic H theorem;
- a new Core theorem, Theory Map object or public API.

The expected pressure is research-level U4/E: the fixed molecule exposes an
event observable and its cost.  No U5 objectification is warranted.
