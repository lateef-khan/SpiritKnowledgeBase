---
id: f85-2019-main-control-cable-pinout
title: Main control cable pin assignments
kind: spec
question: What are the pin assignments of the main control cable between the console
  and the driver board on a Sole F85-2019 treadmill?
asked_as:
- pinout of the treadmill computer cable
- which pin is the safety key signal
- console to controller cable pins
keywords:
- main control cable
- computer cable
- pinout
- six pin
- txd
- rxt
- vcc
- safety switch line
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2019
  applies_to:
  - f85-2019
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- f85-2019-incline-position-sensor-pinout
see_also:
- f85-2019-e5-communication-error
- f85-2019-e0-safety-key-error
- f85-2019-driver-board-sockets
source:
  ref: sole-tm-f85-2019-service-manual
  locator: section 8.3 Test configuration, console to driver board connector pin define
    function, printed page 65
  extracted_at: '2026-09-04'
---

**This is the 6 pin cable between the console and the driver board, into socket JK90. It is not the 3 pin incline position sensor cable, which has its own card.**

| Pin | Function |
|---|---|
| 1 | GND |
| 2 | TXD |
| 3 | RXT |
| 4 | VCC |
| 5 | SW |
| 6 | N/A |

- **TXD and RXT** carry the speed signal and the console-to-controller traffic. A break here gives E1 or E5.
- **SW** is the safety switch line. The lower controller sends +12V up this line to close the safety switch loop. A break here gives E0.

**Source wording.** The printed table labels the last two rows "Pin 5 SW" and "Pin 5 N/A". The connector is drawn with six positions, numbered 1 to 6, so the second of those rows is pin 6. The pin number, not the function, is the misprint.
