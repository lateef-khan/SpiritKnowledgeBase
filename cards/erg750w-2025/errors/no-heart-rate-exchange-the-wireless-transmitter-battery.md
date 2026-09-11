---
id: erg750w-2025-errors-no-heart-rate-exchange-the-wireless-transmitter-battery
title: 'No heart rate is bad detection from the wireless transmitter: exchange the
  transmitter''s battery and test again'
kind: troubleshooting
question: Why is there no heart rate on the console of an Xterra erg750w-2025 water
  rower, according to the service manual?
asked_as:
- xterra water rower no heart rate
- erg750w chest strap not detected
- rower transmitter battery
- heart rate blank on my xterra rower
keywords:
- no heart rate
- wireless transmitter
- chest strap
- transmitter battery
- bad detection
- bluetooth heart rate
- water rower
facets:
  brand:
  - xterra
  product_line: rower
  model: erg750w-2025
  applies_to:
  - erg750w-2025
  section: errors
  code: '*'
  model_number:
  - '175926'
authority: 3
not_to_be_confused_with:
- erg550w-2023-errors-console-cannot-get-pulse-data-5-0-khz-chest-belt
- erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032
see_also:
- erg750w-2025-errors-no-action-or-dim-lcd-power-failure-batteries-and-battery-case-wires
- erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032
- erg550w-2023-errors-console-cannot-get-pulse-data-5-0-khz-chest-belt
source:
  ref: xterra-rower-erg750w-2025-service-manual
  locator: ERG-750W SM "TZ-8145-2AA Trouble Shooting" table (Problem / Possible cause
    / Things to Check / Solution), PDF p. 26, text.md lines 360-391; the page was
    also read from a 110 dpi render because the text layer interleaves the columns;
    ERG750W OM CONSOLE FUNCTIONS, PULSE paragraph (Bluetooth heart rate monitor, 90-second
    scan, wake on any button), PDF p. 18 (printed 17), lines 548-581
  extracted_at: '2026-09-11'
---

The *No heart rate* row of the console troubleshooting table (the console is named by its part number, TZ-8145-2AA):

| Possible cause | Things to check | Solution |
|---|---|---|
| Bad detection from wireless transmitter | Exchange the battery of the wireless transmitter | Test again |

One cause and one remedy, and the book names neither the battery type nor a working range. **This console pairs its heart rate monitor over Bluetooth**, the owner's manual says - the heartbeat scan turns off after 90 seconds if no Bluetooth heartbeat is found and any button wakes it - so the first thing to rule out is a scan that has simply timed out: press a button, then change the transmitter's battery if the number still does not come.

That makes this rower's strap answer different from its siblings'. The ERG550W wants a 5.0 kHz analogue belt (`erg550w-2023-errors-console-cannot-get-pulse-data-5-0-khz-chest-belt`), and the ERG700 prints a CR2032 cell and a 3-foot range (`erg700-2022-errors-wireless-heartbeat-no-effect-strap-worn-within-3-feet-cr2032`). Neither figure is printed for this machine.
