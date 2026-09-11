---
id: spirit-ce800-xe795-specs-generator-flywheel-power-and-resistance-voltage-leads
title: 'Two leads off the generator flywheel: a three-wire generator power lead from
  the stator and a two-wire generator resistance voltage lead from the coil pack'
kind: spec
question: What are the two wires coming off the generator flywheel on a Spirit CE800
  or XE795 elliptical?
asked_as:
- what wires come off the flywheel on the ce800
- generator resistance voltage wire elliptical
- which flywheel lead is the brake on the xe795
- chi hua flywheel label ce800
keywords:
- generator flywheel
- generator power
- generator resistance voltage
- brake coil
- stator
- three wire
- red white black
- chi hua
- induction brake
- hybrid generator
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce800-2016
  - ce800-2021
  - xe795-2016
  - xe795-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ce800ent-flywheel-and-induction-brake
- ce800-2021-specs-generator-controller-connections
- spirit-ce800-2016-xe795-2016-specs-generator-controller-031101b-connections
- xe795-2023-specs-generator-controller-cs52005-23-connections
- xe795-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v
source:
  ref: spirit-elliptical-ce800-2021-service-manual
  locator: 'CE800-2021: 6-1-5 GENERATOR FLYWHEEL DEFINITION FUNCTION, PDF p. 23 (printed
    22), text.md lines 334-340 (OCR supplement lines 1017-1029). CE800-2016: GENERATOR
    Flywheet definition function, PDF p. 27, lines 474-492 (OCR supplement 1235-1247).
    XE795-2023: 6.5 Driver Board function, third photograph, PDF p. 13, lines 221-227
    (OCR supplement 878-908). XE795-2016: circuit diagram, PDF p. 42, lines 609-616,
    the WHITE, BLACK, RED and RED leads'
  extracted_at: '2026-09-11'
---

Three books photograph the flywheel from the side with the same two call-outs:

- **GENERATOR POWER** - the plug at the edge of the copper stator winding, a **three-wire lead**
  (red, white and black on the circuit diagrams).
- **GENERATOR RESISTANCE VOLTAGE** - the **two-wire lead** (red on the diagrams) leaving the coil
  pack bolted to the bracket at the edge of the flywheel.

Changing resistance means changing the voltage on the second lead; the controller drives it. The
first lead is what powers the console - none of these four machines has an adapter or a mains
cord.

The bracket carries a **CHI HUA** label reading **K500022** on the CE800-2021 and XE795-2023
photographs (the CE800ENT's reads K500054, `ce800ent-flywheel-and-induction-brake`). The XE795-2016
prints no flywheel photograph; its circuit diagram draws the same two leads off the generator.

**No coil resistance, no generator output and no level table is printed for the unit** in any of
the four books. The only figure anywhere near it is the XE795-2016's brake working voltage,
DC 0.4 to 14 V (`xe795-2016-specs-hybrid-generator-brake-working-voltage-dc-0-4-to-14-v`).

