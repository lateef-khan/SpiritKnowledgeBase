---
id: s77-2019-e1-no-rpm-signal
title: 'E1: the console received no speed signal'
kind: troubleshooting
question: What does E1 mean on a Sole S77-2019 treadmill?
asked_as:
- e1 error on my treadmill
- s77 shows e1 during calibration
- belt starts then stops and shows e1
keywords:
- e1
- rpm signal
- speed sensor
- calibration
- magnet
- 8 seconds
- gap
- sensor cable
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e2-over-current
- s77-2019-e3-incline-vr
- s77-2019-e4-motor-power-wire
see_also:
- s77-2019-speed-sensor-check
- s77-2019-calibration-procedure
- sole-e1-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.2 Error Message: E1, pages 38-43'
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety key) and not E7 (input power).**

**Meaning**: the display board CPU did not receive the RPM signal. **It only happens during a calibration.** In normal running the machine does not need the speed RPM sensor; the calibration does.

**Why the motor not turning also gives E1**: if the drive board sent no voltage to the motor, the motor does not turn, so the display board receives no RPM signal either. E1 therefore does not tell you on its own whether the sensor or the motor is at fault.

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board has received no speed signal for **8 seconds** | Is the speed sensor cable well connected? | Make sure the cables are properly connected |
| The speed sensor did not detect the signal completely | The gap between the speed sensor and the magnet | Keep the gap **less than 3 mm** |
| Defective sensor or bad cable connection | Are the sensor and cables shorted or damaged? | Change the sensor or the cables |

The speed signal travels on the TX/RX pair of the **6-pin main wire**. The step-by-step sensor check is on the card `s77-2019-speed-sensor-check`.
