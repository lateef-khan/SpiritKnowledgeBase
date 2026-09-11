---
id: trx5500-2024-specs-driver-board-wire-connections-120-vac-in
title: 'What plugs into the driver board: 120 VAC in (230 VAC in), incline com white,
  up red and down black, motor black M- and red M+, incline VR, speed sensor and a
  5-pin main system line, with the bridge, FET, filter capacitor, relays and transformer
  named'
kind: spec
question: Which wire goes to which terminal on the driver board of an Xterra trx5500-2024
  treadmill, and what components are named?
asked_as:
- trx5500 controller board connections
- trx5500 incline motor wires on the controller
- trx5500 driver board components
- trx5500 main system line 5 pins
keywords:
- driver board
- lower controller
- wire connections
- 120 vac
- incline power
- m plus
- m minus
- incline vr
- speed sensor
- main system line
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx5500-2024
  applies_to:
  - trx5500-2024
  section: specs
  code: '*'
  model_number:
  - '155810'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
see_also:
- trx5500-2024-specs-driver-board-led-location-a-single-power-led
- trx5500-2024-specs-display-board-connections-with-usb-and-a-bluetooth-wifi-board
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: TRX5500 SM (GT90D-NT041) '6-2 Driver Board Wire Connections', PDF p. 27
    (printed 26), lines 413-441; read from the 110 dpi render
  extracted_at: '2026-09-11'
---

**This is the one GT90 driver-board page that prints the 120 V figure first.** The TRX2500/3500/4500 pages label
the same terminals "230VAC IN".

One photograph, fifteen callouts:

| Callout | Where on the board |
|---|---|
| Bridge Rectification | black module, top left, on the heat-sink plate |
| FET | black module, top right, on the plate |
| 120 VAC IN (230 VAC IN) Socket | two terminals on the left edge, top (silkscreen ACN / ACL, with an oval 110V label) |
| Filter capacitor | the large radial electrolytic, centre |
| INCLINE COM WHITE | terminal, left edge |
| INCLINE UP RED | terminal, left edge, below COM |
| INCLINE DOWN BLACK | terminal, left edge, bottom |
| Speed Relay | SONGLE relay beside the incline terminals |
| Incline Relay | second relay below it |
| Transformer | yellow part, centre-right |
| Motor (Black) M- | terminal, right edge, upper |
| Motor (Red) M+ | terminal, right edge, below it |
| Incline VR | white 3-pin socket, right edge |
| Speed Sensor | white 2-pin socket, bottom right |
| Main System Line 5 Pins | the 5-pin header, bottom right |

The board's model number is hidden under the "Filter capacitor" callout; an "EW" logo and a 110V label are visible.
Two things differ from the TRX2500/3500/4500 labelling besides the voltage: the UP and DOWN incline terminals are
listed in the other order (COM, UP, DOWN here; COM, DOWN, UP there), and there is no TORQUE trimmer label. The
single LED is on its own card.
