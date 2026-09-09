---
id: ct850-2016-incline-calibration-fails-checks
title: What to check when the incline calibration fails
kind: procedure
question: What do I check when incline calibration fails on a Spirit CT850-2016 treadmill?
asked_as:
- incline calibration fails on my spirit treadmill
- calibration will not complete
- incline motor wiring check
keywords:
- calibration fails
- incline motor
- position sensor
- vr connector
- wire harness
- pin assignment
- incline board
- neutral
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-incline-err-test-procedure
- ct850-2016-incline-err-during-incline-action
- ct850-2016-incline-motor-replacement
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Incline troubleshooting, AC 120V system with AC motor - If calibration
    fails, page 60 (printed 59)
  extracted_at: '2026-09-08'
---

Remove the motor cover and check every wiring connection from the incline motor to the incline
board. Push all connectors in until they are fully seated. The connectors to be concerned with are:

1. **The 3 power wires for the incline motor.**

   | Pin | Signal |
   |---|---|
   | 1 | Neutral |
   | 2 | Up |
   | 3 | Down |

2. **The position sensor wires, 3-pin connector on the incline motor, marked `VR`.**

   | Pin | Signal |
   |---|---|
   | 1 | Ground |
   | 2 | Position signal (0~5 V depending on incline position) |
   | 3 | 5 Vdc |

3. **The main wire harness at the bottom of the board.**

This section is headed `Incline troubleshooting, AC 120V system with AC motor`, which is the supply
the rest of the manual assumes. The incline test procedure on `ct850-2016-incline-err-test-procedure`
quotes ~230 VAC at the motor instead; that figure does not agree with this heading.

The calibration procedure itself is a console task and is printed twice in this manual with
different speed limits - see the console section.

If a connector check does not clear it, the motor removal procedure is on
`ct850-2016-incline-motor-replacement`.
