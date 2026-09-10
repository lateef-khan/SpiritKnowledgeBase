---
id: spirit-cycle-specs-which-manuals-print-a-parts-list
title: Three of the eight indoor cycle and air bike manuals print an exploded view
  and parts list, and five print none
kind: fact
question: Does the owner's manual for a Spirit indoor cycle or air bike have an exploded
  view and a parts list?
asked_as:
- where is the parts diagram for my spirit indoor cycle
- is there an exploded view in the air bike manual
- what is item 104 on the spirit fitness bike
- i need a part number for the spin bike
keywords:
- parts list
- exploded view
- exploded drawing
- item number
- part number
- diagram
- spare parts
- ordering parts
- assembly drawing
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
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-ct800-specs-no-parts-list
- spirit-2026t-specs-no-parts-list
see_also:
- spirit-cycle-specs-no-specification-table
- spirit-cycle-specs-resistance-systems
- spirit-cic850-specs-dt3268f-console-part-number
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: 'CIC850-2022 Table of Contents printed p. 3 (39 EXPLODED DRAWING, 40 PARTS
    LIST) and printed pp. 39-42; CIC800-2021 printed pp. 23-26; AB950-2024 printed
    pp. 31-33 (PDF pages 33-35); each of the other five manuals was checked at its
    own Table of Contents and through to its back cover'
  extracted_at: '2026-09-09'
---

**Three of the eight print both an exploded view and a numbered parts list. Five
print neither.**

| Manual | Exploded view | Parts list | Item numbers run |
|---|---|---|---|
| CIC800-2021 | printed p. 23 | printed pp. 24-26 | 1 to 113 |
| CIC850-2022 | printed p. 39 | printed pp. 40-42 | 1 to 137 |
| AB950-2024 | printed p. 31 | printed pp. 32-33 | 1 to 160, with gaps |
| **CB900-2013** | **none** | **none** | - |
| **XIC600-2018** | **none** | **none** | - |
| **XIC600-2021** | **none** | **none** | - |
| **AB900-2018** | **none** | **none** | - |
| **JB950-2022** | **none** | **none** | - |

For the five with none, the book runs out at the warranty, the manufacturer
address page and NOTES pages. **The only part numbers those five give are the
step-by-step hardware callouts inside the assembly chapter**, which cover
fasteners and tools and nothing else. The AB900-2018 and the JB950-2022 both end
that way despite being 52 and 76 pages long.

## Do not settle this from the table of contents

**The CIC800-2021 prints a parts list that its own table of contents does not
list.** Its contents end at `20 MANUFACTURER'S LIMITED WARRANTY`, and the
exploded drawing and three parts pages follow anyway. The CIC850-2022 and the
AB950-2024 do list theirs. Read to the back cover before answering that a manual
has no parts list.

## The CIC800 description column is a picture, and pdftotext drops it

On the CIC800-2021 the parts list is printed as three tables of No. /
DESCRIPTION / QTY. **On printed pages 24 and 26 the DESCRIPTION column is a flat
image.** A text extract of those pages returns the item numbers and quantities
with no descriptions at all - an item list that looks complete and names nothing.
Printed page 25 extracts normally.

Both pages were recovered here by rendering at 300 dpi and reading with
`tesseract --psm 4`. **A word count would not have caught printed page 26**: it
extracts 112 native words against 179 rendered, well inside any plausible
threshold. Cross-check any part description you quote for a CIC800 against the
rendered page.

## The AB950 drawing carries a factory code, and it is not a part number

The bottom-left border of the AB950-2024 exploded view prints

```
AU900-GA001-02
20230412
```

**That is a drawing code and a drawing date, not a model number and not a part
number to quote to a customer.** The date is over a year older than the manual it
sits in. Both are drawn into the image and do not extract; they were read from a
300 dpi render. The AB950 cover also prints its own document code,
`AB950_950744_OM_20240419`. **No other manual in this group prints a part number
or a document code on its cover** - a code that appears only in a file name on
somebody's disk is not evidence of anything.

## The CIC850 belt-tension procedure cites numbers its own parts list does not match

The CIC850-2022 BELT TENSION ADJUSTMENT steps on printed p. 21 name a *Guard
(Top) Cover (No. 47)*, a *Guard (top) (No. 46)*, *Screws (No. 50 and 51)*, a
*Right guard (No. 44)*, *Hex Screws (No. 55)* and a *Screw (No. 17)*. In the same
book's parts list, item 47 is a Permanent magnet, 46 a flat cross head screw, 50
the Left crank, 51 the Bottom bracket set, 44 the Flywheel AXIS, 55 a Bearing
block and 17 a sweat guard. **The two numbering schemes disagree.** This is what
the source prints; it has not been reconciled here. Do not order a CIC850 part by
a number taken from that procedure - take it from the parts list, and describe
the part by name.

## Do not read one bike's list for another

These are six unrelated machine types. The CIC800 and CIC850 are the closest pair
in the group and still differ: the CIC850 list adds a console, a console bracket,
a tablet holder and left and right dumbbell holders that the CIC800 has none of,
and their drive belts are different lengths - **5PK 1515L on the CIC800 and 5PK
1360L on the CIC850**. The AB950's list shares nothing with either. **Quote an
item number only from the book for the machine in front of you.**

Both CIC lists carry a stray `/112` and `/136` row with no description and no
quantity; neither is an item.
