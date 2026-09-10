---
id: csc880-2025-errors-error-code-table
title: Five ER codes on an eleven-row table, four of them renumbered from the other
  stair climber
kind: spec
question: What error codes can a Spirit CSC880-2025 stair climber display and what
  does each one mean?
asked_as:
- list of error codes for my spirit stair climber
- what do the er codes mean on a csc880
- spirit stair climber error code list
- csc880 troubleshooting table
keywords:
- error code
- error code table
- er01
- er02
- er03
- er04
- er07
- stair climber
- troubleshooting
- index
facets:
  brand:
  - spirit
  product_line: climber
  model: csc880-2025
  applies_to:
  - csc880-2025
  section: errors
  code: '*'
  model_number:
  - '880665'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-error-code-table
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
see_also:
- csc880-2025-errors-er01-console-not-receiving-controller-data
- csc880-2025-errors-er02-infrared-emergency-stop-triggered
- csc880-2025-errors-er03-controller-not-receiving-console-data
- csc880-2025-errors-er04-overcurrent-magnetic-wheel-short
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
- csc880-2025-errors-no-pulse-data-pulse-cable-insulation
- csc880-2025-errors-safe-in-the-display-emergency-stop-wiring
- csc900-2024-errors-speed-abnormal-then-data-resets
- csc900-2024-errors-brake-does-not-turn-on
- csc900-2024-errors-membrane-key-failure
source:
  ref: spirit-climber-csc880-2025-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, the No./Problem/Causes/Solution
    table on printed pages 33 and 34 (PDF pages 35 and 36). Both pages carry a real
    text layer; the codes were read from the native extraction and confirmed against
    a 400 dpi render of both pages.
  extracted_at: '2026-09-10'
---

Eleven numbered rows, of which five carry a code. **The codes are written `ER` and two digits** -
no `E`, no hyphen. Each code has its own card; this table is only the index.

| Code | Problem as printed | Cause named |
|---|---|---|
| ER01 | Console displays ER01 | The Console cannot receive data from the controller |
| ER02 | Console displays ER02 | Trigger infrared emergency stop switch |
| ER03 | Console displays ER03 | The controller cannot receive data from the console |
| ER04 | Console displays ER04 | Overcurrent protection, excessive current |
| ER07 | Console displays ER07 | Emergency stop switch malfunction, a loose connection wire, or an incorrect wire sequence |

**There is no ER05, ER06, ER08, ER09, ER10, ER11 or ER12 in this book**, and there is no ER00.
A machine showing any of those is showing something this manual does not describe.

## The other Spirit stair climber numbers the same faults differently

This is the trap. The CSC900 2024 book prints `ER02`, `ER05`, `ER07`, `ER11` and `ER12`, and
**only ER07 means the same thing on both machines.**

| Fault | On this machine | On the CSC900 2024 |
|---|---|---|
| Console not receiving controller data | **ER01** | **ER12** (and the machine cannot brake) |
| Controller not receiving console data | **ER03** | **ER11** (and the machine will not start) |
| Over-current | **ER04** | **ER05** |
| Emergency stop switch or its wiring | **ER07** | **ER07** |
| Infrared emergency stop switch triggered | **ER02** | not printed |
| Magnet wheel wiring or a shorted MOS | folded into **ER04** | **ER02** |

So `ER02` names two different faults on two Spirit stair climbers, and a technician who reads the
CSC900 table to a CSC880 caller sends them to the wrong part. Establish the model before the code.
The CSC900 2024 set is at `csc900-2024-errors-error-code-table`.

## The six rows that carry no code

Rows 6 to 11 are symptom rows with no code at all: the light sensor, the power-off brake, the
membrane keypad, a console that will not light, no pulse data, and the word `Safe` in the display.
Four of the six state the same fact as the CSC900 2024 rows and are carded on the shared cards
listed in `see_also`; two are this machine's own -
`csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks`, whose voltages differ, and
`csc880-2025-errors-safe-in-the-display-emergency-stop-wiring`, which the CSC900 book does not
print.

**This manual prints no `RAM ERROR`, no `EEPROM ERROR` and no `Err`** - the messages the Spirit
steppers of the same generation use. It is a different console.
