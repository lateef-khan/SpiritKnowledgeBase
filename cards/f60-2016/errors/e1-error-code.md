---
id: f60-2016-e1-error-code
title: 'E1 error: no speed feedback signal'
kind: troubleshooting
question: What does an E1 error mean on a Sole F60-2016?
asked_as:
- e1 error on my treadmill
- treadmill will not run and shows e1
- sole treadmill error e1
keywords:
- e1
- e1 error
- speed feedback
- rpm sensor
- speed sensor
- reed switch
- motor does not turn
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2016
  applies_to:
  - f60-2016
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f60-2016-e0-error-code
- f60-2016-incline-er-message
- f60-2016-e2-error-code
- f60-2016-e4-error-code
- f60-2016-e5-error-code
- f60-2016-e6-error-code
see_also:
- f60-2016-error-code-list
- f60-2016-speed-sensor-check
source:
  ref: sole-tm-f60-2016-service-manual
  locator: pages 40 to 45, 8.2 Error Message E1
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety device) and not E2 (over current).**

**Definition**: the console did not receive the speed feedback signal, E1 appears, and the treadmill does not operate.

**Cause**: the drive board did not send voltage to the motor, so the motor did not operate and the display board received no RPM sensor signal. The RPM sensor signal reaches the display board through the driver board and a **5-pin** connection; the sensor itself is on a 2-pin connection to the driver board.

| Possible cause | Things to check | Solution |
|---|---|---|
| The monitor hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the cables are connected well |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap distance **less than 3 mm** |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or the cables |
