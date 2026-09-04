---
id: f60-2020-e1-error-code
title: 'E1 error: no RPM signal in calibration'
kind: troubleshooting
question: What does an E1 error mean on a Sole F60-2020?
asked_as:
- e1 error on my treadmill
- e1 comes up when i calibrate
- belt does not move and shows e1
keywords:
- e1
- e1 error
- rpm signal
- speed sensor
- calibration
- reed switch
- shut-d light
- motor does not turn
facets:
  brand:
  - sole
  product_line: treadmill
  model: f60-2020
  applies_to:
  - f60-2020
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- f60-2020-e0-error-code
- f60-2020-e2-error-code
- f60-2020-e3-error-code
- f60-2020-e4-error-code
- f60-2020-e5-error-code
- f60-2020-e6-error-code
see_also:
- f60-2020-error-code-list
- f60-2020-speed-sensor-check
source:
  ref: sole-tm-f60-2020-service-manual
  locator: pages 36 to 41, 8.2 Error Message E1, and page 56 of the matrix
  extracted_at: '2026-09-04'
---

**This is E1, not E0 (safety key) and not E3 (incline).**

**Definition**: the display board CPU did not receive the RPM signal. **This only happens during a calibration.**

**Cause**: the motor does not turn, so E1 appears. The drive board did not send voltage to the motor, so the motor did not operate and the display board received no RPM sensor signal. The signal path runs through a 5-pin connection.

| Possible cause | Things to check | Solution |
|---|---|---|
| The monitor hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the cables are connected well |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | Keep the gap distance **less than 3 mm** |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or the cables |

**A second E1 case, from the troubleshooting matrix**: you press START, the running belt does not run, and after **10 seconds** the window displays E1.

| Reason | Solve |
|---|---|
| The controller experienced an unusual shut down; the **Shut-D light is always bright** | Turn the power off and reset the treadmill |
| The motor wires (red, black) aren't plugged into the controller | Plug the wires in again |
| The computer cables are not connected properly | Plug the wire in again on the controller, connector and console |
| The computer cables are broken or damaged | Replace with new wires |
| The motor belt is broken | Replace with a new motor belt |
| The controller is broken | Replace with a new controller |
| The motor is broken | Replace with a new motor |
| The console is broken | Replace with a new console |
