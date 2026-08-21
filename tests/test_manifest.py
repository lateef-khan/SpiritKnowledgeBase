from kb.manifest import SourceRow, load_manifest, save_manifest, source_refs

ROW = SourceRow(
    id="ticket-88421",
    title="RE: F63 belt slips under load",
    kind="email_thread",
    origin_uri="sharepoint://x/ticket-88421.eml",
    sha256="9f2c",
    ingested_at="2026-08-21",
)


def test_round_trips(tmp_path):
    (tmp_path / "sources").mkdir()
    save_manifest(tmp_path, [ROW])
    assert load_manifest(tmp_path) == [ROW]


def test_missing_manifest_is_empty(tmp_path):
    assert load_manifest(tmp_path) == []
    assert source_refs(tmp_path) == set()


def test_source_refs_returns_ids(tmp_path):
    (tmp_path / "sources").mkdir()
    save_manifest(tmp_path, [ROW])
    assert source_refs(tmp_path) == {"ticket-88421"}
