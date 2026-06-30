# 🚀 TalentLens AI

> **An AI-Powered Intelligent Candidate Discovery & Ranking System**
>
> Built for the **India Runs Data & AI Challenge**.

---

# 📌 Overview

TalentLens AI is an intelligent recruitment system designed to rank candidates based on much more than keyword matching.

Unlike traditional Applicant Tracking Systems (ATS), TalentLens AI evaluates:

- Technical skills
- Career trajectory
- Production experience
- Behavioral hiring signals
- Recruiter engagement
- Company background
- Explainable AI reasoning

The system produces a ranked list of the Top 100 candidates best suited for a given Job Description.

---

# 🎯 Problem Statement

Traditional recruitment systems rely heavily on keyword matching.

This often leads to:

- False positives
- Missing strong candidates
- Ignoring production experience
- Poor recruiter experience

TalentLens AI solves this by combining multiple intelligence layers into a unified ranking engine.

---

# 🧠 Key Features

✅ Intelligent JD Parser

✅ Candidate Profile Loader

✅ Career Intelligence Engine

✅ Technical Skill Matching

✅ Behavioral Signal Analysis

✅ Recruiter-Aware Ranking

✅ Explainable AI Reasoning

✅ Top-100 Candidate Generation

---

# 🏗 Architecture

```

                 Job Description
                        │
                        ▼
                 JD Intelligence
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼

 Skill Matcher   Career Analyzer   Behavior Analyzer

      │                 │                 │
      └─────────────────┼─────────────────┘
                        ▼

             Intelligent Scoring Engine
                        │
                        ▼

              Explainable AI Reasoning
                        │
                        ▼

            Ranked Top 100 Candidates

```

---

# 📂 Project Structure

```

TalentLens_AI/

├── src/

│ ├── loader.py

│ ├── jd_parser.py

│ ├── career_analyzer.py

│ ├── scoring_engine.py

│ └── reasoning.py

│

├── challenge_data/

├── rank.py

├── submission.csv

├── test_loader.py

├── test_jd.py

└── test_score.py

```

---

# ⚙️ Technology Stack

- Python 3.11
- JSON
- DOCX Parser
- Rule-Based AI
- Career Intelligence Engine
- Explainable AI
- Git
- GitHub

---

# 🧩 Ranking Factors

The ranking engine evaluates candidates using:

- Technical Skills
- Relevant Experience
- Career Progression
- Production AI Experience
- Behavioral Signals
- Recruiter Response Rate
- Notice Period
- Open-to-Work Status
- Company Background
- Hiring Risk Detection

---

# 📊 Workflow

Job Description

↓

JD Intelligence

↓

Candidate Analysis

↓

Multi-Factor Scoring

↓

Explainable Ranking

↓

Top 100 Candidates

---

# 🚀 How to Run

Clone repository

```bash
git clone https://github.com/robo99oo/TalentLens-AI.git
```

Install dependencies

```bash
pip install python-docx
```

Generate rankings

```bash
python rank.py --candidates challenge_data/India_runs_data_and_ai_challenge/candidates.jsonl --out submission.csv
```

Validate submission

```bash
python challenge_data/India_runs_data_and_ai_challenge/validate_submission.py submission.csv
```

---

# 🎯 Future Enhancements

- Semantic Candidate Matching
- Hybrid AI + Rule-Based Ranking
- Recruiter Dashboard
- Resume Parsing
- Interview Recommendation Engine
- Candidate Insights Dashboard
- LLM-based Career Intelligence

---

# 👩‍💻 Author

**Kshiti Tyagi**

AI / ML Engineer

Generative AI | RAG | LLM | Agentic AI | Intelligent Hiring Systems

---

# ⭐ If you found this project interesting, consider giving it a star!
