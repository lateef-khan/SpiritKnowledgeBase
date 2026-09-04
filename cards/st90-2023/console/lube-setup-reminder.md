---
id: st90-2023-lube-setup-reminder
title: The lube deck reminder
kind: fact
question: What is the lube reminder on a Sole ST90-2023 treadmill and how do I clear
  it?
asked_as:
- my treadmill says lube deck
- how do i reset the lube message on my st90
- lube setup hours on the treadmill
keywords:
- lube setup
- lube deck
- reminder
- 90 hours
- reset
- zeroing
- stop key
- engineering mode
facets:
  brand:
  - sole
  product_line: treadmill
  model: st90-2023
  applies_to:
  - st90-2023
  section: console
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- st90-2023-engineering-mode-entry
- sole-lubricate-running-belt
- st90-2023-belt-hesitates-when-stepped-on
source:
  ref: sole-tm-st90-2023-service-manual
  locator: Section 8.2 Lube Setup, page 26
  extracted_at: '2026-09-04'
---

**Lube Setup** reminds the user to lubricate the deck.

| Field | Value |
|---|---|
| Default | 90 hours |
| Range | 90 to 200 hours |
| Message | `LUBE DECK PRESS STOP TO RESET LUBE MESSAGE` |

**What happens.** Power the machine on with the total hours at or past the setting and the message shows for about 3 seconds, then closes and the display goes to idle mode. The total using hour appears at the top right of the display.

**Clearing it.** Press **STOP** while the message is showing. Or open Lube Setup and hit **Zeroing**; the display asks "Are you sure the lube parameter needs to be reset?" and Yes resets the total using hour.

**The total hours and distance are not cleared** when the message closes on its own or when you press STOP. They keep accumulating, and the message returns at the next multiple of the setting.

If you hit Zeroing before the hours reach the setting, the accumulated using hour resets to zero anyway.

**The earlier ST90 console had a belt check reminder here instead**, defaulting to off with a range of 100 to 1000 hours.
