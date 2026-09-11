---
id: ct850-2016-low-speed-solution-flow-chart
title: Working through the LOW SPEED fault step by step
kind: procedure
question: How do I diagnose a LOW SPEED message on a Spirit CT800-2016 or CT850-2016
  treadmill?
asked_as:
- how to fix low speed on my spirit treadmill
- step by step for ls1 low speed
- treadmill low speed troubleshooting flow
keywords:
- low speed
- flow chart
- pwm led
- controller
- motor cable
- m+ m-
- replace controller
- replace motor
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - ct850-2016
  section: errors
  code: low-speed
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-low-speed-error-message
- ct850-2016-low-speed-check-rpm-sensor
- ct850-2016-low-speed-troubleshooting-form
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 8.1, LOW SPEED solution follow chart, page 32 (printed 31). This
    page is a flattened image; it was read from raw/page-32.png, not from the OCR
    text; CT800 2016 service manual LOW SPEED solution follow chart, a flat picture
    read from the render, PDF p. 35 (printed 34), text.md lines 595-602
  extracted_at: '2026-09-08'
---

The manual gives this as a flow chart. Read in order.

1. **Did the belt move after start?**
   - Yes -> go to the RPM sensor check, `ct850-2016-low-speed-check-rpm-sensor`.
   - No -> continue.
2. Open the motor hood and turn the power back on.
3. Press **start** to count down and watch the **PWM LED** on the controller.
4. **Is the PWM LED on?**
   - No -> is the cable connection OK? If it is, replace the cable. If it is not, connect it
     properly. Then turn the power back on: if it works, the problem is fixed; if not, replace the
     console, and if that still fails, replace the controller.
   - Yes -> continue.
5. **Are only the POWER and PWM LEDs on?** If yes, replace the controller.
6. **Is the motor cable connected to the M+ and M- terminals properly?**
   - Yes -> problem fixed.
   - Otherwise -> replace the controller, turn the power back on and press start to count down. If
     it still does not work, replace the motor.

Two defects in the printed chart, stated so nobody reads past them:

- Both branches leaving `Are only POWER and PWM LEDs on` are labelled **YES**. The right-hand branch
  ends at `Replace controller`; the downward branch continues to the motor cable check.
- The `Cable connection OK?` diamond sends **YES** to `Replace cable` and **NO** to `Connect
  properly`, which reads backwards. The sense the manual intends is: if the connection looks sound
  and it still fails, the cable itself is bad.

What the message means is on `ct850-2016-low-speed-error-message`.

**The CT800 2016 service manual prints the identical chart**, both defects included - the two branches labelled YES out of the POWER-and-PWM diamond, and the cable diamond that sends YES to *Replace cable*. It was read from the rendered page.
