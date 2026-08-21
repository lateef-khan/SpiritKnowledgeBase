from __future__ import annotations

import datetime
import os
from pathlib import Path

import click

from kb.card import CardParseError, load_cards, load_cards_leniently
from kb.config import ConfigError, load_config
from kb.embed import EmbedError, build_embedder
from kb.ingest import IngestError, ingest as run_ingest
from kb.lint import lint_cards
from kb.manifest import ManifestError, source_refs
from kb.qdrant import AliasConflictError, apply_plan, ensure_alias, rebuild
from kb.scaffold import ScaffoldError, card_path, new_card_text
from kb.state import load_state, save_state
from kb.syncplan import DEFAULT_DELETE_RATIO_LIMIT, DangerousSyncError, plan_sync
from kb.vocab import build_vocab, render_vocab

QDRANT_URL_VARIABLE = "QDRANT_URL"
DEFAULT_QDRANT_URL = "http://localhost:6333"

DOMAIN_ERRORS = (
    AliasConflictError,
    CardParseError,
    ConfigError,
    DangerousSyncError,
    EmbedError,
    IngestError,
    ManifestError,
    ScaffoldError,
)


class DomainErrorGroup(click.Group):
    """Report a domain error as a message and exit 1, never as a traceback.

    CI runs `kb lint` on every pull request and the extractor parses its output
    to repair its own cards, so a stack trace is an unreadable failure mode.
    """

    def invoke(self, ctx: click.Context):
        try:
            return super().invoke(ctx)
        except DOMAIN_ERRORS as exc:
            click.echo(str(exc))
            ctx.exit(1)


@click.group(cls=DomainErrorGroup)
@click.option("--root", default=".", type=click.Path(file_okay=False), help="Repository root")
@click.pass_context
def main(ctx: click.Context, root: str) -> None:
    ctx.obj = {"root": Path(root)}


def _load_config(ctx):
    root = ctx.obj["root"]
    return root, load_config(root)


def _lint(root, config, cards, failures):
    return lint_cards(cards, config, source_refs(root), failures)


@main.command()
@click.pass_context
def lint(ctx: click.Context) -> None:
    root, config = _load_config(ctx)
    cards, failures = load_cards_leniently(root)
    errors = _lint(root, config, cards, failures)
    for error in errors:
        click.echo(f"{error.path}: [{error.check}] {error.message}")
    click.echo(f"{len(errors)} problems in {len(cards) + len(failures)} cards")
    ctx.exit(1 if errors else 0)


@main.command()
@click.pass_context
def vocab(ctx: click.Context) -> None:
    root, config = _load_config(ctx)
    cards = load_cards(root)
    click.echo(render_vocab(build_vocab(cards, config)))


@main.command()
@click.argument("card_id")
@click.option("--today", default=None, help="Override the extracted_at date")
@click.pass_context
def new(ctx: click.Context, card_id: str, today: str | None) -> None:
    root, config = _load_config(ctx)
    target = card_path(root, card_id)
    if target.exists():
        click.echo(f"{target} already exists")
        ctx.exit(1)
    target.parent.mkdir(parents=True, exist_ok=True)
    stamp = today or datetime.date.today().isoformat()
    target.write_text(new_card_text(card_id, config, stamp))
    click.echo(f"wrote {target.relative_to(root)}")


@main.command()
@click.argument("path", type=click.Path(exists=True, dir_okay=False))
@click.option("--id", "source_id", required=True)
@click.option("--title", required=True)
@click.option("--origin", required=True, help="Where the original artefact lives")
@click.option("--today", default=None)
@click.pass_context
def ingest(ctx, path, source_id, title, origin, today) -> None:
    root, config = _load_config(ctx)
    stamp = today or datetime.date.today().isoformat()
    result = run_ingest(root, config, Path(path), source_id, title, origin, stamp)
    verb = "skipped, already ingested" if result.skipped else "wrote"
    click.echo(f"{verb} {result.text_path}")


@main.command()
@click.option("--dry-run", is_flag=True, help="Plan only; no network, no state written")
@click.option("--force", is_flag=True, help="Allow a sync that deletes over the limit")
@click.option("--rebuild", "do_rebuild", is_flag=True, help="Rebuild into a new collection behind the alias")
@click.option("--stamp", default=None, help="Suffix for a newly created collection")
@click.pass_context
def sync(ctx, dry_run, force, do_rebuild, stamp) -> None:
    root, config = _load_config(ctx)
    cards, failures = load_cards_leniently(root)

    errors = _lint(root, config, cards, failures)
    if errors:
        for error in errors:
            click.echo(f"{error.path}: [{error.check}] {error.message}")
        click.echo(f"refusing to sync: {len(errors)} lint problems")
        ctx.exit(1)

    state = load_state(root)
    plan = plan_sync(cards, state, delete_ratio_limit=1.0 if force else DEFAULT_DELETE_RATIO_LIMIT)

    counts = plan.counts()
    summary = " ".join(f"{op} {counts[op]}" for op in ("upsert", "set_payload", "delete", "skip"))
    click.echo(summary)
    if dry_run:
        return

    from qdrant_client import QdrantClient

    client = QdrantClient(
        url=os.environ.get(QDRANT_URL_VARIABLE, DEFAULT_QDRANT_URL),
        prefer_grpc=False,
        timeout=120,
    )
    embedder = build_embedder(config)
    suffix = stamp or datetime.date.today().isoformat().replace("-", "_")

    if do_rebuild:
        name = rebuild(client, config, cards, embedder, suffix)
        click.echo(f"rebuilt into {name}")
    else:
        name = ensure_alias(client, config, suffix)
        apply_plan(client, config, name, plan, cards, embedder)

    save_state(root, plan.next_state)
    click.echo(f"state written for {len(plan.next_state)} cards")
