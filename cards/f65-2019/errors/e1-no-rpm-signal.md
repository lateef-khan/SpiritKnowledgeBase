---
id: f65-2019-e1-no-rpm-signal
title: 'E1 error: display board received no RPM signal'
kind: troubleshooting
question: What does an E1 error mean on a Sole f65-2019 treadmill?
asked_as:
- e1 error on my treadmill
- treadmill shows e1 during calibration
- e1 error and the belt will not move
keywords:
- e1
- rpm signal
- speed sensor
- reed switch
- calibration
- no speed signal
- magnet
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2019
  applies_to:
  - f65-2019
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f65-2019-e0-safety-key-error
- f65-2019-e2-over-current
see_also:
- f65-2019-speed-sensor-check
- f65-2019-calibration-procedure
- sole-e1-error
source:
  ref: sole-tm-f65-2019-service-manual
  locator: 'Section 8.2, Error Message: E1'
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety key) and not E2 (over current).**

**Definition**: "Display board CPU did not receive the RPM signal." The manual adds that this **only happens during the calibration** - in normal running the speed RPM sensor is not necessary, but during calibration it is.

**Cause**: the motor does not turn, so E1 appears. The drive board did not send voltage to the motor, the motor did not operate, and the display board did not receive the RPM sensor signal. The speed signal travels through TX/RX of the 6-pin main line.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board hasn't receive any speed signal for 8 seconds | check the speed sensor cable is in good connection | Make sure the good connection for cables |
| The speed sensor didn't detect signal completely. | Check the gap between speed sensor and magnet. | To keep the gap-distance **less than 3 mm**. |
| Defective sensor or bad cable connection. | Check if the sensor and cables are circuit short damaged. | Change the sensor or cables. |
