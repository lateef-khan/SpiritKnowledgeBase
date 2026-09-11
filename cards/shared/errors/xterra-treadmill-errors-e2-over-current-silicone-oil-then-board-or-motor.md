---
id: xterra-treadmill-errors-e2-over-current-silicone-oil-then-board-or-motor
title: 'E2 over current: check for silicone oil and a blocked belt first, then replace
  the lower control board or the motor'
kind: troubleshooting
question: What does E2 mean on an Xterra tr150-2021, tr260-2023, trx1400-2023, trx2500-2024,
  trx3500-2024, trx4500-2024 or trx5500-2024 treadmill according to the service manual,
  and what is the fix?
asked_as:
- e2 over current xterra treadmill
- treadmill shows e2 and stops
- e2 lower board protecting itself
keywords:
- e2
- over current
- overload
- lower board
- silicone oil
- lubricate
- belt blocked
- replace controller
- replace motor
- youtube
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - tr260-2023
  - trx1400-2023
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  - trx5500-2024
  section: errors
  code: e2
authority: 3
not_to_be_confused_with:
- xterra-tr-errors-e2-incline-position-error
- xterra-ws-errors-e02-power-assault-power-tube
- f63-2023-e2-error-code
- f85-2019-e2-over-current
see_also:
- xterra-treadmill-errors-e2-over-current-owner-checks-belt-lube-bearing-motor
- xterra-treadmill-errors-e2-over-rated-current-for-3-seconds
- trx1400-2023-errors-e2-overload-over-rated-current-for-6-seconds
- spirit-xt-2015-errors-e2-over-current-silicone-oil-then-board-or-motor
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: 'TRX2500 SM 8.3 Error Message: E2, PDF p. 46 (printed 45); text.md lines
    762-787; TR150 SM 8.3 Error Message: E2/OVER CURRENT, PDF p. 40; text.md lines
    602-613; TR260 SM 8-5 Error Message: E2/OVER CURRENT, PDF p. 38; text.md lines
    563-578; TRX1400 SM 8.3 Error Message: E2/OVER CURRENT, PDF p. 45 (printed 44);
    text.md lines 732-757; TRX3500/TRX4500 SM 8.3 Error Message: E2/OVER CURRENT,
    PDF p. 51 (printed 50); text.md lines 807-832; TRX5500 SM 7-5 Error Message: E2
    / OVER CURRENT, PDF p. 44 (printed 43); text.md lines 653-670'
  extracted_at: '2026-09-11'
---

**This is E2 as the Dyaco service manuals define it: over current on the lower board.** On the TR6.6 and TR6.4 an E2 is an incline position error (`xterra-tr-errors-e2-incline-position-error`).

*Definition.* When the lower board detects over current, its LED lights up (the TR150 book omits the LED) and the display shows "E2". The lower board is protecting itself and the motor, to prevent the lower board and motor being burned. The code tables word it "Over current, over limit current of lower controller and motor" (TR150, TRX1400) or "Treadmill motor is overload" (the others).

*Solve over current.* First, check whether silicone oil has been applied. Then, while the treadmill is in use, do not block the belt running. If that does not fix the problem, the books suggest **replacing the lower control board or replacing the motor.** That is the whole procedure; no current figure and no meter test is printed.

The TRX5500 book adds a linked reference video: `https://www.youtube.com/watch?v=KTiXDfndj-Y`.

The owner's manuals give the same code a checklist of belt alignment, lubrication, bearing damage and motor overheating (`xterra-treadmill-errors-e2-over-current-owner-checks-belt-lube-bearing-motor`) or a trip time of 3 or 6 seconds (`xterra-treadmill-errors-e2-over-rated-current-for-3-seconds`, `trx1400-2023-errors-e2-overload-over-rated-current-for-6-seconds`). The TR260 check list adds bearing wear, an overheated circuit and a stuck incline (`tr260-2023-errors-err-code-troubleshooting-check-list`).
