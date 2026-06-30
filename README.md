# 🚀 TalentLens AI

**Explainable Candidate Ranking Engine for AI Hiring**

TalentLens AI ranks candidates for a given job description using a hybrid scoring engine based on skills, career history, behavioral signals, and hiring risk indicators.

## 🎯 Goal

To identify the top 100 best-fit candidates from a large candidate pool while going beyond simple keyword matching.

## 🧠 What Makes It Different

- JD-aware scoring
- Career intelligence analysis
- Behavioral signal weighting
- Product/company fit scoring
- Risk detection for keyword-heavy or suspicious profiles
- Explainable reasoning for each ranked candidate

## 🏗️ Architecture

Job Description
      ↓
JD Parser
      ↓
Role Profile
      ↓
Candidate Loader
      ↓
Career Analyzer
      ↓
Scoring Engine
      ↓
Reasoning Engine

## 📂 Project Structure

TalentLens-AI/
├── src/
│   ├── loader.py
│   ├── jd_parser.py
│   ├── career_analyzer.py
│   ├── scoring_engine.py
│   └── reasoning.py
├── rank.py
├── submission.csv
├── test_loader.py
├── test_jd.py
└── test_score.py
      ↓
Top 100 Candidates CSV

## ⚙️ How to Run

pip install python-docx
python rank.py --candidates challenge_data/India_runs_data_and_ai_challenge/candidates.jsonl --out submission.csv
python challenge_data/India_runs_data_and_ai_challenge/validate_submission.py submission.csv

## 📊 Scoring Signals
Technical skill match
Retrieval/ranking/search experience
Production system evidence
Years of experience
Product-company alignment
Recruiter response rate
Interview completion rate
Notice period
Open-to-work status
Risk penalty

## 🛠️ Tech Stack

Python 3.11, JSONL, DOCX parsing, rule-based ranking, feature engineering, GitHub.

## 👩‍💻 Author

Kshiti Tyagi
AI/ML Engineer | Generative AI | RAG | LLMs | Agentic AI
