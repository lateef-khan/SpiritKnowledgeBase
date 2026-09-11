---
id: spirit-cr800ent-cu800ent-specs-electrical-configuration-induction-brake
title: Console, main controller and a resistance unit the text calls a generator flywheel
  but the photos call an induction brake, plus an incline-motor paragraph copied from
  a treadmill
kind: fact
question: What electrical parts does the service manual name on a Spirit CR800ENT
  or CU800ENT bike, and what does each do?
asked_as:
- what is the induction break on the cu800 ent
- does the cr800ent have an incline motor
- what electronic parts are in the cu800ent
- what is the pcb and power converter on the cr800 ent
keywords:
- electrical configuration
- induction brake
- induction break
- generator flywheel
- incline motor
- main controller
- tft lcd touch panel
- earphone port
- thumb switch
- pcb & power converter
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800ent-2023
  - cu800ent-2022
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-cr800-cu800-2021-specs-electrical-configuration-generator-flywheel
see_also:
- spirit-cr800ent-cu800ent-specs-unit-block-diagram
- spirit-cr800ent-cu800ent-specs-driver-board-connections
- spirit-bike-specs-generator-brake-or-induction-brake
- spirit-xt-ent-specs-electrical-part-descriptions
source:
  ref: spirit-bike-cu800ent-2022-service-manual
  locator: 'CU800ENT: section 3 Electrical Configurations, PDF p. 10 (printed 10),
    text.md lines 124-144; section 2 Electronic Parts, PDF pp. 7-8, lines 82-116.
    CR800ENT: PDF p. 10, lines 131-151; PDF pp. 7-8, lines 89-123. Identical wording'
  extracted_at: '2026-09-11'
---

**Section 3 names four parts**, and the fourth does not exist on a bike:

- **CONSOLE** - controls all functions of the Bike; key controls and a **TFT LCD touch panel**.
- **MAIN CONTROLLER** - the power supply for the console, linking the console "to output
  appropriate voltages for braking resistance".
- **GENERATOR FLYWHEEL** - increases or decreases the resistance level of the brake.
- **INCLINE MOTOR** - "This is an AC motor. User can to control variable elevation by console
  within main controller." **Copied from a treadmill book.** Neither bike has an incline motor,
  and no other page of either book mentions one.

**The chapter-2 photographs name the real parts** (`spirit-cr800ent-cu800ent-specs-parts-electronic-parts-named`):
the brake on the flywheel is captioned **Induction Break** (spelt so), and the lower page adds a
**PCB & Power Converter** - the power-bridge board with its converter, photographed on p. 20.

**So the text's "generator flywheel" is the photos' "induction brake".** These bikes plug into the
wall: the controller takes AC L / AC N and drives a brake coil; nothing here generates. The
owner's-manual parts lists agree and name an *Induction Brake* with an *EMS Controller* - see
`spirit-bike-specs-generator-brake-or-induction-brake`. No voltage is printed for the brake.

The treadmill ENT books print the same four-part text with the incline motor in its right place:
`spirit-xt-ent-specs-electrical-part-descriptions`.

