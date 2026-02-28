from fastapi import FastAPI, HTTPException
from app.models import EvaluationRequest, EvaluationResponse
from app.profile_parser import parse_profile
from app.tiering_engine import evaluate_profile
from app.question_generator import generate_questions
from app.tiering_engine import evaluate_profile, generate_risk_flags

app = FastAPI()


@app.post("/evaluate", response_model=EvaluationResponse)
def evaluate(request: EvaluationRequest):

    # 🔹 Input validation
    if not request.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty.")

    if not request.job_description.strip():
        raise HTTPException(status_code=400, detail="Job description cannot be empty.")

    profile = parse_profile(request.resume_text, request.job_description)
    tier_result = evaluate_profile(profile, request.job_description)

    risk_flags = generate_risk_flags(profile, tier_result)

    profile_summary = f"Skills: {profile.skills}, Impact: {profile.impact_statements}"
    questions = generate_questions(profile_summary, tier_result.tier)

    return EvaluationResponse(
        tier_result=tier_result,
        risk_flags=risk_flags,
        questions=questions
    )