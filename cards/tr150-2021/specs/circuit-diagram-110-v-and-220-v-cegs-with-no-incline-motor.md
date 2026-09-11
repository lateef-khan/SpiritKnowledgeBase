---
id: tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
title: 'The circuit diagram: mains through the AC switch and breaker into the controller,
  motor on M+ red and M- black, a 2-pin sensor wire and a 5-pin computer cable; the
  220 V CE/GS sheet adds a filter and choke'
kind: spec
question: What does the circuit diagram in the Xterra tr150-2021 treadmill service
  manual show, and how does the 220 V CE/GS sheet differ?
asked_as:
- tr150 wiring diagram
- tr150 circuit diagram
- which wire goes to the breaker on the tr150
- tr150 220 volt version
keywords:
- circuit diagram
- wiring diagram
- ac switch
- breaker
- controller
- motor wires
- computer cable
- sensor wire
- filter choke
- cegs
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr150-2021
  applies_to:
  - tr150-2021
  section: specs
  code: '*'
  model_number:
  - '450887'
authority: 3
not_to_be_confused_with:
- trx1400-2023-specs-circuit-diagram-110-v-and-220-v-cegs
- tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
see_also:
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- tr150-2021-specs-driver-board-b426d-wire-connections
- tr150-2021-specs-mcb-terminal-map-from-the-annotated-photograph
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM (GT65-NT014) '8.9 Circuit diagram', PDF p. 46 (printed 54) 'GT65-NT014
    110V', lines 804-810, OCR supplement lines 1301-1328; PDF p. 47 (printed 55) 'GT65-NT014
    220V CEGS', lines 810-811, OCR supplement lines 1329-1368. Both sheets read from
    a 170 dpi render
  extracted_at: '2026-09-11'
---

Two sheets, **GT65-NT014 110V** and **GT65-NT014 220V CEGS**, both headed TREADMILL CIRCUIT DIAGRAM. There is no
incline motor on either.

**Mains path (110 V sheet).** AC POWER INPUT plug → CONNECTOR (FEMALE) / AC SOCKET. From the socket: the **green
wire (green with yellow)** to ground; the **white wire** to the AC SWITCH; the **black wire** to the AC SWITCH. From
the switch the black wire goes through the **BREAKER** and, with the white wire, into the CONTROLLER's two **AC**
terminals.

**Controller outputs.** **M+** ← motor **RED WIRE**; **M-** ← motor **BLACK WIRE**; the motor also has a GROUND WIRE.
One **JK** takes the **2pin SENSOR WIRE**; the other **JK** takes the **5 PIN COMPUTER CABLE (LOWER)**, which joins
the **COMPUTER CABLE (MIDDLE)** and runs up to the console. Two HAND PULSE grips hang off the console.

**Main System Pin Define** (printed on both sheets): 1 S/W, 2 VDD, 3 TXD, 4 RXD, 5 GND - see the 5-pin card.

**220 V CEGS sheet.** Identical except that the white and black wires from the switch and breaker pass through a
**FILTER** and a **CHOKE** before reaching the controller's AC terminals; the ground lug is captioned "CARD". This is
the "additional Filter Choke circuit" the book's p. 3 note describes for the 230 VAC version.

The driver board this feeds is the B426D on the wire-connections card; the annotated MCB photograph shows the same
terminals on a real board.
