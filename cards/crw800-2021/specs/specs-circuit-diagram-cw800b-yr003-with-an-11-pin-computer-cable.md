---
id: crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable
title: 'Rower schematic CW800B-YR003: an 11-pin computer cable to the console, an
  8-pin cable to the gear motor, 3-pin generator cables and a transistor-output speed
  sensor'
kind: spec
question: What does the circuit diagram of the Spirit crw800-2021 rower service manual
  show?
asked_as:
- crw800 wiring diagram
- cw800b-yr003 rower schematic
- how many pins is the crw800 computer cable
- where does the speed sensor plug in on the crw800 2020
keywords:
- circuit diagram
- schematic
- cw800b-yr003
- yr003 console
- 11 pin computer cable
- 8 pin computer cable
- 3 pin cable
- generator
- speed sensor
- rf module
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
- spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
see_also:
- crw800-2021-specs-generator-controller-ae0076-connector-definition
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
- crw800-2021-specs-display-board-aa0210-photographed
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 9. Circuit diagram (CRW800), PDF p. 41 (printed 40), text.md line 620;
    a flattened line drawing read from a 170 dpi render (OCR supplement lines 1449-1491)
  extracted_at: '2026-09-11'
---

The sheet is titled **#CW800B-YR003 ROWER SCHEMATIC** and the console block **YR003 CONSOLE** - the
same drawing code the 2021 owner's-manual parts list heads itself with.

**Console side.** One **11 PIN COMPUTER CABLE** leaves the console and runs down the mast. At its
lower end it meets two plugs: an **8 pin / 8 pin** junction and a **3 pin / 3 pin** junction.

**Gear motor.** An **8 PIN COMPUTER CABLE** from the **GEAR MOTOR** plugs into the 8-pin junction.
A **3 PIN CABLE** from the generator controller's **JK3** runs up to a second connector on the
motor - so the motor is the junction box: generator power in on 3 pins, motor and console lines
out on 8.

**Generator.** **GENERATOR** -> **3 PIN CABLE** -> **JK 1** on the **GENERTOR CONTROLLER** [sic].

**Speed sensor.** A **TRANSISTOR OUTPUT SENSOR** on a lead labelled **SPEED SENSOR** plugs into the
3-pin junction of the 11-pin cable.

**Handlebar.** Drawn on its own with an **RF Module** inside the grip and no wire to anything - the
resistance buttons are wireless.

**No adapter, no plug, no switch and no fuse are drawn.** No pin of any cable is defined anywhere
in the book. The 2016 CRW800 and XRW600 books draw a wholly different circuit with a 12 V adapter
(`spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor`).

The JK 1 / JK3 socket names on this sheet are the reverse of the generator-controller page's
(`crw800-2021-specs-generator-controller-ae0076-connector-definition`).

