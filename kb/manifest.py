from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

import yaml

MANIFEST_RELATIVE = Path("sources") / "manifest.yaml"


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
    raw = yaml.safe_load(path.read_text()) or []
    return [SourceRow(**row) for row in raw]


def save_manifest(root: Path, rows: list[SourceRow]) -> None:
    path = Path(root) / MANIFEST_RELATIVE
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(row) for row in sorted(rows, key=lambda r: r.id)]
    path.write_text(yaml.safe_dump(payload, sort_keys=False, allow_unicode=True))


def source_refs(root: Path) -> set[str]:
    return {row.id for row in load_manifest(root)}
