import json
import ssl
import urllib.request
from typing import List
from urllib.error import HTTPError, URLError

from langchain_core.embeddings import Embeddings

from app.config import BGE_TOKEN, BGE_URL, SSL_VERIFY
print("BGE_URL:", BGE_URL)
print("BGE_TOKEN set:", bool(BGE_TOKEN))

def call_embeddings_api(texts: List[str]) -> List[List[float]]:
    if not isinstance(texts, list):
        raise TypeError("texts must be a list of strings")

    embeddings: List[List[float]] = []
    ssl_context = None if SSL_VERIFY else ssl._create_unverified_context()

    for text in texts:
        payload = {"instances": [{"input": text}]}
        body = json.dumps(payload).encode("utf-8")

        headers = {
            "Authorization": f"Bearer {BGE_TOKEN}",
            "Content-Type": "application/json",
        }

        req = urllib.request.Request(BGE_URL, data=body, headers=headers, method="POST")
        # with urllib.request.urlopen(req, context=ssl_context) as resp:
        #     resp_text = resp.read().decode("utf-8")
        #     result = json.loads(resp_text)
        #     emb = result["predictions"][0][0]["embedding"]
        #     embeddings.append(emb)
        try:
            with urllib.request.urlopen(req, context=ssl_context) as resp:
                resp_text = resp.read().decode("utf-8")
        except HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(
                f"Embedding request failed with HTTP {e.code}: {e.reason}\n{error_body}"
            ) from e
        except URLError as e:
            raise RuntimeError(f"Embedding request failed: {e}") from e

        try:
            result = json.loads(resp_text)
            emb = result["predictions"][0][0]["embedding"]
            embeddings.append(emb)
        except Exception as e:
            raise RuntimeError(f"Unexpected embedding response format: {resp_text}") from e

    return embeddings


class BGEEmbeddings(Embeddings):
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return call_embeddings_api(texts)

    def embed_query(self, text: str) -> List[float]:
        return call_embeddings_api([text])[0]
