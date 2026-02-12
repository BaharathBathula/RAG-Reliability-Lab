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

Components

ingest.py: Loads docs, chunks text, stores embeddings (vector store).

retrieve.py: Retrieves Top-K relevant chunks for a query.

generate.py: Generates a grounded answer with citations (e.g., [1], [2]) using retrieved context.

pipeline.py: Orchestrates retrieval → generation and returns a structured response.

evals/: Defines metrics + runner to score reliability and prepare SLA reporting.

reports/: Stores evaluation outputs (next: JSON + HTML summary).

Reliability signals (v1 placeholders)

Latency SLA: request latency within threshold

Citation presence: answer includes citation markers

Keyword recall proxy: expected keywords appear in answer

Has sources: at least one retrieved chunk/source used

Next planned upgrades

HTML report generation

Regression testing (compare metrics vs baseline)

SLA gate for PR checks

Expand dataset and add groundedness checks
