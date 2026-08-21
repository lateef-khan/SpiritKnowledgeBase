# Spirit Knowledge Base

Markdown knowledge cards, one card per question, synced into Qdrant.

Design: `AgentCore/docs/superpowers/specs/2026-08-21-knowledge-bank-qdrant-design.md`

## Setup

```bash
uv venv && uv pip install -e ".[dev]"
```

## Adding knowledge

```bash
kb ingest ~/Downloads/2026_F63_OM.pdf --id 2026-f63-om \
    --title "2026 F63 owner's manual" --origin "sharepoint://.../2026_F63_OM.pdf"
```

Then in Claude Code:

```
/kb-extract 2026-f63-om
```

Review the pull request it opens. Merging it syncs the cards to Qdrant.

## Commands

| Command | What it does | Needs a key? |
|---|---|---|
| `kb ingest <file>` | Raw artefact to `sources/<id>/text.md` plus a manifest row | no |
| `kb vocab` | Facet vocabulary and card ids, for the extractor | no |
| `kb new <id>` | Scaffold one card with valid frontmatter | no |
| `kb lint` | Ten repo-wide checks | no |
| `kb sync --dry-run` | Plan the diff and print the counts | no |
| `kb sync` | Apply the diff to Qdrant | `OPENAI_API_KEY`, `QDRANT_URL` |
| `kb sync --rebuild` | Rebuild every vector behind the alias | `OPENAI_API_KEY`, `QDRANT_URL` |

## Tests

```bash
.venv/bin/pytest                                    # unit tests
docker compose up -d
.venv/bin/pytest -m integration                     # needs a live Qdrant
docker compose down
```
