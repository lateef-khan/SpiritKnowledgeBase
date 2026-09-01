"""A keyword filter over an array facet is the mechanism company-wide cards use.

A card listing both brands must survive either brand's filter, and a card listing
one brand must be excluded by the other's. AgentCore asserts the excluding
direction only on a scalar facet, so this locks it in on an array.
"""

import pytest
from qdrant_client import QdrantClient, models

from kb.qdrant import VECTOR_NAME

pytestmark = pytest.mark.integration

COLLECTION = "kb_array_filter_it"
URL = "http://localhost:6333"
VECTOR = [1.0, 0.0, 0.0, 0.0]

POINTS = [
    (1, "spirit-only", ["spirit"], ["ct900"]),
    (2, "sole-only", ["sole"], ["f63"]),
    (3, "company-wide", ["sole", "spirit"], ["ct900", "f63"]),
]


@pytest.fixture
def corpus():
    client = QdrantClient(url=URL, timeout=180)
    if client.collection_exists(COLLECTION):
        client.delete_collection(COLLECTION)
    client.create_collection(
        COLLECTION,
        vectors_config={
            VECTOR_NAME: models.VectorParams(size=4, distance=models.Distance.COSINE)
        },
    )
    for field in ("facets.brand", "facets.applies_to"):
        client.create_payload_index(COLLECTION, field, models.PayloadSchemaType.KEYWORD, wait=True)
    client.upsert(
        COLLECTION,
        points=[
            models.PointStruct(
                id=number,
                vector={VECTOR_NAME: VECTOR},
                payload={"card_id": card_id, "facets": {"brand": brand, "applies_to": applies}},
            )
            for number, card_id, brand, applies in POINTS
        ],
        wait=True,
    )
    yield client
    client.delete_collection(COLLECTION)


def matching(client, key, value):
    condition = models.FieldCondition(key=key, match=models.MatchValue(value=value))
    found = client.query_points(
        COLLECTION,
        query=VECTOR,
        using=VECTOR_NAME,
        limit=10,
        query_filter=models.Filter(must=[condition]),
        with_payload=True,
    ).points
    return sorted(point.payload["card_id"] for point in found)


@pytest.mark.parametrize(
    ("key", "value", "expected"),
    [
        ("facets.brand", "spirit", ["company-wide", "spirit-only"]),
        ("facets.brand", "sole", ["company-wide", "sole-only"]),
        ("facets.applies_to", "ct900", ["company-wide", "spirit-only"]),
        ("facets.applies_to", "f63", ["company-wide", "sole-only"]),
    ],
)
def test_array_facet_filter_includes_listed_and_excludes_unlisted(corpus, key, value, expected):
    assert matching(corpus, key, value) == expected
