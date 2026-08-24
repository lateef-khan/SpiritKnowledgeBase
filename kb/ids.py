from __future__ import annotations

import hashlib
import uuid

from kb.card import Card

ID_PREFIX = "kb:"


def point_id(card_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, ID_PREFIX + card_id))


def retrieval_text(card: Card) -> str:
    head = [card.title, card.question, *card.asked_as]
    if card.keywords:
        head.append(", ".join(card.keywords))
    return "\n".join(head) + "\n\n" + card.body


def embed_hash(card: Card) -> str:
    return hashlib.sha256(retrieval_text(card).encode("utf-8")).hexdigest()
