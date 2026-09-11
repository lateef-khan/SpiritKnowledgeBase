---
id: cu900ent-error-code-messages-list
title: Every error code the console can show
kind: spec
question: What error codes can a Spirit CU900ENT or CR900ENT-2021 bike or CE900ENT
  elliptical display and what does each one mean?
asked_as:
- list of error codes for my spirit bike
- what do the codes mean on a cu900
- spirit bike error code table
keywords:
- error code
- error code table
- mcu board
- gui error
- ucb
- lcb
- list
- index
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce900ent
  - cr900ent-2021
  - cu900ent
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-40h-unknown-mode
- cu900ent-41h-inverter-no-response
- cu900ent-42h-bike-board-no-response
- cu900ent-44h-console-i2c-no-response
- cu900ent-50h-abnormal-mcu-firmware-update
- cu900ent-eah-ucb-does-not-match-lcb-device
- cu900ent-ech-ucb-to-lcb-no-response
- cu900ent-edh-lcb-unknown-device
- cu900ent-eeprom-err
- cu900ent-error-code-log
- sole-lwr-not-match
- lcb-2023-lwr-not-match
- cu1000ent-2023-errors-error-code-list-four-driver-board-codes
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Error Code Messages table, page 22; Error code items table, page 23; CR900ENT
    2021 service manual Error Code Messages table, PDF p. 21, text.md lines 222-239;
    CR900ENT 2021 service manual Error code items table, PDF p. 22, text.md lines
    239-262; CE900ENT service manual Error Code Messages table, PDF p. 22, text.md
    lines 301-318
  extracted_at: '2026-09-08'
---

The manual splits its codes into two families by where the fault is reported, and gives no solution
column for either.

**By MCU Board Error** - the motor control unit board raised it.

| Error Code | Description |
|---|---|
| 40H | Un-know mode |
| 41H | Inverter no-response |
| 42H | Bike board no-response |
| 44H | Console I2CNo-response |
| 50H | Abnormal Update MCU FW |

**GUI Error** - the console software raised it.

| Error Code | Description |
|---|---|
| EAH | UCB Is Not Math LCB Device |
| ECH | UCB To LCB Is No Response |
| EDH | LCB Unknown Device |

`UCB` is the upper control board, that is the console. `LCB` is the lower control board.

A separate one-row table on the next page names a message rather than a code:

| Error Message | Explain |
|---|---|
| EEPROM ERR | EEPROM failure |

Four things worth knowing before using this table.

- **No cause and no fix is printed for any of the eight codes.** The only tool the error section
  names is a multi-meter.
- **`Math` in EAH is a misprint for `Match`.** The error log screenshot elsewhere in this manual
  spells the same entry `UCB No Match LCB Device`.
- The codes are written with a trailing `H` for hexadecimal in this table, but the console's own
  error log writes them as `0x` values - `EAH` appears in the log as `0xea`.
- **`EEPROM ERR` is not in the code table**, and no code number is given for it anywhere.

Sole uses the message `LWR NOT MATCH` for the same upper-to-lower board mismatch on its own
machines; those cards are linked below and describe different machines.

**The CR900ENT 2021 recumbent service manual prints both tables word for word** - the eight hex codes with the same descriptions and remarks (`Un-know mode`, `Is Not Math` misprints included) and the one-row `EEPROM ERR` table - so this list answers for the recumbent as well as the upright. The CU1000ENT 2023 upright does **not** share it: its table is four driver-board codes, `0xB0` to `0xB3`, on `cu1000ent-2023-errors-error-code-list-four-driver-board-codes`.

**The CE900ENT elliptical service manual prints both tables word for word** - the eight hex codes with the same descriptions and remarks (`Un-know mode`, `Is Not Math` and even `Bike board no-response` on an elliptical) and the one-row `EEPROM ERR` table - so this list answers for the elliptical as well. The elliptical book's `5. Troubleshooting (Electronic)` heading is empty, and its `7. Troubleshooting` chapter is belt tension, noise and shaking, not codes.
