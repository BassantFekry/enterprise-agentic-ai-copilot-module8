"""Retrieve evidence only; LLM generation is a separate responsibility."""
from app.rag.embeddings import embed_texts
from app.rag.vector_store import get_collection


def retrieve(question: str, department: str, top_k: int = 3) -> list[dict]:
    if not 1 <= top_k <= 8:
        raise ValueError("top_k must be between 1 and 8")
    collection = get_collection(department)
    if collection.count() == 0:
        return []
    result = collection.query(
        query_embeddings=embed_texts([question]),
        n_results=min(top_k, collection.count()),
        include=["documents", "metadatas", "distances"],
    )
    evidence = []
    for text, meta, distance in zip(
        result["documents"][0], result["metadatas"][0], result["distances"][0]
    ):
        evidence.append({
            "text": text,
            "source": meta["source"],
            "page": meta["page"],
            "department": department,
            "distance": round(float(distance), 4),
        })
    return evidence
