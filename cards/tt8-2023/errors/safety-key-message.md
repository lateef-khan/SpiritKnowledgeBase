---
id: tt8-2023-safety-key-message
title: Display reads PLEASE REPLACE THE SAFETY KEY
kind: troubleshooting
question: Why does my Sole tt8-2023 treadmill say PLEASE REPLACE THE SAFETY KEY?
asked_as:
- console says replace the safety key
- treadmill wont start says safety key
- please replace the safety key message
keywords:
- safety key
- tether
- safety module
- 12v loop
- safety switch loop
- android console
- will not start
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2023
  applies_to:
  - tt8-2023
  section: errors
  code: please-replace-the-safety-key
authority: 3
not_to_be_confused_with:
- tt8-2023-e1-error-code
see_also:
- tt8-2023-error-code-list
- tt8-2023-display-mode-setting
source:
  ref: sole-tm-tt8-2023-service-manual
  locator: Section 8.1, pages 35-36 of 69
  extracted_at: '2026-09-04'
---

**TT8 2023 ST738-YT066, DC drive motor.**

**This is the words PLEASE REPLACE THE SAFETY KEY, not a numbered E code.** This console has no E0.

Definition: console is not inserted safety, or safety module may be broken. Or else component of upper
control board or lower controller is broken.

Cause: the safety key is not inserted, so the console does not form a **+12 V loop** (safety switch loop).
The lower controller sends the +12 V signal through the S/W line of the main control wire to the upper
control board to close that loop, so a broken main control wire or a failed lower controller component
gives the same message.

The safety key module connector plugs into a socket on the **Android 10 console board**.

| Part | Troubleshooting |
|---|---|
| Safety module | Insert the safety key, then use a multi-meter on the short-circuit range to check whether the safety module wires are short or not. |
| Main control wires | Reinsert the main control wire. Replace the main control wire. |
| Display board | Replace the upper control board. |

**Check the software setting before the hardware.** Remove the safety key, press STOP & START & ENTER and
insert the safety key at the same time to reach ENGINEERING MODE. Use FAST/SLOW or UP/DOWN to find
"functions", ENTER into DISPLAY MODE, then ENTER to choose on or off. "Off" means the display goes off when
the safety key is removed; "on" means the display stays on and shows PLEASE REPLACE THE SAFETY KEY.
