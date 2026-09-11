---
id: 85s-2025-specs-lower-control-board-cs51009-01-sockets-and-leds
title: The CS51009-01 lower control board takes 24 V in, sends 12 V to the console,
  drives two brake coil sockets and reads two sensor sockets, with a power LED to
  check first
kind: spec
question: What are the sockets and indicator LEDs on the lower control board of a
  Spirit 85s-2025 recumbent stepper, and what does the board do?
asked_as:
- 8.5s lower control board connectors
- cs51009 board
- which led is the power light on the 8.5s lcb
- what does the lcb do on the 8.5s stepper
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
  product_line: climber
  model: 85s-2025
  applies_to:
  - 85s-2025
  section: specs
  code: '*'
  model_number:
  - '785545'
authority: 3
not_to_be_confused_with:
- csc880-2025-specs-controller-seven-cables-named
see_also:
- 85s-2025-specs-electrical-wiring-diagram-numbered-cables-and-boards
- 85s-2025-specs-power-supply-module-mean-well-rps-120s-24-v
- spirit-climber-specs-electromagnet-eddy-current-brake
source:
  ref: spirit-stepper-85s-2025-service-manual
  locator: 4-4 Circuit Board, 4.4.1 Lower Control Board (#105), PDF p. 13 (printed
    13), text.md lines 189-193 (the sentence is native; the photograph with its callouts
    read from a 150 dpi render, OCR supplement 786-806); 5-1 No power steps 3-4, PDF
    p. 17, lines 234-244
  extracted_at: '2026-09-11'
---

**What it does, in the book's words:** "Power Supply #081 provides 24 VDC to the LCB. The board
converts it to 12 VDC for the console and supplies power to the angle and magnet sensors. Sensor
readings are used to control resistance on Brake #086." (The diagram numbers the power supply
#097 and the brake #085; the sentence's numbers are slips.)

**The board photographed:** a red **CS51009-01 V10** board (sticker *CS51009-01, C11312020002,
04-0100-0004*; CoreStar silkscreen, Rev 1.4, date code 2340) on an aluminium heat-sink plate, with
two large capacitors and a heatsinked output stage. Callouts:

| Callout | Silkscreen beside it | What lands there (from the wiring diagram) |
|---|---|---|
| **J5** | Hall Sensor | the brake's magnet/angle sensor lines |
| **J6** | OPTO | IR reflective sensor board #106 (step position and direction) |
| **J8** | obscured by the callout (reads like ISP) | cable #181, a ten-way socket |
| **J4** | CONSOLE | cable #103/#104 to console J3 - **12 VDC out** |
| **J2** | DC 24V | cable #099 from the power supply module - **24 VDC in** |
| **CN1** | Coil2 | brake #085, cable #102 |
| **CN2** | Coil1 | brake #085, cable #102 |
| **D13** | a green-boxed LED near J5 | - |
| **D5** | a green-boxed LED at the bottom | **power indicator** |

**Using it.** The no-power procedure reads D5: if it is off, meter pins 1 and 4 of the power
supply's CN100 for 24 VDC - no 24 V means a new power supply module, 24 V present means a new
LCB; if D5 is on, meter pins 1 and 2 of the J3 cable at the console for 12 VDC. A UART error with
the cables sound and a software version reading V255A255 is a firmware update; otherwise replace
LCB and console together.

CN1/CN2 are marked Coil1/Coil2 because the 8.5S brakes with an electromagnet on a disc rather than
a gear-motor magnet (`spirit-climber-specs-electromagnet-eddy-current-brake`); there is no tension
motor on this board.

