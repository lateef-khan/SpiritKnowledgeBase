---
id: f85-2016-e0-safety-key-error
title: 'E0: the safety switch loop is open'
kind: troubleshooting
question: What does E0 mean on a Sole F85-2016 treadmill and how do I fix it?
asked_as:
- my treadmill shows e0
- e0 error on the display
- treadmill says e zero with the key in
keywords:
- e0
- safety key
- safety module
- tether cord
- safety switch loop
- main control wire
- display board
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f85-2016-e1-no-rpm-signal
- f85-2016-e2-over-current
- f85-2016-e3-incline-vr-error
- f85-2016-e4-motor-power-wire-error
- f85-2016-e5-communication-error
- f85-2016-e6-lower-controller-error
- f85-2016-e7-input-power-error
see_also:
- f85-2016-display-mode-setting
- f85-2016-console-modes-and-buttons
source:
  ref: sole-tm-f85-2016-service-manual
  locator: 'section 8.1 Error Message: E0, printed pages 37 to 38, and the error code
    table on page 36'
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no RPM signal during calibration) and not E7 (input power).**

| Field | Value |
|---|---|
| Code | E0 |
| Cause, as printed | Safety keys dose not insert the safety module. Or safety module is broken. |
| Definition | Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken. |

**Why it happens.** The console needs a +12V loop, the safety switch loop, before it will run. The lower controller sends +12V up the S/W line of the main control wire to the upper control board to close that loop. With no safety key the loop is open and the display shows E0. A broken main control wire or a broken part in the lower controller opens the same loop.

| Part | What to do |
|---|---|
| Safety module | Insert the safety key, then set the multimeter to its continuity (short circuit) position and check whether the safety module wires are shorted. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before you check any hardware.** DISPLAY MODE decides whether the console shows E0 at all when the key is pulled. See the display mode card.
