from pathlib import Path

import pytest

from kb.config import FacetSpec, KbConfig
from kb.embed import BATCH_SIZE, EmbedError, OpenAIEmbedder, build_embedder

CONFIG = KbConfig(
    root=Path("."),
    collection="kb",
    embedding_model="text-embedding-3-small",
    embedding_dimensions=1024,
    kinds=("fact",),
    facets={"model": FacetSpec(index="keyword", array=False, values=())},
    payload_indexes={},
    pdf_command=None,
)


def item(position: int, embedding: list[float]):
    return type("Item", (), {"index": position, "embedding": embedding})()


def response(items: list):
    return type("Response", (), {"data": list(items)})()


class FakeEmbeddings:
    def __init__(self):
        self.calls = []

    def create(self, *, model, input, dimensions):
        self.calls.append({"model": model, "input": list(input), "dimensions": dimensions})
        return response(
            [item(i, [float(len(t))] * dimensions) for i, t in enumerate(input)]
        )


class FakeClient:
    def __init__(self):
        self.embeddings = FakeEmbeddings()


def test_sends_model_and_dimensions_from_config():
    client = FakeClient()
    OpenAIEmbedder(CONFIG, client).embed(["abc"])
    assert client.embeddings.calls[0]["model"] == "text-embedding-3-small"
    assert client.embeddings.calls[0]["dimensions"] == 1024


def test_returns_one_vector_per_input_in_order():
    client = FakeClient()
    vectors = OpenAIEmbedder(CONFIG, client).embed(["a", "bb", "ccc"])
    assert [v[0] for v in vectors] == [1.0, 2.0, 3.0]
    assert all(len(v) == 1024 for v in vectors)


def test_batches_at_the_batch_size():
    client = FakeClient()
    texts = [f"text-{i}" for i in range(BATCH_SIZE + 5)]
    vectors = OpenAIEmbedder(CONFIG, client).embed(texts)
    assert len(client.embeddings.calls) == 2
    assert len(client.embeddings.calls[0]["input"]) == BATCH_SIZE
    assert len(client.embeddings.calls[1]["input"]) == 5
    assert len(vectors) == len(texts)


def test_empty_input_makes_no_call():
    client = FakeClient()
    assert OpenAIEmbedder(CONFIG, client).embed([]) == []
    assert client.embeddings.calls == []


def test_wrong_width_from_the_api_raises():
    class BadEmbeddings(FakeEmbeddings):
        def create(self, *, model, input, dimensions):
            super().create(model=model, input=input, dimensions=dimensions)
            return response([item(0, [0.0] * 512)])

    client = FakeClient()
    client.embeddings = BadEmbeddings()
    with pytest.raises(EmbedError, match="1024"):
        OpenAIEmbedder(CONFIG, client).embed(["abc"])


def test_a_shuffled_response_still_pairs_each_input_with_its_own_vector():
    class ShuffledEmbeddings(FakeEmbeddings):
        def create(self, *, model, input, dimensions):
            self.calls.append({"model": model, "input": list(input), "dimensions": dimensions})
            items = [item(i, [float(len(t))] * dimensions) for i, t in enumerate(input)]
            return response([items[2], items[0], items[1]])

    client = FakeClient()
    client.embeddings = ShuffledEmbeddings()
    vectors = OpenAIEmbedder(CONFIG, client).embed(["a", "bb", "ccc"])
    assert [v[0] for v in vectors] == [1.0, 2.0, 3.0]


def test_a_short_response_raises_rather_than_misaligning():
    class ShortEmbeddings(FakeEmbeddings):
        def create(self, *, model, input, dimensions):
            self.calls.append({"model": model, "input": list(input), "dimensions": dimensions})
            return response([item(0, [1.0] * dimensions)])

    client = FakeClient()
    client.embeddings = ShortEmbeddings()
    with pytest.raises(EmbedError, match="1 embeddings for 3 inputs"):
        OpenAIEmbedder(CONFIG, client).embed(["a", "bb", "ccc"])


def test_a_response_index_outside_the_batch_raises():
    class WildIndexEmbeddings(FakeEmbeddings):
        def create(self, *, model, input, dimensions):
            self.calls.append({"model": model, "input": list(input), "dimensions": dimensions})
            return response([item(9, [1.0] * dimensions), item(0, [2.0] * dimensions)])

    client = FakeClient()
    client.embeddings = WildIndexEmbeddings()
    with pytest.raises(EmbedError, match="index"):
        OpenAIEmbedder(CONFIG, client).embed(["a", "bb"])


def test_a_duplicated_response_index_raises():
    class DuplicateIndexEmbeddings(FakeEmbeddings):
        def create(self, *, model, input, dimensions):
            self.calls.append({"model": model, "input": list(input), "dimensions": dimensions})
            return response([item(0, [1.0] * dimensions), item(0, [2.0] * dimensions)])

    client = FakeClient()
    client.embeddings = DuplicateIndexEmbeddings()
    with pytest.raises(EmbedError, match="index"):
        OpenAIEmbedder(CONFIG, client).embed(["a", "bb"])


def test_build_embedder_without_a_key_raises(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(EmbedError, match="OPENAI_API_KEY"):
        build_embedder(CONFIG)
