---
id: tt8-2019-e2-error-code
title: E2 over current on the controller
kind: troubleshooting
question: What does error E2 mean on a Sole tt8-2019 treadmill?
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
  model: tt8-2019
  applies_to:
  - tt8-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- tt8-2019-e0-error-code
- tt8-2019-e1-error-code
- tt8-2019-e3-error-code
- tt8-2019-e4-error-code
- tt8-2019-e5-error-code
- tt8-2019-e6-error-code
- tt8-2019-e7-error-code
see_also:
- tt8-2019-driver-board-led-debugging
- tt8-2019-error-code-list
source:
  ref: sole-tm-tt8-2019-service-manual
  locator: Section 8.3, page 44
  extracted_at: '2026-09-04'
---

**DC model: TT8 2019 ST928-YT035, DC drive motor. The AC inverter TT8 2019 (ST928A-YT037) is a different machine and this card does not apply to it.**

**This is E2, not E7 (input power) and not E1 (no RPM signal).**

Table definition: "Over current, over limit current of lower controller and motor."

Section definition: when the lower board detects over current the LED lights up and the display shows
"E2". The lower board is protecting itself and the motor from being burned.

To solve the over current:

1. Check whether **silicone oil** has been smeared on the deck or not.
2. While the treadmill is in use, do not block the running belt.
3. If neither clears it, replace the lower control board or replace the motor.

The driver board's **LIMIT** LED covers the same fault from the hardware side: it lights when motor
current exceeds **18 A on a 220 Vac system** or **28 A on a 120 Vac system**.
