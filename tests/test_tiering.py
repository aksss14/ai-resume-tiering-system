import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.models import CandidateProfile
from app.tiering_engine import evaluate_profile


def test_tier_a_candidate():
    profile = CandidateProfile(
        skills=["distributed", "systems", "rest", "scalability"],
        impact_statements=["40%"],
        leadership_indicators=["led", "designed"]
    )

    jd = "Looking for distributed systems and REST APIs engineer with scalability experience."

    result = evaluate_profile(profile, jd)

    assert result.tier in ["A", "B"]  # depending on scoring logic
    assert result.skill_score > 0


def test_tier_c_candidate():
    profile = CandidateProfile(
        skills=["python"],
        impact_statements=[],
        leadership_indicators=[]
    )

    jd = "Looking for distributed systems and REST APIs engineer with scalability experience."

    result = evaluate_profile(profile, jd)

    assert result.tier == "C"