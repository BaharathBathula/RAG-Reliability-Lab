"""
Evaluation Datasets (Placeholder)

Small, human-readable eval set.
Later, we can add JSONL datasets, gold citations, and regression suites.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class EvalCase:
    query: str
    expected_keywords: List[str]


def default_eval_set() -> List[EvalCase]:
    """
    Starter evaluation set.
    Edit these to match your sample_docs content.
    """
    return [
        EvalCase(
            query="What is RAG?",
            expected_keywords=["retrieval", "generation", "context"]
        ),
        EvalCase(
            query="What does this project focus on?",
            expected_keywords=["reliability", "latency", "retrieval"]
        ),
    ]
