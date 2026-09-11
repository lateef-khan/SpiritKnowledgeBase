---
id: cu800-2012-errors-no-display-check-the-power-adaptor-dc-connector-and-harnesses
title: 'No display: the power adaptor and its DC connector first, then every harness,
  opening the console if you must'
kind: troubleshooting
question: What does the service manual say to check when there is no display on a
  Spirit cu800-2012 upright bike?
asked_as:
- no display on my 2012 spirit cu800
- xu878 console is dead
- spirit upright bike screen blank check adaptor
- cu800 power adaptor connected but no display
keywords:
- no display
- power adaptor
- dc connector
- harness
- computer cable
- console
- upright bike
- q&a
facets:
  brand:
  - spirit
  product_line: bike
  model: cu800-2012
  applies_to:
  - cu800-2012
  section: errors
  code: no-display
  model_number:
  - '800343'
authority: 3
not_to_be_confused_with:
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
- ce900-2025-errors-eeprom-error-replace-upper-controller
see_also:
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
- spirit-2024-errors-leds-not-bright-generator-power-connection
- cu800-2012-errors-no-resistance-check-the-brake-coil-harness
source:
  ref: spirit-bike-cu800-2012-service-manual
  locator: CU800 2012 (XU878) service manual 8-9 Console and Error Messages, PDF p.
    47, text.md lines 742-765
  extracted_at: '2026-09-11'
---

Section 8-9, `Console and Error Messages`, in full:

1. Follow the steps below in case there is no display.
2. Make sure **power adaptor has been plug in and DC connector is connected properly** to the unit.
3. Make sure **all wire harness including computer cables are connected properly.** Disassembling the console, if necessary, to determine if there are broken harness or improper connection of connectors.

**Two things set this apart from the later CU800 and CR800 books.** It starts at the **power adaptor** - the XU878 is the one CU800 generation in the repository whose console is fed from an adaptor and DC jack rather than from the generator, which is why its Q&A checks the adaptor and the CU800 2020-book's does not (`spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter`). And it never says to meter anything: the later books end at *take measurements of power outputs*; this one ends at looking for a broken harness.

The book's only error message is `EEPROM ERROR`, which blanks every window and is a different fault with a different fix: `ce900-2025-errors-eeprom-error-replace-upper-controller`. Its matrix row for a display that is lit but dim sends you to the generator power connection: `spirit-2024-errors-leds-not-bright-generator-power-connection`.
