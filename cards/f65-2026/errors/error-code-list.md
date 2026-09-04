---
id: f65-2026-error-code-list
title: Every message the console can show and what each one means
kind: fact
question: What error codes can a Sole F65-2026 treadmill show?
asked_as:
- list of treadmill error codes
- what do the e codes mean on my sole treadmill
- treadmill error code chart
keywords:
- error codes
- error messages
- code list
- console message
- fault codes
- diagnosis
- e codes
- lube
facets:
  brand:
  - sole
  product_line: treadmill
  model: f65-2026
  applies_to:
  - f65-2026
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f65-2026-e01-over-current
- f65-2026-e02-hall-mistake
- f65-2026-e03-hardware-current
- f65-2026-e04-phase-loss
- f65-2026-e05-undervoltage
- f65-2026-e06-overvoltage
- f65-2026-e22-communication-error
- f65-2026-e3-incline-adjustment-error
- f65-2026-e31-overtemperature
- f65-2026-lube-message
- f65-2026-motor-not-responsive-after-start
- f65-2026-safety-key-removed-message
source:
  ref: sole-tm-f65-2026-owners-manual
  locator: page 28, ERROR MESSAGES FOR DIGITAL-CONTROL SYSTEM TREADMILLS
  extracted_at: '2026-09-04'
---

| Console shows | Meaning | Card |
|---|---|---|
| **LUBE** | Reminder to check lubrication under the walking deck | `f65-2026-lube-message` |
| **E01** | Over current protection - treadmill over loaded, controller protection is activated | `f65-2026-e01-over-current` |
| **E02** | Hall mistake | `f65-2026-e02-hall-mistake` |
| **E03** | The hardware current is too large | `f65-2026-e03-hardware-current` |
| **E04** | Phase loss | `f65-2026-e04-phase-loss` |
| **E05** | Undervoltage | `f65-2026-e05-undervoltage` |
| **E06** | Overvoltage | `f65-2026-e06-overvoltage` |
| **E3** | Incline adjustment error | `f65-2026-e3-incline-adjustment-error` |
| **E22** | The communication between the upper computer and the lower controller is incorrect | `f65-2026-e22-communication-error` |
| **E31** | Overtemperature | `f65-2026-e31-overtemperature` |

**That is the whole table.** It is printed in the order above, with **E3 between E06 and E22** rather than in numeric order.

**Three codes look alike and are not related.** **E3** is an incline fault, **E03** is a current fault, and **E31** is overtemperature. Each has its own card, and each card names the other two in its first line.

**"Safety key removed, machine stopped" is not in this table**; it is a console message described on page 4. See `f65-2026-safety-key-removed-message`.

The header of this page repeats the diagnosis guide's caveat: *"This list includes common problems that may not be covered under the treadmill's warranty."*
