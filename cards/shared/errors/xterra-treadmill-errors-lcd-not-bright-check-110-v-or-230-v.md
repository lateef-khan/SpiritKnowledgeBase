---
id: xterra-treadmill-errors-lcd-not-bright-check-110-v-or-230-v
title: 'The LCD is dim, incomplete or imperfect: a broken backlight, or console power
  too low, checked against 110V or 230V'
kind: troubleshooting
question: Why is the LCD display dim or incomplete on an Xterra tr150-2021 or trx1400-2023
  treadmill, and what should I check?
asked_as:
- display dim on my xterra treadmill
- console screen incomplete
- treadmill display missing segments
keywords:
- lcd
- not bright
- incomplete
- backlight
- power to console
- replace console
- lower controller
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
- tr260-2023-errors-tft-not-bright-check-120-v
- xterra-trx-errors-lcd-not-bright-check-220-v
see_also:
- xterra-treadmill-errors-power-switch-not-lit-nine-causes
- xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
- spirit-xt-2015-errors-lcd-not-bright-110-v-or-230-v
source:
  ref: xterra-treadmill-tr150-2021-service-manual
  locator: TR150 SM 8.11 Troubleshooting procedure matrix, PDF pp. 49-50 (printed
    57-58); text.md lines 826-906; TRX1400 SM Troubleshooting procedure matrix, PDF
    pp. 61-63 (printed 55-57); text.md lines 1102-1208
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints two rows for the display:

*Condition:* LCDs not bright, incomplete or imperfect.

| Reason | Solve |
|---|---|
| 1. LCD light is broken | 1. Replace with new LCD or console |
| 2. Power to console too low | 2. Check AC power is **110V or 230V**. 3. Check power to console. 4. Replace lower controller |

*Condition:* LCD displays not bright, incomplete or imperfect. *Reason:* 1. LCD displays are broken. *Solve:* 1. Replace with new console.

The voltage figure follows the book: 110V or 230V in the TR150 and TRX1400 books, 120V in the TR260 book (which calls the display a TFT), 220V in the TRX2500 and TRX3500/TRX4500 books. Those last books draw both 120 V and 220 V circuit diagrams, so check against the supply the machine is built for. A console that is completely dark is a different row (`xterra-treadmill-errors-power-switch-not-lit-nine-causes` and the no-display-with-key cards).
