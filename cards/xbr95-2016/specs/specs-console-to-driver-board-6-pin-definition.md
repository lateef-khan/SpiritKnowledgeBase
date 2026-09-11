---
id: xbr95-2016-specs-console-to-driver-board-6-pin-definition
title: 'Six-pin console to driver board cable: 12 VDC, GND, a 6 or 5 VDC rail, NC,
  RES or PWM, and RPM or SPD - the two ends labelled differently'
kind: spec
question: What is the console to driver board connector pin definition on a Spirit
  xbr95-2016 recumbent bike?
asked_as:
- xbr95 2016 console cable pinout
- 6 pin cable xr829
- which pin is pwm on the xbr95 driver board
- res pin xbr95 console
keywords:
- pinout
- pin define
- console to driver board
- 6 pin
- 12 vdc
- 6 vdc
- 5 vdc
- res
- pwm
- rpm
facets:
  brand:
  - spirit
  product_line: bike
  model: xbr95-2016
  applies_to:
  - xbr95-2016
  section: specs
  code: '*'
  model_number:
  - '951115'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
- sole-bike-7-pin-console-cable-pinout
see_also:
- spirit-xbr95-2016-cu800-2012-specs-generator-controller-031101b-connections
- xbr95-2016-specs-display-amplifier-and-interface-board-connections
source:
  ref: spirit-bike-xbr95-2016-service-manual
  locator: '''Test configuration. The console to driver board connector pin define
    function'', PDF p. 39, text.md lines 528-545, and ''Test Configuration. Driver
    board control function relate parts location'', PDF p. 40, lines 547-570 (OCR
    supplement lines 1528-1583); photographs read from a 300 dpi render'
  extracted_at: '2026-09-11'
---

Two pages, two lists for the two ends of the same six-way cable, numbered **6, 5, 4, 3, 2, 1** on
the drawing:

| Pin | Console end (p. 39) | Driver-board end (p. 40) |
|---|---|---|
| 1 | **12 VDC** | 12 VDC |
| 2 | GND | GND |
| 3 | **+6 VDC** | **+5 VDC** |
| 4 | NC | NC |
| 5 | **RES** | **PWM** |
| 6 | **RPM** | **SPD** |

**Pin 3 is printed +6 VDC at the console and +5 VDC at the driver board**, and pins 5 and 6 are
named for what they carry (the resistance command and the speed pulse) with different words at
each end. The book does not reconcile them; treat pin 3 as one rail whose nominal value the two
pages disagree on, and measure before assuming either.

The p. 40 photograph also marks the board's **GENERATOR BRAKE OUTPUT** and **GENERATOR INPUT**
plugs; the troubleshooting text on p. 41 calls the console-cable socket **CN2** and speaks of an
"8-PIN cable" for the same link - a third count for one cable.

The Sole LCB/LCR 2016 print a seven-pin list with a D/A pin (`sole-bike-7-pin-console-cable-pinout`)
- a different machine.

