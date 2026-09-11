---
id: spirit-xs895-specs-console-to-driver-board-11-pin-definition-with-incline-pins
title: 'Eleven-pin console-to-driver-board connector: SPEED, GND, VCC+5V, ZERO, COUNT,
  MOTOR-, MOTOR+, VIN, INC UP, INC DOWN, INC VR'
kind: spec
question: What are the eleven pins of the console to driver board connector on a Spirit
  XS895 incline stepper?
asked_as:
- xs895 console connector pinout
- 11 pin cable on the spirit incline stepper
- which pins are incline up and down on the xs895
- what is zero and count on the xs895 console board
keywords:
- pinout
- pin define
- console to driver board
- 11 pin
- inc up
- inc down
- inc vr
- zero
- count
- vin
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
- crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines
- cs800-2021-specs-console-to-driver-board-14-pin-definition-ten-used
- spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition
see_also:
- spirit-xs895-specs-display-board-aa0175-interface-board-and-amplifier-yj-8509-connections
- spirit-xs895-specs-tension-motor-8-pin-plug-unnamed-and-2-pin-speed-sensor
- spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor
source:
  ref: spirit-stepper-xs895-2021-service-manual
  locator: 7-6 Test configuration. The console to driver board connector pin define
    function, PDF p. 34 (printed 33), text.md lines 500-528, native list beside a
    photograph of the AA0175 board with the socket numbered 11 down to 1 (OCR supplement
    1386-1418)
  extracted_at: '2026-09-11'
---

**The only stepper list with incline lines**, and the one book in this family whose "driver board"
heading is literal - the XS895 has a lower controller
(`spirit-xs895-specs-circuit-diagram-appliance-inlet-controller-and-incline-motor`).

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **SPEED** | 7 | **MOTOR+** |
| 2 | GND | 8 | **VIN** |
| 3 | VCC+5V | 9 | **INC UP** |
| 4 | **ZERO** | 10 | **INC DOWN** |
| 5 | **COUNT** | 11 | **INC VR** |
| 6 | **MOTOR-** | | |

The socket is the eleven-way at the bottom right of the **AA0175** display board, numbered **11,
10 ... 1**; the same photograph names the board's other sockets AMP POWER, FAN, HR HAND, KEYS and
HR RECEIVE.

**Reading it.** SPEED, ZERO and COUNT are the gear motor's sensor lines - the motor reports its
brake position as a count from a zero mark rather than a potentiometer voltage, the same eight
signals the XRW600 rower names on its motor plug
(`spirit-xs895-specs-tension-motor-8-pin-plug-unnamed-and-2-pin-speed-sensor`). VIN is the
controller's supply to the console. **INC UP, INC DOWN and INC VR** are the console's commands to
the AC incline motor and the return from its 3-pin position sensor; the E3 STEP ERROR page tells
you to "inspect the incline wire and 11-pin cable connections" when that VR voltage is out of
range.

The CRS800S's eleven pins are a wholly different list
(`crs800s-2021-specs-console-to-driver-board-11-pin-definition-two-rpm-lines`). **No wire colours
are printed.**

