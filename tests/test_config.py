from pathlib import Path

import pytest

from kb.config import ConfigError, load_config

MINIMAL = """
collection: kb
embedding:
  model: text-embedding-3-small
  dimensions: 1024
kinds: [fact, policy]
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


def write(tmp_path: Path, text: str) -> Path:
    (tmp_path / "kb.yaml").write_text(text)
    return tmp_path


def test_loads_collection_and_embedding(tmp_path):
    cfg = load_config(write(tmp_path, MINIMAL))
    assert cfg.collection == "kb"
    assert cfg.embedding_model == "text-embedding-3-small"
    assert cfg.embedding_dimensions == 1024


def test_loads_facets_with_array_flag(tmp_path):
    cfg = load_config(write(tmp_path, MINIMAL))
    assert cfg.facets["model"].index == "keyword"
    assert cfg.facets["model"].values == ("f63", "*")
    assert cfg.facets["model"].array is False
    assert cfg.facets["applies_to"].array is True
    assert cfg.facets["applies_to"].values == ()


def test_kinds_is_a_tuple(tmp_path):
    cfg = load_config(write(tmp_path, MINIMAL)).kinds
    assert cfg == ("fact", "policy")


def test_missing_file_raises(tmp_path):
    with pytest.raises(ConfigError, match="kb.yaml not found"):
        load_config(tmp_path)


def test_wrong_dimensions_raises(tmp_path):
    bad = MINIMAL.replace("dimensions: 1024", "dimensions: 1536")
    with pytest.raises(ConfigError, match="1024"):
        load_config(write(tmp_path, bad))


def test_missing_collection_raises(tmp_path):
    bad = MINIMAL.replace("collection: kb\n", "")
    with pytest.raises(ConfigError, match="collection"):
        load_config(write(tmp_path, bad))


def test_unknown_facet_index_type_raises(tmp_path):
    bad = MINIMAL.replace("index: keyword\n    values: [f63", "index: banana\n    values: [f63")
    with pytest.raises(ConfigError, match="banana"):
        load_config(write(tmp_path, bad))


def test_non_mapping_yaml_raises(tmp_path):
    with pytest.raises(ConfigError, match="mapping"):
        load_config(write(tmp_path, "- a\n- b\n"))


def test_kinds_as_scalar_raises(tmp_path):
    bad = MINIMAL.replace("kinds: [fact, policy]", "kinds: fact")
    with pytest.raises(ConfigError, match="kinds"):
        load_config(write(tmp_path, bad))


def test_list_shaped_payload_indexes_raises(tmp_path):
    bad = MINIMAL.replace("payload_indexes:\n  card_id:\n    index: keyword", "payload_indexes: [a, b]")
    with pytest.raises(ConfigError, match="payload_indexes"):
        load_config(write(tmp_path, bad))


def test_list_shaped_ingest_raises(tmp_path):
    bad = MINIMAL.replace("ingest:\n  pdf_command: null", "ingest: [a, b]")
    with pytest.raises(ConfigError, match="ingest"):
        load_config(write(tmp_path, bad))


def test_list_shaped_facet_spec_raises(tmp_path):
    bad = MINIMAL.replace("  model:\n    index: keyword\n    values: [f63, \"*\"]", "  model: [a, b]")
    with pytest.raises(ConfigError, match="model"):
        load_config(write(tmp_path, bad))
