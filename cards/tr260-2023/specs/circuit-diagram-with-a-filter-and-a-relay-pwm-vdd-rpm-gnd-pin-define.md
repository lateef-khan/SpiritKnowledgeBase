---
id: tr260-2023-specs-circuit-diagram-with-a-filter-and-a-relay-pwm-vdd-rpm-gnd-pin-define
title: 'The circuit diagram: mains through switch, breaker and a filter into the controller,
  an incline motor on down, up and com with a 3-pin incline cable, and a pin define
  that reads relay, PWM, VDD, RPM, GND'
kind: spec
question: What does the circuit diagram in the Xterra tr260-2023 treadmill service
  manual show, and what does it print for the 5-pin cable?
asked_as:
- tr260 wiring diagram
- tr260 circuit diagram
- tr260 5 pin cable pin define
- is there a filter on the tr260 mains
keywords:
- circuit diagram
- wiring diagram
- filter
- breaker
- incline motor
- controller
- pin define
- pwm
- rpm
- computer cable
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- tr150-2021-specs-circuit-diagram-110-v-and-220-v-cegs-with-no-incline-motor
- xterra-trx-specs-circuit-diagram-gt90-family-120-v-and-220-v
see_also:
- xterra-treadmill-specs-main-control-wires-5-pin-sw-vdd-txd-rxd-gnd
- tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: 'TR260 SM (GT75A-NT050) ''8-10 Circuit Diagram'', PDF p. 46 (printed 46)
    ''GT75A-NT050 110V'', lines 713-719, OCR supplement lines 2020-2056; the page
    is printed rotated and was read from a 170 dpi render turned upright. The contradicting
    pin list: PDF p. 41, lines 604-639'
  extracted_at: '2026-09-11'
---

One sheet, **GT75A-NT050 110V TREADMILL CIRCUIT DIAGRAM**, printed sideways on the page.

**Mains path.** AC POWER INPUT plug → CONNECTOR (FEMALE) / AC SOCKET; the green wire (green with yellow) to a ground
lug captioned "CARD". The **white wire** and **black wire** go to the AC SWITCH; the black wire continues through the
**BREAKER**. Both then pass through a **FILTER** box before landing on the CONTROLLER's two **AC** terminals - this
110 V sheet draws the filter that the GT65 and T3 books reserve for their 220 V CE/GS sheets.

**Controller outputs.** **M+** ← motor RED WIRE, **M-** ← motor BLACK WIRE, motor GROUND WIRE; one **JK** to the
**2pin SENSOR WIRE**; the other **JK** to the **5 PIN COMPUTER CABLE (LOWER)** → COMPUTER CABLE (MIDDLE) → console.
Three incline terminals, **DOWN**, **UP** and **COM**, take the INCLINE MOTOR's BLACK, RED and WHITE wires; a **3-PIN
INCLINE COMPUTER CABLE** runs from the motor's sensor to the controller; the incline motor has its own GROUND WIRE.
Two HAND PULSE grips hang off the console.

**Main System Pin Define, as printed on this sheet: 1 RELAY, 2 PWM, 3 VDD, 4 RPM, 5 GND.** This is a different list
from every other Xterra sheet (1 S/W, 2 VDD, 3 TXD, 4 RXD, 5 GND) and from **this same book's p. 41**, which labels
the 5-pin socket "1. SW 2.+12V 3.TXD 4.RXD 5.GND". The book contradicts itself; the driver-board silkscreen is not
legible enough on its photographs to settle it. Meter the cable before trusting either list.
