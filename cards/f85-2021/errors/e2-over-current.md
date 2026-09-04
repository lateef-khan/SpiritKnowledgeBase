---
id: f85-2021-e2-over-current
title: 'E2: over current on the lower board'
kind: troubleshooting
question: What does E2 mean on a Sole F85-2021 treadmill and how do I fix it?
asked_as:
- e2 error on my treadmill
- treadmill keeps showing e2
- over current error on the console
keywords:
- e2
- over current
- lower control board
- silicone oil
- lubrication
- motor
- error code
- limit led
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2021
  applies_to:
  - f85-2021
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- f85-2021-e0-safety-key-message
- f85-2021-e1-no-rpm-signal
- f85-2021-e3-incline-vr-error
- f85-2021-e4-motor-power-wire-error
- f85-2021-e5-communication-error
- f85-2021-e6-lower-controller-error
- f85-2021-e7-input-power-error
see_also:
- f85-2021-driver-board-leds
- f85-2021-belt-deck-lubrication
- sole-e2-error
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: 'section 8.3 Error Message: E2 / OVER CURRENT, printed page 50'
  extracted_at: '2026-09-04'
---

**This is E2, not E1 (no RPM signal) and not E3 (incline).**

| Field | Value |
|---|---|
| Code | E2 |
| Cause, as printed | Over current, over limit current of lower controller and motor. |
| Definition | When lower board detect over current, then display light up and display appear "E2". |

The lower board is protecting itself and the motor so that neither burns out.

**How the manual says to solve it, in order:**

1. Check whether silicone oil has been smeared between the belt and the running board.
2. While the treadmill is in use, do not block the belt from running.
3. If neither of those clears it, replace the lower control board, or replace the motor.

The **LIMIT** LED on the driver board lights for the same condition, at 18A on a 220Vac system or 28A on a 120Vac system. See the driver board LED card.
