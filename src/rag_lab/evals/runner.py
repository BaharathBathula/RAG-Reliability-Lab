"""
Evaluation Runner (Placeholder)

Runs a small eval set against the RAG pipeline and returns a summary.
Later: write results to JSON/HTML reports + regression alerts (SLA).
"""

from typing import Dict, Any, List
from .datasets import default_eval_set
from .metrics import score_single
from ..pipeline import ask


def run_eval(latency_sla_ms: int = 2500) -> Dict[str, Any]:
    cases = default_eval_set()
    results = []
    score_sums = {}

    for c in cases:
        out = ask(c.query)  # pipeline output dict
        r = score_single(
            query=c.query,
            expected_keywords=c.expected_keywords,
            pipeline_output=out,
            latency_sla_ms=latency_sla_ms
        )
        results.append(r)

        # accumulate scores
        for k, v in r.scores.items():
            score_sums[k] = score_sums.get(k, 0.0) + float(v)

    n = max(len(results), 1)
    avg_scores = {k: v / n for k, v in score_sums.items()}

    return {
        "num_cases": len(results),
        "avg_scores": avg_scores,
        "results": [
            {
                "query": r.query,
                "scores": r.scores,
                "latency_ms": r.latency_ms,
                "sources_count": len(r.sources),
            }
            for r in results
        ],
    }
