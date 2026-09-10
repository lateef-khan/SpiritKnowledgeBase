---
id: csc900-2019-assembly-handrail-cover-screw-m4-x-25
title: The handrail cover screw is M4 x 25 on the 2019 printing and M4 x 30 on every
  printing after it
kind: fact
question: What size screw holds the handrail covers on a Spirit CSC900 (csc900-2019)
  stairclimber, and why do other manuals say a different length?
asked_as:
- what screw holds the handrail cover on the csc900
- is the stairclimber cover screw m4x25 or m4x30
- my csc900 manual says a different screw size
- which m4 screw for the stair climber handrail cover
keywords:
- handrail cover
- m4x25
- m4x30
- screw length
- cover screw
- step four
- printing difference
- hardware table
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: assembly
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2024-assembly-hardware-kit
- csc900-2024-assembly-step-one-bolt-length-contradiction
see_also:
- csc900-2024-assembly-procedure
- csc900-2024-assembly-hardware-kit
- csc900-2024-assembly-tools-included
source:
  ref: spirit-climber-csc900-2019-owners-manual
  locator: printed p. 12 (PDF p. 14), CSC900 STEP FOUR, its Hardware For Step 4 table,
    its step text item 3 and its drawing call-outs; compared against the same page of
    the 2021 printing (`spirit-climber-csc900-2021-owners-manual`) and printed p. 14
    (PDF p. 16) of the 2024 printing (`spirit-climber-csc900-2024-owners-manual`).
    Both pages read from a 300 dpi render as well as from the text layer
  extracted_at: '2026-09-10'
---

**On a 2019 CSC900, work to M4 x 25.** The 2019 book says 25 in all three places it
prints the figure - the Hardware For Step 4 table (`SCREW, M4 X 25L, 4`), the step text
(*Attach the Handrail Covers on each side using M4\*25L Screws (4pcs)*) and the drawing
call-outs beside it.

**On a 2021 or 2024 CSC900, work to M4 x 30.** Those two printings say 30 in the same
three places. Nothing else in step four changed: the console still takes 4 M8 x 20L
bolts and the handlebars still take 2 ST4.2 x 15L screws.

| Printing | Table | Step text | Drawing |
|---|---|---|---|
| 2019 | M4 X 25L | M4*25L | M4*25 |
| 2021 | M4 X 30L | M4*30L | M4*30 |
| 2024 | M4 X 30L | M4*30L | M4*25 is in the file, see below |

## The 2021 page was patched, and the old number is still in the file

The 2021 PDF's text layer returns **both** figures for the drawing call-out - `M4*25`
and, on top of it, `30`. A 300 dpi render of the printed page shows only **M4*30**. The
25 is a covered label that was never deleted, and `pdftotext` hands it back as if it
were printed.

**The same trick hides an ST4.2 label in both books.** Both the 2019 and the 2021 text
layers return `ST4.2*16Screw` above `ST4.2*15 Screw` for the same call-out, and the
render of either page shows only **ST4.2*15**. The 16 is not on the page.

**In the 2024 re-layout the cover came off.** A 300 dpi render of the 2024 step four
page shows **ST4.2\*16 Screw** printed in plain sight beside a table and a step that both
say ST4.2 x 15L. The stale label the 2019 and 2021 books hid is visible in the 2024 book.

Work to **ST4.2 x 15** on all three. The 16 has never been the manual's own answer, only
the one it forgot to erase.

## Why this matters when you read the extraction rather than the page

Anyone answering from the converted text of a 2019 or 2021 CSC900 will report a
contradiction between the drawing and the table that a person holding the manual cannot
see. Read the render before carding a drawing call-out on these three books.
