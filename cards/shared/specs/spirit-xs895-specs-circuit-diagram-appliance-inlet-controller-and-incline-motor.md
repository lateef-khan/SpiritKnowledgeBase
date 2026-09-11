---
id: spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor
title: Circuit diagram with an appliance inlet and fuse feeding a controller on ACN
  and ACL, an 11-pin computer cable, an 8-pin motor cable and an incline motor on
  red, white and black wires plus a 3-pin VR cable
kind: spec
question: What does the circuit diagram of the Spirit XS895 incline stepper service
  manual show?
asked_as:
- xs895 wiring diagram
- how is the incline motor wired on the xs895
- acn acl on the xs895 controller
- where is the fuse on the xs895
keywords:
- circuit diagram
- schematic
- appliance inlet
- fuse
- controller
- acn
- acl
- 11 pin computer cable
- incline motor
- 3 pin vr cable
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - xs895-2018
  - xs895-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
- crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
see_also:
- spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
- spirit-xs895-specs-unit-block-diagram-display-board-driver-board-amplifier-and-fuse
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 8. Circuit Diagram, PDF p. 39 (printed 38), text.md line 608, a flattened
    line drawing read from a 170 dpi render (OCR supplement 1428-1477 is rotated)
  extracted_at: '2026-09-11'
---

**Mains.** A **POWER CORD** into an **APPLIANCE INLET** drawn with its **FUSE** drawer and rocker
switch. Three leads leave the inlet: **GROUNDING** to earth, and two **Red wires** to the
**CONTROLLER**'s **ACN** and **ACL** terminals. The stepper takes mains straight into its lower
board - there is no adapter anywhere on the sheet.

**Console.** Three leads leave the **CONSOLE**: the **11 PIN COMPUTER CABLE** down to the
controller, and two leads to the handlebar buttons (the level and incline thumb switches), each
through an inline plug. Two **HANDPULSE SENSOR** grips hang from the console on their own leads.

**Controller outputs.**

| Terminal | Lead | To |
|---|---|---|
| (bottom) | **8 pin Motor W/cable** | **GEAR MOTOR**, which also carries the **RPM Sensor** on a second lead |
| **UP** | **Red wire** | INCLINE MOTOR |
| **COM** | **White wire** | INCLINE MOTOR |
| **DOWN** | **Black wire** | INCLINE MOTOR |
| **INC VR** | **3 Pin VR Cable** | the incline position sensor on the motor |

The **INCLINE MOTOR** has its own **GROUNDING** lead - the green wire of the electrical
configuration page
(`spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor`).

**No voltage, fuse rating or part number is printed** on the drawing. The 11-pin cable's pins are
on `spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins`; the 8-pin
motor plug is numbered but not named on its own page.

The CS800 and CRS800S have no lower controller and no incline; their cables go straight from the
console to the motor (`cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse`).

