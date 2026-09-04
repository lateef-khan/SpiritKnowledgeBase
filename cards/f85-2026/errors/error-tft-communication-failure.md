---
id: f85-2026-error-tft-communication-failure
title: The plain ERROR message and touchscreen communication failure
kind: troubleshooting
question: What does the plain ERROR message mean on an F85-2026 treadmill?
asked_as:
- my treadmill just says error
- treadmill screen says error with no number
- touchscreen communication failure on my treadmill
keywords:
- error message
- tft electronic watch
- communication failure
- touchscreen
- damaged display
- power cycle
- two minutes
- no code number
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2026
  applies_to:
  - f85-2026
  section: errors
  code: error
authority: 3
not_to_be_confused_with:
- f85-2026-e23-tft-to-led-communication
see_also:
- f85-2026-e23-tft-to-led-communication
- f85-2026-led-fallback-when-tft-fails
- f85-2026-error-message-table
source:
  ref: sole-tm-f85-2026-owners-manual
  locator: page 33, Error Messages, Console ERROR
  extracted_at: '2026-09-04'
---

**This row has no code number. The console shows the word ERROR, not E01 or E03 or any other numbered code.**

**Meaning.** TFT electronic watch communication failure — the touchscreen board is not communicating.

1. **Check whether the TFT electronic watch is damaged.**
2. **After 2 minutes of power failure, power it on again** — leave it unplugged for two minutes before powering
   back up.

**E23 is the related but different fault**: E23 is a communication error *between* the touchscreen and the LED
display, and it names cables to check. This plain ERROR row names only the touchscreen board itself.

If the touchscreen is dead, the manual's documented workaround is to unplug the TFT connection cable and operate
the machine from the LED display alone.
