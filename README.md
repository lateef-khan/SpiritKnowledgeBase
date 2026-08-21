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
| `kb sync` | Apply the diff to Qdrant | `OPENAI_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY` |
| `kb sync --rebuild` | Rebuild every vector behind the alias | `OPENAI_API_KEY`, `QDRANT_URL`, `QDRANT_API_KEY` |

`QDRANT_URL` defaults to `http://localhost:6333`. `QDRANT_API_KEY` is optional:
set it for Qdrant Cloud or any authenticated endpoint, leave it unset for an
unauthenticated self-hosted container.

Both sync modes address the collection name in `kb.yaml` as a **Qdrant alias**.
The first sync creates `<collection>_<stamp>` and points the alias at it; every
`--rebuild` builds a new stamped collection and moves the alias. The .NET reader
queries the alias and never sees the swap.

## Not yet supported

`kb ingest` handles local `.md`, `.markdown`, `.txt`, `.eml` and `.pdf` files.
The design's `kb ingest <file-or-uri>` also names a web-page-to-Markdown path;
that is a deliberate deferral, not an oversight — URL fetching and HTML
conversion are a feature with their own dependencies. Until it exists, save the
page as Markdown by hand and ingest the file.

## Tests

```bash
.venv/bin/pytest                                    # unit tests
docker compose up -d
.venv/bin/pytest -m integration                     # needs a live Qdrant
docker compose down
```
