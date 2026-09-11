---
id: xterra-treadmill-specs-no-specification-table-in-nineteen-owners-manuals
title: No owner's manual prints a specification table; running surface, motor rating,
  size and weight are not stated anywhere
kind: fact
question: Does the Xterra treadmill owner's manual print a specification table with
  the running surface, motor horsepower, dimensions or product weight?
asked_as:
- xterra treadmill specs
- how big is the running belt on my xterra
- what horsepower is the xterra motor
- xterra treadmill dimensions and weight
keywords:
- specifications
- spec table
- running surface
- belt size
- motor horsepower
- dimensions
- product weight
- folded size
- absence
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr200-2021
  - tr260-2023
  - tr300-2021
  - tr64-2024
  - tr65-2023
  - tr66-2021
  - tr75-2024
  - tr75h-2025
  - tr85-2024
  - tr95h-2024
  - trx1000-2021
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  - ws200-2023
  - ws300-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-ct800-specs-no-specification-table
- xt-2023-specs-no-specification-table
- xterra-tr-specs-speed-and-incline-range-running-and-climbing-modes
- xterra-ws-specs-speed-range-0-6-to-8-0-mph
source:
  ref: xterra-treadmill-tr150-2021-owners-manual
  locator: Every page of all nineteen owner's manuals, native text and the 300 dpi
    render sweep. Only the words 'temperature specification' (electrical page) and
    'features or specifications ... subject to change' (warranty page) occur, e.g.
    TR150 PDF p. 6 lines 164-209 and p. 22 lines 677-749; the same two lines sit in
    every other book. Loose greps for HP, horse power, running surface/area, belt
    size, dimension, weight, N.W/G.W and an inch-by-inch pattern returned nothing
    but those lines, the belt-tension sentence and 'GFCI'
  extracted_at: '2026-09-11'
---

**None of the nineteen Xterra treadmill owner's manuals in this wave prints a specification table.** No book states
the running-surface size, the drive-motor horsepower or wattage, the assembled or folded dimensions, the product
weight, or a power rating beyond the outlet it must be plugged into. The word *specification* occurs twice per book
and both times in prose: the electrical page's "temperature specification is 40 degrees C, and humidity is 95%,
non-condensing", and the warranty page's "Product features or specifications as described or illustrated are subject
to change without notice".

What each family prints instead, and where the figure lives in this knowledge base:

| Figure a spec table would carry | What the books print | Card |
|---|---|---|
| User weight limit | On the safety page, as a rule, where printed (a 'Weight Limit' line reads 250, 265, 300 or 350 lb by book; six of the 2021 and 2024 batch books print no such line) | the safety section's user-weight cards |
| Operating temperature and humidity | 40 degrees C, 95% non-condensing, on the electrical page | the safety section's electrical-page cards |
| Outlet | "a 120-volt, 15-amp grounded outlet" (the TRX4500 and TRX5500 books say "nominal 110-volt circuit") | the safety section's outlet cards |
| Speed and incline range | Only the TR75H, TR95H, WS200 and WS300 books state one, on their console pages | `xterra-tr-specs-speed-and-incline-range-running-and-climbing-modes`, `xterra-ws-specs-speed-range-0-6-to-8-0-mph`, `ws300-2023-specs-incline-range-0-to-10-percent` |
| Motor voltage | Only the Dyaco service manuals, as a 0-90 or 0-180 V DC range | the electrical-configuration cards |

The service manuals do not fill the gap either: their chapter 1 *Outlines* pages are drawings or photographs with
part-name callouts and **no dimensions**, and no service manual prints a motor rating.

This was checked twice: a loose-word grep of `text.md` including every OCR supplement, and a fresh `pdftotext` of
each PDF, after a render sweep that OCR'd every page. The Spirit CT800 and 2023 XT books lack a spec table in the same
way (`spirit-ct800-specs-no-specification-table`, `xt-2023-specs-no-specification-table`).
