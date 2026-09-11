---
id: spirit-med-bike-errors-touchscreen-console-shows-the-message-and-the-fix
title: The touchscreen bike console writes the fault and a possible solution on the
  screen, and the owner's manual prints no code list; the service manual prints four
  procedures
kind: fact
question: What does the console of a Spirit Medical 8.0U or 8.5R bike show when something
  goes wrong, and where is the error code list?
asked_as:
- my 8.0u screen is showing a warning message
- where is the error code list for the 8.5r
- what does the message on the rehab bike touchscreen mean
- spirit medical bike error message with a solution
keywords:
- error message
- possible solution
- touchscreen
- no error code
- fault message
- console message
- no troubleshooting page
- medical bike
- self-test
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-error-code-table
- 80t-2026-errors-inverter-error-code-table-48-rows
- spirit-commercial-bike-errors-no-error-codes-printed
see_also:
- 85ue-2025-errors-console-shows-the-message-and-the-fix
- 85s-2025-errors-console-shows-the-fault-and-a-suggested-fix
- 80t-2026-errors-console-shows-message-with-solution
- spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc
- spirit-med-bike-errors-uart-communication-error-cables-089-and-090-then-software-version-v255a255
source:
  ref: spirit-bike-80u-2025-owners-manual
  locator: 8.0U 2025 owner's manual POWER ON & CONSOLE OPERATION, the NOTE box, PDF
    p. 23 (printed 21), text.md lines 592-625; 8.5R 2025 owner's manual the same NOTE,
    PDF p. 28 (printed 26), text.md lines 753-786. Absence checked 2026-09-11 over
    the full text, the contents page (PDF p. 3) and every page's 300 dpi render of
    both books; whole-word counts of troubleshooting and fault 0, error 2 (this NOTE
    and its OCR copy)
  extracted_at: '2026-09-11'
---

Both owner's manuals print the same NOTE, word for word, on the POWER ON & CONSOLE OPERATION page:

> **NOTE:** If there is an issue, the console will show an error message along with a possible solution. Follow the message to resolve the issue.

**The screen is the answer.** The console names the fault in words and suggests what to do about it, so there is nothing to look up - and there is nothing to look up in the book either. **Neither owner's manual prints an error code table, a fault code or a troubleshooting chapter**; their contents pages run Machine Care, Specifications, Exploded View, Warranty and stop. Across the two books (66 and 73 PDF pages) the word *error* appears twice each, both times in this NOTE; *troubleshooting* and *fault* appear not at all; every page was rendered and read against its text layer.

**Wait for the self-test before you judge the screen.** The same paragraph says that on first power-on the console needs a few minutes for an internal self-test before it reaches the login page, and that it powers itself down after 30 minutes of inactivity - press any function key to wake it. A console that looks stuck on boot may be mid-self-test, and a dark one may be asleep.

**The service manuals print four procedures for the faults the screen cannot explain**, and a fifth that the screen names:

- No power, console does not light: `spirit-med-bike-errors-no-power-touchscreen-wake-then-cn1-d5-24-vdc-then-12-vdc`
- `UART Communication Error` - the one message the service manual spells out: `spirit-med-bike-errors-uart-communication-error-cables-089-and-090-then-software-version-v255a255`
- No revolutions: `spirit-med-bike-errors-no-revolutions-d13-then-hall-sensor-2-to-3-mm-then-cable-072`
- Incorrect symmetry value: `spirit-med-bike-errors-incorrect-symmetry-value-crank-calibration-then-magnet-90-degrees-to-the-hall-sensor`

The console keeps an **Error Log** under Maintenance Mode > Service (*Displays the history of system errors*), carded under `section: console`. The 8.5UE ergometer, the 8.5S stepper and the 8.0T treadmill of the same family print the identical NOTE (`85ue-2025-errors-console-shows-the-message-and-the-fix`, `85s-2025-errors-console-shows-the-fault-and-a-suggested-fix`, `80t-2026-errors-console-shows-message-with-solution`). **Do not hand this owner a code list from another Spirit machine** - the 7.0T's `E1`-`E38` and the 8.0T's inverter codes belong to treadmill drives this bike does not have.

