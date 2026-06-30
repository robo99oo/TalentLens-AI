class EvidenceEngine:
    def evidence_score(self, candidate):
        career = candidate.get("career_history", [])
        text = " ".join(job.get("description", "") for job in career).lower()

        score = 0

        strong_evidence = [
            "deployed", "production", "real users", "scale",
            "ranking system", "recommendation engine",
            "search infrastructure", "retrieval system",
            "a/b testing", "ndcg", "mrr", "map"
        ]

        weak_evidence = [
            "tutorial", "course", "demo", "side project",
            "kaggle", "learning", "experimented"
        ]

        for word in strong_evidence:
            if word in text:
                score += 10

        for word in weak_evidence:
            if word in text:
                score -= 5

        return max(0, min(score, 100))