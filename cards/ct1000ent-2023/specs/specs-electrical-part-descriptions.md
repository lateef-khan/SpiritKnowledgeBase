---
id: ct1000ent-2023-specs-electrical-part-descriptions
title: What each electrical part does, with a 220 volt AC drive motor and a 230 volt
  incline motor
kind: fact
question: What does each electrical part do on a Spirit ct1000ent-2023 treadmill,
  and what voltages do the motors run on?
asked_as:
- what voltage is the incline motor on the ct1000
- is the ct1000 ent a 230 volt machine
- incline motor wire colours ct1000
- what does the main controller do
keywords:
- electrical configuration
- main controller
- ac motor
- incline motor
- safety key
- console
- voltage
- wire colour
- tft
- 230 volt
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct1000ent-2023
  applies_to:
  - ct1000ent-2023
  section: specs
  code: '*'
  model_number:
  - '210854'
authority: 3
not_to_be_confused_with:
- ct900ent-specs-electrical-part-descriptions
- ct900-specs-electrical-part-descriptions
see_also:
- ct1000ent-2023-specs-circuit-diagram
- ct1000ent-2023-specs-io-board-connectors
source:
  ref: spirit-treadmill-ct1000ent-2023-service-manual
  locator: PDF p. 8 (printed 8), section 3 Electrical Configurations, text.md lines
    144-166
  extracted_at: '2026-09-11'
---

- **Safety key** - fits on the console and activates all functions. With no safety key the console cannot
  be controlled.
- **Console** - the interface that controls all functions of the treadmill; key controls and a **TFT**
  display.
- **Main controller** - the circuit board that carries the AC power supply for the console, the incline
  driver and the AC motor driver, and links the console to output the voltages for the "Incline Interface
  Board and inverter". The general-information line lists power supply, AC motor, incline motor, inverter
  control circuit and incline control circuit.
- **AC motor** - work voltage **AC 220V~**; controls speed increases and decreases.
- **Incline motor** - a **230 volt AC** motor with four wires (red, black, white, green) plus one 3-pin
  position-sensor cable. AC on **red = UP**, AC on **black = DOWN**, **white = COM (neutral)**, **green =
  ground**.

The whole book is a 230-volt book: its circuit diagram is headed "230V", its safety page asks for a
230-volt 15-amp outlet, and its controller-debugging table checks for 220~230V. Its troubleshooting
matrix adds "On 120Vac electronic power system need 110V", so a 120-volt variant exists, but nothing else
in the book describes it.
