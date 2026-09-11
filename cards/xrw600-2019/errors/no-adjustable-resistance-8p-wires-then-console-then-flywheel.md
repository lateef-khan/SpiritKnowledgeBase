---
id: xrw600-2019-errors-no-adjustable-resistance-8p-wires-then-console-then-flywheel
title: No adjustable resistance on the wired-handle rower is worked through the 8-pin
  console wires, the gear motor cables, then the steel cable and flywheel
kind: troubleshooting
question: What do I check when the resistance will not adjust on a Spirit xrw600-2019
  rower?
asked_as:
- xrw600 resistance wont change
- spirit rower level up and down do nothing
- xrw600 stuck at one resistance level
keywords:
- no adjustable resistance
- 8p wires
- console control board
- gear motor
- steel cable
- flywheel
- computer cable
- drive belt
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: xrw600-2019
  applies_to:
  - xrw600-2019
  section: errors
  code: no-code
  model_number:
  - '600976'
authority: 3
not_to_be_confused_with:
- spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel
see_also:
- spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel
- crw800-2024-errors-e2-cable-tension-communication-error
- sr500-2016-no-adjustable-resistance
source:
  ref: spirit-rower-xrw600-2019-service-manual
  locator: 9-12 No Adjustable Resistance, PDF p. 65-66; text.md lines 755-778
  extracted_at: '2026-09-11'
---

**The XRW600 has no radio handlebar controller, so its version of this page has no RF module and no controller battery.** The CRW800 books put an RF calibration and a battery check first (`spirit-crw800-errors-no-adjustable-resistance-controller-and-rf-module-then-console-then-flywheel`); this book starts at the console's 8-pin wires.

The page opens with the CRW800 wording - *check Controller Assembly (36) and Console Assembly (43) separately; controller, see step 1; console, see step 3* - and then prints steps that do not match that sentence. Read the steps, not the preamble:

**First:** use an 8 mm hex key to loosen the 3/8" x 3-3/4" socket head cap bolt (83), take off the console (43), and check that the **8P wires (44)** are connecting well with the control board of the console (43).

**1.** Release the four 3.5 x 12L sheet metal screws (112) from the Console (43). Check the PCB board (43~4) and the 500 mm Computer Cable (Upper). Release the Chain Cover (R) (72) and check the Gear Motor (35) and the 500 mm Computer Cable (Lower) (45).

**2.** Release the Chain Cover (R) (72) and check the Drive Belt (24) and Flywheel (23). Check the connections with Gear Motor (35), Steel Cable (66) and Flywheel (23). The problems could be:

- **Gear Motor (35)** - check whether there is any noise while working. If yes, get the Steel Cable (66) to the maximum. If not, replace Gear Motor (35) directly.
- **Flywheel (23)** - check if the Steel Cable is broken or the Flywheel gets stuck.

**The preamble is copied from the CRW800 book** - it refers to a step 3 that this page does not have and to a Controller Assembly (36) the XRW600 does not use for resistance. That is a copy-and-paste defect in the source, not a missing page.

The electrical half of this fault is the `E2` code and its voltage test (`crw800-2024-errors-e2-cable-tension-communication-error`, `spirit-crw800-errors-cable-tensioner-voltage-test-5-5-to-6-5-vdc-then-the-power-adapter`).
