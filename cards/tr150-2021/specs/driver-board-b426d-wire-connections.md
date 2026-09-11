---
id: tr150-2021-specs-driver-board-b426d-wire-connections
title: 'What plugs into the lower controller: AC power input on a board marked 110
  V or 220 V, motor black wire to M- and red wire to M+, a 2-pin speed sensor socket
  and the 5-pin main control socket'
kind: spec
question: Which wire goes to which terminal on the driver board (lower controller)
  of an Xterra tr150-2021 treadmill?
asked_as:
- tr150 lower controller connections
- which motor wire goes to m minus on the tr150
- tr150 controller board model
- where does the speed sensor plug in on the tr150 controller
keywords:
- driver board
- lower controller
- motor control board
- wire connections
- ac power input
- m plus
- m minus
- speed sensor
- main control wires
- b426d
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with:
- tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
- trx1400-2023-specs-driver-board-b307d-wire-connections
see_also:
- tr150-2021-specs-driver-board-b426d-components-bridge-igbt-relay-and-transformer
- tr150-2021-specs-mcb-terminal-map-from-the-annotated-photograph
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- spirit-ct800-specs-driver-board-connector-locations
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM (GT65-NT014) '6.3 Driver Board Wire Connections', PDF p. 26 (printed
    27), lines 319-351; '6.4 Driver Board PCB Component Locations' PDF p. 27 (printed
    28), lines 351-357, an uncaptioned photograph. Board markings read from the 110
    dpi render
  extracted_at: '2026-09-11'
---

The board photographed is a **ShangHai EWay MODEL: B426D** on a finned aluminium plate, with an "EW" logo, a RoHS
sticker, an oval **110V** label and tick boxes for **110V** and **220V** by the AC terminals. Five callouts:

| Callout | Terminal |
|---|---|
| AC POWER INPUT, AC 110V / AC 220V | two spade terminals on the left edge, silkscreened **ACL** (upper) and **ACN** (lower) |
| M- connected with black wire of motor | spade terminal, right edge, upper, silkscreened **BLACK** |
| M+ connected with red wire of motor | spade terminal, right edge, lower, silkscreened **RED** |
| Speed sensor socket connected with 2-pin of speed sensor wires | small white socket, bottom right |
| MAIN control wires socket connected with 5-pin of control wires | black 5-pin header, bottom centre |

There is no incline terminal on this board - the GT65 has no incline motor. The photograph also shows the 1000 µF
electrolytic capacitor with a QR sticker and the EE22-1.2mH transformer that the component-function card names.

**Black to M-.** The book's electrical-configuration chapter says "The White wire is inserted into M-"; this page and
the circuit diagram both say black. Follow the board: BLACK beside M-, RED beside M+.

Section 6.4 is the same board photographed without callouts. The annotated technician's photograph of this board
agrees with every label here and adds the two on/off-switch leads (white to AC N, black to AC L).
