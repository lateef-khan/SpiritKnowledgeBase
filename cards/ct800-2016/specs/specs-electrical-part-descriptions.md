---
id: ct800-2016-specs-electrical-part-descriptions
title: What each electrical part does, with a 90 volt DC drive motor and a 120 volt
  incline motor
kind: fact
question: What does each electrical part do on a Spirit ct800-2016 treadmill, and
  what voltages do the motors run on?
asked_as:
- what voltage is the drive motor on the 2016 ct800
- is the ct800 a dc motor treadmill
- incline motor wire colours ct800
- what does the main controller do
keywords:
- electrical configuration
- main controller
- dc motor
- incline motor
- safety key
- console
- voltage
- wire colour
- inverter
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
- ct850-2016-electrical-part-descriptions
- ct850-2020-electrical-part-descriptions
see_also:
- ct800-2016-specs-circuit-diagram
- spirit-ct800-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: PDF p. 11 (printed 10), section 3 Electrical Configurations, text.md lines
    132-165
  extracted_at: '2026-09-11'
---

- **Safety key** - fits on the console and activates all functions. With no safety key the console cannot
  be controlled.
- **Console** - the interface that controls all functions of the treadmill; key controls and an LED display.
- **Main controller** - the circuit board that carries the AC power supply for the console, the incline
  driver and the **DC motor driver**, and links the console to output the voltages for the "Incline
  Interface Board and inverter". The general-information line lists power supply, DC motor, incline motor,
  inverter control circuit and incline control circuit.
- **DC motor** - work voltage **DC 90V~**; increases and decreases speed.
- **Incline motor** - a **120 volt AC** motor with four wires (red, black, white, green) plus one 3-pin
  position-sensor cable. AC on **red = UP**, AC on **black = DOWN**, **white = COM (neutral)**, **green =
  ground**.

**The wording contradicts the drawings.** The main-controller sentence names an "Incline Interface Board
and inverter", but this machine has neither: its circuit diagram and driver-board pages show a single
YJ-2350L control board driving a DC motor through a transformer. The sentence is carried over from the
AC-inverter CT850-2016 book, which prints it word for word.

The CT800-2020 and CT800ENT-2022 print the same section with a **110 volt** incline motor and no DC motor
voltage; the CT850 books describe an AC motor. Do not carry a figure between them.
