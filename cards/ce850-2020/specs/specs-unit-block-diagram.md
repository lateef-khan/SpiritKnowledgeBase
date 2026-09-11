---
id: ce850-2020-specs-unit-block-diagram
title: Block diagram with a transformer on the driver board, a stride motor and VR
  set, and no tension motor or amplifier block
kind: spec
question: What does the unit block diagram of a Spirit ce850-2020 elliptical show?
asked_as:
- ce850 2020 block diagram
- how are the boards connected on the 2020 ce850
- does the ce850 block diagram show the gear motor
- ce850 signal flow
keywords:
- block diagram
- display board
- driver board
- transformer
- stride motor
- vr set
- rpm sensor
- power switch
- fuse
- thumb switch
facets:
  brand:
  - spirit
  product_line: elliptical
  model: ce850-2020
  applies_to:
  - ce850-2020
  section: specs
  code: '*'
  model_number:
  - '850040'
authority: 3
not_to_be_confused_with:
- spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram
see_also:
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- ce850-2020-specs-circuit-diagram-xe898d-se028
- ce850-2020-specs-display-board-cs24005-and-interface-board-connections
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: Section 5 Unit Block Diagrams, Elliptical Configuration, PDF p. 18 (printed
    18), text.md lines 355-361; the drawing is a flattened image read from a 300 dpi
    render (OCR supplement lines 1121-1141)
  extracted_at: '2026-09-11'
---

**Into the DISPLAY BOARD:** KEY, HR HANDLEBAR, WIRELESS HR RECEIVER, THUMB SWITCH.
**Out of the display board:** COOLING FAN.
**Display board and DRIVER BOARD** exchange signals both ways.
**Into the driver board:** POWER -> POWER SWITCH -> FUSE, RPM SENSOR, **VR SET**.
**Driver board and TRANSFORMER** - a double-headed arrow.
**Out of the driver board:** **STRIDE MOTOR**.

Three things the 2016 drawing had are gone: the **tension motor block**, the **amplifier and
speakers**, and the *incline motor* label - the actuator is at last called a stride motor. The
missing tension-motor block is a defect of the drawing, not of the machine: the gear motor is on
the driver board's J9, on the circuit diagram as *GEAR MOTOR, 5 PIN Motor wire*, and in the
electrical configuration as *TENSION MOTOR (GEAR MOTOR)*.

The transformer is the one the circuit diagram wires to J5 and J12
(`ce850-2020-specs-circuit-diagram-xe898d-se028`). The 2016 books' drawing is
`spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram`.

