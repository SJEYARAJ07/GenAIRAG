# # # from langchain.chains import RetrievalQA
# # #
# # # from app.rag.llm import LlamaAPI
# # # from app.rag.retriever import get_retriever
# # #
# # #
# # # retriever = get_retriever()
# # #
# # # llm = LlamaAPI(
# # #     model="llama33-70b-instruct",
# # #     temperature=0.0,
# # # )
# # #
# # # qa_chain = RetrievalQA.from_chain_type(
# # #     llm=llm,
# # #     chain_type="stuff",
# # #     retriever=retriever,
# # #     return_source_documents=False,
# # # )
# # #
# # #
# # # def get_answer(query: str) -> str:
# # #     result = qa_chain.invoke({"query": query})
# # #     return result["result"]
# # #
# #
# # # from langchain_classic.chains import create_retrieval_chain
# # # from langchain_classic.chains.combine_documents import create_stuff_documents_chain
# # from langchain_core.prompts import ChatPromptTemplate
# #
# # from app.rag.llm import LlamaAPI
# # from app.rag.retriever import get_retriever
# #
# # from langchain_classic.chains.retrieval import create_retrieval_chain
# # from langchain_classic.chains.combine_documents import create_stuff_documents_chain
# #
# # retriever = get_retriever()
# #
# # llm = LlamaAPI(
# #     model="llama33-70b-instruct",
# #     temperature=0.0,
# # )
# #
# # prompt = ChatPromptTemplate.from_template(
# #     """
# # Answer the question based only on the context below.
# #
# # Context:
# # {context}
# #
# # Question:
# # {input}
# # """
# # )
# #
# # combine_docs_chain = create_stuff_documents_chain(llm, prompt)
# # qa_chain = create_retrieval_chain(retriever, combine_docs_chain)
# #
# #
# # def get_answer(query: str) -> str:
# #     result = qa_chain.invoke({"input": query})
# #     return result["answer"]
# #
#
# from langchain_core.prompts import PromptTemplate
# from langchain_core.runnables import RunnablePassthrough
#
# from app.rag.llm import LlamaAPI
# from app.rag.retriever import get_retriever
#
# #kkdkdkdkdkdkdk
#
# retriever = get_retriever()
#
# llm = LlamaAPI(
#     model="llama33-70b-instruct",
#     temperature=0.0,
# )
#
# prompt = PromptTemplate.from_template(
#     """
# Answer the question based only on the context below.
#
# Context:
# {context}
#
# Question:
# {question}
# """
# )
#
#
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)
#
#
# qa_chain = (
#     {
#         "context": retriever | format_docs,
#         "question": RunnablePassthrough(),
#     }
#     | prompt
#     | llm
# )
#
#
# def get_answer(query: str) -> str:
#     return qa_chain.invoke(query)
#
from typing import List

from langchain_core.prompts import PromptTemplate

from app.rag.llm import call_llm
from app.rag.retriever import get_retriever


PROMPT = PromptTemplate.from_template(
    """
You are a helpful assistant.
Answer the question using only the context below.
Write a short plain-English answer.
Do not return JSON.
Do not return citation markers like [1].

Context:
{context}

Question:
{question}
"""
)

retriever = get_retriever()


def _retrieve_docs(question: str):
    """
    Works with both older and newer LangChain retriever interfaces.
    """
    if hasattr(retriever, "invoke"):
        return retriever.invoke(question)

    if hasattr(retriever, "get_relevant_documents"):
        return retriever.get_relevant_documents(question)

    raise TypeError("Retriever does not support invoke() or get_relevant_documents().")


def _format_docs(docs) -> str:
    return "\n\n".join(doc.page_content for doc in docs)


def get_answer(question: str) -> str:
    docs = _retrieve_docs(question)
    context = _format_docs(docs)

    prompt = PROMPT.format(context=context, question=question)
    answer = call_llm(prompt)

    return answer.strip() if isinstance(answer, str) else str(answer).strip()