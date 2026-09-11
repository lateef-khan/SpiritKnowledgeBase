---
id: crw800-2024-errors-wireless-heartbeat-has-no-effect
title: The wireless strap shows no heartbeat at all, and the battery is a CR2032 within
  3 feet
kind: troubleshooting
question: Why does the wireless chest strap show no heart rate on a Spirit CRW800
  or XRW600 rower?
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
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - crw800-2024
  - xrw600-2019
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
- spirit-crw800-errors-heart-rate-rises-when-keys-are-pressed-receiver-board-position-and-interference
- sr500-2016-wireless-heart-rate-no-reading
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING, Happening / Caused / Processing Step table on printed
    page 32. That page is a flat picture with no text layer and was read from the
    rendered page; CRW800 2016 (CW800-YR001) service manual 8.5 Troubleshooting Quick
    Lookup Table, PDF p. 38-39, text.md lines 487-519; XRW600 (DW400-YR002) service
    manual 8.5 Troubleshooting Quick Lookup Table, PDF p. 38-39, text.md lines 478-505;
    CRW800 2021 (800940) service manual 7-5 Troubleshooting Quick Lookup Table, PDF
    p. 37 (printed 36), text.md lines 536-561; CRW800 2021 7-7-1 No display of heart
    rate, PDF p. 38 (printed 37), text.md lines 576-582; CRW800 2016 8.7, PDF p. 39,
    text.md lines 529-535; XRW600 8.7, PDF p. 39, text.md lines 512-518
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

## The three rower service manuals print this row word for word, and add a five-item list

The CRW800 2016 (`CW800-YR001`), CRW800 2021 (`800940`) and XRW600 (`DW400-YR002`) service manuals all print the row above - same three causes, `3 feet`, `CR2032` - and then, under **No display of heart rate**:

> A. Make sure that the heart rate strap is worn in place.
> B. Make sure that the battery power of the heart rate strap is sufficient.
> C. Whether the range of the wireless heartbeat has been exceeded.
> D. Check whether the wireless heartbeat module is in the correct position.
> E. Replace the wireless heartbeat receiver module.

**Items D and E are what the table does not say**: the receiver module inside the console can be out of position, and it can be replaced. A strap that has a fresh cell, sits right and is within range, and still reads nothing, is the receiver. The same books' next list - a reading that rises when a key is pressed - is `spirit-crw800-errors-heart-rate-rises-when-keys-are-pressed-receiver-board-position-and-interference`. Sole's SR500 2016 prints both (`sr500-2016-wireless-heart-rate-no-reading`).
