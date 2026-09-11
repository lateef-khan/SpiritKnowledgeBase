---
id: spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram
title: Block diagram with a driver board fed through a power switch and fuse, driving
  a tension motor and an incline motor with a VR set, and an amplifier with speakers
kind: spec
question: What does the unit block diagram of a Spirit CE850-2016, XE395, XE395ENT
  or XE895 elliptical show?
asked_as:
- ce850 block diagram
- xe395 signal flow between the boards
- does the xe895 block diagram show a stride motor
- xe395ent block diagram
keywords:
- block diagram
- display board
- driver board
- tension motor
- incline motor
- vr set
- amplifier
- speaker
- line in
- line out
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe395-2016
  - xe395ent-2021
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce850-2020-specs-unit-block-diagram
- spirit-xe-2016-specs-unit-block-diagram-no-driver-board
see_also:
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
- xe395ent-2021-specs-circuit-diagram-xe539s-se025
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: section 5 Unit Block Diagrams, Elliptical Configuration, PDF
    p. 24 (printed 24), text.md lines 462-468. XE895-2016: PDF p. 24, lines 457-463.
    XE395-2016: PDF p. 24, lines 452-458. XE395ENT-2021: PDF p. 15, lines 193-199.
    All flattened images read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

Four books print one drawing with small differences in the audio corner.

**Into the DISPLAY BOARD:** KEY, HR HANDLEBAR, WIRELESS HR RECEIVER, THUMB SWITCH.
**Out of the display board:** COOLING FAN, and an **AMPLIFIER** that feeds **SPEAKER L/R**.
**Display board and DRIVER BOARD** exchange signals both ways.
**Into the driver board:** **POWER -> POWER SWITCH -> FUSE**, RPM SENSOR, **VR SET**.
**Out of the driver board:** **TENSION MOTOR**, **INCLINE MOTOR**.

| Book | Audio blocks beside the amplifier |
|---|---|
| CE850-2016 | LINE IN and LINE OUT |
| XE895-2016 | LINE IN and LINE OUT |
| XE395-2016 | LINE IN only |
| XE395ENT-2021 | LINE OUT only |

**The CE850 and XE895 have no incline.** Their drawing keeps the *INCLINE MOTOR* block for the
stride actuator, as their outline drawings keep the *Incline Motor* label; *VR SET* is that
actuator's position sensor. **The CE850 and XE895 list no amplifier or speakers** in their
electronic-parts chapter either - the audio corner is inherited from the XE395 drawing. On the
XE395ENT the speakers are driven from the display board and the "amplifier" block has no
separate board behind it.

Power is mains through a switch and a fuse into the driver board: none of these four machines
has an adapter. The 2020 CE850 redraws the lower half with a transformer and a stride motor
(`ce850-2020-specs-unit-block-diagram`); the XE195/XE295/XG400 have no driver board at all
(`spirit-xe-2016-specs-unit-block-diagram-no-driver-board`).

