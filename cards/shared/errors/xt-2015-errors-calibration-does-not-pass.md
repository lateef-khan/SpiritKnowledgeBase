---
id: xt-2015-errors-calibration-does-not-pass
title: Calibration does not pass, and the speed sensor alignment it points to
kind: troubleshooting
question: What do I check when calibration will not pass on a Spirit XT185-2015, XT285-2015,
  XT385-2015, XT485-2015 or XT685-2015 treadmill?
asked_as:
- calibration keeps failing on my treadmill
- factory settings wont finish calibrating
- treadmill calibration will not complete
- speed sensor not picking up
keywords:
- calibration does not pass
- calibration fails
- speed sensor
- sensor alignment
- front roller pulley
- magnet
- motor cover hood
- speed reads wrong
- rpm signal
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt285-2015
  - xt385-2015
  - xt485-2015
  - xt685-2015
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- f63-2016-e1-error-code
- f65-2023-e1-no-rpm-signal
see_also:
- xt-2023-errors-e1-motor-not-responsive
- xt-2023-maintenance-adjusting-the-speed-sensor
source:
  ref: spirit-treadmill-xt185-2015-owners-manual
  locator: 'ADJUSTING THE SPEED SENSOR, page 30; the same section is page 38 of the
    XT285 2015 manual, page 39 of the XT385, page 44 of the XT485 and page 43 of the
    XT685'
  extracted_at: '2026-09-09'
---

**The manuals give one answer for a calibration that will not pass: check the speed sensor
alignment.** They print no error code for it and no second cause.

> If the calibration does not pass you may need to check the speed sensor alignment.

The alignment check itself is a maintenance procedure and is carded as
`xt-2023-maintenance-adjusting-the-speed-sensor`. In short, as all five 2015 manuals print
it: loosen the 4 screws holding the motor cover hood, find the small black sensor with a
wire on the **left side of the frame next to the front roller pulley**, and set it **as
close as possible to the pulley without touching it**, aligned with the magnet on the face
of the pulley. A screw holds the sensor; loosen it to adjust and re-tighten it afterwards.
**No gap measurement is printed** - only "as close as possible without touching".

**All five 2015 manuals carry this section, including the XT185 and the XT285.** That is a
change from 2023: the 2023 XT185 and XT285 manuals have no speed sensor section at all, so
`xt-2023-maintenance-adjusting-the-speed-sensor` covers only the 2023 XT385, XT485 and
XT685. The 2015 text is otherwise word for word the same.

The other end of this fact is the E1 row of the troubleshooting table
(`xt-2023-errors-e1-motor-not-responsive`): when the belt moves but stops after a short time
and the display shows E1, the manual says run calibration. This card is what to do when that
calibration then fails.

**A Sole E1 is not this fault.** On several Sole treadmills `E1` *is* the no-RPM-signal
code raised during calibration (`f63-2016-e1-error-code`, `f65-2023-e1-no-rpm-signal`).
These Spirit manuals raise no code at all when calibration fails.
