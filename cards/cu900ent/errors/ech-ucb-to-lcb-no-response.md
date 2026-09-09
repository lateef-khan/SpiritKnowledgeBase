---
id: cu900ent-ech-ucb-to-lcb-no-response
title: 'ECH: upper board gets no response from the lower board'
kind: troubleshooting
question: What does error code ECH mean on a Spirit CU900ENT bike?
asked_as:
- what does ech mean on my spirit bike
- bike console showing ech
- spirit upright bike error ech
keywords:
- ech
- '0xec'
- ucb
- lcb
- no response
- upper board
- lower board
- error code
facets:
  brand:
  - spirit
  product_line: bike
  model: cu900ent
  applies_to:
  - cu900ent
  section: errors
  code: ech
authority: 3
not_to_be_confused_with: []
see_also:
- cu900ent-eah-ucb-does-not-match-lcb-device
- cu900ent-edh-lcb-unknown-device
- cu900ent-error-code-messages-list
- cu900ent-error-code-log
source:
  ref: spirit-bike-cu900ent-service-manual
  locator: Error Code Messages table, page 22
  extracted_at: '2026-09-08'
---

**This is ECH, and it is not any other code in the same table.** UCB is the upper control board (the console); LCB is the lower control board. The console asked and got nothing back.

| Field | Value |
|---|---|
| Error Code | ECH |
| Description, word for word | UCB To LCB Is No Response |
| Remarks Error | GUI Error |

**The manual prints no cause and no fix for this code.** The table has three columns and none of
them is a solution column; the only tool the manual names anywhere in the error section is a
multi-meter. Anything beyond the description above would be invention.

The whole printed table, and what the two families of code mean, is on `cu900ent-error-code-messages-list`.
