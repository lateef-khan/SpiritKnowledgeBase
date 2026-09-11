---
id: xterra-trx-specs-driver-board-gt90-components-230-vac-in-to-incline-vr
title: 'The driver board labelled for 230 VAC in: bridge rectification, FET, filter
  capacitor, motor red wire M+ and black wire M-, incline com white, down black and
  up red, incline and speed relays, transformer, torque trimmer, speed sensor, incline
  VR and the main system line'
kind: spec
question: What are the labelled terminals and components on the driver board of an
  Xterra TRX treadmill in the TRX2500 and TRX3500/TRX4500 service manuals?
asked_as:
- trx3500 controller board connections
- trx2500 driver board components
- trx4500 incline motor wires on the controller
- what is the torque pot on the treadmill board
keywords:
- driver board
- lower controller
- components
- wire connections
- incline power
- m plus
- m minus
- torque
- speed relay
- b017d
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- trx5500-2024-specs-driver-board-wire-connections-120-vac-in
- trx1400-2023-specs-driver-board-b307d-wire-connections
see_also:
- trx2500-2024-specs-driver-board-led-locations-led1-communication-led2-power-led3-speed
- xterra-trx-specs-driver-board-led-locations-power-led3-and-info-led-on-the-b017d
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
- xterra-trx-specs-electrical-configuration-printed-for-230-vac-with-a-220-volt-incline-motor
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
- spirit-ct800-specs-driver-board-connector-locations
source:
  ref: xterra-treadmill-trx3500-trx4500-2024-service-manual
  locator: TRX3500/TRX4500 SM '6.7 Driver Board function', PDF p. 35 (printed 34),
    lines 525-559, OCR supplement lines 1712-1753; '6.3 Driver Board Wire Connections'
    PDF p. 31 (printed 30), lines 480-486, an uncaptioned photograph; '6.4' PDF p.
    32, uncaptioned. TRX2500 SM '6.3 Driver Board Wire Connections' PDF p. 26 (printed
    25), lines 412-418, OCR supplement lines 1683-1719, and '6.7 Driver Board function'
    PDF p. 30 (printed 29), lines 479-513, OCR supplement lines 1734-1760, both with
    the same labels. Board markings read from the 110 dpi renders
  extracted_at: '2026-09-11'
---

**These labels read "230VAC IN" although the machines are 120 V** - like the electrical-configuration chapter, the
page was made for the export build. The TRX5500 book prints the same board with "120 VAC IN (230 VAC IN)" on its own
card.

All three machines get the same photograph labels; the TRX2500 book prints them on both its 6.3 and 6.7 pages, the
TRX3500/4500 book only on 6.7 (its 6.3 is the same board with no labels at all):

| Label | Where on the board |
|---|---|
| 230VAC IN | two terminals on the left edge, top (silkscreen ACN / ACL) |
| Bridge Rectification | black module, top left, on the heat-sink plate |
| FET | black module, top right, on the plate |
| Filter capacitor | the large radial electrolytic, centre |
| MOTOR (RED WIRE) M+ | terminal, right edge, upper |
| MOTOR (BLACK WIRE) M- | terminal, right edge, below it |
| INCLINE COM WHITE | terminal, left edge |
| INCLINE DOWN BLACK | terminal, left edge, below COM |
| INCLINE UP RED | terminal, left edge, bottom |
| Incline Relay | SONGLE relay by the incline terminals |
| Speed Relay | second relay below it |
| Transformer | yellow part, centre (PEE25-030 in the TRX2500 photograph, PEE25-020C in the TRX3500/4500 one) |
| TORQUE | a blue trimmer potentiometer, right of centre |
| SPEEDD SENSOR (so spelled) | white 2-pin socket, bottom right |
| INCLINE VR | white 3-pin socket, right edge |
| Main system line | the 5-pin header, bottom right |

**Board identity.** The TRX3500/4500 photographs show a board silkscreened **MODEL: B017D** (ShangHai Electronics
Way Co.,LTD) with a 110V sticker and an 832A-1A-C 12V DC relay. The TRX2500 photographs are cropped so that no model
number is visible; the board carries a SONGLE SLA-12VDC-SL-A relay and a PEE25-030 transformer, and an IQC PASSED
sticker on the capacitor. The book does not say whether the two are the same board.

No fuse is labelled on this page. The LEDs are on separate cards, and what they mean is the errors section's.
