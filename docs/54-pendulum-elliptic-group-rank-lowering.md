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

the chord-tangent composition `(+)` is the elliptic group law, and the flow objectifies the translation schema `tau_t: p -> p (+) S(t)` with `S(t) = P(t) (+) P(0)`. The executable essay certifies:

1. the exact Weierstrass reduction (with `j = 1728` on the lemniscatic leaf `E = 0`);
2. the exact Euler addition theorem on the carrier, in chord and tangent form: `omega(P (+) Q) = omega(P) + omega(Q)` as an exact one-form identity modulo the curve ideal;
3. the twisted subgroup law of the closed-form lemniscatic flow `U(t) = -sn^2(t/sqrt(2), i)`: `P(t1) (+) P(t2) = P(t1+t2) (+) P(0)`, with `P(0) = (0,0)` a 2-torsion point, so the untwisted orbit is an exact one-parameter subgroup (sampled numerical certificate);
4. three red teams: an unmarked endpoint merges distinct Cartesian continuations; a fixed curve point does not identify the flow schema (period ambiguity and the torsion twist); coordinatewise addition leaves the carrier.

## 2. The structural reading

The analogy with AEG is exact in shape, not merely verbal:

| AEG (arithmetic) | Pendulum (geometric) |
| --- | --- |
| lower-rank objects: Translation `T_a` | lower-rank objects: carrier points `p` |
| objectified schema: `R_k(T_a) = T_(ka)` | objectified schema: `tau_t: p -> p (+) S(t)` |
| composition: repeated addition / `D_k D_l = D_(kl)` | composition: chord-tangent `(+)` |
| cross relation: `D_k T_a = T_(ka) D_k` (noncommutative) | cross relation: the torsion twist `P(t1)(+)P(t2) = P(t1+t2)(+)P(0)` (commutative) |
| rank lowering: displacement / clock sum | rank lowering: the clock `omega` integral, kernel = period lattice |
| fixed-output red team: `T_6` identifies no schema | fixed-point red team: `P(t)` identifies no `tau_t` |
| continuation red team: `abs(q)` merges S and P | continuation red team: unmarked `(U,Y)` merges the Z2 fiber |

Both domains therefore support the same T1 refinement already recorded in `docs/52`: the thing objectified at the next rank is a stable *process/action on lower-rank semantic objects*, not a point. The geometric calibration adds one new datum the arithmetic one could not: the kernel of rank lowering is here the *period lattice* — the same obstruction data that the marked-carrier hypothesis (`C,D,omega`) places in its group/completion layer. Euler's addition theorem is the exact certificate that this lowering is a homomorphism.

## 3. What remains open (kill conditions, unchanged)

This note does not claim that the group law is canonical, minimal, or forced among presentation choices, and it does not promote TR-0001. The standing kill conditions of `docs/52` remain in force; in particular the essay does not address observer nonuniqueness, does not touch the Z2 Cartesian state fiber beyond the red team (the group law lives on the carrier itself, and the fiber is the reconstruction boundary of the Cartesian task), and does not construct the completion object whose existence H-C conjectures.

The flow subgroup tests are sampled numerical certificates (30-digit mpmath), not interval or formal proofs. The essay changes no public or experimental API and imports nothing beyond the canonical `process_geometry` namespaces.

## 4. Onward links

- `tests/research/test_aeg_translation_objectification_rank_lowering.py`
- `tests/research/test_aeg_addition_multiplication_rank_transition.py`
- `tests/classical/test_pendulum_observable_quotient_fiber.py`
- `docs/52-canonical-completion-hypothesis.md` (TR-0001)
- `docs/vignettes/simple-pendulum.md` (pendulum family guide)
