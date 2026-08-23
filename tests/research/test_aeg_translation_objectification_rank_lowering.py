"""AEG Addition calibration of V1 -> V2 -> V3 -> V4.

This executable essay keeps the first vertical calibration research-local.  It
starts from free signed unit translations, compresses histories by their exact
continuation-stable translation semantics, objectifies those semantic classes as
new translation primitives, freely composes the new primitives, and lowers every
higher-rank word back to lower-rank process history.

The key requirement is compositionality: lowering must interpret arbitrary legal
higher-rank words, not merely decode one objectified symbol at a time.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from process_geometry.process.history import ProcessWord


LOWER_DISPLACEMENT = {"S": 1, "P": -1}


def displacement(history: ProcessWord[str]) -> int:
    """Exact semantic quotient of a signed unit-translation history."""

    return sum(LOWER_DISPLACEMENT[step] for step in history)


def interpret_lower(history: ProcessWord[str], initial: int) -> int:
    return initial + displacement(history)


@dataclass(frozen=True)
class TranslationPrimitive:
    """Research-local objectification of one stable translation semantic class."""

    displacement: int

    def apply(self, value: int) -> int:
        return value + self.displacement


def objectify(history: ProcessWord[str]) -> TranslationPrimitive:
    """Promote the exact lower-rank semantic class, not one literal history."""

    return TranslationPrimitive(displacement(history))


def lower_primitive(primitive: TranslationPrimitive) -> ProcessWord[str]:
    """Choose one canonical lower-rank representative for a rank-one primitive."""

    amount = primitive.displacement
    if amount > 0:
        return ProcessWord(("S",) * amount)
    if amount < 0:
        return ProcessWord(("P",) * (-amount))
    return ProcessWord()


def lower_higher_history(
    history: ProcessWord[TranslationPrimitive],
) -> ProcessWord[str]:
    """Compositionally interpret every legal rank-one word at rank zero."""

    lowered = ProcessWord[str]()
    for primitive in history:
        lowered = lowered.compose(lower_primitive(primitive))
    return lowered


def interpret_higher(
    history: ProcessWord[TranslationPrimitive],
    initial: int,
) -> int:
    value = initial
    for primitive in history:
        value = primitive.apply(value)
    return value


def absolute_displacement(history: ProcessWord[str]) -> int:
    """Deliberately weak terminal statistic used by the red team."""

    return abs(displacement(history))


def test_semantic_compression_identifies_history_not_syntax():
    short = ProcessWord(("S", "S"))
    long = ProcessWord(("S", "P", "S", "S", "S", "P"))

    assert short != long
    assert displacement(short) == displacement(long) == 2
    assert objectify(short) == objectify(long) == TranslationPrimitive(2)

    for initial in (-7, 0, 11):
        assert interpret_lower(short, initial) == interpret_lower(long, initial)


def test_translation_semantics_is_stable_under_bounded_free_continuations():
    left = ProcessWord(("S", "P", "S"))
    right = ProcessWord(("S",))

    assert displacement(left) == displacement(right)

    # The algebraic reason is q(hk)=q(h)+q(k).  This finite exhaustive sweep is
    # only an executable calibration of that identity, not the proof itself.
    for length in range(5):
        for items in product(("S", "P"), repeat=length):
            continuation = ProcessWord(tuple(items))
            assert displacement(left.compose(continuation)) == displacement(
                right.compose(continuation)
            )
            assert displacement(left.compose(continuation)) == (
                displacement(left) + displacement(continuation)
            )


def test_objectified_primitives_open_a_new_free_composition_space():
    plus_two = objectify(ProcessWord(("S", "S")))
    minus_one = objectify(ProcessWord(("P",)))

    # +3 was not supplied as an objectified seed. It appears from free
    # higher-rank composition of the two retained primitives.
    higher = ProcessWord((plus_two, plus_two, minus_one))

    assert len(higher) == 3
    assert sum(item.displacement for item in higher) == 3
    assert interpret_higher(higher, 10) == 13
    assert displacement(lower_higher_history(higher)) == 3
    assert interpret_lower(lower_higher_history(higher), 10) == 13


def test_rank_lowering_preserves_composition_not_only_generators():
    plus_two = TranslationPrimitive(2)
    minus_three = TranslationPrimitive(-3)
    plus_one = TranslationPrimitive(1)

    left = ProcessWord((plus_two, minus_three))
    right = ProcessWord((plus_one, plus_two))

    # Lowering is defined homomorphically on the full free higher-rank language.
    assert lower_higher_history(left.compose(right)) == lower_higher_history(
        left
    ).compose(lower_higher_history(right))

    for initial in (-5, 0, 8):
        assert interpret_higher(left.compose(right), initial) == interpret_lower(
            lower_higher_history(left.compose(right)), initial
        )


def test_lowering_semantics_for_all_small_unseen_composites():
    alphabet = (
        TranslationPrimitive(-2),
        TranslationPrimitive(1),
        TranslationPrimitive(3),
    )

    for length in range(5):
        for items in product(alphabet, repeat=length):
            higher = ProcessWord(tuple(items))
            lowered = lower_higher_history(higher)
            expected = sum(item.displacement for item in items)
            assert displacement(lowered) == expected
            assert interpret_higher(higher, 17) == interpret_lower(lowered, 17)


def test_high_rank_addition_relation_lowers_soundly():
    for left_amount in range(-3, 4):
        for right_amount in range(-3, 4):
            left = ProcessWord(
                (
                    TranslationPrimitive(left_amount),
                    TranslationPrimitive(right_amount),
                )
            )
            right = ProcessWord(
                (TranslationPrimitive(left_amount + right_amount),)
            )

            # T_m T_n == T_(m+n) is a high-rank relation. Literal lowered words
            # can differ because cancellation has not been normalized, but their
            # declared lower-rank semantics must agree.
            assert displacement(lower_higher_history(left)) == displacement(
                lower_higher_history(right)
            )

            swapped = ProcessWord(
                (
                    TranslationPrimitive(right_amount),
                    TranslationPrimitive(left_amount),
                )
            )
            assert displacement(lower_higher_history(left)) == displacement(
                lower_higher_history(swapped)
            )


def test_objectification_moves_history_depth_into_primitive_description():
    lower = ProcessWord(("S",) * 100)
    primitive = objectify(lower)
    higher = ProcessWord((primitive,))

    assert len(lower) == 100
    assert len(higher) == 1
    assert displacement(lower_higher_history(higher)) == 100


def test_absolute_displacement_red_team_is_not_continuation_stable():
    positive = ProcessWord(("S",))
    negative = ProcessWord(("P",))
    continuation = ProcessWord(("S",))

    # A terminal-only statistic would merge these histories.
    assert absolute_displacement(positive) == absolute_displacement(negative) == 1

    # But future composition exposes the discarded sign, so this relation cannot
    # ground a reusable objectification for exact translation semantics.
    assert absolute_displacement(positive.compose(continuation)) == 2
    assert absolute_displacement(negative.compose(continuation)) == 0
