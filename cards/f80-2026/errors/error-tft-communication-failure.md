---
id: f80-2026-error-tft-communication-failure
title: Console shows ERROR
kind: troubleshooting
question: What does the plain ERROR message mean on a Sole F80-2026 treadmill?
asked_as:
- my treadmill just says error
- treadmill screen shows error with no number
- sole treadmill error message no code
keywords:
- error message
- tft electronic watch
- communication failure
- damaged
- 2 minutes
- power cycle
- touchscreen
- no code
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2026
  applies_to:
  - f80-2026
  section: errors
  code: error
authority: 3
not_to_be_confused_with:
- f80-2026-e23-tft-led-communication
- f80-2026-e22-led-control-board-communication
see_also:
- f80-2026-error-code-list
- f80-2026-using-led-console-when-tft-fails
source:
  ref: sole-tm-f80-2026-owners-manual
  locator: page 33, Service Checklist - Diagnosis Guide
  extracted_at: '2026-09-04'
---

**This is the word ERROR on its own, not E01 and not any numbered code.**

**Meaning:** TFT electronic watch communication failure.

**Solution / cause, as printed:**

1. **Check whether the TFT electronic watch is damaged.**
2. **After 2 minutes of power failure, power it on again.**

**On the printed message.** The problem column of this row reads "Console ERROR" followed by a stray arrow
glyph, which `pdftotext` rendered as "ERROR<-". The manual gives no other spelling of this message, so this
card files it under the code `error`.

**How it differs from E23.** E23 is a communication error between the TFT and the LED watch and its list
starts with the cable between them. This message is a TFT communication failure with no cable check at all.
