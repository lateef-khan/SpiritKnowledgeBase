---
id: spirit-bike-specs-no-specification-table
title: No specification table in sixteen commercial bike owner's manuals, and the
  figures printed instead
kind: fact
question: Where are the dimensions, machine weight, shipping weight and flywheel weight
  for a Spirit commercial upright or recumbent bike?
asked_as:
- how much does the spirit commercial bike weigh
- how big is the cr900 recumbent
- what is the shipping weight of the upright bike
- how heavy is the flywheel on this bike
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
- pedal spacing
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cr800-2023
  - cr800-2024
  - cr800ent-2023
  - cr800ent-2024
  - cr900-2018
  - cr900-2025
  - cr900ent-2021
  - cu800-2012
  - cu800-2021
  - cu800-2024
  - cu800ent-2022
  - cu800ent-2024
  - cu900-2018
  - cu900-2025
  - cu900ent
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cycle-specs-no-specification-table
- spirit-residential-bike-specs-no-specification-table
- spirit-ce-specs-no-specification-table
- spirit-xe-specs-no-specification-table
- spirit-ct800-specs-no-specification-table
see_also:
- spirit-bike-specs-console-display-type
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-ce-specs-forty-resistance-levels
- cu800-2012-specs-q-factor-and-pedal-tilt
- cr800-2024-specs-parts-list
- cu800-2024-specs-parts-list
source:
  ref: spirit-bike-cr900-2025-owners-manual
  locator: 'Table of Contents p. 1 and whole document; the same absence was checked
    in all sixteen manuals - CR800-2021, CR800-2023, CR800-2024, CR800ENT-2023, CR800ENT-2024,
    CR900-2018, CR900ENT-2021, CU800-2012, CU800-2021, CU800-2024, CU800ENT-2022, CU800ENT-2024,
    CU900-2018, CU900-2025 and CU900ENT-2021, each at its own Table of Contents and throughout'
  extracted_at: '2026-09-09'
---

**None of the sixteen Spirit commercial upright and recumbent bike owner's
manuals contains a specification table.** All sixteen were checked. No table of
contents has a Specifications entry, the word *dimension* appears in none of
them, and none of these figures is printed anywhere in any of them:

- **assembled dimensions** - no length, width or height, in any unit
- **machine weight**, shipping weight, gross weight or carton size
- **flywheel weight or diameter**, and no gear ratio. The word *flywheel* appears
  in only one of the sixteen, as a callout label on the CR800ENT-2023
  parts-of-your-bike drawing, with no figure attached
- a **floor footprint** or a required operating area
- a **resistance range in watts, newtons or kilograms**. Resistance is given only
  as a count of console levels
- a **Q factor** or pedal-spacing measurement. One manual discusses Q factor at
  length and still prints no number - see
  `cu800-2012-specs-q-factor-and-pedal-tilt`

Get these figures from Spirit Fitness or the product spec sheet, and say the
owner's manual does not state them. **Do not carry a figure across from one
generation to another, and never in from a Sole bike.**

## The only weight figures any of the sixteen print

There are exactly two, and neither is a machine weight:

- the **450 lb user weight limit** (a safety figure), and
- **300 in-lbs / 34 N·m**, the pedal tightening torque printed in the six
  900-series books - CR900-2018, CR900-2025, CR900ENT-2021, CU900-2018,
  CU900-2025 and CU900ENT-2021 (an assembly figure).

A search for `lbs`, `pounds`, `lb` or `kg` in any of the sixteen returns only
those two plus the `kg-m/min` unit used in the fitness-test tables. **If someone
quotes you a machine weight in pounds for one of these bikes, it did not come
from the owner's manual.**

## What the sixteen books do print, and where each fact lives

