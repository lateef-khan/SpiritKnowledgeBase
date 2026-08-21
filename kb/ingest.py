from __future__ import annotations

import email
import email.policy
import hashlib
import shlex
import subprocess
from dataclasses import dataclass
from pathlib import Path

from kb.config import KbConfig
from kb.manifest import SourceRow, load_manifest, save_manifest

EMAIL_HEADERS = ("From", "To", "Cc", "Subject", "Date")
KIND_BY_SUFFIX = {
    ".md": "markdown",
    ".markdown": "markdown",
    ".txt": "text",
    ".eml": "email_thread",
    ".pdf": "pdf",
}


class IngestError(Exception):
    pass


@dataclass(frozen=True)
class IngestResult:
    row: SourceRow
    text_path: str
    skipped: bool


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _flatten_email(path: Path) -> str:
    message = email.message_from_bytes(path.read_bytes(), policy=email.policy.default)
    lines = [f"{name}: {message[name]}" for name in EMAIL_HEADERS if message[name]]
    body = message.get_body(preferencelist=("plain", "html"))
    lines.append("")
    lines.append(body.get_content().strip() if body else "")
    return "\n".join(lines) + "\n"


def _convert_pdf(command_template: str | None, source: Path, target: Path) -> str:
    if not command_template:
        raise IngestError(
            f"{source.name} is a PDF but ingest.pdf_command is not set in kb.yaml"
        )
    command = command_template.format(input=shlex.quote(str(source)), output=shlex.quote(str(target)))
    completed = subprocess.run(command, shell=True, capture_output=True, text=True)
    if completed.returncode != 0:
        raise IngestError(f"ingest.pdf_command failed ({completed.returncode}): {completed.stderr.strip()}")
    if not target.is_file():
        raise IngestError("ingest.pdf_command produced no output file")
    return target.read_text()


def ingest(
    root: Path,
    config: KbConfig,
    path: Path,
    source_id: str,
    title: str,
    origin_uri: str,
    today: str,
) -> IngestResult:
    root = Path(root)
    path = Path(path)
    if not path.is_file():
        raise IngestError(f"{path} does not exist")

    suffix = path.suffix.lower()
    kind = KIND_BY_SUFFIX.get(suffix)
    if kind is None:
        raise IngestError(f"no ingest handler for {suffix!r}; supported: {sorted(KIND_BY_SUFFIX)}")

    digest = _sha256(path)
    rows = load_manifest(root)
    existing = next((row for row in rows if row.id == source_id), None)
    text_relative = f"sources/{source_id}/text.md"
    target_dir = root / "sources" / source_id
    target = target_dir / "text.md"

    if existing is not None:
        if existing.sha256 == digest and target.is_file():
            return IngestResult(row=existing, text_path=text_relative, skipped=True)
        raise IngestError(
            f"source id {source_id!r} already exists with different bytes; choose a new id"
        )

    target_dir.mkdir(parents=True, exist_ok=True)
    if kind == "pdf":
        text = _convert_pdf(config.pdf_command, path, target)
    elif kind == "email_thread":
        text = _flatten_email(path)
    else:
        text = path.read_text()
    target.write_text(text)

    row = SourceRow(
        id=source_id,
        title=title,
        kind=kind,
        origin_uri=origin_uri,
        sha256=digest,
        ingested_at=today,
    )
    save_manifest(root, [*rows, row])
    return IngestResult(row=row, text_path=text_relative, skipped=False)
