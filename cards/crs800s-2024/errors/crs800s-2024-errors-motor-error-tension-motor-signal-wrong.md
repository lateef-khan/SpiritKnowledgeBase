---
id: crs800s-2024-errors-motor-error-tension-motor-signal-wrong
title: MOTOR ERROR means the tension motor is abnormal or sending the wrong signal, and no remedy is printed
kind: troubleshooting
question: What does MOTOR ERROR mean on a Spirit CRS800S-2024 semi-recumbent stepper?
asked_as:
- my spirit stepper says motor error
- what does motor error mean on the console
- stepper resistance motor error
keywords:
- motor error
- tension motor
- resistance
- wrong signal
- console
- stepper
- no troubleshooting
- error message
facets:
  brand:
  - spirit
  product_line: climber
  model: crs800s-2024
  applies_to:
  - crs800s-2024
  section: errors
  code: motor-error
  model_number: '800525'
authority: 3
not_to_be_confused_with:
- cvc800-e-2-tension-motor-error
- ce850-2024-errors-err-tension-motor-failure
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
see_also:
- cvc800-e-2-tension-motor-error
- cvc800-tension-motor-voltage-test
- crs800s-2024-errors-ram-error-replace-the-display-board
source:
  ref: spirit-climber-crs800s-2024-owners-manual
  locator: ERROR CODES, printed page 36. That page is a flat picture with no text layer
    and was read from the rendered page.
  extracted_at: '2026-09-10'
---

**This machine prints the message with no code letter and no number** - the words `MOTOR ERROR` and
nothing else.

The manual, word for word:

> MOTOR ERROR :
> Tension Motor operates abnormal or provide wrong signal to the console.

**No troubleshooting line is printed.** The `RAM ERROR` above it on the same page has a
`Troubleshooting :` heading and an instruction; this one stops at the definition. The rendered page
was checked at 400 dpi to be sure nothing was lost to the extraction: the page really does end
there, with white space below the sentence.

So the manual tells the owner of this machine what has failed and not what to do about it.

**The Spirit CVC800 climber prints this same sentence under the code `E-2`, and adds the whole
diagnosis** - a signal path, an operating voltage, a troubleshooting table and a voltage test with a
pass band. See `cvc800-e-2-tension-motor-error` and `cvc800-tension-motor-voltage-test`. That is a
different machine, and its voltages are its own, but it is the only Spirit document that says what
to measure when a tension motor sends the wrong signal.

The other message this manual carries is `RAM ERROR`:
`crs800s-2024-errors-ram-error-replace-the-display-board`.
