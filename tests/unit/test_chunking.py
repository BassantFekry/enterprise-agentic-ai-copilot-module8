import pytest
from app.rag.chunking import chunk_text


def test_chunking_preserves_overlap():
    chunks = chunk_text("abcdefghijklmnopqrstuvwxyz", chunk_size=10, overlap=3)
    assert chunks[0][-3:] == chunks[1][:3]
    assert len(chunks) >= 3


def test_invalid_overlap_raises():
    with pytest.raises(ValueError):
        chunk_text("hi", chunk_size=5, overlap=5)



def test_chunking_with_assignment_values():
    text = (
        "Employees should use strong passwords to protect company accounts. "
        "Passwords must contain letters, numbers, and special characters. "
        "Employees should never share their passwords with other people."
    )

    chunks = chunk_text(text, chunk_size=50, overlap=15)

    assert len(chunks) > 1
    assert chunks[0][-15:] == chunks[1][:15]
    assert all(len(chunk) <= 50 for chunk in chunks)