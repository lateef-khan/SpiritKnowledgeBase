---
id: ct850-2016-incline-interface-board-sections-are-missing
title: The incline interface board sections listed in the contents are not in the
  manual
kind: fact
question: Where are the incline interface board PCB and LED indicator locations for
  a Spirit CT850-2016 treadmill?
asked_as:
- where are the leds on the ct850 incline board
- incline interface board layout 2016 ct850
- section 6.3 missing from the ct850 manual
- up and down lights on the incline board location
keywords:
- incline interface board
- led indicator
- missing section
- table of contents
- component locations
- incline board
- gap
- not printed
- inverter
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850-2016
  applies_to:
  - ct850-2016
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with: []
see_also:
- ct850-2016-inverter-board-connector-locations
- ct850-2016-inverter-board-connector-pinouts
- ct850-2016-incline-err-test-procedure
- ct850-2020-driver-board-connector-locations
source:
  ref: spirit-treadmill-ct850-2016-service-manual
  locator: Table of contents p. 2 (printed 1) lists 6.3-6.6; the body runs 6.1 on
    p. 23 (printed 22) to 6.2 on p. 25 (printed 24), and p. 26 (printed 25) is section
    7
  extracted_at: '2026-09-08'
---

Sections **6.3, 6.4, 6.5 and 6.6 are listed in the table of contents but are not in the manual.**
They are:

- 6.3 INCLINE INTERFACE BOARD PCB Component Locations
- 6.4 Inverter LED Indicator Locations
- 6.5 INCLINE INTERFACE BOARD LED Indicator Locations
- 6.6 Controller Indicator LED debugging

Section 6 runs from its title page on p. 22 to p. 25. p. 23 is 6.1 PCB Board Top, p. 24 is the
PCB Board Bottom connector map, p. 25 is 6.2 Inverter PCB Component Locations, and p. 26 is
already section 7, Product Safety Instructions. Nothing between them was dropped by the text
extraction: p. 23 is the only flattened-image page in that range and it is 6.1.

So this manual gives you **no incline interface board component map and no LED indicator
locations at all**. What it does give, elsewhere:

- The inverter's own connector map, including CN13 (incline VR) and CN6 (incline power), is in
  6.2 on p. 25, with pin definitions on p. 42.
- The incline board's UP and DOWN indicator LEDs appear only as unlabelled circles on the
  INCLINE ERR configuration drawings on pp. 36 and 44, and in the test procedure on p. 43, which
  tells you to watch "the Up/down lights on the incline board" without saying where they are.

Do not fill the gap from the 2020 CT850 manual: that machine uses a different driver
(RM6T6-1003, YT058) with a different board layout.
