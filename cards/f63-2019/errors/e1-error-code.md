---
id: f63-2019-e1-error-code
title: 'E1 error: no RPM signal in calibration'
kind: troubleshooting
question: What does an E1 error mean on a Sole F63-2019?
asked_as:
- e1 error on my treadmill
- e1 comes up when i calibrate
- sole treadmill error e1
keywords:
- e1
- e1 error
- rpm signal
- speed sensor
- calibration
- reed switch
- motor does not turn
facets:
  brand:
  - sole
  product_line: treadmill
  model: f63-2019
  applies_to:
  - f63-2019
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f63-2019-e0-error-code
- f63-2019-e2-error-code
- f63-2019-e3-error-code
- f63-2019-e4-error-code
- f63-2019-e5-error-code
- f63-2019-e6-error-code
- f63-2019-e7-error-code
see_also:
- f63-2019-error-code-list
- f63-2019-speed-sensor-check
source:
  ref: sole-tm-f63-2019-service-manual
  locator: pages 38 to 43, 8.2 Error Message E1
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety key) and not E7 (input power).**

**Definition**: the display board CPU did not receive the RPM signal. **This only happens during a calibration.** In normal running the console does not need the speed RPM sensor, but calibration does.

**Cause**: the motor does not turn, so E1 appears. The drive board did not send voltage to the motor, so the motor did not operate and the display board received no RPM sensor signal. The speed signal travels on the TX/RX lines of the 6-pin main wire.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the cables are connected well |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap distance **less than 3 mm** |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or the cables |

The step by step sensor check is on its own card.
