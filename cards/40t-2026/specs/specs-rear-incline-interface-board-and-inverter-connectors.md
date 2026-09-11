---
id: 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
title: The rear incline interface board with its 30 amp relay, and the Rhymebus inverter
  connectors
kind: spec
question: Where are the connectors on the rear incline interface board and the inverter
  of a Spirit 40t-2026 treadmill?
asked_as:
- what is the rear incline interface board on the 4.0t
- cs56007 board connectors
- where does the console plug into the 4.0t inverter
- what relay is on the 4.0t interface board
keywords:
- rear incline interface board
- driver board
- inverter
- rhymebus
- relay
- connector
- esp
- console interface
- ac inverter
- high voltage
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 40t-2026
  applies_to:
  - 40t-2026
  section: specs
  code: '*'
  model_number:
  - '740885'
authority: 3
not_to_be_confused_with:
- ct850-2020-driver-board-connector-locations
see_also:
- 40t-2026-specs-circuit-diagram
- 40t-2026-specs-electrical-part-descriptions
- 40t-2026-assembly-rear-incline-motor-replacement
source:
  ref: spirit-treadmill-40t-2026-service-manual
  locator: PDF p. 23 (printed 23) 'DRIVER BOARD PCB Component Locations', text.md
    lines 315-346, OCR supplement lines 1147-1180; PDF p. 24, the inverter, lines
    335-346; board markings read from the renders
  extracted_at: '2026-09-11'
---

The driver-board section has two pages, one per board.

**Rear incline interface board (p. 23)** - silkscreened **CS56007 Rev 1.0** (sticker CS56007-00). Its
terminals, read from the board: **AC IN** with **NEUTRAL** and **AC HOT** spades, **AC OUT**, **J1
INCLINE MOTOR**, **J4 CONSOLE INTERFACE**, **J2 AC INVERTER** and **ESP**. A relay marked **Song Chuan
832A-1A-C, 12V DC coil, 30A 250V~ / 2HP** switches the incline motor, and the board carries a
**HIGH VOLTAGE DANGER** legend. The manual prints no call-outs on this photograph and no pin table.

**Inverter (p. 24)** - a boxed **RHYMEBUS** drive with printed call-outs **INCLINE**, **INCLINE VR**,
**ESP** and **CONSOLE** on the left edge and **AC POWER** and **AC MOTER** (as printed) on the right.
The silkscreen behind the call-outs reads INCLINE, VR, SB, ESP, CONSOLE.

The circuit diagram gives the interface board's plugs as J1, J4 (12-pin, 1200 mm bottom connection), J6
/ J7 (fan) and a "6PIN-2PIN 300mm" link to the inverter's CN3 / CN2, and the inverter's as CN4 (VR) and
CN5 (incline motor). The CT850-2020's Rhymebus inverter has the same left-edge call-outs and no
interface board.
