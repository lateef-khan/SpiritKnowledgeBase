---
id: spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
title: 'Driver board sockets on the two-LED controller: incline power, incline VR,
  6-pin main control and speed sensor, plus the function map'
kind: spec
question: Where are the connectors and LEDs on the driver board of a Spirit XT185
  or XT285 treadmill, 2015 or 2023, and what plugs into each?
asked_as:
- which socket is the incline motor on the xt185 controller
- jk90 main socket
- where does the speed sensor plug in on the xt285
- where are the leds on the xt185 lower board
keywords:
- driver board
- lower controller
- controller
- socket
- jk80
- jk60
- jk90
- jk50
- led
- transformer
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
- spirit-xt-ent-specs-driver-board-connectors
- f65-2016-driver-board-connectors
see_also:
- spirit-xt-specs-console-cable-6-pin-pinout
- spirit-xt-2015-specs-incline-sensor-pinout-pin-1-5v
- spirit-xt-specs-incline-sensor-pinout-pin-1-ground
- spirit-xt-errors-controller-led-debugging-power-and-limit-only
- spirit-xt-2015-assembly-lower-controller-replacement
- spirit-xt-2023-assembly-controller-replacement
source:
  ref: spirit-treadmill-xt185-2015-service-manual
  locator: 'XT185-2015: PDF p. 28 (printed 27), section 6.4 Driver Board Wire Connections,
    text.md lines 392-426; p. 30, 6.6 LED Indicator Locations, lines 429-433; p. 32,
    6.8 Driver Board function, lines 472-511. XT285-2015: pp. 29-33, lines 398-517.
    XT185-2023: p. 14, 6.3, line 258; p. 15, 6.4-6.5, line 264 (render); p. 16, 6.6,
    line 275. XT285-2023: pp. 14-16, lines 259-277'
  extracted_at: '2026-09-11'
---

Four books describe the same board.

**Sockets (6.4 in 2015, 6.3 in 2023)**

| Socket | As printed |
|---|---|
| AC POWER INPUT | "(110V or 220v)" |
| M- | connected with the black wire of the motor |
| M+ | connected with the red wire of the motor |
| **JK80** | incline power output: **Com** white incline power wire, **UP** red, **DOWN** black |
| **JK60** | incline VR socket, the 3-pin VR wire |
| **JK90** | MAIN socket, the 6-pin control wire |
| **JK50** | speed sensor socket, the 2-pin speed sensor wire |

**Function map (6.8 in 2015, 6.5 in 2023)** - the same photograph with the parts named: Bridge, IGBT, L,
N, Varistor, X capacitor (Safety CAP.), Filter capacitor, FUSE, COM / UP / DOWN, INCLINE RELAY,
TRANCEFORMER (as printed), RELAY, Main IC, M-, M+, INCLINE VR, MAIN CONTROL WIRE (2023: "MAIN CONTORL"
connector), SPEED SENSOR. The 2023 render shows the transformer marked EE25-870UH and the relay a
JQX-105F-1.

**LEDs (6.6)** - only two are ringed: the **Limit current LED** and the **Power LED**, at the edge of the
board near the main-control socket. What they mean is on the LED-debugging cards.

**The 6.3 / 6.4 pages are the 2015 book's text and drawing reused**; the 2023 photographs show the same
socket layout. The XT385 / XT485 / XT685 use a different board (PA-AE00300L) with JK3 / JK1 / SPEED names
and five LEDs; the ENT machines a third board with a 5-pin JK11.
