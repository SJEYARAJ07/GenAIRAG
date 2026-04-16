from app.ingestion.loader import load_pdfs
from app.ingestion.splitter import split_docs
from app.vectorstore.chroma_db import create_db


def run():
    print("Loading PDFs...")
    docs = load_pdfs()
    print(f"Loaded {len(docs)} document pages.")

    print("Splitting documents into chunks...")
    chunks = split_docs(docs)
    print(f"Created {len(chunks)} chunks.")

    print("Creating vector database...")
    create_db(chunks)
    print("Ingestion complete.")


if __name__ == "__main__":
    run()