---
id: spirit-ct900-specs-no-specification-table
title: Three owner's manuals with no specification table; the service manuals add a drive-belt
  figure for each machine, and the only motor rating is 3.0HP AC
kind: fact
question: Where are the motor rating, running deck size, dimensions and unit weight
  for a Spirit CT900, CT900ENT or CTSBS900 commercial treadmill?
asked_as:
- what size motor is in this treadmill
- how much does the ct900 weigh
- how big is the running deck on the ct900
- what should the belt tension be on my spirit treadmill
keywords:
- specifications
- spec sheet
- motor horsepower
- chp
- wattage
- running surface
- deck size
- assembled dimensions
- unit weight
- belt tension
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct900
  - ct900ent
  - ctsbs900
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ct800-specs-no-specification-table
- spirit-ct850-specs-no-specification-table
- 40t-2026-specs-no-specification-table
see_also:
- spirit-2026t-specs-drive-motor-rating
- spirit-ct900-specs-drive-belt-tension-120-to-130-hz
- ctsbs900-specs-belt-sag-260-to-265-mm
- ctsbs900-specs-no-wiring-diagram-in-the-service-manual
- spirit-ct900-specs-driver-board-is-a-delta-inverter
- ctsbs900-electrical-requirements
- ct900-full-parts-list-and-exploded-view
- ct900ent-specs-no-parts-list
- ctsbs900-exploded-view-and-parts-diagram
- ct900-belt-deck-cleaning
source:
  ref: spirit-treadmill-ct900-owners-manual
  locator: Table of Contents p. 1 and whole document; the same absence holds in the
    CT900ENT owner's manual (Table of Contents p. 2) and the CTSBS900 owner's manual
    (Table of Contents p. 1). Service-manual figures - CT900 service manual p. 67, text.md
    lines 1444-1446; CT900ENT service manual p. 69, lines 1229-1230; CTSBS900 service manual
    p. 20, lines 263-264
  extracted_at: '2026-09-09'
---

**None of the three owner's manuals contains a specification table.** All three
were checked - the CT900 book, the CT900ENT book and the CTSBS900 slat belt sled
book. No table of contents has a Specifications entry, and none of these figures
is printed anywhere in any of them:

- running surface / running deck size, and roller diameters
- assembled dimensions, floor footprint, or shipping carton size
- unit weight or shipping weight
- a speed range or an incline range stated as a machine specification
- a certifications list

Get these from Spirit Fitness or the product spec sheet, and say the owner's
manual does not state them. Do not carry a figure in from a CT800, CT850 or 2026
T-series manual.

## Only one of the three prints a motor rating

**The CTSBS900 prints `Motor: 3.0HP AC`** as a bullet on its Grounding
Instructions page (p. 7), beside the power requirement. That is the only motor
figure in any of the three books, and it is the same figure the 2026 7.0T and
8.0T print in the same bullet position - see
`spirit-2026t-specs-drive-motor-rating`.

**The CT900 and the CT900ENT print no motor rating at all.** No horsepower, no
CHP, no wattage and no motor part number appears in either book, for either the
drive motor or the incline motor. The CT900 parts list names item 10 "AC Motor"
and item 13 "Incline Motor" with no rating beside either, and items 11, 12, 14
and 15 - the front roller, rear roller, running deck and running belt - carry no
dimensions. Never read the CTSBS900's 3.0HP across to a CT900 or a CT900ENT.

## There is no tread-belt tension figure in any of the three

All three give belt tension only as a procedure, never as a force, a deflection
or a number of turns from a datum:

- The **CT900** and the **CT900ENT** use an 8 mm Allen wrench on the rear roller
  bolts at the end of the step rails, **1/4 turn each**, judged by walking on the
  belt (`ct900-belt-tension-adjustment`, `ct900ent-belt-tension-adjustment`).
- The **CTSBS900** instead has you run the belt up to **4.0 mph (6.4 kph)** and
  rotate both sides **1/4 turn** clockwise to tighten
  (`ctsbs900-adjusting-belt-tightness`).

For the drive belt under the motor cover all three owner's manuals say only that
tightening it "should be done by a trained service person". **The service manuals
do print the drive-belt figure, and each machine has a different one**: the CT900
and CT900ENT service manuals set it at **120 to 130 Hz** on a sonic tension meter
(`spirit-ct900-specs-drive-belt-tension-120-to-130-hz`), and the CTSBS900 service
manual sets its slat belt by a **260 to 265 mm vertical gap** measured at the belt
centre (`ctsbs900-specs-belt-sag-260-to-265-mm`). **Do not answer any of these from
`spirit-ct850-drive-belt-tension`** - its 70 to 75 lbs on a gauge is the CT800 /
CT850 / XT figure for a different belt on different machines, and no CT900 or
CTSBS900 book states it.

The CT900 and CT900ENT service manuals also print an incline-motor voltage (220
volts in the CT900 book, 120 in the CT900ENT book) and caption the inverter
VFD015TM12A, but still no drive-motor horsepower; the CTSBS900 service manual is
a parts-replacing guide with no electrical section at all.

## The running-surface figure in the CT900 PDF is not the CT900's

The text layer of `spirit-treadmill-ct900-owners-manual` carries a duplicated
*GENERAL MAINTENANCE* block laid over the manual's own p. 36 column, and that
block prints **`Running surface : 56x224cm`**. It is not CT900 content: the same
string sits in the same overlaid block in the 2026 4.0T, 7.0T and 8.0T manuals,
which are three differently sized machines. **Never quote 56x224cm as the running
surface of any of them.** The overlay is recorded in full at
`ct900-belt-deck-cleaning`.

## Which of the three books you are holding

| Book | Code printed on it | Revision | Exploded view | Parts list |
|---|---|---|---|---|
| CT900 | `CT900_900825_OM_20250612` | 06.12.25 | p. 49 | pp. 50-51, 120 rows |
| CT900ENT | none | 11.19.2021 | **none printed** | **none printed** |
| CTSBS900 | `CTSBS900_900885_OM_20251029` | 10.29.25 | p. 53 | **none printed** |

## What the books do print is not in a spec table and is not a `specs` fact

The user weight limit, the nominal outlet voltage, circuit rating and plug type,
the operating temperature and humidity, and the minimum clearance around the
machine are all printed on the safety and electrical pages - they are `safety`
facts and are carded there. The deck life before the deck is flipped is printed
in the belt/deck section and is a `maintenance` fact. Several of these differ
between the three books, so read each from the book for the machine in hand
rather than from a sister model.
