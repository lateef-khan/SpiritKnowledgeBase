---
id: xt-2015-errors-calibration-does-not-pass
title: Calibration does not pass, and the speed sensor alignment it points to
kind: troubleshooting
question: What do I check when calibration will not pass on a Spirit CT800, CT800ENT,
  CT850 or XT treadmill?
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
  - ct800-2012
  - ct800-2016
  - ct800-2020
  - ct800ent-2022
  - ct850-2018
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
- spirit-ct800-maintenance-speed-sensor-alignment
- ct850-2016-motor-not-responsive-after-start
source:
  ref: spirit-treadmill-xt185-2015-owners-manual
  locator: 'ADJUSTING THE SPEED SENSOR, page 30; the same section is page 38 of the
    XT285 2015 manual, page 39 of the XT385, page 44 of the XT485 and page 43 of the
    XT685; all four CT800 owner''s manuals print the same sentence under Adjusting The Speed Sensor - printed page 24 of the 2012 manual (text.md lines 1053-1054), printed page 36 of the 2016 manual (text.md lines 938-939), printed page 38 of the 2020 manual (text.md lines 976-977) and printed page 51 of the CT800ENT 2022 manual (text.md lines 1154-1155); the CT850 2018 owner''s manual prints the same sentence under ADJUSTING THE SPEED SENSOR on printed page 40 (text.md lines 1020-1021)'
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

**All four CT800 generations print the same one-line answer**, word for word, with no error
code and no second cause. The **alignment check itself differs from the XT one**, so do not
carry the XT figures onto a CT800: the CT800 manuals have the reader loosen **8** motor-hood
screws rather than 4, describe **two** screws holding the sensor rather than one, and ask for
the sensor to be aligned with the **centre of the magnet as it passes** rather than set "as
close as possible to the pulley without touching it". The alignment procedure is a
maintenance fact and belongs on a maintenance card, not here.

**Of the four CT850 owner's manuals only the 2018 prints this sentence.** It carries the whole
Adjusting The Speed Sensor section and words the sentence exactly as the CT800 manuals do. The
CT850 2016, CT850 2020 and CT850ENT 2022 owner's manuals print a calibration procedure but no
speed sensor section and no statement of what to do when calibration fails - that is those
documents being silent, not those machines behaving differently. The CT850 2018 alignment check
matches the CT800 one - 8 motor-hood screws, two screws on the sensor, aligned with the centre of
the magnet - and is carded with them as `spirit-ct800-maintenance-speed-sensor-alignment`.

**The CT800ENT 2022 manual points at a calibration it never prints.** It carries this
sentence and the whole Adjusting The Speed Sensor section, but the manual has no calibration
procedure and no engineering mode section anywhere - so a CT800ENT owner told to run
calibration has nothing in the book telling them how. The 2012, 2016 and 2020 CT800 manuals
all print a calibration procedure.

**A Sole E1 is not this fault.** On several Sole treadmills `E1` *is* the no-RPM-signal
code raised during calibration (`f63-2016-e1-error-code`, `f65-2023-e1-no-rpm-signal`).
These Spirit manuals raise no code at all when calibration fails.
