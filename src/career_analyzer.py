import json


class CareerAnalyzer:
    def __init__(self):
        self.high_value_keywords = [
            "retrieval", "ranking", "search", "recommendation",
            "matching", "embedding", "vector", "faiss", "milvus",
            "elasticsearch", "opensearch", "qdrant", "weaviate",
            "production", "deployed", "scale", "real users",
            "a/b", "ab test", "ndcg", "mrr", "map",
            "evaluation", "relevance", "hybrid search"
        ]

        self.product_keywords = [
            "product", "saas", "marketplace", "platform",
            "startup", "internet", "software"
        ]

    def get_career_text(self, candidate):
        career_history = candidate.get("career_history", [])
        return json.dumps(career_history).lower()

    def career_score(self, candidate):
        text = self.get_career_text(candidate)
        score = 0

        for keyword in self.high_value_keywords:
            if keyword in text:
                score += 6

        return min(score, 100)

    def product_company_score(self, candidate):
        profile = candidate.get("profile", {})
        career_history = candidate.get("career_history", [])

        text = (
            str(profile.get("current_industry", "")) + " " +
            json.dumps(career_history)
        ).lower()

        score = 0

        for keyword in self.product_keywords:
            if keyword in text:
                score += 10

        if "it services" in text or "consulting" in text:
            score -= 15

        return max(0, min(score, 100))