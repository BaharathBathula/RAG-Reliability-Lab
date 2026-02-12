# RAG Reliability Lab

A production-focused Retrieval-Augmented Generation (RAG) project that emphasizes
reliability, latency, and retrieval quality rather than demo-only workflows.

## Why this project exists
Most GenAI examples stop at “it works.”
This project focuses on **what breaks in production**:
- Retrieval quality degradation
- Latency spikes
- Ungrounded answers
- Missing evaluation signals

## Core Capabilities
- Document ingestion and chunking
- Vector-based retrieval
- Citation-based answer generation
- Hooks for evaluation, latency, and SLA tracking

## Tech Stack
- Python
- LangChain
- OpenAI embeddings & chat models
- ChromaDB (local vector store)

## Project Status
🚧 Initial scaffold created.  
Evaluation framework and SLA reporting coming next.

## Author
Baharath Bathula  
Senior Data Engineer / GenAI Systems

## Attribution
This is an original implementation focused on reliability patterns in
production RAG systems.
