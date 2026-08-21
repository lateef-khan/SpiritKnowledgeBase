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


class AliasConflictError(Exception):
    pass


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


def _alias_names(client) -> set[str]:
    return {alias.alias_name for alias in client.get_aliases().aliases}


def _point_alias(client, alias_name: str, collection_name: str) -> None:
    client.update_collection_aliases(
        change_aliases_operations=[
            models.CreateAliasOperation(
                create_alias=models.CreateAlias(
                    collection_name=collection_name, alias_name=alias_name
                )
            )
        ]
    )


def _refuse_concrete_collection(client, name: str) -> None:
    # collection_exists answers true for an alias, so the alias list is the discriminator.
    if client.collection_exists(name) and name not in _alias_names(client):
        raise AliasConflictError(
            f"{name!r} is a concrete collection, not an alias. Qdrant refuses an alias "
            f"whose name a collection already holds, so --rebuild could never swap it. "
            f"Delete the collection {name!r} in Qdrant, then run 'kb sync --rebuild' to "
            f"build a stamped collection behind the alias."
        )


def ensure_alias(client, config: KbConfig, stamp: str) -> str:
    """Guarantee `config.collection` resolves as an alias and return that name.

    Spec 6.3 swaps the alias on every rebuild, so the ordinary sync path must
    address the alias too or the first rebuild collides with a same-named
    collection after paying the whole embedding bill.
    """
    if config.collection in _alias_names(client):
        ensure_collection(client, config, config.collection)
        return config.collection

    _refuse_concrete_collection(client, config.collection)
    target = f"{config.collection}_{stamp}"
    ensure_collection(client, config, target)
    _point_alias(client, config.collection, target)
    return config.collection


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
    _refuse_concrete_collection(client, config.collection)

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
    _point_alias(client, config.collection, target)
    for old in previous - {target}:
        client.delete_collection(old)
    return target
