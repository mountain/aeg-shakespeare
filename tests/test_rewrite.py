from aeg_shakespeare.presentation.history import (
    WordRewriteRule,
    normalize_word,
    rewrite_once,
)
from aeg_shakespeare.process.history import ProcessWord


def word(*steps):
    return ProcessWord(tuple(steps))


def test_ordered_relation_normalizes_without_commuting_processes_by_default():
    swap = WordRewriteRule(word("B", "A"), word("A", "B"), name="BA->AB")

    assert rewrite_once(word("A", "B"), (swap,)) is None
    result = normalize_word(word("B", "A", "B", "A"), (swap,))

    assert result.terminated
    assert result.reason == "normal_form"
    assert result.normal_form == word("A", "A", "B", "B")
    assert result.rewrite_steps == 3
    assert [step.position for step in result.trace] == [0, 2, 1]


def test_rewrite_trace_preserves_literal_history_while_relation_compresses_depth():
    contract = WordRewriteRule(word("A", "A"), word("A"), name="contract")
    original = word("A", "A", "A", "A")
    result = normalize_word(original, (contract,))

    assert result.original == original
    assert result.normal_form == word("A")
    assert result.rewrite_steps == 3
    assert result.depth_delta == -3
    assert result.trace[0].before == original
    assert result.trace[-1].after == word("A")


def test_nonterminating_relation_system_returns_cycle_certificate():
    to_b = WordRewriteRule(word("A"), word("B"), name="A->B")
    to_a = WordRewriteRule(word("B"), word("A"), name="B->A")

    result = normalize_word(word("A"), (to_b, to_a), max_steps=10)
    assert not result.terminated
    assert result.reason == "cycle"
    assert result.normal_form == word("A")
    assert result.rewrite_steps == 2


def test_rewrite_budget_is_explicit_when_normalization_has_not_finished():
    contract = WordRewriteRule(word("A", "A"), word("A"), name="contract")
    result = normalize_word(word("A", "A", "A", "A"), (contract,), max_steps=1)

    assert not result.terminated
    assert result.reason == "max_steps"
    assert result.normal_form == word("A", "A", "A")
