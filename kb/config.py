from __future__ import annotations

from dataclasses import dataclass
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


def load_config(root: Path) -> KbConfig:
    path = Path(root) / "kb.yaml"
    if not path.is_file():
        raise ConfigError(f"kb.yaml not found at {path}")

    try:
        raw = yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        raise ConfigError(f"kb.yaml is not valid YAML: {exc}") from exc

    collection = raw.get("collection")
    if not isinstance(collection, str) or not collection:
        raise ConfigError("kb.yaml is missing a non-empty 'collection'")

    embedding = raw.get("embedding") or {}
    model = embedding.get("model")
    dimensions = embedding.get("dimensions")
    if model != REQUIRED_MODEL:
        raise ConfigError(f"embedding.model must be {REQUIRED_MODEL}, got {model!r}")
    if dimensions != REQUIRED_DIMENSIONS:
        raise ConfigError(
            f"embedding.dimensions must be {REQUIRED_DIMENSIONS} to match AgentCore, got {dimensions!r}"
        )

    kinds = raw.get("kinds") or []
    if not kinds or not all(isinstance(k, str) for k in kinds):
        raise ConfigError("kb.yaml needs a non-empty list of string 'kinds'")

    facets: dict[str, FacetSpec] = {}
    for name, spec in (raw.get("facets") or {}).items():
        spec = spec or {}
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
    for name, spec in payload_indexes.items():
        if (spec or {}).get("index") not in VALID_INDEX_TYPES:
            raise ConfigError(f"payload index {name!r} has unknown index type")

    return KbConfig(
        root=Path(root),
        collection=collection,
        embedding_model=model,
        embedding_dimensions=dimensions,
        kinds=tuple(kinds),
        facets=facets,
        payload_indexes=payload_indexes,
        pdf_command=(raw.get("ingest") or {}).get("pdf_command"),
    )
