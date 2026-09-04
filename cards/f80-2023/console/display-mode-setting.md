---
id: f80-2023-display-mode-setting
title: Display mode setting
kind: spec
question: What does the Display Mode setting do on a Sole f80-2023 treadmill?
asked_as:
- what is display mode on my treadmill
- treadmill screen turns off when i pull the safety key
- console powers down after 30 minutes
keywords:
- display mode
- safety key
- power down
- 30 minutes
- inactivity
- engineering mode
- machine information
- wake
facets:
  brand:
  - sole
  product_line: treadmill
  model: f80-2023
  applies_to:
  - f80-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- f80-2023-sleep-mode
- f80-2023-engineering-mode
- sole-sleep-mode-touchscreen
source:
  ref: sole-tm-f80-2023-service-manual
  locator: Section 8.10 item 2 Machine Information, page 50
  extracted_at: '2026-09-04'
---

**Display Mode. Default: ON. Setting: ON/OFF.** It lives in Machine Information inside engineering mode
and governs the sleeping mode function and the SAFETY KEY display behaviour.

- **ON**: the console does **not** power down when the user removes the SAFETY KEY.
- **OFF**: the console powers down when the SAFETY KEY is removed, and the display turns off to power the console
  down automatically after **30 minutes of inactivity**.
- Any key wakes the console.

**This overlaps the Sleep Mode switch in Settings**, which defaults to OFF, uses the opposite polarity, and gives
**15 minutes** as its automatic timer. Both are printed in this manual. Check both before telling a customer why
the screen does or does not sleep.
