---
id: crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
title: 'Eleven-pin console-to-driver-board connector: MTR-, MTR+, 5V, MTR_AD, GND,
  RPM1, GND, RPM2, GND, 12V, GND'
kind: spec
question: What are the eleven pins of the console to driver board connector on a Spirit
  crs800s-2021 recumbent stepper?
asked_as:
- crs800s console connector pinout
- which pin is 12v on the crs800s system cable
- rpm1 and rpm2 pins on the spirit recumbent stepper
- mtr_ad pin crs800s
keywords:
- pinout
- pin define
- console to driver board
- 11 pin
- mtr-
- mtr+
- mtr_ad
- rpm1
- rpm2
- 12v
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
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
- cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
- spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
- spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition
see_also:
- spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
- crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: '8-4 Test configuration: The console to driver board connector pin defines
    function, PDF p. 32 (printed 32), text.md lines 435-462, native list beside a
    photograph of the CS24005-23ED board with the socket numbered 11 down to 1'
  extracted_at: '2026-09-11'
---

**Eleven pins with two RPM lines.** The CS800's list is fourteen pins with one RPM
(`cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used`); the XS895's eleven pins
are a different list with incline lines
(`spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins`); the Spirit XBR55/
XBU55 2023 bikes' eleven-pin header is different again
(`spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition`).

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **MTR-** | 7 | GND |
| 2 | **MTR+** | 8 | **RPM2** |
| 3 | 5V | 9 | GND |
| 4 | **MTR_AD** | 10 | **12V** |
| 5 | GND | 11 | GND |
| 6 | **RPM1** | | |

The socket is the white eleven-way on the bottom edge of the **CS24005-23ED** display board,
numbered **11, 10, 9 ... 1** from left to right in the photograph. **The heading says "driver
board", but the CRS800S has none** - the display board is the controller, and this header is where
the 14-pin computer cable's branches meet it
(`crs800s-2021-specs-circuit-diagram-14-pin-computer-cable-and-photo-coupler-board`).

Pins 1-5 are the tension motor's five lines - the same signals as M-, M+, +5V, VR, GND at the
motor (`spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1`), with
MTR_AD the position feedback. **RPM1 and RPM2** are the two channels of the optical step sensor,
which is why the recumbent has two where the upright has one. 12V on pin 10 is the adapter's
supply arriving at the console. **No wire colours are printed.**

