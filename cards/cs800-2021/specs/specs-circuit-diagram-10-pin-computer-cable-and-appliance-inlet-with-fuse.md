---
id: cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
title: Circuit diagram with a 10-pin computer cable to 5, 2 and 3-pin plugs, an appliance
  inlet with switch and fuse feeding an internal AC adapter, and 3-pin and 4-pin hand-pulse
  cables
kind: spec
question: What does the circuit diagram of the Spirit cs800-2021 stepper service manual
  show?
asked_as:
- cs800 2020 wiring diagram
- does the cs800 have a fuse
- where is the ac adapter on the cs800
- hand pulse cables on the cs800 console
keywords:
- circuit diagram
- schematic
- 10 pin computer cable
- appliance inlet
- fuse
- ac adapter
- gear motor
- speed sensor
- hp-right
- hp-left
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2021
  applies_to:
  - cs800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
- cs800-2016-specs-circuit-diagram-xs200-ss003-with-an-external-ac-adapter
see_also:
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
- spirit-climber-specs-fuse-rating
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: 8. Circuit diagram (CS800(2020)), PDF p. 35 (printed 34), text.md line
    561, a flattened line drawing read from a 170 dpi render (OCR supplement 1358-1400)
  extracted_at: '2026-09-11'
---

**Console.** A **MAIN CONNECTOR** takes the **10 PIN COMPUTER CABLE**, which fans out into three
plugs at the machine end:

| Plug | Lead | To |
|---|---|---|
| **5Pin** | 5Pin Motor wire | **Gear Motor** |
| **2Pin** | 2Pin RPM Sensor wire | **SPEED SENSOR** |
| **3Pin** | 3Pin DC power cord, into a **DC output wire** | **AC Adapter** |

**Heart rate.** **HP-RIGHT** on a **3 PIN CABLE** and **HP-LEFT** on a **4 PIN CABLE**, each to a
pair of grip plates - the two sides are not wired alike.

**Power.** An **Appliance inlet** with a **FUSE** drawer and a rocker switch is drawn at the top
right; its **Black** and **White** leads run through spade connectors to the **AC Adapter**, which
is inside the machine. A mains cord with a plug goes to the inlet. This is the "POWER SWITCH ->
AC Adapter" chain of the block diagram (`spirit-crs800s-cs800-2021-specs-unit-block-diagram`).
**No fuse rating, voltage or adapter rating is printed** on the drawing; the troubleshooting
matrix's "Check AC power is 220-240V or 110-120V" is the only mains figure, and the owner's-manual
fuse card for the family does not cover this machine (`spirit-climber-specs-fuse-rating`).

**Ten pins here, fourteen on the pin-definition page.** The drawing and the display-board page say
10; the console-socket list numbers 14 with four spares
(`cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used`).

The recumbent CRS800S draws an external adapter and a fourth, photo-coupler branch instead
(`crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board`).

