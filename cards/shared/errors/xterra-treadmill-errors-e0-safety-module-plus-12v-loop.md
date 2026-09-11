---
id: xterra-treadmill-errors-e0-safety-module-plus-12v-loop
title: 'E0: the safety key is not closing the +12 V safety switch loop through the
  main control wires'
kind: troubleshooting
question: What does E0 mean on an Xterra tr150-2021 or trx1400-2023 treadmill, and
  what does the service manual say to check?
asked_as:
- e0 on my xterra treadmill with the key in
- e0 safety module
- treadmill shows e0 when key is inserted
keywords:
- e0
- safety key
- safety module
- safety switch loop
- 12v
- main control wire
- display board
- multi-meter
- short circuit
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - trx1400-2023
  section: errors
  code: e0
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e0-safety-key-device-buzzer-test
- xterra-ws-errors-e07-safety-lock-not-in-place
- f63-2023-e0-error-code
see_also:
- xterra-treadmill-errors-e0-safety-switch-malfunction-owner-checks
- xterra-treadmill-errors-e0-safety-key-device-buzzer-test
- xterra-treadmill-errors-service-manual-error-code-tables-by-book
- spirit-xt-errors-e0-safety-key-loop
source:
  ref: xterra-treadmill-trx1400-2023-service-manual
  locator: 'TRX1400 SM 8.1 Error message: E0, PDF p. 38 (printed 36); text.md lines
    591-624; TR150 SM 8.1 Error message: E0, PDF p. 33; text.md lines 461-494'
  extracted_at: '2026-09-11'
---

**This is E0 on the two books that describe a safety *module* and a +12 V loop.** The TR260, TRX2500, TRX3500, TRX4500 and TRX5500 books describe the same code as a missing safety-device signal with a buzzer test - `xterra-treadmill-errors-e0-safety-key-device-buzzer-test`.

*Definition.* The console is not inserted safety, or safety module may be broken, or else a component of the upper control board or lower controller is broken.

*Configuration.* The lower controller sends a **+12 V signal through the S/W line of the main control wires** to the console; the safety module and safety key close that line into a safety switch loop.

*Cause.* The console is not inserted the safety key, so the console cannot form the +12 V loop and the display shows E0. But possibly the main control wires or components of the lower controller are broken, because the +12 V has to travel over the main control wires to reach the upper control board.

*Troubleshooting*

| Part | What to do |
|---|---|
| Safety module | Insert the safety key, then use a multi-meter switched to the short-circuit (continuity) position to check whether the safety module wires are short or not |
| Main control wire | Reinsert the main control wires. Replace the main control wire |
| Display board | Replace the upper control board |

The owner's manuals for these machines print the same code as "Safety Switch Malfunction" with three questions; see `xterra-treadmill-errors-e0-safety-switch-malfunction-owner-checks`. The matrix rows for a console that stays dark with the key in, or that runs without the key, are `xterra-treadmill-errors-no-display-when-safety-key-inserted-5-pin-main-control-wires` and `xterra-treadmill-errors-runs-without-safety-key-safety-device-shorted`.
