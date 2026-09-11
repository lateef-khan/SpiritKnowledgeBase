---
id: crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
title: Unit block diagram with a generator feeding a generator controller and the
  tension motor, and RF level control from the handlebar
kind: spec
question: What does the unit block diagram of the Spirit crw800-2021 rower service
  manual show?
asked_as:
- block diagram of the crw800 rower
- how is the crw800 2020 wired up
- does the crw800 have a generator
- what does the rf level control on the rower handle talk to
keywords:
- block diagram
- generator
- generator controller
- tension motor
- display board
- rf level control
- handlebar
- wireless hr receiver
- rpm sensor
- key
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
- crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar
- xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
see_also:
- crw800-2021-specs-generator-controller-ae0076-connector-definition
- crw800-2021-specs-circuit-diagram-cw800b-yr003-with-an-11-pin-computer-cable
- crw800-2024-specs-resistance-system
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 5. CRW800 Unit Block Diagrams, PDF p. 24 (printed 23), text.md line 355;
    the diagram is a flattened image read from a 110 dpi render (OCR supplement lines
    1358-1371 is rotated)
  extracted_at: '2026-09-11'
---

Seven blocks. The **DISPLAY BOARD** is the centre and carries a **KEY** block inside it.

- **RF LEVEL CONTROL (HANDLEBAR)** <-> DISPLAY BOARD - a double-headed open arrow, the only
  wireless link on the drawing: the resistance buttons on the handle talk to the console by
  radio.
- **WIRELESS HR RECEIVER** -> DISPLAY BOARD.
- **GENERATOR** -> **GENERATOR CONTROLLER** -> **TENSION MOTOR** -> DISPLAY BOARD, drawn as one
  chain of blue arrows: the generator's output goes through the controller, and the power reaches
  the display board *through the tension motor block*. The display board also drives the tension
  motor (a black arrow back down).
- **RPM SENSOR** -> DISPLAY BOARD.

**There is no POWER, POWER SWITCH or AC ADAPTER block.** The 2016 CRW800 and the XRW600 diagrams
have one (`crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar`,
`xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13`); this 2020-version machine draws
its power from the generator on the flywheel. Chapter 11 of the same book adds a **Generator motor
replacement** and a **Batteries replacement** ("a screw of battery cover on the back of console")
that the 2016 book does not have, and its console-problem page says to "check the generator power
is the normal power supply". The generator controller's sockets are on
`crw800-2021-specs-generator-controller-ae0076-connector-definition`.

**No hand-pulse block.** The 2016 diagram has an HR HANDLEBAR block; this one has only the wireless
receiver, and the electronic-parts page names a *Built-in Heart Rate Receiver* on the console.

