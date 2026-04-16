import os
from langchain_community.document_loaders import PyMuPDFLoader
from app.config import PDF_DIR


def load_pdfs():
    docs = []

    if not os.path.exists(PDF_DIR):
        raise FileNotFoundError(f"PDF directory not found: {PDF_DIR}")

    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        raise FileNotFoundError(f"No PDF files found in: {PDF_DIR}")

    for file_name in pdf_files:
        file_path = os.path.join(PDF_DIR, file_name)
        loader = PyMuPDFLoader(file_path)
        file_docs = loader.load()

        for doc in file_docs:
            doc.metadata["source_file"] = file_name

        docs.extend(file_docs)

    return docs