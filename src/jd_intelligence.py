class JDIntelligence:
    def build_weights(self, role_profile: object) -> dict[str, float]:
        jd_text = role_profile.get("job_description", "").lower()

        weights = {
            "technical": 0.20,
            "career": 0.25,
            "experience": 0.15,
            "behavior": 0.15,
            "product": 0.10,
            "decision": 0.15
        }

        if "retrieval" in jd_text or "ranking" in jd_text or "search" in jd_text:
            weights["career"] += 0.05
            weights["decision"] += 0.03
            weights["technical"] -= 0.03

        if "evaluation" in jd_text or "ndcg" in jd_text or "mrr" in jd_text or "map" in jd_text:
            weights["career"] += 0.03
            weights["decision"] += 0.02
            weights["behavior"] -= 0.02

        if "product" in jd_text or "ship" in jd_text or "users" in jd_text:
            weights["product"] += 0.04
            weights["decision"] += 0.03
            weights["technical"] -= 0.03

        total = sum(weights.values())

        for key in weights:
            weights[key] = weights[key] / total

        return weights