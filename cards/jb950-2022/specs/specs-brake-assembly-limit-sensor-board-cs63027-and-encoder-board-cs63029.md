---
id: jb950-2022-specs-brake-assembly-limit-sensor-board-cs63027-and-encoder-board-cs63029
title: 'Inside the level-control brake: a DC motor, a CS63027 limit sensor board with
  upper-limit and home sensors and a position flag, and a CS63029 optical encoder
  board'
kind: spec
question: What are the parts and boards inside the level-control brake assembly of
  a Spirit jb950-2022 indoor cycle, and how are they connected?
asked_as:
- what is the limit sensor board on the jb950
- jb950 encoder board
- how is the jb950 brake motor wired
- what is the brake position flag on the jb950
keywords:
- brake assembly
- dc motor
- limit sensor board
- cs63027
- encoder board
- cs63029
- upper limit sensor
- home position sensor
- brake position flag
- encoder wheel
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: specs
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- spirit-xb-specs-gear-motor-connector-5-pin-definition
see_also:
- jb950-2022-specs-lower-control-board-cs52003-connectors-and-pin-definitions
- jb950-2022-specs-circuit-diagram-9-pin-console-cable-and-6-pin-key-cable
- jb950-2022-errors-motor-error-brake-does-not-reach-home
- jb950-2022-errors-encoder-error-pedal-then-check-wires
- jb950-2022-console-limit-sensor-test
source:
  ref: spirit-bike-jb950-2022-service-manual
  locator: 4.4 Brake Assembly, PDF p. 33 (printed 33), text.md lines 489-502; 4.5
    Limit Sensor board, PDF p. 34, lines 504-529; 4.6 DC Motor Encoder Board, PDF
    p. 35, lines 531-556; all three photographs read from 300 dpi renders (board silkscreens
    CS63027 Rev 2.0 and CS63029); the circuit diagram on PDF p. 38 names the sockets
  extracted_at: '2026-09-11'
---

**4.4 Brake Assembly** photographs three parts on the magnet carrier: the **DC motor**, the
**Limit Sensor board** and the **DC Motor Encoder Board**.

**4.5 Limit Sensor board** (silkscreen **CS63027 Rev 2.0**) - three leads and three sensors:

| Lead / part | What it is | Socket, per the circuit diagram |
|---|---|---|
| **Brake Cable** | the eight-wire cable up to the lower board's J4 | **J2** |
| **DC Motor Power Cable** | the two motor wires, **M+** and **M-** | **J1** |
| **DC Motor Encoder Board Cable** | to the encoder board's OUT | **J3** |
| **Upper Limit Sensor** | an opto-interrupter at the top of travel | **U1** on the silkscreen |
| **Home Position Sensor** | an opto-interrupter at the home end - the HOME pin | **U2** |
| **Brake Position Flag** | the metal tab on the carrier that passes through the two sensors | - |

**4.6 DC Motor Encoder Board** (silkscreen **CS63029**) - the **DC Encoder Board Cable**, an
**Encoder Optical Sensor**, the **Encoder Wheel** on the motor's rear shaft and the **Encoder
Sensor** that reads it.

**How it fails, in the book's own words:** MOTOR ERROR is "ENCODER is read, but motor does not
reach home position" - the flag "may have crashed into, or traveled past the home position
sensor"; ENCODER ERROR is the encoder not being read, from low capacitor voltage, a bad wire or
a disconnected motor. Those cards are in the errors section; the maintenance-menu *Limit Sensor
Test* that exercises U1 and U2 is in the console section.

**Not a gear motor of the XBR/XBU kind.** Those bikes' motor has a five-way plug with a
potentiometer for position; this one reports position through an optical encoder and two limit
sensors, and its motor plug is a bare two-wire M+/M-.

