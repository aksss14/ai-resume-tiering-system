from app.models import CandidateProfile, TierResult


def calculate_skill_score(profile: CandidateProfile, jd_text: str):
    jd_words = set(jd_text.lower().split())
    if not jd_words:
        return 0.0
    return min(len(profile.skills) / len(jd_words), 1.0)


def calculate_impact_score(profile: CandidateProfile):
    return min(len(profile.impact_statements) / 5, 1.0)


def calculate_leadership_score(profile: CandidateProfile):
    return min(len(profile.leadership_indicators) / 3, 1.0)


def classify_tier(skill_score: float, impact_score: float):
    if skill_score > 0.6 and impact_score > 0.5:
        return "A"
    elif skill_score > 0.3:
        return "B"
    else:
        return "C"


def evaluate_profile(profile: CandidateProfile, jd_text: str) -> TierResult:
    skill_score = calculate_skill_score(profile, jd_text)
    impact_score = calculate_impact_score(profile)
    leadership_score = calculate_leadership_score(profile)

    tier = classify_tier(skill_score, impact_score)

    reasoning = [
        f"Skill overlap score: {round(skill_score, 2)}",
        f"Impact score: {round(impact_score, 2)}",
        f"Leadership signals detected: {len(profile.leadership_indicators)}"
    ]

    return TierResult(
        tier=tier,
        reasoning=reasoning,
        skill_score=skill_score,
        impact_score=impact_score,
        leadership_score=leadership_score,
    )

def generate_risk_flags(profile: CandidateProfile, tier_result: TierResult):

    flags = []

    if tier_result.skill_score < 0.3:
        flags.append("Weak skill overlap with job description")

    if tier_result.impact_score < 0.3:
        flags.append("Low quantified impact evidence")

    if len(profile.leadership_indicators) == 0:
        flags.append("No leadership signals detected")

    return flags