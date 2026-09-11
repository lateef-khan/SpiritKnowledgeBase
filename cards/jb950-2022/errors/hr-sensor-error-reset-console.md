---
id: jb950-2022-errors-hr-sensor-error-reset-console
title: 'HR SENSOR ERROR: the heart-rate module did not finish initialising, so reset
  the console with Play and +'
kind: troubleshooting
question: What does HR SENSOR ERROR mean on a Spirit jb950-2022 Johnny G bike and
  how is it fixed?
asked_as:
- johnny g bike says hr sensor error
- jb950 heart rate sensor error on the console
- spirit indoor bike hr module error
- how do i clear hr sensor error
keywords:
- hr sensor error
- heart rate module
- generator
- power up
- reset console
- play and plus
- initialization
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: hr-sensor-error
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
see_also:
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
- jb950-2022-errors-cant-find-the-chest-strap-worn-or-battery
- jb950-2022-errors-error-message-table-four-messages
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.1 Error Messages table, PDF p. 37, text.md
    lines 564-593
  extracted_at: '2026-09-11'
---

**This is `HR SENSOR ERROR`, one of four messages the JB950 console prints. It is not `USING DEFAULT SETUP`, `MOTOR ERROR` or `ENCODER ERROR`.**

| Explanation | Troubleshooting |
|---|---|
| 1. Generator power up sequence is not complete resulting in incomplete initialization of the read HR module, so it is impossible to interpret HR | 1. Press Play and + Key to Reset Console |

That is the whole entry: **one cause and one fix.** The console came up before the generator had finished powering it, the heart-rate module never initialised, and a reset - **`PLAY` and `+` held together**, three seconds by the maintenance-mode chapter - starts it again. The manual names no part to replace for this message.

It is the heart-rate twin of `USING DEFAULT SETUP`, which the same incomplete power-up raises on the EEPROM: `jb950-2022-errors-using-default-setup-reset-then-mcu-board`.

A chest strap the console cannot find at all, with no message on the screen, is the `Can't find the chest strap` row of the troubleshooting matrix: `jb950-2022-errors-cant-find-the-chest-strap-worn-or-battery`.
