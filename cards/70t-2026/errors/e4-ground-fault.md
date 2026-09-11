---
id: 70t-2026-errors-e4-ground-fault
title: 'E4 Ground Fault: check wiring, replace the drive'
kind: troubleshooting
question: What does error code E4 (Ground Fault) mean on a Spirit treadmill, and what
  does the manual say to check?
asked_as:
- what does e4 mean on my treadmill
- treadmill display says e4
- ground fault error on the running machine
keywords:
- e4
- ground fault
- error code
- fault code
- commercial treadmill
- console error
- check wiring
- replace drive
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2025
  - 70t-2026
  - mt200-2010
  - mt200-2022
  section: errors
  code: e4
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e5-igbt-fault
- 70t-2026-errors-e28-phase-loss
- ct900-e4-motor-overload
- sole-e4-error
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 1 of 5, lines 1484-1486; the same row is printed word for word in both
    MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page
    41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and
    solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522);
    7.0T (MT200 2022) service manual 4.2.3 Error Codes: Messages, Cause and Solution,
    PDF p. 12-17, text.md lines 208-385; spirit-treadmill-mt200-error-codes-list,
    Error Codes List MT200 - English, text.md lines 3-165 (a one-page 2024 leaflet);
    7.0T 2025 owner''s manual (Rev 01.10.25, spirit-treadmill-70t-2025-owners-manual)
    prints the same table word for word, ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48
    (printed 46), text.md lines 1478-1513 (compared with difflib on 2026-09-11); the
    7.0T-770885 export of that service manual (spirit-treadmill-70t-2026-service-manual,
    February 2026, 99.7% the same text) prints 4.2.3 identically at PDF p. 12-17,
    text.md lines 236-413'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E4 (Ground Fault) - not E5 (IGBT Fault), not E28 (Phase Loss), not the CT900 E4 (Motor Overload) and not the Sole E4 (drive motor voltage).**

| Field | Value |
|---|---|
| Code | E4 |
| Name, as printed | Ground Fault |

**The causes and remedies the table lists under it, in printed order:**

1. Check wiring
2. Replace Drive

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E4 Ground Fault: The output terminal(s) of Inverter is grounded.** and gives, in order:

1) Check the motor wire connections between the Inverter and Motor for possible short circuits. Also check if wires are shorted to ground.
2) Replace Inverter.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E4 Ground Fault` with one line: *Check wiring, replace inverter.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
