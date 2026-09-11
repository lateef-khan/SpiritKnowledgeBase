---
id: trx1400-2023-specs-driver-board-b307d-wire-connections
title: 'What plugs into the driver board: AC power on ACN and ACL, incline power com
  white, up red and down black, motor black wire to M- and red to M+, a 2-pin speed
  sensor socket, the incline VR socket and the main control socket silkscreened SW,
  VDD, TXD, RXD, GND'
kind: spec
question: Which wire goes to which terminal on the driver board (lower controller)
  of an Xterra trx1400-2023 treadmill?
asked_as:
- trx1400 lower controller connections
- trx1400 incline motor wires on the controller
- trx1400 driver board model
- which pin is txd on the trx1400 controller socket
keywords:
- driver board
- lower controller
- wire connections
- acn
- acl
- incline power
- m plus
- m minus
- incline vr
- b307d
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-driver-board-b426d-wire-connections
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
see_also:
- trx1400-2023-specs-driver-board-b307d-components-with-a-fuse-and-an-incline-relay
- trx1400-2023-specs-driver-board-led-locations-power-led-and-info-led
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
- trx1400-2023-specs-incline-position-sensor-pin-1-is-5-volts
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- spirit-ct800-specs-driver-board-connector-locations
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '6.3 Driver Board Wire Connections', PDF p. 29
    (printed 27), lines 410-445; '6.4 Driver Board PCB Component Locations' PDF p.
    30, lines 445-451, uncaptioned. Silkscreen read from the 110 dpi render
  extracted_at: '2026-09-11'
---

The page is a silkscreen drawing of a **ShangHai EWay MODEL: B307D** board with tick boxes 110V / 220V. Callouts:

| Callout | Terminal |
|---|---|
| AC POWER INPUT (110V or 220v) | two terminals on the left edge, **ACN** (upper) and **ACL** (lower) |
| "This area are Incline power output socket": Com: white incline power wires; UP: red incline power wires; DOWN: black incline power wires | three terminal pairs down the left edge, **COM**, **UP**, **DOWN** |
| M- black wire of motor | terminal on the right edge, silkscreened **BLACK** |
| M+ red wire of motor | terminal below it, silkscreened **RED** |
| Speed sensor socket connected (2-pins) | small socket, right edge, lower (silkscreen SPEED) |
| Incline VR socket connected | 3-pin socket, bottom right (silkscreen INC VR) |
| MAIN control wires socket connected | 5-pin socket, bottom right, silkscreened **SW VDD TXD RXD GND** |

The silkscreen order SW, VDD, TXD, RXD, GND is the circuit diagram's pin define 1 to 5. Section 6.4 is the board
photographed without captions. The component labels (bridge, IGBT, fuse, relays, transformer) are on the
component card; the two LEDs on the LED card.
