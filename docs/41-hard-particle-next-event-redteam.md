# Independent red team — four-particle next-collision task

**Status:** independent process calibration; no API proposal.  
**Executable essay:** `tests/research/test_hard_particle_next_collision_argmin.py`.  
**Purpose:** test whether the Phase-14 pairwise-clean obstruction reappears outside Lonely Runner for independent physical reasons.

## 1. Engineering boundary

This note deliberately does **not** generalize the Sonnet result into a new public abstraction.

The calibration lives only in `tests/research/` plus this note.  It changes neither `src/` nor the public API.  The question is simply whether an unrelated process naturally produces the same distinction between

```text
pairwise information sufficiency
and
clean task-compatible decision geometry.
```

One additional example is evidence, not promotion pressure by itself.

---

## 2. Physical process

Take four point particles on a line with

\[
x_0<x_1<x_2<x_3,
\qquad
v_0>v_1>v_2>v_3.
\]

Until the first contact they move freely:

\[
x_i(t)=x_i+v_i t.
\]

Every adjacent gap is closing.  The three candidate first-contact times are

\[
\boxed{
\tau_i
=
\frac{x_{i+1}-x_i}{v_i-v_{i+1}},
\qquad i=0,1,2.
}
\]

The task is the nonempty set of adjacent contacts attaining

\[
\min(\tau_0,\tau_1,\tau_2).
\]

The process stops at that first event, so no rule for resolving simultaneous multi-particle collisions is required.

This process has no Lonely Runner torus, contact centers, lifted sheets, or pair-ratio wall alphabet.

---

## 3. Every positive three-clock configuration is physically realizable

Fix velocities

\[
(v_0,v_1,v_2,v_3)=(3,2,1,0).
\]

Then every adjacent relative closing speed equals one.  Given arbitrary positive rational numbers

\[
(t_0,t_1,t_2),
\]

choose consecutive gaps equal to those values:

\[
x_0=0,
\quad
x_1=t_0,
\quad
x_2=t_0+t_1,
\quad
x_3=t_0+t_1+t_2.
\]

The physical candidate collision times are exactly

\[
(\tau_0,\tau_1,\tau_2)=(t_0,t_1,t_2).
\]

Hence every nonempty subset of the three adjacent contacts occurs as an exact first-collision group for some physical initial condition.

The executable test constructs these states explicitly rather than assuming an abstract event-clock model.

---

## 4. Pairwise observation grammar

Use the three natural pairwise event-time comparisons

\[
\tau_0?\tau_1,
\qquad
\tau_0?\tau_2,
\qquad
\tau_1?\tau_2.
\]

For a task region whose minimum group is `S`, a comparison has sign

```text
-    first event is minimal, second is not
0    both are minimal
+    second event is minimal, first is not
⊥    neither is minimal; their loser order is not fixed by the task region
```

The physical state construction independently yields the exact seven-region matrix

```text
minimum group     pairwise partial signs
{0}               (-, -, ⊥)
{1}               (+, ⊥, -)
{2}               (⊥, +, +)
{0,1}             (0, -, -)
{0,2}             (-, 0, +)
{1,2}             (+, +, 0)
{0,1,2}           (0, 0, 0)
```

For every `⊥` entry, the test supplies two explicit physical states with the same first-collision task and opposite loser order.

---

## 5. Independent clean-separability result

Every pair of distinct first-collision tasks can be distinguished by at least one pairwise comparison whose sign is fixed on both regions.

So the pairwise grammar is information-theoretically sufficient.

But no one of the three comparisons is resolved on all seven task regions: for each pair, the third contact can be uniquely earliest while the order of the two losers remains arbitrary.

Therefore the Phase-13 research-local exact checker returns

\[
\boxed{
\text{pairwise separable}
\quad\text{and}\quad
\neg\operatorname{Clean}.
}
\]

The obstruction is atomic: the mixed seven-task root family has no clean pairwise query.

This reproduces the structural separation found in the exceptional Lonely Runner safe-window parent, but from an unrelated free-flight collision process.

---

## 6. Pairwise completion again over-refines

Enumerating physically realizable complete pairwise sign patterns gives exactly

\[
13
\]

weak total-order states for the three collision times, while the next-collision task has only

\[
7
\]

minimum-group values.

Thus pairwise completion again retains six distinctions consisting only of loser order:

\[
oxed{13\text{ completed states}\to7\text{ task values}.}
\]

This count is derived from explicit physical states, not copied from the Sonnet calibration.

---

## 7. What is and is not supported

We now have two process domains in which a natural multiway next-event task exhibits the same phenomenon:

1. Lonely Runner safe-window closure after a canonical first witness;
2. one-dimensional free-flight first collision of four closing particles.

This is enough to treat the phenomenon as worth continued investigation.  It is **not** enough to promote a generic public `ArgminPrimitive`, `MinimumGroup`, `Race`, or `Completion` abstraction.

The next evidence gate should differ more substantially in process semantics—ideally a non-kinetic or non-free-flight example—before any reusable API surface is discussed.

## Claim boundary

The result is a finite exact calibration of one first-event task.  It proves no new collision-mechanics theorem and makes no claim that multiway observation is computationally cheaper under a universal cost model.
