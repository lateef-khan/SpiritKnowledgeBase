---
id: f85-2026-error-message-table
title: Every error message this manual lists, and how the code family differs
kind: spec
question: What error codes can an F85-2026 treadmill show?
asked_as:
- list of error codes for my treadmill
- what do the e codes mean on my treadmill
- treadmill error code list
keywords:
- error codes
- error message list
- digital control system
- code family
- console showing
- fault codes
- e01
- e31
- lube
facets:
  brand:
  - sole
  product_line: treadmill
  model: f85-2026
  applies_to:
  - f85-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f85-2026-lube-message
- f85-2026-e01-over-current
- f85-2026-e02-hall-mistake
- f85-2026-e03-hardware-over-current
- f85-2026-e04-phase-loss
- f85-2026-e05-undervoltage
- f85-2026-e06-overvoltage
- f85-2026-e3-incline-adjustment-error
- f85-2026-e22-led-console-communication
- f85-2026-e23-tft-to-led-communication
- f85-2026-e31-overtemperature
- f85-2026-error-tft-communication-failure
- sole-dc-controller-error-code-list
source:
  ref: sole-tm-f85-2026-owners-manual
  locator: page 33, Error Messages For Digital-Control System Treadmills
  extracted_at: '2026-09-04'
---

**Read the code exactly. This table contains E03 and E3 and E31 as three different faults.**

| Message as printed | Meaning as printed |
|---|---|
| Console Showing LUBE | Reminder to check lubrication under walking deck |
| Console Showing E01 | Over Current Protection. Treadmill over loaded, controller protection is activated. |
| Console Showing E02 | Hall mistake |
| Console Showing E03 | The hardware current is too large. |
| Console Showing E04 | Phase loss |
| Console Showing E05 | undervoltage |
| Console Showing E06 | overvoltage |
| Console Showing E3 | Incline adjustment error |
| Console Showing E22 | Error in communication between the LED electronic watch and the control board |
| Console Showing E23 | TFT electronic watch has communication error with LED electronic watch |
| Console Showing E31 | overtemperature |
| Console ERROR | TFT electronic watch communication failure |

Each row has its own card with the full solution list.

**"Electronic watch" means the display board.** The manual uses it throughout for the console displays — "LED
electronic watch" is the LED display board and "TFT electronic watch" is the touchscreen board.

**E31 is printed with no solution at all.** The overtemperature row has a meaning and an empty solution column.
That is how the manual prints it; nothing has been supplied.

**This code family is not the E1 to E8 family of the earlier Sole treadmills.** The shared knowledge base card
`sole-dc-controller-error-code-list` lists E1 to E8 for the DC digital controller and names **f85-2026** in its
`applies_to`, but this machine's own manual prints a different family, and the meanings do not line up:

| This manual | Meaning here | Nearest code in the E1-E8 family | Meaning there |
|---|---|---|---|
| E01 | over current protection | E2 | overload trips overcurrent protection |
| E02 | hall mistake | E1 | no speed signal |
| E03 | hardware current too large | (no equivalent printed) | |
| E04 | phase loss | E4 | abnormal voltage at motor terminals |
| E05 / E06 | undervoltage / overvoltage | E7 | external voltage abnormality |
| E3 | incline adjustment error | E3 | incline abnormality |
| E22 / E23 | display communication | E5 | console to control board communication |
| E31 | overtemperature | (no equivalent printed) | |

**Only E3 means the same thing in both.** The two documents disagree about what a two-character code such as E2
means on this machine, and neither acknowledges the other. This card picks no winner and reports both; the
orchestrator should decide whether `sole-dc-controller-error-code-list` should still claim f85-2026.
