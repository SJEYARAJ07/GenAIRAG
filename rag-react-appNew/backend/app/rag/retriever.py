from app.vectorstore.chroma_db import load_db


def get_retriever():
    db = load_db()
    return db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )