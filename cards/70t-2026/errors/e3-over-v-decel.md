---
id: 70t-2026-errors-e3-over-v-decel
title: 'E3 Over V Decel: check the AC line voltage and the brake'
kind: troubleshooting
question: What does error code E3 (Over V Decel) mean on a Spirit treadmill, and what
  does the manual say to check?
asked_as:
- what does e3 mean on my treadmill
- treadmill display says e3
- over voltage while slowing down error on the running machine
keywords:
- e3
- over v decel
- over voltage while slowing down
- error code
- fault code
- commercial treadmill
- console error
- check ac line v
- check brake
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
  code: e3
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-e2-over-volt
- 70t-2026-errors-e11-over-i-decel
- 70t-2026-errors-e26-bk-chopper
- ct900-e3-igbt-over-temp
- ct850-2020-e3-incline-motor-cannot-work
- sole-e3-error
see_also:
- 70t-2026-errors-error-code-table
- spirit-mt200-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 1 of 5, lines 1481-1483; the same row is printed word for word in both
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

**This is the 7.0T and MT200 E3 (Over V Decel) - not E2 (Over Volt), not E11 (Over I Decel), not the CT900 E3 (IGBT Over Temp), not Spirit CT850-2020 E3 (incline motor) and not the Sole E3 (incline fault).**

| Field | Value |
|---|---|
| Code | E3 |
| Name, as printed | Over V Decel |

**The causes and remedies the table lists under it, in printed order:**

1. Check AC line V
2. Check Brake

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

**Service manual remedy.** The 7.0T (MT8000-ST021-02) service manual, section 4.2.3 *Error Codes: Messages, Cause and Solution*, prints this code as **E3 Over-Voltage, Decel: The DC voltage inside Inverter exceeded the maximum allowable value during deceleration.** and gives, in order:

1) Check the AC line voltage.
2) Replace Inverter.

**The 2024 MT200 error-codes leaflet (`spirit-treadmill-mt200-error-codes-list`) prints it as `E3 Over Voltage Deceleration` with one line: *Check AC line voltage and motor brake.*** The leaflet is titled for the MT200 with no year and is carried for both MT200 revisions; it is a summary of the list above in fewer words, and where it names parts it names the same ones.
