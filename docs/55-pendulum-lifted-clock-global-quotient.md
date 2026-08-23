# Pendulum lifted-clock lattice and the unramified mark cover

**Status:** research note; T0/T1 exploration. No Theory Map node or edge is added or promoted by this note.

**Code:** `tests/research/test_pendulum_lifted_clock_global_quotient.py`

**Theory Map relation:** `supports` the lifted-clock/geometric-phase contract of `docs/54-pendulum-elliptic-group-rank-lowering.md` by realizing its third level globally; `refines` TR-0001's global-period arrow for the lemniscatic leaf; `corrects` the primitive-period statement of the merged P10 essay. The stable map is unchanged.

## 1. What this note records

`docs/54` established three clock levels

```text
lifted real clock R
    -> geometric real action R / T_p Z
    -> complex Abel-Jacobi torus C / Lambda
```

and used `T_p = 2 sqrt(2) varpi` as the real period. Global analysis of the `E = 0` flow corrects and completes that chain. The executable essay certifies:

1. the Jacobi half-period relations for `k = i` (each identity certified at 30 digits), which pin the primitive period lattice of the flow `(U, Y) = (-sn^2, -sqrt(2) sn cn dn)` as `p1 = 2 sqrt(2) K(i)` and `p2 = 2 sqrt(2) i K'(i)`, equal to `<omega_A, omega_A (1 + i)>` with `omega_A = sqrt(2) varpi`;
2. the exact sigma symmetry `sigma(U, Y) = (-U, iY)` with `sigma*omega = i omega`, so the primitive basis satisfies `omega_B = i omega_A`: the lattice is the square lattice `Lambda = Z omega_A + Z i omega_A` with `tau = i`;
3. `P(z + omega_A) = P(z)` and `P(z + i omega_A) = P(z)`, with no real period in `(0, omega_A)` (sampled witnesses plus the invoked period theorem);
4. the decoder chart degenerates at `U = +/-1` (`0/0`); on the real `E = 0` physical loop only `U = -1` is reached, and the exact energy identity keeps the two distinct lifts `v_x = +/- sqrt(2)` there: the physical cover is **unramified**;
5. sheet transport: the true Cartesian velocity is continuous through `q_x = 0`, the mark flips once per traverse of the base loop (`q_x(0) = +1`, `q_x(omega_A) = -1`), and the marked state closes after two traverses (`q_x(2 omega_A) = +1`): the physical cover is the **nontrivial unramified double cover** of the real carrier loop;
6. the clock chain reads off exactly: `R -> R/omega_A Z` forgets winding (kernel `omega_A Z`), the real phase embeds in `C/Lambda` (`R cap Lambda = omega_A Z`), and the physical pendulum phase `R / 2 omega_A Z` double-covers the curve phase.

## 2. Three structural points

### 2.1 Correction: the primitive period is `omega_A`, not `2 omega_A`

The merged P10 essay wrote the geometric action as `R / T_p Z` with `T_p = 2 sqrt(2) varpi`. The carrier flow is already periodic with `omega_A = sqrt(2) varpi = T_p / 2` (the `sn^2` half-period `2K` transported to the z-coordinate), so the geometric action phase is `R / omega_A Z`, and `2 omega_A` is the period of the *physical pendulum state* — the marked point closes at `2 omega_A`, not at `omega_A`. The projection kernel is therefore `omega_A Z`, not `2 omega_A Z`.

### 2.2 The third arrow embeds; the physical phase double-covers

The chain should be read as

```text
R --quotient by omega_A Z--> R / omega_A Z --embedding--> C / Lambda,
Lambda = Z omega_A + Z i omega_A,   R cap Lambda = omega_A Z,
physical pendulum phase = R / 2 omega_A Z --2:1 unramified--> R / omega_A Z.
```

The third arrow is a complexification (it adds the imaginary period `i omega_A`), not a further quotient. The physical state phase is the nontrivial double cover of the curve phase: the mark is precisely the data that distinguishes the two lifts.

### 2.3 Chart failure is not ramification

The decoder formula `v_x = -sigma U Y / sqrt(1 - U^2)` becomes `0/0` at `U = +/-1`, and a fixed section `sigma = sign(q_x)` cannot be extended continuously through `q_x = 0`. On the real `E = 0` physical loop only `U = -1` is reached; there the energy identity gives the two distinct states `v_x = +/- sqrt(2)`, so the sheets do not merge. The signed Jacobi continuation `q_x(z) = cn(z/sqrt(2), i) dn(z/sqrt(2), i)` satisfies `q_x^2 = 1-U^2` and `dq_x/dz = v_x`, and yields `q_x(0)=1`, `q_x(omega_A)=-1`, `q_x(2 omega_A)=1`. This is sheet transport: monodromy of the unramified double cover around the whole base loop, not around a branch point.

## 3. What remains open (unchanged kill conditions)

This note does not claim canonicity of the clock chain and does not promote TR-0001. It is restricted to the `E = 0` lemniscatic leaf and to the real base loop for the cover statement (the complex global cover is not constructed). The primitive-lattice claim rests on the invoked Jacobi period theorem ([Whittaker-Watson-1927, Ch. XXII], [DLMF-22.4]) plus numeric certifications; the sampled certificates are 30-digit mpmath, not interval or formal proofs. No public or experimental API changes; all objects are research-local and import only the canonical namespaces.

## 4. Onward links

- `tests/research/test_pendulum_elliptic_group_rank_lowering.py` (P10, whose period naming this note corrects)
- `docs/54-pendulum-elliptic-group-rank-lowering.md`
- `tests/classical/test_pendulum_local_branch_decoder.py`
- `docs/52-canonical-completion-hypothesis.md` (TR-0001)
- `docs/vignettes/simple-pendulum.md` (pendulum family guide)
