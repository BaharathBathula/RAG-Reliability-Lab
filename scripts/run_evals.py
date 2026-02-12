"""
Run evaluation suite and write report artifacts.

Outputs:
- reports/latest.json  (machine-readable)
- reports/latest.md    (human-readable summary)
"""

import json
import os
from datetime import datetime, timezone

from src.rag_lab.evals.runner import run_eval


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_json(path: str, payload: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def write_md(path: str, payload: dict) -> None:
    avg = payload.get("avg_scores", {})
    num_cases = payload.get("num_cases", 0)

    lines = []
    lines.append("# RAG Reliability Lab — Latest Evaluation Report")
    lines.append("")
    lines.append(f"- Generated at: **{payload.get('generated_at_utc', '')}**")
    lines.append(f"- Cases run: **{num_cases}**")
    lines.append("")
    lines.append("## Average scores")
    for k, v in sorted(avg.items()):
        try:
            lines.append(f"- **{k}**: `{float(v):.3f}`")
        except Exception:
            lines.append(f"- **{k}**: `{v}`")
    lines.append("")
    lines.append("## Per-case results")
    for r in payload.get("results", []):
        lines.append(f"### {r.get('query', '')}")
        lines.append(f"- latency_ms: `{r.get('latency_ms')}`")
        lines.append(f"- sources_count: `{r.get('sources_count')}`")
        lines.append(f"- scores: `{r.get('scores')}`")
        lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    # Run evals
    summary = run_eval(latency_sla_ms=2500)

    # Attach metadata
    summary["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    summary["project"] = "rag-reliability-lab"
    summary["report_version"] = "v1"

    # Write artifacts
    ensure_dir("reports")
    write_json("reports/latest.json", summary)
    write_md("reports/latest.md", summary)

    print("✅ Wrote reports/latest.json and reports/latest.md")


if __name__ == "__main__":
    main()
