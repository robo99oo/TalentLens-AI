class BehaviorAnalyzer:
    def behavior_score(self, candidate):
        signals = candidate.get("redrob_signals", {})
        score = 0

        profile_complete = signals.get("profile_completeness_score", 0)
        response_rate = signals.get("recruiter_response_rate", 0)
        interview_rate = signals.get("interview_completion_rate", 0)
        notice = signals.get("notice_period_days", 90)
        github = signals.get("github_activity_score", -1)
        views = signals.get("profile_views_received_30d", 0)
        saved = signals.get("saved_by_recruiters_30d", 0)

        score += min(profile_complete, 100) * 0.15
        score += response_rate * 25
        score += interview_rate * 20

        if signals.get("open_to_work_flag"):
            score += 10

        if notice <= 30:
            score += 12
        elif notice <= 60:
            score += 6
        elif notice > 90:
            score -= 10

        if github >= 70:
            score += 10
        elif github >= 40:
            score += 6
        elif github >= 20:
            score += 3

        if views >= 50:
            score += 5

        if saved >= 5:
            score += 5

        if signals.get("verified_email"):
            score += 3
        if signals.get("verified_phone"):
            score += 3
        if signals.get("linkedin_connected"):
            score += 3

        return max(0, min(score, 100))