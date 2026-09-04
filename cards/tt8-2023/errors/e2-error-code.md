---
id: tt8-2023-e2-error-code
title: E2 over current on the controller
kind: troubleshooting
question: What does error E2 mean on a Sole tt8-2023 treadmill?
asked_as:
- e2 over current on treadmill
- my treadmill keeps showing e2
- what does e2 mean
keywords:
- e2
- over current
- overcurrent
- limit
- lubricant
- silicone oil
- belt friction
- controller
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2023
  applies_to:
  - tt8-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- tt8-2023-safety-key-message
- tt8-2023-e1-error-code
- tt8-2023-e3-error-code
- tt8-2023-e4-error-code
- tt8-2023-e5-error-code
- tt8-2023-e6-error-code
- tt8-2023-e7-error-code
see_also:
- tt8-2023-error-code-list
source:
  ref: sole-tm-tt8-2023-service-manual
  locator: Section 8.3, page 41 of 69
  extracted_at: '2026-09-04'
---

**TT8 2023 ST738-YT066, DC drive motor.**

**This is E2, not E7 (input power) and not E1 (no RPM signal).**

Definition: when the controller detects that the operating current for the drive motor is above standard,
the display lights up and shows "E2". The controller is protecting itself and the drive motor from damage.

The usual cause is the **running belt needing lubricant, or its bottom fibre being worn seriously and
needing replacement**. A dried or worn belt raises friction against the deck, and the controller has to
supply more current to hold speed.

1. Lubricate the bottom of the running belt as the owner's manual describes.
2. If that does not clear it, the belt is worn out — replace the running belt. That returns the drive
   motor's operating current to normal.
3. If E2 still occurs with a new belt, either the controller or the drive motor is defective. **The drive
   motor is a passive component and is the less likely of the two, so replace the controller first.**
