---
id: tt8-2016-e0-error-code
title: E0 safety key not detected
kind: troubleshooting
question: What does error E0 mean on a Sole tt8-2016 treadmill?
asked_as:
- e0 on my treadmill display
- treadmill shows e0 with the key in
- what is error e0
keywords:
- e0
- safety key
- tether
- safety module
- 12v loop
- safety switch loop
- main control wire
- will not start
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016
  applies_to:
  - tt8-2016
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- tt8-2016-e1-error-code
- tt8-2016-e2-error-code
- tt8-2016-e3-error-code
- tt8-2016-e4-error-code
- tt8-2016-e5-error-code
- tt8-2016-e6-error-code
- tt8-2016-e7-error-code
see_also:
- tt8-2016-error-code-list
- tt8-2016-maintenance-menu
source:
  ref: sole-tm-tt8-2016-service-manual
  locator: Section 8.1, pages 38-39
  extracted_at: '2026-09-04'
---

**DC model: TT8 2016 ST925-YT021, DC drive motor. The AC inverter TT8 2016 (ST925A-YT030) is a different machine and this card does not apply to it.**

**This is E0, not E1 (no RPM signal) and not E6 (lower controller).**

Table definition: "Safety keys dose not insert the safety module. Or safety module is broken."

Full definition: console is not inserted safety, or safety module may be broken. Or else a component of
the upper control board or lower controller is broken.

Cause: with no safety key the console does not form a **+12 V loop** (safety switch loop), so E0 appears.
The lower controller sends the +12 V signal through the S/W line of the main control wire to the upper
control board to close that loop, so a broken main control wire or a failed lower controller component
produces E0 as well.

| Part | Troubleshooting |
|---|---|
| Safety module | Insert the safety key, then use a multi-meter on the short-circuit range to check whether the safety module wires are short or not. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before the hardware.** Remove the safety key, press STOP & START & ENTER and
insert the safety key at the same time to reach ENGINEERING MODE. Use FAST/SLOW or UP/DOWN to find
"functions", ENTER into DISPLAY MODE, then ENTER to choose on or off. "Off" means the display goes off
after the safety key is removed; "on" means the display stays on and shows E0.
