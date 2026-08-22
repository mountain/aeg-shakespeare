"""Minimal cross-domain contract for task-relative presentation morphisms."""

from aeg_shakespeare.presentation.morphism import PresentationMorphism


def test_morphism_allows_heterogeneous_presentation_spaces():
    morphism = PresentationMorphism(
        source=("B2", (1, 1, 1)),
        target={"braid_group": "B3", "word": (1, 1, 1, 2)},
        task_semantics="standard-closure Alexander polynomial",
        certificate={"source": "t^2-t+1", "target": "t^2-t+1"},
        witness=("positive Markov stabilization", 2),
        label="trefoil stabilization",
    )

    assert morphism.source == ("B2", (1, 1, 1))
    assert morphism.target["braid_group"] == "B3"
    assert morphism.task_semantics == "standard-closure Alexander polynomial"
    assert morphism.certificate["source"] == morphism.certificate["target"]
    assert morphism.witness == ("positive Markov stabilization", 2)
    assert morphism.label == "trefoil stabilization"


def test_morphism_does_not_impose_a_universal_verifier_or_category():
    morphism = PresentationMorphism(
        source="raw presentation",
        target="quotient presentation",
        task_semantics=("observer", "Q"),
        certificate=("caller-defined", 0),
    )

    # These absences are intentional API boundaries, not missing helpers.
    assert not hasattr(morphism, "verified")
    assert not hasattr(morphism, "compose")
    assert not hasattr(morphism, "inverse")
    assert morphism.witness is None
