---
id: spirit-ce-2024-specs-brake-and-resistance-unit
title: Three resistance units across the three commercial ellipticals - a generator
  brake, a gear motor and an EMS controller
kind: spec
question: What kind of resistance or brake does a Spirit commercial elliptical trainer
  of the 2024 range use, and does it generate its own power?
asked_as:
- how does the resistance work on the spirit elliptical
- is the commercial elliptical magnetic
- does the elliptical make its own power or plug in
- what is the brake part on the ce800
keywords:
- resistance
- brake
- generator
- magnetic
- gear motor
- ems controller
- flywheel
- brake coil
- power adaptor
- eddy current
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce800-2024
  - ce800ent-2024
  - ce850-2024
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-residential-bike-specs-gear-motor-or-generator-brake
- spirit-climber-2024-specs-resistance-system
see_also:
- spirit-ce-specs-no-specification-table
- ce800-2024-specs-parts-list
- ce850-2024-specs-parts-list
- ce800ent-2024-specs-parts-list
- ce800ent-flywheel-and-induction-brake
- spirit-ce-specs-forty-resistance-levels
source:
  ref: spirit-elliptical-ce800-2024-owners-manual
  locator: Parts List printed pp. 40-41 (PDF pp. 42-43), items 29, 30-14, 30-16, 31
    and 32; also CE850-2024 Parts List printed pp. 41-43, items 48, 49, 50, 56, 59,
    64, 65, 66 and 73; CE800ENT-2024 Parts List printed pp. 53-54, items 29, 30, 33,
    43, 44, 45 and 47
  extracted_at: '2026-09-10'
---

**None of the three manuals states a resistance rating in watts, newtons or
kilograms, and none uses the word *magnetic*.** What they do tell you is which
resistance unit is fitted, and it is a different one on each of the three
machines. The parts lists name it.

| Machine | What sets the resistance | Where its power comes from |
|---|---|---|
| **CE800-2024** | `Flywheel` (item 29) with a `Generator/Brake Controller` (31), a `Magnet(Ø15×7T)` (32), a generator wire harness (30-14) and a 1000 mm wire brake coil harness (30-16) | **built-in generator - no outlet needed** |
| **CE850-2024** | `Flywheel` (49) and `Magnet` (50), driven by a **`Gear Motor` (56)**, with an `Adaptor` (65) and two `Resistance Button W/Cable` (66); a separate `Incline Motor` (73) and `Incline Controller` (64) run the ramp | `Power Cord` (59) into a **110-volt, 5-amp** outlet |
| **CE800ENT-2024** | `Flywheel` (29), `Magnet` (30) and a 900 mm wire brake coil harness (33), driven by an **`EMS Controller` (44)** | `Power Adaptor` (45), `Power Cord` (43) and `AC Electronic Module` (47) into a **120-volt AC, 15-amp** outlet |

## The three do not share a brake, and two of them name no brake unit at all

- **The CE800-2024 brakes against the same generator that powers its console.**
  Its console chapter says the machine has "a built-in generator for power and
  do[es] not need to be plugged into an AC outlet. To power up the elliptical
  trainer simply start to [pedal]", and its troubleshooting page names a
  "Generator brake resistance voltage wire". Asking for its brake controller gets
  item 31.
- **The CE850-2024 is not generator-braked.** It has a mains cord, a gear motor
  that positions a magnet, and a second motor for the powered ramp. There is no
  `Generator/Brake` row anywhere in its 208-row list.
- **The CE800ENT-2024 names no brake unit.** It has an EMS controller and a brake
  coil harness and a flywheel and a magnet, but **no `Induction Brake` row** of
  the kind the CR800ENT-2024 and CU800ENT bikes carry at item 55 and item 20.
  Describe it as an EMS-controlled magnetic brake and say the parts list names no
  single brake part.

**None of the three lists a brake as one orderable item except the CE800's
controller.** On all three, the coil, the magnet and the flywheel are separate
rows.

## What the service manual already said about the ENT machine

`ce800ent-flywheel-and-induction-brake` records the CE800ENT **service** manual's
account of the same flywheel, brake and resistance voltage wire, and gives no
figures either. That card is written from the service manual for the earlier
CE800ENT; this one is written from the October 2024 owner's manual parts list.
They agree, and neither supplies a rating.

## Where the power supply itself is answered

Whether the machine needs an outlet, and at what voltage and amperage, is a
safety question and lives in the `safety` section. Two things are worth knowing
before you look:

- **The CE800ENT-2024 asks for 120 volts and 15 amps.** Earlier ENT ellipticals
  and the CE850 books ask for **110 volts and 5 amps**. Same family, a different
  requirement, so read the book for the machine in front of you.
- **Only the plain CE800 needs no outlet at all.**

## No resistance figure is printed anywhere

Level 1 to 40 on the CE800 and 1 to 20 on the CE850 are console scales, not
physical ratings - see `spirit-ce-specs-forty-resistance-levels` and
`spirit-ce850-specs-twenty-resistance-levels`. **The CE800ENT-2024 owner's manual
states no level count at all.** No Spirit elliptical manual prints a
level-to-watts table.

**Do not answer an elliptical from a bike card.** The commercial bikes' generator
and induction brakes are different units in different machines - see
`spirit-bike-specs-generator-brake-or-induction-brake`.
