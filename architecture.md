---
title: TalentLens AI - Intelligent Candidate Discovery & Ranking System
---

```mermaid
flowchart TB

subgraph INPUT["Input Layer"]
A[📄 Job Description DOCX]
B[👥 Candidate Knowledge Base<br/>100K Candidate Profiles]
end

subgraph JD["JD Intelligence Layer"]
C[JD Parser]
D[JD Intelligence Engine]
E[Dynamic Weight Generator]
end

subgraph DATA["Candidate Processing Layer"]
F[Candidate Loader]
end

subgraph AI["AI Intelligence Layer"]
G[Career Analyzer]
H[Behavior Analyzer]
I[Evidence Engine]
J[Recruiter Decision Engine]
end

subgraph SCORE["Decision Layer"]
K[Dynamic Scoring Engine]
L[Explainable Reasoning Engine]
end

subgraph OUTPUT["Output Layer"]
M[Top 100 Ranked Candidates]
N[submission.csv]
O[Challenge Submission Validator]
end

A --> C
C --> D
D --> E

B --> F

F --> G
F --> H
F --> I
F --> J

E --> K
G --> K
H --> K
I --> K
J --> K

K --> L
L --> M
M --> N
N --> O

classDef input fill:#4F81BD,color:#fff,stroke:#2F5597;
classDef jd fill:#5B9BD5,color:#fff,stroke:#2F5597;
classDef process fill:#A5A5A5,color:#fff,stroke:#666666;
classDef ai fill:#70AD47,color:#fff,stroke:#548235;
classDef score fill:#ED7D31,color:#fff,stroke:#C55A11;
classDef output fill:#C00000,color:#fff,stroke:#7F0000;

class A,B input;
class C,D,E jd;
class F process;
class G,H,I,J ai;
class K,L score;
class M,N,O output;
```