| Figure | What is printed | Section |
|---|---|---|
| Resistance levels | **40** on twelve of the sixteen; **not stated at all** in the CR800ENT-2023, CR800ENT-2024, CU800ENT-2022 and CU800ENT-2024 books | specs |
| Console display | blue LED, white LED, or a 10.1 in touchscreen, depending on the machine - see `spirit-bike-specs-console-display-type` | specs |
| Brake and resistance unit | named only where there is a parts list - a generator brake on seven, an induction brake with an EMS controller on four, and **no brake part named at all** in the other five - see `spirit-bike-specs-generator-brake-or-induction-brake` | specs |
| Exploded view and parts list | in **eleven** of the sixteen; **none** in CR900-2018, CR900ENT-2021, CU800-2012, CU900-2018 or CU900ENT-2021 - see `spirit-bike-specs-which-manuals-print-a-parts-list` | specs |
| Pedal Q factor and tilt | **CU800-2012 only**, and with no measurement | specs |
| User weight limit | **450 lb** in fifteen of the sixteen; the CU800-2012 safety page prints **none** | safety |
| Operating temperature / humidity | 40 to 120 °F, 95% non-condensing, in fourteen; the **CU800ENT-2024 and the CR800ENT-2024 print "40 degrees C" instead** | safety |
| Power source | built-in generator on the **ten** LED-console machines; **all six touchscreen machines plug into a wall outlet** - and the CR800ENT-2024, like the CU800ENT-2024, asks for **120-volt AC, 15-amp** where the 2022-2023 ENT books asked for 110-volt, 5-amp | safety |

## This absence was proved from rendered pages, not from the text extract

A missing specification table is exactly the claim a flat-image page fakes, so
this was checked against the PDFs themselves rather than the text extract.

**Five of the older thirteen manuals were rendered in full at 300 dpi and read with
`tesseract --psm 4` - 232 pages** - and every page's OCR word count was compared
against its `pdftotext` word count to find partly-imaged pages:

- **CR900-2025 and CU900-2025**, all 44 pages each, because they use a new layout
  and were the likeliest to have gained a spec page.
- **CU800ENT-2024** (60 pages), the longest and newest book in the range.
- **CR800ENT-2023** (52 pages), the book with the most imaged pages.
- **CU800-2012** (32 pages), which is an image-only scan with **zero** extractable
  text on 26 of its pages, so its whole content is OCR.

Across all 232 rendered pages the words *specification*, *dimension*, *shipping*
and *carton* occur **only** in warranty boilerplate ("Product features or
specifications ... subject to change"), in the operating-temperature safety line,
and in "remove all parts from the carton". A search for dimension-shaped and
weight-shaped figures - `NN lbs`, `NN kg`, `NN" x NN" x NN"` - returns **only**
fastener sizes from the parts lists, the 450 lb user weight limit, an FCC 20 cm
separation distance, and a 155 lb example body weight in a fitness-test chart.

**There is no specification table. Do not re-run this check.**

**The three 2024 bikes were checked the same way and add nothing to this page.**
The CR800-2024, CR800ENT-2024 and CU800-2024 books are the New Black Units
reissue, warranted September and October 2024; measured on native PDF text only
about 43% of the CR800ENT-2023, 48% of the CU800-2021 and 56% of the CR800-2023
text survives into them. Every page of all three had already been rendered at
300 dpi and read with `tesseract --psm 4`, and the combined native-plus-OCR text
contains no specification table, no dimension, no machine weight and no flywheel
figure. **The word *flywheel* does not appear in any of the three at all**, not
even as a drawing callout.

Two partly-imaged pages *were* found, and neither carries specification data:
the **product-label stickers on page 5** of both 2025 books print their full
English and French warning text as a picture, and the **console program-button
labels** are drawn into the console image. Those belong to `safety` and `console`.

## The recumbent and the upright are not interchangeable here

Whole-document, a CR manual and its CU twin run 77% to 90% word-for-word alike,
and the narrative specification facts on this page really are shared - the
resistance-level paragraph, the absence of a specification table and the display
description are word for word the same in a pair.

**Their parts lists are not.** Measured at word level over the parts-list pages
alone, CR800-2021 against CU800-2021 is **10.5%** alike, CR800ENT-2023 against
CU800ENT-2022 is **18.4%**, and CR900-2025 against CU900-2025 is **18.7%**. A
recumbent carries a seat carriage, an aluminium seat track, seat track wheels and
a seat back frame that an upright has no equivalent of. **Never answer a parts
question for one from the other's list.**
