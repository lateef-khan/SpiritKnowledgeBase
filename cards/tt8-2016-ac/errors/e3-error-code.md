---
id: tt8-2016-ac-e3-error-code
title: E3 rear incline motor error on the inverter machine
kind: troubleshooting
question: What does error E3 mean on a Sole tt8-2016-ac treadmill?
asked_as:
- e3 on my treadmill
- rear incline motor error
- grade shows e3 on the console
keywords:
- e3
- rear incline motor
- incline motor transfer board
- vr wire
- incline error
- inverter
- adapter board
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016-ac
  applies_to:
  - tt8-2016-ac
  section: errors
  code: e3
authority: 3
not_to_be_confused_with:
- tt8-2016-ac-e-50h-error-code
- tt8-2016-ac-e-51h-error-code
- tt8-2016-ac-e-52h-error-code
- tt8-2016-ac-e-53h-error-code
- tt8-2016-e3-error-code
see_also:
- tt8-2016-ac-error-code-list
- tt8-2016-ac-rear-incline-motor-replacement
source:
  ref: sole-tm-tt8-2016-ac-service-manual
  locator: Section 8.1 Error Message / Troubleshooting, pages 36-38
  extracted_at: '2026-09-04'
---

**AC model: TT8 2016 ST925A-YT030, AC drive motor driven by an inverter. The DC drive motor TT8 2016 (ST925-YT021) is a different machine and this card does not apply to it.**

**On this machine E3 means the rear incline motor.** It is not E-53H, which is the *front* incline motor,
and it is not the E3 of the DC-motor TT8 2016 (ST925-YT021), where E3 means the incline VR voltage is
out of range. Same two characters, three different faults across the TT8 range — check which machine you
are standing at before you act.

Printed description: "Machine (rear) incline motor error"

Troubleshooting, in the manual's order:

1. Check whether the VR wire of the incline motor is connected or bad in contact **with the incline motor
   transfer board**.
2. Check whether the power wire of the incline motor is connected or bad in contact **with the incline
   motor transfer board**.
3. Check if the incline motor is lock dead or bad in contact.
4. Replace the incline motor transfer board.
5. Replace the incline motor.

Note that the fix list for E3 never asks you to replace the inverter — the rear incline motor hangs off its
own transfer board, not off the inverter.
