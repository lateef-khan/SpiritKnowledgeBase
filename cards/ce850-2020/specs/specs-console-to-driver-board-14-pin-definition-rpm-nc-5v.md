---
id: ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v
title: The 14-pin console-to-driver cable with a single RPM line on pin 6, NC on pin
  8 and 5 V on pin 9
kind: spec
question: What are the fourteen pins of the console-to-driver-board cable on a Spirit
  ce850-2020 elliptical?
asked_as:
- ce850 2020 14 pin cable pinout
- which pin is rpm on the ce850 system cable
- ce850 computer cable pin definition
- why is pin 8 nc on the ce850 cable
keywords:
- 14-pin
- console cable
- system cable
- computer cable
- pin define
- pinout
- rpm
- nc
- inc+ inc- ipos
- mpos
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2020
  applies_to:
  - ce850-2020
  section: specs
  code: '*'
  model_number:
  - '850040'
authority: 3
not_to_be_confused_with:
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
see_also:
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- ce850-2020-specs-circuit-diagram-xe898d-se028
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: Console to Driver board wire pin define, PDF p. 40 (printed 40), text.md
    lines 660-692; RPM sensor pin define, PDF p. 41, lines 692-718
  extracted_at: '2026-09-11'
---

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | MTR- | 8 | **NC** |
| 2 | MTR+ | 9 | **5V** |
| 3 | +5V | 10 | +12V |
| 4 | MPOS | 11 | GND |
| 5 | GND | 12 | INC+ |
| 6 | **RPM** | 13 | INC- |
| 7 | GND | 14 | IPOS |

Eleven of the fourteen rows match the 2016 CE850 table
(`spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins`). The three
that differ follow the hardware: this machine's driver board (CS51007) has a **2-pin RPM socket**
and the RPM sensor table on the next page lists two pins, so the second RPM line of the 2016 cable
is gone - pin 6 is plain **RPM**, pin 8 is **NC**, and pin 9 carries **5V** where the 2016 cable
had a ground.

INC+, INC- and IPOS still drive and read the stride actuator; MTR-, MTR+, +5V and MPOS still pass
through to the 5-pin gear-motor plug
(`spirit-elliptical-specs-tension-motor-connector-5-pin-definition`). The circuit diagram draws
this cable as the **14 PIN COMPUTER CABLE** between MAIN CONNECTOR and MAIN CONNECT
(`ce850-2020-specs-circuit-diagram-xe898d-se028`).

