---
id: xt-2023-errors-e1-motor-not-responsive
title: E1 on the display when the motor does not respond after pressing Start
kind: troubleshooting
question: What does E1 mean on a Spirit XT treadmill, 2015 or 2023, when the motor
  is not responsive after pressing Start?
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
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2015
  - xt685-2023
  - xt685ent-2023
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- ct850-2016-motor-not-responsive-after-start
- ct900-e1-over-current
- cvc800-e-1-ram-error
- f65-2026-e01-over-current
- f65-2026-e31-overtemperature
- f63-2016-e1-error-code
- f65-2023-e1-no-rpm-signal
see_also:
- ct900ent-motor-unresponsive-after-start
- xt-2023-maintenance-adjusting-the-speed-sensor
- xt-2023-console-calibration-basic
- xt-2015-errors-calibration-does-not-pass
- spirit-xt-errors-e1-solution-flow-chart
- spirit-xt-errors-e1-check-rpm-sensor-procedure
- spirit-xt-errors-error-code-list-eight-codes
source:
  ref: spirit-treadmill-xt185-2023-owners-manual
  locator: 'page 43, TROUBLESHOOTING - Service Checklist Diagnosis Guide, row "Motor
    is not responsive after pressing start"; the same row is page 51 in the XT285
    manual, page 56 in the XT385 and XT485 manuals and page 55 in the XT685 manual;
    and the identical row is in the Service Checklist Diagnosis Guide on page 31 of
    the XT185 2015 manual, page 39 of the XT285, page 41 of the XT385, page 45 of
    the XT485 and page 46 of the XT685; both ENT manuals print the same table - Service
    Checklist Diagnosis Guide on printed page 54 of the XT485ENT owner''s manual (its
    table of contents lists TROUBLESHOOTING as page 55), text.md lines 1040-1082,
    and on printed page 56 of the XT685ENT owner''s manual, text.md lines 1664-1695;
    service manuals - XT185 2023 service manual 8.2 Error Message: E1, PDF p. 20-23,
    text.md lines 404-475; XT285 2023 service manual 8.2 Error Message: E1, PDF p.
    21-24, text.md lines 406-477; XT385 2023 service manual 8.2 Error Message: E1,
    PDF p. 22-25, text.md lines 373-434; XT485 2023 service manual 8.2 Error Message:
    E1, PDF p. 22-25, text.md lines 373-434; XT685 2023 service manual 8.2 Error Message:
    E1, PDF p. 21-24, text.md lines 411-480; XT185 2015 service manual 8.2 Error Message:
    E1, PDF p. 38-43, text.md lines 620-729; XT285 2015 service manual 8.2 Error Message:
    E1, PDF p. 39-44 (printed 38-43), text.md lines 689-798; XT385 2015 service manual
    8.2 Error Message: E1, PDF p. 39-44, text.md lines 577-666; XT485 2015 service
    manual 8.2 Error Message: E1, PDF p. 39-44, text.md lines 578-666; XT485ENT 2023
    service manual 8.2 Error Message: E1, PDF p. 35-40, text.md lines 492-586; XT685ENT
    2023 service manual 8.2 Error Message: E1, PDF p. 22-27, text.md lines 375-428'
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
alignment (`xt-2015-errors-calibration-does-not-pass`,
`xt-2023-maintenance-adjusting-the-speed-sensor`).

**The 2015 manuals print both branches word for word, and E1 is still the only code they
carry.** All five 2015 owner's manuals (XT185, XT285, XT385, XT485, XT685) were read end to
end for this card: nothing in them names a second error code. The remedy did not change
between 2015 and 2023.

Look-alike codes on other machines answer to something else entirely: `E1` on a Spirit CT900
is an inverter over-current, `E-1` on a Spirit CVC800 is a display board RAM error, and the
Sole 2026 treadmills use `E01` (over current) and `E31` (over temperature). A Spirit CT900ENT
prints no code at all for this row - it says reset the power, then contact service
(`ct900ent-motor-unresponsive-after-start`).

**The XT485ENT and XT685ENT print both branches word for word, and E1 is still the only code
either of them carries.** Both ENT owner's manuals were read end to end for this card:
nothing in either names a second error code.

**Neither ENT manual prints the calibration procedure this row tells you to run.** The word
*calibration* appears exactly once in the XT485ENT owner's manual and exactly once in the
XT685ENT owner's manual - in this troubleshooting row, and nowhere else. Neither document has
a Calibration Procedure section, and neither has a speed-sensor adjustment section. A reader
of either manual is told to run calibration and is not told how. The base XT 2015 and 2023
manuals do print the procedure (`xt-2023-console-calibration-basic`), so answer an ENT owner
from those rather than from the manual in their hands, and say that is where it comes from.

**The XT685 did not always print E1 in this row.** The XT685 **2010** owner's manual prints
the identical condition and the identical two branches with **`LS`** in place of `E1`
(Service Checklist - Diagnosis Guide, printed page 31), which is the code the CT800 and CT850
manuals use (`ct850-2016-motor-not-responsive-after-start`). The 2010 machine is on that card,
not this one. The symptom, the split by whether the belt moved and both remedies are the same
in all three revisions - only the code string changed between 2010 and 2015. Do not answer a
2010 XT685 with `E1`.

**Service manual remedy.** All eleven XT service manuals in the repository - the 2015 XT185, XT285, XT385 and XT485, the 2023 XT185, XT285, XT385, XT485 and XT685, and the XT485ENT and XT685ENT - define E1 the same way: *Display board CPU did not receive the RPM signal. (Only happen in the Calibration. In generally, it does not necessary speed RPM sensor, but when the Calibration which it is a necessary.)* The cause: *The motor doesn't turn then E1 appears. The drive board did not sent voltage to the motor, so the motor did not operate. And the display board did not receive the RPM sensor signal.* The speed signal travels over the TX/RX lines of the 6-pin main wire (5-pin on the two ENT consoles).

The troubleshooting form, headed `The motor cannot move`:

| Possible cause | Things to check | Solution |
|---|---|---|
| The upper console board hasn't received any speed signal for 8 seconds | Check the speed sensor cable is in good connection | Make sure the good connection for cables |
| The speed sensor didn't detect signal completely | Check the gap between speed sensor and magnet | To keep the gap-distance less than 3 mm |
| Defective sensor or bad cable connection | Check if the sensor and cables are circuit short damaged | Change the sensor or cables |

The **8 second** timeout and the **3 mm** gap are the only two figures printed. The step-by-step flow chart is on `spirit-xt-errors-e1-solution-flow-chart`, and the sensor check it branches to is on `spirit-xt-errors-e1-check-rpm-sensor-procedure`.

**The XT285 2015 service manual contradicts itself about the code.** Its own checklist row prints *display shows "LS1/LOW SPEED", run calibration (See section 8.2 on Error Message: LS1/LOW SPEED)*, while its section 8.2 is E1 and no LS1 message exists anywhere in that book. `LS1/LOW SPEED` is the CT800 and CT850 code pasted in; the XT285 shows E1.
