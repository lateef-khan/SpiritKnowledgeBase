---
id: tr260-2023-errors-tft-not-bright-check-120-v
title: 'The TFT is dim, incomplete or imperfect: a broken backlight, or console power
  too low, checked against 120V'
kind: troubleshooting
question: Why is the TFT display dim or incomplete on an Xterra tr260-2023 treadmill,
  and what should I check?
asked_as:
- display dim on my xterra treadmill
- console screen incomplete
- treadmill display missing segments
keywords:
- tft
- not bright
- incomplete
- backlight
- power to console
- replace console
- lower controller
- 120v
- matrix
facets:
  brand:
  - xterra
  product_line: treadmill
  model: tr260-2023
  applies_to:
  - tr260-2023
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-lcd-not-bright-check-110-v-or-230-v
- xterra-trx-errors-lcd-not-bright-check-220-v
see_also:
- xterra-treadmill-errors-power-switch-not-lit-nine-causes
- xterra-treadmill-errors-e7-input-power-too-low-too-high-or-unstable
- spirit-xt-errors-lcd-not-bright-connector-then-power
source:
  ref: xterra-treadmill-tr260-2023-service-manual
  locator: TR260 SM 8-13 Troubleshooting procedure matrix, PDF pp. 51-53; text.md
    lines 794-900
  extracted_at: '2026-09-11'
---

The troubleshooting procedure matrix prints two rows for the display:

*Condition:* TFTs not bright, incomplete or imperfect.

| Reason | Solve |
|---|---|
| 1. TFT light is broken | 1. Replace with new TFT or console |
| 2. Power to console too low | 2. Check AC power is **120V**. 3. Check power to console. 4. Replace lower controller |

*Condition:* TFT displays not bright, incomplete or imperfect. *Reason:* 1. TFT displays are broken. *Solve:* 1. Replace with new console.

The voltage figure follows the book: 110V or 230V in the TR150 and TRX1400 books, 120V in the TR260 book (which calls the display a TFT), 220V in the TRX2500 and TRX3500/TRX4500 books. Those last books draw both 120 V and 220 V circuit diagrams, so check against the supply the machine is built for. A console that is completely dark is a different row (`xterra-treadmill-errors-power-switch-not-lit-nine-causes` and the no-display-with-key cards).
