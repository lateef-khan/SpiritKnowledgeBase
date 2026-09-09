---
id: 70t-2026-errors-e6-drive-ovrload
title: 'E6 Drive Ovrload: deck lube, brake locked, bad drive or motor'
kind: troubleshooting
question: What does error code E6 (Drive Ovrload) mean on a Spirit treadmill, and what does the manual say to check?
asked_as:
- what does e6 mean on my treadmill
- treadmill display says e6
- drive overload error on the running machine
keywords:
- e6
- drive ovrload
- drive overload
- error code
- fault code
- commercial treadmill
- console error
- deck lube
- brake locked
- bad drive
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
  code: e6
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e7-thrm-ovrload
- 70t-2026-errors-e34-thrm-ovrld-2
- 70t-2026-errors-e8-over-torque
- ct900-e6-external-fault
- sole-e6-error
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md column 1 of 5, lines 1490-1494; the same row is printed word for word in both MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page 41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522)'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E6 (Drive Ovrload) - not E7 (Thrm Ovrload), not E34 (Thrm Ovrld 2), not the CT900 E6 (External Fault) and not the Sole E6 (motor controller fault).**

| Field | Value |
|---|---|
| Code | E6 |
| Name, as printed | Drive Ovrload |

**The causes and remedies the table lists under it, in printed order:**

1. Deck Lube
2. Brake locked
3. Bad Drive
4. Bad Motor

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
