---
id: ct850-2016-motor-not-responsive-after-start
title: The motor does not respond after START is pressed and the display shows LS
kind: troubleshooting
question: What does it mean when the motor does not respond after START on a Spirit CT800,
  CT800ENT or CT850 treadmill?
asked_as:
- motor not responding after i press start
- belt moves then stops and shows ls
- spirit treadmill motor unresponsive
keywords:
- motor unresponsive
- ls
- low speed
- calibration
- belt stops
- contact service
- start button
- run calibration
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
  - ct850-2016
  - ct850-2018
  - ct850-2020
  - ct850ent-2022
  section: errors
  code: low-speed
authority: 3
not_to_be_confused_with:
- ct850-2020-motor-not-responsive-after-start
- ct900ent-motor-unresponsive-after-start
- xt-2023-errors-e1-motor-not-responsive
- sole-ls-error
see_also:
- ct850-2016-low-speed-error-message
- ct850-2020-motor-not-responsive-after-start
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Section 9.2 Service Troubleshooting Checklist - Diagnosis Guide, pages
    56-57 (printed 55-56); all four CT800 owner's manuals print the same two-way row - Service Checklist - Diagnosis Guide on printed page 23 of the 2012 manual (text.md lines 996-999), printed page 38 of the 2016 manual (text.md lines 989-992), TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 42 of the 2020 manual (text.md lines 1088-1091) and TROUBLESHOOTING on printed page 52 of the CT800ENT 2022 manual (text.md lines 1180-1181); all four CT850 owner's manuals print the same two-way row - TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 42 of the 2016 manual (text.md lines 1085-1088) and of the 2020 manual (text.md lines 1084-1087), SERVICE CHECKLIST - DIAGNOSIS GUIDE on printed page 41 of the 2018 manual (text.md lines 1048-1051) and TROUBLESHOOTING on printed page 52 of the CT850ENT 2022 manual (text.md lines 1186-1187)
  extracted_at: '2026-09-08'
---

The checklist splits this by what the belt does first.

1. If the belt moves but stops after a short time and the display shows `LS`, **run calibration**.
2. If you press start and the belt never moves, and then the display shows `LS`, **contact service**.

`LS` here is the same fault the manual elsewhere calls `LOW SPEED`, `LS1/LOW SPEED` and
`SPEED ERROR`: see `ct850-2016-low-speed-error-message`.

**All four CT800 generations print this row word for word**, LS distinction included - the
2012, 2016 and 2020 owner's manuals and the CT800ENT 2022 owner's manual alike. `LS` is the
**only code any CT800 owner's manual prints**; those manuals carry no error-code table at
all.

**All four CT850 owner's manuals print it word for word too** - the 2016, 2018 and 2020
manuals and the CT850ENT 2022 manual. The same holds there: `LS` is the **only code any
CT850 owner's manual prints**, and none of the four carries an error-code table.

**The CT850 2020 *service* manual answers this differently.** It drops the LS distinction
entirely and says only `Reset power. If still no good contact service.` - see
`ct850-2020-motor-not-responsive-after-start`. That is the service document disagreeing with
the owner's manual for the same machine, not a second machine. The CT900ENT gives the short
answer as well (`ct900ent-motor-unresponsive-after-start`).

**Three look-alikes for the same symptom.** The Spirit XT manuals print `E1` in this row
rather than `LS` (`xt-2023-errors-e1-motor-not-responsive`), and several Sole treadmills
raise an `LS` of their own with a different diagnostic path (`sole-ls-error`). A Sole `LS`
is not this fault, and `E1` is not this code.
