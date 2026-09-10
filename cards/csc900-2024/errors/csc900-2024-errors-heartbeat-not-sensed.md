---
id: csc900-2024-errors-heartbeat-not-sensed
title: The grips read no heartbeat, and the hand pulse wire is tested for DC volts at the seat
kind: troubleshooting
question: Why does a Spirit CSC900-2024 stairclimber not read my heart rate from the
  grips?
asked_as:
- no heart rate on my stairclimber
- csc900 hand grips dont read my pulse
- contact heart rate not working on my stair climber
keywords:
- heartbeat
- hand pulse
- handpulse wire
- dc voltage
- multimeter
- harness
- stairclimber
- no pulse
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-hand-pulse-not-working
see_also:
- csc900-2024-errors-error-code-table
- spirit-hand-pulse-not-working
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING - CONTINUED, Problem / Reason / Method table on printed page
    35. That page is a flat picture with no text layer and was read from the rendered
    page at 500 dpi.
  extracted_at: '2026-09-10'
---

**Condition:** After pressing "START" to start, the heartbeat data is not sensed.

| Reason | Method |
|---|---|
| The hand pulse wire problem | The handpulse wire is not good generally for the installation of extrusion broken. You can use a multimeter DC voltage test hand-held heartbeat seat voltage; if there is no voltage it is determined that the harness is not good. |

**One cause and one test.** The manual blames the wire and nothing else - not the grips, not the
board, not the user's hands - and the test is a DC voltage reading at the hand-held heartbeat seat.
**No pass figure is printed**; the only stated outcome is that *no* voltage means a bad harness.

**This is not the answer the rest of the 2024 range gives.** Nine of the other thirteen New Black
manuals print a four-cause row that starts with the user's hands and ends at the hand pulse board
(`spirit-hand-pulse-not-working`). This machine's book prints that row's symptom with one cause and
one measurement instead.

**The machine has a wireless heart rate receiver and the troubleshooting table never mentions it.**
The console chapter says the StairClimber takes both a Bluetooth telemetric strap and contact heart
rate, and that it detects the closest sensor automatically - but the Problem/Reason/Method table
carries no chest strap row, no battery, no range and no receiver. So a caller whose *strap* is not
reading has nothing in this manual to work from, and the row above answers only for the grips. The
comparable rows for the rest of the range are `spirit-wireless-chest-belt-no-pulse` and
`spirit-erratic-pulse-display`; neither was written for this machine and neither should be quoted as
if it were.
