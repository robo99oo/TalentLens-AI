class RecruiterDecisionEngine:
    def decision_score(self, candidate: object) -> int:
        profile = candidate.get("profile", {})
        career = candidate.get("career_history", [])
        signals = candidate.get("redrob_signals", {})

        title = str(profile.get("current_title", "")).lower()
        years = profile.get("years_of_experience", 0)
        career_text = " ".join(job.get("description", "") for job in career).lower()

        score = 0

        if 5 <= years <= 9:
            score += 20
        elif 4 <= years < 5:
            score += 12
        elif years > 12:
            score -= 8

        if any(word in title for word in ["ai engineer", "ml engineer", "machine learning", "applied scientist", "search engineer"]):
            score += 18

        if any(word in career_text for word in ["search", "retrieval", "ranking", "recommendation", "matching"]):
            score += 22

        if any(word in career_text for word in ["production", "deployed", "scale", "real users", "latency", "monitoring"]):
            score += 18

        if any(word in career_text for word in ["ndcg", "mrr", "map", "a/b", "ab test", "evaluation", "benchmark"]):
            score += 12

        if signals.get("open_to_work_flag"):
            score += 8

        if signals.get("recruiter_response_rate", 0) >= 0.5:
            score += 8

        if signals.get("notice_period_days", 90) <= 30:
            score += 6

        return max(0, min(score, 100))