---
id: cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
title: 'Fourteen-pin console-to-driver-board connector with ten pins used: MTR-, MTR+,
  5V, MTR_AD, GND, RPM, GND, N/A, GND, 12V, then four spares'
kind: spec
question: What are the fourteen pins of the console to driver board connector on a
  Spirit cs800-2021 stepper?
asked_as:
- cs800 2020 console connector pinout
- which pin is 12v on the cs800 system cable
- 14 pin cable on the spirit stepper
- is the cs800 system cable 10 or 14 pins
keywords:
- pinout
- pin define
- console to driver board
- 14 pin
- mtr-
- mtr+
- mtr_ad
- rpm
- 12v
- n/a
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
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
- cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
see_also:
- spirit-crs800s-cs800-2021-specs-display-board-cs24005-and-interface-board-connections
- cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
source:
  ref: spirit-stepper-cs800-2021-service-manual
  locator: 7-5 Test configuration and the console to driver board connector pin define
    function, PDF p. 31 (printed 30), text.md lines 481-502, native list beside a
    photograph of the CS24005-12ED board with the socket numbered 1 to 14 (OCR supplement
    1314-1348)
  extracted_at: '2026-09-11'
---

**Fourteen positions, ten carrying anything.** The recumbent CRS800S prints eleven pins with two
RPM lines instead (`crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines`).

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **MTR-** | 8 | N/A |
| 2 | **MTR+** | 9 | GND |
| 3 | 5V | 10 | **12V** |
| 4 | **MTR_AD** | 11 | N/A |
| 5 | GND | 12 | N/A |
| 6 | **RPM** | 13 | N/A |
| 7 | GND | 14 | N/A |

The socket is the white fourteen-way on the bottom edge of the **CS24005-12ED** display board,
numbered **1 to 14** left to right. The heading says "driver board"; the CS800 has none - this is
where the computer cable's branches meet the console
(`cs800-2021-specs-circuit-diagram-10-pin-computer-cable-and-appliance-inlet-with-fuse`).

**The book contradicts itself on the count.** Its display-board page labels this socket *SYSTEM
CABLE (10 PINS)* and its circuit diagram draws a *10 PIN COMPUTER CABLE*; this page numbers
fourteen. Ten lines are used either way (pins 1-7, 9 and 10, plus pin 8's N/A makes ten positions
in the first block). Count the plug before ordering a cable.

Pins 1-5 are the tension motor's five lines
(`spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1`); RPM on pin 6 is
the speed sensor; 12V on pin 10 is the adapter supply. The Spirit XB 2016 bikes print a different
fourteen-way list under the same heading
(`spirit-xb-2016-specs-console-to-driver-board-14-pin-definition`). **No wire colours are printed.**

