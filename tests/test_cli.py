import json

import pytest
from click.testing import CliRunner

from kb.cli import main

KB_YAML = """
collection: kb
embedding:
  model: text-embedding-3-small
  dimensions: 1024
kinds: [fact, troubleshooting]
facets:
  model:
    index: keyword
    values: [f63, "*"]
  applies_to:
    index: keyword
    array: true
payload_indexes:
  card_id:
    index: keyword
ingest:
  pdf_command: null
"""

CARD = """---
id: card-a
title: Card A
kind: fact
question: What is A?
asked_as: [one phrasing, two phrasing]
keywords: [alpha, beta, gamma, delta]
facets:
  model: f63
  applies_to: [f63]
authority: 3
not_to_be_confused_with: []
see_also: []
source:
  ref: src-1
  locator: p.1
  extracted_at: 2026-08-21
---

Body text.
"""

MANIFEST = """
- id: src-1
  title: Source One
  kind: markdown
  origin_uri: file:///one.md
  sha256: abc
  ingested_at: 2026-08-21
"""


@pytest.fixture
def repo(tmp_path):
    (tmp_path / "kb.yaml").write_text(KB_YAML)
    (tmp_path / "cards").mkdir()
    (tmp_path / "cards" / "card-a.md").write_text(CARD)
    (tmp_path / "sources").mkdir()
    (tmp_path / "sources" / "manifest.yaml").write_text(MANIFEST)
    return tmp_path


def run(repo, *args):
    return CliRunner().invoke(main, ["--root", str(repo), *args])


def test_lint_passes_on_a_clean_repo(repo):
    result = run(repo, "lint")
    assert result.exit_code == 0
    assert "0 problems" in result.output


def test_lint_fails_and_names_the_check(repo):
    (repo / "cards" / "card-b.md").write_text(CARD.replace("ref: src-1", "ref: ghost").replace("id: card-a", "id: card-b"))
    result = run(repo, "lint")
    assert result.exit_code == 1
    assert "unknown-source" in result.output


def test_vocab_prints_facets_and_card_ids(repo):
    result = run(repo, "vocab")
    assert result.exit_code == 0
    assert "card-a" in result.output
    assert "applies_to" in result.output


def test_new_writes_a_card_that_parses(repo):
    result = run(repo, "new", "card-z", "--today", "2026-08-21")
    assert result.exit_code == 0
    written = (repo / "cards" / "card-z.md").read_text()
    assert "id: card-z" in written
    assert "REPLACE-WITH-SOURCE-ID" in written


def test_new_refuses_to_overwrite(repo):
    run(repo, "new", "card-z", "--today", "2026-08-21")
    result = run(repo, "new", "card-z", "--today", "2026-08-21")
    assert result.exit_code == 1
    assert "already exists" in result.output


def test_ingest_writes_source_and_manifest_row(repo, tmp_path):
    src = tmp_path / "two.md"
    src.write_text("# Two\n")
    result = run(
        repo, "ingest", str(src), "--id", "src-2", "--title", "Source Two",
        "--origin", "file:///two.md", "--today", "2026-08-21",
    )
    assert result.exit_code == 0
    assert (repo / "sources" / "src-2" / "text.md").read_text() == "# Two\n"
    assert "src-2" in (repo / "sources" / "manifest.yaml").read_text()


def test_sync_dry_run_prints_counts_and_writes_no_state(repo):
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 0
    assert "upsert 1" in result.output
    assert not (repo / ".kb-state.json").exists()


def test_sync_dry_run_reports_the_safety_rail(repo):
    (repo / ".kb-state.json").write_text(
        json.dumps({f"ghost-{i}": {"embed_hash": "e", "payload_hash": "p", "point_id": "x"} for i in range(20)})
    )
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "--force" in result.output


def test_sync_refuses_when_lint_fails(repo):
    (repo / "cards" / "card-b.md").write_text(CARD.replace("ref: src-1", "ref: ghost").replace("id: card-a", "id: card-b"))
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "unknown-source" in result.output
