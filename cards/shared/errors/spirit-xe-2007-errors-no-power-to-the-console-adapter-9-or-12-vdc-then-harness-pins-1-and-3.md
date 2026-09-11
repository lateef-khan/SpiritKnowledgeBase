---
id: spirit-xe-2007-errors-no-power-to-the-console-adapter-9-or-12-vdc-then-harness-pins-1-and-3
title: 'No power to the console: a few volts above the 9 VDC or 12 VDC on the adapter
  label, the same reading across harness pins 1 and 3, then the harness is replaced'
kind: troubleshooting
question: Why is there no power to the console on a Spirit XE100-2007, XE200-2007,
  XE300-2007, XE400-2007 or XE500-2007 elliptical, and how does the dealer manual
  test the adapter and harness?
asked_as:
- no power to the console on my spirit xe300
- elliptical console dead how to test the adapter
- xe200 display wont come on
- test the wire harness on a spirit elliptical
keywords:
- no power
- console
- adapter
- 9vdc
- 12vdc
- wire harness
- pin 1
- pin 3
- volt meter
- elliptical
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - xe100-2007
  - xe200-2007
  - xe300-2007
  - xe400-2007
  - xe500-2007
  section: errors
  code: no-power
authority: 3
not_to_be_confused_with:
- spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
see_also:
- spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console
- spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers
- spirit-xe-2007-errors-no-resistance-change-5k-ohm-potentiometer-then-gear-motor-4-to-6-volts
source:
  ref: spirit-elliptical-xe100-xe200-xe300-xe400-xe500-2007-service-manual
  locator: XE100-XE500 2007 dealer service manual Troubleshooting Guide, ELECTRONIC
    SYSTEM, PDF p. 3, text.md lines 51-98; XE100-XE500 2007 dealer service manual
    Repair Procedures, PROCEDURE 1 and PROCEDURE 2, PDF p. 5, text.md lines 136-170
  extracted_at: '2026-09-11'
---

**The 2008 dealer manual for the XE100 to XE500 prints no error code of any kind.** Its `Troubleshooting Guide` is four electronic rows and five mechanical rows, each pointing at a numbered procedure; this card is the first row and its two procedures.

`No power to the console`
1. Unit must be plugged into an outlet with power.
2. Test adapter for voltage with a volt meter. (Procedure 1)
3. Disconnect console, test harness for voltage. (Procedure 2)

**Procedure 1 - test adapter for voltage.** Plug the adapter into a working outlet. Turn the meter on to test for DC voltage. Put one lead into the end of the plug and the other lead to the metal on the outside. **The adapter will be labeled 9VDC or 12VDC. When testing, the reading should be a few volts higher than the label says.** If there is less voltage than what the label says, replace the adapter.

**Procedure 2 - test harness for power supply voltage.** After testing the adapter, plug in the machine and take the console off. Turn the meter on to test for DC voltage. Put one lead on the **1st wire** and the other on the **3rd wire** - *the triangle always points to pin #1*. **You should have basically the same voltage here as at the adapter. If the reading is vastly different, the harness needs to be replaced.**

**The book stops at the harness.** It does not say what to replace when the harness reads correctly and the console is still dark; the XBR25/XBR55 2007 bike book of the same year, which prints the same two-step test with its own figures, does say *the console needs to be replaced* (`spirit-xbr-2007-errors-no-power-adapter-then-harness-then-console`). The parts lists name the adapter as a **1.5 Amp adaptor (000137)** on the XE100 and XE200 and a **9V, 2.0 A adaptor (000138)** on the XE300; the XE400 and XE500 have a power cord and an incline transformer as well.

The 2016 residential books that replaced these machines trace wires and connectors and measure nothing (`spirit-xe-2016-errors-no-display-power-adaptor-connectors-then-covers`, `spirit-ce850-2016-errors-no-display-ac-adapter-wires-adapter-fuse-then-covers`).
