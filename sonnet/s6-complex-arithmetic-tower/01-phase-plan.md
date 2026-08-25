# Initial research plan and gates

This plan keeps external calibration and arithmetic construction separate
until an explicit equivariant bridge is available.

## Phase 0 — freeze and reproduce the source certificate

### Tasks

1. archive the reviewed PDF version and record its checksum;
2. extract the literal rank-four lattice basis and monodromy matrices;
3. verify determinants, orders \(3,4\), and the cusp relation
   \(M_0=I+N\) with \(N^2=0\);
4. compute invariant and coinvariant filtrations over \(\mathbb Z\);
5. reproduce the twist formula
   \[
   \pi_1(X)\cong
   \mathbb Z/\left|12\ell_0-4\ell_1-3\ell_2\right|\mathbb Z;
   \]
6. separate manuscript theorems, locally reproduced certificates, and our
   interpretations in a claim ledger.

### Gate 0

Do not begin strong Process Geometry or arithmetic extrapolation until the
finite matrix and topology certificate is reproducible from the frozen source.

## Phase 1 — Process Geometry calibration

### Tasks

1. construct a lossless translation ledger with four columns:
   classical datum, process role, information at risk, and genuinely new
   consequence;
2. exhibit two same-endpoint histories whose monodromy differs, then state the
   exact continuation task that detects the difference;
3. calculate the normalization conductor data for
   \(dP_6\to W\) and test it as a canonicalization defect;
4. keep finite-order fillings and the unipotent cusp separate in every
   materialization account;
5. test whether local history data can compile into any part of the global
   \(\pi_1\) or homology calculation.

### Gate 1

Pass only if the process language yields a new criterion, computable defect,
compression, prediction, or sharper failure localization.  Otherwise record
the phase as faithful re-expression.

## Phase 2 — arithmetic closure and finite-shadow search

### Tasks

1. formalize the \(A/M/P\) flows on an explicit logarithmic history cover;
2. compute the bracket closure filtration
   \[
   \mathfrak g_0=\operatorname{span}\{A,M,P\},
   \qquad
   \mathfrak g_{k+1}
   =
   \mathfrak g_k+[\mathfrak g_0,\mathfrak g_k]
   \]
   through a frozen finite depth;
3. record dimension growth, pole order, branch action, and exact relations;
4. freeze a task semantics before searching for finite quotients;
5. search first inside the native arithmetic grammar;
6. only after freezing that result, compare unrestricted algebraic or matrix
   presentations;
7. test candidate shadows against integral rank, Jordan data, finite orders,
   and unipotent filtration without using those targets during proposal
   generation.

### Gate 2

Pass only with an explicit quotient certificate and equivariant comparison.
Shared dimension, suggestive terminology, or post-hoc fitting does not pass.

## Phase 3 — local-to-global and neighboring constructions

### Tasks

1. determine whether arithmetic boundary behavior selects any completion;
2. test whether orders \(3,4\) arise internally from unit, branch, or discrete
   quotient constraints;
3. replace \((3,4,\infty)\) by neighboring
   \((m,n,\infty)\) signatures and freeze predictions before comparison;
4. determine whether twist closure is an arithmetic constraint or independent
   geometric input.

### Gate 3

Only a new verifiable prediction, classification, or exclusion result can
justify promotion to later work on memory mechanisms, natural machines, or
continuous computation.

## First four executable certificates

The next implementation PR should choose one owner file per certificate:

1. **matrix certificate** — exact finite-order and unipotent checks plus
   invariant/coinvariant data;
2. **closure certificate** — symbolic \(A/M/P\) bracket census at frozen depth;
3. **shadow comparison** — representation invariants with a strict oracle
   firewall;
4. **non-normal audit** — one exact conductor/cohomology witness for
   information lost by \(dP_6\to W\).

Long source reconstruction and exploratory searches must not become routine CI
gates.  Small exact semantic regressions may enter tests/research after their
cost is measured and bounded.

## Decision record

The initial allocation is:

\[
\text{source verification}
\prec
\begin{cases}
\text{Process Geometry calibration},\\
\text{native arithmetic closure},
\end{cases}
\prec
\text{strict interface search}.
\]

The two middle branches may proceed independently.  Neither may borrow the
other's desired answer.  Work on learning, natural correspondences, or
continuous universal computation remains downstream of Gate 3.
