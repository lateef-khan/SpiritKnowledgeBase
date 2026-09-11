---
id: 80t-2026-errors-inverter-error-code-table-48-rows
title: The 48-row inverter error table, with fourteen rows marked not applicable and
  two message rows without a code
kind: fact
question: What is the full list of inverter error codes on a Spirit 80t-2026 treadmill,
  and which ones are not applicable to it?
asked_as:
- 8.0t error code list
- list of inverter codes for the medical treadmill
- what are the drive codes on the 8.0t
- treadmill shows a code that is not in the owners manual
keywords:
- error code table
- inverter codes
- fault codes
- drive codes
- not applicable
- mt2000
- medical treadmill
- error log
- vfd
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: errors
  code: '*'
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-error-code-table
- ct850-2020-inverter-error-code-list
- spirit-xt-errors-error-code-list-eight-codes
- ct1000ent-2023-errors-error-code-list-25-hex-codes
see_also:
- 80t-2026-errors-console-shows-message-with-solution
- 80t-2026-errors-rler-dc-voltage-too-low-during-operation
- 80t-2026-errors-conf-rs-485-communication-error-cn8-j18-j19-then-tx-rx-leds
- 80t-2026-errors-pgo-abnormal-motor-speed-encoder-cable-brake-then-transmission
- 80t-2026-errors-erp2-parameter-write-error-printed-on-two-rows
- 80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version
- 80t-2026-errors-incline-motor-operation-error-calibrate-then-swap-j9-j15-j6-j7
- 80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Error Codes table, PDF p. 20-22; text.md lines 245-358, checked against
    a 130 dpi render of p. 20 for the row structure (the two-cause rows). Maintenance
    Mode Error Log, PDF p. 13, text.md line 196
  extracted_at: '2026-09-11'
---

**The service manual prints a 48-row inverter error table plus two message rows; the owner's manual prints no code list at all** (`80t-2026-errors-console-shows-message-with-solution` - the touchscreen puts the fault and a fix on screen). These are drive codes read on the inverter, and **none of them is an `E<n>` code**: the 7.0T of the same year uses a numbered `E1`-`E38` table (`70t-2026-errors-error-code-table`) and the CT850 2020 uses `E-01H`-style hex codes (`ct850-2020-inverter-error-code-list`). Never carry a code between those families.

**Each applicable code has its own card**; fourteen rows are printed as *Not applicable to this model* and have no card - if one of those appears on a screen, the book has nothing to say about it.

