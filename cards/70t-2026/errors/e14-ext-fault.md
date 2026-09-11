---
id: 70t-2026-errors-e14-ext-fault
title: 'E14 Ext Fault: reset power'
kind: troubleshooting
question: What does error code E14 (Ext Fault) mean on a Spirit treadmill, and what
  does the manual say to check?
asked_as:
- what does e14 mean on my treadmill
- treadmill display says e14
- external fault error on the running machine
keywords:
- e14
- ext fault
- external fault
- error code
- fault code
- commercial treadmill
- console error
- reset power
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
  code: e14
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e38-ext-bb
- 70t-2026-errors-e17-hw-fault
- ct900-e14-dc-low-volt
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 2 of 5, lines 1495-1496; the same row is printed word for word in both
    MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page
    41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and
    solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522);
    7.0T (MT200 2022) service manual 4.2.3 Error Codes: Messages, Cause and Solution,
    PDF p. 12-17, text.md lines 208-385; spirit-treadmill-mt200-error-codes-list,
    Error Codes List MT200 - English, text.md lines 3-165 (a one-page 2024 leaflet)'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E14 (Ext Fault) - not E38 (Ext BB), not E17 (HW Fault) and not the CT900 E14 (DC Low Volt).**

| Field | Value |
|---|---|
| Code | E14 |
| Name, as printed | Ext Fault |

**The one cause or remedy the table lists under it:** Reset Power

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E14 Ext Fault: External fault** and gives, in order:

1) Reset the power.
2) Check Wiring.
3) Check the AC line voltage.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E14 External Fault` with one line: *Reset power.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
