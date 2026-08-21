from __future__ import annotations

import hashlib
import json
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


def payload_hash(card: Card) -> str:
    material = {
        "kind": card.kind,
        "facets": card.facets,
        "path": card.path,
        "authority": card.authority,
        "see_also": list(card.see_also),
        "not_to_be_confused_with": list(card.not_to_be_confused_with),
        "source": {
            "ref": card.source_ref,
            "locator": card.source_locator,
            "extracted_at": card.source_extracted_at,
        },
    }
    canonical = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()
