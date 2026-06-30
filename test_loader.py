from src.loader import CandidateLoader

loader = CandidateLoader(
    "challenge_data/India_runs_data_and_ai_challenge/candidates.jsonl"
)

candidates = loader.load_candidates()

print(f"Total Candidates: {len(candidates)}")

print(candidates[0])