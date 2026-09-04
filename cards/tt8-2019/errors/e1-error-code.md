---
id: tt8-2019-e1-error-code
title: E1 no RPM signal from the speed sensor
kind: troubleshooting
question: What does error E1 mean on a Sole tt8-2019 treadmill?
asked_as:
- treadmill shows e1 and stops
- e1 error belt does not move
- what is error code e1
keywords:
- e1
- rpm signal
- speed sensor
- reed switch
- magnet
- calibration
- belt does not move
- 8 seconds
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2019
  applies_to:
  - tt8-2019
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- tt8-2019-e0-error-code
- tt8-2019-e2-error-code
- tt8-2019-e3-error-code
- tt8-2019-e4-error-code
- tt8-2019-e5-error-code
- tt8-2019-e6-error-code
- tt8-2019-e7-error-code
- tt8-2019-ac-e-01h-error-code
see_also:
- tt8-2019-speed-sensor-check
- tt8-2019-calibration-procedure
- tt8-2019-error-code-list
source:
  ref: sole-tm-tt8-2019-service-manual
  locator: Section 8.2, pages 38-43
  extracted_at: '2026-09-04'
---

**DC model: TT8 2019 ST928-YT035, DC drive motor. The AC inverter TT8 2019 (ST928A-YT037) is a different machine and this card does not apply to it.**

**This is E1, not E7 (input power) and not E2 (over current).**

Definition: display board CPU did not receive the RPM signal. It only happens during calibration; in
normal running the speed RPM sensor is not necessary, but for calibration it is.

Cause: the motor does not turn, so E1 appears. The drive board did not send voltage to the motor, the
motor did not operate, and the display board did not receive the RPM sensor signal. Speed signal is sent
and received on **TX/RX of the 6-pin main wire**.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the good connection for cables |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap-distance less than 3 mm |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or cables |

The service troubleshooting checklist adds a split the fault table does not: **if the belt moves and then stops with E1, run calibration; if you press START and the belt never moves at all and E1 appears, contact service.**
