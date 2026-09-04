---
id: f85-2023-e1-no-rpm-signal
title: 'E1 error: no RPM signal during calibration'
kind: troubleshooting
question: What does an E1 error mean on a Sole f85-2023 treadmill?
asked_as:
- e1 error on my treadmill
- treadmill shows e1 during calibration
- e one error on the console
keywords:
- e1
- e1 error
- rpm signal
- speed sensor
- calibration
- magnet gap
- 3 mm
- display board
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2023
  applies_to:
  - f85-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f85-2023-e2-over-current
- ct900-e1-over-current
- ct900-e10-accel-ovr-curr
- cc81-2020-e1-eeprom-failure
see_also:
- f85-2023-error-code-list
- f85-2023-speed-sensor-alignment
- sole-e1-error
source:
  ref: sole-tm-f85-2023-service-manual
  locator: 'Section 8.2 Error Message: E1, pages 35-38'
  extracted_at: '2026-09-04'
---

**This is E1, not E2 (over current) and not E3 (incline VR voltage).**

**Definition.** The display board CPU did not receive the RPM signal. It only happens during calibration: the
speed RPM sensor is not generally needed, but calibration needs it.

**Cause.** The motor does not turn, so E1 appears. The drive board did not send voltage to the motor, so the motor
did not run, and the display board received no RPM sensor signal.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board has not received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the cables are connected properly |
| The speed sensor did not detect the signal completely | Check the gap between the speed sensor and the magnet | **Keep the gap less than 3 mm** |
| Defective sensor or bad cable connection | Check whether the sensor and cables are short circuit damaged | Change the sensor or the cables |

Where the sensor sits and how to move it is on the speed sensor alignment card.
