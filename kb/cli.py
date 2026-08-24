from __future__ import annotations

import contextlib
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
from kb.qdrant import (
    AliasConflictError,
    QdrantError,
    apply_plan,
    ensure_alias,
    rebuild,
    refuse_concrete_collection,
)
from kb.scaffold import ScaffoldError, card_path, new_card_text
from kb.state import read_state
from kb.syncplan import DEFAULT_DELETE_RATIO_LIMIT, DangerousSyncError, plan_sync
from kb.vocab import build_vocab, render_vocab

QDRANT_URL_VARIABLE = "QDRANT_URL"
QDRANT_API_KEY_VARIABLE = "QDRANT_API_KEY"
DEFAULT_QDRANT_URL = "http://localhost:6333"
ENV_FILENAME = ".env"


def default_stamp() -> str:
    return datetime.date.today().isoformat().replace("-", "_")


def client_kwargs() -> dict:
    kwargs = {
        "url": os.environ.get(QDRANT_URL_VARIABLE, DEFAULT_QDRANT_URL),
        "prefer_grpc": False,
        "timeout": 120,
    }
    api_key = os.environ.get(QDRANT_API_KEY_VARIABLE)
    if api_key:
        kwargs["api_key"] = api_key
    return kwargs


def build_client():
    from qdrant_client import QdrantClient

    return QdrantClient(**client_kwargs())


@contextlib.contextmanager
def qdrant_errors(url: str):
    """Report any Qdrant API failure as a message, not a traceback.

    ApiException is the shared base of a transport failure, every 4xx and 5xx, and a
    response whose body fails validation. Catching one named class keeps the
    domain-error invariant below.
    """
    from qdrant_client.http.exceptions import ApiException

    try:
        yield
    except ApiException as exc:
        raise QdrantError(
            f"Qdrant call to {url} failed: {exc}. Check that the server is up and that "
            f"{QDRANT_URL_VARIABLE} and {QDRANT_API_KEY_VARIABLE} name and authenticate it."
        ) from exc


# Invariant: a domain error class is raised only by explicit validation, never by
# wrapping a broad except, so this handler can never swallow an unrelated bug.
DOMAIN_ERRORS = (
    AliasConflictError,
    CardParseError,
    ConfigError,
    DangerousSyncError,
    EmbedError,
    IngestError,
    ManifestError,
    QdrantError,
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


def load_env_file(root: Path) -> None:
    """Read <root>/.env, letting a real environment variable win.

    CI supplies its secrets through the environment and ships no .env, so a file
    that overrode the environment would silently sync a developer's laptop keys.
    """
    from dotenv import load_dotenv

    load_dotenv(Path(root) / ENV_FILENAME, override=False)


@click.group(cls=DomainErrorGroup)
@click.option("--root", default=".", type=click.Path(file_okay=False), help="Repository root")
@click.pass_context
def main(ctx: click.Context, root: str) -> None:
    ctx.obj = {"root": Path(root)}
    load_env_file(Path(root))


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
@click.option("--dry-run", is_flag=True, help="Plan only; reads Qdrant, writes nothing")
@click.option("--force", is_flag=True, help="Allow a sync that deletes over the limit")
@click.option("--rebuild", "do_rebuild", is_flag=True, help="Rebuild into a new collection behind the alias")
@click.option("--stamp", default=None, help="Suffix for a newly created collection")
@click.pass_context
def sync(ctx, dry_run, force, do_rebuild, stamp) -> None:
    """Bring the Qdrant collection in line with the cards.

    Needs QDRANT_URL and QDRANT_API_KEY, and OPENAI_API_KEY unless every card
    skips. `kb lint` needs none of them and stays offline.
    """
    root, config = _load_config(ctx)
    cards, failures = load_cards_leniently(root)

    errors = _lint(root, config, cards, failures)
    if errors:
        for error in errors:
            click.echo(f"{error.path}: [{error.check}] {error.message}")
        click.echo(f"refusing to sync: {len(errors)} lint problems")
        ctx.exit(1)

    url = client_kwargs()["url"]
    client = build_client()
    with qdrant_errors(url):
        state = read_state(client, config.collection)
        refuse_concrete_collection(client, config.collection)

    plan = plan_sync(cards, state, delete_ratio_limit=1.0 if force else DEFAULT_DELETE_RATIO_LIMIT)
    counts = plan.counts()
    if do_rebuild:
        click.echo(f"rebuilding {len(cards)} cards")
    else:
        click.echo(" ".join(f"{op} {counts[op]}" for op in ("upsert", "set_payload", "delete", "skip")))
    if dry_run:
        return

    embedder = build_embedder(config) if do_rebuild or counts["upsert"] else None
    suffix = stamp or default_stamp()

    with qdrant_errors(url):
        if do_rebuild:
            name = rebuild(client, config, cards, embedder, suffix)
        else:
            name = ensure_alias(client, config, suffix)
            apply_plan(client, config, name, plan, cards, embedder)
    click.echo(f"rebuilt into {name}" if do_rebuild else f"synced into {name}")
