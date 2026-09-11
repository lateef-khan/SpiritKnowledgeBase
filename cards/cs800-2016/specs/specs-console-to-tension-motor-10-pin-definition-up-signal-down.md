---
id: cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
title: 'Ten-pin console-to-tension-motor connector: VCC +5V, GND, UP, SIGNAL, DOWN,
  SPEED SENSOR, SPEED GND, VCC +12V, NA, GND'
kind: spec
question: What are the ten pins of the console connector to the tension motor on a
  Spirit cs800-2016 stepper?
asked_as:
- cs800 2016 console connector pinout
- 10 pin cable on the xs200 stepper
- which pin is up and down on the cs800 motor cable
- speed sensor pins on the 2016 cs800
keywords:
- pinout
- pin define
- console to tension motor
- 10 pin
- up
- down
- signal
- speed sensor
- vcc +12v
- interface board
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: specs
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
see_also:
- cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable
- cs800-2016-specs-display-board-cs22002-and-interface-board-cs11002-1-connections
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: Test configuration. The console to driver board connector pin define function,
    PDF p. 38 (printed 38), text.md lines 545-567, native list beside a photograph
    of the CS11002-1 interface board with the J6 socket numbered 10 down to 1
  extracted_at: '2026-09-11'
---

**A different list from every later stepper book** - the 2020-version CS800 and CRS800S name the
motor lines MTR-/MTR+/MTR_AD (`cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used`);
this book names them by what they do.

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **VCC +5V** | 6 | **SPEED SENSOR** |
| 2 | GND | 7 | SPEED GND |
| 3 | **UP** | 8 | **VCC +12V** |
| 4 | **SIGNAL** | 9 | NA |
| 5 | **DOWN** | 10 | GND |

**The heading and the callout disagree about what this is.** The page heading says "the console
to driver board connector"; the callout beside the list says "The console to Tension Motor
connector pin define function". The photograph settles the location: it is **J6 INTERFACE**, the
ten-way socket on the **CS11002-1 interface board** (silkscreens J7 EMS, J3 HP, J5 H-INC, J4 H-RES,
J13 also visible), numbered **10, 9 ... 1** left to right. There is no driver board on this
machine.

UP, SIGNAL and DOWN are the motor drive and position lines - the E2 test says "Press the Level Up
is +5VDC; Level DOWN is -5VDC" on the drive board output; SPEED SENSOR and SPEED GND are the RPM
sensor; VCC +12V is the adapter supply. **No pin-to-colour map is printed**, although the same
book draws the ten-way cable's colours on the E2 page
(`cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable`).

