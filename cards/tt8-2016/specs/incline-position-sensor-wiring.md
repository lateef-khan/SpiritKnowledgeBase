---
id: tt8-2016-incline-position-sensor-wiring
title: Incline position sensor pinout and voltages
kind: spec
question: What voltages should the incline position sensor read on a Sole tt8-2016
  treadmill?
asked_as:
- what should the incline potentiometer read
- incline position sensor pinout
- 5 volts on the incline sensor
keywords:
- position sensor
- potentiometer
- incline vr
- pin 1
- pin 2
- pin 3
- 5vdc
- 0-5v
- wiring
facets:
  brand:
  - sole
  product_line: treadmill
  model: tt8-2016
  applies_to:
  - tt8-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tt8-2016-ac-incline-position-sensor-wiring
see_also:
- tt8-2016-incline-vr-test-procedure
- tt8-2016-e3-error-code
source:
  ref: sole-tm-tt8-2016-service-manual
  locator: General Information, page 13
  extracted_at: '2026-09-04'
---

**DC model: TT8 2016 ST925-YT021, DC drive motor. The AC inverter TT8 2016 (ST925A-YT030) is a different machine and this card does not apply to it.**

The 3-pin connector is wired the same at the incline board and at the console:

| Pin | Signal |
|---|---|
| 1 | Ground |
| 2 | Position signal 0~5 Vdc |
| 3 | 5 Vdc |

Expected readings at the potentiometer: **5 Vdc between the black and red wire**, and a voltage between the
red and white wire that sits around **4.5 to 4.7 Vdc when the motor is at the lowest position**. The exact
figure is not critical as long as it is in that neighbourhood.

The wiring diagram labels the three position sensor wires directly:

- **Black = ground**
- **White = position signal**
- **Red = 5 Vdc**

The white wire carries 0~5 V depending on incline position.
