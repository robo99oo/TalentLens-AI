class ReasoningEngine:
    def build_reason(self, candidate, score):
        profile = candidate.get("profile", {})
        signals = candidate.get("redrob_signals", {})
        skills = candidate.get("skills", [])
        career = candidate.get("career_history", [])

        title = profile.get("current_title", "Candidate")
        years = profile.get("years_of_experience", "unknown")
        location = profile.get("location", "unknown location")

        skill_names = [s.get("name", "") for s in skills[:6] if s.get("name")]
        skill_text = ", ".join(skill_names) if skill_names else "relevant technical skills"

        career_text = " ".join(
            job.get("description", "") for job in career
        ).lower()

        evidence = []

        if any(word in career_text for word in ["retrieval", "ranking", "search", "recommendation", "matching"]):
            evidence.append("career history shows search, ranking, retrieval, or recommendation system exposure")

        if any(word in career_text for word in ["production", "deployed", "scale", "real users", "pipeline"]):
            evidence.append("has evidence of production or scalable system experience")

        if signals.get("open_to_work_flag"):
            evidence.append("is open to work")

        response_rate = signals.get("recruiter_response_rate", 0)
        if response_rate >= 0.5:
            evidence.append(f"has strong recruiter response rate of {response_rate:.0%}")
        elif response_rate > 0:
            evidence.append(f"has recruiter response rate of {response_rate:.0%}")

        notice = signals.get("notice_period_days", "unknown")

        if not evidence:
            evidence.append("shows partial alignment with the JD through technical and behavioral signals")

        return (
            f"{title} with {years} years of experience from {location}. "
            f"Relevant skills include {skill_text}. "
            f"Ranked with score {score:.2f} because the candidate {', and '.join(evidence[:3])}; "
            f"notice period is {notice} days."
        )