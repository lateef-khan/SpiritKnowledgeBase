---
id: tr260-2023-errors-err-code-troubleshooting-check-list
title: 'The Err code troubleshooting check list: OK/NG boxes for a dead console and
  for each code, with the E1 sensor gap printed as 3 to 5 mm'
kind: troubleshooting
question: What is the Err code troubleshooting check list in the Xterra tr260-2023
  service manual, and what does it say to inspect for each error code?
asked_as:
- tr260 error code check list
- tr260 e1 speed sensor gap 3 to 5 mm
- console without power check list tr260
keywords:
- check list
- ok ng
- console without power
- fuse
- varistor
- relay click
- md light
- reed switch
- speed sensor gap
- 3 to 5 mm
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-trx-errors-e1-after-10-seconds-belt-not-running-eight-causes
see_also:
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- xterra-treadmill-errors-power-switch-not-lit-nine-causes
- tr260-2023-errors-controller-led-debugging-speed-led
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM 8-12 Err code troubleshooting check list, PDF pp. 48-50; text.md
    lines 738-794
  extracted_at: '2026-09-11'
---

Section 8-12 of the TR260 service manual is a one-page inspection form with an OK / NG box against every item. It is the only Xterra book that prints one. The rows:

| Trouble | Diagnosis / inspection | Possible cause / inspection item |
|---|---|---|
| Console without power | External power problem | Check power outlet to the treadmill. Make sure power switch light is on after turning on the switch |
| | Internal control / lower controller | Make sure fuse is OK and varistor is free from damage. The relay clicks after power is on and the safety key is put on |
| | All connectors are inserted properly | Terminal wire coppers are tight, secure and free from damage. Console and controller boards are properly connected and the connecting cables are free from damage. Motor power is connected properly with correct polarity |
| Console shows E1 | Motor turns about 10 seconds after pressing start, then stops with E1 | Speed sensor by the front roller is not properly connected to the controller, or the sensor body or cable is damaged. The sensor body is not properly located (**must be less than 3~5mm of gap** between the sensor and front roller). Console and controller boards properly connected, cables free from damage |
| | Motor does not turn at all after pressing start, E1 after about 10 seconds | Check if **MD light** is on after start is pressed. Motor power connected with correct polarity. Check if the problem persists with a new controller |
| Console shows E0 | Safety switch malfunction or intermittence | Safety key placed properly and the safety switch mechanism not loose. Cable for the **mileage switch** in the console properly connected, connector free from damage. Reed switch free from damage |
| Console shows E2 | Treadmill is overloaded and the controller's protection device is activated | Has the tread belt shifted; is lubrication sufficient, is the resistance high. Is the bearing worn. Is the circuit over heated. Is the incline mechanism stuck or defective. Is calibration done; is there still E3 after calibration |
| Console shows E3 | Incline malfunction | Incline cables connected properly. Incline mechanism stuck or defective. Is calibration done; is there still E3 showing after calibration |
| Console shows E4 | Abnormal voltage between motor terminals | Motor cable is not properly connected |
| Console shows E5 | Communication between console and controller is disconnected | Console and drive board connected properly with connecting cable free from damage |
| Console shows E6 | Controller is defective | Controller component malfunction - Replace controller |
| Console shows E7 | Abnormal input voltage | Check if input voltage fulfils the requirement. Check switch light is on after turning on; check if power is normal |

Three things only this list says. The E1 sensor gap is **3~5 mm** here and less than 3 mm everywhere else in the same book. The E2 row carries two incline items ("incline mechanism stuck", "still E3 after calibration") that look copied from the E3 row. And the list has an **E7** row although the book's own code table (8-1) stops at E6 and the book has no 8-x section for E7.

Per-code detail: `xterra-treadmill-errors-e0-safety-key-device-buzzer-test`, `xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`, `xterra-treadmill-errors-e2-over-current-silicone-oil-then-board-or-motor`, `xterra-treadmill-errors-e3-incline-vr-out-of-range`, `xterra-treadmill-errors-e4-motor-power-wires-not-in-lower-controller`, `xterra-treadmill-errors-e5-console-controller-communication-poor`, `xterra-treadmill-errors-e6-lower-controller-component-fault`, `xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable`.
