---
id: f80-2016-e0-safety-key-error
title: 'E0 error: safety key or safety module'
kind: troubleshooting
question: What does an E0 error mean on a Sole f80-2016 treadmill?
asked_as:
- e0 error on my treadmill
- treadmill shows e0 when i pull the key
- what is error e0 on a sole treadmill
keywords:
- e0
- safety key
- safety module
- 12v loop
- safety switch loop
- main control wire
- display board
- error code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2016
  applies_to:
  - f80-2016
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f80-2016-e1-no-rpm-signal
- f80-2016-e2-over-current
see_also:
- f80-2016-engineering-mode-menu
- sole-safety-key-not-detected
source:
  ref: sole-tm-f80-2016-service-manual
  locator: 'Section 8.1, Error message: E0'
  extracted_at: '2026-09-04'
---

**This is E0, not E1 (no RPM signal) and not E2 (over current).**

**Definition**: "Console is not inserted safety, or safety module may be broken. Or else component of upper control board or lower controller is broken."

**Cause**: the console has no safety key in it, so the console does not form the +12V loop (the safety switch loop) and E0 appears. The main control wires or a component of the lower controller can also be broken, because the lower controller sends the +12V signal through S/W of the main control wire up to the upper control board to close that loop.

| Part | Troubleshooting |
|---|---|
| Safety module | Insert the safety key, then use a multi-meter set to the short-circuit gear position to check whether the safety module wires are short or not. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before the hardware.** Remove the safety key, press STOP + START + ENTER and insert the safety key at the same time. The display enters ENGINEERING MODE. Press FAST/SLOW or UP/DOWN to find "functions", press Enter for "DISPLAY MODE", then Enter to choose on or off.

- **off** means the display goes off after the safety key is removed.
- **on** means the display stays on and shows E0 after the safety key is removed.
