---
id: xe795-2016-specs-unit-block-diagram
title: Block diagram of the 2016 generator elliptical with the RPM sensor into the
  display board, an amplifier, and a generator into the driver board driving the generator
  brake
kind: spec
question: What does the unit block diagram of a Spirit xe795-2016 elliptical show?
asked_as:
- xe795 2016 block diagram
- where does the rpm sensor go on the xe795
- xe795 signal flow between the boards
- does the xe795 block diagram show an adapter
keywords:
- block diagram
- display board
- driver board
- generator
- generator brake
- rpm sensor
- amplifier
- speaker
- line in
- cooling fan
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2016
  applies_to:
  - xe795-2016
  section: specs
  code: '*'
  model_number:
  - '795015'
authority: 3
not_to_be_confused_with:
- xe795-2023-specs-unit-block-diagram
- spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram
see_also:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xe795-2016-specs-display-amplifier-and-interface-board-connections
- xe795-2016-specs-circuit-diagram-xe815-se024
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: Section 5 Unit Block Diagrams, Elliptical Configuration, PDF p. 24 (printed
    24), text.md lines 400-406; the drawing is a flattened image read from a 300 dpi
    render (OCR supplement lines 1215-1239)
  extracted_at: '2026-09-11'
---

**Into the DISPLAY BOARD:** KEY, HR HANDLEBAR, WIRELESS HR RECEIVER, and **RPM SENOR** (spelt so).
**Out of the display board:** COOLING FAN, and an **AMPLIFIER** with **SPEAKER** and **LINE IN**.
No thumb-switch block is drawn, though the display board has a LEVEL thumb-switch socket.
**Display board and DRIVER BOARD** exchange signals both ways.
**Into the driver board:** **GENERATOR**.
**Out of the driver board:** **GENERATOR BRAKE**.

**The RPM sensor goes to the display board**, matching the CS11020's J3 *RPM IN* socket and the
RPM pin on the 6-pin console cable - the 031101B controller has no sensor socket. **No mains,
adapter or fuse block** is drawn: the generator is the only power source.

The 2023 book moves the sensor to the driver board and drops the amplifier
(`xe795-2023-specs-unit-block-diagram`). The 2016 XBR95 bike and the 2012 CU800 draw the same
generator-into-driver-board layout (`spirit-xbr95-2016-cu800-2012-specs-unit-block-diagram`).

