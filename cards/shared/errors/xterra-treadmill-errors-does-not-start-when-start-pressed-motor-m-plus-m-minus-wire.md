---
id: xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire
title: 'The treadmill does not start when START is pressed: the motor M+ or M- wire,
  a broken motor, or a controller that shut down and needs the AC switch cycled'
kind: troubleshooting
question: Why does an Xterra treadmill do nothing when I press START, and what should
  I check?
asked_as:
- treadmill does nothing when i press start xterra
- belt will not move start button
- motor wire m+ m- not connected
keywords:
- will not start
- start button
- motor wire
- m+
- m-
- motor broken
- controller shut down
- ac switch
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-motor-not-responsive-after-start-contact-service
- xterra-treadmill-errors-stops-immediately-after-start-controller
see_also:
- xterra-treadmill-errors-e4-motor-power-wires-not-in-lower-controller
- xterra-treadmill-errors-stops-immediately-after-start-controller
- xterra-trx-errors-e1-after-10-seconds-belt-not-running-eight-causes
- spirit-xt-errors-does-not-start-motor-m-plus-m-minus-wire
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246; TR150 SM 8.11
    Troubleshooting procedure matrix, PDF pp. 49-50 (printed 57-58); text.md lines
    826-906; TR260 SM 8-13 Troubleshooting procedure matrix, PDF pp. 51-53; text.md
    lines 794-900; TRX1400 SM Troubleshooting procedure matrix, PDF pp. 61-63 (printed
    55-57); text.md lines 1102-1208; TR150 MCB wiring photo (authority 2), the labels
    SPD / 'If you have speed sensor, then it plugs here', 'M+ Red lead from drive
    motor', 'M- Black lead from drive motor'; text.md lines 1-40
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints this row in all five service manuals:

*Condition:* When press "START", treadmill doesn't start.

| Reason | Solve |
|---|---|
| 1. Motor M+ or M- wire isn't connected in the right position (TR260: "Motor wire") | 1. Check and plug again |
| 2. Motor is broken | 2. Replace motor, or check the wire and connector if it was broken |
| 3. Treadmill controller shut down (TR260 adds "and TFT would be ON"; TRX2500/TRX3500/TRX4500 add "and LED would be ON") | 3. Turn off the AC switch and turn on power again |

On the TR150 board the photo marks the motor leads **M+ red** and **M- black**. A START press that is followed by an E1 has its own rows (`xterra-trx-errors-e1-after-10-seconds-belt-not-running-eight-causes`, `xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`); a belt that starts and then stops at once is `xterra-treadmill-errors-stops-immediately-after-start-controller`. The owner's-manual row for the new-layout books simply says to contact service (`xterra-treadmill-errors-motor-not-responsive-after-start-contact-service`).
