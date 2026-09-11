---
id: xrw600-2019-specs-unit-block-diagram-ac-adapter-motor-and-j13
title: Unit block diagram with the AC adapter feeding the motor and the motor feeding
  the console's system socket, plus a radio pulse receiver and an optocoupler switch
kind: spec
question: What does the unit block diagram of the Spirit xrw600-2019 rower service
  manual show?
asked_as:
- block diagram of the xrw600
- how does power get to the xrw600 console
- what is j13 on the xrw600 console
- dw400 block diagram
keywords:
- block diagram
- model dw400
- ac adapter
- motor
- j13
- console
- key board
- radio pulse
- rf pulse
- optocoupler switch
facets:
  brand:
  - spirit
  product_line: rower
  model: xrw600-2019
  applies_to:
  - xrw600-2019
  section: specs
  code: '*'
  model_number:
  - '600976'
authority: 3
not_to_be_confused_with:
- crw800-2016-specs-unit-block-diagram-power-switch-and-hr-handlebar
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
see_also:
- xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor
- spirit-crw800-2016-xrw600-specs-power-adapter-12-v-1-5-a-through-a-dc-jack
- spirit-crw800-2016-xrw600-specs-circuit-diagram-12-v-adapter-and-yj-9900-gear-motor
source:
  ref: spirit-rower-xrw600-2019-service-manual
  locator: 5. DW400-YR002 Unit Block Diagrams, PDF p. 23 (printed 22), text.md line
    361; a flattened image read from a 110 dpi render (OCR supplement lines 1165-1177)
  extracted_at: '2026-09-11'
---

A different drawing from the CRW800 books', and the only one of the three rower block diagrams
that names a connector. Its title block reads **Model DW400**.

- **POWER INPUT** (a mains plug) -> **AC ADAPTER** -> **MOTOR**.
- **MOTOR** -> **J13** on the **CONSOLE**. The console's power comes up through the motor, which is
  why the E2 page says the tension motor "supply the console DC12V power" and the no-display
  troubleshooting checks "has the tension motor output DC12V".
- **OPTOCOUPLER SWITCH** joins the motor-to-J13 line - the speed sensor, which the same book's
  section 8.8 calls the *Photo coupler sensor (RPM sensor device)*.
- **RADIO PULSE** -> **RF PULSE** socket on the console - the wireless heart-rate receiver.
- **KEY BOARD** is drawn as a strip along the bottom of the console block.

**No power switch, no fuse, no HR handlebar and no RF level control.** The XRW600 has no
resistance buttons on the handle; its motor plug carries the extra COUNT, ZERO and SPEED lines that
the console needs instead (`xrw600-2019-specs-tension-motor-connector-8-pin-and-2-pin-speed-sensor`).

J13 is the long white socket on the bottom of the AA0127 display board
(`spirit-crw800-2016-xrw600-specs-display-board-aa0127-with-and-without-the-rf-module`).

