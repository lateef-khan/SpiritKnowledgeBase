---
id: 70t-2026-errors-er2-decline-err
title: 'ER2 Decline Err: the decline message that appears in the Grade window'
kind: troubleshooting
question: What does ER2 mean in the Grade window of a Spirit 70t-2026 treadmill?
asked_as:
- treadmill shows er2 in the grade window
- what is er2 on my treadmill
- decline error on the display
keywords:
- er2
- decline err
- decline error
- grade window
- negative incline
- downhill
- error code
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 70t-2025
  - 70t-2026
  section: errors
  code: er2
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-err-incline-err
- spirit-mt200-errors-e42-decline-err
- spirit-mt200-errors-e41-incline-err
- 70t-2026-errors-e2-over-volt
- ct900-e2-over-voltage
- cvc800-e-2-tension-motor-error
- sole-e2-error
see_also:
- 70t-2026-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md
    column 5 of 5, lines 1476-1477; 7.0T 2025 owner's manual (Rev 01.10.25, spirit-treadmill-70t-2025-owners-manual)
    prints the same table word for word, ERROR MESSAGE & TROUBLESHOOTING, PDF p. 48
    (printed 46), text.md lines 1478-1513 (compared with difflib on 2026-09-11)
  extracted_at: '2026-09-09'
---

**This is ER2 (Decline Err) - not ERR (Incline Err), and not E2 (Over Volt) on this same machine, nor the CT900 E2 (Over Voltage), the CVC800 E-2 (tension motor) or the Sole E2 (motor overcurrent).**

| Field | Value |
|---|---|
| Code | ER2 |
| Name, as printed | Decline Err |
| Where it appears | The Grade window |

This machine declines as well as inclines, and the manual gives the decline direction its own message. `ER2` and `ERR` are the only two rows in the table that are not numbered `E<n>`, and the only two whose printed row names the window they appear in.

**The table lists no cause and no remedy for ER2.** Every numbered code in the same table carries at least one; this row carries none. Do not read the neighbouring column's causes across into it - they belong to the numbered codes.

**The MT200 numbers this fault instead of naming it.** Both Spirit MT200 owner's manuals
print the identical E1-E38 table and then end it with `E41 Incline Err` and `E42 Decline
Err` rather than `ERR` and `ER2`, and print no window note
(`spirit-mt200-errors-e42-decline-err`). Same fault, different identifier - which is why it
is a separate card.
