---
id: spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
title: 'Driver board connections on the PA-AE00300L controller: 6-pin system cable,
  incline VR on JK3, two AC fans and five LEDs'
kind: spec
question: Where are the connectors and LEDs on the driver board of a Spirit XT385,
  XT485 or XT685 treadmill, and what plugs into each?
asked_as:
- which plug is the incline vr on the xt385 controller
- where do the fans plug in on the xt485 lower board
- xt685 controller connections
- which leds are on the xt385 controller
keywords:
- driver board
- lower controller
- motor driver controller
- connector
- jk3
- jk1
- fan121
- fan120
- led
- system cable
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt685-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
- spirit-xt-ent-specs-driver-board-connectors
- ct800-2016-specs-driver-board-connectors-and-leds
see_also:
- spirit-xt-specs-console-cable-6-pin-pinout
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
- spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps
- spirit-xt-2023-errors-controller-led-debugging-five-leds
- spirit-xt-2015-assembly-lower-controller-replacement
- spirit-xt-2023-assembly-controller-replacement
source:
  ref: spirit-treadmill-xt385-2015-service-manual
  locator: 'XT385-2015: PDF p. 28 (printed 27), section 6.4 Driver Board Wire Connections,
    text.md line 409 (render); p. 29, 6.5, OCR supplement for the board markings;
    p. 30, 6.6 LED Indicator Locations, line 421; p. 32, 6.8 Driver Board function,
    line 472 (OCR). XT485-2015: pp. 28-32, lines 408-471. XT385-2023: p. 16, 6.5,
    line 234 (render); p. 17, 6.6-6.7, lines 237-242 (OCR); p. 18, 6.8, line 245 (render).
    XT485-2023: pp. 16-18. XT685-2023: p. 15, 6.5, line 253 (OCR); p. 16, 6.6-6.7;
    p. 17, 6.8, line 270'
  extracted_at: '2026-09-11'
---

Five books draw the same board, silkscreened **PA-AE00300L** (sticker BJ04300L010360; the 2015 books'
photo also carries A512-160105014/800).

**Wiring drawing (6.4 in 2015, 6.5 in 2023)** - the board is drawn as "MOTOR DRIVER CONTROLLER" with:

| Terminal | Goes to |
|---|---|
| M- (white or black wire) and M+ (red wire) | DC MOTOR |
| JK3 | INCLINE VR SENSOR |
| SPEED | RPM SENSOR |
| JK1 | SYSTEM CABLE (6 PIN) |
| L (black) and N (white) | POWER SWITCH, from the BREAKER and AC POWER |
| FAN121 and FAN120 | AC FAN (two) |
| DOWN (black), COM (white), UP (red) | INCLINE MOTOR |

Two large capacitors and the transistors D1 / Q4 / Q5 are drawn on the board.

**Function map (6.8 in 2015, 6.7 in 2023)**: M- WHITE / BLACK WIRE, M+ RED WIRE, INPUT POWER (2023: AC in
L / N), VR sensor of incline, CONNECT TO CONSOLE (2023: Display board), SENSOR (2023: Speed Sensor), and
in 2023 the AC FAN pair and the incline motor's VR / DOWN / COM / UP.

**LEDs (6.6 in 2015, 6.8 in 2023)** - five: **LIMIT** (limit current), **INC_UP**, **INC_DW**, **POWER**
and **SPEED** (speed sensor). What each means is on the LED-debugging cards.

The XT185 / XT285 board is a different one (JK80 / JK60 / JK90 / JK50, two LEDs); the ENT board has a
5-pin JK11 and only a power LED.
