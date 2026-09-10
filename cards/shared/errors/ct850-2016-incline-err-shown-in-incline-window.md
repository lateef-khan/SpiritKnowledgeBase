---
id: ct850-2016-incline-err-shown-in-incline-window
title: The incline window displays INCLINE ERR
kind: troubleshooting
question: What do I do when the incline window shows INCLINE ERR on a Spirit CT800ENT-2024,
  CT850 or CT850ENT-2024 treadmill?
asked_as:
- incline err on my spirit treadmill
- treadmill display says incline error
- how to clear incline err
keywords:
- incline err
- incline error
- position sensor
- incline motor
- calibrate
- reboot
- incline window
- vr
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2024
  - ct850-2016
  - ct850-2020
  - ct850ent-2024
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-during-incline-action
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-incline-err
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 8.3 Troubleshooting procedure matrix, pages 49-52 of the CT850
    2016 manual (printed 48-51); the same row is section 8-7, pages 47-51 of the CT850
    2020 manual (printed 46-50)
  extracted_at: '2026-09-08'
---

This is the one-line matrix row. Both manuals print it identically.

| Condition | Reason | Solve |
|---|---|---|
| INCLINE ERR, INCLINE window displays "INCLINE ERR" | Position sensor value of incline motor is wrong | 1. Turn off the AC switch and turn on power again. 2. Calibrate the monitor. |

The manuals also carry a full section on this message, and the two manuals do not define it the same
way. The 2016 manual defines `INCLINE ERR` twice, with two different meanings
(`ct850-2016-incline-err-vr-out-of-range` and `ct850-2016-incline-err-during-incline-action`). The
2020 manual splits the same pair into the code `E3` and the message `INCLINE ERR`
(`ct850-2020-e3-incline-motor-cannot-work` and `ct850-2020-incline-err`).

**The CT800ENT 2024 and CT850ENT 2024 owner's manuals print this row word for word** in the
Condition/Reason/Solve matrix on printed pages 57 to 59. Both of those pages are flat pictures
with no text layer and were read from the rendered page.

Neither 2024 ENT manual carries a full section on the message; the one-line matrix row is all
either of them says about it. **The CT850ENT 2024 does print `E3` in its error code table** for the
same incline motor, with a different remedy again - see `ct850-2020-e3-incline-motor-cannot-work`.
The CT800ENT 2024's table prints `E3` too, with a remedy of its own:
`spirit-2024-errors-e3-incline-motor-did-not-work-correctly`.
