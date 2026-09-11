---
id: jb950-2022-errors-error-message-table-four-messages
title: 'Every error message the console can show: four messages, each with its own
  explanation and fix'
kind: spec
question: What error messages can a Spirit jb950-2022 Johnny G bike display and what
  does each one mean?
asked_as:
- list of error messages on the johnny g spirit bike
- jb950 error codes
- what errors can the jb950 console show
- spirit indoor bike error message table
keywords:
- error message
- error code table
- using default setup
- hr sensor error
- motor error
- encoder error
- list
- johnny g
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- cu900ent-error-code-messages-list
- cu1000ent-2023-errors-error-code-list-four-driver-board-codes
see_also:
- jb950-2022-errors-using-default-setup-reset-then-mcu-board
- jb950-2022-errors-hr-sensor-error-reset-console
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- spirit-jb950-errors-update-fail-or-search-update
- spirit-jb950-errors-limit-sensor-test-after-motor-error
- spirit-commercial-bike-errors-no-error-codes-printed
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: JB950 2022 service manual 5.1 Error Messages table, PDF p. 37, text.md
    lines 564-593
  extracted_at: '2026-09-11'
---

The JB950 console prints words, not codes. Section 5.1 of the service manual is one table with four rows, and unlike the other Spirit bike books every row has a fix.

| Error Message | Explanation | Troubleshooting |
|---|---|---|
| USING DEFAULT SETUP | 1. Generator power up sequence is not complete causing an error when reading the EEPROM. 2. If USING DEFAULT SETUP still appears after resetting the Console, MCU board must be replaced | 1. Press Play and + Key to Reset Console. 2. Replace the upper control board (MCU Board) |
| HR SENSOR ERROR | 1. Generator power up sequence is not complete resulting in incomplete initialization of the read HR module, so it is impossible to interpret HR | 1. Press Play and + Key to Reset Console |
| MOTOR ERROR | 1. ENCODER is read, but motor does not reach home position. | 1. Make sure cables aren't broken or shorted to other pins or the frame. 2. Brake position flag may have crashed into, or traveled past the home position sensor. Replace brake assembly. 3. Replace the Limit SENSOR BOARD & controller |
| ENCODER ERROR | 1. Capacitor voltage is too low, causing ENCODER SENSOR not to read. 2. Bad Wire connection causing ENCODER SENSOR not to read. 3. MOTOR wire is disconnected, MOTOR does not operate, ENCODER SENSOR has no signal | 1. Continue to pedal and press Play and + Key to Reset Console to see if it has been remedied. 2. Check if the wire between the console & controller is seated properly. 3. Check if the MOTOR wire is seated properly. 4. Check if brake assembly is malfunctioning. |

Two of the four start with the same reset - **`PLAY` and `+` held together** - because the bike is generator powered and a console that wakes before the generator has finished its power-up sequence misreads its EEPROM or never initialises its heart-rate module. The other two are the brake: an encoder that reads but a brake that never homes, and an encoder that does not read at all.

One card per message: `jb950-2022-errors-using-default-setup-reset-then-mcu-board`, `jb950-2022-errors-hr-sensor-error-reset-console`, `jb950-2022-errors-motor-error-brake-does-not-reach-home`, `jb950-2022-errors-encoder-error-pedal-then-check-wires`.

Two more messages live in the software updater rather than this table - `SEARCH UPDATE`, `UPDATE DONE` and `UPDATE FAIL` (`spirit-jb950-errors-update-fail-or-search-update`) - and the console says `CONSOLE RESET` when the reset lands and `MAINTENANCE MODE` when the three-key hold does. None of the other Spirit bikes shares any of these strings; the JB950 owner's manual prints none of them either (`spirit-commercial-bike-errors-no-error-codes-printed`).
