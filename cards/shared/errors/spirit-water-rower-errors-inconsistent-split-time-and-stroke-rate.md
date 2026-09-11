---
id: spirit-water-rower-errors-inconsistent-split-time-and-stroke-rate
title: The 500 metre split time and the stroke rate read inconsistently, and the first
  check is the sensor gap with the console back cover as a gap tool
kind: troubleshooting
question: Why do the 500 metre split time and the strokes per minute read inconsistently
  on a Spirit water rower?
asked_as:
- my rower split time keeps jumping around
- strokes per minute reading is wrong on my spirit rower
- rowing machine numbers are all over the place
- spm and split time not steady
keywords:
- inconsistent readings
- 500 metre split
- split time
- spm
- strokes per minute
- sensor gap
- gap tool
- magnetic ring
- wiring harness
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800h2o
  - crw900-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- crw800h2o-console-shows-no-data
see_also:
- crw800h2o-console-shows-no-data
- crw800h2o-console-shows-no-display
- spirit-water-rower-errors-tank-water-turns-cloudy
- spirit-rower-errors-no-error-codes-printed
- crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets
source:
  ref: spirit-rower-crw900-2021-owners-manual
  locator: 'TROUBLESHOOTING table, the "Inconsistent readings" row: CRW900 2021 owner''s
    manual printed page 53 (PDF page 53); CRW800H2O 2021 owner''s manual printed page
    34 (PDF page 34). Both pages were read from a 300 dpi render as well as the text
    layer, and the two agree; CRW900 service manual 1.1 Speed Sensor Troubleshooting,
    PDF p. 4-5, text.md lines 31-49'
  extracted_at: '2026-09-10'
---

Both water rower manuals print this row in the same words. The issue is printed as
`Inconsistent readings on the console for 500meter split time and SPM (strokes per minute)`.

| Possible Cause | Instructions |
|---|---|
| Sensor gap issue | Use the back cover of the computer as a "gap tool" to check the gap between sensor head and magnetic ring, or see if the sensor head has moved out of position. |
| Faulty sensor | |
| Sensor has moved out of position | |
| Wiring harness issue | Please contact your nearest SPIRIT customer service center for details. |

**The console's own back cover is the gap gauge.** That is the whole tool: take the back cover off
the computer and use it to set the clearance between the sensor head and the magnetic ring. The
manual prints **no gap figure in millimetres or inches** for either machine, so the cover is the
only measurement there is.

Four causes, two answers. The gap and the sensor position are things a technician can check; a
faulty sensor or a wiring harness fault sends you to Spirit customer service, and the manual gives
no test to tell them apart.

**This is a reading that is present but wrong.** A console that is lit and shows nothing at all is
a different row of the same table, and the sensor gap appears there too as `Sensor gap too wide` -
see `crw800h2o-console-shows-no-data`.

**The CRW900 service manual does print a gap figure: 2-3 mm between the sensor and the magnetic ring**, with two further checks the owner's manual lacks - all six magnets present and flush, and the sensor head not receded into its housing (`crw900-2021-errors-speed-sensor-gap-2-to-3-mm-and-six-magnets`). The back-cover gauge remains the owner's-manual method; the millimetre figure is the service manual's, and it is printed for the CRW900 only. The CRW800H2O service manual has no speed sensor page and no figure.
