---
id: spirit-2024-errors-e7-abnormal-ac-input-voltage
title: E7 is an abnormal AC input voltage, and the check is a stable 100 to 120 volt
  supply
kind: troubleshooting
question: What does E7 mean on a Spirit CT800-2020, CT800-2024, CT800ENT-2022 or CT800ENT-2024
  treadmill?
asked_as:
- what does e7 mean on my spirit treadmill
- treadmill showing e7
- how do i fix e7 on a spirit treadmill
keywords:
- e7
- ac input voltage
- mains voltage
- wall socket
- supply voltage
- unstable
- brown out
- error code
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct800-2024
  - ct800ent-2022
  - ct800ent-2024
  - ct850-2020
  section: errors
  code: e7
authority: 3
not_to_be_confused_with:
- ct850-2020-e-01h-abnormal-ac-input-voltage
- ct850-2020-e-23h-low-voltage
- f85-2019-e7-input-power-error
- spirit-2024-errors-e4-drive-motor-input-voltage-abnormal
see_also:
- spirit-2024-errors-seven-code-table-with-no-hyphen
source:
  ref: spirit-treadmill-ct800-2024-owners-manual
  locator: ERROR CODES, printed page 42 of the CT800 2024 owner's manual and printed
    page 60 of the CT800ENT 2024 owner's manual. Both pages are flat pictures with
    no text layer and were read from the rendered page; CT800 2020 service manual
    8-1 Error Codes, PDF p. 35 (printed 34), text.md lines 467-474; CT800ENT 2022
    service manual 8-1 Error code items, PDF p. 31, text.md lines 574-599; spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 1 (DC list headed "ERROR MESSAGE of New CT800&CT850(2020)")
  extracted_at: '2026-09-10'
---

| Field | CT800 2024 | CT800ENT 2024 |
|---|---|---|
| Cause | Abnormal AC input voltage. | The AC input voltage is abnormal. |
| Solution | Check the AC input voltage is stable 100~120V. | Check whether the wall socket provides a stable voltage of about 100~120V. |

The figure is **100~120V** in both books, and it is the wall supply, not the motor supply. The
motor's own supply has its own code, `E4`
(`spirit-2024-errors-e4-drive-motor-input-voltage-abnormal`).

**The CT850 2024 and CT850ENT 2024 print this same cause and this same figure under a different code
string** - `E-01H` in their twenty-three-code inverter table
(`ct850-2020-e-01h-abnormal-ac-input-voltage`). One family, two consoles, two names for one fault.
Do not offer `E7` to a CT850 caller or `E-01H` to a CT800 caller.

**The 100 volt floor here disagrees with the same manual's own troubleshooting page.** The CT800
2024's diagnosis table demands *a minimum of 120 volt AC* for a belt that caps near 7 mph, and its
`Display does not light` row names a 230 VAC outlet - three supply figures in one book. See
`ct800-2020-errors-speed-caps-at-7-mph` and
`spirit-2024-errors-display-does-not-light-230-vac-outlet`.

Sole's F85 uses `E7` for an input power error (`f85-2019-e7-input-power-error`).

**The two service manuals print these rows word for word.** The CT800 2020 service manual's 8-1 Error Codes table carries the CT800 2024 wording, and the CT800ENT 2022 service manual's 8-1 Error code items table carries the CT800ENT 2024 wording, so both readings of E7 are two generations old.

**A Spirit service bulletin on the CT800 #800840 (`spirit-treadmill-ct800-2020-e50h-service-bulletin`) photographs an error card headed *ERROR MESSAGE of New CT800&CT850(2020)* that lists this code under *For D/C Motor Controlling System*.** Its wording is shorter than either manual's: *E7: Abnormal voltage input to control board from house power.*. On the strength of that heading the card carries both the CT800 2020 and the CT850 2020; note that the CT850 2020 service manual itself prints only the twenty-three `E-xxH` inverter codes and no DC-controller list (`ct850-2020-inverter-error-code-list`), so for the CT850 2020 this code rests on the bulletin's heading alone.
