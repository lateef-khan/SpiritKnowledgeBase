---
id: spirit-xt-specs-electrical-part-descriptions
title: What each electrical part does on the DC-drive folding treadmills, with a 0
  to 90 or 0 to 180 volt motor and a 110 or 230 volt incline motor
kind: fact
question: What does each electrical part do on a Spirit XT185, XT285, XT385, XT485
  or XT685 treadmill, and what voltages do the motors run on?
asked_as:
- what voltage is the drive motor on the xt285
- is the xt185 a dc motor treadmill
- incline motor wire colours xt385
- what does the decline motor do on the xt685
keywords:
- electrical configuration
- main controller
- dc motor
- incline motor
- decline motor
- safety key
- console
- voltage
- wire colour
- filter and chock
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2023
  - xt485-2023
  - xt685-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
- spirit-xt-ent-specs-electrical-part-descriptions
- ct800-2016-specs-electrical-part-descriptions
see_also:
- spirit-xt-specs-driver-board-sockets-jk80-jk60-jk90-jk50
- spirit-xt-specs-driver-board-pa-ae00300l-connectors-and-leds
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: spirit-treadmill-xt185-2015-service-manual
  locator: 'XT185-2015: PDF pp. 11-12 (printed 10-11), section 3 Electrical Configurations,
    text.md lines 112-165. XT285-2015: the same pages, lines 118-171. XT185-2023:
    PDF p. 6, lines 86-117; XT285-2023: p. 6, lines 88-119; XT385-2023: p. 6, lines
    100-131; XT485-2023: p. 6, lines 100-131; XT685-2023: p. 6, lines 79-112, which
    adds the Decline Motor rows'
  extracted_at: '2026-09-11'
---

Seven books print the same section; the XT685-2023 adds one part.

- **Safety key** - fits into the console to activate all functions; without it the console cannot be
  controlled and the treadmill will not be activated.
- **Console** - the interface that controls all functions; keys, LCD display, speaker, fan, hand pulse
  grip, safety key.
- **Main controller** - the circuit board with the DC power supply for the console, the incline driver and
  the DC motor driver. The 220 V (or CEGS) lower-controller area also has a **Filter and Chock**.
- **Treadmill / drive motor** - a variable-speed DC motor controlled over **0-90 (or 0-180) volts**. Three
  wires: "red, black and green" in the list, but the wiring lines then say **red into M+, white into M-,
  green is ground** - the book names the second wire both ways. The higher the voltage, the faster the
  motor.
- **Incline motor** - a **110 or 230 volt AC** motor; four wires (red, black, white, green) plus one 3-pin
  position-sensor cable. AC on **red = UP**, AC on **black = DOWN**, **white = COM (neutral)**,
  **green/yellow = ground**.
- **Decline motor (XT685-2023 only)** - "an AC motor. User can control variable elevation by console within
  decline control board", and the incline-motor row is retitled **Incline/Decline Motor** with the same 110
  or 230 volt figure and wire colours. No decline control board appears anywhere else in that book, and
  its circuit diagram draws one incline motor.

The two voltages are alternatives for the 110-volt and 220-volt builds, not a range. The XT385-2015 and
XT485-2015 print the same parts with the figures the other way round ("0-180 DC volts, 0-90 on 120Vac");
the ENT books print an LCD-less "10-inch" or "15.6-inch screen" console and a 120 / 220 volt incline
motor.
