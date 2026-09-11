---
id: spirit-xt-ent-specs-driver-board-connectors
title: 'Driver board connections on the touch-screen machines: a 5-pin system cable
  on JK11, ACL and ACN, and a single power LED'
kind: spec
question: Where are the connectors and LEDs on the driver board of a Spirit XT485ENT
  or XT685ENT treadmill, and what plugs into each?
asked_as:
- which plug is the console cable on the xt485 ent controller
- jk11 5 pin
- xt685ent lower board connections
- is there a speed sensor plug on the ent controller
keywords:
- driver board
- lower controller
- motor driver controller
- connector
- jk11
- acl
- acn
- inc
- power led
- speed sensor reserve
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt485ent-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
see_also:
- spirit-xt-ent-specs-console-cable-5-pin-pinout
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
- spirit-xt-ent-errors-controller-power-led-only
- xt485ent-2023-assembly-drive-motor-replacement
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: 'XT485ENT-2023: PDF p. 25 (printed 25), section 6.3 Driver Board Wires
    Connections, text.md line 359 (render); p. 27, 6.5 LED Indicator Locations, lines
    371-384; p. 28, 6.6; p. 29, 6.7 Driver Board function, line 399 (OCR). XT685ENT-2023:
    p. 14, 6.3, line 240 (render); p. 16, 6.5 (OCR); p. 17, 6.6-6.7, lines 254-264'
  extracted_at: '2026-09-11'
---

Both books draw the same board as "MOTOR DRIVER CONTROLLER":

| Terminal | Goes to |
|---|---|
| M- (white or black wire) and M+ (red wire) | DC MOTOR |
| INC | INCLINE VR SENSOR |
| SENSOR | SPEED SENSOR |
| **JK11** | **SYSTEM CABLE (5 PIN)** |
| ACN (white) and ACL (black) | ON/OFF SWITCH, from the BREAKER and AC POWER |
| COM (white), UP (red), DOWN (black) | INCLINE MOTOR |

The transistors are marked D1a / G2a / G1a and one capacitor is drawn. The function map (6.7) repeats the
names and adds **"SPEED SENSOR (RESERVE)"** - and the circuit diagram draws no speed sensor at all, so
on these machines the RPM input is a spare.

**LEDs (6.5 / 6.6)** - only a **POWER LED** is ringed, with the note "IT'S MUST BE CONNECT CONSLOE AND SET
SAFETY KEY TO CHECK" (as printed): the LED lights only with the console connected and the safety key
fitted. The debugging table has one row.

The non-ENT XT boards carry a 6-pin console socket (JK90 or JK1) and a speed-sensor plug that is used.
