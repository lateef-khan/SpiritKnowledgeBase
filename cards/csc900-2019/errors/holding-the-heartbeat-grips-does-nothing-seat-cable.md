---
id: csc900-2019-errors-holding-the-heartbeat-grips-does-nothing-seat-cable
title: Holding the heartbeat grips does nothing, and the heartbeat seat cable is checked
  and replaced
kind: troubleshooting
question: Why does a Spirit csc900-2019 stair climber not read a heart rate from the
  handrail grips?
asked_as:
- climbmill hand pulse not working
- csc900 heart rate grips read nothing
- no pulse from the handrails on my stair climber
keywords:
- heartbeat
- hand pulse
- heartbeat seat cable
- grips
- no pulse
- climbmill
- stair climber
- poor contact
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: no-pulse
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- spirit-hand-pulse-not-working
see_also:
- csc900-2019-errors-error-code-table
- csc900-2024-errors-heartbeat-not-sensed
- spirit-hand-pulse-not-working
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 12, PDF p. 10; text.md
    lines 368-369
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **Issue:** Holding a heartbeat has no effect.

| Analysis | Method |
|---|---|
| Poor contact of the heartbeat seat cable. | Check and replace the heartbeat cable. |

**One cause, one cable.** The book blames the cable between the grip "seat" - the metal pads in the handrails - and the console, and nothing else: not the user's hands, not the grips, not a board. It prints no voltage to measure, which the 2022 magnetic-system book does (`csc900-2024-errors-heartbeat-not-sensed`, a DC reading at the seat).

**No chest strap row is printed in this book**, and its console chapter does not mention one. A caller whose strap is not reading has nothing here to work from; do not quote the four-cause hand pulse row of the bikes and treadmills at them either (`spirit-hand-pulse-not-working`) - it was not written for this machine.
