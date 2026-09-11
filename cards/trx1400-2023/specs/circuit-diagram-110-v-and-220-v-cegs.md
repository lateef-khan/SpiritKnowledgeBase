---
id: trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
title: 'The circuit diagram: mains through the AC switch and breaker into the controller,
  quick handrail buttons with the hand pulse, an incline motor on down, up and com
  with a 3-pin VR cable; the 220 V CE/GS sheet adds a filter choke'
kind: spec
question: What does the circuit diagram in the Xterra trx1400-2023 treadmill service
  manual show, and how does the 220 V CE/GS sheet differ?
asked_as:
- trx1400 wiring diagram
- trx1400 circuit diagram
- trx1400 incline motor wires on the controller
- trx1400 220 volt version
keywords:
- circuit diagram
- wiring diagram
- breaker
- incline motor
- incline vr cable
- controller
- computer cable
- quick handrail button
- filter choke
- cegs
facets:
  brand:
  - xterra
  product_line: treadmill
  model: trx1400-2023
  applies_to:
  - trx1400-2023
  section: specs
  code: '*'
  model_number:
  - '140082'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
see_also:
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- trx1400-2023-specs-driver-board-b307d-wire-connections
- trx1400-2023-specs-incline-position-sensor-pin-1-is-5-volts
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: TRX1400 SM (T3-NT053-01) '8.9 Circuit diagram', PDF p. 58 (printed 57)
    'T3-NT053 110V', lines 1073-1083, OCR supplement lines 2417-2461; PDF p. 59 (printed
    58) 'T3-NT053 220V CEGS', lines 1083-1089, OCR supplement lines 2462-2506. The
    110 V sheet read from a 150 dpi render
  extracted_at: '2026-09-11'
---

Two sheets, **T3-NT053 110V** and **T3-NT053 220V CEGS**, both headed TREADMILL CIRCUIT DIAGRAM.

**Mains path (110 V sheet).** AC POWER INPUT plug → CONNECTOR (FEMALE) / AC SOCKET; **green wire (green with
yellow)** to ground; **white wire** and **black wire** to the AC SWITCH; the black wire through the **BREAKER**; both
into the CONTROLLER's two **AC** terminals.

**Controller outputs.** **M+** ← motor RED WIRE, **M-** ← motor BLACK WIRE, motor GROUND WIRE. One **JK** takes the
**2pin SENSOR WIRE**; the other **JK** takes the **5 PIN COMPUTER CABLE (LOWER)** → COMPUTER CABLE (MIDDLE) → console.
Three incline terminals **DOWN**, **UP** and **COM** take the INCLINE MOTOR's **BLACK**, **RED** and **WHITE** wires;
an **INC VR 3-PIN INCLINE VR CABLE** comes back from the motor's position sensor; the incline motor has its own GROUND
WIRE.

**Console side.** Two grips captioned "HAND PULSE & Quick handrail button" hang off the console - the handrail
speed and incline buttons share the grip with the pulse plates.

**Main System Pin Define**: 1 S/W, 2 VDD, 3 TXD, 4 RXD, 5 GND, the same on both sheets and on the book's p. 48
pin-define page.

**220 V CEGS sheet.** Identical except for a **FILTER CHOKE** box between the switch/breaker and the controller's AC
terminals - the "additional Filter Choke circuit" of the book's p. 5 note on the 230 VAC version.
