---
id: csc880-2025-specs-exploded-view-with-no-parts-list
title: Three exploded-view pages of numbered balloons with no parts list, headed by
  an untranslated Chinese factory title block
kind: fact
question: How do I get a part number off the exploded view in the Spirit csc880-2025
  stair climber manual?
asked_as:
- what do the numbers on the csc880 diagram mean
- there is no parts list in my stair climber manual
- how do i order a part for the csc880
- why is there chinese writing in my manual
keywords:
- exploded view
- parts list
- item number
- part number
- diagram
- chinese
- oem
- factory drawing
- cle450s
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: specs
  code: '*'
  model_number: '880665'
authority: 3
not_to_be_confused_with:
- ct900ent-specs-no-parts-list
- spirit-climber-specs-which-manuals-print-a-parts-list
see_also:
- spirit-climber-specs-which-manuals-print-a-parts-list
- spirit-climber-specs-no-specification-table
- spirit-climber-2024-specs-resistance-system
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: EXPLODED VIEW, printed pp. 35-37 (PDF pp. 37-39); Table of Contents printed
    p. 1, which runs Machine Care 31, Troubleshooting 33, Exploded View 35, Warranty
    38; the cover, PDF p. 1. Each exploded-view page was rendered at 300 dpi and read
    with `tesseract --psm 4` as well as extracted
  extracted_at: '2026-09-10'
---

**The CSC880-2025 prints three pages of exploded view and no parts list at all.**
The table of contents goes Machine Care 31, Troubleshooting 33, **Exploded View
35**, Warranty 38, and stops. Printed p. 38 onwards is warranty.

**The balloons carry hierarchical assembly numbers, not item numbers** - `1.8`,
`1.8.2`, `1.8.5`, `2.2.3`, `2.2.6`, `1.7.11`, `1.10.2`, `1.45`. Nothing in the
book says what any of them is. **A number read off these pages cannot be turned
into a part.** Go to Spirit Fitness, describe the part, and say the owner's
manual prints a diagram with no list.

## Every page carries the factory's own title block, untranslated

The bottom right corner of each exploded-view page prints a Chinese drawing title
block that was never localised:

```
机种  CLE450S-3A1楼梯机
设计  夏祥朋
校对
审核
工艺
批准
```

`机种` is *model*, `楼梯机` is *stair machine*, and `设计` is *designed by*. So the
drawing's own model designation is **`CLE450S-3A1`** - the OEM's code for this
stair climber, not a Spirit part number. `校对`, `审核`, `工艺` and `批准` are the
empty proofread, review, process and approval sign-off lines of the factory's
drawing sheet.

**`CLE450S-3A1` also appears on the front cover**, on line 1 of the extracted
text. It is not a model a customer can order against and it is not the machine's
name. **The machine is a CSC880.** If a customer reads `CLE450S-3A1` off their
manual, tell them it is the factory's drawing code left in by mistake.

## The pages are drawings with a real text layer, so nothing is hidden

Each page was rendered at 300 dpi and read with `tesseract --psm 4`. The render
returns fewer words than `pdftotext` does - 2, 31 and 84 against 67, 124 and 167 -
because the pages are line art. **The extraction already has everything the pages
print**; there is no imaged parts table waiting to be recovered. The only English
words on the three pages are `EXPLODED VIEW`.

## Two other manuals in the wave do the same thing

The 8.5S-2025 and 8.5S-FIT-2026 also print an exploded view with no list, and
their drawings carry dates rather than Chinese title blocks. See
`spirit-climber-specs-which-manuals-print-a-parts-list` for the whole picture.
The CSC900 of 2019, 2021 and 2024 prints neither a drawing nor a list.
