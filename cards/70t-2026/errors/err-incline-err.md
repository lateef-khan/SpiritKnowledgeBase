---
id: 70t-2026-errors-err-incline-err
title: 'ERR Incline Err: the incline message that appears in the Grade window'
kind: troubleshooting
question: What does ERR mean in the Grade window of a Spirit 70t-2026 treadmill?
asked_as:
- my treadmill shows err where the incline number goes
- grade window says err
- incline error on the display
keywords:
- err
- incline err
- incline error
- grade window
- elevation
- ramp
- error code
- console error
facets:
  brand:
  - spirit
  product_line: treadmill
  model: 70t-2026
  applies_to:
  - 70t-2026
  section: errors
  code: err
  model_number:
  - '770885'
authority: 3
not_to_be_confused_with:
- 70t-2026-errors-er2-decline-err
- spirit-mt200-errors-e41-incline-err
- spirit-mt200-errors-e42-decline-err
- 70t-2026-errors-e3-over-v-decel
- ct900-e33-incline-err
- ct850-2020-incline-err
- ct850-2016-incline-err-shown-in-incline-window
- st90-2023-err-after-pressing-start
see_also:
- 70t-2026-errors-error-code-table
source:
  ref: spirit-treadmill-70t-2026-owners-manual
  locator: 'Error Codes table, ERROR MESSAGE & TROUBLESHOOTING, printed page 46; text.md column 5 of 5, lines 1474-1475'
  extracted_at: '2026-09-09'
---

**This is ERR (Incline Err) - not ER2 (Decline Err), not the CT900 E33 (INCLINE ERR), not the CT850's INCLINE ERR, and not the Sole `Err` that means no pulse or a failed start.**

| Field | Value |
|---|---|
| Code | ERR |
| Name, as printed | Incline Err |
| Where it appears | The Grade window |

`ERR` and `ER2` are the only two messages in this table that are not numbered `E<n>`, and the only two whose printed row names the window they appear in. The manual is telling you where to look, not what failed: an incline fault shows up in the Grade window rather than as a number in the message window.

**The table lists no cause and no remedy for ERR.** Every numbered code in the same table carries at least one; this row carries none. Do not read the neighbouring column's causes across into it - they belong to the numbered codes.

**The MT200 numbers this fault instead of naming it.** Both Spirit MT200 owner's manuals
print the identical E1-E38 table and then end it with `E41 Incline Err` and `E42 Decline
Err` rather than `ERR` and `ER2`, and print no window note
(`spirit-mt200-errors-e41-incline-err`). Same fault, different identifier - which is why it
is a separate card.
