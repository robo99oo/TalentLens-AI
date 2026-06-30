```mermaid
flowchart TD
    A[Job Description DOCX] --> B[JD Parser]
    B --> C[JD Intelligence Engine]
    C --> D[Dynamic Weight Generator]

    E[100K Candidate Profiles JSONL] --> F[Candidate Loader]

    F --> G[Career Analyzer]
    F --> H[Behavior Analyzer]
    F --> I[Evidence Engine]
    F --> J[Recruiter Decision Engine]

    D --> K[Dynamic Scoring Engine]
    G --> K
    H --> K
    I --> K
    J --> K

    K --> L[Reasoning Engine]
    L --> M[Top 100 Ranked Candidates]
    M --> N[submission.csv]

    N --> O[Submission Validator]
```