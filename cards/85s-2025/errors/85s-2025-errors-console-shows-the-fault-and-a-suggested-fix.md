---
id: 85s-2025-errors-console-shows-the-fault-and-a-suggested-fix
title: The stepper touchscreen puts the fault and a suggested fix on the screen, and
  the book lists no codes to look up
kind: fact
question: What does the console of a Spirit 85s-2025 recumbent stepper show when something
  goes wrong?
asked_as:
- my stepper touchscreen is showing a warning
- where is the error code list for the 8.5s
- what does the message on my spirit stepper screen mean
- spirit stepper error code list
keywords:
- error message
- possible solution
- touchscreen
- no error code
- fault message
- on screen
- console message
- troubleshooting
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: errors
  code: no-code
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- 80t-2026-errors-console-shows-message-with-solution
- csc880-2025-errors-error-code-table
- csc900-2024-errors-error-code-table
see_also:
- spirit-climber-errors-no-error-codes-printed
- 80t-2026-errors-console-shows-message-with-solution
- 85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc
- 85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version
- 85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap
- spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm
source:
  ref: spirit-climber-85s-2025-owners-manual
  locator: POWER ON & CONSOLE OPERATION, the NOTE box, printed page 28 (PDF page 30);
    also present in the OCR supplement for that page; 8.5S (MS2000-SB036-01) service
    manual 4-2 Maintenance Mode (the Error Log item), PDF p. 8-11, text.md lines 99-186,
    and 5. Troubleshooting (Electronic), PDF p. 16-21, text.md lines 216-305
  extracted_at: '2026-09-10'
---

The manual's note, word for word:

> **NOTE:** If there is an issue, the console will show an error message along with a possible
> solution. Follow the message to resolve the issue.

**The screen is the answer.** This console states the fault in words and suggests what to do, so
there is nothing to look up. The manual prints **no error code table, no fault code and no
troubleshooting chapter**, and its contents page has no Troubleshooting entry - it runs Machine Care
56, Specifications 59, Exploded View 61, Warranty 63 and stops.

**Do not hand this owner a code list from another Spirit machine.** The stair climbers use `ER01` to
`ER12` (`csc880-2025-errors-error-code-table`, `csc900-2024-errors-error-code-table`), the LCD
steppers use `EEPROM ERROR`, `MOTOR ERROR`, `RAM ERROR` and `Err`, and none of them is what this
console displays.

**The 8.5S-FIT 2026 does not print this note.** Its book has no troubleshooting section either, but it
carries no sentence about on-screen messages at all - the words *error*, *fault* and *troubleshooting*
appear nowhere in it. See `spirit-climber-errors-no-error-codes-printed`.

The Spirit 8.0T 2026 treadmill carries the same note in the same words on a different product line:
`80t-2026-errors-console-shows-message-with-solution`.

## The service manual adds an Error Log and three electronic procedures

**The 8.5S service manual (`MS2000-SB036-01`) does not print a code table either**, but it does two things the owner's manual does not. Its Maintenance Mode - entered by tapping the Wi-Fi icon once and the clock in the status bar six times on the Home Screen - has a **Service > Error Log** item that *displays the history of system errors*, which is where a technician reads back what the screen showed. And its `5. Troubleshooting (Electronic)` chapter prints three procedures: no power with a 24 V and 12 V chain (`85s-2025-errors-no-power-console-does-not-light-24-vdc-then-12-vdc`), a **`UART Communication Error`** message with a cable check and a software-version check (`85s-2025-errors-uart-communication-error-cables-103-and-104-then-software-version`), and no revolutions - the step sensor and the angle sensor (`spirit-med-stepper-errors-left-right-step-graph-incorrect-step-sensor-5-volts-and-7-to-9-mm`, `85s-2025-errors-no-data-when-pedaled-angle-sensor-5-volts-and-3-mm-magnet-gap`). `UART Communication Error` is the one message the service manual names in words.
