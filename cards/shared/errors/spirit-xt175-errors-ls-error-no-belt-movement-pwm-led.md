---
id: spirit-xt175-errors-ls-error-no-belt-movement-pwm-led
title: 'LS error with no belt movement at all: the PWM LED decides between the controller
  and the console'
kind: troubleshooting
question: What do I do when the belt never moves and then shows an LS error on a Spirit
  XT175, XT275, XT375, XT475 or XT675 2007 or CT800 2016 treadmill?
asked_as:
- belt never moves and shows ls
- ls error and nothing happens when i press start
- pwm led on the treadmill controller
keywords:
- ls error
- ls
- low speed
- no belt movement
- pwm led
- controller
- console
- wire harness
- calibration
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
  code: ls
authority: 3
not_to_be_confused_with:
- spirit-xt175-errors-ls-error-after-belt-moves
- sole-ls-error
see_also:
- spirit-xt175-errors-checking-wire-harness-continuity
- ct850-2016-low-speed-solution-flow-chart
- ct850-2016-motor-not-responsive-after-start
source:
  ref: spirit-treadmill-xt175-xt275-xt375-xt475-xt675-2007-service-manual
  locator: XT175-XT675 2008 dealer service manual Troubleshooting Guide - Electronic
    System, PDF p. 3, text.md lines 48-113; CT800 2016 service manual Treadmill Troubleshooting
    - Electronic System, PDF p. 63 (printed 62), text.md lines 1273-1333
  extracted_at: '2026-09-11'
---

**This is the LS row for a belt that never moved - not the row for a belt that ran a few seconds first** (`spirit-xt175-errors-ls-error-after-belt-moves`), and not a Sole LS.

1. Run the calibration procedure.
2. Check the wire harness for continuity (`spirit-xt175-errors-checking-wire-harness-continuity`).
3. Look at the LED labelled **PWM** on the controller.
   - If it lights up when the START button is pressed, **replace the controller**.
   - If it does not light when the START button is pressed, **replace the console**.

Printed identically in the 2008 XT dealer manual and the CT800 2016 service manual's *Treadmill Troubleshooting* chapter. The logic: the console asks for speed over the harness; a PWM LED that answers START means the controller heard the request and failed to drive the motor, a dark one means the request never arrived. The CT800 2016's own LOW SPEED flow chart uses the same PWM LED test with more branches (`ct850-2016-low-speed-solution-flow-chart`).
