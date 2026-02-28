from pydantic import BaseModel
from typing import List, Optional


class EvaluationRequest(BaseModel):
    resume_text: str
    job_description: str


class CandidateProfile(BaseModel):
    skills: List[str]
    impact_statements: List[str]
    leadership_indicators: List[str]
    years_experience: Optional[float] = None


class TierResult(BaseModel):
    tier: str
    reasoning: List[str]
    skill_score: float
    impact_score: float
    leadership_score: float


class EvaluationResponse(BaseModel):
    tier_result: TierResult
    questions: List[str]