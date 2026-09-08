---
id: cu900ent-error-code-log
title: Reading and clearing the error code log
kind: procedure
question: Where do I find the logged error codes on a Spirit CU900ENT bike?
asked_as:
- where is the error log on my spirit bike
- how to clear the error log on the console
- diagnostics screen on a cu900
keywords:
- error code log
- diagnostics
- engineering mode
- clear errors
- fault history
- console
- technician
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-error-code-messages-list
- cu900ent-eah-ucb-does-not-match-lcb-device
- ce800ent-error-code-log
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Diagnostics, page 27. This page is a flattened image and was read from
    raw/page-27.png, not from the OCR text
  extracted_at: '2026-09-08'
---

**Diagnostics** in engineering mode holds the console's fault history.

> Diagnose and save malfunction error messages for technician to inspect the machine and
> troubleshooting.
> Press "Error Code Log" button 10 consecutive repetitions to clear the error message.

So: **press the `Error Code Log` button ten times in a row to clear the log.** When it is empty the
screen shows a `Deleted All Error Log` button.

Each logged line carries a code, a description and a timestamp. The worked example in the manual
reads `0xea  UCB No Match LCB Device  2015-12-16 11:04:14`.

Two things to note.

- The log writes codes as `0x` values, while the error code table writes the same code as `EAH`.
  They are the same code.
- The log spells the entry `No Match`, which confirms that `Is Not Math` in the code table is a
  misprint.

To reach engineering mode, press the `Home` button ten times in a row. Diagnostics is the third
entry in the Settings list.

The CE800ENT elliptical has the same console family and the same Diagnostics screen, but its manual
does not print the ten-press clearing instruction: `ce800ent-error-code-log`.
