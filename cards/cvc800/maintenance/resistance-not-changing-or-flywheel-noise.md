---
id: cvc800-resistance-not-changing-or-flywheel-noise
title: Resistance will not change, or the flywheel makes a noise
kind: troubleshooting
question: Why will the resistance not change, or the flywheel make a noise, on a Spirit
  cvc800 climber?
asked_as:
- resistance level does not do anything on the climber
- noise coming from the flywheel
- steel cable came off the flywheel
keywords:
- resistance not functional
- steel cable
- flywheel
- drive pulley
- idle wheel assembly
- friction
- gear motor
facets:
  brand:
  - spirit
  product_line: climber
  model: cvc800
  applies_to:
  - cvc800
  section: maintenance
  code: '*'
  model_number:
  - '800440'
authority: 3
not_to_be_confused_with:
- cvc800-e-2-tension-motor-error
- cvc800-tension-motor-voltage-test
see_also:
- cvc800-noise-troubleshooting
- cvc800-drive-belt-drops-off
source:
  ref: spirit-climber-cvc800-service-manual
  locator: Section 10-3 Troubleshooting for Flywheel and Drive belt, p. 49 (printed
    49)
  extracted_at: '2026-09-08'
---

The manual gives these two symptoms one heading: "Adjust the resistance level but it is not
functional or some noise comes from Flywheel."

1. **If the gear motor is operating normally**, check that the **steel cable is mounted on the
   flywheel in the right way.**
2. **If there is noise when the flywheel is spinning**, check whether the **flywheel, drive pulley
   and idle wheel assembly are rubbing against each other** and causing the noise, or whether the
   **flywheel makes the noise itself.**

## Rule out the tension motor first

Step 1 begins "If Gear motor is operating normally" — that is a precondition, not a check. If the
resistance is dead rather than merely wrong, the fault may be electronic: this machine reports a
tension motor fault as **E-2** (`cvc800-e-2-tension-motor-error`), and there is a voltage test for
the motor (`cvc800-tension-motor-voltage-test`). This card is the mechanical half, for when the
motor is proven good.

For other noises see `cvc800-noise-troubleshooting`.
