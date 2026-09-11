---
id: spirit-xt-specs-incline-sensor-pinout-pin-1-ground
title: 'Incline position sensor: pin 1 is ground, pin 2 the position signal, pin 3
  5 volts, and the books disagree on the wire colours'
kind: spec
question: What is the pinout of the 3-pin incline position sensor on a Spirit XT385,
  XT485, XT685, XT485ENT or XT685ENT treadmill, or a 2023 XT185 / XT285?
asked_as:
- incline vr pinout xt385
- which pin is ground on the xt485 incline sensor
- incline sensor wire colours xt685
- position sensor red white black which is 5 volts
keywords:
- incline sensor
- position sensor
- vr
- potentiometer
- pinout
- 3 pin
- 5vdc
- position signal
- incline motor
- wire colour
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2023
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v
- f80-2023-incline-sensor-connector-pinout
see_also:
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
- spirit-xt-ent-specs-driver-board-connectors
- spirit-xt-errors-e3-incline-test-procedure-nine-steps
- spirit-xt-2023-errors-e3-incline-vr-out-of-range
- xt485ent-2023-errors-e3-incline-vr-out-of-range
- spirit-xt-assembly-incline-motor-replacement-225mm
source:
  ref: spirit-treadmill-xt385-2015-service-manual
  locator: 'XT385-2015: PDF p. 49 (printed 48), Incline motor wire define, text.md
    lines 719-732; test p. 50, line 766. XT485-2015: p. 49, lines 720-733; test p.
    50, line 770. XT185-2023: p. 26, OCR supplement lines 1705-1719; test lines 559-561.
    XT285-2023: p. 27. XT385-2023 / XT485-2023: p. 28 (OCR). XT685-2023: p. 27 (OCR).
    XT485ENT: p. 45, lines 636-658; test p. 46, lines 687-690. XT685ENT: p. 32 (OCR)'
  extracted_at: '2026-09-11'
---

**The pin order is the same in all nine books**: **Pin 1 = ground, Pin 2 = position signal (0~5vdc), Pin
3 = 5vdc**, and the incline power wires are **RED - UP, WHITE - COM (the XT485ENT says NEUTRAL), BLACK -
DOWN**.

**The wire colours of the sensor cable are not.**

| Books | Sensor wire colours as printed |
|---|---|
| XT385-2015, XT485-2015, XT685-2023, XT485ENT, XT685ENT | **Black = Ground, White = Position signal, Red = 5vdc** |
| XT185-2023, XT285-2023, XT385-2023, XT485-2023 | **P1 GND (Red), P2 Position signal (White), P3 +5Vcc (Black)** |

Red and black are swapped between the two groups, and the four 2023 books that swap them are the same
model year as the XT685-2023 that does not. Nothing in any book explains the change; a new sensor cable
may be either. Identify the pins by function - ground, wiper, 5 volts - with a meter, not by colour.

The XT185-2015 / XT285-2015 books print the opposite pin order (pin 1 = 5vdc). The Sole F80 prints the
same ground-first order for its own sensor (`f80-2023-incline-sensor-connector-pinout`); it is a
different brand and board.
