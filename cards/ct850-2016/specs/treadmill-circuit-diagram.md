---
id: ct850-2016-treadmill-circuit-diagram
title: 2016 treadmill circuit diagram and named electrical parts
kind: spec
question: What does the circuit diagram of a Spirit CT850-2016 treadmill show, and
  which parts does it name?
asked_as:
- wiring diagram for my 2016 ct850
- what inverter is in the old ct850
- what motor does the 2016 ct850 use
- ct850 2016 schematic
keywords:
- circuit diagram
- wiring diagram
- schematic
- inverter
- ac motor
- filter
- incline motor
- breaker
- harness
- coil
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-treadmill-circuit-diagram
see_also:
- ct850-2016-inverter-board-connector-locations
- ct850-2016-console-12-pin-connector-pinout
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'p. 4 (printed 3), full-page drawing titled ''SPIRIT #CT850(ST8100-CT001)
    TREADMILL CIRCUIT DIAGRAM'''
  extracted_at: '2026-09-08'
---

The page is drawn sideways as one flat image; the values below are read off the 300 dpi render,
not off the extracted text, which is unusable here.

| Item | As printed |
|---|---|
| Input power | 120V/60HZ, plug then in-line connector |
| Breaker | 20A |
| Ground wire | green/yellow, from the connector and from the AC motor |
| Line filter | GD20-FCC110A, 115V/20A, 50/60 HZ, LINE side to AC switch, LOAD side to inverter |
| AC motor | Kuo Shuay **KSP131**, three black wires |
| Heat-sink fan | AC, 110V~ 50/60HZ, wired to the inverter's FAN1/FAN2 pads |
| Inverter | **RM6T3-1003B** |
| Incline motor | **JS25-A**, 3-pin VR cable plus red / white / black power wires and a green/yellow ground |
| Ferrite coils | one "Coil 5" and two "Coil 3", all φ35x21x13L |

Harness lengths on the drawing: **12PIN 700 mm** upper connection, **BLACK 12PIN 1700 mm** DOWN
connection, **BLACK 12PIN TO 6PIN 300 mm** bottom connection, **SENSOR wire 1300 mm**, and
450 mm white and black wires between the AC switch and the filter. The console cable ends in a
12-pin male and a 12-pin female shell.

Inverter terminals shown: TB1 (AC IN(N), AC IN(L)), CN13 to the incline VR, CN6 to the incline
motor UP / COM / DOWN, CN10 down to the console, and u / v / w out to the AC motor.
Mains wiring convention on the sheet: **L = black wire, N = white wire.**

The 2020 CT850 manual prints a different circuit diagram with different part numbers.
