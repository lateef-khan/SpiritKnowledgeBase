---
id: spirit-med-40-bike-specs-display-board-cs24004-sockets-hp-wp-csafe-gen-and-keypad
title: The console display board is a CoreStar CS24004 with its sockets silkscreened
  HP/WP, CSAFE, GEN INTERFACE, S.S. INTERFACE, KEY GND and KEY PAD
kind: spec
question: What display board is inside the console of a Spirit Medical 4.0R or 4.0U
  bike, and what sockets does it have?
asked_as:
- 4.0r console board number
- cs24004 board
- what connectors are on the back of the 4.0u display board
- where does the generator cable plug into the spirit medical bike console
keywords:
- display board
- cs24004
- corestar
- pcb component locations
- hp/wp
- csafe
- gen interface
- s.s. interface
- key pad
- buzzer
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40r-2025
  - 40u-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
see_also:
- spirit-med-40-bike-specs-driver-board-generator-in-brake-out-speed-sensor-and-system-wire
- spirit-med-40-bike-specs-circuit-diagram-6-pin-computer-cable-to-a-cs52005-controller
- spirit-cr800-cu800-2021-specs-display-board-cs24005-connections
- xbr95-2023-specs-generator-controller-cs52005-33-connections
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: '4.0R: 7-1 PCB Board Top and 7-2 PCB Board Bottom, PDF pp. 23-24 (printed
    23-24), text.md lines 278-292; the board marking and the socket silkscreen read
    from a 300 dpi render of p. 24 (OCR supplement lines 1049-1091 reads the marking
    only). 4.0U: 7-1, PDF pp. 26-27 (printed 20-21), lines 307-330 (OCR 955-1007);
    the same two photographs'
  extracted_at: '2026-09-11'
---

**Top face (7-1):** a red CoreStar board silkscreened **CS24004 Rev 1.0**, carrying a row of
sixteen-segment message-window digits, the dot-matrix LED block, two three-digit seven-segment groups
and the driver ICs. No call-outs are printed on the photograph.

**Bottom face (7-2):** the assembly sticker reads **CS24004-12MS-V10 (RoHS)**, batch C1080520005. The
sockets are silkscreened, and read from the photograph rather than printed as call-outs:

| Silkscreen | Position | What it is for |
|---|---|---|
| **HP/WP** | bottom left, 4-pin | hand pulse / wireless pulse |
| **CSAFE** | bottom left | the CSAFE POWER and COMM ports the operation chapter describes |
| **GEN INTERFACE** | bottom centre, 6-pin | the 6-pin computer cable from the generator controller |
| **S.S. INTERFACE** | bottom centre, 10-pin header | speed-sensor / second interface header |
| **KEY GND** and **KEY PAD** | bottom right | the membrane keypad |
| a 3-pin socket, a 6-pin socket and a boxed 2x3 header | right edge | unlabelled on the render |
| a round buzzer | top right | the beep the maintenance menu can silence |

A coin cell sits at the lower left. **No pin definition is printed for any socket**, so what is on
each pin of the GEN INTERFACE cable has to come from the controller end
(`xbr95-2023-specs-generator-controller-cs52005-33-connections` photographs the same CS52005 sockets).

The CS24004 is a relative of the **CS24005** in the 2020-generation CR800 and CU800 consoles
(`spirit-cr800-cu800-2021-specs-display-board-cs24005-connections`); do not read one board's socket
list against the other, the 4.0 board carries a CSAFE socket the CS24005 photographs do not show.

