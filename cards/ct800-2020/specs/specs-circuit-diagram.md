---
id: ct800-2020-specs-circuit-diagram
title: 'The 2020 circuit diagram: a Ya Cheng DC motor, a 20 amp breaker and a 6-pin
  console cable'
kind: spec
question: What does the circuit diagram of a Spirit ct800-2020 treadmill show, and
  which parts does it name?
asked_as:
- wiring diagram for the 2020 ct800
- what motor is in the ct800 2020
- ct800 2020 schematic
- how long are the console cables on the ct800
keywords:
- circuit diagram
- wiring diagram
- schematic
- dc motor
- breaker
- line filter
- harness
- control board
- heat-sink fan
- coil
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2020
  applies_to:
  - ct800-2020
  section: specs
  code: '*'
  model_number:
  - '800840'
authority: 3
not_to_be_confused_with:
- ct850-2020-treadmill-circuit-diagram
- ct800-2016-specs-circuit-diagram
- ct800ent-2022-specs-circuit-diagram
see_also:
- spirit-ct800-specs-driver-board-connector-locations
- spirit-ct800-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-ct800-2020-service-manual
  locator: PDF p. 52 (printed 51), full-page drawing titled 'CT800_ST8600-YT57 TREADMILL
    CIRCUIT DIAGRAM', section 9; text.md lines 797-803, OCR supplement lines 1453-1502;
    read from the 300 dpi render
  extracted_at: '2026-09-11'
---

The page is a flattened image; the values below are read off the 300 dpi render.

| Item | As printed |
|---|---|
| Input power | 120V/60HZ, plug, then an in-line connector |
| Breaker | **20A** |
| Ground wire | green/yellow |
| Line filter | LINE side to the AC switch, LOAD side to the control board, N and L marked |
| Drive motor | **DC MOTOR, Ya Cheng YC782**; white wire to M-, red wire to M+; green/yellow ground wire |
| Heat-sink fan | AC, **115V~ 50/60HZ**, one fan on FAN121 (N) / FAN120 (L) |
| Control board | **AE00301L-002** |
| Incline motor | **JS25-A**, 3-pin VR cable plus red / white / black wires and a green/yellow ground cable |
| Ferrite coils | two "Coil 3", φ35x21x13L |

Harnesses: **6PIN 1100 mm Upper Connection** and **6PIN 2000 mm Bottom Connection**, mated through a
6-pin male / 6-pin female pair, and a **SENSOR wire 1300mm**.

Control board terminals shown: **JK90** (6-pin bottom connection), **JK50** (sensor), **JK60**
(Incline-VR), **JK81** three times (UP, COM, DOWN), **AC IN(1) N / AC IN(2) L**, **FAN121 N / FAN120 L**,
**M-** and **M+**. Mains convention: **N = white wire, L = black wire.**

The CT850-2020 sheet in the sister book has an RM6T6-1003 inverter and a KSP485 AC motor; the CT800-2016
sheet has the same DC motor but a transformer, a 15A breaker and a 12-pin console cable.
