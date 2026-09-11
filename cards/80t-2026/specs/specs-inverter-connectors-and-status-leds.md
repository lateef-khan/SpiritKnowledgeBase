---
id: 80t-2026-specs-inverter-connectors-and-status-leds
title: The inverter drives the motor from its own feedback, on a board with a three-phase
  motor terminal, a three-voltage mains terminal and four status LEDs
kind: spec
question: What connectors and indicator LEDs does the inverter of a Spirit 80t-2026
  treadmill have, and what does the book say it does?
asked_as:
- 8.0t inverter connections
- where does the motor plug into the 8.0t inverter
- tx rx leds on the 8.0t inverter
- what does the inverter do on the 8.0t
keywords:
- inverter
- cn2 u v w
- cn8
- cn6
- cn4
- j5
- err run tx rx
- charge lamp
- motor feedback
- encoder
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
- 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
- mt200-2022-specs-wiring-diagram
see_also:
- 80t-2026-specs-electrical-wiring-diagram-lcb-inverter-and-numbered-cables
- 80t-2026-specs-lower-control-board-cs56018-sockets-and-leds
- spirit-2026t-specs-operating-principle
- 80t-2026-specs-fuse-and-breaker-ratings
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Circuit Board, Inverter (#282), PDF p. 18 (printed 18), text.md lines 223-225
    (the sentence is native; the photograph and call-outs read from a 130 dpi render);
    the wiring diagram PDF p. 15; RS-485 procedure, PDF p. 28, lines 391-403; PGO
    procedure step 5, PDF p. 30, lines 429-432
  extracted_at: '2026-09-11'
---

**"The inverter functions by controlling motor based on motor feedback status."** That is the whole
printed description; the rest is the photograph and the wiring sheet.

**The board photographed:** a green board on a finned aluminium base, four large capacitors, a yellow
transformer, a Tyco **TR90-12VDC-SC-A4** relay beside the mains terminal, a white block on the motor
terminal and a strip of four LEDs. Call-outs:

| Call-out | On the wiring sheet |
|---|---|
| **CN2** | the motor's three phases, terminals marked **U, V, W** |
| **CN8** | mains in from the LCB's J18/J19, terminals marked **L-110, L-N, L-220** - the 110 VAC model uses L-110 and L-N |
| **CN6** | **#272**, the *RS-485 & Safety Switch Cable* to the LCB's J2 (SG+, SG-, GND) |
| **CN4** | a small red socket at the bottom left, unlabelled on the sheet |
| **J5** | a white socket at the top left; the sheet draws the console run **#273-1** starting here |
| **ERR, RUN, TX, RX** | four LEDs beside CN6 - the RS-485 procedure watches **TX and RX** flash |
| **CHARGE** | a lamp at the top right, next to CN2 |

**Using it.** The RS-485 procedure meters the AC at **CN8** first - none means check #258/#274 and
the LCB's AC out; correct AC means check both ends of **#272**, then watch **TX and RX**: no flash is a
new inverter, flashing is a new #272 cable. A PGO error with the brake releasing and the drive train
free is a new inverter and encoder together (#282 and #284); the book's Table 1 gives the no-load
figures to compare against in maintenance mode.

**The error-code table is the inverter's own list** - forty-eight codes from rLEr to StoP, with
mains ranges of 100-120 VAC 60 Hz for the 110 VAC model and 200-240 VAC 50 Hz for the 220 VAC model
- and is carded by code in the errors section. The 4.0T's inverter is a boxed Rhymebus drive with
different call-outs (`40t-2026-specs-rear-incline-interface-board-and-inverter-connectors`); the
7.0T's is the MT8000 board with J-numbered sockets (`mt200-2022-specs-wiring-diagram`).

