---
id: crw800-2024-errors-e1-console-eeprom-failure
title: E1 on the rower is a console EEPROM failure, shown with RAM ERROR, and the
  service manuals say replace the console
kind: troubleshooting
question: What does E1 mean on a Spirit CRW800 or XRW600 rower?
asked_as:
- my spirit rower says e1
- what does e1 mean on a rowing machine console
- rower showing e1
keywords:
- e1
- eeprom
- console
- electronic desk
- memory
- rower
- error message code
- failure
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - xrw600-2019
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- crw800-2024-errors-e2-cable-tension-communication-error
- spirit-2024-errors-e1-no-speed-sensor-signal
- spirit-2024-errors-e1-drive-motor-no-output-signal
- cvc800-e-1-ram-error
- xt-2023-errors-e1-motor-not-responsive
see_also:
- crw800-2024-errors-e2-cable-tension-communication-error
- ce900-2025-errors-eeprom-error-replace-upper-controller
- cs800-2024-errors-eeprom-error-replace-the-console
- crw800h2o-console-shows-no-display
- sr500-2016-e1-eeprom-failure
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: ERROR CODES, printed page 34. That page is a flat picture with no text
    layer and was read from the rendered page; CRW800 2021 (800940) service manual
    7-1 Error Codes, PDF p. 31 (printed 30), text.md lines 412-421, and 7-3 Error
    Message, PDF p. 33-34 (printed 32-33), text.md lines 437-483; CRW800 2016 (CW800-YR001)
    service manual 8. Error Messages / Troubleshooting, PDF p. 31-33, text.md lines
    398-445; XRW600 (DW400-YR002) service manual 8. Error Messages / Troubleshooting,
    PDF p. 31-33, text.md lines 390-445
  extracted_at: '2026-09-10'
---

| Error Message Code | Problem Description |
|---|---|
| E1 | Console (Electronic Desk) EEPROM failure |

**That is the whole of what this manual says.** No definition of what the console does, no
troubleshooting column, and no part to replace. The table has two columns; the other Spirit
manuals' error tables have three.

**The CRW800 2024 is not the CRW800 H2O.** The water rower already in the repository prints no
codes at all - its faults are described as symptoms
(`crw800h2o-console-shows-no-display`, `crw800h2o-console-shows-no-data`). The two machines share a
name and nothing else here; do not answer one from the other.

**Every other Spirit machine that calls an EEPROM failure by name gives it a remedy, and this one
does not.** The CE800 2024, CE850 2024, CR800 2024, CU800 2024 and CE900 2025 family name the upper
controller (`ce900-2025-errors-eeprom-error-replace-upper-controller`), the CS800 2024 names the
console (`cs800-2024-errors-eeprom-error-replace-the-console`), the CES880 2025 names the display
board (`ces880-2025-errors-eeprom-error-replace-display-board`) and the CRS800S 2024 names the
display board under the heading `RAM ERROR`
(`crs800s-2024-errors-ram-error-replace-the-display-board`). All four end at the console assembly;
none of them is written for this machine.

Look-alike codes: `E1` on the 2024 treadmills is a speed or drive-motor signal fault
(`spirit-2024-errors-e1-no-speed-sensor-signal`,
`spirit-2024-errors-e1-drive-motor-no-output-signal`), and `E-1` on the Spirit CVC800 climber is the
display board RAM error (`cvc800-e-1-ram-error`).

## Three service manuals print the code with a symptom and a fix

**The CRW800 2016 (`CW800-YR001`), the CRW800 2021 (`800940`) and the XRW600 (`DW400-YR002`) service manuals all print the same two-row table** - `E1 | Console (Electronic Desk) EEPROM failure` (the XRW600 shortens it to `Console EEPROM failure`) - and then, unlike the 2024 owner's manual, say what it looks like and what to do:

> Error code: E1. When the screen displays "E1" "RAM ERROR" message, it means that the system console EEPROM failure, all functions are disabled. Troubleshooting: Replace the console (Electronic Desk).

So **the console shows the words `RAM ERROR` beside `E1`, every function stops, and the remedy is a new console.** The 2021 book's code row reads `Console (Electronic Desk) EEPROM failure`, as the 2024 owner's manual does; the 2016 book's is the same; the XRW600 drops the parenthesis. The only tool the chapter names is a multi-meter, and it is not used for this code.

**So the 2021 owner's manual's silence is not the machine's.** The CRW800 2021 owner's manual prints no code at all (`spirit-rower-errors-no-error-codes-printed`); its service manual prints this one and `E2`. A 2021 owner reporting `E1` has a real code with a real answer.

Sole's SR500 2016 prints the same code, message and remedy for its own rower: `sr500-2016-e1-eeprom-failure`.
