# Pendulum elliptic group law as compositional rank lowering

**Status:** research note; T0/T1 exploration. No Theory Map node or edge is added or promoted by this note.

**Code:** `tests/research/test_pendulum_elliptic_group_rank_lowering.py`

**Theory Map relation:** `supports` V3–V4 (objectification -> free higher-rank composition -> compositional rank lowering) with a second, geometric (non-arithmetic) domain; `refines` the group-layer arrow of TR-0001 (`docs/52-canonical-completion-hypothesis.md`) with executable content for the pendulum carrier. The stable map is unchanged.

## 1. What this note records

The AEG arithmetic calibrations (`docs/50`, `docs/51`) made the vertical axis executable in one domain: signed unit translations objectify into Translation primitives, and the uniform repeated-Addition schema `R_k(T_a) = T_(ka)` objectifies into Multiplication. Both essays certified that the objectified thing is an *action schema*, not one of its outputs, and that rank lowering is a homomorphism on the free higher-rank language.

This note records a second, geometric calibration of the same mechanism. On the pendulum observable carrier

```text
Y^2 = 2 (E - U) (1 - U^2),   D U = Y,   D Y = 3 U^2 - 2 E U - 1,
omega = dU / Y,   omega(D) = 1,
```

the chord-tangent composition `(+)` is the elliptic group law. The flow admits a lifted translation schema `tilde_tau_t: p -> p (+) S(t)` with `S(t) = P(t) (+) P(0)`; its projection to the actual geometric action identifies clocks differing by a real period. The executable essay certifies:

1. the exact Weierstrass reduction (with `j = 1728` on the lemniscatic leaf `E = 0`);
2. the exact Euler addition theorem on the carrier, in chord and tangent form: the group-law pullback of the invariant differential splits as the sum of the two factor differentials, so the Abel-Jacobi integral is additive modulo periods;
3. the closed-form lemniscatic flow `U(t) = -sn^2(t/sqrt(2), i)` numerically obeys the base-point correction `P(t1) (+) P(t2) = P(t1+t2) (+) P(0)`, with `P(0) = (0,0)` a 2-torsion point; after correction, the expected one-parameter subgroup law is sampled numerically;
4. three red teams: an unmarked endpoint merges distinct Cartesian continuations; a fixed curve point does not identify the flow schema (period ambiguity and the torsion twist); coordinatewise addition leaves the carrier.

## 2. The structural reading

The analogy with AEG is exact in shape, not merely verbal:

| AEG (arithmetic) | Pendulum (geometric) |
| --- | --- |
| lower-rank objects: Translation `T_a` | lower-rank objects: carrier points `p` |
| objectified schema: `R_k(T_a) = T_(ka)` | objectified schema: `tau_t: p -> p (+) S(t)` |
| composition: repeated addition / `D_k D_l = D_(kl)` | composition: chord-tangent `(+)` |
| cross relation: `D_k T_a = T_(ka) D_k` (noncommutative) | base-point/torsor correction: `P(t1)(+)P(t2) = P(t1+t2)(+)P(0)` |
| rank lowering: displacement / clock sum | lifted clock `t`; geometric phase `[t]`; Abel-Jacobi value modulo the period lattice |
| fixed-output red team: `T_6` identifies no schema | fixed-point red team: `P(t)` identifies no `tau_t` |
| continuation red team: `abs(q)` merges S and P | continuation red team: unmarked `(U,Y)` merges the Z2 fiber |

Both domains therefore support the same T1 refinement already recorded in `docs/52`: the thing objectified at the next rank is a stable *process/action on lower-rank semantic objects*, not a point. The geometric calibration adds one new datum the arithmetic one could not: lowering from lifted history to the actual geometric action forgets the *period lattice*. More precisely, the real flow has a lifted clock `t in R`, while the action on the real carrier retains only `[t] in R / T_p Z`; after complexification the Abel-Jacobi coordinate lies in `C / Lambda`. The period group is the kernel of the projection from lifted clocks to geometric actions, not the kernel of a map from an unlifted action back to a bare real clock. Euler's addition theorem is the exact invariant-differential certificate behind Abel-Jacobi additivity modulo periods.

## 2.1 The three clock levels

The type distinction is part of the information contract:

```text
lifted real clock R
    -> geometric real action R / T_p Z
    -> complex Abel-Jacobi torus C / Lambda
```

A lifted schema retains history/covering data and may lower to a bare real clock. An unlifted geometric action cannot: `tau_t = tau_(t+T_p)`. Thus the period group measures precisely what is forgotten when process history is quotiented to state action.

## 3. What remains open (kill conditions, unchanged)

This note does not claim that the group law is canonical, minimal, or forced among presentation choices, and it does not promote TR-0001. The standing kill conditions of `docs/52` remain in force; in particular the essay does not address observer nonuniqueness, does not touch the Z2 Cartesian state fiber beyond the red team (the group law lives on the carrier itself, and the fiber is the reconstruction boundary of the Cartesian task), and does not construct the completion object whose existence H-C conjectures.

The flow subgroup tests are sampled numerical certificates (30-digit mpmath), not interval or formal proofs. The essay changes no public or experimental API and imports nothing beyond the canonical `process_geometry` namespaces.

## 4. Onward links

- `tests/research/test_aeg_translation_objectification_rank_lowering.py`
- `tests/research/test_aeg_addition_multiplication_rank_transition.py`
- `tests/classical/test_pendulum_observable_quotient_fiber.py`
- `docs/52-canonical-completion-hypothesis.md` (TR-0001)
- `docs/vignettes/simple-pendulum.md` (pendulum family guide)
