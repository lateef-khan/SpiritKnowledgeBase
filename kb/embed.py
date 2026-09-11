from __future__ import annotations

import os
from typing import Protocol

from kb.config import KbConfig

BATCH_SIZE = 100
API_KEY_VARIABLE = "OPENAI_API_KEY"
# text-embedding-3-small refuses a single input over this many tokens.
MAX_INPUT_TOKENS = 8192


class EmbedError(Exception):
    pass


class Embedder(Protocol):
    def embed(self, texts: list[str]) -> list[list[float]]: ...


class OpenAIEmbedder:
    def __init__(self, config: KbConfig, client) -> None:
        self._model = config.embedding_model
        self._dimensions = config.embedding_dimensions
        self._client = client

    def embed(self, texts: list[str]) -> list[list[float]]:
        vectors: list[list[float]] = []
        for start in range(0, len(texts), BATCH_SIZE):
            batch = texts[start : start + BATCH_SIZE]
            response = self._client.embeddings.create(
                model=self._model, input=batch, dimensions=self._dimensions
            )
            data = list(response.data)
            if len(data) != len(batch):
                raise EmbedError(
                    f"the API returned {len(data)} embeddings for {len(batch)} inputs"
                )
            # Response order is not contractual; each item carries its input's index.
            data.sort(key=lambda entry: entry.index)
            if [entry.index for entry in data] != list(range(len(batch))):
                raise EmbedError(
                    f"the API returned the index set {[entry.index for entry in data]} "
                    f"for a batch of {len(batch)} inputs"
                )
            for item in data:
                vector = list(item.embedding)
                if len(vector) != self._dimensions:
                    raise EmbedError(
                        f"expected {self._dimensions} dimensions, got {len(vector)}"
                    )
                vectors.append(vector)
        return vectors


def count_tokens(text: str, model: str) -> int:
    """Count tokens the way the embedding model will.

    tiktoken fetches the model's token table on first use and caches it, so a
    fresh machine needs the network once.
    """
    import tiktoken

    return len(tiktoken.encoding_for_model(model).encode(text))


def build_embedder(config: KbConfig) -> OpenAIEmbedder:
    key = os.environ.get(API_KEY_VARIABLE)
    if not key:
        raise EmbedError(f"{API_KEY_VARIABLE} is not set")
    from openai import OpenAI

    return OpenAIEmbedder(config, OpenAI(api_key=key))
