---
id: ct850-2020-inverter-error-code-list
title: Every error code the display can show
kind: spec
question: What error codes can a Spirit CT850-2020 treadmill display and what does
  each one mean?
asked_as:
- list of error codes for my spirit treadmill
- what do the e codes mean on a ct850
- spirit treadmill error code table
keywords:
- error code
- error code table
- inverter
- list
- index
- hex codes
- console
- treadmill
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2020
  applies_to:
  - ct850-2020
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2020-e-01h-abnormal-ac-input-voltage
- ct850-2020-e-02h-igbt-temperature-sensor-feedback-low
- ct850-2020-e-04h-output-over-current
- ct850-2020-e-06h-inverter-overvoltage
- ct850-2020-e-07h-console-to-controller-communication-delay
- ct850-2020-e-09h-inverter-over-heat
- ct850-2020-e-0ah-motor-overcurrent
- ct850-2020-e-0bh-inverter-overcurrent
- ct850-2020-e-0ch-system-overcurrent
- ct850-2020-e-21h-flash-program-defective
- ct850-2020-e-22h-eeprom-defective
- ct850-2020-e-23h-low-voltage
- ct850-2020-e-25h-emergency-stop-warning
- ct850-2020-e-26h-driver-setting-abnormal
- ct850-2020-e-27h-lp-input-low-voltage
- ct850-2020-e-28h-hp-input-high-voltage
- ct850-2020-e-29h-inverter-over-heat
- ct850-2020-e-41h-system-overload
- ct850-2020-e-42h-high-temperature-warning
- ct850-2020-e-50h-console-controller-communication-abnormal
- ct850-2020-e-51h-communication-inside-console-abnormal
- ct850-2020-e-52h-incline-motor-fails-during-calibration
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-incline-err
- ct850-2016-error-code-items-list
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36)
  extracted_at: '2026-09-08'
---

The manual lists twenty-three codes. Each has its own card; this table is only the index. Section
8-2 names one tool for the lot: a **multi-meter**.

| Code | Cause | Solution |
|---|---|---|
| E-01H | Abnormal AC input voltage. | Check the AC input voltage is stable 100~120V. |
| E-02H | Feedback voltage of IGBT temperature sensor is too low. | The Inverter temperature sensor is defective, try to reboot the treadmill that may restore the sensor. |
| E-04H | Output over current. | Check if the motor, driver belt, rollers, and running belt cause the motor stuck. |
| E-06H | The inverter is overvoltage. | Check the AC input voltage is stable 100~120V. |
| E-07H | The communication from console to the controller is delay. | Check all the wires from the controller board to the console. |
| E-09H | The invertor is over heat. | 1. Check the fan of invertor. 2. Clean the invertor. 3. Is the ambient temperature too high? |
| E-0AH | The overcurrent of the motor. | The running belt is worn need lubricate or replacement. |
| E-0BH | The overcurrent of the invertor. | The running belt is worn need lubricate or replacement. |
| E-0CH | The overcurrent of the system. | The running belt is worn need lubricate or replacement. |
| E-21H | PrEr Flash program is defective. | Reboot the treadmill may restore or the console requires replacement. |
| E-22H | EEPROM is defective. | 1. Try to press and hold the STOP button to reset the console. 2. The console requires replacement. |
| E-23H | Low voltage. | Check the AC input voltage is stable 100~120V. |
| E-25H | The warning of emergency stop. | Check the wires of Safe Key set or reboot the treadmill. |
| E-26H | drvF Driver setting abnormal. | Reboot the treadmill may restore or the console requires replacement. |
| E-27H | LP input low voltage. | Reboot the treadmill may restore. |
| E-28H | HP input high voltage. | Reboot the treadmill may restore. |
| E-29H | The invertor is over heat. | 1. Check the fan of invertor. 2. Clean the invertor. 3. Is the ambient temperature too high? |
| E-41H | OLO The system is overload. | 1. Check if the motor, driver belt, rollers, and running belt cause the motor stuck. 2. The running belt is worn need lubricate or replacement. |
| E-42H | The warning of high temperature. | 1. Check the fan of invertor. 2. Clean the invertor. 3. Is the ambient temperature too high? |
| E-50H | The communication from console to the controller is abnormal. | Check all the wires from the controller board to the console. |
| E-51H | The communication inside the console is abnormal. | Check all the wires from the controller board to the console. |
| E-52H | The incline motor can't work normally when doing the calibration procedure. | 1. Recalibration again. 2. Check the wires of incline motor. 3. Check the incline motor is stuck. |
| E3 | The incline motor can't work normally | 1. Recalibration again. 2. Check the wires of incline motor. 3. Check the incline motor is stuck. |

Three things to know before using this table.

- **E-09H and E-29H are printed with the identical cause and the identical solution.** The manual
  never says how a technician should tell them apart.
- **E3 is printed without the `-` and without the `H`** that every other code in the table carries.
  It is a console message, not an inverter code, and it has a full section of its own at 8-3.
- The message `INCLINE ERR` is **not** in this table, although it has its own section at 8-4.

The earlier CT850 2016 manual has no code table at all; it names two messages only, on
`ct850-2016-error-code-items-list`.
