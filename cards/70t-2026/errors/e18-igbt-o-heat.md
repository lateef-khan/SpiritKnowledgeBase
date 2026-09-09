---
id: 70t-2026-errors-e18-igbt-o-heat
title: 'E18 IGBT O-Heat: bad drive fan, dirty heat sink'
kind: troubleshooting
question: What does error code E18 (IGBT O-Heat) mean on a Spirit treadmill, and what does the manual say to check?
asked_as:
- what does e18 mean on my treadmill
- treadmill display says e18
- igbt overheat error on the running machine
keywords:
- e18
- igbt o-heat
- igbt overheat
- error code
- fault code
- commercial treadmill
- console error
- bad drive fan
- dirty heat sink
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2026
  - mt200-2010
  - mt200-2022
  section: errors
  code: e18
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e5-igbt-fault
- 70t-2026-errors-e19-ambient-temp
- 70t-2026-errors-e31-fan
- ct900-e18-over-torque
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md column 3 of 5, lines 1474-1476; the same row is printed word for word in both MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page 41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522)'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E18 (IGBT O-Heat) - not E5 (IGBT Fault), not E19 (Ambient Temp) and not the CT900 E18 (Over Torque).**

| Field | Value |
|---|---|
| Code | E18 |
| Name, as printed | IGBT O-Heat |

**The causes and remedies the table lists under it, in printed order:**

1. Bad Drive Fan
2. Dirty Heat Sink

The table prints nothing else for this code - no description, no test procedure and no part number. The wording above is the manual's own, abbreviated as it prints it.

**Three manuals print this row, and they agree.** The 7.0T 2026 owner's manual and both
MT200 owner's manuals - the 2010 revision effective July 2013 and the 2022 revision - print
the same code, the same name and the same causes, in the same printed order. The MT200 is a
medical treadmill and the 7.0T a commercial one, but they carry the same AC drive and the
same fault table.

**Where the two tables stop differing.** The MT200 table runs on past E38 to two numbered
incline codes, `E41 Incline Err` and `E42 Decline Err`
(`spirit-mt200-errors-e41-incline-err`, `spirit-mt200-errors-e42-decline-err`), which the
7.0T instead prints unnumbered as `ERR` and `ER2`. Those four are separate cards because
they are separate identifiers.
