---
id: spirit-med-stepper-errors-one-pedal-has-no-resistance-drive-cable
title: One pedal with no resistance while the other has it means the drive cable has
  jumped off the pulley system
kind: troubleshooting
question: Why does one pedal on a Spirit recumbent stepper have no resistance while
  the other one does?
asked_as:
- one pedal on my stepper feels loose
- left pedal has no resistance on my spirit stepper
- one side of the stepper is dead
- stepper pedal goes down with no effort
keywords:
- one pedal
- no resistance
- drive cable
- pulley
- jumped off
- uneven resistance
- one side
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
see_also:
- spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode
- spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: 'Troubleshooting, "One pedal has no resistance but the other does", printed
    page 40 (PDF page 42) of the 7.0S 2025 manual; the same text on printed page 42 (PDF
    page 44) of the 7.5S 2025 manual and printed page 60 (PDF page 60) of the MS300 2021
    manual, where the bullet is empty in the text layer and was recovered from a 300 dpi
    render.'
  extracted_at: '2026-09-10'
---

The whole of what the manual prints:

> One pedal has no resistance but the other does
> - The drive cable has jumped off of the pulley system.

**One cause, stated flatly, with no test and no remedy.** The manual does not say how to get the
cable back on, whether the shrouds have to come off, or whether it is a service job.

**It is a cable-and-pulley machine, not two independent resistance units.** Both pedals are driven
from one resistance unit through a cable, which is why losing the cable on one side leaves the other
side feeling normal - and why the fault is mechanical rather than an error message. The console will
report nothing.

**This is not `Motor Error`.** A resistance motor that did not respond takes resistance changes away
from **both** pedals and puts a message on the screen
(`spirit-med-stepper-errors-motor-error-press-stop-for-idle-mode`). One pedal soft and one pedal
normal is the cable.

**Expect the Symmetry Index to be wrong at the same time**, since the machine is measuring two sides
that are genuinely no longer doing the same work
(`spirit-med-stepper-errors-symmetry-or-watt-reading-wrong`). Fix the cable before reading anything
into the symmetry figure.

**On the MS300 2021 this bullet is empty in the text layer.** `pdftotext` returns the heading and a
bare bullet with nothing after it, which reads as though the manual names no cause. The printed page
carries the sentence; it was read from a 300 dpi render of PDF page 60.
