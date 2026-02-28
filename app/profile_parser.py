import re
import string
from app.models import CandidateProfile

LEADERSHIP_WORDS = [
    "led", "designed", "architected", 
    "owned", "spearheaded", "built"
]

IMPACT_PATTERN = r"\b\d+%|\b\d+\b"


def normalize_text(text: str):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def extract_skills(resume_text: str, jd_text: str):

    normalized_resume = normalize_text(resume_text)
    normalized_jd = normalize_text(jd_text)

    resume_words = set(normalize_text(resume_text).split())
    jd_words = set(normalized_jd.split())
    return list(jd_words.intersection(resume_words))


def extract_impact_statements(resume_text: str):
    return re.findall(IMPACT_PATTERN, resume_text)


def extract_leadership_indicators(resume_text: str):
    lower_text = resume_text.lower()
    return [word for word in LEADERSHIP_WORDS if word in lower_text]


def parse_profile(resume_text: str, jd_text: str) -> CandidateProfile:
    return CandidateProfile(
        skills=extract_skills(resume_text, jd_text),
        impact_statements=extract_impact_statements(resume_text),
        leadership_indicators=extract_leadership_indicators(resume_text),
    )
