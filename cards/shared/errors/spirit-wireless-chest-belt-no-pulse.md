---
id: spirit-wireless-chest-belt-no-pulse
title: The wireless chest belt shows no pulse
kind: troubleshooting
question: Why is the wireless chest belt not reading on a Spirit CE800ENT, CT850,
  CU900ENT or CVC800?
asked_as:
- chest strap not reading on my spirit machine
- wireless heart rate not working
- what battery does the chest belt take
keywords:
- chest belt
- chest strap
- wireless
- no pulse
- cr2032
- battery
- receiver
- telemetry
facets:
  brand:
  - spirit
  product_line: '*'
  model: '*'
  applies_to:
  - ce800ent
  - ct850-2016
  - ct850-2020
  - cu900ent
  - cvc800
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-erratic-pulse-display
- spirit-hand-pulse-not-working
- ce800ent-bluetooth-chest-strap-no-heart-rate
- crw800h2o-console-shows-no-pulse-data
source:
  ref: spirit-elliptical-ce800ent-service-manual
  locator: 'Troubleshooting procedure matrix: CE800ENT section 7-3 page 27; CT850
    2016 section 8.3 pages 49-52; CT850 2020 section 8-7 pages 47-51; CU900ENT page
    39; CVC800 section 8-5 page 34'
  extracted_at: '2026-09-08'
---

Five Spirit commercial manuals print this row and all five give the same three causes and the same
three fixes. The condition is printed as
`Wireless lost its function. (No pulse displayed on monitor)`.

| Reason | Solve |
|---|---|
| Chest belt not worn properly | Check chest belt has proper contact with skin and is oriented correctly |
| Distance is too far and exceeds range of receiver | User chest belt in front of console within 3 feet |
| Chest belt battery is weak or dead | Replace with new lithium battery type is CR2032 |

The battery is a **CR2032** lithium cell. Working range is **within 3 feet** of the console.

A second row with the same answer follows it in the CT850 2016, CT850 2020, CU900ENT and CVC800
manuals - `Chest belt too close to the [machine]. Weak battery. Replace with new lithium battery
with type CR2032.` **The CE800ENT manual does not print that second row**, and prints instead a
Bluetooth chest strap row the other four do not have: `ce800ent-bluetooth-chest-strap-no-heart-rate`.

The CRW800H2O rower answers this question differently again - it asks for a 5.0 kHz belt worn
correctly, and names no battery: `crw800h2o-console-shows-no-pulse-data`.

A jumpy rather than absent reading is `spirit-erratic-pulse-display`.
