---
id: f65-2023-e0-safety-key-not-detected
title: 'E0 error: safety key not detected'
kind: troubleshooting
question: What does an E0 error mean on a Sole f65-2023 treadmill?
asked_as:
- e0 error on my treadmill
- treadmill shows e zero
- console will not see the safety key
keywords:
- e0
- e0 error
- safety key
- safety module
- main control wire
- display board
- 12v loop
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2023
  applies_to:
  - f65-2023
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- f65-2023-e1-no-rpm-signal
see_also:
- f65-2023-error-code-list
- sole-safety-key-not-detected
source:
  ref: sole-tm-f65-2023-service-manual
  locator: 'Section 8.1 Error Message: E0, page 21'
  extracted_at: '2026-09-04'
---

**This is E0, the safety key fault. It is not E1 (no RPM signal during calibration).**

**Definition.** The console is not inserted safety, or the safety module may be broken. A component of the
upper control board or the lower controller can also be broken.

**Cause.** With no safety key the console cannot form the +12V loop (the safety switch loop). The lower controller
sends the +12V signal through the S/W line of the main control wire up to the upper control board to close that
loop, so a broken main control wire or a broken lower controller component gives the same result.

| Part | Troubleshooting |
|---|---|
| Safety module | Insert the safety key, then set a multi-meter to the short circuit gear position and check whether the safety module wires are short or not. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before the hardware.** Remove the safety key, press STOP, START and ENTER, and insert
the safety key at the same time. The display enters ENGINEERING MODE. Press FAST/SLOW or UP/DOWN to find
"functions", press Enter for "DISPLAY MODE", then press Enter to choose on or off. "off" means the display goes
off after the safety key is removed. "on" means the display stays on and shows E0 after the key is removed.

**Section 3 of the same manual disagrees.** Its Safety Key row says the display will show "Please Replace the
Safety Key" with no key fitted. Section 8 prints E0. The 2023 touchscreen manuals use the words, not the code.
