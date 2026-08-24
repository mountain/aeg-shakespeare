"""Frozen final reset-Bellman acceptance surface."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "sonnet" / "stochastic-feedback-trap-first-passage" / "08-phase4-reset-bellman-contract.md"


def test_phase4_contract_freezes_actions_bellman_units_and_red_teams():
    text = CONTRACT.read_text()
    for required in (
        "left-reset",
        "center-reset",
        "right-reset",
        "J=\\min_a",
        "right-exit",
        "J_phys = (L/V) J",
        "Swapping absorbing labels",
        "coordinate-distance reset charge",
        "closes the current canonicalization–Bellman research line",
    ):
        assert required in text
