---
id: f85-2021-e1-no-rpm-signal
title: 'E1: no RPM signal reached the display board'
kind: troubleshooting
question: What does E1 mean on a Sole F85-2021 treadmill and how do I fix it?
asked_as:
- e1 error on my treadmill
- treadmill shows e1 during calibration
- belt starts then stops and shows e1
keywords:
- e1
- rpm signal
- speed sensor
- magnet gap
- calibration
- six pin main wire
- error code
- no speed reading
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f85-2021-e0-safety-key-message
- f85-2021-e2-over-current
- f85-2021-e3-incline-vr-error
- f85-2021-e4-motor-power-wire-error
- f85-2021-e5-communication-error
- f85-2021-e6-lower-controller-error
- f85-2021-e7-input-power-error
see_also:
- f85-2021-speed-sensor-check
- f85-2021-calibration-procedure
- sole-e1-error
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: 'section 8.2 Error Message: E1, printed pages 43 to 49, and section 10.2
    diagnosis guide, printed page 85'
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety key) and not E2 (over current).**

| Field | Value |
|---|---|
| Code | E1 |
| Cause, as printed | Display board CPU did not receive the RPM signal. |
| When | Only happen in the Calibration. In generally, it does not necessary speed RPM sensor, but when the Calibration which it is a necessary. |

The speed signal travels on the **TX/RX pair of the 6-pin main wire**. The manual's own explanation is that the drive board sent no voltage to the motor, so the motor did not turn and the display board never saw an RPM pulse.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the good connection for cables |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | To keep the gap-distance less than 3 mm |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or cables |

**Two different symptoms, from the diagnosis guide:**

- The belt moves but stops after a short time and the display shows E1: **run calibration.**
- You press start, the belt never moves, and the display shows E1: **contact service.**
