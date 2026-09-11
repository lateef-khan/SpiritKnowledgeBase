---
id: crw800-2024-errors-rf-handheld-board-problem
title: The RF receiving board row lists four checks and prints no symptom to go with
  them
kind: troubleshooting
question: What are the checks for an RF handheld board problem on a Spirit CRW800
  rower?
asked_as:
- rf board fault on my spirit rower
- heart rate receiver board checks on a crw800
- rower wireless receiver not working
keywords:
- rf handheld board
- receiving board
- interference
- fluorescent lamp
- rectifier
- cable
- radio reception module
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- crw800-2024-errors-light-sensor-problem
- crw800-2024-errors-wireless-heartbeat-has-no-effect
- crw800-2024-errors-heartbeat-value-incorrect
- spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel
- sr500-2016-rf-handheld-board-problem
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, Happening / Caused / Processing
    Step table on printed pages 32 and 33. Both pages are flat pictures with no text
    layer and were read from the rendered page; CRW800 2016 (CW800-YR001) service
    manual 8.5 Troubleshooting Quick Lookup Table, PDF p. 38-39, text.md lines 487-519;
    CRW800 2021 (800940) service manual 7-5 Troubleshooting Quick Lookup Table, PDF
    p. 37 (printed 36), text.md lines 536-561; CRW800 2016 8.9 RF handheld board problem,
    PDF p. 40, text.md lines 552-556; CRW800 2021 7-7-4, PDF p. 39 (printed 38), text.md
    lines 602-608
  extracted_at: '2026-09-10'
---

The condition is printed as `RF handheld board problem`, and **the Caused column beside it is
empty.** The rendered page was checked: the manual really does print a symptom with four processing
steps and no cause.

| Processing Step |
|---|
| 1. Check that the receiving board is in the correct position |
| 2. Near the source of interference (such as fluorescent lamp rectifier, cable interference power, etc.) |
| 3. Check the cable |
| 4. Replace the RF radio reception module |

**Step 2 is a cause printed in the remedy column.** It is telling the reader to look for a nearby
fluorescent lamp ballast or a power cable running close to the board, not to do anything.

**This row is not a symptom a customer would report.** It is a hardware heading, and it is the only
place in the manual that names the *receiving board's position* as something to check - which is
worth knowing when a strap reads intermittently and a new CR2032 has not fixed it
(`crw800-2024-errors-wireless-heartbeat-has-no-effect`).

The row below it has the same shape, for the optical sensor:
`crw800-2024-errors-light-sensor-problem`.

## The two CRW800 service manuals print this row, and the 2021 book gives it a cause and a first step

**The CRW800 2016 (`CW800-YR001`) service manual prints the row exactly as the 2024 owner's manual does** - an empty Caused column and the same four steps.

**The CRW800 2021 (`800940`) service manual fills the Caused column and adds a step:** the cause is `Level UP/DOWN cannot be changed` (printed *canned not changed*), and the processing steps are 1. **Check the battery.** 2. Check that the receiving board is in the correct position. 3. Near the source of interference (such as fluorescent lamp rectifier, cable interference power, etc.). 4. Check the cable, or replace the RF radio reception module.

**That names what the RF board does.** It is the radio link from the handlebar controller's level keys to the console - the "handheld" in the row's name - and the handlebar controller runs on its own battery, which is why the 2021 book checks the battery before the board. A rower whose level keys on the handle do nothing is this row, and the fuller procedure for it is the Q&A page (`spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel`).

**The XRW600 has no RF handheld board and prints no such row** - its handle is wired. Its quick lookup table goes from the reception-too-short row straight to the light sensor. Sole's SR500 2016 prints this row (`sr500-2016-rf-handheld-board-problem`).
