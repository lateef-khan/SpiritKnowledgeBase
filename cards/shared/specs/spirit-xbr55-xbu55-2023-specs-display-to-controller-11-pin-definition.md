---
id: spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition
title: 'Eleven-pin display board to controller board connector: FLY, PGND, +5Vcc,
  MPOS, GND, MTR-, MTR+, VIN and three spares'
kind: spec
question: What is the display board to controller board connector pin definition on
  a Spirit XBR55 or XBU55 2023 bike?
asked_as:
- xbr55 2023 console connector pinout
- which pin is fly on the xbu55 console board
- mpos pin xbr55
- 11 pin header cs11037
keywords:
- pinout
- pin define
- display board to controller board
- 11 pin
- fly
- pgnd
- mpos
- mtr-
- mtr+
- vin
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr55-2023
  - xbu55-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
see_also:
- spirit-xb-specs-gear-motor-connector-5-pin-definition
- b94-2016-console-to-driver-board-pinout
- spirit-xbr55-xbu55-2023-specs-display-board-cs11037-and-interface-board-connections
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55-2023: ''Test configuration: The console to driver board connector
    pin define function'', PDF pp. 13-14 (printed 13-14 of 30), text.md lines 290-293;
    the list is drawn over the board photograph and was read from a 300 dpi render
    (OCR supplement lines 1011-1024 carries only the board marking). XBU55-2023: PDF
    p. 14, lines 286-292 (OCR 865-891)'
  extracted_at: '2026-09-11'
---

Printed on the error page under "Test configuration", overlaid on the CS11037 board photograph
and pointing at the eleven-way header on the board's left edge:

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| P1 | **FLY** | P7 | **MTR+** |
| P2 | **PGND** | P8 | **VIN** |
| P3 | **+5Vcc** | P9 | N/A |
| P4 | **MPOS** | P10 | N/A |
| P5 | GND | P11 | N/A |
| P6 | **MTR-** | | |

FLY is the flywheel (RPM) signal, MPOS the motor position feedback, VIN the adapter's DC input;
MTR- and MTR+ are the lines the E2 voltage test probes. **The heading says "controller board",
but these bikes have no lower controller** - the header is where the ten-pin computer cable's
branches to the motor, sensor and adapter meet the console PCB.

**Not the 2016 list.** The 2016 XBR/XBU books define a fourteen-way header starting MTR-, MTR+,
+5V (`spirit-xb-2016-specs-console-to-driver-board-14-pin-definition`). This eleven-way list is
the one the Sole B94-2016 and R92-2016 print (`b94-2016-console-to-driver-board-pinout`) - a
Sole card for a Sole machine.

