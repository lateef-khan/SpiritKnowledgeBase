---
id: crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
title: Circuit diagram with a 14-pin computer cable that branches to a 5-pin motor
  wire, a 3-pin RPM sensor, a 2-pin DC power cord and a 4-pin photo coupler board
kind: spec
question: What does the circuit diagram of the Spirit crs800s-2021 recumbent stepper
  service manual show?
asked_as:
- crs800s wiring diagram
- how many pins is the crs800s computer cable
- where does the photo coupler board plug in on the crs800s
- hr cables on the crs800s console
keywords:
- circuit diagram
- schematic
- 14 pin computer cable
- gear motor
- rpm sensor wire
- dc power cord
- photo coupler board
- ac adapter
- hr cable
- main connector
facets:
  brand:
  - spirit
  product_line: climber
  model: crs800s-2021
  applies_to:
  - crs800s-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
- cs800-2016-specs-circuit-diagram-xs200-ss003-with-an-external-ac-adapter
see_also:
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 8-3 Circuit Diagram, PDF p. 31 (printed 31), text.md lines 429-434, a flattened
    line drawing read from a 170 dpi render (OCR supplement 864-914)
  extracted_at: '2026-09-11'
---

**Console.** A **MAIN CONNECTOR** on the console takes the **14 PIN COMPUTER CABLE**, which fans out
at the machine end into four plugs:

| Plug | Lead | To |
|---|---|---|
| **5Pin** | 5Pin Motor wire | **Gear Motor** |
| **3Pin** | 3Pin RPM Sensor wire | **SPEED SENSOR** |
| **2Pin** | 2Pin DC power cord, into a **DC output wire** | **AC adapter** |
| **4Pin** | 4Pin Photo coupler wire | **Photo coupler board** |

The photo coupler board is the optical step sensor on the cable drive pulley - the *F/R sensor* of
the block diagram and the source of the RPM1/RPM2 lines at the console
(`crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines`).

**Heart rate.** An **HR CONNECTOR** on the console takes a **4 PIN HR CABLE** that splits into two
**2Pin** plugs, each running as a **2 PIN HR CABLE** to a pair of grip plates - four plates in all.

**Power.** The **AC adapter** is drawn as an external block with a barrel plug into the DC power
cord; **no appliance inlet, switch or fuse is drawn**, unlike the CS800 (2020)
(`cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse`). No
voltage, wattage or part number appears on the drawing; the troubleshooting matrix's "Check AC
power is 110~120V" is the only mains figure in the book.

**Fourteen at the console, eleven on the board.** The cable is drawn with 14 pins; the console
socket it lands on is defined with 11. The books never reconcile the two counts.

