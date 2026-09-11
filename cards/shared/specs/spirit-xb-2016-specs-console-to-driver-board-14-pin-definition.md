---
id: spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
title: 'Fourteen-pin console to driver board connector: MTR-, MTR+, +5V, MPOS, GND,
  RPM1, GND, RPM2, GND, +12V and four spares'
kind: spec
question: What is the console to driver board connector pin definition on a Spirit
  XBR25, XBR55 or XBU55 2016 bike?
asked_as:
- xbr55 2016 console cable pinout
- which pin is rpm on the xbu55 console connector
- mpos pin spirit recumbent
- 14 pin connector xbr25
keywords:
- pinout
- pin define
- console to driver board
- 14 pin
- mtr-
- mtr+
- mpos
- rpm1
- rpm2
- +12v
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbr55-2016
  - xbu55-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition
- xbr95-2016-specs-console-to-driver-board-6-pin-definition
see_also:
- spirit-xb-specs-gear-motor-connector-5-pin-definition
- spirit-xb-2016-specs-display-board-cs11016-and-interface-board-connections
- b94-2016-console-to-driver-board-pinout
source:
  ref: spirit-bike-xbr55-2016-service-manual
  locator: 'XBR55-2016: ''Test configuration. The console to driver board connector
    pin define function'', PDF p. 40, text.md lines 564-592 (OCR supplement lines
    1606-1632). XBR25-2016: PDF p. 38, lines 543-571 (OCR 1538-1574, which also shows
    the board sticker). XBU55-2016: PDF p. 38, lines 543-571 (OCR 1405-1431). Identical
    lists'
  extracted_at: '2026-09-11'
---

Printed inside the error chapter as a "test configuration", but it is a connector definition. The
header is numbered **14 down to 1** in the drawing and the list reads:

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | **MTR-** | 8 | **RPM2** |
| 2 | **MTR+** | 9 | GND |
| 3 | **+5V** | 10 | **+12V** |
| 4 | **MPOS** | 11 | N/A |
| 5 | GND | 12 | N/A |
| 6 | **RPM1** | 13 | N/A |
| 7 | GND | 14 | N/A |

MTR- and MTR+ are the two motor lines that the E2 / "- -" voltage test probes (+5.5 to 6.0 V DC
on Level Up, the reverse on Level Down); MPOS is the motor's position feedback, the *VR* pin of
the motor plug. The XBR25 book's photograph shows the board this header sits on as a CoreStar
board, but the marking is not legible enough to quote.

**Ten used pins here against eleven on the 2023 boards**, whose list starts FLY, PGND, +5Vcc -
`spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition`. The Sole B94-2016 prints
that 11-pin list, not this one (`b94-2016-console-to-driver-board-pinout`).

**The ENT 2021 books drop this page**: they keep the motor plug definition but print no
console-to-board list at all.

