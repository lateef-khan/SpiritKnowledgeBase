---
id: spirit-med-bike-specs-parts-which-manuals-print-a-parts-list
title: Which of the medical bike owner's and service manuals print a parts list, which
  print only a drawing, and the one whose list is another machine's
kind: fact
question: Does the owner's manual or the service manual for a Spirit medical bike
  - 4.0R, 4.0U, 7.0R, 7.0U, 8.0U, 8.5R and their Dyaco PT and MED editions - print
  an exploded view and a parts list?
asked_as:
- does the 8.0u manual have a parts list
- which medical bike manuals have parts lists
- where do the item numbers in the 8.5r service manual come from
- spirit medical bike exploded view
keywords:
- parts list
- exploded view
- item number
- service manual
- owner's manual
- medical bike
- dyaco edition
- ghost text
- absence
- ordering parts
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40r-pt
  - 40u-2025
  - 40u-pt
  - 70r-2021
  - 70r-2025
  - 70u-2025
  - 80u-2025
  - 85r-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-residential-bike-specs-which-manuals-print-a-parts-list
see_also:
- spirit-40r-specs-parts-list-items-1-to-191
- spirit-40u-specs-parts-list-items-1-to-150
- 70r-2025-specs-parts-list
- 70r-2021-specs-parts-list
- 70u-2025-specs-parts-list
- 70u-2025-specs-parts-service-manual-list
- 85r-2025-specs-parts-list
- 80u-2025-specs-parts-exploded-view-with-no-matching-list
- 85ue-2025-specs-parts-list
- spirit-bike-specs-which-manuals-print-a-parts-list
- spirit-bike-specs-parts-which-service-manuals-print-a-parts-list
source:
  ref: spirit-bike-85r-2025-owners-manual
  locator: 'Every book below was read at its table of contents and at its exploded-view
    and parts pages, and each parts page was parsed row by row; the 7.0R and 8.0U
    service-manual pages were rendered because their text layers disagree with the
    page. 8.5R owner''s manual: EXPLODED VIEW DIAGRAM PDF pp. 65-66, then WARRANTY
    p. 67. The other books'' pages are on the cards named in the table'
  extracted_at: '2026-09-11'
---

**Every medical bike has a list somewhere, but not always in the book in hand, and one book's list is another machine's.** No book in the range prints a Spirit part number; every list is item number, description and quantity.

| Machine | Owner's manual | Service manual | Card |
|---|---|---|---|
| 4.0R (2025, and the Dyaco PT edition) | drawing + list, pp. 35-38 (PT: pp. 57-63) | drawing + the same list, pp. 51-59 | `spirit-40r-specs-parts-list-items-1-to-191` |
| 4.0U (2025, and the Dyaco PT edition) | drawing + list, pp. 35-37 (PT: pp. 55-59) | drawing + the same list, pp. 49-55 | `spirit-40u-specs-parts-list-items-1-to-150` |
| 7.0R 2025 | drawing + list, pp. 49-52 | drawing + the same list **printed**, pp. 38-44 - but the PDF's text layer under it is the 2021 list | `70r-2025-specs-parts-list` |
| 7.0R 2021 (Dyaco MED edition) | drawing + list, pp. 75-81 | - | `70r-2021-specs-parts-list` |
| 7.0U 2025 | drawing + list, pp. 47-49 | the same drawing + a **differently worded** list, pp. 37-41 | `70u-2025-specs-parts-list`, `70u-2025-specs-parts-service-manual-list` |
| 8.0U 2025 | **drawing only**, p. 58 | the same drawing + **the 8.5R's list**, pp. 43-50 | `80u-2025-specs-parts-exploded-view-with-no-matching-list` |
| 8.5R 2025 | **two drawings only**, pp. 63-64 | one drawing + the list for both, pp. 38-44 | `85r-2025-specs-parts-list` |

The 8.5UE upper body ergometer follows the 8.5R pattern - two drawings in the owner's manual, the list in the service manual (`85ue-2025-specs-parts-list`) - and is filed as its own product line.

## Three things to know before quoting a number

- **The three generations of the two smaller bikes share one list.** The Dyaco PT 4.0 R and 4.0 U user manuals, undated but exported in 2016, print exactly the lists the 2025 Spirit books print, under drawings with the same 2019 stamps.
- **The 7.0R service manual is two lists in one file.** Its printed pages are the 2025 list; `pdftotext` returns the 2021 MED list from the same pages. Anything that reads the PDF's text rather than the page will name the wrong part.
- **The 8.0U has no list of its own anywhere.** The list in its service manual decodes the 8.5R's drawings, not the 8.0U's; a number read off the 8.0U drawing cannot be resolved from either book.

The commercial and residential bike ranges are counted on their own cards (`spirit-bike-specs-which-manuals-print-a-parts-list`, `spirit-residential-bike-specs-which-manuals-print-a-parts-list`), and the twenty-four earlier bike service manuals on `spirit-bike-specs-parts-which-service-manuals-print-a-parts-list`.

