---
id: crw800-2024-errors-rf-handheld-board-problem
title: The RF receiving board row lists four checks and prints no symptom to go with them
kind: troubleshooting
question: What are the checks for an RF handheld board problem on a Spirit CRW800-2024
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
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: errors
  code: no-code
  model_number: '800925'
authority: 3
not_to_be_confused_with: []
see_also:
- crw800-2024-errors-light-sensor-problem
- crw800-2024-errors-wireless-heartbeat-has-no-effect
- crw800-2024-errors-heartbeat-value-incorrect
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, Happening / Caused /
    Processing Step table on printed pages 32 and 33. Both pages are flat pictures with
    no text layer and were read from the rendered page.
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
