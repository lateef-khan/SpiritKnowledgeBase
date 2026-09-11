---
id: crw800-2024-errors-wireless-heartbeat-reception-too-short
title: The strap only reads very close to the console, and the single cause is a low
  battery
kind: troubleshooting
question: Why does the chest strap on a Spirit CRW800 or XRW600 rower only read when
  it is very close to the console?
asked_as:
- my rower only picks up my heart rate when i lean forward
- chest strap range is tiny on my spirit rower
- heart rate cuts out unless im close to the console
keywords:
- wireless heartbeat
- short range
- reception
- weak battery
- cr2032
- lithium battery
- chest strap
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
- crw800-2024-errors-wireless-heartbeat-has-no-effect
- spirit-wireless-chest-belt-no-pulse
see_also:
- crw800-2024-errors-wireless-heartbeat-has-no-effect
- spirit-wireless-chest-belt-no-pulse
- spirit-crw800-errors-heart-rate-rises-when-keys-are-pressed-receiver-board-position-and-interference
source:
  ref: spirit-rower-crw800-2024-owners-manual
  locator: TROUBLESHOOTING, Happening / Caused / Processing Step table on printed
    page 32. That page is a flat picture with no text layer and was read from the
    rendered page; CRW800 2016 (CW800-YR001) service manual 8.5 Troubleshooting Quick
    Lookup Table, PDF p. 38-39, text.md lines 487-519; XRW600 (DW400-YR002) service
    manual 8.5 Troubleshooting Quick Lookup Table, PDF p. 38-39, text.md lines 478-505;
    CRW800 2021 (800940) service manual 7-5 Troubleshooting Quick Lookup Table, PDF
    p. 37 (printed 36), text.md lines 536-561
  extracted_at: '2026-09-10'
---

The condition is printed as `Wireless heartbeat reception is too short (must be very close to the
console)`.

| Caused | Processing Step |
|---|---|
| The battery is low | Please replace the new lithium battery type **CR2032** |

**One cause and one part.** The manual offers no alternative - not the receiver, not the position of
the machine - so a strap whose range has shrunk is a battery until a new CR2032 proves otherwise.

**The 3 foot range this row is measured against is printed in the row above it**, which is the one
for a strap that reads nothing at all
(`crw800-2024-errors-wireless-heartbeat-has-no-effect`). Neither row repeats the other's figure, so
a reader who lands on this one is not told what the range is supposed to be.

Ten of the other 2024 manuals print the same fact as `Chest belt too close to the [machine]. Weak
battery.` (`spirit-wireless-chest-belt-no-pulse`) - the same battery, the same single cause, the
opposite way round in the wording.

**The three rower service manuals - CRW800 2016 (`CW800-YR001`), CRW800 2021 (`800940`) and XRW600 (`DW400-YR002`) - print this row word for word**: one cause, the battery, one part, the CR2032. Each also prints a list headed *Wireless receiving distance is short* alongside two other symptoms, whose answers are the receiving board's position, the keypad beep and nearby interference (`spirit-crw800-errors-heart-rate-rises-when-keys-are-pressed-receiver-board-position-and-interference`) - the checks to make when a new cell has not restored the range.
