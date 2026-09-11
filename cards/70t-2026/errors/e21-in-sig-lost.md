---
id: 70t-2026-errors-e21-in-sig-lost
title: 'E21 In Sig Lost: check wiring, bad drive'
kind: troubleshooting
question: What does error code E21 (In Sig Lost) mean on a Spirit treadmill, and what
  does the manual say to check?
asked_as:
- what does e21 mean on my treadmill
- treadmill display says e21
- input signal lost error on the running machine
keywords:
- e21
- in sig lost
- input signal lost
- error code
- fault code
- commercial treadmill
- console error
- check wiring
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
  code: e21
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e29-i-signl-stop
- 70t-2026-errors-e32-analog-in
- 70t-2026-errors-e27-pg-error
- ct900-e21-safety-key
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 3 of 5, lines 1483-1485; the same row is printed word for word in both
    MT200 owner''s manuals - "Error Codes, Messages and Solution/Cause", printed page
    41 of the 2010 manual (text.md lines 1496-1541), and "Error codes, messages and
    solution/cause", printed pages 65-66 of the 2022 manual (text.md lines 2453-2522);
    7.0T (MT200 2022) service manual 4.2.3 Error Codes: Messages, Cause and Solution,
    PDF p. 12-17, text.md lines 208-385; spirit-treadmill-mt200-error-codes-list,
    Error Codes List MT200 - English, text.md lines 3-165 (a one-page 2024 leaflet)'
  extracted_at: '2026-09-09'
---

**This is the 7.0T and MT200 E21 (In Sig Lost) - not E29 (I Signl Stop), not E32 (Analog In) and not the CT900 E21 (Safety Key).**

| Field | Value |
|---|---|
| Code | E21 |
| Name, as printed | In Sig Lost |

**The causes and remedies the table lists under it, in printed order:**

1. Check Wiring
2. Bad Drive

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E21 Input Sig Lost: Analog input signal lost** and gives, in order:

1) Check Wiring.
2) Replace Inverter.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E21 Input Signal Lost` with one line: *Check wiring, check inverter.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
