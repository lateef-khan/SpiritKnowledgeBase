---
id: csc900-2019-errors-no-power-and-no-beep-adapter-indicator-first
title: 'No power and no beep after power is applied: the adapter indicator is checked
  first, then console wire, control line, and three parts in turn'
kind: troubleshooting
question: What do I check when a Spirit csc900-2019 stair climber has no power and
  does not beep?
asked_as:
- climbmill dead no beep
- csc900 console does not respond when plugged in
- no power on my spirit stair climber
keywords:
- no power
- no beep
- power adapter
- indicator light
- control line
- console wire
- climbmill
- stair climber
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: no-power
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-console-does-not-light-up-after-power-on
- csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks
see_also:
- csc900-2019-errors-error-code-table
- csc900-2019-errors-communication-line-continuity-test
- csc900-2019-errors-button-failure-membrane-key-or-handrail-button
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, row 8, PDF p. 9; text.md
    lines 337-345
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** **Issue:** No power (console does not respond and no beep sounds after power is applied).

| Analysis | Method |
|---|---|
| The console is not powered. Bad reasons: 1. Bad power adapter. 2. Bad control. 3. Bad control line. 4. Bad console. | 1. Check if the power adapter indicator is on and replace the test. 2. Check if the console wire is normal and reconnect it. 3. Check whether the control line is pinched or otherwise defective. 4. Replace the console, the control line, and the lower control board in turn for troubleshooting. |

**The adapter has an indicator light, and it is the first check.** A dark adapter LED narrows the fault to the supply before a meter comes out; "replace the test" is the book's phrasing for swapping in a known-good adapter. **No voltage figure is printed anywhere in this row** - not at the adapter, not at the console - which is the difference from the two later stair climber books: the 2022 magnetic CSC900 measures 24 V at two points (`csc900-2024-errors-console-does-not-light-up-after-power-on`) and the CSC880 24 V then 12 V (`csc880-2025-errors-console-does-not-light-up-24v-and-12v-checks`). Do not carry their figures onto this machine.

**Step 4 is substitution, in a printed order:** console, then control line, then lower control board. The control line can also be buzzed out end to end before anything is swapped (`csc900-2019-errors-communication-line-continuity-test`).

**The beep matters.** The row's condition is *no response and no beep*; a console that beeps at a key press is powered, and a dead key on a powered console is the button row (`csc900-2019-errors-button-failure-membrane-key-or-handrail-button`).
