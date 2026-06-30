# 🚀 TalentLens AI

## Explainable Candidate Ranking Engine for AI Hiring

TalentLens AI ranks candidates for a given job description using a hybrid scoring engine based on:

- Technical skills
- Career history
- Behavioral signals
- Product experience
- Hiring risk indicators

The system generates the **Top 100 best-fit candidates** with explainable reasoning.

---

# 🎯 Goal

To identify the best candidates from a large candidate pool while going beyond simple keyword matching.

---

# 🧠 What Makes TalentLens AI Different?

- ✅ JD-aware scoring
- ✅ Career Intelligence Analysis
- ✅ Behavioral Signal Weighting
- ✅ Product / Company Fit Scoring
- ✅ Hiring Risk Detection
- ✅ Explainable AI Reasoning

---

# 🏗️ System Architecture

```text
                Job Description
                        │
                        ▼
                  JD Parser
                        │
                        ▼
                  Role Profile
                        │
                        ▼
                Candidate Loader
                        │
                        ▼
                Career Analyzer
                        │
                        ▼
                 Scoring Engine
                        │
                        ▼
                Reasoning Engine
                        │
                        ▼
           Top 100 Ranked Candidates
```

---

# 📂 Project Structure

```text
TalentLens-AI/

├── src/
│   ├── loader.py
│   ├── jd_parser.py
│   ├── career_analyzer.py
│   ├── scoring_engine.py
│   └── reasoning.py

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
- JSONL
- DOCX Parsing
- Explainable AI
- Rule-Based Ranking
- Git
- GitHub

---

# 📊 Scoring Signals

TalentLens AI evaluates candidates using:

- Technical Skill Match
- Career Intelligence
- Production Experience
- Company Background
- Behavioral Signals
- Recruiter Response Rate
- Notice Period
- Interview Completion Rate
- Open-to-Work Status
- Hiring Risk Detection

---

# 🚀 How to Run

Clone the repository

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

# 🎯 Future Roadmap

- Hybrid AI + Rule-Based Ranking
- Semantic Candidate Matching
- Resume Parser
- Recruiter Dashboard
- Candidate Insights
- Interview Recommendation Engine
- LLM-based Career Intelligence

---

# 👩‍💻 Author

## Kshiti Tyagi

**AI/ML Engineer | Generative AI | RAG | LLMs | Agentic AI**
