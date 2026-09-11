---
id: spirit-xb-specs-gear-motor-connector-5-pin-definition
title: 'Five pins on the gear motor plug: motor +, motor -, +5 V, position feedback
  (VR or MTR_AD) and ground'
kind: spec
question: What is the gear motor connector pin definition on a Spirit XBR25, XBR55,
  XBU55, XBR55ENT or XBU55ENT bike?
asked_as:
- gear motor wiring on the xbr55
- which pin is motor positive on the xbu55 tension motor
- tension motor connector pinout spirit recumbent
- what is mtr_ad on the xbr55 2023
keywords:
- gear motor
- tension motor
- connector
- pinout
- pin definition
- m+
- m-
- vr
- mtr_ad
- +5v
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbr55-2016
  - xbr55-2023
  - xbr55ent-2021
  - xbu55-2016
  - xbu55-2023
  - xbu55ent-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xb-2016-specs-console-to-driver-board-14-pin-definition
see_also:
- spirit-xb-specs-gear-motor-working-voltage-dc-4-5-to-7-5-v
- sole-bike-tension-motor-connector-pinout
- spirit-xbr55-xbu55-2023-specs-display-to-controller-11-pin-definition
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: 'XBR55-2023: 6.4 Gear Motor connector definition function, PDF p. 10, text.md
    lines 168-172, photograph read from a 300 dpi render (OCR supplement lines 944-950).
    XBU55-2023: PDF p. 10, lines 165-169 (OCR 798-804). XBR55-2016: ''Tension Motor
    connector definition function'', PDF p. 31, lines 420-440. XBR25-2016: PDF p.
    29, lines 396-416. XBU55-2016: PDF p. 29, lines 396-416. XBR55ENT-2021: PDF p.
    21, lines 217-237. XBU55ENT-2021: PDF p. 21, lines 214-234'
  extracted_at: '2026-09-11'
---

One five-way plug on the motor, numbered **5 down to 1** on the motor side and **1 to 5** on the
main-control side. The function of each pin is the same in all seven books; the label changes
between printings.

| Pin | 2016 and ENT 2021 books | 2023 books | What it is |
|---|---|---|---|
| 1 | **M+** | **MTR+** | motor drive |
| 2 | **M-** | **MTR-** | motor drive |
| 3 | **+5V** | **+5Vcc** | supply to the position sensor |
| 4 | **VR** | **MTR_AD** | the position feedback the console reads |
| 5 | **GND** | **GND** | ground |

The 2016 and ENT pages draw the **steel rope** the motor pulls; the 2023 page photographs the
motor with the plug's coloured leads (the wire colours are not named).

**Same list as the Sole B94/R92 tension motor** (`sole-bike-tension-motor-connector-pinout`) -
the Dyaco motor is shared across brands, but that card is a Sole card and this one is Spirit's.

The XBR95 has no gear motor; its brake lead is a two-wire coil on a generator controller.

