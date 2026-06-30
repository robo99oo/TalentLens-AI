from pathlib import Path
from docx import Document


class JDParser:
    """
    Reads the Job Description and creates a simple role profile.
    """

    def __init__(self, jd_path):
        self.jd_path = Path(jd_path)

    def extract_text(self):
        if not self.jd_path.exists():
            raise FileNotFoundError(f"Job Description not found: {self.jd_path}")

        document = Document(self.jd_path)
        paragraphs = []

        for para in document.paragraphs:
            if para.text.strip():
                paragraphs.append(para.text.strip())

        return "\n".join(paragraphs)

    def build_role_profile(self):
        jd_text = self.extract_text()
        lower = jd_text.lower()

        important_skills = [
            "python", "embeddings", "retrieval", "ranking",
            "vector database", "hybrid search", "faiss", "milvus",
            "elasticsearch", "opensearch", "qdrant", "weaviate",
            "llm", "fine-tuning", "learning-to-rank",
            "ndcg", "mrr", "map", "a/b testing"
        ]

        found_skills = []

        for skill in important_skills:
            if skill in lower:
                found_skills.append(skill)

        return {
            "job_description": jd_text,
            "required_skills": found_skills,
            "experience": "5-9 years",
            "preferred_location": [
                "pune", "noida", "delhi ncr", "hyderabad", "mumbai"
            ],
            "role_focus": [
                "production ml",
                "candidate ranking",
                "retrieval systems",
                "product engineering",
                "evaluation frameworks"
            ]
        }