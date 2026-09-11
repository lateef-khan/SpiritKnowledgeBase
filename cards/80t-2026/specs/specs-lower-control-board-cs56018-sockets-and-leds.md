---
id: 80t-2026-specs-lower-control-board-cs56018-sockets-and-leds
title: The CS56018 lower control board switches the mains to the inverter, makes the
  DC, drives both incline motors and the brake, and carries a power LED and two incline
  LEDs
kind: spec
question: What are the sockets and indicator LEDs on the lower control board of a
  Spirit 80t-2026 treadmill, and what does the board do?
asked_as:
- 8.0t lower control board connectors
- cs56018 board
- which led is the power light on the 8.0t lcb
- what does the lcb do on the 8.0t treadmill
keywords:
- lower control board
- lcb
- cs56018
- j16 j17
- j18 j19
- j10 brake
- d17
- d13
- d6
- for feature expansion
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
- spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds
- 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
see_also:
- 80t-2026-specs-electrical-wiring-diagram-lcb-inverter-and-numbered-cables
- 80t-2026-specs-inverter-connectors-and-status-leds
- 80t-2026-specs-fuse-and-breaker-ratings
- spirit-2026t-specs-operating-principle
source:
  ref: spirit-treadmill-80t-2026-service-manual
  locator: Circuit Board, Lower Control Board (#269), PDF p. 17 (printed 17), text.md
    lines 218-223 (the paragraph is native; the photograph and its call-outs read
    from a 130 dpi render); 5. Troubleshooting no-power steps 2-4, PDF pp. 26-28,
    lines 363-378; PGO steps 3-4, PDF p. 30, lines 423-427; incline fault steps 2-3,
    PDF p. 33, lines 470-478
  extracted_at: '2026-09-11'
---

**What it does, in the book's words:** "The input voltage to the inverter is controlled by the LCB
based on whether the system requires sleep mode. Additionally, the LCB performs AC-to-DC conversion
and manages peripheral component control. This includes dual elevation control, step sensor signal
detection, inverter control signal input, electromagnetic brake control, and emergency safety
interruption of the motor drive circuit."

**The board photographed:** a green board silkscreened **CS56018 Rev 1.1**, with a Nuvoton
microcontroller, two Panasonic relays and a large Song Chuan relay at the mains end, on a metal
plate. Call-outs:

| Call-out | What lands there (from the wiring diagram and the procedures) |
|---|---|
| **J16** (NEUTRAL) and **J17** (AC HOT) | mains in from the filter - **meter the AC here first** |
| **J18** and **J19** | mains out to the inverter's CN8 (#258 neutral, #274 line) |
| **J3** | the console cable (#273/#275): +12 V, GND, RX, TX, ERP, safety switch |
| **J2** | #272 RS-485 and safety switch cable from the inverter's CN6 |
| **J1** | a second red socket beside J2, unlabelled on the sheet |
| **J11** | #271 from the step sensor |
| **J6** (silkscreened REAR) and **J7** (FRONT) | the two incline motors' Com / Up / Down |
| **J9** and **J15** | the two incline motors' 3-pin position sensors (GND, VR, +5 V) |
| **J10** | the motor's brake cable - **12 VDC across pins 1 and 3** when the brake is released |
| **J20** | the motor's thermal switch cable |
| two white sockets at the top edge | labelled **For feature expansion** |
| **D17** | **power indicator** |
| **D13** | turns **red as the front platform moves** |
| **D6** | turns **red as the rear platform moves** |
| **D5**, **D12** | on the sheet, not called out on the photograph |

**Using it.** No power: AC at J16/J17, then D17 and 12 VDC on J3 pins 1 and 2 - no 12 V is a new LCB.
RS-485 error: AC out at J18/J19 - none is a new LCB. PGO error: brake not releasing and no 12 V on
J10 pins 1 and 3 is a new LCB; 12 V present and the cable seated is a mechanical brake fault inside
the motor, which is replaced whole. Incline fault: enter a D/A value in maintenance mode, watch D13
(front) or D6 (rear); no light is a new LCB, then swap J9 with J15 and J6 with J7 to see whether the
fault follows the motor.

The firmware file named in the update procedure, **CS56018.bin**, is this board's; CS31003.bin is the
console's. The medical bikes on the same console use a different LCB, the CS51009-01
(`spirit-med-8-bike-specs-lower-control-board-cs51009-01-sockets-and-leds`).

