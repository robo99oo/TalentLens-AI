import json

from src.career_analyzer import CareerAnalyzer
from src.behavior_analyzer import BehaviorAnalyzer

class ScoringEngine:
    def __init__(self):
        self.bad_industries = ["it services", "consulting"]
        self.good_industries = ["software", "internet", "saas", "ai", "product"]
        self.career_analyzer = CareerAnalyzer()
        self.behavior_analyzer = BehaviorAnalyzer()

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

    def behavior_score(self, candidate):
        signals = candidate.get("redrob_signals", {})
        score = 0

        score += signals.get("profile_completeness_score", 0) * 0.15
        score += signals.get("recruiter_response_rate", 0) * 25
        score += signals.get("interview_completion_rate", 0) * 20

        if signals.get("open_to_work_flag"):
            score += 10
        if signals.get("verified_email"):
            score += 5
        if signals.get("verified_phone"):
            score += 5
        if signals.get("linkedin_connected"):
            score += 5

        notice = signals.get("notice_period_days", 90)
        if notice <= 30:
            score += 10
        elif notice > 90:
            score -= 10

        github = signals.get("github_activity_score", -1)
        if github >= 50:
            score += 10
        elif github >= 20:
            score += 5

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
        risk = self.risk_penalty(candidate)

        final = (
            0.25 * tech +
            0.30 * career +
            0.15 * exp +
            0.20 * behavior +
            0.10 * product -
            risk
        )

        return max(0, round(final, 4))