class ReasoningEngine:
    def build_reason(self, candidate, score):
        profile = candidate.get("profile", {})
        signals = candidate.get("redrob_signals", {})
        skills = candidate.get("skills", [])

        title = profile.get("current_title", "Candidate")
        years = profile.get("years_of_experience", "unknown")
        location = profile.get("location", "unknown location")

        skill_names = [s.get("name", "") for s in skills[:8]]
        skill_text = ", ".join(skill_names)

        response_rate = signals.get("recruiter_response_rate", 0)
        notice = signals.get("notice_period_days", "unknown")

        return (
            f"{title} with {years} years of experience from {location}; "
            f"relevant skills include {skill_text}. "
            f"Score {score:.2f} reflects technical fit, experience, recruiter response rate "
            f"{response_rate:.0%}, and notice period of {notice} days."
        )