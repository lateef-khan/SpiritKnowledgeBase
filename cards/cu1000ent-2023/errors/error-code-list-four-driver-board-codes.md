---
id: cu1000ent-2023-errors-error-code-list-four-driver-board-codes
title: 'Every error code the console can show: four driver-board hex codes and the
  EEPROM ERR message'
kind: spec
question: What error codes can a Spirit cu1000ent-2023 upright bike display and what
  does each one mean?
asked_as:
- list of error codes for the cu1000 bike
- what do the 0xb codes mean on a spirit ent bike
- spirit cu1000ent error code table
- cu1000 hex error codes
keywords:
- error code
- error code table
- hex code
- driver board
- eeprom err
- list
- index
- ent upright bike
facets:
  brand:
  - spirit
  product_line: bike
  model: cu1000ent-2023
  applies_to:
  - cu1000ent-2023
  section: errors
  code: '*'
  model_number:
  - '210354'
authority: 3
not_to_be_confused_with:
- cu900ent-error-code-messages-list
- ct1000ent-2023-errors-error-code-list-25-hex-codes
see_also:
- cu1000ent-2023-errors-0xb0-eeprom-error-driver-board
- cu1000ent-2023-errors-0xb1-resist-error-driver-board
- cu1000ent-2023-errors-0xb2-uart-error-driver-board
- cu1000ent-2023-errors-0xb3-cmd-error-driver-board
- cu900ent-eeprom-err
- cu900ent-error-code-log
- ce800ent-e5-console-controller-communication
source:
  ref: spirit-bike-cu1000ent-2023-service-manual
  locator: CU1000ENT 2023 service manual 7.1 Error Code List, 7.2 Error code items
    and 7.3 Tools Required, PDF p. 12, text.md lines 229-259
  extracted_at: '2026-09-11'
---

The CU1000ENT 2023 service manual prints two small tables and no solution column for either.

**7.1 Error Code List** - every row is raised by the driver board.

| Code | Description |
|---|---|
| 0xB0 | EEPROM Error, By Driver Board Error |
| 0xB1 | Resist Error, By Driver Board Error |
| 0xB2 | UART Error, By Driver Board Error |
| 0xB3 | CMD Error, By Driver Board Error |

**7.2 Error code items** - a message rather than a code.

| Error Message | Explain |
|---|---|
| EEPROM ERR | EEPROM failure |

**7.3 Tools Required**: a multi-meter, and nothing in the chapter uses it.

Three things to know before using the table.

- **No cause and no fix is printed for any of the five entries.** The per-code cards (`cu1000ent-2023-errors-0xb0-eeprom-error-driver-board`, `-0xb1-resist-error-driver-board`, `-0xb2-uart-error-driver-board`, `-0xb3-cmd-error-driver-board`) can therefore only say what the row says.
- **`0xB0` and `EEPROM ERR` are two different entries.** The hex code is an EEPROM fault reported *by the driver board*; the message is the console's own EEPROM failure, which the book leaves with no fix exactly as the CU900ENT and CR900ENT books do (`cu900ent-eeprom-err`).
- **This is a different family from the other ENT bikes.** The CU900ENT and CR900ENT print `40H`-`50H` MCU-board codes and `EAH`/`ECH`/`EDH` GUI codes (`cu900ent-error-code-messages-list`); the CU800ENT and CR800ENT print one code, `E5` (`ce800ent-e5-console-controller-communication`). The CT1000ENT treadmill also writes its codes as `0x` values, but its list runs `0x01` to `0x44` and none of them is `0xB0`-`0xB3` (`ct1000ent-2023-errors-error-code-list-25-hex-codes`).

Logged codes are read back, and cleared with ten presses, under Service > Error Code Log: `cu900ent-error-code-log`.
