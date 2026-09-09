---
id: ct850-2016-console-12-pin-connector-pinout
title: 12-pin console-to-driver-board connector, signal and wire colour
kind: spec
question: What is the 12-pin console cable pinout on a Spirit CT850-2016 treadmill,
  and what colour is each wire?
asked_as:
- what are the 12 pins on the ct850 console cable
- wire colours of the treadmill computer cable
- which pin is safe on the 2016 ct850
- system cable pinout
keywords:
- 12 pin
- console cable
- system cable
- pinout
- wire colour
- jk10
- vcc
- safe
- vdd
- adc
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-display-board-connector-locations
- ct850-2016-treadmill-circuit-diagram
- ct850-2016-incline-err-test-procedure
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: p. 4 (printed 3) for the wire colours; p. 40 (printed 39) 'Pin definition,
    JK10' for the signal names
  extracted_at: '2026-09-08'
---

This is the display board's **JK10**, the 12-pin system cable that runs down the mast to the
inverter. The circuit diagram gives the wire colours; the JK10 table on p. 40 gives the signal
names. The two agree pin for pin.

| Pin | Signal (JK10 table) | Wire colour (circuit diagram) |
|---|---|---|
| 1 | VCC5 | Green |
| 2 | VR input (ADC) | Pink |
| 3 | GND | Yellow |
| 4 | Incline up output (UP) | Light blue |
| 5 | Incline down output (DOWN) | Orange |
| 6 | Speed sensor input (SENSOR) | White |
| 7 | SAFE | Red |
| 8 | START | Gray |
| 9 | Speed down output (SLOW) | Brown |
| 10 | Speed up output (FAST) | Purple |
| 11 | GND | Black |
| 12 | VDD | Blue |

On the board the connector is numbered **1 at the bottom rising to 12 at the top**.
