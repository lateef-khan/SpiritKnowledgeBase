---
id: csc900-2019-errors-error-code-table
title: 'Every code the alternator-drive climbmill can show: four codes on a twelve-row
  matrix'
kind: spec
question: What error codes can a Spirit csc900-2019 stair climber display and what
  does each one mean?
asked_as:
- list of error codes for the csc900 climbmill
- spirit stair climber er codes
- what codes does the alternator climbmill show
keywords:
- error code
- error code table
- list
- index
- climbmill
- stair climber
- alternator
- four codes
facets:
  brand:
  - spirit
  product_line: climber
  model: csc900-2019
  applies_to:
  - csc900-2019
  section: errors
  code: '*'
  model_number:
  - '900669'
authority: 3
not_to_be_confused_with:
- csc900-2024-errors-error-code-table
- csc880-2025-errors-error-code-table
see_also:
- csc900-2019-errors-er07-safety-switch-connector
- csc900-2019-errors-er11-lower-control-not-receiving-console-data
- csc900-2019-errors-er12-console-not-receiving-controller-data
- csc900-2019-errors-er22-speed-out-of-control-alternator
- csc900-2019-errors-speed-and-distance-stay-at-zero-magnetic-safety-switch
- csc900-2019-errors-speed-buttons-change-the-display-not-the-speed-blue-feedback-wire
- csc900-2019-errors-button-failure-membrane-key-or-handrail-button
- csc900-2019-errors-no-power-and-no-beep-adapter-indicator-first
- csc900-2019-errors-countdown-normal-no-code-and-no-motion-power-failure-brake
- csc900-2019-errors-incorrect-pedal-position-when-stopping-stopper
- csc900-2019-errors-abnormal-sound-four-sources
- csc900-2019-errors-holding-the-heartbeat-grips-does-nothing-seat-cable
- csc900-2019-errors-communication-line-continuity-test
- csc900-2019-errors-power-off-brake-24-volt-snap-test
- csc900-2019-errors-magnetic-safety-switch-magnet-and-buzzer-test
- csc900-2019-errors-brake-resistor-reads-about-half-an-ohm
source:
  ref: spirit-climber-csc900-2019-service-manual
  locator: 6. Troubleshooting & parts replacement matrix, rows 1-12, PDF p. 9-10;
    text.md lines 289-369
  extracted_at: '2026-09-11'
---

**This book is the alternator-drive CSC900 (the `V1.0` service manual, March 2020 PDF), not the 2022 magnetic-system book that the CSC900 2024 cards rest on.** The CSC900 2019 *owner's* manual prints no codes at all; this table comes from the service manual, which prints four codes inside a twelve-row Issues / Analysis / Method matrix. **They are written `ER` and two digits.**

| Code | Issue as printed | What it means |
|---|---|---|
| ER11 | When you press start, the countdown is normal, but the machine doesn't work | The lower control panel doesn't receive the data sent by the console |
| ER12 | Countdown normal, machine doesn't work, and it cannot be stopped except by pulling the emergency switch | Console cannot receive the controller data |
| ER22 | When you press start, the speed is out of control | Abnormal alternator - its wire, the brake resistor wire, or the alternator or resistor itself |
| ER07 | Out of order, the machine doesn't work | Safety switch connector loose and fallen off, or safety switch failure |

**The other eight rows carry no code.** They are symptom rows - speed and distance stuck at zero, speed keys that change the display and not the steps, dead buttons, no power and no beep, a normal countdown with no motion and no code, wrong pedal position at stop, abnormal sound, and grips that read no heartbeat - and each has its own card (linked below).

## Three books, three code sets

| Fault | This book (alternator, V1.0) | CSC900 2022 magnetic book | CSC880 2025 |
|---|---|---|---|
| Lower board not receiving console data | **ER11** | **ER11** | ER03 |
| Console not receiving controller data | **ER12** | **ER12** | ER01 |
| Emergency stop switch or its connector | **ER07** | **ER07** | ER07 |
| Speed out of control - alternator or resistor | **ER22** | not printed | not printed |
| Magnet wheel wiring or shorted MOS | not printed | ER02 | folded into ER04 |
| Controller over-current | not printed | ER05 | ER04 |

**The alternator book and the magnetic book agree on ER07, ER11 and ER12 and disagree on everything else**, because the machines are built differently: this one holds its speed with an alternator and a power resistor, the 2022 machine with a magnetic wheel. An `ER22` belongs only here; an `ER02` or `ER05` belongs only to the magnetic book (`csc900-2024-errors-error-code-table`). Establish which CSC900 the caller has - the alternator machine's book is `V1.0`, the magnetic one's says *2022 (Magnetic system)* on its cover - before reading a code back.

The four component tests printed after the matrix - communication line continuity, the brake's 24 V snap, the magnetic safety switch with a magnet, and the resistor at about 0.5 ohms - are each carded separately and linked below.
