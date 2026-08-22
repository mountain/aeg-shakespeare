from aeg_shakespeare import (
    ProcessWord,
    enumerate_process_words,
    histories_task_equivalent,
    history_process_jet_signature,
)


def word(*steps):
    return ProcessWord(tuple(steps))


def transition(state, step):
    a, b = state
    if step == "a":
        return (a + 1, b)
    if step == "b":
        return (a, b + 1)
    if step == "mix":
        return (a + b, b)
    raise ValueError(step)


def observe_a(state):
    return state[0]


def test_free_continuation_tree_is_ordered_and_bounded():
    words = enumerate_process_words(("a", "b"), 2)
    assert words == (
        word(),
        word("a"),
        word("b"),
        word("a", "a"),
        word("a", "b"),
        word("b", "a"),
        word("b", "b"),
    )


def test_histories_can_be_task_equivalent_even_when_hidden_state_differs():
    initial = (0, 0)
    left = word("b")
    right = word("b", "b")

    assert left != right
    assert histories_task_equivalent(
        left,
        right,
        initial,
        ("a", "b"),
        transition,
        observe_a,
        depth=2,
    )

    left_signature = history_process_jet_signature(
        left,
        initial,
        ("a", "b"),
        transition,
        observe_a,
        depth=2,
    )
    right_signature = history_process_jet_signature(
        right,
        initial,
        ("a", "b"),
        transition,
        observe_a,
        depth=2,
    )
    assert left_signature.observations == right_signature.observations


def test_future_continuation_can_reveal_state_hidden_from_current_task_value():
    initial = (0, 0)
    left = word("b")
    right = word("b", "b")

    # Both histories currently have the same task observation a=0, but allowing
    # the future process "mix" makes the hidden b-coordinate task-relevant.
    assert not histories_task_equivalent(
        left,
        right,
        initial,
        ("a", "b", "mix"),
        transition,
        observe_a,
        depth=1,
    )
