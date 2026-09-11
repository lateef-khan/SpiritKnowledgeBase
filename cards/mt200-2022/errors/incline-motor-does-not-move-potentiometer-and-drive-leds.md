---
id: mt200-2022-errors-incline-motor-does-not-move-potentiometer-and-drive-leds
title: 'The incline motor does not move: 5 V and 0.5 to 5 V at the potentiometer,
  the drive LEDs for the front motor, the board LEDs for the rear'
kind: troubleshooting
question: What do I check when the front or rear incline motor does not move on a
  Spirit mt200-2022 treadmill?
asked_as:
- 7.0t incline does not move
- rear incline motor not working on the medical treadmill
- incline relay stuck tap it
keywords:
- incline motor
- decline motor
- rear incline
- potentiometer
- position sensor
- 5v dc
- relay
- incline led
- drive
- low control board
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
- spirit-mt200-errors-e41-incline-err
- spirit-mt200-errors-e42-decline-err
- mt200-2022-errors-step-sensors-no-response-10-to-12-v-dc
source:
  ref: spirit-treadmill-mt200-2022-service-manual
  locator: 7.0T (MT200 2022) service manual 5. Troubleshooting and Problem solving,
    item 5 Incline motor, PDF p. 23-24, text.md lines 448-481 The February 2026 export
    of the same book is titled 7.0T-770885 (MT8000-ST021-01), spirit-treadmill-70t-2026-service-manual,
    and prints this page unchanged; the 7.0T-770885 export of the same book (spirit-treadmill-70t-2026-service-manual,
    "MT8000-ST021-01" on its cover, February 2026) prints this page identically at
    the same PDF page, text.md lines 28 higher from line 52 on (99.7% at word level;
    only the cover, the component-description callouts and the parts-list heading
    differ)
  extracted_at: '2026-09-11'
---

Section 5, item 5 of the 7.0T service manual - the *troubleshooting section* the E41 and E42 remedies point at (`spirit-mt200-errors-e41-incline-err`, `spirit-mt200-errors-e42-decline-err`).

1. Make sure the wiring connections have no problems, then run the **incline motor test in maintenance mode** (a console procedure; incline keys drive the front motor, speed keys the rear, and the display shows both position-sensor numbers). Go to step 2 if the motor does not move during the test. **If the motor moves but its position number does not change**, measure the potentiometer in the motor: remove the cover's Phillips screw and measure **5 V DC across pins 1 and 3**, and **0.5 to 5 V DC across pins 1 and 2**. If not, replace the motor - the book says the potentiometer alone could be replaced but that it is a difficult factory procedure needing special training.
2. Check the power to the motor.
   - **Front incline: the LEDs on the drive.** One should light when raising the front incline, the other when lowering it. Lights normal and no movement: replace the incline motor. **A light that stays on without an incline command: hit the relay (the black box) with the handle of a screwdriver.** No light on an incline command: replace the drive.
   - **Rear incline: the LEDs on the low control board.** The left one lights when the rear incline is increased, the right one when it is decreased. Lights normal and no movement: replace the incline motor. Otherwise replace the low control board.

So the front motor is driven from the inverter and the rear from the lower board, and each has its own pair of LEDs. The tap-the-relay step is the same one the E41 remedy prints as *Relay stuck. Check the incline LEDs on control board. Use something to tap the relay*.

**This book is also the 7.0T 770885's service manual.** Spirit's February 2026 export of it is titled *7.0T-770885 (MT8000-ST021-01)* and is 99.7% the same text (the parts-list header reads MT8000 where the 2021 export reads MT7000), so the 2026 7.0T (`70t-2026`) is listed here alongside the MT200.
