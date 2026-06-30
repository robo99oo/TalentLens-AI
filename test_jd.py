from src.jd_parser import JDParser

parser = JDParser(
    "challenge_data/India_runs_data_and_ai_challenge/job_description.docx"
)

profile = parser.build_role_profile()

print(profile)