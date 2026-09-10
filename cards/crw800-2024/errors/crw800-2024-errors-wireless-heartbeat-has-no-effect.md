---
id: crw800-2024-errors-wireless-heartbeat-has-no-effect
title: The wireless strap shows no heartbeat at all, and the battery is a CR2032 within 3 feet
kind: troubleshooting
question: Why does the wireless chest strap show no heart rate on a Spirit CRW800-2024
  rower?
asked_as:
- chest strap not reading on my rowing machine
- no heart rate from my strap on a spirit rower
- what battery does the rower chest strap take
keywords:
- wireless heartbeat
- chest strap
- heart rate strap
- cr2032
- battery
- 3 feet
- receiver
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2024
  applies_to:
  - crw800-2024
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-wireless-chest-belt-no-pulse
- crw800-2024-errors-wireless-heartbeat-reception-too-short
see_also:
- spirit-wireless-chest-belt-no-pulse
- crw800-2024-errors-wireless-heartbeat-reception-too-short
- crw800h2o-console-shows-no-pulse-data
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING, Happening / Caused / Processing Step table on printed page
    32. That page is a flat picture with no text layer and was read from the rendered
    page.
  extracted_at: '2026-09-10'
---

The condition is printed as `Wireless heartbeat has no effect (The heartbeat value is not displayed
on the monitor)`.

| Caused | Processing Step |
|---|---|
| The Heart rate strap is not properly worn | Check that the Heart rate strap is in proper contact with the skin and in the right direction |
| The distance is too far above the receiver | Keep the chest strap within **3 feet** of the console |
| The battery of heart rate strap is low or has no voltage | Please replace the new lithium battery type **CR2032** |

**Both figures match every other Spirit machine** - a **CR2032** cell and a **3 foot** working range
(`spirit-wireless-chest-belt-no-pulse`). Only the wording differs: this book says *heart rate strap*
where the others say *chest belt*, and *the distance is too far above the receiver* where the others
say *exceeds range of receiver*.

**A strap that reads only when it is very close to the console is the next row down**, and it has a
single cause: `crw800-2024-errors-wireless-heartbeat-reception-too-short`.

A strap that reads the *wrong* number rather than no number is a different row again:
`crw800-2024-errors-heartbeat-value-incorrect`.
