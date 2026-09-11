---
id: ct800-2016-specs-circuit-diagram
title: 'The 2016 circuit diagram: a 90 volt DC motor, a 15 amp breaker and a 12-pin
  console cable'
kind: spec
question: What does the circuit diagram of a Spirit ct800-2016 treadmill show, and
  which parts does it name?
asked_as:
- wiring diagram for my 2016 ct800
- what motor does the old ct800 use
- ct800 2016 schematic
- what breaker is in the ct800
keywords:
- circuit diagram
- wiring diagram
- schematic
- dc motor
- transformer
- breaker
- harness
- control board
- heat-sink fan
- coil
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: specs
  code: '*'
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-treadmill-circuit-diagram
- ct800-2020-specs-circuit-diagram
see_also:
- ct800-2016-specs-console-12-pin-cable-pinout
- ct800-2016-specs-driver-board-connectors-and-leds
- ct800-2016-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: Section 1 opener, PDF p. 4 (printed 3), full-page drawing titled 'ST8000(B)-YT09
    TREADMILL CIRCUIT DIAGRAM'; text.md line 61 holds only the folio, the OCR supplement
    at lines 1544-1613 is garbled; read from the 300 dpi render
  extracted_at: '2026-09-11'
---

The page is drawn sideways as one flat image; the values below are read off the 300 dpi render, not off
the extracted text, which is unusable here. The sheet is headed **ST8000(B)-YT09**, the book's own code.

| Item | As printed |
|---|---|
| Input power | 110V/60HZ, plug, then an in-line connector |
| Breaker | **15A** |
| Ground wire | green/yellow, from the connector and from the DC motor |
| AC switch | 450mm black wire and 450mm white wire to the control board |
| Control board | **YJ-2350L** |
| Drive motor | **DC MOTOR, Ya Cheng YC782**; white wire to M-, red wire to M+ |
| Heat-sink fans | two, **AC 110V~ 50/60HZ**, on the board's FAN1 / FAN2 pads |
| Transformer | **06144, 110VAC**, black / red / blue leads to JK5 / JK6 / JK7 |
| Incline motor | **JS25-A**, 3-pin VR cable plus red / white / black wires and a green/yellow ground cable |
| Ferrite coil | one "Coil 3", φ35x21x13L |

Harness lengths on the drawing: **12PIN 400 mm** upper connection, **12PIN 600 mm** middle connection,
**BLACK 12PIN 1700 mm** bottom connection and **SENSOR wire 1300 mm**. The console cable is drawn with
12-pin male / female shells at each break, and its twelve wire colours are on the console-cable card.

Control board terminals shown: **JK1** (12-pin bottom connection), **JK3** (sensor), **JK5 / JK6 / JK7**
(transformer black / red / blue), **JK2** three times (DOWN, COM, UP to the incline motor), **JK4**
(Incline-VR), **AC IN(2) L** and **AC IN(1) N**, **FAN1 L / FAN2 N**, **M+** and **M-**. Mains convention
on the sheet: **N = white wire, L = black wire.**

This is a DC-motor machine with a transformer-fed controller. The CT850-2016 sheet, on the same-shaped
page of that book, shows an AC motor and an inverter instead; the CT800-2020 sheet keeps the DC motor
but drops the transformer and the 12-pin cable. Check which sheet you are holding before you order a part.
