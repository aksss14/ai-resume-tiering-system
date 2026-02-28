import google.generativeai as genai
import os
from dotenv import load_dotenv

import google.generativeai as genai

for m in genai.list_models():
    print(m.name, "→", m.supported_generation_methods)

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(profile_summary: str, tier: str):

    if tier == "A":
        difficulty = "advanced system design and architectural"
    elif tier == "B":
        difficulty = "intermediate implementation-focused"
    else:
        difficulty = "fundamental conceptual"

    prompt = f"""
You are an expert technical interviewer.

Candidate Summary:
{profile_summary}

Generate 5 {difficulty} technical interview questions tailored specifically
to this candidate's background.

Return them as a numbered list.
"""

    try:
        response = model.generate_content(prompt)
        content = response.text.strip()

        questions = [line.strip() for line in content.split("\n") if line.strip()]
        return questions

    except Exception as e:
        return [f"Question generation failed: {str(e)}"]