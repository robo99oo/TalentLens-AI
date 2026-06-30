import json
import gzip
from pathlib import Path


class CandidateLoader:
    """
    Loads candidate profiles from .jsonl or .jsonl.gz
    """

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load_candidates(self):
        candidates = []
        print(f"Loading candidates from {self.file_path}...")

        if self.file_path.suffix == ".gz":
            opener = gzip.open
        else:
            opener = open

        with opener(self.file_path, "rt", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    candidates.append(json.loads(line))

        print(f"Loaded {len(candidates)} candidates.")
        return candidates