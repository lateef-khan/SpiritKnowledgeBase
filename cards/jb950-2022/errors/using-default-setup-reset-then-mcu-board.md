---
id: jb950-2022-errors-using-default-setup-reset-then-mcu-board
title: 'USING DEFAULT SETUP: reset the console with Play and +, and replace the MCU
  board if it comes back'
kind: troubleshooting
question: What does USING DEFAULT SETUP mean on a Spirit jb950-2022 Johnny G bike
  and how is it fixed?
asked_as:
- johnny g bike says using default setup
- jb950 console shows default setup message
- how do i reset the johnny g spirit bike console
- spirit indoor bike eeprom message
keywords:
- using default setup
- eeprom
- generator
- power up
- reset console
- mcu board
- upper control board
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: using-default-setup
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-errors-hr-sensor-error-reset-console
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- spirit-bike-errors-eeprom-err-replace-upper-controller
see_also:
- jb950-2022-errors-hr-sensor-error-reset-console
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- jb950-2022-errors-error-message-table-four-messages
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.1 Error Messages table, PDF p. 37, text.md
    lines 564-593
  extracted_at: '2026-09-11'
---

**This is `USING DEFAULT SETUP`, one of four messages the JB950 console prints. It is not `HR SENSOR ERROR`, `MOTOR ERROR` or `ENCODER ERROR`.**

| Explanation | Troubleshooting |
|---|---|
| 1. Generator power up sequence is not complete causing an error when reading the EEPROM | 1. Press Play and + Key to Reset Console |
| 2. If USING DEFAULT SETUP still appears after resetting the Console, MCU board must be replaced | 2. Replace the upper control board (MCU Board) |

So the first move is the reset: **hold `PLAY` and `+` together** - the maintenance-mode chapter of the same book gives that combination as three seconds and says the console then shows `CONSOLE RESET`. Only if the message survives the reset is the MCU board (the upper control board inside the console) replaced.

**Why a generator bike shows an EEPROM message**: the console is powered by pedalling, and if it comes up before the generator has finished its power-up sequence the EEPROM read fails and the console falls back to default settings. The same incomplete power-up produces `HR SENSOR ERROR` on the heart-rate module: `jb950-2022-errors-hr-sensor-error-reset-console`.

This is the JB950's only memory message. It is not the `EEPROM ERR` of the other Spirit bikes and it names a different part and a different first step; do not send a JB950 owner to an upper-controller or display-board card.
