from __future__ import annotations

import datetime
import os
from pathlib import Path

import click

from kb.card import load_cards
from kb.config import load_config
from kb.embed import build_embedder
from kb.ingest import ingest as run_ingest
from kb.lint import lint_cards
from kb.manifest import source_refs
from kb.qdrant import apply_plan, ensure_collection, rebuild
from kb.scaffold import new_card_text
from kb.state import load_state, save_state
from kb.syncplan import DangerousSyncError, plan_sync
from kb.vocab import build_vocab, render_vocab

QDRANT_URL_VARIABLE = "QDRANT_URL"
DEFAULT_QDRANT_URL = "http://localhost:6333"


@click.group()
@click.option("--root", default=".", type=click.Path(file_okay=False), help="Repository root")
@click.pass_context
def main(ctx: click.Context, root: str) -> None:
    ctx.obj = {"root": Path(root)}


def _load(ctx):
    root = ctx.obj["root"]
    return root, load_config(root), load_cards(root)


def _lint(root, config, cards):
    return lint_cards(cards, config, source_refs(root))


@main.command()
@click.pass_context
def lint(ctx: click.Context) -> None:
    root, config, cards = _load(ctx)
    errors = _lint(root, config, cards)
    for error in errors:
        click.echo(f"{error.path}: [{error.check}] {error.message}")
    click.echo(f"{len(errors)} problems in {len(cards)} cards")
    ctx.exit(1 if errors else 0)


@main.command()
@click.pass_context
def vocab(ctx: click.Context) -> None:
    root, config, cards = _load(ctx)
    click.echo(render_vocab(build_vocab(cards, config)))


@main.command()
@click.argument("card_id")
@click.option("--today", default=None, help="Override the extracted_at date")
@click.pass_context
def new(ctx: click.Context, card_id: str, today: str | None) -> None:
    root, config, _ = _load(ctx)
    target = root / "cards" / f"{card_id}.md"
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
    root, config, _ = _load(ctx)
    stamp = today or datetime.date.today().isoformat()
    result = run_ingest(root, config, Path(path), source_id, title, origin, stamp)
    verb = "skipped, already ingested" if result.skipped else "wrote"
    click.echo(f"{verb} {result.text_path}")


@main.command()
@click.option("--dry-run", is_flag=True, help="Plan only; no network, no state written")
@click.option("--force", is_flag=True, help="Allow a sync that deletes over the limit")
@click.option("--rebuild", "do_rebuild", is_flag=True, help="Rebuild into a new collection behind the alias")
@click.option("--stamp", default=None, help="Suffix for the rebuilt collection")
@click.pass_context
def sync(ctx, dry_run, force, do_rebuild, stamp) -> None:
    root, config, cards = _load(ctx)

    errors = _lint(root, config, cards)
    if errors:
        for error in errors:
            click.echo(f"{error.path}: [{error.check}] {error.message}")
        click.echo(f"refusing to sync: {len(errors)} lint problems")
        ctx.exit(1)

    state = load_state(root)
    try:
        plan = plan_sync(cards, state, delete_ratio_limit=1.0 if force else 0.10)
    except DangerousSyncError as exc:
        click.echo(str(exc))
        ctx.exit(1)

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

    if do_rebuild:
        suffix = stamp or datetime.date.today().isoformat().replace("-", "_")
        name = rebuild(client, config, cards, embedder, suffix)
        click.echo(f"rebuilt into {name}")
    else:
        ensure_collection(client, config, config.collection)
        apply_plan(client, config, config.collection, plan, cards, embedder)

    save_state(root, plan.next_state)
    click.echo(f"state written for {len(plan.next_state)} cards")
