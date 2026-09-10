---
id: spirit-jb950-errors-limit-sensor-test-after-motor-error
title: The limit sensor test that is run only after a motor error, and the fifteen
  minute memory wait
kind: procedure
question: How do I test the resistance motor's limit sensor on a Spirit JB950-2022
  Johnny G bike after a motor error?
asked_as:
- johnny g bike motor error what do i check
- how do i test the limit sensor on a jb950
- resistance motor fault on my spirit johnny g bike
- s1 s2 sensor test on the johnny g bike
keywords:
- limit sensor
- home sensor
- motor error
- s1
- s2
- encoder count
- flag
- brake test
- maintenance mode
- resistance motor
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: errors
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-jb950-errors-update-fail-or-search-update
- spirit-commercial-bike-errors-no-error-codes-printed
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: MAINTENANCE MODE, LIMIT SENSOR, PDF page 56. MOTOR TEST MANUAL and the
    encoder/limit sensor readings are on PDF page 55
  extracted_at: '2026-09-09'
---

**The manual says this test is performed only when a motor error has occurred.** It is the one
fault-driven check in the whole book, and it is the nearest thing the JB950 has to a diagnostic
for the resistance system.

It tests that the **flag moves properly between the home sensor (`S1`) and the limit sensor
(`S2`)**.

1. Reach it inside Maintenance Mode - hold `+`, `-` and `Play` on the forward control pad for 3
   seconds, then scroll with `+` to `LIMIT SENSOR`.
2. At rest the screen reads **`S1 OFF`, `S2 OFF`**, and the bottom number is the **encoder wheel
   count (`0`)**.
3. Use the **`+` and `-` keys to drive the motor** and try to change `S1` to `ON`. Pedalling
   resistance should change as the keys are pressed.
4. **If `S1` goes `ON`, stop pedalling immediately.** Let the console power down and **leave the
   bike standing for a minimum of 15 minutes** so the memory clears before riding it again.
5. `EXIT` returns to the setting screen.

The **`LIMIT SENSOR CONDITION`** figure shown in the upper right of MOTOR TEST MANUAL, on the
previous page, reads: **`1` = HOME, `2` = ACTIVE RANGE, `3` = END**.

**No error code goes with this.** The JB950 console prints no fault code and the manual has no
troubleshooting chapter - `spirit-commercial-bike-errors-no-error-codes-printed`. A caller
reporting a "motor error" on this bike is describing a symptom, not quoting a code.

Brake Test, Motor Test Auto and the rest of Maintenance Mode are console settings rather than
fault work and are carded under `section: console`.
