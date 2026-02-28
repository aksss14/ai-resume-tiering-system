Perfect. I’ll frame a **clean, professional, internship-ready README** for you.

You can copy-paste this directly into `README.md`.

---

# AI Resume Shortlisting & Interview Assistant

### (Option C — Intelligent Tiering & Question Generator)

---

## Overview

This project implements an AI-powered resume evaluation system that:

* Compares candidate resumes against job descriptions
* Classifies candidates into Tier A / B / C
* Provides explainable reasoning for classification
* Highlights potential hiring risk flags
* Generates adaptive technical interview questions using Gemini LLM

The focus of this implementation is **Option C — Intelligent Tiering & Question Generator**, with an emphasis on explainability, robustness, and modular architecture.

---

## Problem Statement

Hiring teams often need to:

* Quickly shortlist candidates
* Understand why a candidate is strong or weak
* Identify potential risks
* Generate role-specific interview questions

This system automates that process while maintaining transparency in classification decisions.

---

## System Architecture

### High-Level Flow

```
Resume + Job Description
        ↓
Profile Parsing Layer
        ↓
Deterministic Tiering Engine
        ↓
Risk Flag Generator
        ↓
LLM Question Generator (Gemini 2.5 Flash)
        ↓
Structured API Response
```

---

## Design Principles

### Deterministic Tiering (Explainable Core)

Tier classification is rule-based to ensure:

* Transparency
* Testability
* Stability across runs
* Predictable behavior

LLMs are not used for classification to avoid opaque decision-making.

---

### LLM for Adaptive Question Generation

Gemini 2.5 Flash is used to:

* Generate context-aware interview questions
* Scale question difficulty based on candidate tier
* Tailor questions to detected skills

---

### Risk Flags (Standout Feature)

The system surfaces structured hiring concerns such as:

* Weak skill overlap with JD
* Low quantified impact evidence
* No leadership indicators

This makes the output actionable for interviewers, not just analytical.

---

## Tiering Logic

Signals extracted:

* Skill overlap with JD
* Quantified achievements (%, numbers)
* Leadership indicators

Classification rules:

| Tier | Criteria                             |
| ---- | ------------------------------------ |
| A    | Strong skill overlap + strong impact |
| B    | Moderate skill overlap               |
| C    | Weak overlap                         |

Tier decisions include structured reasoning in the response.

---

## API Structure

### Request

```json
{
  "resume_text": "...",
  "job_description": "..."
}
```

### Response

```json
{
  "tier_result": {
    "tier": "B",
    "reasoning": [...],
    "skill_score": 0.45,
    "impact_score": 0.3,
    "leadership_score": 0.66
  },
  "risk_flags": [
    "Low quantified impact evidence"
  ],
  "questions": [
    "Explain how REST APIs work...",
    "Describe optimistic locking..."
  ]
}
```

---

## Testing

Unit tests validate the deterministic tiering logic.

Run tests:

```bash
pytest
```

---

## Setup & Run

### Run server

```bash
uvicorn app.main:app --reload --port 8001
```

Open:

```
http://127.0.0.1:8001/docs
```

---

## Assumptions & Trade-offs

* Resume processed as plain text
* Skill overlap is lexical (no embeddings)
* No persistent storage (stateless design)
* Impact detection is regex-based

Time-boxed design decisions prioritized clarity and modularity.

---

## Future Improvements

* Embedding-based semantic skill matching
* Feedback loop from interviewer outcomes
* Bias detection mechanisms
* Resume PDF ingestion
* Deployment-ready containerization

---

## Scalability Considerations

To scale to 10,000+ resumes per day:

* Move parsing and question generation to async workers
* Use batch LLM calls where possible
* Cache embeddings (if added)

---

## Security & Secrets

* API keys are injected via environment variables
* No credentials are stored in the repository
* Sensitive files are excluded via `.gitignore`

---

## AI Usage Disclosure

AI tools were used for:

* Architecture brainstorming
* Debugging assistance
* Prompt refinement

---

## Project Structure

```
app/
  main.py
  models.py
  profile_parser.py
  tiering_engine.py
  question_generator.py

tests/
  test_tiering.py

requirements.txt
README.md
.gitignore
```

---
like an engineer.
