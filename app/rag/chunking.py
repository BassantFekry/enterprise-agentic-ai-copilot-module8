"""Simple overlapping character chunker. Improved semantic chunking comes later."""


def chunk_text(text: str, chunk_size: int = 450, overlap: int = 90) -> list[str]:
    if not 0 <= overlap < chunk_size:
        raise ValueError("overlap must be >= 0 and smaller than chunk_size")
    text = " ".join(text.split())
    chunks = []
    for start in range(0, len(text), chunk_size - overlap):
        piece = text[start : start + chunk_size]
        if piece:
            chunks.append(piece)
        if start + chunk_size >= len(text):
            break
    return chunks
