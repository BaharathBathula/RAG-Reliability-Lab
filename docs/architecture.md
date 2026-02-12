# RAG Reliability Lab — Architecture

This project implements a production-minded RAG pipeline with reliability hooks:
latency measurement, citation presence, retrieval quality proxies, and an eval runner.

## Diagram
See: **docs/architecture_diagram.md**

## Components
- **ingest.py**: Loads docs, chunks text, stores embeddings (vector store).
- **retrieve.py**: Retrieves Top-K relevant chunks for a query.
- **generate.py**: Generates a grounded answer with citations using retrieved context.
- **pipeline.py**: Orchestrates retrieval → generation and returns a structured response.
- **evals/**: Defines metrics + runner to score reliability and prepare SLA reporting.
- **reports/**: Stores evaluation outputs (next: JSON + HTML summary).

## Reliability signals (v1)
- **Latency SLA**: request latency within threshold
- **Citation presence**: answer includes citation markers like `[1]`
- **Keyword recall proxy**: expected keywords appear in answer
- **Has sources**: at least one retrieved chunk/source used

## Next planned upgrades
- HTML report generation
- Regression testing (compare metrics vs baseline)
- SLA gate for PR checks
- Expand dataset and add groundedness checks
