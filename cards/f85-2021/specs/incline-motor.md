---
id: f85-2021-incline-motor
title: Incline motor voltage and wire colours
kind: spec
question: What voltage does the incline motor run on, and which wire is which, on
  a Sole F85-2021 treadmill?
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
  model: f85-2021
  applies_to:
  - f85-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2021-drive-motor
see_also:
- f85-2021-drive-motor
- f85-2021-incline-position-sensor-pinout
- f85-2021-incline-motor-replacement
source:
  ref: sole-tm-f85-ent-2021-service-manual
  locator: section 3 General Information, printed page 14, and section 12-9, printed
    page 102
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

The 3 pin position sensor cable is separate from these four wires and has its own card.

**Note on the source.** Section 12-9 step 4 says "Connect incline motor wiring with controller" but this manual prints no wire-to-terminal list under that step. The colour to function mapping above comes from section 3 and from the incline motor control test page. The 2016 and 2019 manuals for the neighbouring builds print the list under step 4 as red to UP, white to COM, black to DOWN.
