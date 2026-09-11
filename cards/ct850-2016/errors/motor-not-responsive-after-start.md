---
id: ct850-2016-motor-not-responsive-after-start
title: The motor does not respond after START is pressed and the display shows LS
kind: troubleshooting
question: What does it mean when the motor does not respond after START on a Spirit
  CT800, CT800ENT, CT850, CT900ENT or 2010 XT685 treadmill?
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
  - ct800-2024
  - ct800ent-2022
  - ct850-2016
  - ct850-2018
  - ct850-2020
  - ct850-2024
  - ct850ent-2022
  - ct900ent
  - xt685-2010
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
- ct900ent-errors-error-code-messages-list
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: 'Section 9.2 Service Troubleshooting Checklist - Diagnosis Guide, pages
    56-57 (printed 55-56); all four CT800 owner''s manuals print the same two-way
    row - Service Checklist - Diagnosis Guide on printed page 23 of the 2012 manual
    (text.md lines 996-999), printed page 38 of the 2016 manual (text.md lines 989-992),
    TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 42 of the 2020 manual (text.md
    lines 1088-1091) and TROUBLESHOOTING on printed page 52 of the CT800ENT 2022 manual
    (text.md lines 1180-1181); all four CT850 owner''s manuals print the same two-way
    row - TROUBLESHOOTING - DIAGNOSIS GUIDE on printed page 42 of the 2016 manual
    (text.md lines 1085-1088) and of the 2020 manual (text.md lines 1084-1087), SERVICE
    CHECKLIST - DIAGNOSIS GUIDE on printed page 41 of the 2018 manual (text.md lines
    1048-1051) and TROUBLESHOOTING on printed page 52 of the CT850ENT 2022 manual
    (text.md lines 1186-1187); the XT685 2010 owner''s manual prints the same two-way
    row in Service Checklist - Diagnosis Guide on printed page 31 (PDF page 35, text.md
    lines 1397-1400); CT800 2016 service manual 9.1 Service Troubleshooting Checklist,
    PDF p. 61-62 (printed 60-61), text.md lines 1222-1273; CT900ENT service manual
    Service Troubleshooting Checklist (first printing), PDF p. 50-51, text.md lines
    848-900; the CT900ENT service manual prints the checklist a second time on PDF
    p. 58-59 with the row worded "LS/LOW SPEED" and the pointer "See section 8.1 on
    Error Message: LS/LOW SPEED"'
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

**Three look-alikes for the same symptom.** The 2015 and 2023 Spirit XT manuals print `E1`
in this row rather than `LS` (`xt-2023-errors-e1-motor-not-responsive`), and several Sole
treadmills raise an `LS` of their own with a different diagnostic path (`sole-ls-error`). A
Sole `LS` is not this fault, and `E1` is not this code.

**The XT685 changed code between generations, and the 2010 machine is on this card.** The
XT685 **2010** owner's manual prints this row with `LS`, word for word as the CT800 and CT850
manuals do. The XT685 2015 and 2023 manuals print the identical two branches with `E1`
instead. The symptom, the split by whether the belt moved, and both remedies are unchanged -
only the code string moved. Answer a 2010 XT685 owner with `LS`; do not carry `E1` back onto
that machine, and do not carry `LS` forward onto the 2015 or 2023 one.

**The CT900 owner's manual prints this same two-way row, but the CT900 is not on this card.**
`spirit-treadmill-ct900-owners-manual`, TROUBLESHOOTING on printed page 40 (text.md lines
1317-1318), prints both branches word for word. The CT900 is left out of `applies_to` only
because the fact is already held for that machine by `ct900-motor-not-responsive-or-wont-start`,
which is filed under `section: maintenance` with `code: '*'` - so a scope filtered to
`section: errors` or to `code: low-speed` reaches the CT800 and CT850 answer but not the
CT900's. Folding the CT900 in belongs with a decision about that card, not with a second copy
of the row here.

**"No error-code table" is a CT800/CT850 statement, not a Spirit-wide one.** Two other Spirit
commercial treadmills print this same LS row *and* carry a code table. The CT900 owner's
manual devotes printed pages 44-48 to ERROR CODES, three of them headed *ERROR CODES - AC
MOTOR DRIVE INVERTER*; the CTSBS900 owner's manual prints a seventeen-row inverter table on
printed pages 46-48 (`ctsbs900-le1-inverter-low-voltage` and its siblings). Neither family
uses `LS`-style codes.

**The CT800 2024 and CT850 2024 owner's manuals print both branches word for word**, `LS` included,
on printed page 41. `LS` is still the only code either of those two books prints in its diagnosis
table - the CT800 2024's separate ERROR CODES page carries E1 to E7 and the CT850 2024's carries the
twenty-three-code inverter table, and neither of those tables mentions `LS`.

**The two ENT treadmills of the same 2024 family answer this row differently**, with no code at
all: `Reset power. If still no good contact service.` See `ct900ent-motor-unresponsive-after-start`.

**The CT800 2016 service manual prints this row word for word**, `LS` and the two branches, and sends the reader to *the procedure on next page* for the calibration. **The CT900ENT service manual prints it twice** - once with `LS` and once, in a second copy of the checklist at the end of the book, with `LS/LOW SPEED` and a pointer to a section 8.1 that does not exist in that book (its error chapter is chapter 6). Both copies say run calibration if the belt moved, contact service if it never did. That contradicts the CT900ENT *owner's* manual, which answers the same row with `Reset power. If still no good contact service.` (`ct900ent-motor-unresponsive-after-start`); nothing reconciles the two for that machine. The CT900ENT's own error table has no LS code either - the message the console will show is one of its hex codes (`ct900ent-errors-error-code-messages-list`).
