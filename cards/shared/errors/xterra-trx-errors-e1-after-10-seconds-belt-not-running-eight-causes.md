---
id: xterra-trx-errors-e1-after-10-seconds-belt-not-running-eight-causes
title: 'E1 after 10 seconds with the belt never running: eight causes from a controller
  that shut down with the Shut_D light on to a broken console'
kind: troubleshooting
question: Why does an Xterra TRX treadmill show E1 after 10 seconds without the belt
  running, according to the troubleshooting matrix?
asked_as:
- e1 after 10 seconds belt not running trx
- shut_d light on controller e1
- motor belt broken e1
keywords:
- e1
- 10 seconds
- shut_d light
- motor wires
- red black
- computer cable
- motor belt
- controller
- console
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- tr260-2023-errors-err-code-troubleshooting-check-list
- spirit-xt175-errors-ls-error-no-belt-movement-pwm-led
see_also:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-treadmill-errors-e1-solution-flow-chart-pwm-led
- xterra-treadmill-errors-does-not-start-when-start-pressed-motor-m-plus-m-minus-wire
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246
  extracted_at: '2026-09-11'
---

The TRX2500 and TRX3500/TRX4500 service manuals' troubleshooting procedure matrix prints one E1 row that the TR150, TR260 and TRX1400 matrices do not have:

*Condition:* When press "START" button to start treadmill, running belt isn't running and window displays "E1" error message after 10 seconds.

| Reason | Solve |
|---|---|
| 1. Controller experienced unusual shut down; the **Shut_D light will be always bright** | 1. Turn off power and reset the treadmill |
| 2. Motor wires (red, black) aren't plugged into controller | 2. Plug wires again |
| 3. Computer cables not connected properly | 3. Plug the wire again on controller, connector and console |
| 4. Computer cables are broken or damaged | 4. Replace with new wires |
| 5. Motor belt is broken | 5. Replace with new motor belt |
| 6. Controller is broken | 6. Replace with new controller |
| 7. Motor is broken | 7. Replace with new motor |
| 8. Console is broken | 8. Replace with new console |

The "Shut_D light" is not one of the three LEDs the TRX2500 book's own LED table names (`trx2500-2024-errors-controller-led-debugging-three-leds`) nor the INFO/POWER pair of the TRX3500/TRX4500 table; the matrix is the only place it is mentioned. The E1 definition and flow charts are on `xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration` and `xterra-treadmill-errors-e1-solution-flow-chart-pwm-led`.
