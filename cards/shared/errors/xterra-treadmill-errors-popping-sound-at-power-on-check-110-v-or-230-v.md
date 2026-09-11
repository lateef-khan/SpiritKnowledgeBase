---
id: xterra-treadmill-errors-popping-sound-at-power-on-check-110-v-or-230-v
title: 'A popping sound after power-on: the varistor on the controller has blown from
  incorrect input power, so check the supply is 110V or 230V and replace the controller'
kind: troubleshooting
question: Why does an Xterra tr150-2021 or trx1400-2023 treadmill make a popping sound
  after it is switched on?
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
- 110v-or-230v
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr150-2021
  - trx1400-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- tr260-2023-errors-popping-sound-at-power-on-check-120-v
- xterra-trx-errors-popping-sound-at-power-on-check-220-v
see_also:
- xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
- xterra-treadmill-errors-power-switch-not-lit-nine-causes
- spirit-xt-2015-errors-popping-sound-at-power-on-110-v-or-230-v
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM 8.11 Troubleshooting procedure matrix, PDF pp. 49-50 (printed
    57-58); text.md lines 826-906; TRX1400 SM Troubleshooting procedure matrix, PDF
    pp. 61-63 (printed 55-57); text.md lines 1102-1208
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints one line for this:

*Condition:* After turning on power, treadmill has a popping sound. *Reason:* 1. Incorrect input power; varistor is blown (broken) on controller. *Solve:* 1. Check the voltage of power is **110V or 230V**. Replace controller.

The voltage the books say to check differs by book: **110V or 230V** in the TR150 and TRX1400 service manuals, **120V** in the TR260 book, **220V** in the TRX2500 and TRX3500/TRX4500 books. Those last books also draw both a 120 V and a 220 V circuit diagram, so the figure is the book's, not necessarily the machine's - check against the supply the machine is built for. The TR260 check list names the same part: "Make sure fuse is OK and varistor is free from damaging" (`tr260-2023-errors-err-code-troubleshooting-check-list`). The E7 input-power code covers an unstable supply that has not yet blown anything (`xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable`).
