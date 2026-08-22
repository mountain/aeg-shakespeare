# KdV soliton scattering as parametric history rewriting

**Status:** Level-2 research calibration; executable, not yet a public API contract.

## 1. Why this is the next threshold

The first KdV calibration stopped at the traveling-wave quotient:

```text
local process
    -> discovered first integral
    -> cubic curve
    -> generic genus one
    -> soliton degeneration.
```

That result showed that the solitary-wave sector can appear as a degeneration of a
discovered algebraic quotient.  It did not yet use Shakespeare's literal history
machinery in an essentially multi-body way.

The next question is therefore narrower and harder:

> Can elastic multi-soliton scattering be represented as local history rewrites whose
> residual phase data remain globally consistent when several rewrite orders are
> possible?

This is the first place where a deterministic normalizer is not enough.  A useful
process presentation must explain why *alternative local histories join*.

## 2. The pair rule

For KdV solitons with distinct positive wave numbers, Hirota's pair interaction
factor is

\[
A_{ij}=\left(\frac{k_i-k_j}{k_i+k_j}\right)^2.
\]

The executable test stores, for each asymptotic soliton, a dimensionless phase
coordinate

\[
q_i=k_i x_{0,i}.
\]

For an adjacent speed inversion with \(k_f>k_s\), define

\[
L_{fs}=-\log A_{fs}.
\]

The research-local parametric history rule is

\[
\boxed{
(f,q_f)(s,q_s)
\longrightarrow
(s,q_s-L_{fs})(f,q_f+L_{fs}).
}
\]

The rule has three immediate certificates:

1. the visible soliton identities and wave numbers are preserved;
2. the visible order is exchanged;
3. the local phase balance is exact:

\[
(q_f+L_{fs})+(q_s-L_{fs})=q_f+q_s.
\]

If \(q=kx_0\) is decoded to a physical center, the displacement is

\[
\Delta x_f=\frac{L_{fs}}{k_f},\qquad
\Delta x_s=-\frac{L_{fs}}{k_s},
\]

in the phase convention used by the test.

The important Shakespeare distinction is that the rewrite does not erase the
collision.  The visible order changes, while the phase transfer remains attached to
the history trace as a residual.

## 3. Three solitons produce a genuine critical pair

Start from a descending speed history

\[
3\;2\;1.
\]

There are two initial inversions, so one may normalize leftmost-first or
rightmost-first.  The adjacent transposition words are

\[
s_1s_2s_1
\qquad\text{and}\qquad
s_2s_1s_2.
\]

Both end in the visible order

\[
1\;2\;3.
\]

For the KdV rule, every unordered pair crosses exactly once, and the phase transfer
for that pair depends only on its two wave numbers.  Hence the final phases are

\[
q_3' = q_3+L_{32}+L_{31},
\]

\[
q_2' = q_2-L_{32}+L_{21},
\]

\[
q_1' = q_1-L_{31}-L_{21},
\]

independently of which critical branch is taken first.

The executable statement is therefore stronger than ordinary sorting:

\[
\boxed{
\text{same visible normal form}
+\text{same transported residual data}.
}
\]

This is a restricted braid/Yang--Baxter-type consistency test for the calibrated
pair map.  The repository does **not** yet claim a general Yang--Baxter structure.

## 4. A red team that passes every local balance check

A weak red team would simply break conservation in a two-soliton collision.  That
would not demonstrate that three-body consistency adds information.

Instead the test perturbs the transferred amount by

\[
L_{fs}
\longmapsto
L_{fs}+\varepsilon(q_f-q_s),
\]

while still adding the same amount to the fast phase and subtracting it from the
slow phase.

Thus every local rewrite still satisfies

\[
q_f'+q_s'=q_f+q_s,
\]

and the visible pair is still exchanged correctly.

But the transfer now depends on the current phase state, which itself depends on
earlier collisions.  The two three-soliton rewrite branches therefore produce
unequal final phase assignments.

This gives a clean separation:

```text
local pair conservation              insufficient
local pair conservation + joinability discriminating
```

The red team is useful precisely because it survives the obvious two-body test.

## 5. What API pressure this creates

The existing public `WordRewriteRule` is a concrete contiguous-word replacement.
The KdV calibration instead needs a rule of the form

```text
match(local parameterized history)
    -> bindings

rewrite(bindings)
    -> replacement history + residual data

certificate(before, after)
    -> exact semantic checks
```

The three-body test additionally needs

```text
overlapping rewrites
    -> divergent branches
    -> bounded normalization of both branches
    -> visible join test
    -> residual join test.
```

Two candidate abstractions are therefore becoming visible:

- **parametric history relation** — a local process relation with bound parameters
  and a certified replacement;
- **confluence certificate** — evidence that competing rewrite branches join in the
  task-relevant semantics, not merely that one deterministic strategy terminates.

They are deliberately **not** promoted into `presentation.history` yet.  One KdV
family, even with both two- and three-soliton tests, is not enough evidence that the
right generic interface has been found.

## 6. Why the phase residual is not forced into `ProcessCocycle`

`ProcessCocycle` currently represents an additive central residual over one visible
finite family.  KdV scattering instead redistributes phase coordinates attached to
individual soliton tokens:

\[
(q_f,q_s)\mapsto(q_f+L,q_s-L).
\]

That is closer, at this stage, to parameter transport under a local interchange
relation than to one common scalar central coordinate.  Forcing the data into the
existing cocycle API would hide this distinction.

A generalized history-residual abstraction should be considered only if an
independent calibration produces the same pattern.

## 7. Immediate next experiment

The next useful step is not to publish the research-local matcher.  It is to expose
the same two histories through a second representation of KdV multi-solitons -- most
naturally a small Hirota/Baecklund/Darboux construction -- and test whether the
pairwise residuals extracted there agree with the rewrite presentation.

That would give the first cross-presentation square:

```text
Hirota / transformation history
        |                     |
        v                     v
pair interaction data --> parametric rewrite
        |                     |
        +------ phase --------+
```

If the square commutes for two and three solitons, the case for promoting a generic
parametric-history relation becomes substantially stronger.

## 8. Claim boundary

The current executable vignette does not:

- derive Hirota's interaction coefficient from primitive KdV PDE syntax;
- reconstruct the full tau function;
- prove general N-soliton factorization by induction;
- discover the rewrite rule automatically;
- provide a Knuth--Bendix completion engine;
- establish a general Yang--Baxter or braid-group representation;
- justify a public parametric-rewrite API.

Its narrower result is already nontrivial: **the classical KdV pair phase law defines
a parameterized local history relation whose three-body critical pair joins, while a
state-dependent two-body impostor preserving the same local phase balance does not.**

That is the first executable evidence in Shakespeare that integrability can appear
as global consistency of local history rewrites, rather than only as existence of a
first integral or low-genus quotient.
