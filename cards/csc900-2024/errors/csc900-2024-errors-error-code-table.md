---
id: csc900-2024-errors-error-code-table
title: Every error code this stairclimber can show, five codes written with two digits
kind: spec
question: What error codes can a Spirit CSC900-2024 stairclimber display and what does
  each one mean?
asked_as:
- list of error codes for my spirit stairclimber
- what do the er codes mean on a csc900
- spirit stair climber error code list
keywords:
- error code
- error code table
- list
- index
- stairclimber
- console
- five codes
- diagnosis
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2024
  applies_to:
  - csc900-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-2024-errors-seven-code-table-with-no-hyphen
- ct850-2020-inverter-error-code-list
see_also:
- csc900-2024-errors-er02-magnetic-wheel-or-control-board
- csc900-2024-errors-er05-controller-hardware-overcurrent
- csc900-2024-errors-er07-emergency-stop-switch-failure
- csc900-2024-errors-er11-controller-not-receiving-console-data
- csc900-2024-errors-er12-console-not-receiving-controller-data
- csc900-2024-errors-speed-abnormal-then-data-resets
- csc900-2024-errors-brake-does-not-turn-on
- csc900-2024-errors-membrane-key-failure
- csc900-2024-errors-console-does-not-light-up-after-power-on
- csc900-2024-errors-heartbeat-not-sensed
source:
  ref: spirit-climber-csc900-2024-owners-manual
  locator: TROUBLESHOOTING and TROUBLESHOOTING - CONTINUED, Problem / Reason / Method
    tables on printed pages 34 and 35. Both pages are flat pictures with no text layer
    and were read from the rendered page at 500 dpi.
  extracted_at: '2026-09-10'
---

Five codes, each with its own card; this table is only the index. **They are written `ER` and two
digits** - no `E`, no hyphen, no trailing letter - and no other Spirit machine in the repository uses
that shape.

| Code | Condition as printed | What it means |
|---|---|---|
| ER02 | After pressing "START" to start, the electronic meter shows ER02 | Control board MOS short-circuited, or the magnet wheel connection wire is disconnected |
| ER05 | The Console shows ER05 | Controller hardware overcurrent |
| ER07 | Emergency stop switch failure or ER07 is displayed | The emergency stop switch, its wiring, or a wrong wire sequence |
| ER11 | After pressing "START" does not start, the electronic meter display ER11 | Controller can not receive the console data |
| ER12 | Press "START" to start, the electronic meter shows ER12 (can not brake) | The console does not receive the controller data |

Three things to know before using this table.

- **The numbers are not consecutive.** There is no ER01, ER03, ER04, ER06, ER08, ER09 or ER10 in the
  manual. A machine showing any of those is showing something this document does not describe.
- **ER11 and ER12 have the same two causes and the same two remedies.** What separates them is which
  end of the communication line is not being heard, and what the machine does - ER11 will not start,
  ER12 starts but will not brake.
- **The codes are not printed in a table of their own.** They are scattered through the
  Problem/Reason/Method troubleshooting matrix, in the Problem column, mixed with rows that have no
  code at all. The table above was assembled from those rows; the manual has no error code chapter.

**None of these codes exists on any other Spirit machine.** The 2024 treadmills use `E1`-`E7` or
`E-01H`-`E-52H`, the 2024 bikes and ellipticals use `EEPROM ERROR` and `E5`, the 2024 steppers use
`RAM ERROR`, `MOTOR ERROR`, `EEPROM ERROR` and `Err`, and the 2024 rower uses `E1` and `E2`. Never
answer a CSC900 caller from one of those.
