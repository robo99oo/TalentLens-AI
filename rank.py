import argparse
import csv

from src.loader import CandidateLoader
from src.jd_parser import JDParser
from src.scoring_engine import ScoringEngine
from src.reasoning import ReasoningEngine


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", required=True)
    parser.add_argument("--out", default="submission.csv")
    args = parser.parse_args()

    loader = CandidateLoader(args.candidates)
    candidates = loader.load_candidates()

    jd_parser = JDParser(
        "challenge_data/India_runs_data_and_ai_challenge/job_description.docx"
    )
    role_profile = jd_parser.build_role_profile()

    scorer = ScoringEngine()
    reasoner = ReasoningEngine()

    scored = []

    for candidate in candidates:
        score = scorer.final_score(candidate, role_profile)
        scored.append((candidate["candidate_id"], score, candidate))

    scored.sort(key=lambda x: (-x[1], x[0]))

    top_100 = scored[:100]

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["candidate_id", "rank", "score", "reasoning"]
        )
        writer.writeheader()

        for rank, (candidate_id, score, candidate) in enumerate(top_100, start=1):
            writer.writerow({
                "candidate_id": candidate_id,
                "rank": rank,
                "score": score,
                "reasoning": reasoner.build_reason(candidate, score)
            })

    print(f"Created {args.out} with 100 ranked candidates.")


if __name__ == "__main__":
    main()