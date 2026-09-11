---
id: spirit-ct800-specs-driver-board-connector-locations
title: Driver board connectors on the 3.5 horsepower 110 volt lower controller
kind: spec
question: Where are the connectors on the driver board of a Spirit CT800 2020 or CT800ENT
  treadmill?
asked_as:
- ct800 2020 lower controller connectors
- where does the console plug into the ct800 driver board
- dc motor m plus and m minus on the ct800
- what is the rating printed on the ct800 controller
keywords:
- driver board
- lower controller
- connector
- incline vr
- reed switch
- dc motor
- ac fan
- ac in
- console
- horsepower
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2020
  - ct800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-driver-board-connector-locations
- ct800-2016-specs-driver-board-connectors-and-leds
see_also:
- spirit-ct800-specs-electrical-part-descriptions
- ct800-2020-specs-circuit-diagram
- ct800ent-2022-specs-circuit-diagram
- spirit-ct800-specs-no-specification-table
source:
  ref: spirit-treadmill-ct800-2020-service-manual
  locator: 'CT800-2020: PDF p. 29 (printed 28), section 6-1-5 ''DRIVER BOARD PCB Component
    Locations(YT057)'', text.md lines 374-379, OCR supplement lines 1261-1284, read
    from the render. CT800ENT-2022: PDF p. 18 (printed 18) ''Driver Board PCB Component
    Locations'', lines 305-336'
  extracted_at: '2026-09-11'
---

Both books photograph the same board and caption it **PA-AE00301L-002, 3.5HP / 110V**. The 2020 book
tags the section **(YT057)**; the ENT book calls the console plug "Connection to Console STD control".
The board silkscreen reads AE00301L-001 and its sticker AE00300C_170720_V1.1; a 110VAC capacitor and a
fuse sit near the AC input.

Call-outs, going round the board:

| Call-out | What it is |
|---|---|
| CONNECTION TO CONSOLE (STD control) | red multi-way socket at the top edge |
| REED SWITCH SENSOR | speed sensor |
| INCLINE VR | 3-pin position sensor |
| DC MOTOR M+ / DC MOTOR M- | drive motor |
| INCLINE UP / COM / DOWN | incline motor power, three spade terminals |
| AC FAN | heat-sink fan, N and L spades |
| AC IN N / L | mains in |

The circuit diagram of the CT800-2020 numbers the same board's plugs **JK90** (6-pin console), **JK60**
(Incline-VR), **JK81** (UP / COM / DOWN), **JK50** (sensor), **FAN120 / FAN121** and **AC IN(1) N / AC
IN(2) L**.

**3.5HP / 110V is printed on the driver board, not on the motor.** No CT800 book prints a drive-motor
horsepower anywhere else, and the owner's-manual absence card still stands for the motor itself.

The CT850-2020's lower controller is a boxed Rhymebus inverter with U / V / W motor terminals; do not read
this DC board's call-outs against it.
