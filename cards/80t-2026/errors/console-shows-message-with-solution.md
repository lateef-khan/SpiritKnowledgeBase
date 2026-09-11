---
id: 80t-2026-errors-console-shows-message-with-solution
title: The console states the fault in words with a suggested fix, instead of a numbered
  code
kind: fact
question: What does the console of a Spirit 80t-2026 treadmill show when something
  goes wrong?
asked_as:
- my treadmill screen is showing a warning message
- where is the error code list for this treadmill
- what does the message on the touchscreen mean
keywords:
- error message
- possible solution
- touchscreen
- no error code
- fault message
- warning on screen
- console message
- troubleshooting
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: no-code
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-error-code-table
- ct850-2020-inverter-error-code-list
see_also:
- 70t-2026-errors-error-code-table
- 80t-2026-errors-inverter-error-code-table-48-rows
- 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
- 80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc
source:
  ref: spirit-treadmill-80t-2026-owners-manual
  locator: POWER ON & CONSOLE OPERATION, the NOTE box, printed page 24; text.md lines
    825-828; the absence is the owner's manual's only; the 8.0T (MT2000-ST022/027-01)
    service manual prints a 48-row inverter error table at PDF p. 20-22 (added 2026-09-11)
  extracted_at: '2026-09-09'
---

The manual's note reads: **if there is an issue, the console will show an error message
along with a possible solution. Follow the message to resolve the issue.**

So the message on screen is the answer - the machine tells you the fault and what to do
about it in plain words. There is nothing to look up.

**The manual prints no error code table and no troubleshooting section at all**, and its
contents page has no Troubleshooting entry. If you are hunting for an `E<n>` chart for
this machine, there is not one. The 7.0T of the same year is the machine that carries a
numbered table - see [the 7.0T error code table](../../70t-2026/errors/error-code-table.md)
- and its numbers do not apply here.

**The service manual is where the codes are.** The 8.0T (MT2000) service manual prints a 48-row inverter error table - `rLEr`, `Lu`, `ocA`, `oL`, `Hoc1`, `ErP0`, `conF`, `Pgo` and the rest, fourteen of them marked not applicable - plus the two on-screen messages `UART Communication Error` and `Incline Motor operation error`, and a no-power procedure for a screen that shows nothing: `80t-2026-errors-inverter-error-code-table-48-rows`. The absence above is about the owner's manual only (added 2026-09-11).

