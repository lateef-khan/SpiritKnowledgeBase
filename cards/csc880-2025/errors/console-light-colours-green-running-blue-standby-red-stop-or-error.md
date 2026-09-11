---
id: csc880-2025-errors-console-light-colours-green-running-blue-standby-red-stop-or-error
title: The console and handrail lights read green for running, blue for standby, and
  red for stop, emergency, or an error code
kind: fact
question: What do the green, blue and red lights on a Spirit csc880-2025 stair climber
  mean?
asked_as:
- my stair climber lights are red what does it mean
- csc880 console glowing blue
- what colour should the climber handrail lights be
keywords:
- light colour
- green light
- blue light
- red light
- standby
- emergency
- error code
- handrail light
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: '*'
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with: []
see_also:
- csc880-2025-errors-error-code-table
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
source:
  ref: spirit-climber-csc880-2025-service-manual
  locator: 4. Working Principle, the three console photographs on PDF p. 6 (a flat
    picture with no text layer; the page was read from a 200 dpi render, and the OCR
    supplement at text.md lines 404-414 misses the blue caption)
  extracted_at: '2026-09-11'
---

The service manual prints three photographs of the console and handrails, each lit a different colour, with one caption each:

| Light colour | Caption as printed | What the console shows in the photo |
|---|---|---|
| **Green** | Green Light - RUNNING | A workout in progress, profile bars lit |
| **Blue** | Blue light - Standby | The idle screen with a large `2` in the centre |
| **Red** | Red Light - STOP/EMERGENCY /OR ERROR CODE | Text in the centre window where a code would be |

**The lights are a status colour, not a fault list.** The ring around the console's centre key and the light bars on both handrails change together: green while the steps run, blue while the machine waits, red whenever it has stopped - for a stop key, for either emergency stop, or for a code. So a **red machine is not necessarily a faulty one**; it is a stopped one. Read the centre window to find out which: an `ER` code has its own card (`csc880-2025-errors-error-code-table`), the word `Safe` is the swapped stop-switch wiring (`csc880-2025-errors-safe-in-the-display-emergency-stop-wiring`), and a plain stop shows no code at all.

**That is all the book says.** No blink pattern, no fourth colour and no way to change the colours is printed, and the owner's manual for this machine does not describe the lights at all. The 8.5S recumbent stepper's beacon uses colours to show workout *progress* instead - a different scheme on a different product.
