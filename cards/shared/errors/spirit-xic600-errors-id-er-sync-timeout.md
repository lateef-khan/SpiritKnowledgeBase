---
id: spirit-xic600-errors-id-er-sync-timeout
title: The console shows ID ER because the transmitter was not answered within ten
  seconds
kind: troubleshooting
question: What does ID ER mean on a Spirit indoor cycle console?
asked_as:
- my spirit spin bike says id er
- what does id er mean on an indoor cycle
- spirit cycle wont sync with the transmitter
- console shows id er instead of id 0
keywords:
- id er
- id 0
- id dashes
- synchronize
- transmitter
- speed sensor
- blue button
- ten seconds
- pairing failed
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xic600-2018
  - xic600-2021
  section: errors
  code: error
authority: 3
not_to_be_confused_with:
- spirit-cic850-errors-err-transmitter-pairing-failed
- sole-spinner-id-er-transmitter-sync-failure
see_also:
- spirit-indoor-cycle-errors-cadence-jumps-console-code
- spirit-indoor-cycle-errors-no-display-on-console
source:
  ref: spirit-bike-xic600-2021-owners-manual
  locator: 'XIC600 STEP FIVE, Synchronizing the transmitter to the console, PDF page
    13. The same block is on PDF page 13 of the XIC600 2018 manual, word for word'
  extracted_at: '2026-09-09'
---

**`ID ER` means the synchronising sequence timed out. Nothing has failed.**

The sequence, done after installing the batteries and before attaching the console and
transmitter to the bike:

1. Press and hold **the two keys on the front of the console** for about **3 seconds**, until
   the display shows `ID - -`.
2. Press and hold the **blue button on the transmitter** for **3 seconds**, then release. The
   console should show `ID 0`.

**The blue button must be pressed within 10 seconds of `ID - -` appearing.** Miss that window
and the console shows `ID ER`. Start the procedure again.

If the error keeps coming back, the manual says to **remove and re-install the batteries in
both the console and the transmitter**.

**This is not the CIC850's `Err`.** That console reports a failed pair stage as `Err`, uses
named `MODE` and `SET` keys and a SPEED CONTROL PAIR KEY rather than a blue button, and reports
success as `0` rather than `ID 0` - `spirit-cic850-errors-err-transmitter-pairing-failed`.

**It is also not the Sole `ID ER`.** The Sole SB700 and SB900 indoor cycles print the identical
sequence at `sole-spinner-id-er-transmitter-sync-failure`. Same string, different brand, and a
Sole card must not be served for a Spirit machine.
