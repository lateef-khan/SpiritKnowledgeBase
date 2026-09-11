---
id: air650-2021-errors-heart-rate-value-incorrect-another-strap-interference-or-receiver
title: 'The heart rate value is wrong: another strap nearby, electrical interference,
  or a damaged wireless receiver'
kind: troubleshooting
question: Why is the heart rate reading wrong or erratic on an Xterra air650-2021
  air bike, and what does the service manual say to check?
asked_as:
- air650 heart rate reading wrong
- xterra airbike pulse jumps around
- air650 chest strap reads someone else
- air bike heart rate erratic
keywords:
- heart rate
- incorrect
- erratic pulse
- chest strap
- interference
- electric field
- wireless receiver
- replace receiver
- air bike
facets:
  brand:
  - xterra
  product_line: bike
  model: air650-2021
  applies_to:
  - air650-2021
  section: errors
  code: '*'
  model_number:
  - '165718'
authority: 2
not_to_be_confused_with: []
see_also:
- spirit-erratic-pulse-display
- xterra-treadmill-errors-erratic-pulse-display-chest-belt-interference-receiver
- air650-2021-errors-chest-strap-no-heart-rate-worn-properly-within-3-feet-new-cr2032
source:
  ref: xterra-bike-air650-2021-service-note
  locator: 'AIR650 service note (scan), PDF pp. 1-2, OCR; text.md lines 5-28: ''See
    Spirit AB900 Service Manual'', differences Blue Tooth No, iron-net wind cover,
    connecting-arm cover. The fact itself is in AB900 SM Troubleshooting Quick Lookup
    Table, row 2, PDF p. 31; text.md lines 545-571'
  extracted_at: '2026-09-11'
---

**The AIR650 has no service manual of its own.** The manufacturer's service note for it reads *See Spirit AB900 Service Manual* and lists the only differences: the AIR650 has **no Bluetooth**, no iron-net wind cover and no connecting-arm covers. Everything below is the AB900 book's text, applied to the AIR650 by way of that note.


The book's *Troubleshooting Quick Lookup Table*, second row:

| Happening | Caused | Processing Step |
|---|---|---|
| The heartbeat display value is incorrect | 1. May be receiving another heart rate strap's signal. 2. There may be other electric-field noise interference. 3. The wireless heartbeat receiver is damaged. | 1. Check that there is no other heart rate strap around the machine being used. 2. Try changing the machine's direction or position. 3. Replace the wireless heartbeat receiver. |

The AIR650 reads a chest strap only (its owner's manual sells none with the bike and prints no grip sensor),
so "receiver" is the wireless board in the console. The owner's manual's own list of seven interference
sources - microwaves, fluorescent lights, security systems, pet fences, another transmitter within 3 feet -
is a console-section matter; this row is the service answer that ends in a new receiver. A strap that reads
nothing at all is the next row
(`air650-2021-errors-chest-strap-no-heart-rate-worn-properly-within-3-feet-new-cr2032`).

The Spirit card for this row across the commercial range is `spirit-erratic-pulse-display`; the Xterra
treadmill matrix prints it as `xterra-treadmill-errors-erratic-pulse-display-chest-belt-interference-receiver`.

