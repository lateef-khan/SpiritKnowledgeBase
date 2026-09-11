---
id: crs800s-2024-errors-motor-error-tension-motor-signal-wrong
title: MOTOR ERROR means the tension motor is abnormal or sending the wrong signal;
  the owner's manual prints no remedy and the service manual prints one
kind: troubleshooting
question: What does MOTOR ERROR (Err) mean on a Spirit CRS800S semi-recumbent stepper?
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
  model: '*'
  applies_to:
  - crs800s-2021
  - crs800s-2024
  section: errors
  code: motor-error
authority: 3
not_to_be_confused_with:
- cvc800-e-2-tension-motor-error
- ce850-2024-errors-err-tension-motor-failure
- cs800-2024-errors-err-in-the-level-window-tension-motor-feedback
see_also:
- cvc800-e-2-tension-motor-error
- cvc800-tension-motor-voltage-test
- crs800s-2024-errors-ram-error-replace-the-display-board
- crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer
source:
  ref: spirit-climber-crs800s-2024-owners-manual
  locator: 'ERROR CODES, printed page 36. That page is a flat picture with no text
    layer and was read from the rendered page; CRS800S 2020 ver. service manual 8-2
    Error Message: Err, with the Tension Motor Operation and Troubleshooting tables,
    PDF p. 28-29 (printed 27-28), text.md lines 354-399'
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

## The CRS800S 2020-version service manual prints the remedy the owner's manual leaves out

Its section is headed `8-2 Error Message: Err` and opens with the same two lines - `MOTOR ERROR:` / *Tension Motor operates abnormal or provide wrong signal to the console.* **So the console shows `Err` and the book calls it MOTOR ERROR**; the 2020-book CRS800S (`crs800s-2021`) and the 2024 CRS800S print the same definition. The service manual then draws the signal path - the `+/- KEYS` and `LEVEL +/- KEYS` into the display board, a *Level +/- signal* down to the tension motor and a *Level VR signal* back - and prints:

**Tension Motor Operation**

| Part | Description |
|---|---|
| Console | Key signal travels to the display. The main program IC then sends a command signal to the drive board. Console directly controls the motor. Level UP: **+4~5VDC**; Level DOWN: **-4~5VDC** |

**Tension Motor Troubleshooting**

| Part | Description |
|---|---|
| Console | If the key beeps when pressed, assume that the signal was sent. Inspect console power output to the motor. Press the Level Up is +4~5VDC; Level DOWN is -4~5VDC. If there is power to the motor, but the motor does not operate, replace it. If there is no power output, inspect whether the transformer has power. |
| Data cable | Inspect the cable and connections. |

**Beep, then voltage, then motor or transformer.** A key that beeps has sent its signal; 4 to 5 V at the motor with no movement is a dead motor; no voltage is the transformer. The voltage test that follows, with a 4 to 5.5 V pass band and a 9-pin cable table, is `crs800s-2021-errors-tension-motor-voltage-test-4-to-5-5-vdc-then-the-transformer`. The connector pin map on the same pages gives `MTR-` and `MTR+` as pins 1 and 2 and `MTR_AD` as pin 4 of the 11-pin console-to-driver connector.
