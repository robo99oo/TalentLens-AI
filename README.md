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

```text
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
      ↓
Top 100 Candidates CSV
