---
id: xt-2023-errors-e1-motor-not-responsive
title: E1 on the display when the motor does not respond after pressing Start
kind: troubleshooting
question: What does E1 mean on a Spirit XT 2023 treadmill when the motor is not responsive
  after pressing Start?
asked_as:
- my treadmill shows e1 and stops after a few seconds
- press start and the belt never moves it just says e1
- what is error e1 on my spirit treadmill
keywords:
- e1
- motor not responsive
- belt stops after a short time
- start button
- calibration
- speed signal
- error code
- contact service
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2023
  - xt285-2023
  - xt385-2023
  - xt485-2023
  - xt685-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- ct900-e1-over-current
- cvc800-e-1-ram-error
- f65-2026-e01-over-current
- f65-2026-e31-overtemperature
see_also:
- ct900ent-motor-unresponsive-after-start
- xt-2023-maintenance-adjusting-the-speed-sensor
- xt-2023-console-calibration-basic
source:
  ref: spirit-treadmill-xt185-2023-owners-manual
  locator: page 43, TROUBLESHOOTING - Service Checklist Diagnosis Guide, row "Motor
    is not responsive after pressing start"; the same row is page 51 in the XT285
    manual, page 56 in the XT385 and XT485 manuals and page 55 in the XT685 manual
  extracted_at: '2026-09-09'
---

**This is E1, not E01 and not E31.** E1 on these treadmills is the one code the owner's
manuals print, and which branch you are in depends on whether the belt moved at all.

The condition is printed as *Motor is not responsive after pressing start*, with two answers:

1. **The belt moves, but stops after a short time and the display shows "E1"** - run
   calibration. The Calibration Procedure is printed in the Belt and Deck Cleaning &
   Calibration Procedure section of the same manual.
2. **You press Start and the belt never moves, then the display shows E1** - contact
   service.

If the calibration does not pass, the manuals send the reader on to the speed sensor
alignment (`xt-2023-maintenance-adjusting-the-speed-sensor`).

Look-alike codes on other machines answer to something else entirely: `E1` on a Spirit CT900
is an inverter over-current, `E-1` on a Spirit CVC800 is a display board RAM error, and the
Sole 2026 treadmills use `E01` (over current) and `E31` (over temperature). A Spirit CT900ENT
prints no code at all for this row - it says reset the power, then contact service
(`ct900ent-motor-unresponsive-after-start`).
