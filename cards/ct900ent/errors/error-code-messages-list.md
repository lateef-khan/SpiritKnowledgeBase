---
id: ct900ent-errors-error-code-messages-list
title: Every hex error code the console can show, in three families, with no solution
  column
kind: spec
question: What error codes can a Spirit ct900ent treadmill display and what does each
  one mean?
asked_as:
- list of error codes for my spirit ct900ent
- what do the hex codes mean on the ent treadmill
- spirit touchscreen treadmill error code table
keywords:
- error code
- error code table
- hex codes
- inverter
- mcu board
- gui error
- list
- index
- ent
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct900ent
  applies_to:
  - ct900ent
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-inverter-error-code-list
- ct900-error-code-table
- ct1000ent-2023-errors-error-code-list-25-hex-codes
- cu900ent-error-code-messages-list
see_also:
- ct900ent-errors-01h-low-voltage-trip
- ct900ent-errors-02h-abnormal-temperature-sensor
- ct900ent-errors-04h-output-overcurrent
- ct900ent-errors-06h-inverter-overvoltage
- ct900ent-errors-08h-abnormal-ground
- ct900ent-errors-09h-inverter-overheat
- ct900ent-errors-0ah-motor-overload
- ct900ent-errors-0bh-inverter-overload
- ct900ent-errors-0ch-system-overload
- ct900ent-errors-0dh-motor-disconnection-detection
- ct900ent-errors-0eh-brake-fault
- ct900ent-errors-21h-flash-drive-program-failure
- ct900ent-errors-22h-eeprom-failure
- ct900ent-errors-23h-low-voltage-display
- ct900ent-errors-25h-emergency-stop-esp
- ct900ent-errors-29h-motor-overheat
- cu900ent-40h-unknown-mode
- cu900ent-41h-inverter-no-response
- cu900ent-42h-bike-board-no-response
- cu900ent-44h-console-i2c-no-response
- cu900ent-50h-abnormal-mcu-firmware-update
- cu900ent-eah-ucb-does-not-match-lcb-device
- cu900ent-ech-ucb-to-lcb-no-response
- cu900ent-edh-lcb-unknown-device
- cu900ent-error-code-log
- spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter
source:
  ref: spirit-treadmill-ct900ent-service-manual
  locator: CT900ENT service manual Error Code Messages, PDF p. 19, text.md lines 256-288
  extracted_at: '2026-09-11'
---

**This table is printed only in the service manual - the CT900ENT owner's manual has no error-code section at all** (`ct900-error-code-table` says so). Twenty-four codes in three families, by who raised the fault, and no solution column for any of them; the only tool the chapter names is a multi-meter.

**By Inverter Error**

| Error Code | Description |
|---|---|
| 01H | Low voltage trip |
| 02H | Abnormal temperature sensor |
| 04H | Output overcurrent |
| 06H | Inverter overvoltage |
| 08H | Abnormal ground |
| 09H | Inverter overheat |
| 0AH | Motor overload |
| 0BH | Inverter overload |
| 0CH | System overload |
| 0DH | Motor disconnection detection |
| 0EH | Brake fault |
| 21H | Flash drive program failure |
| 22H | EEPROM failure |
| 23H | Low voltage display |
| 25H | Emergency Stop (ESP) |
| 29H | Motor overheat |

**By MCU Board Error**

| Error Code | Description |
|---|---|
| 40H | Un-know mode |
| 41H | Inverter no-response |
| 42H | Bike board no-response |
| 44H | Console I2CNo-response |
| 50H | Abnormal Update MCU FW |

**GUI Error**

| Error Code | Description |
|---|---|
| EAH | UCB Is Not Math LCB Device |
| ECH | UCB To LCB Is No Response |
| EDH | LCB Unknown Device |

Each code has its own card. Four things to know before using the table.

- **The inverter numbers are the CT850 2020's `E-xxH` numbers without the `E-`**, and their descriptions are shorter. The CT850 explains `E-01H` as abnormal AC input voltage and offers a solution; this book says `Low voltage trip` and offers none. Two machines, two strings; never answer one from the other (`ct850-2020-inverter-error-code-list`).
- **Two inverter codes have no CT850 twin**: `0DH` motor disconnection and `0EH` brake fault.
- **The eight MCU and GUI codes are the CU900ENT bike's, word for word**, `Bike board no-response` and the `Math` misprint included (`cu900ent-error-code-messages-list`).
- **The CT900, the non-touch-screen sibling with the same VFD015TM12A inverter, uses a completely different family** - `E1` to `E34` plus the inverter's own `oc`, `oL`, `cE1` mnemonics (`ct900-error-code-table`). The same inverter, two consoles, two code sets.

The console's Diagnostics screen logs these codes as `0x` values and clears with ten presses of the Error Code Log button (`cu900ent-error-code-log`). `INCLINE ERR` is a message with a section of its own and is not in this table (`spirit-ct-ent-errors-incline-err-no-vr-change-8-pin-cable-then-inverter`). The `LS1/LOW SPEED` and `LS` strings in this book's matrix and checklist belong to the CT800 template and are not codes this console shows (`ct800-2016-errors-low-speed-after-ten-seconds`).
