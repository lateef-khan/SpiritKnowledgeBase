---
id: 40t-2026-specs-circuit-diagram
title: 'The circuit diagram: a KSP485 AC motor on an RM6T6-1003 inverter, a control
  board with two incline motors, and a 20 amp breaker'
kind: spec
question: What does the circuit diagram of a Spirit 40t-2026 treadmill show, and which
  parts does it name?
asked_as:
- wiring diagram for the 4.0t
- 4.0t schematic
- what inverter is in the 4.0t
- how long is the 4.0t console cable
keywords:
- circuit diagram
- wiring diagram
- schematic
- inverter
- ac motor
- breaker
- line filter
- control board
- incline motor
- coil
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
- ct850-2020-treadmill-circuit-diagram
see_also:
- 40t-2026-specs-rear-incline-interface-board-and-inverter-connectors
- 40t-2026-specs-electrical-part-descriptions
- 40t-2026-specs-unit-block-diagram
source:
  ref: spirit-treadmill-40t-2026-service-manual
  locator: 'PDF p. 34 (printed 34), section 9 Circuit Diagram, drawing titled ''ST8700
    TREADMILL CIRCUIT DIAGRAM''; text.md lines 517-522, OCR supplement lines 1341-1401
    (partly misread); read from the 300 dpi render, which is itself a low-resolution
    raster. ST8700A-ST026-01 revision (spirit-treadmill-40t-2026-service-manual-st8700a):
    Circuit diagram, PDF p. 35 (printed 34), text.md lines 547-591, the same "ST8700
    TREADMILL CIRCUIT DIAGRAM" sheet in a worse raster (OCR supplement lines 1331-1362)'
  extracted_at: '2026-09-11'
---

The page is a flattened, low-resolution image; the values below are read off the 300 dpi render and the
blurriest labels are flagged.

| Item | As printed |
|---|---|
| Sheet code | **ST8700** |
| Input power | 120V/60HZ, plug, then an in-line connector |
| Breaker | **RFMB 20A** |
| AC switch | to a line filter, LINE / LOAD sides marked |
| Drive motor | **AC MOTOR KSP485**, three black wires to the inverter's U / V / W, plus a ground wire |
| Inverter | **RM6T6-1003**, "AC100-120V 50/60Hz" as far as the blur reads; CN2 / CN3 from the control board, CN4 3-pin VR cable, CN5 to the incline motor |
| Incline motor | **JS25A**, VR cable plus red / white / black wires and a ground wire, on CN5 |
| Second incline motor | labelled **Decline Motor JS25A**, VR cable plus red / white / black wires and a ground wire, on the control board's J1 |
| Control board | **CS56007-00 CONTROL BOARD**: J1 INCLINE MOTOR, J4 (12-pin, "1200 mm Bottom Connection"), a fan on J6 / J7, N / L pairs, "6PIN-2PIN 300mm" to the inverter's CN3 / CN2 |
| Ferrite coils | two "Coil 3", φ35x21x13L (the OCR misreads one as 30x21x13L) |

Harnesses: **12PIN 600 mm Upper Connection** and **12PIN 1200 mm Bottom Connection**. Mains convention:
**L = black wire, N = white wire.**

The sheet is the only place the book names the inverter model, the motor model and the breaker; the
driver-board pages show the same parts without numbers. The CT850-2020's sheet names the same KSP485
motor, RM6T6-1003 inverter and RFMB 20A breaker, but with 6-pin console cables and no second incline
motor.

**The ST8700A revision of the service manual prints the same sheet**, still titled ST8700 with the
same motor, inverter, breaker and control-board labels; its copy renders worse, with font-substitution
diamonds over some labels, so read the figures from the ST017 book's copy.

