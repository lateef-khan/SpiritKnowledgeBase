---
id: cc81-console-data-ranges
title: "Display value ranges on the climber console"
kind: spec
question: "What are the display value ranges on a Sole CC81 climber?"
asked_as:
- "how many resistance levels does my sole climber have"
- "what is the max time on the climber console"
- "what does vertical mean on the cc81 display"
keywords:
- "display range"
- "working range"
- "resistance levels"
- "time"
- "steps"
- "calories"
- "pulse"
- "vertical"
- "climber"
facets:
  brand:
  - sole
  product_line: climber
  model: cc81
  applies_to:
  - cc81
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cc81-console-modes
- cc81-console-buttons
source:
  ref: sole-climber-cc81-service-manual
  locator: "Sections 4-1 Display Windows and 4-3 Functions"
  extracted_at: '2026-09-03'
---

The console is a **5.5" LCD display**.

| Value | Display range | Working range | Note |
|---|---|---|---|
| TIME | 0:00 to 99:99 | 0:00 to 99:59 (min:sec) | Count up by default. Count down once the user sets a time. Count down setup range is 10:00 to 99:00. |
| TOTAL STEPS | 0 to 99999 | 0 to 99999 | The manual calls this "the current distance in steps". |
| CALORIES | 0 to 9999 | 0 to 9999 | Cumulative for the workout. |
| LEVEL | 0 to 99 | 1 to 20 | Current resistance level. |
| PULSE | 0 to 999 | 40 to 220 BPM | Needs a receiver, and the user must wear a chest belt. |
| VERTICAL | 0 to 99999 | 0 to 99999 | Height, in FT or MTR. |

**Two things printed oddly in the source.** The TIME row gives a display range of 99:99, which is not a valid minute:second reading; it is copied exactly as printed. The vertical row is spelled "VIRTICAL" in the manual.
