---
id: xe795-2023-specs-generator-controller-cs52005-23-connections
title: 'Four sockets on the CS52005-23 generator controller: generator power, system
  cable, RPM sensor and generator brake resistance'
kind: spec
question: What connects to the driver board on a Spirit xe795-2023 elliptical, and
  what is the board marked?
asked_as:
- xe795 2023 driver board connections
- cs52005 board elliptical
- where does the speed sensor go on the xe795 controller
- xe795 lower board j1 j2 j3 j4
keywords:
- driver board
- generator controller
- cs52005-23
- j1 generator
- j2 system cable
- j3 rpm sensor
- j4 generator brake
- main connect
- generator resistance voltage
facets:
  brand:
  - spirit
  product_line: elliptical
  model: xe795-2023
  applies_to:
  - xe795-2023
  section: specs
  code: '*'
  model_number:
  - '795023'
authority: 3
not_to_be_confused_with:
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xbr95-2023-specs-generator-controller-cs52005-33-connections
see_also:
- xe795-2023-specs-circuit-diagram-6-pin-computer-cable
- xe795-2023-specs-unit-block-diagram
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
- xe795-2023-specs-display-board-cs11039-and-interface-board-connections
source:
  ref: spirit-elliptical-xe795-2023-service-manual
  locator: 6.4 Driver Board PCB Component Locations, PDF p. 12 (printed 12), text.md
    lines 215-221, and 6.5 Driver Board function, PDF p. 13, lines 221-227; photographs
    read from 300 dpi renders (OCR supplement lines 863-908)
  extracted_at: '2026-09-11'
---

The board is silkscreened **CS52005-23** (CoreStar). Four sockets, named on the location page and
again by function captions:

| Socket | Location page | Function page | Circuit diagram |
|---|---|---|---|
| **J1** | GENERATOR | GENERATOR POWER | white, black, red wire from the generator |
| **J2** | SYSTEM CABLE | SYSTEM CABLE (MAIN CONNECT) | 6 PINS COMPUTER CABLE |
| **J3** | RPM SENSOR | RPM SENSOR | speed sensor |
| **J4** | GENERATOR BRAKE | GENERATOR BRAKE RESISTANCE | red wire to the brake coil |

The function page's third photograph is the flywheel with **GENERATOR POWER** and **GENERATOR
RESISTANCE VOLTAGE** leads and a **CHI HUA K500022** label
(`spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads`).

**The RPM sensor lands here**, not on the console as on the 2016 XE795's 031101B board
(`spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections`). The 2023 XBR95
bike uses the sibling **CS52005-33** with the same four sockets
(`xbr95-2023-specs-generator-controller-cs52005-33-connections`) - a different suffix, so quote
the -23 for the elliptical. No pin numbers are printed for any of the four.

