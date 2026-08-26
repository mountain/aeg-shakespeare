"""Central-payload family spine: literal words, task memory, gauge, and units.

Problem
-------
Galilean mass and magnetic flux independently force a central composition
residual.  This spine states the shared process-language contract without
identifying their physical cocycles or promoting a generic connection theory.

Primitive histories and tasks
-----------------------------
Let planar translation parameters compose visibly by addition and let

    omega(a,b) = kappa/2 * (a wedge b)

be one additive central cocycle.  ``ProcessWord`` keeps literal ordered
translation histories.  Two tasks are declared:

1. the visible endpoint task observes only the summed translation;
2. the lifted task also observes the accumulated central phase.

The words ``ab`` and ``ba`` have the same visible endpoint but differ by
``kappa*(a wedge b)`` in the lift.  The visible quotient is therefore
continuation stable only for the visible task.  The lifted phase is necessary
residual memory for the phase-sensitive task.  Lowering from lifted to visible
is exact, while reconstructing phase from the visible endpoint is impossible.

Gauge, units, covers, and boundary
----------------------------------
Adding the coboundary of a declared one-cochain changes the cocycle
representative but preserves its central commutator.  Translation parameters
carry length units, so ``kappa`` carries inverse-area units; changing the
length ruler preserves the dimensionless phase exactly.

The task is finite word composition.  Raw word unfolding is executable, but
topological and analytic developing covers are not required.  This explicit
``not applicable`` result prevents a central extension from being relabelled a
cover or holonomy theorem without additional path/topology data.

Calibration statement
---------------------
Passing this file certifies literal-history preservation, visible and lifted
continuation tasks, quotient information loss, exact lowering, task-visible
residual memory, coboundary covariance, and unit covariance.  It supplies the
family-level decoder evidence missing from the older Galilean stages.

Boundary
--------
This is an exact finite central-extension calibration, not a classification of
cocycles, a quantum representation, a gauge-field solver, or a public generic
history-payload API.  Galilean mass and magnetic flux retain their separate
formulas and physical units in their own vignettes.

References
----------
[Bargmann-1954] V. Bargmann, "On Unitary Ray Representations of Continuous
Groups", *Annals of Mathematics* 59 (1954), 1--46.

[Brown-1964] E. Brown, "Bloch Electrons in a Uniform Magnetic Field",
*Physical Review* 133 (1964), A1038.
"""

from __future__ import annotations

from fractions import Fraction

from process_geometry.process.finite import (
    ProcessCocycle,
    ProcessFamily,
    central_commutator_residual,
    verify_process_cocycle,
)
from process_geometry.process.history import ProcessWord, interpret_history


Vector = tuple[Fraction, Fraction]
Lifted = tuple[Vector, Fraction]


def _add(left: Vector, right: Vector) -> Vector:
    return left[0] + right[0], left[1] + right[1]


def _wedge(left: Vector, right: Vector) -> Fraction:
    return left[0] * right[1] - left[1] * right[0]


def _central_family(kappa: Fraction) -> ProcessCocycle:
    translations = ProcessFamily(
        "T2-central-calibration",
        _add,
        identity=(Fraction(0), Fraction(0)),
    )
    return ProcessCocycle(
        translations,
        lambda left, right: kappa * _wedge(left, right) / 2,
        label="declared area payload",
    )


def _append_lifted(cocycle: ProcessCocycle, current: Lifted, step: Vector) -> Lifted:
    return cocycle.compose_lifted(current, (step, Fraction(0)))


def _interpret_lifted(history: ProcessWord[Vector], cocycle: ProcessCocycle) -> Lifted:
    return interpret_history(
        history,
        (cocycle.family.identity, Fraction(0)),
        lambda current, step: _append_lifted(cocycle, current, step),
    )


def test_visible_task_merges_ordered_words_that_the_lifted_task_distinguishes():
    cocycle = _central_family(Fraction(3))
    a = (Fraction(2), Fraction(0))
    b = (Fraction(0), Fraction(5))
    ab = ProcessWord((a, b))
    ba = ProcessWord((b, a))

    lifted_ab = _interpret_lifted(ab, cocycle)
    lifted_ba = _interpret_lifted(ba, cocycle)

    assert ab != ba
    assert lifted_ab[0] == lifted_ba[0] == (Fraction(2), Fraction(5))
    assert lifted_ab[1] - lifted_ba[1] == Fraction(30)

    continuation = ProcessWord(((Fraction(7), Fraction(-4)),))
    continued_ab = _interpret_lifted(ab.compose(continuation), cocycle)
    continued_ba = _interpret_lifted(ba.compose(continuation), cocycle)
    assert continued_ab[0] == continued_ba[0]
    assert continued_ab[1] - continued_ba[1] == Fraction(30)


def test_lifted_to_visible_lowering_is_exact_but_has_no_phase_decoder():
    cocycle = _central_family(Fraction(1))
    a = (Fraction(1), Fraction(0))
    b = (Fraction(0), Fraction(1))
    lifted_ab = _interpret_lifted(ProcessWord((a, b)), cocycle)
    lifted_ba = _interpret_lifted(ProcessWord((b, a)), cocycle)

    visible_decoder = lambda lifted: lifted[0]
    assert visible_decoder(lifted_ab) == visible_decoder(lifted_ba)
    assert lifted_ab[1] != lifted_ba[1]


def test_coboundary_changes_representative_but_not_central_commutator():
    kappa = Fraction(5)
    gauge_strength = Fraction(7)
    base = _central_family(kappa)

    def gauge(parameter: Vector) -> Fraction:
        return gauge_strength * parameter[0] * parameter[1]

    shifted = ProcessCocycle(
        base.family,
        lambda left, right: (
            base.value(left, right)
            + gauge(left)
            + gauge(right)
            - gauge(_add(left, right))
        ),
        label="coboundary-shifted area payload",
    )
    a = (Fraction(2), Fraction(3))
    b = (Fraction(-1), Fraction(4))
    c = (Fraction(5), Fraction(-2))

    assert verify_process_cocycle(
        shifted,
        ((a, b, c),),
        normalization_parameters=(a,),
    ).exact
    assert shifted.value(a, b) != base.value(a, b)
    assert central_commutator_residual(
        shifted, a, b
    ) == central_commutator_residual(base, a, b)


def test_inverse_area_payload_is_covariant_under_length_ruler_change():
    kappa = Fraction(3, 5)
    ruler = Fraction(7, 2)
    a = (Fraction(4), Fraction(-3))
    b = (Fraction(2), Fraction(5))

    physical_phase = kappa * _wedge(a, b)
    nondimensional_a = (a[0] / ruler, a[1] / ruler)
    nondimensional_b = (b[0] / ruler, b[1] / ruler)
    nondimensional_kappa = kappa * ruler**2

    assert nondimensional_kappa * _wedge(
        nondimensional_a, nondimensional_b
    ) == physical_phase
