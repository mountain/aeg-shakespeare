"""Frozen acceptance surface for the stopped-process task quotient."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "sonnet" / "stochastic-feedback-trap-first-passage" / "04-phase2-task-quotient-contract.md"


def test_phase2_contract_freezes_full_task_payload_and_red_team():
    text = CONTRACT.read_text()
    for required in (
        "diffusion variance",
        "absorbing sections",
        "section labels",
        "initial point",
        "clock",
        "all 242 monotone presentations",
        "precisely",
        "the affine presentations pass",
        "canonical **class**",
        "Kill and shrink conditions",
    ):
        assert required in text
