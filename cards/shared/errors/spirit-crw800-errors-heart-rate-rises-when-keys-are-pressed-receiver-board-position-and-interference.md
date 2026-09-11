---
id: spirit-crw800-errors-heart-rate-rises-when-keys-are-pressed-receiver-board-position-and-interference
title: 'The heart rate jumps up when a key is pressed, keeps climbing, or the strap
  only reads close up: the receiving board position, keypad sound and interference'
kind: troubleshooting
question: Why does the heart rate on a Spirit CRW800 or XRW600 rower rise when I press
  a key, keep increasing, or only read when the strap is very close?
asked_as:
- rower heart rate goes up when i press buttons
- crw800 pulse keeps climbing on its own
- xrw600 chest strap only works right next to the console
keywords:
- heart rate increases
- keypad
- receiving board
- interference
- fluorescent lamp
- wireless receiver
- short range
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - xrw600-2019
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- crw800-2024-errors-wireless-heartbeat-reception-too-short
- crw800-2024-errors-heartbeat-value-incorrect
- crw800-2024-errors-rf-handheld-board-problem
- spirit-erratic-pulse-display
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: CRW800 2021 service manual 7-7-2, PDF p. 38 (printed 37), text.md lines
    584-589; CRW800 2016 (CW800-YR001) service manual 8.7 Wireless heartbeat problem,
    second list, PDF p. 39, text.md lines 536-540; XRW600 (DW400-YR002) service manual
    8.7 Wireless heart rate receive problem, second list, PDF p. 39, text.md lines
    519-523
  extracted_at: '2026-09-11'
---

Three symptoms share one heading in all three books - **Press the keypad heart rate unexpected increase / Heart rate always increasing / Wireless receiving distance is short** - and one four-item list:

> A. Check that the receiving board is in the correct position.
> B. To confirm whether the keypad sound is too loud caused.
> C. Disturbed wireless heartbeat near the source of interference. (Such as fluorescent lamp rectifier, cable interference power, etc.)
> D. Replace the wireless heartbeat receiver module.

**Item B is the one no other Spirit troubleshooting row prints: the console's own key beep can disturb the heart rate receiver.** A reading that jumps every time a key is pressed is the beep, not the user. The book does not say how to quiet it; the same books' engineering mode has no beep switch, so the remedy is the position of the receiving board (item A) or the receiver itself (item D).

**"Receiving board in the correct position" is a physical check.** The wireless receiver is a small board inside the console; if it has been fitted the wrong way round or left loose after a console repair, range shrinks and readings drift. The quick-lookup table of the same books reduces the short-range symptom to a low strap battery (`crw800-2024-errors-wireless-heartbeat-reception-too-short`); this list is the next thing to try when a new battery has not fixed it.

A reading that is *wrong* rather than rising is the table's own row (`crw800-2024-errors-heartbeat-value-incorrect`); a strap that reads nothing is `crw800-2024-errors-wireless-heartbeat-has-no-effect`.
