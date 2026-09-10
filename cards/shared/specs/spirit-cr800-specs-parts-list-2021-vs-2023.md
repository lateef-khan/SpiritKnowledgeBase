---
id: spirit-cr800-specs-parts-list-2021-vs-2023
title: Two fasteners dropped and three quantities altered between the two printings
  of one recumbent parts list
kind: spec
question: What is the difference between the parts lists in the two Spirit CR800 commercial
  recumbent bike owner's manuals, cr800-2021 and cr800-2023?
asked_as:
- how many washers does the cr800 take
- is the 2023 cr800 parts list different from the older one
- what is item 109 on the cr800
- which cr800 manual should i order parts from
keywords:
- parts list
- item number
- quantity
- fastener
- hex head bolt
- flat washer
- nut
- revision
- printing
- ordering parts
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2021
  - cr800-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-bike-specs-no-specification-table
source:
  ref: spirit-bike-cr800-2023-owners-manual
  locator: Parts List pp. 41-43, compared item by item against the CR800-2021 owner's
    manual Parts List pp. 41-43; back cover revision stamps Revision 6 11.08.2021 and
    Revision 7 06.21.2023
  extracted_at: '2026-09-09'
---

**One machine, two printings, one parts list with five changes.** Both lists
carry the same header, `CR800-XR880-SB023-01 Part List_SPIRIT`, the same items in
the same order, and the same highest item number, 203. Nothing was added.

## Two items are in the 2021 list and not in the 2023 list

| Item | Description | Qty in 2021 |
|---|---|---|
| **109** | `3/8" × 7T_Nut` | 4 |
| **110** | `3/8" × 2"_Flat Head Socket Bolt` | 2 |

**If a customer with a 2023 book asks for item 109 or 110 they will not find
it.** Both are plain fasteners, and item 89, `3/8" × 7T_Nylon Nut`, is still in
both lists - do not confuse the two. Item 175, `3/8" × 2-3/4"_Hex Head Bolt`, is
also in both.

## Three quantities changed

| Item | Description | 2021 | 2023 |
|---|---|---|---|
| **68** | `5/16" × UNC18 × 5/8"_Hex Head Bolt` | 8 | **6** |
| **77** | `Ø3/8" × Ø19 × 1.5T_Flat Washer` | 12 | **10** |
| **94** | `5/16" × UNC18 × 3/4"_Hex Head Bolt` | 6 | **8** |

The 5/16 UNC18 bolt count moved two units from the 5/8" length to the 3/4"
length, and the 3/8 flat washer count fell by two along with the two dropped
fasteners. **Quote the quantity from the printing the customer has.**

## What did not change, despite what you may have been told

The **TV Adapter (5C2V) at item 194**, the **PU Wheel at item 166** (qty 4) and
the **Round Cap at item 193** are in **both** printings. They were not added in
2023. **This was confirmed twice** - once from the text extract, and again from
both parts-list pages of both PDFs rendered at 300 dpi and read with
`tesseract --psm 4`, where all three items appear in the 2021 list and items 109
and 110 appear only there. Do not re-open this. So are the AC Input Module (195), the 80 mm black connecting wire (198),
the chain cover attaching plate (201) and the curved washer (203).

## How this was measured

The two lists were compared **item by item in Python**, not with `diff`, which
returns false "identical" results in this environment. Raw word-level similarity
over the parts pages reads only **80.8%**, but that is the two-column layout
re-flowing when items 116 and 194 moved columns - **item for item, every entry
in the two lists agrees except the five above.** Do not read the 80.8% as one
part in five being different.

## Which printing is which

The back cover of the 2021 book reads **Revision 6: 11.08.2021, © 2021**; the
2023 book reads **Revision 7: 06.21.2023, © 2023**. Both lines extract cleanly
from the native text layer; **ignore the OCR supplement for these two pages**,
which renders the 2021 stamp as `Revision 6: | 1.08.202]` and the 2023 back cover
as mirrored gibberish. The 2023 book's exploded-view page also carries the
untranslated factory label `XR880-SPIRIT 爆炸圖`.

**Both books' tables of contents mis-name the assembly chapter as "CU800 ASSEMBLY
INSTRUCTIONS"** on a CR800 recumbent manual. That is a printing error in both
printings, not a sign you have the wrong book.
