---
id: f85-2021-e0-safety-key-message
title: 'E0: the console asks you to replace the safety key'
kind: troubleshooting
question: What does the please replace the safety key message, listed as E0, mean
  on a Sole F85-2021 treadmill?
asked_as:
- console says please replace the safety key
- my treadmill shows e0
- treadmill will not run with the key in
keywords:
- e0
- please replace the safety key
- safety key
- safety module
- safety switch loop
- main control wire
- message window
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f85-2021-e1-no-rpm-signal
- f85-2021-e2-over-current
- f85-2021-e3-incline-vr-error
- f85-2021-e4-motor-power-wire-error
- f85-2021-e5-communication-error
- f85-2021-e6-lower-controller-error
- f85-2021-e7-input-power-error
see_also:
- f85-2021-display-mode-setting
- f85-2021-console-modes-and-buttons
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: section 8.1, printed pages 40 to 42, and the error code table on page 39
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no RPM signal during calibration) and not E7 (input power).**

**On this console the fault is a message, not a code.** The error code table lists it under E0 but describes it as: "The display appears PLEASE REPLACE THE SAFETY KEY. It means safety key is removed." Section 8.1 is titled by that message rather than by the code, and its body still refers to the fault as E0. Both names describe one fault.

| Field | Value |
|---|---|
| Code | E0 |
| Shown on screen | 「PLEASE REPLACE THE SAFETY KEY」in the message window |
| Definition | Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken. |

**Why it happens.** The console needs a +12V loop, the safety switch loop, before it will run. The lower controller sends +12V up the S/W line of the main control wire to the upper control board to close that loop. With no safety key the loop is open. A broken main control wire or a broken part in the lower controller opens the same loop.

The manual shows the **safety pin position on the console board**, with a separate picture for the **Android 6** console.

| Part | What to do |
|---|---|
| Safety module | Insert the safety key, then set the multimeter to its continuity (short circuit) position and check whether the safety module wires are shorted. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before you check any hardware.** Display Mode decides how the console behaves when the key is pulled. See the display mode card.
