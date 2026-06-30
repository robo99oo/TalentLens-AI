from src.loader import CandidateLoader
from src.jd_parser import JDParser
from src.scoring_engine import ScoringEngine

# Load candidates
loader = CandidateLoader(
    "challenge_data/India_runs_data_and_ai_challenge/candidates.jsonl"
)
candidates = loader.load_candidates()

# Load Job Description
parser = JDParser(
    "challenge_data/India_runs_data_and_ai_challenge/job_description.docx"
)
role_profile = parser.build_role_profile()

# Initialize scorer
scorer = ScoringEngine()

# Score first 5 candidates
for candidate in candidates[:5]:
    score = scorer.final_score(candidate, role_profile)
    print(candidate["candidate_id"], score)