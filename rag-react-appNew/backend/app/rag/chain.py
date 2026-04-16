from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
from app.rag.retriever import get_retriever
from app.config import OLLAMA_CHAT_MODEL, OLLAMA_BASE_URL

retriever = get_retriever()

llm = ChatOllama(
    model=OLLAMA_CHAT_MODEL,
    base_url=OLLAMA_BASE_URL,
    temperature=0,
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=False,
)


def get_answer(query: str) -> str:
    result = qa_chain.invoke({"query": query})
    return result["result"]