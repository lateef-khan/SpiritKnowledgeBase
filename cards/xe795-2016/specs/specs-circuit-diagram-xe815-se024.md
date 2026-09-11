---
id: xe795-2016-specs-circuit-diagram-xe815-se024
title: 'Circuit diagram titled with the XE815 drawing code: console cable, generator
  white, black and red lead, red brake lead, an empty fourth socket on the 031101B
  and a speed sensor lead, with no adapter or inlet'
kind: spec
question: What does the circuit diagram of a Spirit xe795-2016 elliptical show?
asked_as:
- xe795 2016 wiring diagram
- xe815 schematic
- which generator wire goes to cn1 on the xe795
- does the xe795 circuit diagram show an adapter
keywords:
- circuit diagram
- wiring diagram
- schematic
- xe815-se024-01
- 031101b
- cn1 cn2 cn3 cn4
- generator
- white black red
- speed sensor
- hand pulse
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
- xe795-2023-specs-circuit-diagram-6-pin-computer-cable
- ce800-2016-specs-circuit-diagram-xe890b-ae10m
see_also:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xe795-2016-specs-console-to-driver-board-6-pin-definition
- xe795-2016-specs-unit-block-diagram
- spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b
source:
  ref: spirit-elliptical-xe795-2016-service-manual
  locator: XE815-SE024-01 ELLIPTICAL CIRCUIT DIAGRAM, PDF p. 42 (printed 42), text.md
    lines 609-616; the drawing is a flattened image read from a 300 dpi render (OCR
    supplement lines 1481-1487)
  extracted_at: '2026-09-11'
---

The sheet is headed **XE815-SE024-01 ELLIPTICAL CIRCUIT DIAGRAM** - XE815 being the XE795's drawing
code, which also labels the console box.

- **Console** with two plugs to the **hand-pulse** plates (drawn as two twin-pad blocks) and one
  console cable down the right side of the sheet to **CN3** on the controller.
- **Controller #031101B** with **CN1**, **CN4** and **CN2** down its left edge and CN3 at its right.
- **Generator** on the flywheel: a **WHITE, BLACK, RED** three-wire lead to **CN1**, and a **RED**
  two-wire lead from the brake coil to **CN2**. **CN4 has nothing wired to it.**
- A **speed-sensor** lead drawn separately with a three-pin plug that meets the console cable near
  the controller - the sensor rides up the console loom to the display board's RPM IN.

**No adapter, DC jack, inlet or fuse** is drawn: the generator is the only power source. **No
thumb-switch leads** are drawn either, though the display board has a LEVEL thumb-switch socket.
The 2012 CU800 and 2016 XBR95 bikes print the same 031101B layout
(`spirit-xbr95-2016-cu800-2012-specs-circuit-diagram-031101b`); the CE800-2016's sheet adds the
9-pin/6-pin console cable split (`ce800-2016-specs-circuit-diagram-xe890b-ae10m`). The 2023 XE795
redraws the machine around a CS52005-23 (`xe795-2023-specs-circuit-diagram-6-pin-computer-cable`).

