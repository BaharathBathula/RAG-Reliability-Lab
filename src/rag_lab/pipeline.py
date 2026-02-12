"""
RAG Reliability Lab
Minimal retrieval + generation pipeline (browser-built).
"""

def ask(question: str) -> dict:
    return {
        "question": question,
        "answer": "Pipeline scaffold created. Retrieval and generation coming next.",
        "latency_ms": None,
        "sources": []
    }
