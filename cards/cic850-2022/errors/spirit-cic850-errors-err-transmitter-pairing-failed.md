---
id: spirit-cic850-errors-err-transmitter-pairing-failed
title: The console shows Err because the speed transmitter pairing failed
kind: troubleshooting
question: What does Err mean on the console of a Spirit CIC850-2022 indoor cycle?
asked_as:
- my spirit cycle console says err
- what does err mean on the cic850
- cic850 wont pair with the speed transmitter
- console shows err instead of 0 when pairing
keywords:
- err
- pairing failed
- speed control pair key
- mode key
- set key
- transmitter
- unpaired
- ten seconds
- console code
facets:
  brand:
  - spirit
  product_line: bike
  model: cic850-2022
  applies_to:
  - cic850-2022
  section: errors
  code: err
authority: 3
not_to_be_confused_with:
- spirit-xic600-errors-id-er-sync-timeout
- sole-spinner-id-er-transmitter-sync-failure
- 70t-2026-errors-err-incline-err
- st90-2023-err-after-pressing-start
- r92-2026-err-no-pulse-input
see_also:
- spirit-indoor-cycle-errors-cadence-jumps-console-code
source:
  ref: spirit-bike-cic850-2022-owners-manual
  locator: PAIRING THE CONSOLE AND TRANSMITTER, PDF pages 17 and 29 (the manual prints
    the block twice)
  extracted_at: '2026-09-09'
---

**`Err` means the pair stage failed, not that a part is broken.**

The manual notes that **all transmitters are paired with the console before shipping**, so
these steps are only needed if the two have been unpaired.

1. Hold **both `MODE` and `SET` keys** on the console for **3 seconds**.
2. On the speed transmitter, press the small **"SPEED CONTROL PAIR KEY"**.
3. The console reads **`0`** once pairing has succeeded.
4. If the console reads **`Err`**, pairing has failed. **Press the `SET` key to repeat the
   steps.**

**If nothing is done for 10 seconds the console leaves pairing mode by itself**, which is the
usual reason `Err` appears at all.

**This is not the XIC600's `ID ER`**, which comes from a different sequence on a console with no
named `MODE` or `SET` key - `spirit-xic600-errors-id-er-sync-timeout`.

**It is also not a Sole `Err`.** Sole treadmills and bikes use `Err` for an incline fault, for a
failed start and for a missing pulse input. Those are different machines with different fixes
and must not be served for this bike.
