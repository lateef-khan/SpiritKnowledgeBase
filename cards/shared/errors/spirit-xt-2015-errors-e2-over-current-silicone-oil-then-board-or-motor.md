---
id: spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor
title: 'E2 over current: check for silicone oil and a blocked belt, then replace the
  lower board or the motor'
kind: troubleshooting
question: What does E2 mean on a Spirit XT 2015 or XT485ENT treadmill, and what does
  the service manual say to do?
asked_as:
- what does e2 mean on my spirit treadmill
- treadmill shows e2 over current
- e2 lower board protection
keywords:
- e2
- over current
- overcurrent
- silicone oil
- lubrication
- block belt
- lower control board
- motor
- protection
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - xt185-2015
  - xt285-2015
  - xt385-2015
  - xt485-2015
  - xt485ent-2023
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller
- f65-2023-e2-over-current
- f65-2026-e01-over-current
see_also:
- spirit-xt-errors-error-code-list-eight-codes
- spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps
- xt485ent-2023-errors-error-code-list-nine-codes
source:
  ref: spirit-treadmill-xt485-2015-service-manual
  locator: 'XT185 2015 service manual Error Message: E2/OVER CURRENT, PDF p. 44, text.md
    lines 729-754; XT285 2015 service manual Error Message: E2/OVER CURRENT, PDF p.
    45 (printed 44), text.md lines 798-823; XT385 2015 service manual Error Message:
    E2/OVER CURRENT, PDF p. 45, text.md lines 666-681; XT485 2015 service manual Error
    Message: E2/OVER CURRENT, PDF p. 45, text.md lines 666-682; XT485ENT 2023 service
    manual 8.3 Error Message: E2/OVER CURRENT, PDF p. 40, text.md lines 553-586'
  extracted_at: '2026-09-11'
---

**This is the 2015 XT and XT485ENT E2 - not the 2023 XT E2, whose books print a longer three-step remedy (`spirit-xt-2023-errors-e2-over-current-lubricate-then-belt-then-controller`), and not E01 on a Sole 2026 treadmill, which is that family's over-current code.**

Section 8.3 (8.2 in the XT285 2015, which numbers its sections one short) is headed `Error Message: E2/OVER CURRENT`.

Definition, as printed: *When lower board detect over current, then LED light up and display appear "E2". The means is lower board need to protect itself and motor. Prevent lower board and motor is burned.* The XT485ENT drops the words `LED light up and`.

Solve over current, as printed: *First, check whether smear Silicone oil or not. And then when during the using treadmill, do not block belt running. If aforementioned did not process problem, suggest Replacing lower control board or Replacing motor.*

So: check the belt has silicone lubricant under it, stop anything from blocking the belt, and only then replace the lower control board or the motor. The book does not say which of the two to try first, where the 2023 books say the controller first. No current figure is printed.

The 2015 XT385 and XT485 give the tripping threshold on their LED page instead: the `LIMIT` LED lights when motor current exceeds **15 A** on the 220 Vac system or **25 A** on the 120 Vac system (`spirit-xt-2015-errors-controller-led-debugging-limit-15-or-25-amps`).
