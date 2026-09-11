---
id: xterra-specs-resistance-set-from-the-console-by-a-gear-motor-on-a-magnetic-brake
title: Resistance is changed from the console; where the book names the mechanism
  it is a gear motor moving a magnetic brake
kind: spec
question: What kind of resistance does an Xterra SB recumbent or upright bike, FS
  or EU elliptical, or RSX seated stepper have - magnetic, motorised, or a knob?
asked_as:
- is the xterra recumbent bike magnetic resistance
- does the sb250 have a resistance knob
- how does the resistance change on the xterra elliptical
- gear motor resistance bike
keywords:
- magnetic resistance
- gear motor
- tension motor
- electronic resistance
- auto tension
- magnetic wheel
- console controlled
- up down keys
- motor cable
- eddy current
facets:
  brand:
  - xterra
  product_line: '*'
  model: '*'
  applies_to:
  - eu150-2024
  - fs15-2019
  - fs150-2016
  - fs25-2020
  - fs35-2020
  - fs58e-2013
  - fs59e-2014
  - rsx1500-2021
  - sb150-2018
  - sb240-2023
  - sb250-2024
  - sb25r-2020
  - sb4500-2021
  - sb45r-2013
  - sb500-2020
  - sb600-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- xterra-specs-resistance-has-24-levels
- xterra-specs-resistance-has-16-levels
- xterra-specs-resistance-level-count-not-printed
- xterra-specs-external-power-adapter-with-no-rating-printed
- xterra-specs-manual-tension-knob-with-8-levels
- spirit-cycle-specs-resistance-systems
source:
  ref: xterra-bike-sb250-2024-owners-manual
  locator: 'SB250 OM ''The cycle is auto tension system'', PDF p. 17 (printed 15),
    text.md line 518; Trouble Shooting ''Magnetic wheel not working properly'', ''gear
    motor'', ''magnetic system'', PDF p. 25 (printed 23) lines 806-870; assembly ''Adapter''
    p. 14. SB150 OM the same table p. 24 (printed 22) lines 711-775; FS150 (scan)
    p. 24 OCR lines 1003-1060; SB240 OM ''Upper Motor Cable (45) with the Lower Motor
    Cable (48)'' p. 13 lines 406-410 and Error Messages ''gear motor'' p. 41 (printed
    40) lines 1258-1276; SB500 OM Engineering Mode ''Motor Test - Continually runs
    the tensioning gear motor'', p. 22 (printed 20) line 807; SB4.5r (scan) p. 22
    OCR line 920; FS5.9e (scan) p. 26 OCR; SB4500 parts list ''Motor'' (72) and ''Motor
    Cable 400mml'' (69), p. 28 lines 1031-1034; SB600 SM parts A1 MOTOR line 208 and
    ''Replacing the Motor and Idler Wheel Assembly'' pp. 29-30 lines 499-511. Console-adjusted
    with no motor named: SB2.5r p. 15 (printed 13) lines 476-478 and p. 18 lines 598-601;
    FS1.5 p. 17 lines 578-581; FS2.5 p. 14 lines 514-516; FS3.5 p. 14; RSX1500 p.
    21 lines 612-614; EU150 key functions p. 17 lines 443-448 and HRC p. 21; FS5.8e
    (scan) p. 14 OCR lines 512-516'
  extracted_at: '2026-09-11'
---

**These sixteen machines have no resistance knob: the load is set from the console with the UP and DOWN keys
(+/- on the SB4500), and the console changes it on its own in the heart-rate and watt programs.** The books that
name the hardware call it a **gear motor** working a **magnetic** brake:

| Machine | Where the book names it |
|---|---|
| SB150, SB250, FS150 | the troubleshooting table: "Magnetic wheel not working properly - replace magnetic wheel", "E1 ... the gear motor", "wire cable from gear motor to magnetic system is too short"; the SB250 adds "The cycle is auto tension system. The monitor will only function while you insert adaptor" |
| SB240 | assembly connects the "Upper Motor Cable (45) with the Lower Motor Cable (48)"; the error-message page describes the gear motor's count signal |
| SB500, SB4.5r, FS5.9e | engineering mode: "Motor Test - Continually runs the tensioning gear motor" (SB500 also "Manual - Allows stepping of the gear motor") |
| SB4500 | parts list: Motor (72), Motor Cable 400 mm (69), Flywheel (62) |
| SB600 | service manual parts: A1 MOTOR, with a replacement procedure and a spring on the motor brace |
| SB2.5r, FS1.5, FS2.5, FS3.5, RSX1500, EU150, FS5.8e | the mechanism is not named; the books say only that "the computer will adjust the resistance load automatically" and that the load changes "gradually" after a key press |

The Important Operation Instructions of the SB240, SB600, SB4500, SB4.5r, SB500, RSX1500, FS5.8e and FS5.9e books
explain the delay: "changes in resistance do not occur immediately. Set
your desired level on the computer console and release the adjustment key. The computer will obey the command
gradually." All sixteen run from an external adapter (`xterra-specs-external-power-adapter-with-no-rating-printed`).
The level counts are on their own cards; the EU100, SB120 and UB120 use a manual 8-level knob instead, and the
indoor cycles a friction pad.

