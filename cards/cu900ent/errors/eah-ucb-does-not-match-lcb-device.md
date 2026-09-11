---
id: cu900ent-eah-ucb-does-not-match-lcb-device
title: 'EAH: upper board does not match the lower board'
kind: troubleshooting
question: What does error code EAH mean on a Spirit CU900ENT bike or CT900ENT treadmill?
asked_as:
- what does eah mean on my spirit bike
- bike console showing eah
- spirit upright bike error eah
keywords:
- eah
- '0xea'
- ucb
- lcb
- not match
- upper board
- lower board
- error code
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ct900ent
  - cu900ent
  section: errors
  code: eah
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-ech-ucb-to-lcb-no-response
- cu900ent-edh-lcb-unknown-device
- cu900ent-error-code-messages-list
- cu900ent-error-code-log
- ct900ent-errors-error-code-messages-list
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Error Code Messages table, page 22; CT900ENT service manual Error Code
    Messages, PDF p. 19, text.md lines 256-288
  extracted_at: '2026-09-08'
---

**This is EAH, and it is not any other code in the same table.** `Math` is a misprint for `Match`: the error log screenshot in this same manual spells the entry `UCB No Match LCB Device` and numbers it `0xea`. UCB is the upper control board (the console); LCB is the lower control board.

| Field | Value |
|---|---|
| Error Code | EAH |
| Description, word for word | UCB Is Not Math LCB Device |
| Remarks Error | GUI Error |

**The manual prints no cause and no fix for this code.** The table has three columns and none of
them is a solution column; the only tool the manual names anywhere in the error section is a
multi-meter. Anything beyond the description above would be invention.

The whole printed table, and what the two families of code mean, is on `cu900ent-error-code-messages-list`.

**The CT900ENT treadmill service manual prints this row word for word** - same code, same description, same remark - in an Error Code Messages table that also carries sixteen inverter codes the bike does not have (`ct900ent-errors-error-code-messages-list`).
