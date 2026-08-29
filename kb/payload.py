from __future__ import annotations

import datetime
import hashlib
import json

from kb.card import Card
from kb.ids import embed_hash, retrieval_text

STATE_FIELDS = ("embed_hash", "payload_hash")

EXCLUDED_FROM_HASH = frozenset({"card_id", "title", "question", "text", "body", *STATE_FIELDS})


def _json_native(value: object) -> object:
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: _json_native(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_native(item) for item in value]
    return value


def build_payload(card: Card) -> dict:
    payload = {
        "card_id": card.id,
        "title": card.title,
        "kind": card.kind,
        "question": card.question,
        "text": retrieval_text(card),
        "body": card.body,
        "path": card.path,
        "authority": card.authority,
        "facets": dict(card.facets),
        "see_also": list(card.see_also),
        "not_to_be_confused_with": list(card.not_to_be_confused_with),
        "source": {
            "ref": card.source_ref,
            "title": card.source_title or card.source_ref,
            "locator": card.source_locator,
            "extracted_at": card.source_extracted_at,
        },
    }
    return _json_native(payload)


def payload_hash(card: Card) -> str:
    payload = build_payload(card)
    material = {key: value for key, value in payload.items() if key not in EXCLUDED_FROM_HASH}
    canonical = json.dumps(material, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_point_payload(card: Card) -> dict:
    """The payload actually written to Qdrant: the card plus its two sync hashes."""
    payload = build_payload(card)
    payload["embed_hash"] = embed_hash(card)
    payload["payload_hash"] = payload_hash(card)
    return payload
