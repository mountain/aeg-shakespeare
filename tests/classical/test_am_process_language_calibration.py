"""A/M family spine: literal words, affine task quotient, and exact lowering.

Problem
-------
The translation, dilation, character-transport, and local-direction essays
certify exact laws, but none alone displays the whole process-language chain.
This family spine fixes one narrow deterministic task and connects them:

    literal ordered A/M words
      -> affine normal form
      -> continuation-stable endpoint task quotient
      -> scalar-state decoder and declared unit frame.

Primitive histories and task
----------------------------
An elementary step ``(s,b)`` acts on a scalar assignment by

    x |-> s*x+b,        s>0.

``ProcessWord`` stores the ordered steps without relations.  The declared task
is to predict the scalar assignment after every future affine continuation.
The sufficient quotient carrier is the affine normal form ``(S,B)`` acting as
``x |-> S*x+B``.  Different literal words may have the same normal form and
therefore the same future task responses; their word depth remains lost.

The translation and positive-dilation subfamilies are ``(1,b)`` and ``(s,0)``.
The exact relation

    M_s T_b M_s^{-1} = T_{s b}

is recovered from ordered word interpretation.  Positive scale also admits
the supplied analytic coordinate ``u=log(s)``, but neither a topological cover
nor an analytic developing cover is needed for this finite endpoint-prediction
task.  Those axes are explicitly not applicable rather than silently absent.

Units, decoder, and boundary
----------------------------
``S`` is dimensionless while ``x`` and ``B`` share one length/value unit.
Changing the ruler by ``ell`` sends ``x,B`` to ``x/ell,B/ell`` and commutes
with affine evaluation.  The decoder evaluates ``S*x+B`` exactly.  It does not
reconstruct the literal word; retaining that word is necessary for grammar or
history-cost tasks.  Scale zero is outside the declared positive affine group.

Calibration statement
---------------------
Passing this file certifies literal-history preservation, exact affine
normalization, continuation stability, information loss, decoding, the A/M
conjugation relation, logarithmic scale round-trip, unit covariance, and the
zero-scale failure boundary.  It makes no Fourier/Mellin synthesis, canonical
word-section, shortest-history, or universal-cover claim.

References
----------
[Hall-2015] Brian C. Hall, *Lie Groups, Lie Algebras, and Representations*,
2nd ed., Springer, 2015.

Related repository evidence: ``test_translation_characters.py``,
``test_dilation_characters.py``, ``test_am_character_transport.py``,
``test_am_process_direction.py``, and
``tests/research/test_am_universal_history_recalibration.py``.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

from process_geometry.process.history import ProcessWord, interpret_history


Affine = tuple[Fraction, Fraction]


def _require_affine_step(step: Affine) -> None:
    scale, _shift = step
    if scale <= 0:
        raise ValueError("A/M affine steps require positive scale")


def _apply_affine(value, step: Affine):
    _require_affine_step(step)
    scale, shift = step
    return scale * value + shift


def _compose_normal_form(current: Affine, step: Affine) -> Affine:
    """Append ``step`` after the affine map stored in ``current``."""

    _require_affine_step(step)
    current_scale, current_shift = current
    scale, shift = step
    return scale * current_scale, scale * current_shift + shift


def _normal_form(history: ProcessWord[Affine]) -> Affine:
    return interpret_history(
        history,
        (Fraction(1), Fraction(0)),
        _compose_normal_form,
    )


def _decode(normal_form: Affine, value):
    return _apply_affine(value, normal_form)


def test_literal_am_words_remain_distinct_before_the_affine_task_quotient():
    translation = (Fraction(1), Fraction(1))
    double = (Fraction(2), Fraction(0))
    half = (Fraction(1, 2), Fraction(0))

    direct = ProcessWord((translation,))
    detour = ProcessWord((translation, double, half))

    assert direct != detour
    assert direct.depth == 1
    assert detour.depth == 3
    assert _normal_form(direct) == _normal_form(detour) == translation

    # Equal normal forms remain equal under every common affine continuation.
    continuation = ProcessWord(
        ((Fraction(3), Fraction(-2)), (Fraction(5, 2), Fraction(7)))
    )
    assert _normal_form(direct.compose(continuation)) == _normal_form(
        detour.compose(continuation)
    )


def test_affine_normal_form_is_a_sufficient_decoder_but_forgets_word_cost():
    history = ProcessWord(
        (
            (Fraction(1), Fraction(3)),
            (Fraction(2), Fraction(0)),
            (Fraction(1), Fraction(-5)),
        )
    )
    normal = _normal_form(history)
    initial = Fraction(11, 3)

    assert interpret_history(history, initial, _apply_affine) == _decode(
        normal, initial
    )
    assert normal == (Fraction(2), Fraction(1))
    assert normal != history.steps


def test_ordered_words_recover_the_finite_am_conjugation_relation():
    scale = Fraction(5, 2)
    shift = Fraction(7, 3)
    multiplication = (scale, Fraction(0))
    inverse_multiplication = (1 / scale, Fraction(0))
    translation = (Fraction(1), shift)

    # Application order is M^{-1}, then T, then M: M T M^{-1} on points.
    conjugated = ProcessWord(
        (inverse_multiplication, translation, multiplication)
    )
    assert _normal_form(conjugated) == (
        Fraction(1),
        scale * shift,
    )


def test_positive_scale_log_chart_and_unit_lowering_round_trip_exactly():
    u = sp.symbols("u", real=True)
    length_unit = Fraction(7, 2)
    value = Fraction(13, 5)
    shift = Fraction(-11, 3)
    scale = Fraction(9, 4)

    assert sp.simplify(sp.log(sp.exp(u)) - u) == 0

    physical = _decode((scale, shift), value)
    nondimensional = _decode(
        (scale, shift / length_unit),
        value / length_unit,
    )
    assert nondimensional == physical / length_unit


def test_zero_scale_is_an_explicit_failure_outcome():
    invalid = (Fraction(0), Fraction(1))

    try:
        _apply_affine(Fraction(2), invalid)
    except ValueError as exc:
        assert "positive scale" in str(exc)
    else:
        raise AssertionError("zero scale must not enter the positive A/M family")
