import json


class CareerAnalyzer:
    def __init__(self):
        self.production_keywords = [
            "production", "deployed", "real users", "scale", "latency",
            "monitoring", "pipeline", "on-call", "quality checks"
        ]

        self.retrieval_keywords = [
            "retrieval", "ranking", "search", "recommendation",
            "matching", "relevance", "bm25", "hybrid search"
        ]

        self.infrastructure_keywords = [
            "embedding", "embeddings", "vector", "faiss", "milvus",
            "pinecone", "qdrant", "weaviate", "opensearch", "elasticsearch"
        ]

        self.evaluation_keywords = [
            "ndcg", "mrr", "map", "a/b", "ab test", "offline evaluation",
            "benchmark", "feedback loop", "quality regression"
        ]

        self.product_keywords = [
            "product", "platform", "marketplace", "saas", "startup",
            "users", "customer", "pm", "growth"
        ]

    def get_career_text(self, candidate):
        career_history = candidate.get("career_history", [])
        return json.dumps(career_history).lower()

    def keyword_score(self, text, keywords, weight):
        score = 0
        for keyword in keywords:
            if keyword in text:
                score += weight
        return score

    def career_score(self, candidate):
        text = self.get_career_text(candidate)

        production = self.keyword_score(text, self.production_keywords, 6)
        retrieval = self.keyword_score(text, self.retrieval_keywords, 8)
        infrastructure = self.keyword_score(text, self.infrastructure_keywords, 7)
        evaluation = self.keyword_score(text, self.evaluation_keywords, 7)
        product = self.keyword_score(text, self.product_keywords, 5)

        score = production + retrieval + infrastructure + evaluation + product

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
                score += 8

        if "it services" in text and "product" not in text:
            score -= 15

        return max(0, min(score, 100))