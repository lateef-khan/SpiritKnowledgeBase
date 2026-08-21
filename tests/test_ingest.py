from pathlib import Path

import pytest

from kb.config import FacetSpec, KbConfig
from kb.ingest import IngestError, ingest
from kb.manifest import load_manifest


def config(pdf_command=None):
    return KbConfig(
        root=Path("."),
        collection="kb",
        embedding_model="text-embedding-3-small",
        embedding_dimensions=1024,
        kinds=("fact",),
        facets={"model": FacetSpec(index="keyword", array=False, values=())},
        payload_indexes={},
        pdf_command=pdf_command,
    )


def test_markdown_source_is_copied(tmp_path):
    src = tmp_path / "in.md"
    src.write_text("# Hello\n\nWorld.\n")
    result = ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.md", "2026-08-21")
    written = tmp_path / "sources" / "doc-1" / "text.md"
    assert written.read_text() == "# Hello\n\nWorld.\n"
    assert result.text_path == "sources/doc-1/text.md"
    assert result.skipped is False


def test_manifest_row_is_appended(tmp_path):
    src = tmp_path / "in.txt"
    src.write_text("plain text")
    ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.txt", "2026-08-21")
    rows = load_manifest(tmp_path)
    assert len(rows) == 1
    assert rows[0].id == "doc-1"
    assert rows[0].kind == "text"
    assert rows[0].ingested_at == "2026-08-21"
    assert len(rows[0].sha256) == 64


def test_re_ingesting_identical_bytes_is_skipped(tmp_path):
    src = tmp_path / "in.txt"
    src.write_text("plain text")
    ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.txt", "2026-08-21")
    again = ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.txt", "2026-08-22")
    assert again.skipped is True
    assert len(load_manifest(tmp_path)) == 1
    assert load_manifest(tmp_path)[0].ingested_at == "2026-08-21"


def test_changed_bytes_under_same_id_raises(tmp_path):
    src = tmp_path / "in.txt"
    src.write_text("plain text")
    ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.txt", "2026-08-21")
    src.write_text("different text")
    with pytest.raises(IngestError, match="different bytes"):
        ingest(tmp_path, config(), src, "doc-1", "Doc One", "file:///in.txt", "2026-08-22")


def test_email_is_flattened_with_headers(tmp_path):
    src = tmp_path / "thread.eml"
    src.write_text(
        "From: tech@example.com\n"
        "To: cust@example.com\n"
        "Subject: belt slips\n"
        "Date: Mon, 3 Aug 2026 09:00:00 +0000\n"
        "\n"
        "Tighten the rear roller bolts.\n"
    )
    ingest(tmp_path, config(), src, "t-1", "belt slips", "file:///thread.eml", "2026-08-21")
    text = (tmp_path / "sources" / "t-1" / "text.md").read_text()
    assert "Subject: belt slips" in text
    assert "Tighten the rear roller bolts." in text
    assert load_manifest(tmp_path)[0].kind == "email_thread"


def test_pdf_without_configured_command_raises(tmp_path):
    src = tmp_path / "manual.pdf"
    src.write_bytes(b"%PDF-1.7 fake")
    with pytest.raises(IngestError, match="ingest.pdf_command"):
        ingest(tmp_path, config(), src, "m-1", "Manual", "file:///manual.pdf", "2026-08-21")


def test_pdf_uses_configured_command(tmp_path):
    src = tmp_path / "manual.pdf"
    src.write_bytes(b"%PDF-1.7 fake")
    command = "printf 'converted %s' {input} > {output}"
    ingest(tmp_path, config(command), src, "m-1", "Manual", "file:///manual.pdf", "2026-08-21")
    text = (tmp_path / "sources" / "m-1" / "text.md").read_text()
    assert text.startswith("converted ")
    assert load_manifest(tmp_path)[0].kind == "pdf"


def test_unknown_extension_raises(tmp_path):
    src = tmp_path / "thing.docx"
    src.write_bytes(b"zip")
    with pytest.raises(IngestError, match="\\.docx"):
        ingest(tmp_path, config(), src, "d-1", "Thing", "file:///thing.docx", "2026-08-21")
