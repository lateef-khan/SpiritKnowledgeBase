---
id: crw800-2021-specs-generator-controller-ae0076-connector-definition
title: 'Generator controller AE0076: a 3-pin AC input from the generator on JK3 and
  a 3-pin DC output, positive on 1 and negative on 3'
kind: spec
question: What are the connectors on the generator controller of the Spirit crw800-2021
  rower, and what does the board do?
asked_as:
- generator controller pins on the crw800
- ae0076 board
- which pin is positive on the rower generator controller output
- what does the generator on the crw800 2020 feed
keywords:
- generator controller
- ae0076
- generator input
- jk3
- output dc
- positive
- negative
- ac
- generator
- rectifier
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2021
  applies_to:
  - crw800-2021
  section: specs
  code: '*'
  model_number:
  - '800940'
authority: 3
not_to_be_confused_with:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
see_also:
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
- crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable
- crw800-2024-specs-resistance-system
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 6-1-4 GENERATOR CONTROLLER CONNECTOR DEFINITION FUNCTION, PDF p. 29 (printed
    28), text.md lines 385-404 (the two pin lists are native text); the board photograph
    read from a 110 dpi render (OCR supplement lines 1409-1426); generator motor and
    controller board replacement, PDF pp. 61-62, lines 924-957
  extracted_at: '2026-09-11'
---

The board is silkscreened **AE0076-V1.0-20200218**, carries an **EE19-9V** transformer, and has two
connectors:

**GENERATOR INPUT - JK3, red three-way at the right edge**

| Pin | Signal |
|---|---|
| 1 | **AC** |
| 2 | **N/A** |
| 3 | **AC** |

**OUTPUT DC - three pins at the left edge, numbered 1 2 3**

| Pin | Signal |
|---|---|
| 1 | **POSITIVE** |
| 2 | **N/A** |
| 3 | **NEGATIVE** |

The generator on the flywheel makes AC; this board rectifies it to DC. Where the DC goes is drawn
on the circuit diagram: a 3-pin cable from **JK3** runs to the **gear motor**, and the console is
fed on from there over the 8-pin and 11-pin computer cables
(`crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable`). The E2 page's
last step is "check the generator controller socket terminals whether the voltage, if not please
change another one controller". **No output voltage is printed** for the board anywhere in the
book.

**The 2020-version rower has no mains adapter on any drawing.** Its block diagram has no power
block, its schematic has no plug, and chapter 11 replaces a *Generator motor* (loosen the M8x7T
idle-wheel nut, remove the button socket cap screw) and a *Controller board* (four M5x10L screws
with the machine lying down). The 2016 CRW800 and the XRW600 are adapter-powered instead
(`spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack`).

**Two callouts from the schematic disagree with this page.** The schematic labels the generator's
cable into the controller **JK 1** and the output socket **JK3**; this page photographs the
generator input on **JK3**. Meter the board, not the label.

The 2016 ellipticals' generator controller is a different board with different sockets
(`spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections`).

