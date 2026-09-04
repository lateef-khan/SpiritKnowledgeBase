---
id: s77-2019-e2-over-current
title: 'E2: the lower board tripped on over current'
kind: troubleshooting
question: What does E2 mean on a Sole S77-2019 treadmill?
asked_as:
- e2 error on my treadmill
- s77 keeps showing e2
- over current error on my treadmill
keywords:
- e2
- over current
- limit led
- silicone oil
- lubrication
- lower control board
- motor
- blocked belt
facets:
  brand:
  - sole
  product_line: treadmill
  model: s77-2019
  applies_to:
  - s77-2019
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- s77-2019-e0-safety-key
- s77-2019-e1-no-rpm-signal
- s77-2019-e3-incline-vr
- s77-2019-e4-motor-power-wire
see_also:
- s77-2019-controller-led-debugging
- sole-lubricate-running-belt
- sole-e2-error
source:
  ref: sole-tm-s77-2019-service-manual
  locator: 'Section 8.2 Error Message: E2/OVER CURRENT, page 44'
  extracted_at: '2026-09-04'
---

**This is E2, not E3 (incline) and not E7 (input power).**

**Meaning**: the lower board detected over current, so it lit its LED and put `E2` on the display. It is protecting itself and the motor from burning out.

**Fix, in the manual's order**

1. Check whether silicone oil has been applied between the belt and the running board. If not, lubricate.
2. Do not block the belt while the treadmill is being used.
3. If neither of those is the cause, replace the lower control board or replace the motor.

The manual links a video for this code: `https://www.youtube.com/watch?v=ak_raMb_6vY&t=1s`.

The controller's **LIMIT current** LED is the same protection seen from the board: it lights when the lower board detects over current. **This manual gives no current threshold**; the earlier ST725 manual gives 18 A on a 220 Vac machine and 28 A on a 120 Vac machine.
