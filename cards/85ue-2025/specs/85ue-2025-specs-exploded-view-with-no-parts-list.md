---
id: 85ue-2025-specs-exploded-view-with-no-parts-list
title: Two exploded-view drawings with balloon numbers and no list anywhere to decode
  them
kind: fact
question: Does the Spirit 8.5UE upper body ergometer (85ue-2025) owner's manual have
  an exploded view and a parts list?
asked_as:
- where is the parts list for the 8.5ue
- i need a part number for my upper body ergometer
- what is part 093 on the 8.5ue diagram
- does the arm ergometer manual have a parts diagram
keywords:
- exploded view
- parts list
- parts diagram
- item number
- balloon number
- part number
- spare parts
- ordering parts
- absence
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number: '785045'
authority: 3
not_to_be_confused_with:
- csc880-2025-specs-exploded-view-with-no-parts-list
- spirit-climber-specs-which-manuals-print-a-parts-list
- spirit-rower-specs-which-manuals-print-a-parts-list
see_also:
- 85ue-2025-assembly-parts-diagram-labels
- 85ue-2025-assembly-hardware-by-step
- 85ue-2025-specs-specification-page
source:
  ref: spirit-ergometer-85ue-2025-owners-manual
  locator: EXPLODED VIEW DIAGRAM, printed pp. 57-58 (PDF pp. 59-60), both pages rendered
    at 300 dpi and read with `tesseract --psm 4` because both are flat images; Table
    of Contents printed p. 1 (PDF p. 3)
  extracted_at: '2026-09-10'
---

**Two drawing pages, no list.** The table of contents promises `Exploded View 57`
and delivers two pages of drawing with three-digit balloon numbers on them -
`032`, `041`, `074`, `075`, `092`, `093`, `094`, `124`, `135`, `200`, `1035` on
the first, `539`, `540`, `559`, `569`, `573`, `611`, `612`, `613` on the second.
**Nothing in the book says what any of those numbers is.** The next page is the
warranty.

**A number read off one of these drawings cannot be turned into a part.** Go to
Spirit Fitness with the balloon number and the machine's serial, and tell the
customer the manual prints a diagram but no list.

## Both pages are flat images

`pdftotext` returns nothing from either. The balloon numbers above were recovered
from a 300 dpi render read with `tesseract --psm 4`, and the recovery is partial -
a drawing balloon is a few characters inside a picture and OCR misses some of
them. **Treat the list of numbers above as a sample, not as the full set.**

Every hardware table in this manual is the same kind of flat image; the assembly
chapter's fastener tables were recovered the same way -
`85ue-2025-assembly-hardware-by-step`.

## The drawings carry their own dates, which are not the manual's

The first page is stamped **`MZ2000` and `2025/12/15`** in its corner; the second
is stamped **`2025/06/11`**. Those are drawing revision dates. `2025/12/15` is
also the manual's own date - the cover reads `8.5UE_785045_OM_20251215` and the
warranty is effective December 15, 2025 - but **`2025/06/11` is six months older
and is the same date printed on one of the 8.5S-2025 stepper's drawings**, so at
least one sheet is shared with the stepper platform rather than drawn for this
machine.

## Where part names do come from

The **`PARTS OF YOUR UPPER BODY ERGOMETER`** page, printed p. 12, labels the
machine A to U in words rather than numbers - console, articulating arm,
adjustable crank arm, arm support, seat adjustments, wheelchair anchor, foot rest
plate, moving wheels, levelling glides, power socket, UART and USB ports. That is
the readable naming of this machine's parts and it is
`85ue-2025-assembly-parts-diagram-labels`. The **assembly steps** also name a few
parts by number in passing - the seat back is **(537)** and the foot rest plate
**(095)** - and those numbers are in the same series as the drawings' balloons.

## Three other Spirit machines print a drawing with no list

The **8.5S-2025**, the **8.5S-FIT-2026** and the **CSC880-2025** do the same thing
- see `spirit-climber-specs-which-manuals-print-a-parts-list`. Among the rowers,
three of six print a usable list and three print nothing at all -
`spirit-rower-specs-which-manuals-print-a-parts-list`.