| Row | Code | Cause | Solution |
|---|---|---|---|
| 01 | rLEr | DC voltage too low during operation | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |
| 02 | Lu | Excessive voltage drop in the power supply / Sudden overload on transmission components | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. / Check the load on transmission components related to the drive belt operation. |
| 03 | ocA | Overcurrent during acceleration | Check for loose connections between the inverter output and the motor terminals. |
| 04 | ocd | Overcurrent during deceleration | Check for loose connections between the inverter output and the motor terminals. |
| 05 | ocn | Sudden fluctuation in AC supply voltage / Impact load causing abrupt current variation | Ensure the equipment is used in an environment with stable AC mains voltage. For the 110 VAC model connect to a 20A dedicated AC power circuit; for the 220 VAC model connect to a 15A dedicated AC power circuit. Avoid sharing the power source with other electrical devices. / Check the load on transmission components related to the drive belt operation. |
| 06 | oL | Prolonged overload operation | Inspect transmission components for any abnormalities, such as damage or wear on the running deck surface. |
| 07 | oL1 | Motor operated under overload for extended periods | Inspect transmission components for any abnormalities, such as damage or wear on the running deck surface. |
| 08 | oL2 | Motor over-torque | Inspect transmission components for any abnormalities, such as damage or wear on the running deck surface. |
| 09 | Hoc1 | Inverter output short circuit, loose wiring, or poor grounding / Sudden overload on transmission components | Check for loose connections between the inverter output and the motor terminals. / Check the load on transmission components related to the drive belt operation. |
| 10 | Hoc2 | *Not applicable to this model* | - |
| 11 | Hoc3 | Short circuit at the output/load end of the inverter | Check for loose connections between the inverter output and the motor terminals. Replace the inverter if necessary. |
| 12 | Hou | Excessive input voltage | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |
| 13 | EF | Safety switch disconnected | Reconnect the safety switch. |
| 14 | ocbE | Unbalanced three-phase output current of the motor | Check for loose connections between the inverter output and the motor terminals. |
| 15 | AutF | Failure in motor auto-tuning process | Check for loose connections between the inverter output and the motor terminals. |
| 16 | ct1E | Loose wiring at the inverter output or internal circuit abnormality | Check for loose connections between the inverter output and the motor terminals. Replace the inverter if necessary. |
| 17 | ct2E | Loose wiring at the inverter output or internal circuit abnormality | Check for loose connections between the inverter output and the motor terminals. Replace the inverter if necessary. |
| 18 | ct3E | Loose wiring at the inverter output or internal circuit abnormality | Check for loose connections between the inverter output and the motor terminals. Replace the inverter if necessary. |
| 19 | ErP0 | EEPROM error | Replace the inverter. |
| 20 | ErP1 | Parameter write error | Replace the inverter. |
| 21 | ErP2 | Parameter write error | Replace the inverter. |
| 22 | ErP2 | Parameter write error *(printed a second time - row 21 is the same code)* | Replace the inverter |
| 23 | conF | RS-485 communication transmission error | Check the RS-485 wiring between the controller and the inverter. |
| 24 | Acio | *Not applicable to this model* | - |
| 25 | tPEr | *Not applicable to this model* | - |
| 26 | PGE | *Not applicable to this model* | - |
| 27 | Pgo | Abnormal motor speed detected via encoder feedback | Refer to the troubleshooting section for details. |
| 28 | oS | Speed exceeds maximum allowable limit | Replace the inverter. |
| 29 | oES | Excessive load caused significant speed deviation | Check whether the electromagnetic brake on the motor is released during operation (refer to the troubleshooting section for details). Check the load on transmission components related to the drive belt operation. |
| 30 | oH0 | Inverter overheat warning | Inspect the inverter's DC fan for malfunction or air duct obstruction. |
| 31 | oH1 | *Not applicable to this model* | - |
| 32 | oH2 | Inverter Overheating | Inspect the inverter's DC fan for malfunction or air duct obstruction. |
| 33 | oH3 | *Not applicable to this model* | - |
| 34 | FbF | *Not applicable to this model* | - |
| 35 | Fbu | *Not applicable to this model* | - |
| 36 | FbEF | *Not applicable to this model* | - |
| 37 | oS1 | *Not applicable to this model* | - |
| 38 | LL | Low torque detected | The load has suddenly decreased, possibly due to a broken belt. Check the transmission components related to drive belt operation. |
| 39 | nAut | *Not applicable to this model* | - |
| 40 | PF | Input voltage too low | Verify that the AC input voltage supplied to both the treadmill and the inverter is within the specified operating range: for the 110 VAC model 100-120 VAC, 60 Hz; for the 220 VAC model 200-240 VAC, 50 Hz. |
| 41 | EPE0 | EEPROM read error | Replace the inverter. |
| 42 | EPE1 | EEPROM write error | Replace the inverter. |
| 43 | ouA | Overvoltage during acceleration | Check motor insulation condition. |
| 44 | oud | Overvoltage during deceleration | Replace the inverter. |
| 45 | oun | Overvoltage during constant speed operation | Check the load on transmission components related to the drive belt operation. |
| 46 | ErP4 | *Not applicable to this model* | - |
| 47 | LP | *Not applicable to this model* | - |
| 48 | StoP | *Not applicable to this model* | - |

**Two message rows close the table, and neither has a code:**

| Category | Error Code | Cause | Solution |
|---|---|---|---|
| Communication | Message | UART communication transmission error | Check wiring between controller and console. |
| Incline Motor | Message | Incline Motor operation error | Refer to the troubleshooting section for details. |

Those two are `80t-2026-errors-uart-communication-error-cables-273-1-273-275-then-software-version` and `80t-2026-errors-incline-motor-operation-error-calibrate-then-swap-j9-j15-j6-j7`.

**Three procedures in the troubleshooting chapter stand behind three of the rows**: `conF` (RS-485 Communication Error), `Pgo` (PGO Error) and `oES` (the brake check inside the PGO procedure). The no-power procedure has no code because a dark console shows nothing: `80t-2026-errors-no-power-console-does-not-light-j16-j17-d17-then-12-vdc`.

**Where the table is untidy.** `ErP2` is printed on both row 21 and row 22 with the same cause and fix, and there is no `ErP3`. Rows `Lu`, `ocn` and `Hoc1` each carry two causes with two different solutions. The voltage range the supply rows quote is 100-120 VAC 60 Hz on the 110 VAC model and 200-240 VAC 50 Hz on the 220 VAC model.

The console's Maintenance Mode keeps an **Error Log** (Service > Error Log, *Displays the history of system errors*) - the place to read a code that has already cleared; that menu is carded under `section: console`.

