---
id: xterra-trx-errors-popping-sound-at-power-on-check-220-v
title: 'A popping sound after power-on: the varistor on the controller has blown from
  incorrect input power, so check the supply is 220V and replace the controller'
kind: troubleshooting
question: Why does an Xterra trx2500-2024, trx3500-2024 or trx4500-2024 treadmill
  make a popping sound after it is switched on?
asked_as:
- treadmill pops when turned on
- popping noise from the controller xterra
- varistor blown treadmill
keywords:
- popping sound
- power on
- varistor
- incorrect input power
- replace controller
- 220v
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - trx2500-2024
  - trx3500-2024
  - trx4500-2024
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-popping-sound-at-power-on-check-110-v-or-230-v
- tr260-2023-errors-popping-sound-at-power-on-check-120-v
see_also:
- xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
- xterra-treadmill-errors-power-switch-not-lit-nine-causes
- spirit-xt-errors-popping-sound-at-power-on-220-v-or-110-v
source:
  ref: xterra-treadmill-trx2500-2024-service-manual
  locator: TRX2500 SM 8.11 Troubleshooting procedure matrix, PDF pp. 60-63 (printed
    59-62); text.md lines 1058-1198; TRX3500/TRX4500 SM 8.11 Troubleshooting procedure
    matrix, PDF pp. 68-71 (printed 67-70); text.md lines 1106-1246
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints one line for this:

*Condition:* After turning on power, treadmill has a popping sound. *Reason:* 1. Incorrect input power; varistor is blown (broken) on controller. *Solve:* 1. Check the voltage of power is **220V**. Replace controller.

The voltage the books say to check differs by book: **110V or 230V** in the TR150 and TRX1400 service manuals, **120V** in the TR260 book, **220V** in the TRX2500 and TRX3500/TRX4500 books. Those last books also draw both a 120 V and a 220 V circuit diagram, so the figure is the book's, not necessarily the machine's - check against the supply the machine is built for. The TR260 check list names the same part: "Make sure fuse is OK and varistor is free from damaging" (`tr260-2023-errors-err-code-troubleshooting-check-list`). The E7 input-power code covers an unstable supply that has not yet blown anything (`xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable`).
