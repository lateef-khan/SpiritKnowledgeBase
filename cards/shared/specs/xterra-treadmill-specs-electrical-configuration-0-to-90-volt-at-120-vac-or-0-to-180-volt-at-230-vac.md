---
id: xterra-treadmill-specs-electrical-configuration-0-to-90-volt-at-120-vac-or-0-to-180-volt-at-230-vac
title: 'What each electrical part does, with both builds side by side: a 0 to 90 volt
  DC motor on 120 VAC or 0 to 180 volt on 230 VAC, and an incline motor of 120 or
  220 to 230 volts'
kind: fact
question: What does the electrical configuration chapter of the Xterra treadmill service
  manual say about the drive motor, incline motor, controller and console, on the
  books that print both the 120 VAC and 230 VAC figures?
asked_as:
- tr260 motor voltage
- trx5500 incline motor voltage
- what does the trx5500 main controller do
- tr260 incline motor wires red up black down
keywords:
- electrical configuration
- dc motor
- 0 to 90 volt
- 120 vac
- 230 vac
- incline motor
- wire colour
- tft display
- touch screen
- main controller
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr260-2023
  - trx5500-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-trx-specs-electrical-configuration-printed-for-230-vac-with-a-220-volt-incline-motor
- tr150-2021-specs-electrical-configuration-dc-motor-0-to-90-volt-and-no-incline-motor
see_also:
- spirit-xt-2015-specs-electrical-part-descriptions-0-to-180-volt
- tr260-2023-specs-driver-board-b407d-sockets-acn-acl-to-m-plus
- trx5500-2024-specs-driver-board-wire-connections-120-vac-in
- xterra-treadmill-specs-incline-position-sensor-red-ground-white-signal-black-5-volts
source:
  ref: xterra-treadmill-trx5500-2024-service-manual
  locator: TRX5500 SM (GT90D-NT041) '3. Electrical Configurations', PDF p. 11 (printed
    10), lines 148-183, and NOTICE BEFORE OPERATION PDF p. 12, lines 183-193. TR260
    SM (GT75A-NT050) '3. Electrical Configurations', PDF p. 9 (printed 9), lines 104-138
  extracted_at: '2026-09-11'
---

**These two books print the 120 VAC and 230 VAC figures together**, unlike the TRX2500/3500/4500 books, which print
only the 230 VAC ones. The common text:

- **Safety key** - fits on the console and activates all functions; without it the console cannot be controlled.
- **Console** - the interface that controls all functions of the treadmill.
- **Main controller** - the DC power supply for the console, the incline driver and the DC motor driver (the TR260
  book says "AC power supply for console ... for DC control Board"); includes power supply, motor driver control
  circuit and incline control circuit.
- **Treadmill motor** - "a variable speed for DC motor. To control the **0-90 (120VAC) or 0 – 180 (230VAC)** voltages
  on the main controller". Three wires, red, black and green: DC on the red (white) wire, M+, turns it clockwise; DC
  on the black wire, M-, turns it counter-clockwise; the higher the voltage the faster it turns; green is ground.
- **Incline motor** - a **120 volt (230 volt)** AC motor in the TRX5500 book, a **220 (120) volt** AC motor in the
  TR260 book. Four wires, red, black, white and green, plus one 3-pin cable for the position sensor. AC on the **red**
  wire (UP) raises the incline, AC on the **black** wire (DOWN) lowers it, **white** (COM) is neutral, green/yellow is
  ground.

Where the two books differ:

| Item | TR260 book | TRX5500 book |
|---|---|---|
| Console description | "Key controls and TFT Display" | "button control and 10-inch touch screen display" |
| Motor sentence | "It's a variable speed on 0-90 volt DC motor for 120V and 0-180 volt DC motor for 230V" | "DC motor with variable speed range 0-90 or (0-180) volt" |
| Incline motor | "220 (120) volt AC motor" | "120 volt (230 volt) AC motor" |
| Notice before operation | mentions "emergency switches both on left and right side" as well as the safety key - text carried over from another machine; the TR260 has no such switches | "check the emergency switch is inserted right position and the clip is on your cloth" |

The TR260's "TFT Display" is itself at odds with its chapter 2, which captions the console "LCD Display". The US
machines are the 120 VAC build, so the drive motor is the 0-90 V range and the incline motor the 120 V one. No
horsepower or current is printed in either book.
