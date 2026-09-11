---
id: spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
title: Elliptical circuit diagram with an appliance inlet and fuse, a controller with
  UP, COM and DOWN spades to an AC actuator, a 317-020004 gear motor and one or two
  speed sensors
kind: spec
question: What does the circuit diagram of a Spirit CE850-2016, XE395-2016 or XE895
  elliptical show?
asked_as:
- ce850 wiring diagram
- xe395 schematic xe539s
- xe895 circuit diagram
- what is 317-020004 on the elliptical schematic
keywords:
- circuit diagram
- wiring diagram
- schematic
- xe539s-se019-01
- xe895-se022-01
- appliance inlet
- fuse
- up com down
- 317-020004
- speed sensor
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2016
  - xe395-2016
  - xe895-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce850-2020-specs-circuit-diagram-xe898d-se028
- xe395ent-2021-specs-circuit-diagram-xe539s-se025
see_also:
- spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
- spirit-ce850-2016-xe395-xe895-specs-unit-block-diagram
- spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor
- spirit-elliptical-specs-motor-controller-fuse-5-a
source:
  ref: spirit-elliptical-xe895-2016-service-manual
  locator: 'XE895-2016: XE895-SE022-01 ELLIPICAL CIRCUIT DIAGRAM, PDF p. 54 (printed
    54), text.md lines 915-922. XE395-2016: XE539S-SE019-01 ELLIPTICAL CIRCUIT DIAGRAM,
    PDF p. 54, lines 908-915. CE850-2016: 8.4 ELLIPICAL CIRCUIT DIAGRAM, PDF p. 53,
    lines 914-920, the XE895 drawing reproduced without its title code. All flattened
    images read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

Three drawings of one layout. Reading down the page:

- **Console** at the top (labelled *XE895 電子錶* on the XE895 sheet, *XE539S* on the XE395 sheet,
  unlabelled on the CE850 sheet), with two leads to the **thumb switches** and two to the
  **hand-pulse** plates on the swing arms, and one loom down to the controller.
- **Mains**: a cord and plug into an **appliance inlet with a FUSE**, two spades to the
  **Controller**.
- **Controller** with **UP / COM / DOWN** spades; a three-wire cable from them runs to the AC
  **actuator** drawn at the bottom - the stride motor on the CE850 and XE895, the incline motor on
  the XE395 - together with the actuator's position-sensor lead back to the board.
- A 5-pin lead from the controller to the **gear motor, drawn as a box marked 317-020004**
  (blank on the CE850 sheet).
- **Speed sensors**: **SPEED SENSOR1 and SPEED SENSOR2** on the XE895 and CE850 sheets (the
  board's 4-pin RPM plug); **one SPEED SENSOR** on the XE395 sheet.

**The CE850-2016 sheet is a low-resolution copy of the XE895 drawing** - same console, same
two-sensor loom, same actuator - with the title code and the motor part number dropped. The
XE895 sheet is the one to read for the figures. 317-020004 is the same gear-motor number the
XE195, XE295 and XG400 sheets carry (`spirit-xe-2016-specs-circuit-diagram-317-020004-gear-motor`).

No wire colours are printed on any of the three; the actuator's colours are on the electrical
configuration page and the board's spade labels
(`spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections`). The 2020 CE850 and the
XE395ENT print different drawings with named cables
(`ce850-2020-specs-circuit-diagram-xe898d-se028`, `xe395ent-2021-specs-circuit-diagram-xe539s-se025`).

