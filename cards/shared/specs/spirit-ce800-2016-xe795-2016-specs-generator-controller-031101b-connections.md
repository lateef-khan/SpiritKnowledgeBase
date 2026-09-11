---
id: spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
title: 'The 031101B generator controller on two ellipticals: generator power in, brake
  resistance voltage out, system cable, and a spare fourth socket'
kind: spec
question: What connects to the 031101B generator controller on a Spirit CE800-2016
  or XE795-2016 elliptical?
asked_as:
- what plugs into the 031101b board
- ce800 2016 generator controller connections
- xe795 2016 lower board sockets
- where does the brake wire go on the xe795 controller
keywords:
- generator controller
- driver board
- 031101b
- cn1
- cn2
- cn3
- generator power
- generator brake resistance voltage
- system cable
- system control
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce800-2016
  - xe795-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ce800-2021-specs-generator-controller-connections
- xe795-2023-specs-generator-controller-cs52005-23-connections
see_also:
- ce800-2016-specs-circuit-diagram-xe890b-ae10m
- xe795-2016-specs-circuit-diagram-xe815-se024
- xe795-2016-specs-console-to-driver-board-6-pin-definition
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
source:
  ref: spirit-elliptical-ce800-2016-service-manual
  locator: 'CE800-2016: Driver Board PCB Component Locations, Driver Board Wire Connections
    and Driver Board function, PDF pp. 24-26 (printed 24-26), text.md lines 417-474
    (OCR supplement lines 1164-1234). XE795-2016: Driver Board Wire Connections, PCB
    Component Locations and function, PDF pp. 31-33, lines 444-471 (OCR supplement
    lines 1355-1391); pin list on PDF p. 40, lines 570-594'
  extracted_at: '2026-09-11'
---

Both books use the board marked **#031101B** - the CE800-2016 shows the silkscreen in its
photographs and both print it on their circuit diagrams. Sockets:

| Socket | CE800-2016 name | XE795-2016 name | What it is |
|---|---|---|---|
| **CN1** | GENERATOR POWER (function page: GENERATOR POWER 1) | GENERATOR | the three-wire stator lead in |
| **CN2** | GENERATOR BRAKE RESISTANCE VOLTAGE (function page: GENERATOR RESISTANCE VOLTAGE) | GENERATOR BRAKE | the two-wire brake coil out |
| **CN3** | SYSTEM CABLE (function page: SYSTEM CONTROL) | SYSTEM CABLE | the console cable |
| **CN4** | GENERATOR POWER 2 on the function page; nothing wired on the schematic | drawn on the schematic, nothing wired | spare |

The XE795-2016 function photograph captions the same plugs **GENERATOR BRAKE OUTPUT**, **GENERATOR
INPUT** and **SYSTEM WIRE**, and its pin-define page lists the six pins of CN3
(`xe795-2016-specs-console-to-driver-board-6-pin-definition`). The CE800-2016 prints no pin list.

**The CE800-2016 captions CN4 "GENERATOR POWER 2"** and CN1 "GENERATOR POWER 1" on its function
page, but its own schematic runs the generator lead to CN1 only and leaves CN4 empty. Take the
second caption as a labelling slip, as the XU878 bike book has at the same position.

The 2016 XBR95 bike and the 2012 CU800 share this board
(`spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections`). The 2020-version
CE800 uses a controller with an RPM socket of its own
(`ce800-2021-specs-generator-controller-connections`); the XE795-2023 a CS52005-23
(`xe795-2023-specs-generator-controller-cs52005-23-connections`).

