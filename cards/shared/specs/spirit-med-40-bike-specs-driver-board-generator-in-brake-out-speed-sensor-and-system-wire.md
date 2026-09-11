---
id: spirit-med-40-bike-specs-driver-board-generator-in-brake-out-speed-sensor-and-system-wire
title: The driver board photograph names four leads - generator input, generator brake
  output, speed sensor and system wire - on a board with two 330 uF 400 V capacitors
kind: spec
question: What plugs into the driver board (generator controller) of a Spirit Medical
  4.0R or 4.0U bike?
asked_as:
- 4.0r driver board connections
- where is the brake output on the 4.0u controller
- what is the system wire on the spirit medical bike
- generator controller 4.0r
keywords:
- driver board
- generator controller
- generator input
- generator brake output
- speed sensor
- system wire
- pcb component locations
- 330uf 400v
- as 1912
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
not_to_be_confused_with: []
see_also:
- spirit-med-40-bike-specs-circuit-diagram-6-pin-computer-cable-to-a-cs52005-controller
- spirit-med-40-bike-specs-display-board-cs24004-sockets-hp-wp-csafe-gen-and-keypad
- xbr95-2023-specs-generator-controller-cs52005-33-connections
- spirit-cr800-cu800-2021-specs-generator-controller-connections
source:
  ref: spirit-bike-40r-2025-service-manual
  locator: '4.0R: 7-3 Driver Board PCB Component Locations and "Driver Board function",
    PDF pp. 25-26 (printed 25-26), text.md lines 292-299; the call-outs and the board
    read from a 110 dpi render (OCR supplement lines 1093-1113). 4.0U: 7-2 and "Driver
    Board function", PDF pp. 27-28 (printed 22-23), lines 307-330 (the four call-outs
    are native text there)'
  extracted_at: '2026-09-11'
---

Two photographs of the same board. The first (7-3) is uncaptioned; the second, *Driver Board
function*, carries four call-outs:

| Call-out | Where on the board | What the circuit diagram calls it |
|---|---|---|
| **GENERATOR INPUT** | white 3-way plug, top left, beside the large capacitor | J1, *Generator AC_IN, 3 pin (red/white/black wire)* |
| **GENERATOR BRAKE OUTPUT** | white 2-way plug, lower left, red wires | J4, *2 pin red wire brake* |
| **SPEED SENSOR** | small 2-way plug, bottom, black lead | J3, *2 pin sensor* |
| **SYSTEM WIRE** | 6-way plug, bottom right, multicoloured lead | J2, the *6 pin computer cable* to the console |

**What the photograph shows and the text does not:** two black CapXon **330 uF 400 V** electrolytic
capacitors at the generator end, a yellow transformer stamped **2828 / AS 1912**, a heatsinked output
stage and a boxed 2x5 header in the middle. **No board number is legible on this photograph**; the
circuit diagram names the board **CS52005**, and the parts lists call it *Generator/Brake Controller*
(item 43 on the 4.0R, item 21 on the 4.0U).

**No voltage is printed for any of the four leads.** The troubleshooting matrix says only "Check power
to console" and "Replace lower controller" when the LEDs are dim.

The XBR95-2023 book photographs the same board with its sockets silkscreened *3-PHASE GEN IN*, *DC
COIL*, *MAIN CONNECT* and *RPM* - the same four functions
(`xbr95-2023-specs-generator-controller-cs52005-33-connections`).

