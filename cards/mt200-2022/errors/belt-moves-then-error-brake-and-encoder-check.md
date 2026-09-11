---
id: mt200-2022-errors-belt-moves-then-error-brake-and-encoder-check
title: 'The belt moves and then an error appears: the motor brake must release, with
  about 19 V DC from the drive, and the encoder LEDs must blink'
kind: troubleshooting
question: What do I check when the belt moves and then an error code appears on a
  Spirit mt200-2022 treadmill?
asked_as:
- 7.0t belt runs then error
- motor brake stuck on the medical treadmill
- encoder leds do not blink
keywords:
- belt moves then error
- motor brake
- brake off
- engineering mode
- 19v dc
- encoder
- red and green led
- flywheel
- replace brake
- replace drive
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2026
  - mt200-2022
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- 70t-2026-errors-e27-pg-error
- mt200-2022-errors-e27-encoder-email-encoder-then-inverter-then-motor
- 70t-2026-errors-e1-over-current
- mt200-2022-errors-no-belt-movement-motor-two-ohms
source:
  ref: spirit-treadmill-mt200-2022-service-manual
  locator: 7.0T (MT200 2022) service manual 5. Troubleshooting and Problem solving,
    item 3 Belt moves then error occurs, PDF p. 20-21, text.md lines 407-433 The February 2026 export of the same book is titled 7.0T-770885 (MT8000-ST021-01), spirit-treadmill-70t-2026-service-manual, and prints this page unchanged.
  extracted_at: '2026-09-11'
---

Section 5, item 3 of the 7.0T service manual:

1. **Check that the motor brake works.** Turn the brake off in maintenance mode (the Motor Brake test under Service Mode); the belt should then move freely. If the belt is still locked with the brake turned off in engineering mode, measure the drive's output to the brake - **about 19 V DC**. Replace the brake if that voltage is present, replace the drive if it is not.
2. **Check the encoder board on the motor.** Its red and green LEDs should blink when the motor's flywheel is turned.

The maintenance-mode brake test itself says the brake coil is energised when the brake is *off* and there should be 18 Vdc at the two brake wires - one volt from the figure here, and both from the same book; either is the neighbourhood to expect. The codes this symptom raises are the over-current and over-torque ones, whose remedies all say *check that the brake is released when the motor is moving* (`70t-2026-errors-e1-over-current`, `70t-2026-errors-e8-over-torque`), and E27 for the encoder (`70t-2026-errors-e27-pg-error`). Spirit's service email on E27 gives the field version of this check (`mt200-2022-errors-e27-encoder-email-encoder-then-inverter-then-motor`).

**This book is also the 7.0T 770885's service manual.** Spirit's February 2026 export of it is titled *7.0T-770885 (MT8000-ST021-01)* and is 99.7% the same text (the parts-list header reads MT8000 where the 2021 export reads MT7000), so the 2026 7.0T (`70t-2026`) is listed here alongside the MT200.
