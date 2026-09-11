---
id: ct850-2016-incline-err-shown-in-incline-window
title: The incline window displays INCLINE ERR
kind: troubleshooting
question: What do I do when the incline window shows INCLINE ERR on a Spirit CT800,
  CT800ENT-2024, CT850, CT850ENT-2024, CT900ENT or 4.0T treadmill?
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
  - 40t-2026
  - ct800-2016
  - ct800-2020
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2016
  - ct850-2020
  - ct850ent-2022
  - ct850ent-2024
  - ct900ent
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-incline-err-vr-out-of-range
- ct850-2016-incline-err-during-incline-action
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-incline-err
- spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Section 8.3 Troubleshooting procedure matrix, pages 49-52 of the CT850
    2016 manual (printed 48-51); the same row is section 8-7, pages 47-51 of the CT850
    2020 manual (printed 46-50); CT800 2016 service manual 8.4 Troubleshooting procedure
    matrix, PDF p. 56-59 (printed 55-58), text.md lines 1076-1215; CT800 2020 service
    manual 8-6 Troubleshooting procedure matrix, PDF p. 46-50 (printed 45-49), text.md
    lines 660-797; CT800ENT 2022 service manual 8-6 Troubleshooting procedure matrix,
    PDF p. 36-38, text.md lines 685-791; CT850ENT 2022 service manual 8-6 Troubleshooting
    procedure matrix, PDF p. 37-39, text.md lines 704-810; CT900ENT service manual
    Troubleshooting procedure matrix, PDF p. 45-48, text.md lines 691-842; 4.0T 2026
    service manual Condition / Reason / Solve matrix, PDF p. 36-38 (printed 47-49),
    text.md lines 566-689; the 4.0T ST8700A-ST026-01 service manual (spirit-treadmill-40t-2026-service-manual-st8700a,
    88% the ST017 book) prints the same page one page later, word for word (compared
    with difflib on 2026-09-11): Condition / Reason / Solve matrix at PDF p. 37-39
    (printed 47-49), text.md lines 635-758'
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
`spirit-2024-errors-e3-incline-motor-wires-then-calibration`.

**Six more service manuals print this row word for word**: the CT800 2016, CT800 2020, CT800ENT 2022, CT850ENT 2022, CT900ENT and 4.0T. The XT and CT1000ENT books print the row for the code `E3` in the incline window, with a different first step (`spirit-xt-errors-incline-window-shows-e3-connector-then-calibrate`, `spirit-xt-2015-errors-incline-window-shows-e3-power-cycle-then-calibrate`). The CT900 prints it for `INCLINE E33`.
