import json
import ssl
import urllib.request
from typing import Any, List, Optional

from langchain_core.language_models.llms import LLM
from pydantic import Field

from app.config import (
    LLM_MAX_TOKENS,
    LLM_MODEL,
    LLM_TOKEN,
    LLM_TOP_P,
    LLM_TEMPERATURE,
    LLM_URL,
    SSL_VERIFY,
)


def call_llm(prompt: str) -> str:
    ssl_context = None if SSL_VERIFY else ssl._create_unverified_context()

    payload = {
        "instances": [
            {
                "messages": [
                    {
                        "content": prompt,
                        "role": "system",
                    }
                ],
                "model": LLM_MODEL,
                "max_tokens": LLM_MAX_TOKENS,
                "temperature": LLM_TEMPERATURE,
                # "response_format": {
                #     "type": "json_object"
                # },
                "top_p": LLM_TOP_P
            }
        ]
    }

    body = json.dumps(payload).encode("utf-8")

    headers = {
        "Authorization": f"Bearer {LLM_TOKEN}",
        "Content-Type": "application/json",
    }

    request = urllib.request.Request(
        LLM_URL,
        data=body,
        headers=headers,
        method="POST",
    )

    with urllib.request.urlopen(request, context=ssl_context) as response:
        result = json.loads(response.read().decode("utf-8"))
        content = result["predictions"][0]["choices"][0]["message"]["content"]
        return content


class LlamaAPI(LLM):
    url: str = Field(default=LLM_URL)
    token: str = Field(default=LLM_TOKEN)
    ssl_verify: bool = Field(default=SSL_VERIFY)
    model: str = Field(default=LLM_MODEL)
    max_tokens: int = Field(default=LLM_MAX_TOKENS)
    temperature: float = Field(default=LLM_TEMPERATURE)
    top_p: float = Field(default=LLM_TOP_P)

    @property
    def _llm_type(self) -> str:
        return "llama_api"

    @property
    def _identifying_params(self) -> dict[str, Any]:
        return {"url": self.url, "model": self.model}

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager=None,
        **kwargs: Any,
    ) -> str:
        return call_llm(prompt)
