from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

MANIFEST_RELATIVE = Path("sources") / "manifest.yaml"
ROW_KEYS = ("id", "title", "kind", "origin_uri", "sha256", "ingested_at")


class ManifestError(Exception):
    pass


@dataclass(frozen=True)
class SourceRow:
    id: str
    title: str
    kind: str
    origin_uri: str
    sha256: str
    ingested_at: str


def load_manifest(root: Path) -> list[SourceRow]:
    path = Path(root) / MANIFEST_RELATIVE
    if not path.is_file():
        return []
    try:
        raw = yaml.safe_load(path.read_text()) or []
    except yaml.YAMLError as exc:
        raise ManifestError(f"{MANIFEST_RELATIVE} is not valid YAML: {exc}") from exc
    if not isinstance(raw, list):
        raise ManifestError(f"{MANIFEST_RELATIVE} must be a list of rows")

    rows = []
    for position, row in enumerate(raw):
        if not isinstance(row, dict):
            raise ManifestError(f"{MANIFEST_RELATIVE} row {position} is not a mapping")
        missing = [key for key in ROW_KEYS if key not in row]
        extra = [key for key in row if key not in ROW_KEYS]
        if missing or extra:
            raise ManifestError(
                f"{MANIFEST_RELATIVE} row {position} "
                f"({row.get('id', 'no id')!r}) has the wrong keys; "
                f"missing {missing}, unexpected {extra}"
            )
        rows.append(SourceRow(**row))
    return rows


def save_manifest(root: Path, rows: list[SourceRow]) -> None:
    path = Path(root) / MANIFEST_RELATIVE
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(row) for row in sorted(rows, key=lambda r: r.id)]
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


def source_refs(root: Path) -> set[str]:
    return {row.id for row in load_manifest(root)}


def source_titles(root: Path) -> dict[str, str]:
    """Map each source id to its title, for the citation the retriever shows."""
    return {row.id: row.title for row in load_manifest(root)}
