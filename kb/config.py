from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml

REQUIRED_MODEL = "text-embedding-3-small"
REQUIRED_DIMENSIONS = 1024
VALID_INDEX_TYPES = frozenset({"keyword", "integer", "float", "bool", "text", "datetime"})


class ConfigError(Exception):
    pass


@dataclass(frozen=True)
class FacetSpec:
    index: str
    array: bool
    values: tuple[str, ...]


@dataclass(frozen=True)
class KbConfig:
    root: Path
    collection: str
    embedding_model: str
    embedding_dimensions: int
    kinds: tuple[str, ...]
    facets: dict[str, FacetSpec]
    payload_indexes: dict[str, dict]
    pdf_command: str | None
    models: dict[str, tuple[str, ...]] = field(default_factory=dict)


def load_config(root: Path) -> KbConfig:
    path = Path(root) / "kb.yaml"
    if not path.is_file():
        raise ConfigError(f"kb.yaml not found at {path}")

    try:
        raw = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        raise ConfigError(f"kb.yaml is not valid YAML: {exc}") from exc

    if not isinstance(raw, dict):
        raise ConfigError("kb.yaml must be a mapping at the top level")

    collection = raw.get("collection")
    if not isinstance(collection, str) or not collection:
        raise ConfigError("kb.yaml is missing a non-empty 'collection'")

    embedding = raw.get("embedding") or {}
    if not isinstance(embedding, dict):
        raise ConfigError("kb.yaml 'embedding' must be a mapping")
    model = embedding.get("model")
    dimensions = embedding.get("dimensions")
    if model != REQUIRED_MODEL:
        raise ConfigError(f"embedding.model must be {REQUIRED_MODEL}, got {model!r}")
    if dimensions != REQUIRED_DIMENSIONS:
        raise ConfigError(
            f"embedding.dimensions must be {REQUIRED_DIMENSIONS} to match AgentCore, got {dimensions!r}"
        )

    kinds = raw.get("kinds") or []
    if not isinstance(kinds, list) or not kinds or not all(isinstance(k, str) for k in kinds):
        raise ConfigError("kb.yaml needs a non-empty list of string 'kinds'")

    raw_facets = raw.get("facets") or {}
    if not isinstance(raw_facets, dict):
        raise ConfigError("kb.yaml 'facets' must be a mapping")

    facets: dict[str, FacetSpec] = {}
    for name, spec in raw_facets.items():
        spec = spec or {}
        if not isinstance(spec, dict):
            raise ConfigError(f"facet {name!r} must be a mapping")
        index = spec.get("index")
        if index not in VALID_INDEX_TYPES:
            raise ConfigError(f"facet {name!r} has unknown index type {index!r}")
        facets[name] = FacetSpec(
            index=index,
            array=bool(spec.get("array", False)),
            values=tuple(spec.get("values") or ()),
        )
    if not facets:
        raise ConfigError("kb.yaml declares no facets")

    payload_indexes = raw.get("payload_indexes") or {}
    if not isinstance(payload_indexes, dict):
        raise ConfigError("kb.yaml 'payload_indexes' must be a mapping")
    for name, spec in payload_indexes.items():
        if not isinstance(spec or {}, dict):
            raise ConfigError(f"payload index {name!r} must be a mapping")
        if (spec or {}).get("index") not in VALID_INDEX_TYPES:
            raise ConfigError(f"payload index {name!r} has unknown index type")

    ingest = raw.get("ingest") or {}
    if not isinstance(ingest, dict):
        raise ConfigError("kb.yaml 'ingest' must be a mapping")

    raw_models = raw.get("models") or {}
    if not isinstance(raw_models, dict):
        raise ConfigError("kb.yaml 'models' must be a mapping of brand to a list of model ids")

    models: dict[str, tuple[str, ...]] = {}
    owner: dict[str, str] = {}
    for brand, ids in raw_models.items():
        if not isinstance(ids, list) or not ids or not all(isinstance(i, str) and i.strip() for i in ids):
            raise ConfigError(f"brand {brand!r} in 'models' needs a non-empty list of model ids")
        for model_id in ids:
            if model_id in owner:
                raise ConfigError(
                    f"model {model_id!r} is listed under both {owner[model_id]!r} and {brand!r}. "
                    f"applies_to is one flat namespace, so a model id names exactly one machine."
                )
            owner[model_id] = brand
        models[brand] = tuple(ids)

    return KbConfig(
        root=Path(root),
        collection=collection,
        embedding_model=model,
        embedding_dimensions=dimensions,
        kinds=tuple(kinds),
        facets=facets,
        payload_indexes=payload_indexes,
        pdf_command=ingest.get("pdf_command"),
        models=models,
    )
