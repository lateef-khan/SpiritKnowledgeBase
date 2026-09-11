---
id: 80t-2026-specs-electrical-wiring-diagram-lcb-inverter-and-numbered-cables
title: Electrical wiring diagram for the 110 VAC model with a CS56018 lower control
  board feeding a separate inverter, two incline motors, a step sensor, a safety switch
  module and every cable numbered
kind: spec
question: What does the electrical wiring diagram of the Spirit 80t-2026 treadmill
  service manual show, and what is on the console, RS-485 and incline-motor connectors?
asked_as:
- 8.0t wiring diagram
- what is cable 273 on the 8.0t
- 8.0t console j3 pinout
- rs-485 cable between the lcb and inverter 8.0t
keywords:
- wiring diagram
- lower control box configuration
- cs56018
- cs31003
- inverter
- rs-485
- safety switch module
- step sensor
- incline motor
- cable numbers
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 80t-2026
  applies_to:
  - 80t-2026
  section: specs
  code: '*'
  model_number:
  - '780885'
authority: 3
not_to_be_confused_with:
- mt200-2022-specs-wiring-diagram
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
see_also:
- 80t-2026-specs-lower-control-board-cs56018-sockets-and-leds
- 80t-2026-specs-inverter-connectors-and-status-leds
- 80t-2026-specs-part-description-twenty-numbered-parts
- 80t-2026-specs-fuse-and-breaker-ratings
- mt200-2022-specs-wiring-diagram
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: '"Lower Control Box Configuration - For 110 VAC model - Electrical Wiring
    Diagram", PDF p. 15 (printed 15), text.md lines 214-217, a flat drawing read from
    a 300 dpi render (OCR supplement lines 974-1028 is partial); "Electrical Wiring
    Photo", PDF p. 16, lines 217-218. Cable numbers used again in 5. Troubleshooting,
    PDF pp. 26-34, lines 358-478'
  extracted_at: '2026-09-11'
---

The sheet is headed **For 110 VAC model** - the book names a 220 VAC model too, in its error-code
table, and prints no sheet for it. Every part and cable carries a **# number**, the book's own item
numbers, which the troubleshooting chapter reuses.

**Boards and parts**

| # | Part | Sockets drawn |
|---|---|---|
| #250 | **Console**, board **CS31003-1** | USB, J6, J5, J9, J4, J3 |
| #269 | **Lower Control Board**, **CS56018** | J1, J2, J3, J9, J15, J6, J7, J11, J16, J17, J18, J19, J20, J10; LEDs D5, D12, D17, D13, D6 |
| #282 | **Inverter** | J5, CN6, CN4, CN2 (U, V, W), CN8 (L-110, L-N, L-220); LEDs ERR, RUN, TX, RX; a CHARGE lamp |
| #280 | **Motor**, with **#284 Encoder** on its end | three phase leads, a Thermal Switch Cable, a Brake Cable, **#281** grounded cable |
| #276 / #277 | **Front Incline Motor** / **Rear Incline Motor** | into the LCB's incline sockets |
| #270 | **Step Sensor** | **#271** into LCB **J11** |
| #251 | **Safety Switch Module** | **#252** into the console |
| #260 | **AC Power Entry Module with Switch and Breaker** | **#265** Line (black), **#261** Neutral (white) |
| #262 | **Breaker** | in the neutral run, **#261** in and **#255** out |
| #263 | **Filter** | **#265** Line and **#255** Neutral in, **#264** grounded cable, then #265 and #255 on to LCB **J16** and **J17** |
| #253 | **Data Transfer Board** (a DB9 and a USB-B) | **#256/#254/#254-1** and **#259/#257/#257-1**, two inline runs from the console |

**Cables between the boards**

| # | From | To |
|---|---|---|
| **#273-1 / #273 / #275** | inverter **J5** and LCB **J3**, drawn as one run | console **J3** - the UART error's "cables #273-1, #273 and #275" |
| **#272** | inverter **CN6** | LCB **J2** - *RS-485 & Safety Switch Cable* |
| **#258** Neutral (white), **#274** Line (brown) | LCB **J18 / J19** | inverter **CN8** - the AC the LCB switches to the inverter |
| **#279** | *Encoder Cable* | to the **#284 Encoder** on the motor; the PGO procedure checks it "at both the LCB and the encoder" |
| Thermal Switch Cable / Brake Cable | LCB **J20** / **J10** | the motor |

**The three pin tables printed on the sheet**

*J3 on #269 (console cable):* 1 +12 V, 2 GND, 3 RX, 4 TX, 5 ERP, 6 Safety Switch - **+12 V attached,
0 V unattached**.

*J2 on #269 (RS-485 & safety switch cable):* 1 SG+, 2 SG-, 3 N/A, 4 N/A, 5 N/A, 6 GND.

*J15 & J9 on #269 (incline motors):* Com - Common, Up - incline up, Down - incline down; 1 GND, 2
position(VR), 3 +5 V.

**What the numbers agree with.** The no-power procedure meters AC at J16 and J17, checks D17 and
12 VDC on J3 pins 1 and 2, then J3 at the console; the RS-485 procedure meters AC at CN8, checks
#258 and #274 and the AC out at J18/J19, then #272 and the inverter's TX/RX LEDs; the PGO procedure
meters 12 VDC across pins 1 and 3 of J10 for the brake; the incline procedure swaps J9 with J15 and
J6 with J7 to move a fault from front to rear. The boards themselves are on
`80t-2026-specs-lower-control-board-cs56018-sockets-and-leds` and
`80t-2026-specs-inverter-connectors-and-status-leds`.

**The 7.0T on the MT8000 book is wired differently** - its console talks to the inverter on its own
RS-485 socket and its LCB has no relay for the inverter's mains
(`mt200-2022-specs-wiring-diagram`); do not read one sheet's socket numbers against the other.

