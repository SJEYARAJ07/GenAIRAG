import os
import shutil

from langchain_chroma import Chroma

from app.config import CHROMA_DIR
from app.vectorstore.bge_embeddings import BGEEmbeddings


def get_embeddings():
    return BGEEmbeddings()


def load_db():
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )


# def create_db(chunks):
#     if os.path.exists(CHROMA_DIR):
#         shutil.rmtree(CHROMA_DIR)
#
#     os.makedirs(CHROMA_DIR, exist_ok=True)
#
#     embeddings = get_embeddings()
#
#     db = Chroma.from_documents(
#         documents=chunks,
#         embedding=embeddings,
#         persist_directory=CHROMA_DIR,
#     )
#
#     return db

def create_db(chunks):
    print("CHROMA_DIR:", CHROMA_DIR)
    print("Chunks received:", len(chunks))

    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    os.makedirs(CHROMA_DIR, exist_ok=True)

    embeddings = get_embeddings()

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DIR,
    )

    print("DB count after creation:", db._collection.count())
    return db

