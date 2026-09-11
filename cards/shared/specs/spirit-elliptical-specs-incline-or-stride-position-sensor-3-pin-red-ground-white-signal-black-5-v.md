---
id: spirit-elliptical-specs-incline-or-stride-position-sensor-3-pin-red-ground-white-signal-black-5-v
title: 'The 3-pin incline or stride position sensor: pin 1 red ground, pin 2 white
  position signal 0 to 5 V, pin 3 black 5 V DC'
kind: spec
question: What are the three pins of the incline or stride motor position sensor on
  a Spirit elliptical with a driver board?
asked_as:
- position sensor pinout on the ce850 stride motor
- which wire is the signal on the xe395 incline sensor
- incline vr sensor wires elliptical
- what voltage should the stride position sensor read
keywords:
- position sensor
- vr
- potentiometer
- 3-pin
- red ground
- white signal
- black 5vdc
- 0-5v
- inc vr
- stride sensor
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - ce850-2020
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-ce850-xe895-specs-stride-motor-115-v-ac-four-wires-and-position-sensor
- spirit-xe395-specs-incline-motor-120-or-115-v-ac-four-wires-and-position-sensor
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
- spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read
- spirit-ce850-2016-errors-stride-motor-and-position-sensor-test-115-vac
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: Incline Motor Position Sensor pin define and RPM sensor pin
    define, PDF p. 48 (printed 48), text.md lines 796-834; test values PDF p. 49,
    lines 834-870. XE895-2016: PDF p. 49, lines 797-835. XE395-2016: PDF p. 49, lines
    789-828. XE395ENT-2021: PDF p. 34, lines 433-461. CE850-2020: PDF p. 41, lines
    692-718, the same three pins without colours'
  extracted_at: '2026-09-11'
---

Every driver-board book prints the same three-pin table under the heading *Incline Motor Position
Sensor* - the CE850 and XE895 keep that heading for the sensor on their stride motor.

| Pin | Colour | Signal |
|---|---|---|
| 1 | Red | **Ground** |
| 2 | White | **Position signal, 0 ~ 5 V** |
| 3 | Black | **5 V DC** |

The **CE850-2020** prints the same order - 1 Ground, 2 Position, 3 5 Vdc - **without colours**.

**What the signal should read.** The test page of the 2016 books measures the same three pins at
the console connector: pin 3 = 5 VDC, pin 2 = 0-5 VDC depending on position, pin 1 = ground, and
expects about **4.5 ~ 4.7 VDC at the lowest position**, moving as the motor runs. A reading that
does not move, or is out of that window, is what the E3 / *Incline ERR* / *Stride ERR* cards
describe (`spirit-ce850-2016-errors-e3-stride-vr-out-of-range-or-not-read`).

The sensor lead lands on the driver board's VR socket (J12 *LIFT* on the CS62004, J7 *INC VR* on
the CS51007, J10 *INC VR* on the CS51005), and its signal reaches the console as the **IPOS** pin
of the 14-pin cable (`spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins`).

The same pages print the **RPM sensor** plug: four pins, **1 RPM1, 2 GND, 3 RPM2, 4 GND**, in the
2016 books and the ENT book; **two pins** in the CE850-2020 book, whose driver board has a 2-pin
RPM socket.

