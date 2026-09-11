---
id: spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor
title: 'Circuit diagram of the adapter-fed ellipticals: console, hand pulse, thumb
  switches, a DC jack and adapter, a 317-020004 gear motor and one or two speed sensors,
  with no lower board'
kind: spec
question: What does the circuit diagram of a Spirit XE195, XE295 or XG400 elliptical
  show?
asked_as:
- xe195 wiring diagram
- xe295 schematic xe519s
- xg400 circuit diagram se551
- what is 317-020004 on the xe295 schematic
keywords:
- circuit diagram
- wiring diagram
- schematic
- xe509s-se021
- xe519s-se020
- se551-se023
- 317-020004
- gear motor
- speed sensor
- dc jack
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe195-2016
  - xe295-2016
  - xg400-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
see_also:
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
- spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers
source:
  ref: spirit-elliptical-xe295-2016-service-manual
  locator: 'XE295-2016: XE519S-SE020-01-01 Elliptical CIRCUIT DIAGRAM, PDF p. 40 (printed
    40), text.md lines 621-628. XE195-2016: XE509S-SE021-01-01-01, PDF p. 40, lines
    620-627. XG400-2016: SE551-SE023-01-01, PDF p. 38, lines 562-569. All flattened
    images read from 300 dpi renders (OCR supplement lines 1653-1665, 1619-1638, 1302-1316)'
  extracted_at: '2026-09-11'
---

Three sheets of one layout, each titled with its machine's drawing code:

| Book | Sheet title | Speed sensors | Thumb switch |
|---|---|---|---|
| XE195 | **XE509S-SE021-01-01-01** | one, *SPEED SENSOR* | none drawn |
| XE295 | **XE519S-SE020-01-01** | two, *SPEED SENSOR1 / 2* | *LEVEL* |
| XG400 | **SE551-SE023-01-01** | two, *SPEED SENSOR1 / 2* | none drawn |

Common to all three: the **console** at the top (labelled with the drawing code and 電子錶,
"electronic meter"), two leads to the **hand-pulse** plates and two to the swing-arm plugs; one loom
down the mast that fans out at the bottom into a plug for the **gear motor, a box marked
317-020004**, the speed sensor lead(s), and a lead to the **DC jack**, which is drawn with the
**adapter** beside it.

**There is no controller, no inlet and no fuse** on any of the three sheets - the console is the
only board (`spirit-xe-2016-specs-unit-block-diagram-no-driver-board`). **No wire colours or pin
numbers** are printed; the loom's pins are on
`spirit-xe-2016-specs-console-to-driver-board-14-pin-definition-ten-pins-used` and the motor
plug on `spirit-elliptical-specs-tension-motor-connector-5-pin-definition`. The same 317-020004
gear motor appears on the XE395, XE895 and CE850 sheets, there driven through a controller
(`spirit-ce850-2016-xe395-xe895-specs-circuit-diagram`).

