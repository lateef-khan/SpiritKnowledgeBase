---
id: ct850-2020-inverter-error-code-list
title: Every error code the display can show
kind: spec
question: What error codes can a Spirit CT800-2020, CT850-2020, CT850-2024, CT850ENT-2022
  or CT850ENT-2024 treadmill display and what does each one mean?
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
  model: '*'
  applies_to:
  - ct800-2020
  - ct850-2020
  - ct850-2024
  - ct850ent-2022
  - ct850ent-2024
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
- spirit-ct-2020-errors-e-08h-ground-failed
- spirit-2024-errors-seven-code-table-with-no-hyphen
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: Section 8-1 Error Codes, pages 36-37 (printed 35-36); CT850ENT 2022 service
    manual 8-1 Error code items, PDF p. 31-32, text.md lines 563-618; spirit-treadmill-ct800-2020-e50h-service-bulletin,
    TRANSCRIPT, PDF PAGE 2 (AC list, "For A/C Transforming System")
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

**The CT850 2024 and CT850ENT 2024 owner's manuals print this whole table word for word**, every
cause and every solution alike, in the ERROR CODES table on printed page 42 of the CT850 2024 manual and
printed pages 60 and 61 of the CT850ENT 2024 manual. Both of those pages are flat pictures with
no text layer, and both were read from the rendered page. The 2024 books changed the machine
around this table but not the table: the whole twenty-three-code list is unchanged from the
2020 service manual.

**The CT850ENT 2024 manual prints two further rows under the same heading that are not codes.**
`Replace Safety Key` and `SAFETY LOCK` are console messages with their own causes and remedies, and
they sit below E3 in that book's table. They are on
`spirit-2024-errors-replace-safety-key-message` and `spirit-2024-errors-safety-lock-child-mode`. The
CT850 2024 manual prints the twenty-three codes and stops.

**The CT850ENT 2022 service manual prints the whole twenty-three-code table word for word**, and already adds the `Replace Safety Key` and `SAFETY LOCK` rows beneath it - so the CT850ENT 2024 table is the 2022 service manual's, unchanged.

**A Spirit service bulletin prints the list a second way, and adds a code the manuals do not have.** The photographed card in `spirit-treadmill-ct800-2020-e50h-service-bulletin`, headed *ERROR MESSAGE of New CT800&CT850(2020) - For A/C Transforming System*, gives each code a one-line label - most carrying the inverter's own mnemonic, `(OC)`, `(OE)`, `(PFC)`, `(GF)`, `(OH)`, `(OL)`, `(OL1)`, `(OLO)`, `(PrEr)`, `(drvF)`, `(LP)`, `(HP)`, `(HT)` - and one solution for all of them: *check the wiring first before replace a new transformer*. It lists **E-08H (GF) Ground failed**, which no CT850 manual prints (`spirit-ct-2020-errors-e-08h-ground-failed`), and it labels **E-07H** *(PFC) Transformer abnormal* where the manual says a communication delay. The card's heading is the only document that puts this inverter list on a CT800 2020, whose own service manual prints the seven DC codes (`spirit-2024-errors-seven-code-table-with-no-hyphen`).
