# RAG Reliability Lab — Architecture

This project implements a production-minded RAG pipeline with reliability hooks:
latency measurement, citation presence, retrieval quality proxies, and an eval runner.

```mermaid
flowchart TD
    A[User Question]
    B[Pipeline Ask]
    C[Vector Retrieval Top K]
    D[Context Chunks with Metadata]
    E[Answer Generation with Citations]
    F[Structured Response JSON]

    G[Evaluation Metrics]
    H[Evaluation Runner]
    I[Reports JSON HTML]
    J[SLA Pass Fail]

    A --> B --> C --> D --> E --> F
    F --> G --> H
    H --> I
    H --> J
