---
id: ct850-2016-stops-or-shuts-off-by-itself
title: The treadmill stops or shuts off by itself
kind: troubleshooting
question: Why does a Spirit CT800, CT800ENT, CT850, CT850ENT, CT900ENT, 4.0T or XT185
  or XT285 2015 treadmill stop or shut off by itself?
asked_as:
- spirit treadmill keeps shutting off on its own
- treadmill cuts out mid workout
- machine powers down by itself
keywords:
- shuts off
- stops by itself
- house breaker
- treadmill breaker
- controller fuse
- shut down led
- cuts out
- power loss
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 40t-2026
  - ct800-2016
  - ct800-2020
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2016
  - ct850-2020
  - ct850ent-2022
  - ct850ent-2024
  - ct900ent
  - xt185-2015
  - xt285-2015
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-stops-immediately-after-start
- spirit-xt-errors-stops-or-shuts-off-by-itself-belt-deck-lubrication
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Section 8.3 Troubleshooting procedure matrix, pages 49-52 of the CT850
    2016 manual (printed 48-51); the same row is section 8-7, pages 47-51 of the CT850
    2020 manual (printed 46-50); XT185 2015 service manual Troubleshooting procedure
    matrix, PDF p. 60-62 (printed 55-57), text.md lines 1119-1221; XT285 2015 service
    manual Troubleshooting procedure matrix, PDF p. 61-63 (printed 55-57), text.md
    lines 1189-1291; CT800 2016 service manual 8.4 Troubleshooting procedure matrix,
    PDF p. 56-59 (printed 55-58), text.md lines 1076-1215; CT800 2020 service manual
    8-6 Troubleshooting procedure matrix, PDF p. 46-50 (printed 45-49), text.md lines
    660-797; CT800ENT 2022 service manual 8-6 Troubleshooting procedure matrix, PDF
    p. 36-38, text.md lines 685-791; CT850ENT 2022 service manual 8-6 Troubleshooting
    procedure matrix, PDF p. 37-39, text.md lines 704-810; CT900ENT service manual
    Troubleshooting procedure matrix, PDF p. 45-48, text.md lines 691-842; 4.0T 2026
    service manual Condition / Reason / Solve matrix, PDF p. 36-38 (printed 47-49),
    text.md lines 566-689; the 4.0T ST8700A-ST026-01 service manual (spirit-treadmill-40t-2026-service-manual-st8700a,
    88% the ST017 book) prints the same page one page later, word for word (compared
    with difflib on 2026-09-11): Condition / Reason / Solve matrix at PDF p. 37-39
    (printed 47-49), text.md lines 635-758'
  extracted_at: '2026-09-08'
---

Four causes, in the order the manual lists them. The 2016 and 2020 manuals print this row identically.

| Reason | Solve |
|---|---|
| House breaker tripped | Reset it |
| Treadmill breaker tripped | Reset treadmill breaker |
| Treadmill controller fuse is broken | Replace with new fuse |
| Treadmill controller shut down and LED would be ON | Turn off the AC switch and turn on power again |

A stop that happens immediately after START is pressed is a different row: see
`ct850-2016-stops-immediately-after-start`.

**The CT800ENT 2024 and CT850ENT 2024 owner's manuals print this row word for word** in the
Condition/Reason/Solve matrix on printed pages 57 to 59. Both of those pages are flat pictures
with no text layer and were read from the rendered page.

One word changed with the console: the fourth reason reads
`Treadmill controller shut down and **TFT** would be ON` in both 2024 ENT books, where the 2016 and
2020 manuals say **LED**. Same condition, named for the screen the 2024 machine actually has.

**Eight more service manuals print the four-cause row**: the CT800 2016, CT800 2020 and 4.0T word for word; the CT800ENT 2022, CT850ENT 2022 and CT900ENT with `TFT` for `LED`; and the 2015 XT185 and XT285, which shorten the fourth cause to `Treadmill controller shut down` and say `Turn off the AC switch`. The 2023 XT books, the 2015 XT385 and XT485 and the CT1000ENT print a three-cause version with a lubrication step (`spirit-xt-errors-stops-or-shuts-off-by-itself-belt-deck-lubrication`).
