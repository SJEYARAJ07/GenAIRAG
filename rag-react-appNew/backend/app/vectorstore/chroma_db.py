import os
import shutil
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from app.config import CHROMA_DIR, OLLAMA_EMBED_MODEL, OLLAMA_BASE_URL


def get_embeddings():
    return OllamaEmbeddings(
        model=OLLAMA_EMBED_MODEL,
        base_url=OLLAMA_BASE_URL,
    )


def load_db():
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )


def create_db(chunks):
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    os.makedirs(CHROMA_DIR, exist_ok=True)

    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    return db