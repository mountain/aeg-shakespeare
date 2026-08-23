# Pendulum lifted-clock global quotient through the branch locus

**Status:** research note; T0/T1 exploration. No Theory Map node or edge is added or promoted by this note.

**Code:** `tests/research/test_pendulum_lifted_clock_global_quotient.py`

**Theory Map relation:** `supports` the lifted-clock/geometric-phase contract of `docs/54-pendulum-elliptic-group-rank-lowering.md` by realizing its third level globally; `refines` TR-0001's global-period arrow for the lemniscatic leaf; `provides` the branch-locus degeneration (the boundary the T1->T2 gate requires). The stable map is unchanged.

## 1. What this note records

`docs/54` established three clock levels

```text
lifted real clock R
    -> geometric real action R / T_p Z
    -> complex Abel-Jacobi torus C / Lambda
```

but certified only the first arrow on the real flow. This note globalizes the chain for the `E = 0` lemniscatic leaf and certifies the branch-locus boundary the pendulum family guide lists as priority 1.

The executable essay certifies:

1. `sigma(U, Y) = (-U, iY)` is an exact automorphism of the carrier with `sigma*omega = i omega`, exchanging the two real branch pairs; hence `omega_B = i omega_A` and `tau = i` (exact symbolic plus exact deduction);
2. the complex flow `U(z) = -sn^2(z/sqrt(2), i)` satisfies `dU/dz = Y` and the carrier equation at generic complex `z` (sampled numerical);
3. `P(z + T_p) = P(z)` and `P(z + i T_p) = P(z)` with `T_p = 2 sqrt(2) varpi` the primitive real period: the period lattice is the square lattice `Lambda = Z T_p + Z i T_p` (sampled numerical plus exact lattice statement);
4. the Jacobi identities `K(i) = varpi/2` and `T_p = 4 sqrt(2) K(i)` match the lattice basis (sampled numerical);
5. the local decoder chart degenerates exactly at `U = +/-1`, and the Z2 mark flips across each turning point: the marked carrier is a ramified double cover with mark monodromy `-1` around each branch point, while the real period loop winds around two branch points and lifts to a closed marked loop (exact degeneration + sampled sign flip);
6. the clock chain reads off exactly: `R -> R/T_p Z` forgets winding (kernel `T_p Z`), and the real phase embeds in `C/Lambda` because `R cap Lambda = T_p Z` — the third arrow is a complexification, not a further quotient.

## 2. Two structural points

### 2.1 The third arrow embeds, it does not quotient

`docs/54` drew the chain as successive quotients. Globally the second and third levels have different roles: the first arrow quotients the lifted clock by the real period (forgetting the winding number — history data), while the second arrow is an embedding of the real circle into the complex torus. What complexification adds is precisely the imaginary period `i T_p` — the new lattice data, invisible to the real flow. The information contract should therefore be read as

```text
R --quotient by T_p Z--> R / T_p Z --embedding--> C / Lambda,
Lambda = Z T_p + Z i T_p,   R cap Lambda = T_p Z.
```

### 2.2 The mark is covering data, not carrier data

The Cartesian mark `sigma = sign(q_x)` is branched exactly over `U = +/-1` — the two turning points of the `E = 0` libration. The decoder output jumps sign across a turning point under any fixed section, so the continuous Cartesian continuation forces the mark to flip. Around a single branch point the mark has monodromy `-1`; the real period loop winds around two branch points, so its monodromy is trivial and `P(z + T_p)` closes as a *marked* point. This is the concrete meaning of the reviewer's separation of lifted clocks from geometric actions: the mark lives on the history/covering side of the projection, exactly the data whose forgetting the period group measures.

## 3. What remains open (unchanged kill conditions)

This note does not claim canonicity of the clock chain and does not promote TR-0001. It is restricted to the `E = 0` lemniscatic leaf: other energy leaves, the generic-`E` lattice, and full Cartesian state continuation across `U = +/-1` into other sheets remain open (family guide priority 1 is partially, not fully, delivered). The period certificates are sampled numerical (30-digit mpmath), not interval or formal proofs. No public or experimental API changes; all objects are research-local and import only the canonical namespaces.

## 4. Onward links

- `tests/research/test_pendulum_elliptic_group_rank_lowering.py` (PR #79, prerequisite)
- `docs/54-pendulum-elliptic-group-rank-lowering.md`
- `tests/classical/test_pendulum_local_branch_decoder.py`
- `docs/52-canonical-completion-hypothesis.md` (TR-0001)
- `docs/vignettes/simple-pendulum.md` (pendulum family guide)
