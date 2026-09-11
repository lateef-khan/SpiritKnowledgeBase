---
id: spirit-xt-ent-specs-electrical-part-descriptions
title: What each electrical part does on the touch-screen machines, with a 0 to 90
  volt DC motor and a 120 volt incline motor
kind: fact
question: What does each electrical part do on a Spirit XT485ENT or XT685ENT treadmill,
  and what voltages do the motors run on?
asked_as:
- what voltage is the incline motor on the xt485 ent
- is the xt685ent a dc motor treadmill
- how big is the xt685 ent screen
- incline motor wire colours xt485ent
keywords:
- electrical configuration
- main controller
- dc motor
- incline motor
- safety key
- console
- voltage
- wire colour
- touch screen
- 120 volt
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt485ent-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xt-specs-electrical-part-descriptions
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
see_also:
- spirit-xt-ent-specs-driver-board-connectors
- spirit-xt-ent-specs-console-cable-5-pin-pinout
- spirit-xt-specs-circuit-diagram-codes-and-contents
source:
  ref: spirit-treadmill-xt485ent-2023-service-manual
  locator: 'XT485ENT-2023: PDF pp. 10-11 (printed 10-11), section 3 Electrical Configurations,
    text.md lines 139-187. XT685ENT-2023: PDF p. 5, lines 68-104'
  extracted_at: '2026-09-11'
---

Both books print the same section; only the screen size differs.

- **Safety key** - fits on the console and activates all functions; without it the console cannot be
  controlled.
- **Console** - the interface that controls all functions; key controls and a **10-inch screen** on the
  XT485ENT, a **15.6-inch screen** on the XT685ENT.
- **Main controller** - the circuit board with the DC power supply for the console, the incline driver and
  the DC motor driver.
- **Treadmill motor** - a variable-speed DC motor. The first table says "0-180 DC volts (0-90 on a 120Vac
  system)"; the general-information lines say **"0-90 volt DC motor (0-180 volts on a 220Vac electronic
  power system)"** - the same two builds, named from opposite ends on one page. Three wires; DC on the
  **red (white) wire (M+)** turns it clockwise, DC on the **black wire (M-)** counter-clockwise; green is
  ground.
- **Incline motor** - a **120 volt AC** motor **(220 volts AC on a 220Vac system)**; four wires (red, black,
  white, green) plus one 3-pin position-sensor cable. AC on **red = UP**, AC on **black = DOWN**, **white =
  COM (neutral)**, **green = ground**.

The non-ENT XT books print "110 or 230" for the incline motor and an LCD console; the CT800 books print a
single 110 or 120 volt figure. Use the book for the machine in hand.
