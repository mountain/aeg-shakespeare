"""Frozen numerical first-passage acceptance surface."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "sonnet" / "stochastic-feedback-trap-first-passage" / "06-phase3-first-passage-contract.md"


def test_phase3_contract_freezes_independent_solvers_units_and_red_team():
    text = CONTRACT.read_text()
    for required in (
        "epsilon              1/4",
        "u+u^3",
        "2u+u^3",
        "101, 201, 401",
        "independently evolved per chart",
        "timestep refinement check",
        "uniform target-coordinate mesh",
        "L/V",
        "Kill and shrink conditions",
    ):
        assert required in text
