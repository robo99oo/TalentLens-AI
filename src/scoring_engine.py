import json

from src.career_analyzer import CareerAnalyzer
from src.behavior_analyzer import BehaviorAnalyzer
from src.recruiter_decision import RecruiterDecisionEngine
from src.jd_intelligence import JDIntelligence
from src.evidence_engine import EvidenceEngine

class ScoringEngine:
    def __init__(self):
        self.bad_industries = ["it services", "consulting"]
        self.good_industries = ["software", "internet", "saas", "ai", "product"]
        self.career_analyzer = CareerAnalyzer()
        self.behavior_analyzer = BehaviorAnalyzer()
        self.recruiter_decision = RecruiterDecisionEngine()
        self.jd_intelligence = JDIntelligence()
        self.evidence_engine = EvidenceEngine()

    def candidate_text(self, candidate):
        return json.dumps(candidate).lower()

    def technical_score(self, candidate, role_profile):
        candidate_skills = [
            skill.get("name", "").lower()
            for skill in candidate.get("skills", [])
        ]

        required_skills = [
            skill.lower()
            for skill in role_profile.get("required_skills", [])
        ]

        matched = []

        for skill in required_skills:
            for candidate_skill in candidate_skills:
                if skill in candidate_skill or candidate_skill in skill:
                    matched.append(skill)
                    break

        if not required_skills:
            return 0

        return round((len(matched) / len(required_skills)) * 100, 2)

    def experience_score(self, candidate):
        profile = candidate.get("profile", {})
        years = profile.get("years_of_experience", 0)

        if 5 <= years <= 9:
            score = 90
        elif 4 <= years < 5:
            score = 75
        elif 9 < years <= 12:
            score = 70
        else:
            score = 45

        industry = str(profile.get("current_industry", "")).lower()

        if any(bad in industry for bad in self.bad_industries):
            score -= 15

        if any(good in industry for good in self.good_industries):
            score += 10

        return max(0, min(score, 100))

    def risk_penalty(self, candidate):
        text = self.candidate_text(candidate)
        penalty = 0

        keyword_count = sum(
            text.count(k)
            for k in ["ai", "ml", "llm", "rag", "langchain", "openai", "genai"]
        )

        if keyword_count > 45:
            penalty += 20

        skills = candidate.get("skills", [])
        expert_zero = 0

        for skill in skills:
            prof = str(skill.get("proficiency", "")).lower()
            months = skill.get("duration_months", 0)

            if prof == "expert" and months <= 3:
                expert_zero += 1

        if expert_zero >= 3:
            penalty += 25

        title = str(candidate.get("profile", {}).get("current_title", "")).lower()

        if "marketing" in title and ("machine learning" in text or "llm" in text):
            penalty += 30

        return penalty

    def final_score(self, candidate, role_profile):
        tech = self.technical_score(candidate, role_profile)
        career = self.career_analyzer.career_score(candidate)
        product = self.career_analyzer.product_company_score(candidate)
        exp = self.experience_score(candidate)
        behavior = self.behavior_analyzer.behavior_score(candidate)
        decision = self.recruiter_decision.decision_score(candidate)
        weights = self.jd_intelligence.build_weights(role_profile)
        risk = self.risk_penalty(candidate)
        evidence = self.evidence_engine.evidence_score(candidate)

        final = (
                weights["technical"] * tech +
                weights["career"] * career +
                weights["experience"] * exp +
                weights["behavior"] * behavior +
                weights["product"] * product +
                weights["decision"] * decision +
                0.10 * evidence -
                risk
        )
        
        return max(0, round(final, 4))