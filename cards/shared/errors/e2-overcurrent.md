---
id: sole-e2-error
title: 'E2 error: motor overcurrent'
kind: troubleshooting
question: What does an E2 error mean on a Sole treadmill?
asked_as:
- e2 error on my treadmill
- treadmill keeps showing e2
keywords:
- e2
- e2 error
- overcurrent
- overload
- motor controller
- lubrication
facets:
  brand:
  - sole
  product_line: treadmill
  model: '*'
  applies_to:
  - f63
  - f63-2013
  - f65
  - f65-2026
  - f80
  - f80-2026
  - f83
  - f83-2026
  - f85
  - f85-2020
  - f85-2026
  - f89
  - tt8
  - tt8-2020
  section: errors
  code: e2
authority: 2
not_to_be_confused_with:
- sole-e3-error
see_also:
- sole-lubricate-running-belt
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-e2-error-treadmill
  locator: whole document
  extracted_at: '2026-09-03'
---

**This is E2 on a 2016 or newer machine. On a machine built before 2016 this same fault shows as E3, and the E3 card covers it.**

**Meaning**: the machine sees the controller drawing too much power to bring the motor up to speed. The usual cause is friction between the belt and the deck, or a damaged motor controller.

If the error appeared after the machine was assembled, replace the computer cables first.

Before you fit a new motor controller, look for the wear that kills controllers:

1. Ask how often the customer lubricates. Whether the answer is good or bad, check the running belt and running deck for wear. Slide a hand between the belt and the deck, palm up, and feel whether the texture in the middle is gone. Turn the palm down and feel the deck for damage.
   - Belt and deck good: go to step 2.
   - Belt or deck worn or damaged: replace the running belt, the running deck and the controller. Replace the deck only if it is worn or damaged.
2. Ask whether the machine is plugged straight into its own circuit on a non-GFCI outlet.
   - Yes: go to step 3.
   - No: have the customer move it to its own non-GFCI circuit and try again. If it runs, it is fixed. If it does not run, replace the motor controller.
3. Ask whether there are squeaking or knocking noises.
   - Yes: ask whether the noise is at the front or the rear, and replace the front roller or the rear roller (possibly both) together with the motor controller.
   - No: replace the motor controller.

**Scope.** This card is the fallback for the Sole treadmills that have no service manual in this knowledge base. Every machine listed in `applies_to` is one of those. A machine with a service manual has its own card for this code, or its manual shows the code does not exist on it — check the model's own cards first. AC inverter machines (ST90, TT9, the AC TT8 variants), the F63 2026 and the C80 use different code families and are deliberately excluded.
