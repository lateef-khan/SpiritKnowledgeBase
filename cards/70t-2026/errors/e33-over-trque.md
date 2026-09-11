---
id: 70t-2026-errors-e33-over-trque
title: 'E33 Over Trque: mechanical, deck lube, brake, bad motor or drive'
kind: troubleshooting
question: What does error code E33 (Over Trque) mean on a Spirit treadmill, and what
  does the manual say to check?
asked_as:
- what does e33 mean on my treadmill
- treadmill display says e33
- over torque error on the running machine
keywords:
- e33
- over trque
- over torque
- error code
- fault code
- commercial treadmill
- console error
- mechanical
- deck lube
- brake
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
  code: e33
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e8-over-torque
- ct900-e33-incline-err
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 4 of 5, lines 1482-1487; the same row is printed word for word in both
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

**This is the 7.0T and MT200 E33 (Over Trque) - not E8 (Over Torque) and not the CT900 E33 (INCLINE ERR).**

| Field | Value |
|---|---|
| Code | E33 |
| Name, as printed | Over Trque |

**The causes and remedies the table lists under it, in printed order:**

1. Mechanical
2. Deck Lube
3. Brake
4. Bad Motor
5. Bad Drive

The table prints nothing else for this code - no description, no test procedure and no part number. The wording above is the manual's own, abbreviated as it prints it.

`Over Trque` is the manual's own spelling.

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E33 Over-Torque: Over-Torque detected.** and gives, in order:

1) Check the deck/belt for high friction or worn out.
2) Check that the Brake is released when Motor is moving.
3) Replace Inverter.
4) Replace Motor.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E33 Over Torque` with one line: *Check whether there are any abnormalities on the mechanism, lubrication, motor brake, drive motor, and inverter.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
