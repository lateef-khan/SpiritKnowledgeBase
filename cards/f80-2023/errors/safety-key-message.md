---
id: f80-2023-safety-key-message
title: PLEASE REPLACE THE SAFETY KEY on the display
kind: troubleshooting
question: Why does a Sole f80-2023 treadmill display PLEASE REPLACE THE SAFETY KEY?
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
  model: f80-2023
  applies_to:
  - f80-2023
  section: errors
  code: safety-key
authority: 3
not_to_be_confused_with:
- f80-2023-e1-no-rpm-signal
see_also:
- f80-2023-error-code-list
- sole-safety-key-not-detected
source:
  ref: sole-tm-f80-2023-service-manual
  locator: 'Section 8.1 Error Message: PLEASE REPLACE THE SAFETY KEY, pages 32-33'
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
