---
id: 70t-2026-errors-e11-over-i-decel
title: 'E11 Over I Decel: deck lube, bad drive or motor'
kind: troubleshooting
question: What does error code E11 (Over I Decel) mean on a Spirit treadmill, and
  what does the manual say to check?
asked_as:
- what does e11 mean on my treadmill
- treadmill display says e11
- over current while slowing down error on the running machine
keywords:
- e11
- over i decel
- over current while slowing down
- error code
- fault code
- commercial treadmill
- console error
- deck lube
- bad drive
- bad motor
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
  code: e11
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e10-over-i-accel
- 70t-2026-errors-e9-over-i-speed
- 70t-2026-errors-e3-over-v-decel
- ct900-e11-decel-ovr-curr
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 2 of 5, lines 1483-1486; the same row is printed word for word in both
    MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page
    41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and
    solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522);
    7.0T (MT200 2022) service manual 4.2.3 Error Codes: Messages, Cause and Solution,
    PDF p. 12-17, text.md lines 208-385; spirit-treadmill-mt200-error-codes-list,
    Error Codes List MT200 - English, text.md lines 3-165 (a one-page 2024 leaflet)'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E11 (Over I Decel) - not E10 (Over I Accel), not E9 (Over I Speed) and not the CT900 E11 (DECEL OVR CURR).**

| Field | Value |
|---|---|
| Code | E11 |
| Name, as printed | Over I Decel |

**The causes and remedies the table lists under it, in printed order:**

1. Deck Lube
2. Bad Drive
3. Bad Motor

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E11 Over-I Decel: Over-current during deceleration.** and gives, in order:

1) Check the deck/belt for high friction or worn out.
2) Check that the Brake is released when Motor is moving.
3) Check the wiring between the Inverter and Motor.
4) Replace Inverter.
5) Replace Motor.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E11 Over Current Deceleration` with one line: *Check the running deck and running belt lubrication, inverter, drive motor.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
