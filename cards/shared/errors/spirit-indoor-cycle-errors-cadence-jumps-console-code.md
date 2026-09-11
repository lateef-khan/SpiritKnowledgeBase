---
id: spirit-indoor-cycle-errors-cadence-jumps-console-code
title: Cadence jumps high or low because two bikes share one console code
kind: troubleshooting
question: Why does the cadence reading jump around on a Spirit indoor cycle?
asked_as:
- my spirit spin bike rpm jumps around
- cadence goes crazy on my indoor cycle
- two spirit cycles showing each others numbers
- rpm wild on spirit bike console
keywords:
- cadence
- rpm
- jumps
- cross-talking
- console code
- re-synchronize
- pair
- transmitter
- rf interference
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cic850-2022
  - xic600-2018
  - xic600-2021
  section: errors
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- spirit-xic600-errors-id-er-sync-timeout
- spirit-cic850-errors-err-transmitter-pairing-failed
- sole-spinner-cadence-jumps-resynchronise
source:
  ref: spirit-bike-xic600-2021-owners-manual
  locator: TROUBLESHOOTING, Cadence number jumps high or low. XIC600 2021 and XIC600
    2018 PDF page 24; CIC850 2022 PDF page 35; CIC850 2022 service manual 6. Troubleshooting
    page, the same five entries as the owner's manual, PDF p. 20 (printed 19), text.md
    lines 288-313
  extracted_at: '2026-09-09'
---

1. **Two bikes are set to the same console code and are cross-talking.** Separate them, or
   pair the transmitter to its own console again.
2. **Move the bike to a different part of the room**, away from any RF interference areas.

**"Console code" is the manual's own phrase for the transmitter identity**, not a fault code.
Nothing is broken; two consoles are listening to one transmitter.

**The re-pairing step is not the same on the two consoles**, so send the caller to the right one:

- **XIC600 (2018 and 2021)** - re-synchronise the transmitter and console. Hold the two keys on
  the front of the console until it shows `ID - -`, then hold the transmitter's blue button
  within ten seconds; success is `ID 0`. Printed page 5 of the manual, and
  `spirit-xic600-errors-id-er-sync-timeout` for what happens when it times out.
- **CIC850 (2022)** - run the transmitter pair stage again: hold `MODE` and `SET` together on
  the console for three seconds, then press the SPEED CONTROL PAIR KEY on the transmitter.
  Success is `0`, failure is `Err`. See
  `spirit-cic850-errors-err-transmitter-pairing-failed`.

The Sole SB700 and SB900 indoor cycles carry this entry too, split across
`sole-spinner-cadence-jumps-resynchronise` and `sole-spinner-cadence-jumps`. Different brand,
separate cards.

**The CIC850 2022 service manual reprints this entry word for word** on its own `Troubleshooting` page, and adds a `Common problems` chapter behind it with a five-check blank-display page (`cic850-2022-errors-display-blank-or-no-speed-five-checks`) and a noise page (`cic850-2022-errors-noise-brake-block-gap-1-5-mm-or-worn-pedals`).
