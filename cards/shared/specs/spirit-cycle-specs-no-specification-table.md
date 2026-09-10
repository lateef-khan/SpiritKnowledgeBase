---
id: spirit-cycle-specs-no-specification-table
title: No specification table in eight indoor cycle and air bike manuals, and the console
  ranges printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight and flywheel weight
  for a Spirit indoor cycle or air bike?
asked_as:
- how much does the spirit indoor cycle weigh
- how big is the air bike
- what is the shipping weight of the spin bike
- how heavy is the flywheel on the spirit cycle
keywords:
- specifications
- spec sheet
- assembled dimensions
- footprint
- machine weight
- shipping weight
- carton size
- flywheel weight
- q factor
- floor space
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - ab900-2018
  - ab950-2024
  - cb900-2013
  - cic800-2021
  - cic850-2022
  - jb950-2022
  - xic600-2018
  - xic600-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-no-specification-table
- spirit-residential-bike-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-xe-specs-no-specification-table
see_also:
- spirit-cycle-specs-which-manuals-print-a-parts-list
- spirit-cycle-specs-resistance-systems
- spirit-cycle-specs-console-display-type
- spirit-bike-safety-user-weight-limit-350-lb
- spirit-xic600-safety-user-weight-limit-300-lbs
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: 'Table of Contents printed p. 3 and whole document; the same absence was
    checked in all eight manuals - CB900-2013, XIC600-2018, AB900-2018, CIC800-2021,
    XIC600-2021, CIC850-2022, JB950-2022 and AB950-2024, each at its own Table of
    Contents and across every page of its PDF'
  extracted_at: '2026-09-09'
---

**None of the eight Spirit indoor cycle and air bike owner's manuals contains a
specification table.** All eight were checked. No table of contents has a
Specifications entry, the word *dimension* appears in none of the eight, and none
of these figures is printed anywhere in any of them:

- **assembled dimensions** - no length, width or height, in any unit
- **machine weight**, shipping weight, gross weight or carton size
- **flywheel weight or diameter**, and no fan diameter on either air bike
- a **floor footprint** or a required operating area
- a **resistance range in watts, newtons or kilograms**
- a **Q factor** or pedal-spacing measurement
- a **screen size**, resolution or panel technology - see
  `spirit-cycle-specs-console-display-type`

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them. **Do not carry a figure across from one of
these machines to another** - this wave is six unrelated machine types, not a
family - **and never in from a Sole bike.**

## The only weight figures the eight print are rider weight limits

There is no machine weight in any of the eight. A search for `lbs`, `pounds`,
`lb` or `kg` returns only the user weight limit and fastener sizes. The limits
themselves are a safety figure and live in the `safety` section:

| Manual | Rider weight limit printed |
|---|---|
| XIC600-2018, XIC600-2021 | 300 lbs |
| CIC800-2021, CIC850-2022, AB900-2018, AB950-2024 | 350 lb (the AB900 adds 159 kilograms) |
| JB950-2022 | **450 lb on one page and 350 lbs / 159 kg on another** |
| CB900-2013 | **none at all** |

See `spirit-bike-safety-user-weight-limit-350-lb`,
`spirit-xic600-safety-user-weight-limit-300-lbs` and
`jb950-2022-safety-user-weight-limit-450-and-350`. **A rider weight limit is not
a machine weight**; a customer asking "how much does it weigh" is not answered by
any of these numbers.

## What these manuals print instead of a specification table

| Figure | What is printed | Where |
|---|---|---|
| Console measuring ranges | a **CONSOLE SPECIFICATION** block on the XIC600, and the same shaped block unheaded on the CIC850 - the two disagree | `console` |
| Resistance | a **kind** of resistance, never a rating; only the JB950 has numbered levels, and it has 20 | specs |
| Exploded view and parts list | in **three** of the eight - see `spirit-cycle-specs-which-manuals-print-a-parts-list` | specs |
| Operating temperature and humidity | 40 to 120 °F, 95% non-condensing | `safety` |
| Power source | AAA or AA cells, or pedalling; **no machine here needs a wall outlet** | `safety` |

The console block is a **console** specification, not a machine specification. It
gives display ranges - RPM, speed, pulse, timer - and nothing about the bike.

## This absence was proved from rendered pages, not from the text extract

A missing specification table is exactly the claim a flat-image page fakes, so
this was checked against the PDFs themselves.

Every page of all eight PDFs - **319 pages** - was counted for extractable words,
and every page whose count was low was rendered at 300 dpi and read with
`tesseract --psm 4`. The pages that turned out to be pictures are the console
photographs, the exploded drawings, a parts-list description column and a handful
of app screenshots. **Not one of them carries specification data.** The CB900's
two wordless pages (PDF pages 2 and 4) are genuinely blank: they OCR to zero
words.

**There is no specification table in these eight manuals. Do not re-run this
check.**

## This is a different set of machines from the thirteen commercial bikes

`spirit-bike-specs-no-specification-table` records the same absence for the
thirteen Spirit commercial upright and recumbent bikes - CR800, CR900, CU800,
CU900 and their ENT variants. **That card's supporting figures do not apply
here**: it reports a 450 lb limit, 40 resistance levels and a generator or
induction brake, and none of those is true of an indoor cycle or an air bike.
Read whichever card names the machine in front of you.
