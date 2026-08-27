# Phase 1J-B4 contract — signed-current identification audit

**Status:** frozen and executed as a source-compatibility audit plus a
conditional exact identification schema. The physical current identity does
not pass this gate.

**Parent question:** Phase 1J-B3 constructed an absolutely summable formal
family of marked signed molecule measures. B4 asks whether that family is
already the collision current of the hard-sphere dynamics.

**Executable owner:**
[test_signed_collision_current_identification.py](../../tests/research/test_signed_collision_current_identification.py).

**Result owner:**
[28-phase1j-b4-signed-current-identification-results.md](./28-phase1j-b4-signed-current-identification-results.md).

## 0. Dependency and claim firewall

B4 uses only the continuum branch 1E--1J-B3. Phase 1J-A/C2 supplies no
continuum evidence. B3 supplies absolute total-variation summability of a
formal marked family, but not its semantic identification.

This phase distinguishes three levels:

1. an endpoint transport or cumulant identity;
2. a path-resolved signed identity retaining collision times and atoms; and
3. the oriented event current obtained by marking those paths.

The first does not imply the second or third. Positive domination proves none
of the equalities.

## 1. Primary-source audit

The source is Deng--Hani--Ma,
[*Long time derivation of the Boltzmann equation from hard sphere dynamics*](https://arxiv.org/abs/2408.07818),
version 3. B4 found more exact signed structure than the statement of
Proposition 3.25 alone displays, but also located the remaining break.

| Source statement | Exact grade used here | What remains absent |
| --- | --- | --- |
| Proposition 4.5 and Proposition 4.7 | the extended and truncated dynamics are path-defined; on the truncated domain they have exactly the same collisions | a current estimate on the complementary error domain |
| Proposition 5.10, equations (5.17), (5.29)--(5.30) | exact one-layer signed Penrose expansion of endpoint transport, with sign \((-1)^{|M|_O}\) | the same equality after inserting a collision-count observable |
| Proposition 5.16 proof, equations (5.62)--(5.63) | exact signed formula for \(E_{H_\ell}\) before the displayed positive bound (5.44) | a physical event-current interpretation of that endpoint function |
| Proposition 7.5, equations (7.13)--(7.15) | the atom integral equals the prescribed collision/overlap indicator; the C-atom calculation fixes collision time, outgoing state and the pre-collisional sign of the kernel | a sum over marked Penrose terms equal to the current of the truncated dynamics |
| Proposition 3.25 and Section 5.6 | positive molecule domination and global state-error estimates | signed weak-pairing equality or current-valued residuals |
| equations (5.45)--(5.46), (3.19)--(3.20) | state-function or \(L^1\) error bounds for \(\mathrm{Err}_1,\mathrm{Err}_2\) and the terminal error | collision-event measures representing those errors |

Equation (5.63) corrects an overly conservative B3 reading: an exact signed
endpoint formula for the cumulant does exist inside the proof. This is real
progress, but it is still an endpoint formula.

Equation (7.15) is also stronger than a generic bulk integral bound. For one
C-atom it is a local collision evaluation identity. It permits a marked term
to be defined. The paper does not state or prove that marking commutes with
the global Penrose decomposition of the truncated transport.

## 2. Common oriented event space

Fix a root-label set \(H\), one time layer, and the truncated dynamics. All
currents must live on one measurable space

\[
\Sigma_{H,\ell}^{\epsilon}
=\{(t,\mathrm{channel},z_{\rm in},z_{\rm out},\sigma)\},
\qquad \sigma\in\{\mathrm{gain},\mathrm{loss}\}.
\]

A physical collision contributes its outgoing event with sign \(+1\) and its
incoming event with sign \(-1\). The sign
\((-1)^{|M|_O}\) belongs to the Penrose coefficient and is independent of
this gain/loss orientation. Erasing either sign is forbidden.

For a path measure \(\widehat\mu\) retaining its collision list, let

\[
\operatorname{Cur}_H(\widehat\mu)
\in\mathcal M(\Sigma_{H,\ell}^{\epsilon})
\]

be the linear pushforward obtained by summing every root-visible collision as
gain minus loss. This operator is defined on path-resolved measures, not on
their endpoint marginal alone.

## 3. The missing marked Penrose identity

For a signed Penrose molecule \(M\) and root-visible C-atom
\(n\in\mathcal C_H(M)\), Proposition 7.5 supports the term-level current

\[
\kappa^{\mathrm{Pen}}_{M,n}
=(e_n)_\#\lambda^{\mathrm{Pen}}_M.
\]

The B3 formal current is

\[
\mathfrak K_{H,\ell}^{\epsilon}
=\sum_{[M]}\sum_{n\in\mathcal C_H(M)}
\kappa^{\mathrm{Pen}}_{M,n},
\]

and its absolute total-variation convergence is already earned.

The new theorem required for identification is not another summability
estimate. It is the bounded weak-pairing identity

\[
\boxed{
\langle J_{H,\ell}^{\Lambda,\Gamma},\psi\rangle
=
\sum_{[M]}\sum_{n\in\mathcal C_H(M)}
\langle\kappa^{\mathrm{Pen}}_{M,n},\psi\rangle
+\langle r_{\mathrm{Pen}},\psi\rangle
}
\]

for every declared bounded event test \(\psi\), where
\(J_{H,\ell}^{\Lambda,\Gamma}\) is obtained from the path-resolved truncated
dynamics and \(r_{\mathrm{Pen}}\) is an explicitly constructed signed current.
For the main family, exact identification asks for
\(r_{\mathrm{Pen}}=0\); error families must remain separately typed.

Equivalently, one may introduce a generating deformation that attaches a
variable to every root-visible C-atom, prove the deformed version of
Proposition 5.10, and differentiate at the neutral mark. Proving only the
undeformed endpoint identity is insufficient.

## 4. Sufficient path-level schema

Suppose a signed identity has first been proved in a path space:

\[
\widehat\mu_{\mathrm{tr}}
=\sum_M\widehat\lambda_M^{\mathrm{Pen}}+\widehat r.
\]

Linearity then gives the current identity

\[
\operatorname{Cur}_H(\widehat\mu_{\mathrm{tr}})
=\sum_M\operatorname{Cur}_H(\widehat\lambda_M^{\mathrm{Pen}})
+\operatorname{Cur}_H(\widehat r).
\]

If each admitted residual path contains at most \(N_C\) eligible collisions,
then

\[
\|\operatorname{Cur}_H(\widehat r)\|_{\mathrm{TV}}
\le 2N_C\|\widehat r\|_{\mathrm{TV}}.
\]

The factor two is the gain/loss pair. This is only a sufficient logical
schema. Proposition 4.5 gives finiteness for fixed \(N\), but an estimate
useful in the Boltzmann--Grad regime still requires the molecule machinery;
the crude global collision count is not substituted for that analysis.

## 5. Actual, truncated, target and residual currents

The full response ledger must be current-valued throughout:

\[
\begin{aligned}
J^{\epsilon}_{\mathrm{actual}}
&=J^{\Lambda,\Gamma}_{\mathrm{tr}}+r_{\mathrm{trunc}},\\
J^{\Lambda,\Gamma}_{\mathrm{tr}}
&=\mathfrak K^\epsilon_H+r_{\mathrm{Pen}},\\
\nu_T^\epsilon
&=J^{\epsilon}_{\mathrm{actual}}-J_T[f].
\end{aligned}
\]

Geometry, \(\mathrm{Err}_2\), and terminal errors add further signed currents
\(r_{\mathrm{geom}},r_{\mathrm{Err}_2},r_{\mathrm{term}}\) only after each is
constructed on the same event space. A state \(L^1\) norm is not a current
and may not be inserted into this ledger by renaming.

Every residual keeps its own pairing and total-variation budget. Aggregation
is allowed only after the individual current constructions and estimates
have passed.

## 6. Exact executable obligations

The rational certificate verifies:

1. path-to-current pushforward is linear;
2. gain/loss orientation and Penrose coefficient signs remain independent;
3. a signed path-level Penrose identity implies every bounded weak pairing;
4. current residual TV is controlled by path-residual TV and eligible mark
   count;
5. equal endpoint marginals can have different collision currents;
6. equal positive majorants can have different signed currents;
7. equal total mass and total variation need not give equal weak pairings;
8. forgetting orientation can erase a nonzero gain/loss pairing;
9. event-forgetting cuts cannot reconstruct the marked pairing;
10. residual path types push to separately auditable current types;
11. actual/truncated/target response reconstruction is exact once the
    path-level identity is supplied; and
12. the source ledger stops at the missing marked Penrose and residual-current
    theorems.

All values are exact rational numbers. The executable is a logic certificate,
not numerical evidence for the continuum theorem.

## 7. Kill conditions

B4 rejects identification if:

- the proof starts only from endpoint marginals or endpoint operators;
- signs are restored after taking an absolute majorant;
- gain/loss orientation and the Penrose overlap sign are conflated;
- equality is checked only for total masses rather than bounded weak tests;
- a cut that forgot event variables is used to reconstruct a mark;
- the physical, truncated and target objects use different event spaces;
- a state error norm is relabelled as a current;
- any residual current is hidden in an unnamed \(o(1)\); or
- the conclusion depends on an arbitrary estimating cut order.

## 8. Claim ceiling and next gate

B4 earns:

- a corrected source audit exposing the exact signed formula (5.63);
- recognition of (7.15) as a term-level collision evaluation identity;
- the minimal path-resolved marked Penrose theorem needed for identification;
- an exact sufficient path-to-current schema;
- four separately typed current residual obligations; and
- exact counterexamples to every weaker identification route.

B4 does **not** earn:

- equality of \(\mathfrak K_H^\epsilon\) with the truncated or actual
  hard-sphere current;
- current-valued bounds for \(\mathrm{Err}_2\) or the terminal error;
- a logarithmic collision test, entropy chain rule or H theorem;
- a Core theorem, Theory Map object, arithmetic-rank promotion or API.

The next gate should be narrower than the original B4 target: prove the
**one-layer marked Penrose insertion identity** by deforming Proposition 5.10
before any absolute value or multi-layer induction. Only after that equality
passes should current-valued truncation and terminal residual estimates be
attempted.

## 9. Repository boundary

### Mathematical Core

Unchanged. The finite theorem is a research-local linear pushforward schema.

### Engineering Architecture

Refined research-locally. A continuum adapter now needs a path-resolved
source, a linear current extractor, two independent sign axes, and typed
current residuals. Endpoint state adapters are insufficient.

### Theory Map

Unchanged. B4 sharpens the history-loss and adaptation seams at U4/E without
objectifying molecules or currents.

### API

No pressure. The exact classes remain executable documentation only.
