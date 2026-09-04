---
id: f85-2019-drive-motor
title: Drive motor voltage and wire colours
kind: spec
question: What voltage does the drive motor run on, and which wire is which, on a
  Sole F85-2019 treadmill?
asked_as:
- what voltage is the treadmill drive motor
- which motor wire is positive
- drive motor wire colours
keywords:
- drive motor
- dc motor
- motor voltage
- wire colours
- m plus
- m minus
- ground wire
- motor speed
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2019-incline-motor
see_also:
- f85-2019-incline-motor
- f85-2019-e4-motor-power-wire-error
- f85-2019-drive-motor-replacement
source:
  ref: sole-tm-f85-2019-service-manual
  locator: section 3 Electrical Configurations and General Information, printed pages
    29 to 30, and section 6.4, printed page 45
  extracted_at: '2026-09-04'
---

**This is the drive motor, the DC motor that turns the belt. It is not the incline motor, which is AC.**

| Field | Value |
|---|---|
| Type | Variable speed DC motor |
| Voltage | 0 to 90, or 0 to 180, volts DC from the main controller |
| Wires | three: red, black, green |

- The **red** wire is inserted into **M+**.
- The **black** wire is inserted into **M-**.
- The higher the voltage, the faster the motor turns.
- The **green** wire is the grounding wire.

The driver board wiring page labels the same two terminals: **M-** connected with the black wire of the motor, **M+** connected with the red wire of the motor.

**This manual gives the voltage as "0 –90 (or 0-180)" without tying either figure to a mains voltage.** The 2016 and 2021 manuals for the neighbouring builds tie 0 to 180 volts to the 230V system and 0 to 90 volts to the 120Vac system.
