from __future__ import annotations

from qdrant_client import models

from kb.card import Card
from kb.config import KbConfig
from kb.embed import Embedder
from kb.ids import point_id, retrieval_text
from kb.payload import build_payload
from kb.syncplan import SyncPlan

VECTOR_NAME = "dense"

SCHEMA_BY_INDEX = {
    "keyword": models.PayloadSchemaType.KEYWORD,
    "integer": models.PayloadSchemaType.INTEGER,
    "float": models.PayloadSchemaType.FLOAT,
    "bool": models.PayloadSchemaType.BOOL,
    "datetime": models.PayloadSchemaType.DATETIME,
}


def _field_schema(spec: dict):
    index = spec["index"]
    if index != "text":
        return SCHEMA_BY_INDEX[index]
    return models.TextIndexParams(
        type=models.TextIndexType.TEXT,
        tokenizer=models.TokenizerType(spec.get("tokenizer", "word")),
        lowercase=spec.get("lowercase", True),
        min_token_len=spec.get("min_token_len", 1),
        max_token_len=spec.get("max_token_len", 30),
    )


def ensure_collection(client, config: KbConfig, name: str) -> None:
    if not client.collection_exists(name):
        client.create_collection(
            collection_name=name,
            vectors_config={
                VECTOR_NAME: models.VectorParams(
                    size=config.embedding_dimensions, distance=models.Distance.COSINE
                )
            },
        )

    for field, spec in config.payload_indexes.items():
        client.create_payload_index(
            collection_name=name, field_name=field, field_schema=_field_schema(spec), wait=True
        )
    for facet, spec in config.facets.items():
        client.create_payload_index(
            collection_name=name,
            field_name=f"facets.{facet}",
            field_schema=SCHEMA_BY_INDEX[spec.index],
            wait=True,
        )


def apply_plan(
    client,
    config: KbConfig,
    name: str,
    plan: SyncPlan,
    cards: list[Card],
    embedder: Embedder,
) -> dict[str, int]:
    by_id = {card.id: card for card in cards}

    to_embed = [action for action in plan.actions if action.op == "upsert"]
    if to_embed:
        vectors = embedder.embed([retrieval_text(by_id[a.card_id]) for a in to_embed])
        points = [
            models.PointStruct(
                id=action.point_id,
                vector={VECTOR_NAME: vector},
                payload=build_payload(by_id[action.card_id]),
            )
            for action, vector in zip(to_embed, vectors, strict=True)
        ]
        client.upsert(collection_name=name, points=points, wait=True)

    for action in plan.actions:
        if action.op == "set_payload":
            client.set_payload(
                collection_name=name,
                payload=build_payload(by_id[action.card_id]),
                points=[action.point_id],
                wait=True,
            )

    doomed = [action.point_id for action in plan.actions if action.op == "delete"]
    if doomed:
        client.delete(
            collection_name=name,
            points_selector=models.PointIdsList(points=doomed),
            wait=True,
        )

    return plan.counts()


def rebuild(
    client, config: KbConfig, cards: list[Card], embedder: Embedder, stamp: str
) -> str:
    target = f"{config.collection}_{stamp}"
    if client.collection_exists(target):
        client.delete_collection(target)
    ensure_collection(client, config, target)

    vectors = embedder.embed([retrieval_text(card) for card in cards])
    if cards:
        client.upsert(
            collection_name=target,
            points=[
                models.PointStruct(
                    id=point_id(card.id),
                    vector={VECTOR_NAME: vector},
                    payload=build_payload(card),
                )
                for card, vector in zip(cards, vectors, strict=True)
            ],
            wait=True,
        )

    previous = {
        alias.collection_name
        for alias in client.get_aliases().aliases
        if alias.alias_name == config.collection
    }
    client.update_collection_aliases(
        change_aliases_operations=[
            models.CreateAliasOperation(
                create_alias=models.CreateAlias(
                    collection_name=target, alias_name=config.collection
                )
            )
        ]
    )
    for old in previous - {target}:
        client.delete_collection(old)
    return target
