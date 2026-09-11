---
id: csc900-2024-errors-speed-abnormal-then-data-resets
title: The light sensor is why the speed window reads wrong or blank and the machine
  gives up after three seconds
kind: troubleshooting
question: Why does a Spirit stair climber show a wrong or missing speed and then reset
  the display three seconds later?
asked_as:
- my stairclimber speed reading is wrong
- csc900 display resets a few seconds after i stop
- speed jumps around on my spirit stair climber
- csc880 stops three seconds after i press start
keywords:
- light sensor
- speed abnormal
- data reset
- grating
- sensor distance
- optical sensor
- stairclimber
- no code
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - csc880-2025
  - csc900-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- ces880-2025-errors-rpm-shows-zero
see_also:
- csc900-2024-errors-error-code-table
- csc880-2025-errors-error-code-table
- ces880-2025-errors-rpm-shows-zero
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: 'CSC900 2024: TROUBLESHOOTING, Problem / Reason / Method table on printed
    page 34; that page is a flat picture with no text layer and was read from the
    rendered page at 500 dpi. Extended 2026-09-10 with the CSC880 2025 owner''s manual,
    spirit-climber-csc880-2025-owners-manual, TROUBLESHOOTING - CONTINUED row 6 on
    printed page 34 (PDF page 36), read from the native text layer and confirmed against
    a 400 dpi render; CSC900 2022 (Magnetic system) service manual, 6. Troubleshooting,
    Item / Problem / Reason / Method table row 1, PDF p. 10 - the page is a flat picture
    (text.md lines 261-266 hold only the heading; OCR supplement lines 464-536) and
    was read from a 200 dpi render; CSC880 service manual (Magnetic), 5. Troubleshooting,
    "CSC880 electrical malfunction Troubleshooting" table row 6, PDF p. 8 - the page
    is a flat picture (text.md lines 123-128 hold only the heading; OCR supplement
    lines 428-505) and was read from a 200 dpi render'
  extracted_at: '2026-09-10'
---

**Condition:** Press "START" to start, the machine speed is abnormal, 3 seconds after the stop,
display data reset.

| Reason | Method |
|---|---|
| Light sensor failure | 1. Check whether the light sensor line is off or damaged. 2. Check whether the distance between the light sensor and the grating can be sensed. 3. Replace the light sensor. |

**This machine reads its speed optically**, from a light sensor and a slotted grating, rather than
from a magnet and a reed or hall sensor as Spirit's treadmills and bikes do. The second check is a
**gap** check - whether the sensor can see the grating at its present distance - and the manual
gives no figure for it.

**No code is printed for this fault.** It is a symptom row, and the console shows nothing but the
wrong number.

The five codes this machine does print are on `csc900-2024-errors-error-code-table`.

## The CSC880 2025 stair climber prints the same cause with a blunter symptom

Its row reads:

> After pressing "START" to start, there is no data in the speed window, and the machine stops after
> 3 seconds.

Same cause - light sensor malfunction - and the same three checks, with one addition:

> 3. Replace the light sensor (this phenomenon may also occur when no one is standing on the back
>    step and the step cannot rotate).

**That parenthesis is the check to make first, and it costs nothing.** A stair climber with nobody on
the back step cannot turn, so the sensor sees nothing and the machine stops - which looks exactly
like a failed sensor. Put someone on the machine before condemning the part.

The CSC880 book calls the slotted part a **light grid**; the CSC900 book calls it a **grating**. It
is one part.

**The CSC900 2022 service manual (the magnetic-system book) prints this row word for word**, as row 1 of the ten-row Troubleshooting table on its page 10. The owner's manual and the service manual print the same table; the service manual adds nothing to this row.

**The CSC880 service manual prints this row word for word**, as row 6 of the eleven-row table on its page 8. Owner's manual and service manual carry the same table; the service manual adds nothing to this row (this is the CSC880 half of the card).
