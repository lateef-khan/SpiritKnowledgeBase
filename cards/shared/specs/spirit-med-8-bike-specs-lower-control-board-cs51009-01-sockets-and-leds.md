---
id: spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds
title: The CS51009-01 lower control board takes 24 V in, sends 12 V to the console,
  drives two brake coil sockets and reads the Hall and angle sensors, with a power
  LED and a revolutions LED
kind: spec
question: What are the sockets and indicator LEDs on the lower control board of a
  Spirit Medical 8.0U or 8.5R bike, and what does the board do?
asked_as:
- 8.0u lower control board connectors
- cs51009 board on the 8.5r
- which led is the power light on the 8.0u lcb
- what does the lcb do on the spirit medical bike
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
- 24 vdc to 12 vdc
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 80u-2025
  - 85r-2025
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- spirit-med-70-bike-specs-wiring-diagram-6-pin-console-9-pin-angle-sensor-and-13-pin-power-cables
see_also:
- spirit-med-8-bike-specs-electrical-wiring-diagram-numbered-cables-and-boards
- spirit-med-8-bike-specs-power-supply-module-mean-well-rps-120s-24-v
- 85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
- spirit-med-8-bike-specs-eddy-current-brake-and-one-hundred-levels
source:
  ref: spirit-bike-80u-2025-service-manual
  locator: '8.0U: 4.4 Circuit Board, 4.4.1 Lower Control Board (#091), PDF p. 18 (printed
    18/51), text.md lines 324-328 (the sentence is native; the photograph and its
    call-outs read from a 130 dpi render); 5.1 No power steps 3-5, PDF pp. 22-23,
    lines 384-399; 5.3 No revolutions, PDF p. 26, lines 420-435. 8.5R: 4.4.1, PDF
    p. 17, lines 250-254; 5.1 and 5.3, PDF pp. 20-21 and 25, lines 280-326; the same
    photograph'
  extracted_at: '2026-09-11'
---

**What it does, in the book's words:** "Power Supply #081 provides 24 VDC to the LCB. The board
converts it to 12 VDC for the console and supplies power to the angle and magnet sensors. Sensor
readings are used to control resistance on Brake #086."

**The board photographed:** a red **CS51009-01 V10** board (sticker *CS51009-01, C11312020002,
04-0100-0004*; CoreStar silkscreen, date code 2340) on an aluminium heat-sink plate, with two large
capacitors and a heatsinked output stage. Call-outs:

| Call-out | Silkscreen beside it | What lands there (from the wiring diagram) |
|---|---|---|
| **J5** | Hall Sensor | the #084 magnet sensor reading the magnet on the drive pulley |
| **J6** | OPTO | unused on these bikes - the 8.5S stepper's step-sensor socket |
| **J8** | obscured by the call-out | the sheet's internal #072 line to CN2 |
| **J4** | CONSOLE | cable #089/#090 to console J3 - **12 VDC out** |
| **J2** | DC 24V | cable #083 from the power supply module - **24 VDC in** |
| **CN1** | Coil2 | brake and angle sensor #086 |
| **CN2** | Coil1 | brake and angle sensor #086 |
| **D13** | a green-boxed LED near J5 | **flashes as the crank turns** - the no-revolutions check |
| **D5** | a green-boxed LED at the bottom | **power indicator** |

**Using it.** The no-power procedure reads D5: off means meter pins 1 and 4 of the power supply's
CN100 for 24 VDC - no 24 V is a new power supply module, 24 V present is a new LCB; on means meter
pins 1 and 2 of the J3 cable at the console for 12 VDC. The no-revolutions procedure watches D13
while pedalling: no flash means check the Hall sensor sits **2 to 3 mm** from the magnet on the drive
pulley, centred between the two arrow marks, then replace LCB and sensor together. A UART error with
the cables sound and a software version reading V255A255 is a firmware update (CS51009-01.bin and
CS31003.bin are this board's and the console's files); otherwise replace LCB and console together.

The same board and photograph are in the 8.5UE book (`85ue-2025-specs-lower-control-board-cs51009-01-sockets-and-leds`)
and the 8.5S stepper book (`85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds`); the 7.0R
and 7.0U use a different, unnumbered brake controller on a 6-pin console cable.

