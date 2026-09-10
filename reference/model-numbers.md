# Where a machine's model number comes from

`facets.model_number` holds the six digit Sole or Spirit SKUs for a machine. It
is a **list**, because one machine often has more than one: a colour variant is
its own SKU, and so is a commercial trim. Recording one and dropping the rest
loses real data - 171 SKUs across 54 products are not yet on any card.

Every card whose `applies_to` names exactly one machine carries that machine's
numbers; every card naming several machines omits the facet, because there is no
single answer.

The facet is **classification, not a quotation.** `model: lcr-2026` is not a
phrase from the manual either. The card **body** is where the manual is quoted,
and where a manual prints no SKU the body still says so and names where the
number came from instead.

- `reference/model-numbers.csv` — the mapping, one row per machine, with the evidence.
- `reference/model-numbers-open.csv` — machines with no number yet, and their candidates.

## The one table

Every brand lives in `dbo.MODEL` in the `CustService` database on the Spirit
Server, reached over `ssh spirit`: 1,257 rows, SPIRIT 850, SOLE 313, XTERRA 59,
CIKADA 32. The Azure `spiritwebdbTest` database is **not** the right source, and
two cards had been written against it claiming a SKU did not exist when it does.

## What counts as evidence, strongest first

| evidence | machines | what it means |
|---|---|---|
| `own-manual-text` | 48 | the SKU is printed inside that machine's own manual |
| `own-filename` | 47 | the SKU is in the file name of that machine's own manual, **and** is a real row for that product |
| `card-confirmed` | 38 | a card already carried it, read from the printed page |
| `only-candidate` | 14 | the product has exactly one row in the table |
| `year-in-name` | 9 | one row's `MODEL` or `DESC` names the model year |
| `fp-date` | 3 | one row's first-production date falls in the model year or the one before |
| `colour-pair` | 3 | two rows whose names differ only by a colour word, so both are the same machine |
| `user-confirmed` | 1 | a person who knows the product line settled it |
| `sibling-pairing` | 1 | the product has exactly as many machines as SKUs, and the first-production dates order the same way |

**A manual is evidence only for its own model id.** Matching by product name
instead attributes a 2024 book's SKU to the 2018 machine: an early pass did
exactly that for six machines and had to be thrown away.

**A file name must be cross-checked against the table.** `F89(2023)_585822_…pdf`
carries the **F85's** number, and `CIC850_800390_OM_…pdf` carries the
**CIC800's**. Both were caught by refusing any file-name number that is not a
real row for that product.

## Two rules that do not work

**Never decode the last two digits into a model year.** Measured against 113
known-good answers the rule is exact 35% of the time, off by one a further 33%,
and misses by as much as 77.

**`FP_DATE` decides nothing on its own.** It lands on the model year or the one
before 89% of the time, which makes it a tie-breaker and nothing more. Where a
row's name gives a year and `FP_DATE` disagrees, the name is right: `570120` is
the SB700 2020 though its `FP_DATE` reads 2019.

## What was deliberately left out

Answers resting **only** on elimination — "every other SKU in this family is
taken, so this machine must have the last one" — were dropped rather than
guessed: `sc200-2019`, `st90` and `st90-2021`. `xth-rails` is an extended
handrail kit, not a machine, and will never carry a machine SKU.

## Which SKUs belong to the same machine is not in the table

The table does not say that `730030` "Spirit MS300 (White)" and `730037` "Spirit
MS300" are one machine in two colours, and it does not separate them from two
generations that simply never got a year in their name. A rule built on "no year
named means the same machine" wrongly tied the 2023 and 2026 E25 numbers to the
2019 machine, and the 2026 F85's number to the 2023 one. It was thrown away.

The same name is reused across generations, which is the trap. **Five** SKUs are
named plainly "LCR" - 522110, 522112, 522116, 522122, 522126 - and they are five
different machines. So a shared name proves nothing.

One shape is safe. Where two rows' names differ **only by a colour word**, they
are one machine in two colours: `Spirit MT200 (White)` and `Spirit MT200`,
`Spirit MS300 (White)` and `Spirit MS300`. Those cards carry both numbers. Every
other second SKU is added only when a person confirms it.

## A SKU can belong to a machine that has no cards yet

`589826` is the **F89 2026**, confirmed by the product owner. The knowledge base
has only `f89-2023`, so that number belongs to a machine nothing here describes,
and `f89-2023` takes `589853`. Expect this shape wherever one model id faces two
SKUs.

`sibling-pairing` is the narrow case where it can be resolved without asking. The
SC200 has two model ids and two SKUs. The two service manuals are **84.3%**
alike, under the 90% that means one document, and print different factory codes -
`XS110A-YS003` for 2016 against `XS110B-YS007` for 2019. Two machines, two
numbers, and the first-production dates run the same way round: December 2015 to
`sc200-2016`, May 2017 to `sc200-2019`.

That reasoning needs a genuine one-to-one count. The ST90 has **four** model ids
and two SKUs, so it does not qualify and is left open.

## One SKU can cover several machines

`588816` is both the AC and the DC TT8 2016. `600377` covers the 2018 and 2021
XIC600 printings, `600976` the 2019 and 2021 XRW600. A model id is a manual
printing; a SKU is a product. They are not one to one, and `kb facet-gaps`
reports only the reverse case — one machine given two different numbers.

## Checking progress

```bash
kb facet-gaps                    # machines still without a number
kb facet-gaps --facet code       # works for any optional facet
```
