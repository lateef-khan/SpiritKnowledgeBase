---
id: spirit-xt175-errors-incline-does-not-work-five-checks
title: 'The incline does not work: calibrate, check the harness, the ERR message and
  the incline motor wires, then the beep and the UP and DOWN lights'
kind: troubleshooting
question: What do I check when the incline does not work on a Spirit XT175, XT275,
  XT375, XT475 or XT675 2007 or CT800 2016 treadmill?
asked_as:
- incline does not move on my spirit treadmill
- err in the incline window
- no beep when i press incline up
keywords:
- incline does not work
- err
- incline motor
- wire harness
- relay click
- up down lights
- beep
- console
- controller
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - xt175-2007
  - xt275-2007
  - xt375-2007
  - xt475-2007
  - xt675-2007
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-err-vr-out-of-range
- spirit-mt200-errors-e41-incline-err
see_also:
- spirit-xt175-errors-checking-wire-harness-continuity
- ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
- ct800-2016-errors-incline-err-during-incline-action
source:
  ref: spirit-treadmill-xt175-xt275-xt375-xt475-xt675-2007-service-manual
  locator: XT175-XT675 2008 dealer service manual Troubleshooting Guide - Electronic
    System, PDF p. 3, text.md lines 48-113; CT800 2016 service manual Treadmill Troubleshooting
    - Electronic System, PDF p. 63 (printed 62), text.md lines 1273-1333
  extracted_at: '2026-09-11'
---

Five checks, in the order printed.

1. Run the calibration procedure.
2. Check the wire harness for continuity (`spirit-xt175-errors-checking-wire-harness-continuity`).
3. If there is an **ERR** message in the incline window, make sure all the wires from the incline motor are connected to the controller correctly - the XT controller diagram gives *Down = black, Com = white, Up = red*. If they are connected correctly and the calibration does not fix it, replace the incline motor.
4. When the UP and DOWN buttons are pressed there should be a **beep** and a number change in the incline window. If there is not, replace the console.
5. Observe the UP and DOWN diagnostic lights on the controller. When UP or DOWN is pressed you should (1) see one of the lights come on and (2) hear a relay click.
   - No relay click and no diagnostic lights: replace the console, the lower and middle wire harness, and the controller.
   - A relay click and a diagnostic light, with the motor wires connected correctly: replace the incline motor.

Printed identically in the 2008 XT dealer manual and the CT800 2016 service manual's *Treadmill Troubleshooting* chapter. The `ERR` here is the message the CT800 2016 calls `INCLINE ERR` in its main error chapter, where it gets a nine-step voltage test (`ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12`). Step 5's no-click-no-light answer replaces three parts at once; the nine-step test measures before condemning any of them.
