"""
Ingest sample docs into the vector store for CI runs.
"""

import os

from src.rag_lab.ingest import ingest_folder


def main():
    folder = "data/sample_docs"
    os.makedirs(folder, exist_ok=True)

    # Ensure at least one doc exists so ingestion doesn't fail
    sample_path = os.path.join(folder, "intro.txt")
    if not os.path.exists(sample_path):
        with open(sample_path, "w", encoding="utf-8") as f:
            f.write("RAG is Retrieval-Augmented Generation: retrieval + generation using context.\n")
            f.write("This project focuses on reliability, latency, and retrieval quality.\n")

    result = ingest_folder(folder)
    print("✅ Ingestion complete:", result)


if __name__ == "__main__":
    main()
