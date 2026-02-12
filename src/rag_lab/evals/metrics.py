"""
Evaluation Metrics (Placeholder)

This module defines what "reliability" means for the RAG pipeline.
We start with simple, explainable signals and later expand to richer evals.
"""

from dataclasses import dataclass
from typing import List, Dict, Any
import time


@dataclass
class EvalResult:
    query: str
    expected_keywords: List[str]
    answer: str
    sources: List[str]
    latency_ms: int
    scores: Dict[str, float]
    meta: Dict[str, Any]


def keyword_recall(answer: str, expected_keywords: List[str]) -> float:
    """
    Simple proxy for 'answer relevance' until we add stronger methods.
    Score = fraction of expected keywords found in the answer.
    """
    if not expected_keywords:
        return 0.0
    a = (answer or "").lower()
    hits = sum(1 for k in expected_keywords if k.lower() in a)
    return hits / max(len(expected_keywords), 1)


def has_citations(answer: str) -> float:
    """
    Checks whether the answer includes citation markers like [1], [2].
    """
    a = answer or ""
    return 1.0 if ("[" in a and "]" in a) else 0.0


def sla_latency_ok(latency_ms: int, threshold_ms: int = 2500) -> float:
    """
    SLA proxy: 1.0 if latency within threshold else 0.0
    """
    return 1.0 if latency_ms is not None and latency_ms <= threshold_ms else 0.0


def score_single(
    query: str,
    expected_keywords: List[str],
    pipeline_output: Dict[str, Any],
    latency_sla_ms: int = 2500
) -> EvalResult:
    """
    Compute placeholder reliability metrics for one pipeline run.
    pipeline_output must contain: answer, sources, latency_ms
    """
    answer = pipeline_output.get("answer", "")
    sources = pipeline_output.get("sources", []) or []
    latency_ms = pipeline_output.get("latency_ms", None)

    scores = {
        "keyword_recall": keyword_recall(answer, expected_keywords),
        "has_citations": has_citations(answer),
        "latency_sla_ok": sla_latency_ok(latency_ms, latency_sla_ms),
        "has_sources": 1.0 if len(sources) > 0 else 0.0,
    }

    meta = {
        "scored_at_epoch": int(time.time()),
        "latency_sla_ms": latency_sla_ms,
    }

    return EvalResult(
        query=query,
        expected_keywords=expected_keywords,
        answer=answer,
        sources=sources,
        latency_ms=latency_ms if latency_ms is not None else -1,
        scores=scores,
        meta=meta,
    )
