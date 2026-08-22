# Literate programming and mathematical lineage

Shakespeare is a mathematical research library. Its source code should be readable not only as an implementation, but also as a record of **why the abstractions were introduced, which older mathematical language they reinterpret, and what remains conjectural**.

The project therefore adopts a literate-programming discipline.

## 1. Narrative before mechanism

A public module should normally begin with a short mathematical narrative before imports and implementation details. The narrative should answer, in this order:

1. **Primitive question** — what process/representation problem forced this module to exist?
2. **Classical shadow** — what familiar construction does the reader eventually recover?
3. **Reinterpretation** — how does Shakespeare change the order of explanation?
4. **Executable contract** — what exact objects or certificates does the module provide?
5. **Boundary** — what the module does *not* claim.

The source should not begin by pretending that a later classical representation was primitive. For example, the canonical pendulum calibration should begin from constrained position/velocity dynamics, not from `theta`, `sin(theta)`, or an elliptic integral.

## 2. Mathematical history is part of the implementation story

For classical analysis, ODE, mechanics, algebraic curves, and function theory, comments and docstrings should preserve the historical reversal that Shakespeare is testing.

A recurring pattern is:

```text
classical development:
    analytic difficulty -> special construction -> geometric/algebraic object

Shakespeare reconstruction:
    primitive process -> history/constraint/invariant -> quotient geometry
    -> adequate function language -> classical formula as a shadow
```

This is especially important for examples whose modern textbook presentation hides how the concepts were discovered historically:

- elliptic integrals -> inversion -> double periodicity -> complex torus -> cubic curve;
- Abelian integrals -> periods -> Jacobian -> higher-genus algebraic geometry;
- addition/multiplication -> noncommutative process calculus -> resonant logarithmic/Jordan extensions;
- recurrence relations -> finite process modules -> spectral language only as a later representation.

The code should explain these transitions close to the functions that make them executable.

## 3. Three levels of equality must remain visible

Literate exposition must not erase the distinction between:

- literal construction/history equality;
- equality modulo declared process relations or algebraic constraints;
- equality of final symbolic/semantic values.

If two constructions happen to simplify to the same SymPy expression, the source should say whether that equality is being used and at which layer.

## 4. Classical names belong late

A classical name is useful when it helps orientation, but it should appear **after** the process structure that forces it whenever practical.

Preferred style:

> The quotient has equation `y^2=P_3(x)` with nonzero discriminant, hence generic genus one. In the classical analytic shadow, integrating `dx/y` and inverting it leads to elliptic functions.

Avoid:

> Use elliptic functions to solve the pendulum.

Likewise, A/M means **Addition/Multiplication** and must be introduced from their finite and infinitesimal process relations before `exp`, `log`, or special-function vocabulary is used as explanation.

## 5. Tests are executable mathematical essays

A substantial test in `tests/classical/` or `tests/research/` should be a **complete mathematical vignette**, not a collection of assertions with explanatory comments added afterward.

Before the first executable line, its module docstring should normally give:

- the mathematical question;
- the primitive data allowed to the program;
- the relevant classical and historical lineage;
- the Shakespeare reconstruction being tested;
- a precise theorem/calibration statement;
- a proof map explaining how the assertions certify the statement;
- the boundary of the claim;
- rigorous bibliographic references.

The executable body should then follow a visible structure such as:

```python
# GIVEN: primitive process data only.
...

# DISCOVER: derive the structural relation with public Shakespeare machinery.
...

# ASSERT: verify the new-language structural statement.
...

# CLASSICAL SHADOW: only now compare with the familiar textbook object.
...
```

A reader should be able to read the file as a short mathematical essay and then use Python execution as a proof/checking layer.

References are mandatory for substantial classical and research essays. Historical statements should cite history or primary sources when practical; standard mathematical facts should cite authoritative monographs, handbooks, or primary literature with a useful locator such as chapter, section, theorem, equation, DOI, or stable institutional URL. The test's own Shakespeare interpretation must be labelled as interpretation rather than presented as a claim made by a cited classical source.

The detailed citation policy and test-essay template live in `docs/11-references-and-test-essays.md`.

## 6. Reusable abstractions go in `src/`; named problems stay in tests

A pendulum, Euler top, Kepler problem, Riccati equation, or Duffing oscillator is not a package feature merely because it is mathematically important.

A named example may force a new reusable abstraction. Only that abstraction moves into `src/`.

Examples:

- the pendulum forced `AlgebraicConstraintSet` and constraint prolongation;
- genus-one and higher hyperelliptic reductions motivated a generic `HyperellipticProfile`;
- A/M motivated `ProcessFrame` and `ProcessFunctionModule` rather than a catalogue of named solutions.

## 7. Claims must be typed by status

Use prose that makes the epistemic status clear:

- **implemented** — exact behavior checked by tests;
- **calibration** — a classical example exercising common machinery;
- **interpretation** — a proposed conceptual reading of an implemented result;
- **conjecture / research direction** — not established by the code.

Do not let an attractive historical analogy silently become a theorem.

## 8. Source layout

For mathematically substantial modules, prefer this order:

```text
module narrative
imports
small public data objects
primitive operations
exact certificates / reductions
higher-level search or composition
```

Do not optimize source layout only for terseness.  The mathematical dependency order should remain visible even when a shorter implementation exists.

## 9. Literate programming is not verbose commenting

Comments should explain representation choices, invariants, proof obligations, failure modes, and mathematical lineage.  They should not paraphrase obvious Python syntax.

A good comment answers one of these questions:

- Why is this object primitive here?
- Which equality layer is being used?
- Why is this transformation admissible?
- What certificate is produced?
- Which historical/classical object appears as a shadow?
- What remains unproved?

A comment that merely says what the following line does should normally be removed.

## 10. Public-domain code, attributed mathematics

The source code is dedicated to the public domain under the repository `LICENSE`.  That does **not** remove scholarly obligations.  Mathematical ideas, historical claims, and borrowed formulations should still be attributed accurately.  Public-domain licensing and rigorous citation serve different purposes and should not be conflated.
