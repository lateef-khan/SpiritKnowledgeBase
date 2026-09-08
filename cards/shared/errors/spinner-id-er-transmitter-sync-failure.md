---
id: sole-spinner-id-er-transmitter-sync-failure
title: The console shows ID ER when synchronising the speed transmitter
kind: troubleshooting
question: My Sole indoor cycle console shows ID ER while pairing the transmitter.
  What does that mean?
asked_as:
- my sole spin bike says id er
- sole indoor cycle wont pair with the transmitter
- what does id er mean on my spin bike
keywords:
- id er
- id 0
- synchronize
- transmitter
- speed sensor
- blue button
- 10 seconds
- batteries
- pairing
facets:
  brand:
  - sole
  product_line: bike
  model: '*'
  applies_to:
  - sb700-2011
  - sb700-2016
  - sb700-2019
  - sb700-2020
  - sb700-2021
  - sb900-2014
  - sb900-2016
  - sb900-2019
  - sb900-2020
  - sb900-2021
  - sb900-2022
  section: errors
  code: error
authority: 3
not_to_be_confused_with: []
see_also:
- sole-spinner-speed-sensor-pairing
- sole-spinner-cadence-jumps-resynchronise
source:
  ref: sole-bike-sb700-2011-2016-owners-manual
  locator: Synchronizing the transmitter to the console. The same block is in the
    SB700 2019, 2020 and 2021 owner's manuals and the SB900 2014-2016, 2019, 2020
    and 2021 owner's manuals.
  extracted_at: '2026-09-08'
---

**`ID ER` means the synchronising sequence timed out, not that a part has failed.**

The sequence, done after installing batteries and before attaching the console and transmitter to the bike:

1. Press and hold the **two keys on the front of the console** for about **3 seconds**, until the display shows `ID - -`.
2. Press and hold the **blue button on the transmitter** for **3 seconds**, then release. The console display should show `ID 0`.

**You must press the blue button within 10 seconds of the console showing `ID - -`.** If you do not, the console shows `ID ER`. If it shows that error, restart the procedure.

If you keep getting the error, the manual says it may be necessary to **remove and re-install the batteries in both the console and the transmitter**.

**This is not the `Err` of the speed pair stage.** The later consoles pair with a MODE and PAGE key sequence and report failure as `Err`, with `0` for success. This older console reports `ID 0` for success and `ID ER` for failure.
