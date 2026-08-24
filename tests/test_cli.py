import pytest
from click.testing import CliRunner
from qdrant_client import models
from qdrant_client.http.exceptions import ResponseHandlingException, UnexpectedResponse

from kb.card import parse_card
from kb.cli import client_kwargs, main
from kb.state import state_for

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

MALFORMED_CARD = """---
id: card-broken
title: Broken
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


class FakeQdrant:
    def __init__(self, records=(), alias="kb"):
        self._records = list(records)
        self._aliases = [
            models.AliasDescription(alias_name=alias, collection_name=f"{alias}_2026_01_01")
        ]
        self.calls = []

    def collection_exists(self, name):
        return name in {alias.alias_name for alias in self._aliases}

    def scroll(self, collection_name, **kwargs):
        self.calls.append("scroll")
        return list(self._records), None

    def get_aliases(self):
        return models.CollectionsAliasesResponse(aliases=list(self._aliases))

    def create_collection(self, **kwargs):
        self.calls.append("create_collection")

    def create_payload_index(self, **kwargs):
        self.calls.append("create_payload_index")

    def upsert(self, **kwargs):
        self.calls.append("upsert")

    def set_payload(self, **kwargs):
        self.calls.append("set_payload")

    def delete(self, **kwargs):
        self.calls.append("delete")

    def delete_collection(self, collection_name):
        self.calls.append("delete_collection")

    def update_collection_aliases(self, **kwargs):
        self.calls.append("update_collection_aliases")


WRITE_CALLS = {
    "create_collection",
    "create_payload_index",
    "upsert",
    "set_payload",
    "delete",
    "delete_collection",
    "update_collection_aliases",
}


class FakeEmbedder:
    def embed(self, texts):
        return [[0.5] * 1024 for _ in texts]


def install_client(monkeypatch, client):
    """Hand `sync` a fake client and return one entry per client built."""
    built = []

    def factory():
        built.append(client)
        return client

    monkeypatch.setattr("kb.cli.build_client", factory)
    return built


def install_embedder(monkeypatch):
    """Hand `sync` a fake embedder and return one entry per embedder built."""
    built = []

    def factory(config):
        built.append(config)
        return FakeEmbedder()

    monkeypatch.setattr("kb.cli.build_embedder", factory)
    return built


class ReadFailsQdrant(FakeQdrant):
    def __init__(self, error):
        super().__init__()
        self._error = error

    def collection_exists(self, name):
        raise self._error


class UpsertFailsQdrant(FakeQdrant):
    def __init__(self, error):
        super().__init__()
        self._error = error

    def upsert(self, **kwargs):
        raise self._error


class ConcreteCollectionQdrant(FakeQdrant):
    def __init__(self):
        super().__init__(alias="something-else")

    def collection_exists(self, name):
        return True


def http_error(status_code, reason_phrase, content):
    return UnexpectedResponse(
        status_code=status_code, reason_phrase=reason_phrase, content=content, headers={}
    )


def spy_on_the_real_embedder(monkeypatch):
    """Record each build_embedder call and still build the real one."""
    from kb.embed import build_embedder as real

    built = []

    def factory(config):
        built.append(config)
        return real(config)

    monkeypatch.setattr("kb.cli.build_embedder", factory)
    return built


def matching_record():
    state = state_for(parse_card(CARD, "cards/card-a.md"))
    return models.Record(
        id=state.point_id,
        payload={
            "card_id": "card-a",
            "embed_hash": state.embed_hash,
            "payload_hash": state.payload_hash,
        },
    )


def ghost(card_id):
    return models.Record(
        id=card_id,
        payload={"card_id": card_id, "embed_hash": "e", "payload_hash": "p"},
    )


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


def test_sync_dry_run_prints_counts_and_writes_nothing(repo, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    client = FakeQdrant()
    install_client(monkeypatch, client)
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 0
    assert "upsert 1" in result.output
    assert not WRITE_CALLS & set(client.calls)


def test_sync_dry_run_reports_the_safety_rail(repo, monkeypatch):
    client = FakeQdrant(records=[ghost(f"ghost-{i}") for i in range(20)])
    install_client(monkeypatch, client)
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "--force" in result.output


def test_sync_never_builds_a_client_when_lint_fails(repo, monkeypatch):
    (repo / "cards" / "card-b.md").write_text(
        CARD.replace("ref: src-1", "ref: ghost").replace("id: card-a", "id: card-b")
    )
    built = install_client(monkeypatch, FakeQdrant())
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert built == []


def test_sync_reads_the_state_before_it_writes(repo, monkeypatch):
    client = FakeQdrant()
    install_client(monkeypatch, client)
    install_embedder(monkeypatch)
    result = run(repo, "sync")
    assert result.exit_code == 0
    assert client.calls.index("scroll") < client.calls.index("upsert")
    assert "synced into kb" in result.output


def test_lint_runs_with_every_credential_unset(repo, monkeypatch):
    for name in ("QDRANT_URL", "QDRANT_API_KEY", "OPENAI_API_KEY"):
        monkeypatch.delenv(name, raising=False)
    result = run(repo, "lint")
    assert result.exit_code == 0
    assert "0 problems" in result.output


def test_sync_refuses_when_lint_fails(repo):
    (repo / "cards" / "card-b.md").write_text(CARD.replace("ref: src-1", "ref: ghost").replace("id: card-a", "id: card-b"))
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "unknown-source" in result.output


def test_new_ignores_a_malformed_card_elsewhere_in_the_repo(repo):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    result = run(repo, "new", "card-z", "--today", "2026-08-21")
    assert result.exit_code == 0
    assert (repo / "cards" / "card-z.md").exists()


def test_ingest_ignores_a_malformed_card_elsewhere_in_the_repo(repo, tmp_path):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    src = tmp_path / "two.md"
    src.write_text("# Two\n")
    result = run(
        repo, "ingest", str(src), "--id", "src-2", "--title", "Source Two",
        "--origin", "file:///two.md", "--today", "2026-08-21",
    )
    assert result.exit_code == 0
    assert (repo / "sources" / "src-2" / "text.md").exists()


def test_lint_reports_the_malformed_card_as_a_named_check(repo):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    result = run(repo, "lint")
    assert result.exit_code == 1
    assert "cards/card-broken.md: [unparseable]" in result.output
    assert "Traceback" not in result.output


def test_lint_still_checks_the_good_cards_beside_a_malformed_one(repo):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    (repo / "cards" / "card-b.md").write_text(
        CARD.replace("ref: src-1", "ref: ghost").replace("id: card-a", "id: card-b")
    )
    result = run(repo, "lint")
    assert "unparseable" in result.output
    assert "unknown-source" in result.output
    assert "2 problems in 3 cards" in result.output


def test_sync_refuses_when_a_card_is_unparseable(repo):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "unparseable" in result.output


def test_a_malformed_kb_yaml_reports_without_a_traceback(repo):
    (repo / "kb.yaml").write_text("- a\n- b\n")
    result = run(repo, "lint")
    assert result.exit_code == 1
    assert "mapping" in result.output
    assert result.exception is None or isinstance(result.exception, SystemExit)


def test_a_malformed_manifest_row_reports_without_a_traceback(repo):
    (repo / "sources" / "manifest.yaml").write_text("- id: src-1\n  title: Only a title\n")
    result = run(repo, "lint")
    assert result.exit_code == 1
    assert "manifest" in result.output
    assert result.exception is None or isinstance(result.exception, SystemExit)


def test_vocab_reports_a_malformed_card_without_a_traceback(repo):
    (repo / "cards" / "card-broken.md").write_text(MALFORMED_CARD)
    result = run(repo, "vocab")
    assert result.exit_code == 1
    assert "frontmatter" in result.output
    assert result.exception is None or isinstance(result.exception, SystemExit)


def test_ingest_reports_a_domain_error_without_a_traceback(repo, tmp_path):
    src = tmp_path / "two.md"
    src.write_text("# Two\n")
    result = run(
        repo, "ingest", str(src), "--id", "bad id", "--title", "Source Two",
        "--origin", "file:///two.md", "--today", "2026-08-21",
    )
    assert result.exit_code == 1
    assert "invalid" in result.output


def test_new_refuses_an_id_that_escapes_the_repo(repo, tmp_path):
    result = run(repo, "new", "../../escaped", "--today", "2026-08-21")
    assert result.exit_code == 1
    assert "escaped" in result.output
    assert not (repo.parent.parent / "escaped.md").exists()
    assert list((repo / "cards").iterdir()) == [repo / "cards" / "card-a.md"]


def test_new_refuses_an_id_with_a_path_separator(repo):
    result = run(repo, "new", "f63/errors/e03", "--today", "2026-08-21")
    assert result.exit_code == 1
    assert not (repo / "cards" / "f63").exists()


def test_new_refuses_an_uppercase_id(repo):
    result = run(repo, "new", "F63-E03", "--today", "2026-08-21")
    assert result.exit_code == 1
    assert "lowercase" in result.output


def test_sync_passes_the_qdrant_api_key_when_the_environment_sets_one(repo, monkeypatch):
    monkeypatch.setenv("QDRANT_API_KEY", "secret-token")
    assert client_kwargs() == {
        "url": "http://localhost:6333",
        "prefer_grpc": False,
        "timeout": 120,
        "api_key": "secret-token",
    }


def test_sync_omits_the_qdrant_api_key_when_the_environment_has_none(repo, monkeypatch):
    monkeypatch.delenv("QDRANT_API_KEY", raising=False)
    assert "api_key" not in client_kwargs()


def test_sync_reads_the_qdrant_url_from_the_environment(repo, monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "https://example.cloud.qdrant.io:6333")
    assert client_kwargs()["url"] == "https://example.cloud.qdrant.io:6333"


def test_lint_reports_an_undecodable_card_without_a_traceback(repo):
    (repo / "cards" / "card-binary.md").write_bytes(b"---\nid: x\n\xff\xfe\n---\n")
    result = run(repo, "lint")
    assert result.exit_code == 1
    assert "cards/card-binary.md: [unparseable]" in result.output
    assert "Traceback" not in result.output


def test_a_sync_where_every_card_skips_needs_no_openai_key(repo, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    install_client(monkeypatch, FakeQdrant(records=[matching_record()]))
    built = spy_on_the_real_embedder(monkeypatch)
    result = run(repo, "sync")
    assert result.exit_code == 0
    assert "skip 1" in result.output
    assert built == []


def test_a_sync_with_an_upsert_still_builds_the_embedder(repo, monkeypatch):
    install_client(monkeypatch, FakeQdrant())
    built = install_embedder(monkeypatch)
    result = run(repo, "sync")
    assert result.exit_code == 0
    assert "upsert 1" in result.output
    assert len(built) == 1


def test_rebuild_reports_the_cards_it_embeds_not_the_plan_it_discards(repo, monkeypatch):
    install_client(monkeypatch, FakeQdrant(records=[matching_record()]))
    built = install_embedder(monkeypatch)
    result = run(repo, "sync", "--rebuild", "--stamp", "later")
    assert result.exit_code == 0
    assert "rebuilding 1 cards" in result.output
    assert "skip 1" not in result.output
    assert len(built) == 1


def test_sync_reports_an_unreachable_qdrant_as_a_message(repo, monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "http://qdrant.example:6333")
    error = ResponseHandlingException(ConnectionError("[Errno 111] Connection refused"))
    install_client(monkeypatch, ReadFailsQdrant(error))
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "http://qdrant.example:6333" in result.output
    assert "Connection refused" in result.output
    assert "Traceback" not in result.output


def test_sync_reports_a_rejected_api_key_as_a_message(repo, monkeypatch):
    monkeypatch.setenv("QDRANT_URL", "http://qdrant.example:6333")
    error = http_error(403, "Forbidden", b"Must provide an API key or an Authorization bearer token")
    install_client(monkeypatch, ReadFailsQdrant(error))
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "403" in result.output
    assert "Must provide an API key" in result.output
    assert "QDRANT_API_KEY" in result.output
    assert "Traceback" not in result.output


def test_sync_reports_a_server_error_as_a_message(repo, monkeypatch):
    install_client(monkeypatch, ReadFailsQdrant(http_error(500, "Internal Server Error", b"boom")))
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "500" in result.output
    assert "Traceback" not in result.output


def test_sync_reports_a_failed_write_as_a_message(repo, monkeypatch):
    install_client(monkeypatch, UpsertFailsQdrant(http_error(500, "Internal Server Error", b"boom")))
    install_embedder(monkeypatch)
    result = run(repo, "sync")
    assert result.exit_code == 1
    assert "500" in result.output
    assert "Traceback" not in result.output


def test_dry_run_refuses_a_concrete_collection_where_an_alias_is_required(repo, monkeypatch):
    install_client(monkeypatch, ConcreteCollectionQdrant())
    result = run(repo, "sync", "--dry-run")
    assert result.exit_code == 1
    assert "concrete collection" in result.output
