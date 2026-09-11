---
id: 85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
title: The CS51009-01 lower control board, numbered 084 in this book, takes 24 V in
  and sends 12 V to the console, with a power LED and a revolutions LED
kind: spec
question: What are the sockets and indicator LEDs on the lower control board of a
  Spirit 8.5UE upper body ergometer (85ue-2025), and what does the board do?
asked_as:
- 8.5ue lower control board connectors
- cs51009 board on the ube
- which led is the power light on the 8.5ue lcb
- what does the lcb do on the upper body ergometer
keywords:
- lower control board
- lcb
- cs51009-01
- j2 dc 24v
- j4 console
- cn1 cn2 coil
- hall sensor
- d5
- d13
- upper body ergometer
facets:
  brand:
  - spirit
  product_line: ergometer
  model: 85ue-2025
  applies_to:
  - 85ue-2025
  section: specs
  code: '*'
  model_number:
  - '785045'
authority: 3
not_to_be_confused_with:
- 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
see_also:
- spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85ue-2025-specs-electrical-wiring-diagram-renumbered-parts
- 85ue-2025-specs-power-supply-module-mean-well-rps-120s-24-v
- 85ue-2025-specs-eddy-current-brake-and-fifty-levels
source:
  ref: spirit-bike-85ue-2025-service-manual
  locator: 4.4 Circuit Board, 4.4.1 Lower Control Board (#084), PDF p. 17 (printed
    17), text.md lines 227-231 (sentence native; the photograph read from a 110 dpi
    render); 5.1 No power steps 3-5, PDF p. 22, lines 270-275; 5.3 No revolutions,
    PDF p. 25, lines 302-312
  extracted_at: '2026-09-11'
---

**In the book's words:** "Power Supply #075 provides 24 VDC to the LCB. The board converts it to 12
VDC for the console and supplies power to the angle and magnet sensors. Sensor readings are used to
control resistance on Brake #079."

The photograph is the one the 8.0U and 8.5R books print - a red **CS51009-01 V10** (sticker
*CS51009-01, C11312020002, 04-0100-0004*) on a heat-sink plate - with the same call-outs: **J5** Hall
Sensor, **J6** OPTO, **J8**, **J4** CONSOLE (12 VDC out), **J2** DC 24V (24 VDC in), **CN1** Coil2 and
**CN2** Coil1 to the brake, **D13** the LED that flashes as the crank turns, **D5** the power
indicator. The full socket table with what lands on each is on the bike card
(`spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds`); this card exists because
the ergometer is its own product line and the part carries its own number here.

**Using it.** D5 off: meter pins 1 and 4 of CN100 on the power supply for 24 VDC - none means a new
power supply module, 24 V means a new LCB. D5 on: meter pins 1 and 2 of the J3 cable at the console
for 12 VDC. No revolutions: watch D13 while cranking; no flash means check the Hall sensor (078) sits
**2 to 3 mm** from the magnet on the **Chain Wheel (208)** - on this machine the magnet is on a chain
wheel, not a drive pulley - then replace LCB and Hall sensor together.

The firmware files named in the update procedure, CS51009-01.bin and CS31003.bin, are this board's
and the console board's.

