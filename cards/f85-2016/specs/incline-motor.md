---
id: f85-2016-incline-motor
title: Incline motor voltage and wire colours
kind: spec
question: What voltage does the incline motor run on, and which wire is which, on
  a Sole F85-2016 treadmill?
asked_as:
- what voltage is the incline motor
- incline motor wire colours
- which incline wire is up
keywords:
- incline motor
- ac motor
- elevation motor
- wire colours
- up wire
- down wire
- common wire
- position sensor
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2016
  applies_to:
  - f85-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2016-drive-motor
see_also:
- f85-2016-drive-motor
- f85-2016-incline-position-sensor-pinout
- f85-2016-incline-motor-replacement
source:
  ref: sole-tm-f85-2016-service-manual
  locator: section 3 General Information, printed page 13, and section 12-9, printed
    page 86
  extracted_at: '2026-09-04'
---

**This is the incline motor, the AC motor that raises the deck. It is not the drive motor, which is DC.**

| Field | Value |
|---|---|
| Type | AC motor |
| Voltage on the 230Vac system | 230 volts AC |
| Voltage on the 120Vac system | 115 volts AC |
| Wires | four: red, black, white, green, plus one 3 pin position sensor cable |

| Wire | Function |
|---|---|
| Red | UP. AC voltage here increases the incline. |
| Black | DOWN. AC voltage here decreases the incline. |
| White | COM, the neutral. |
| Green | Ground. |

The refit step at the end of the manual repeats it as: red to **UP**, white to **COM**, black to **DOWN**.

The 3 pin position sensor cable is separate from these four wires and has its own card.
