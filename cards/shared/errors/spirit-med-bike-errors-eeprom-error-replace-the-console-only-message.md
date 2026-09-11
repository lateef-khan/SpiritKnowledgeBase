---
id: spirit-med-bike-errors-eeprom-error-replace-the-console-only-message
title: EEPROM error on the rehabilitation bike gets one line - replace the console
  - and is the only error message the books admit to
kind: troubleshooting
question: What does EEPROM error mean on a Spirit Medical 7.0R or 7.0U bike?
asked_as:
- 7.0r shows eeprom error
- eeprom error on my rehab bike
- is there a list of error codes for the 7.0u
- spirit medical bike error message
keywords:
- eeprom error
- replace console
- only error message
- error code
- rehabilitation bike
- medical bike
- mr490
- mu470
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 70r-2021
  - 70r-2025
  - 70u-2025
  section: errors
  code: eeprom-err
authority: 3
not_to_be_confused_with:
- spirit-med-bike-errors-eeprom-err-start-stop-fan-three-seconds-then-console
- cs800-2024-errors-eeprom-error-replace-the-console
- spirit-bike-errors-eeprom-err-replace-upper-controller
see_also:
- spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply
- spirit-med-bike-errors-programs-do-not-start-key-test-then-keypad
source:
  ref: spirit-bike-70r-2025-owners-manual
  locator: ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48 (printed 46); text.md lines
    1328-1377; 7.0U 2025 owner's manual ERROR MESSAGE & TROUBLESHOOTING, PDF p. 46
    (printed 44); text.md lines 1285-1329; Dyaco MED 7.0R 2021 owner's manual (Rev.
    1.2.1) Error messages and Troubleshooting, PDF p. 84-85; text.md lines 2642-2730;
    7.0R (MR490-SB018-03) service manual 5.2.2 Error Code, PDF p. 8, text.md lines
    92-120; 7.0U (MU470-SB018) service manual 5.2.2 Error Code, PDF p. 8, text.md
    lines 143-171
  extracted_at: '2026-09-11'
---

**This is the 7.0R/7.0U `EEPROM error`, and every book that prints it - three owner's manuals and two service manuals - gives the same one line:**

> EEPROM error: Solution for this is to replace the console (Note: this is the only error message)

The service manuals say it as *EEPROM Error - Replace the console when the error code shows. This is the only error code for this unit.*

**No key sequence, no reset, no board.** The 4.0R and 4.0U of the same range clear the same message with a three-key hold before the part is replaced (`spirit-med-bike-errors-eeprom-err-start-stop-fan-three-seconds-then-console`); these two do not. The 7.0S/7.5S rehabilitation steppers print the identical line (`cs800-2024-errors-eeprom-error-replace-the-console`) - and there "the only error message" is contradicted by a `Motor Error` on the next line; on these bikes it is true, no other message is printed anywhere in the five books.

**The Dyaco MED 7.0R 2021 edition (Rev. 1.2.1) prints the same line under the heading *Error messages*** on the page before its troubleshooting list, so the message pre-dates the Spirit cover.

Everything else the console can do wrong is a symptom row, not a message: no power, programs do not start, no data when pedalled, symmetry wrong, resistance wrong - each its own card, linked from `spirit-med-bike-errors-no-power-90-to-240-vac-fuse-12-vdc-at-the-console-then-24-vdc-supply`.

