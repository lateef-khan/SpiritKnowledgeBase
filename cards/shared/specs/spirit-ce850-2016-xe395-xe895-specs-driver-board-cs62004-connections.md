---
id: spirit-ce850-2016-xe395-xe895-specs-driver-board-cs62004-connections
title: 'The CS62004-00L driver board: AC in through the switch and fuse, transformer
  sockets, UP red, COM white and DOWN black spades to the actuator, and sockets for
  the tension motor, position sensor, 14-pin system cable and RPM'
kind: spec
question: What connects where on the CS62004 driver board of a Spirit CE850-2016,
  XE395-2016 or XE895 elliptical?
asked_as:
- cs62004 driver board connections
- ce850 lower board wiring
- which terminal is up on the xe395 controller
- xe895 driver board j7 j8 j12
keywords:
- driver board
- controller
- cs62004-00l
- corestar
- up com down
- transformer
- tension motor j7
- system cable j8
- rpm j11
- lift j12
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
- ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections
- xe395ent-2021-specs-driver-board-cs51005-connections
see_also:
- spirit-elliptical-specs-console-to-driver-board-14-pin-definition-with-incline-pins
- spirit-elliptical-specs-tension-motor-connector-5-pin-definition
- spirit-elliptical-specs-motor-controller-fuse-5-a
- spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds
- xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v
- spirit-ce850-2016-xe395-xe895-specs-circuit-diagram
source:
  ref: spirit-elliptical-ce850-2016-service-manual
  locator: 'CE850-2016: Driver Board PCB Component Locations, PDF p. 30 (printed 30),
    text.md lines 500-506, and Driver Board function, PDF p. 34, lines 544-578. XE895-2016:
    PDF pp. 31 and 35, lines 501-507 and 545-579. XE395-2016: PDF pp. 31 and 35, lines
    497-503 and 543-573. Photographs read from 300 dpi renders'
  extracted_at: '2026-09-11'
---

Three books photograph the same **CoreStar CS62004-00L REV 1.2** board in its metal tray. The
function page names every socket:

| Socket | Lead | Notes |
|---|---|---|
| **J10** | POWER SWITCH - **AC NEUTRAL** | spade |
| **J4** | FUSE - **AC HOT** | spade, from the inlet fuse holder |
| **J9** | TRANSFORMER IN | |
| **J13** | TRANSFORMER OUT | |
| **J1** | **UP - red wire** | spade to the actuator |
| **J2** | **COM - white wire** | spade |
| **J3** | **DOWN - black wire** | spade |
| **J7** | **TENSION MOTOR** (MOTOR 1) | 5-pin |
| **J6** | MOTOR 2 | **not used** |
| **J12** | INCLINE MOTOR VR (silkscreen **LIFT**) | 3-pin position sensor |
| **J8** | **SYSTEM CABLE** | 14-pin to the console |
| **J11** | **RPM** | 4-pin, two sensors |

Three LEDs - **PWR, UP, DN** - sit near the actuator terminals; the error chapters read them
(`spirit-ce850-2016-errors-controller-led-debugging-stride-motor-leds`,
`xe395-2016-errors-controller-led-debugging-power-up-down-110-120-v`).

On the CE850 and XE895 the UP / COM / DOWN spades and J12 serve the **stride** motor; on the XE395
the **incline** motor - same board, same sockets, different actuator. The circuit diagram draws
this board as *Controller* (`spirit-ce850-2016-xe395-xe895-specs-circuit-diagram`). The CE850-2020
book draws a CS62004 but photographs a **CS51007** with a different socket set
(`ce850-2020-specs-driver-board-cs62004-cs51008-or-cs51007-connections`); the XE395ENT uses a
CS51005 (`xe395ent-2021-specs-driver-board-cs51005-connections`).

