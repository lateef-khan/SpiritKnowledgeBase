---
id: f89-2023-safety-key-message
title: PLEASE REPLACE THE SAFETY KEY on the display
kind: troubleshooting
question: Why does a Sole f89-2023 treadmill display PLEASE REPLACE THE SAFETY KEY?
asked_as:
- treadmill says please replace the safety key
- console asking for the safety key
- safety key message will not go away
keywords:
- safety key
- please replace the safety key
- safety module
- main control wire
- display board
- 12v loop
- console message
facets:
  brand:
  - sole
  product_line: treadmill
  model: f89-2023
  applies_to:
  - f89-2023
  section: errors
  code: safety-key
authority: 3
not_to_be_confused_with:
- f89-2023-e1-no-rpm-signal
see_also:
- f89-2023-error-code-list
- sole-safety-key-not-detected
source:
  ref: sole-tm-f89-2023-service-manual
  locator: 'Section 8.1 Error Message: PLEASE REPLACE THE SAFETY KEY, pages 33-34'
  extracted_at: '2026-09-04'
---

**This is the missing safety key message, not an E code.** This console prints no E0.

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

**The socket for the Safety Key module connector is on the Android 10 console board.** The manual shows it in a photograph.

**Check the software setting before the hardware.** Remove the safety key, press STOP, START and ENTER, and insert
the safety key at the same time. The display enters ENGINEERING MODE. Press FAST/SLOW or UP/DOWN to find
"functions", press Enter for "DISPLAY MODE", then press Enter to choose on or off. "off" means the display goes
off after the safety key is removed. "on" means the display stays on and shows PLEASE REPLACE THE SAFETY KEY
after the key is removed.

**The manual contradicts itself here.** This note reaches ENGINEERING MODE with the STOP, START and ENTER keys,
but section 8.10 of the same manual reaches it by pressing the word "Settings" ten times on the touchscreen, and
section 4.4 lists no ENTER key on this console. Treat the touchscreen route as the one to try first.
