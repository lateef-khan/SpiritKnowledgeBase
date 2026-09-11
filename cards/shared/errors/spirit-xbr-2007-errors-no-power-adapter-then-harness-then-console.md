---
id: spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
title: 'No power to the console: 24 volts at the adapter plug, about 6 volts across
  harness pins 2 and 3, then the console'
kind: troubleshooting
question: Why is there no power to the console on a Spirit XBR25-2007 or XBR55-2007
  recumbent bike, and how does the dealer manual test the adapter and harness?
asked_as:
- no power to the console on my old spirit recumbent
- xbr25 console dead how do i test the adapter
- what voltage should the xbr55 power adapter give
- spirit recumbent bike harness voltage test
keywords:
- no power
- adapter
- 24 volts
- harness
- 6 volts
- pin 2
- pin 3
- volt meter
- recumbent
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2007
  - xbr55-2007
  section: errors
  code: no-code
authority: 3
not_to_be_confused_with:
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
- spirit-residential-bike-errors-display-does-not-light-115-vac
see_also:
- spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
source:
  ref: spirit-bike-xbr25-xbr55-2007-service-manual
  locator: XBR25/XBR55 2007 dealer service manual Bike Troubleshooting guide and Procedures
    1-3, PDF p. 3, text.md lines 38-63
  extracted_at: '2026-09-11'
---

**The 2008 dealer manual for the XBR25 and XBR55 prints no error code of any kind.** Its `Bike Troubleshooting` guide is two electronic rows and one mechanical row, each pointing at a numbered procedure; this card is the first row and its two procedures.

`No power - There is no power to the console.`

1. Unit must be plugged into an outlet with power.
2. Test adapter for DC voltage using volt meter. (procedure 1)
3. Remove the console and test the wire harness with a volt meter for DC voltage. (procedure 2)
4. Make sure all wires are plugged into the controller securely.

**Procedure 1 - test adapter for voltage.** Turn the meter to AC voltage. Put the leads in the two holes of the adapter plug. **There should be at least 24 volts.** If there is voltage but no power to the display, go to procedure 2. If there is no voltage, replace the adapter (assuming the outlet has power).

**Procedure 2 - test harness for voltage.** Turn the meter to DC voltage. Remove the console. Put one lead on **pin #2** and the other on **pin #3** of the harness. **There should be around 6 volts.** If there is voltage there but no power to the display, **the console needs to be replaced.**

**The book contradicts itself on the adapter.** Step 2 of the guide calls the adapter reading DC, procedure 1 sets the meter to AC and measures at the plug that goes into the bike. The parts list calls the part `AC Transformer - Adapter` (002107) and the harness `1200mm AC Wire Assembly`, so the adapter output is AC and procedure 1's meter setting is the one to follow; the 6 V on the harness is DC and is measured after the controller has rectified it.

The 2016 books that replaced these machines answer a dead display by checking the computer cable and metering each contact (`spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter`), and the 2016-2023 owner's manuals send a customer to a 115 VAC outlet (`spirit-residential-bike-errors-display-does-not-light-115-vac`). Neither prints the 24 V or 6 V figures; they belong to this book only. The resistance row of the same guide is `spirit-xbr-2007-errors-no-resistance-change-dc-voltage-at-the-controller`.
