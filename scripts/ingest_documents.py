"""Run: uv run --extra rag python scripts/ingest_documents.py"""
from pathlib import Path
from app.rag.indexing import index_department


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1] / "data" / "raw"
    for department in ("hr", "accounting", "legal"):
        print(index_department(root, department))
