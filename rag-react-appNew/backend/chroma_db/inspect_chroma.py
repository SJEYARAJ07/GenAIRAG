import sys
from pathlib import Path

# Add backend root to import path
BACKEND_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(BACKEND_ROOT))

from langchain_chroma import Chroma
from app.config import CHROMA_DIR
from app.vectorstore.bge_embeddings import BGEEmbeddings


def main():
    print("CHROMA_DIR:", CHROMA_DIR)

    db = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=BGEEmbeddings(),
    )

    count = db._collection.count()
    print("Total documents:", count)

    if count == 0:
        print("No documents found in Chroma.")
        return

    print("\nSample stored chunks:\n")
    data = db._collection.get(limit=min(5, count))

    docs = data.get("documents", [])
    metas = data.get("metadatas", [])
    ids = data.get("ids", [])

    for i, doc in enumerate(docs):
        print(f"--- Chunk {i + 1} ---")
        print("ID:", ids[i] if i < len(ids) else "")
        print("Text:", doc[:500])
        print("Metadata:", metas[i] if i < len(metas) else {})
        print()

    print("Retrieval test:\n")
    results = db.similarity_search("test query", k=3)
    for i, r in enumerate(results, 1):
        print(f"Result {i}:")
        print(r.page_content[:400])
        print("Metadata:", r.metadata)
        print("-" * 40)


if __name__ == "__main__":
    main()