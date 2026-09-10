---
id: spirit-med-stepper-errors-symmetry-or-watt-reading-wrong
title: A wrong Symmetry Index or watt reading gets one line of troubleshooting and
  no tolerance figure
kind: troubleshooting
question: What does a Spirit recumbent stepper manual say to do when the symmetry or
  watt measurement is incorrect?
asked_as:
- symmetry index looks wrong on my stepper
- watts reading is wrong on the spirit stepper
- left and right numbers dont match on my stepper
- how do i calibrate the watts on a stepper
keywords:
- symmetry index
- watts
- left and right
- incorrect reading
- sensor test
- maintenance mode
- no tolerance
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
see_also:
- spirit-med-stepper-errors-no-data-when-pedaled-sensor-test
- spirit-med-stepper-errors-one-pedal-has-no-resistance-drive-cable
source:
  ref: spirit-climber-70s-2025-owners-manual
  locator: 'Troubleshooting, "Symmetry and/or watt measurement is incorrect", printed
    page 40 (PDF page 42) of the 7.0S 2025 manual; the same text on printed page 42 (PDF
    page 44) of the 7.5S 2025 manual and printed page 60 (PDF page 60) of the MS300 2021
    manual. Read from the native text layer and confirmed against a 300 dpi render of
    the 7.0S page.'
  extracted_at: '2026-09-10'
---

The whole of what the manual prints:

> Symmetry and/or watt measurement is incorrect
> - Perform the sensor tests in Maintenance Mode

**One line, and it is the same test the "no data registers" row sends you to** - the Sensor Test
under Maintenance mode, reading the two reflector sensors and the two step position counters. A
Symmetry Index is a left-against-right comparison, so a sensor reading badly on one side skews it
without stopping the machine.

**No tolerance is printed, and no calibration procedure exists.** The manual never says how far out a
Symmetry Index has to be before it counts as incorrect, gives no expected watt figure to check
against, and offers nothing to adjust if the sensor test passes. There is no "calibrate the watts"
step on these machines to be found.

**These consoles report watts left and right separately**, and the specification page rates the work
load from 5 watts up to 1000 watts on the 7.0S and 7.5S and 5 watts up to 650 watts on the MS300 -
so an out-of-range reading is worth checking against the machine's own ceiling before calling it a
fault.

If no numbers appear at all, that is the row above:
`spirit-med-stepper-errors-no-data-when-pedaled-sensor-test`.
