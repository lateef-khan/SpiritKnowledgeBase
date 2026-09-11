---
id: spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
title: 'The display won''t come on: check the console-to-computer-cable connection,
  then meter the output voltage at each contact'
kind: troubleshooting
question: What does the service manual say to check when the display will not come
  on at all on a Spirit XBR, XBU, CR800 or CU800 bike?
asked_as:
- spirit bike display wont come on
- recumbent console shows nothing at all
- upright bike screen is dead what do i check first
- no display on my spirit bike
keywords:
- display
- no display
- dead console
- computer cable
- multi-meter
- output voltage
- connection
- bike
- q&a
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - cr800-2009
  - cr800-2021
  - cu800-2021
  - xbr25-2016
  - xbr55-2016
  - xbr55-2023
  - xbr55ent-2021
  - xbr95-2016
  - xbr95-2023
  - xbu55-2016
  section: errors
  code: no-display
authority: 3
not_to_be_confused_with:
- spirit-residential-bike-errors-display-does-not-light-115-vac
- spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
- cu800-2012-errors-no-display-check-the-power-adaptor-dc-connector-and-harnesses
- ab900-2018-errors-console-without-display-check-the-four-batteries
see_also:
- spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet
- spirit-bike-errors-no-pulse-displayed-check-hand-pulse-wiring-then-continuity
- spirit-residential-bike-errors-display-does-not-light-115-vac
- spirit-lcd-dim-or-incomplete
- spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: XBR25 2016 service manual Q&A Console, Display won't come on, PDF p. 69,
    text.md lines 1047-1076; XBR55 2016 service manual Q&A Console, Display won't
    come on, PDF p. 73, text.md lines 1098-1127; XBR95 2016 service manual Q&A Console,
    Display won't come on, PDF p. 71, text.md lines 1054-1071; XBR55ENT 2021 service
    manual Q&A Console, Display won't come on, PDF p. 64, text.md lines 905-934; XBR55
    2023 service manual Q&A Console, Display won't come on, PDF p. 28, text.md lines
    604-636; XBR95 2023 service manual Q&A Console, Display won't come on, PDF p.
    26, text.md lines 537-569; CR800 2009 (XR898) service manual II. Q&A 1. Console,
    Display won't come on, PDF p. 16, text.md lines 449-491; CR800 2020-book (cr800-2021)
    service manual 9-1 Console and Error Messages, The console without display, PDF
    p. 31, text.md lines 442-489; XBU55 2016 service manual 9-11 Console and Error
    Messages, no display, PDF p. 56, text.md lines 856-883; CU800 2020-book (cu800-2021)
    service manual 9-1 Console and Error Messages, When there is no display, PDF p.
    31, text.md lines 464-485
  extracted_at: '2026-09-11'
---

**Ten service manuals answer a dead display with the same two moves, and none of them names a fuse, a breaker or a voltage.**

The recumbent books (XBR25 2016, XBR55 2016, XBR95 2016, XBR55ENT 2021, XBR55 2023, XBR95 2023, CR800 2009 as XR898, CR800 2020-book):

1. Follow procedures below for checking when your display couldn't show anything.
2. Make sure that **Console (19) and computer cable (44)** are connected properly. The XBR95 2016 and the XR898 call it the **9P computer cable** (44).
3. **Use multi-meter to check output voltage at each connect contact.** The CR800 2020-book words it *take measurements of power outputs to find out the problem*.

The upright books (XBU55 2016, CU800 2020-book), in fewer words:

1. Make sure the **console (34) and computer cables (29)** are connected properly.
2. If all are connected properly, **take measurements of power outputs** to find out the problem.

So: reseat the computer cable at the console first; if that is not it, the book stops at "meter it" and prints no figure to meter against. The XBR25/XBR55 2007 dealer manual is the only Spirit bike book that does print figures for this fault - 24 V at the adapter, about 6 V across harness pins 2 and 3 (`spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console`) - and those are figures for that generation's adapter, not these.

**Every one of the ten ends its console Q&A with a remark to the same effect** - the recumbent books word it *Console and related parts were factory tested and it is rare that the unit fails at this part*; the upright books and the CR800 2020-book say the parts were inspected or tested before shipping and the probability of a defect is low.

Two books of the same shape answer differently and have their own cards: the CU800 2012 (XU878) checks the power adaptor and its DC connector before the harnesses and never meters (`cu800-2012-errors-no-display-check-the-power-adaptor-dc-connector-and-harnesses`); the AB900 air bike ends at its four batteries (`ab900-2018-errors-console-without-display-check-the-four-batteries`). The CU900 2018, CR900 2018, CR900ENT, CU1000ENT, CU800ENT and CR800ENT books print no Q&A for a dead display at all.

A customer-facing answer for the residential bikes is the owner's-manual row that ends at a 115 VAC outlet: `spirit-residential-bike-errors-display-does-not-light-115-vac`. A display that is lit but dim is a matrix row, not this one (`spirit-lcd-dim-or-incomplete`).
