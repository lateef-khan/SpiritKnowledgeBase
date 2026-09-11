---
id: ce850-2020-specs-circuit-diagram-xe898d-se028
title: Schematic with a power cord into a fused appliance inlet, a transformer, a
  14-pin computer cable, 3-pin and 4-pin hand-pulse cables, four 3-pin handle wires,
  a 5-pin gear-motor wire and a grounded stride motor
kind: spec
question: What does the circuit diagram of a Spirit ce850-2020 elliptical show?
asked_as:
- ce850 2020 wiring diagram
- xe898d schematic
- how many pins is the computer cable on the ce850
- which handle wire is incline on the ce850 schematic
keywords:
- circuit diagram
- schematic
- xe898d-se028
- appliance inlet
- transformer
- 14 pin computer cable
- handle wire
- 5 pin motor wire
- inc vr
- rpm sensor wire
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
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
see_also:
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v
- ce850-2020-specs-unit-block-diagram
- ce850-2020-specs-motor-controller-fuse-10-a-with-a-t2-0a-on-the-board
source:
  ref: spirit-elliptical-ce850-2020-service-manual
  locator: '8.4 CIRCUIT DIAGRAM, #XE898D-SE028 SCHEMATIC, PDF p. 46 (printed 46),
    text.md lines 797-803; the drawing is a flattened image read from a 300 dpi render
    (OCR supplement lines 1602-1656)'
  extracted_at: '2026-09-11'
---

The drawing is headed **#XE898D-SE028 SCHEMATIC** - the XE898 code of the CE850 family with a D
suffix. Every cable is named:

**Mains.** POWER CORD -> **APPLIANCE INLET** (with FUSE) -> two **Red wires** to the controller and a
**GROUNDING** lead. A **TRANSFORMER** hangs off the controller: **Black wire to J5, Blue wire to
J12**.

**Console.** **HP-RIGHT on a 3 PIN CABLE** and **HP-LEFT on a 4 PIN CABLE** to the two HANDPULSE
SENSOR plates. Two **HAND KEY** sockets take **3 PIN Handle Wire (Upper), Resistance** and **3 PIN
Handle Wire (Upper), Incline**; each continues as a **3 PIN Handle Wire (Lower)** to the **Handle
Switch Bracket**. **MAIN CONNECTOR** to the controller's **MAIN CONNECT** by a **14 PIN COMPUTER
CABLE**.

**Controller.** **UP - Red wire, COM - White wire, DOWN - Black wire** and **INC VR - 3 Pin VR
Cable** to the **STRIDE MOTOR**, which has its own **GROUNDING**. **MOTOR - 5 pin Motor W/cable**
to a **5 PIN** plug and the **GEAR MOTOR**'s **5 PIN Motor wire**. **RPM SEN - RPM Sensor wire**.

**The thumb-switch wires are labelled "Incline" on a machine whose actuator is a stride motor** -
the same inheritance as the *INC VR* silkscreen on the board. The 4-pin left hand-pulse cable
carries the extra wire, as on the CE800-2021 schematic. J5/J12 for the transformer matches the
CS51007 photograph, not the CS 62004 drawing
(`ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections`). The 14-pin cable's
signals are on `ce850-2020-specs-console-to-driver-board-14-pin-definition-rpm-nc-5v`.

