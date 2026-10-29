import sys
from pathlib import Path

root_dir= Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from app.rag.ingestion import load_document, iter_department_files

def main():
    data_dir = root_dir / "data" / "raw"
    it_dir = data_dir / "it"

    print("Data directory:", data_dir)
    print("IT folder exists:", it_dir.is_dir())

    if not it_dir.is_dir():
        print("IT folder is missing.")
        return

    print("IT folder contents:", list(it_dir.iterdir()))
    print("--- Testing Iter Department Files For IT ---")

    it_files = list(iter_department_files(data_dir, "it"))

    for f in it_files:
        print(f"Found: {f.name}")

    if not it_files:
        print("No supported files found in IT.")
        return

    print("\n--- Testing Load Document ---")
    docs = load_document(it_files[0])

    if docs:
        print("Page Number:", docs[0]["page"])
        print("Text Preview:", docs[0]["text"][:150])
        print("Ingestion test passed.")
    else:
        print("The file was empty or contained no readable text.")
if __name__ == "__main__":
    main()