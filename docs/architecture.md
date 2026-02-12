# RAG Reliability Lab — Architecture

This project implements a production-minded RAG pipeline with reliability hooks:
latency measurement, citation presence, retrieval quality proxies, and an eval runner.

## High-level flow

```mermaid

flowchart TD
    A[User Question] --> B[pipeline.ask()]
    B --> C[retrieve.py<br/>Vector Search (Top-K)]
    C --> D[Context Chunks<br/>+ source metadata]
    D --> E[generate.py<br/>LLM Answer + Citations]
    E --> F[Answer JSON<br/>answer, sources, latency_ms]

    %% Evaluation path
    F --> G[evals/metrics.py<br/>Scoring Functions]
    G --> H[evals/runner.py<br/>Batch Eval Runner]
    H --> I[reports/<br/>JSON/HTML (next)]
    H --> J[SLA Gate<br/>pass/fail (next)]
