---
id: xterra-tr-errors-e1-jkexer-no-speed-signal-or-current-limit
title: 'E1 on the JKEXER console: no speed signal about 6 or 7 seconds after start,
  or the current limit has shut the machine down until it cools'
kind: troubleshooting
question: What does E1 mean on an Xterra tr75h-2025 or tr95h-2024 treadmill, and what
  should I check?
asked_as:
- e1 on my tr95h
- tr75h e1 after a few seconds
- treadmill shuts down with e1 then works again later
keywords:
- e1
- speed signal
- speed sensor
- 3 to 6 mm
- 6 seconds
- 7 seconds
- current limit
- lubricant
- driver motor
- driver board
facets:
  brand:
  - xterra
  product_line: treadmill
  model: '*'
  applies_to:
  - tr75h-2025
  - tr95h-2024
  section: errors
  code: e1
authority: 3
not_to_be_confused_with:
- xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration
- xterra-tr-errors-e1-console-memory-or-cpu-fault
- xterra-treadmill-errors-e2-over-current-silicone-oil-then-board-or-motor
see_also:
- xterra-tr-errors-jkexer-error-messages-e1-e3-e6-and-dashes
- xterra-tr-errors-e3-jkexer-poor-communication-upper-lower-controller
- xterra-tr-errors-e6-jkexer-incline-vr-value-did-not-change
source:
  ref: xterra-treadmill-tr95h-2024-service-manual
  locator: TR95H SM 11. Explanation and troubleshooting of error messages, PDF pp.
    16-17; text.md lines 209-258; TR75H SM 12. Explanation and troubleshooting of
    error messages, PDF pp. 16-17; text.md lines 346-421; TR95H OM Troubleshooting,
    PDF p. 53 (printed 52); text.md lines 1920-1939; TR75H OM Troubleshooting, PDF
    p. 49 (printed 48); text.md lines 1845-1864
  extracted_at: '2026-09-11'
---

**This is E1 on the JKEXER-built TR75H and TR95H.** The Dyaco-built Xterra treadmills raise E1 only during calibration with an 8-second form and a 3 mm gap (`xterra-treadmill-errors-e1-no-rpm-signal-only-in-calibration`); the TR6.6 and TR6.4 use E1 for a memory fault.

*Owner's manual:* E1 (Error 1): when the machine starts but the computer could not read the signal from the sensor for **7 seconds**, E1 is shown. If this happens, consult the distributor.

*Service manual* - two causes, three scenarios:

**Cause I - the console does not receive the speed signal.**

- *Scenario 1:* the console displays E1 after no operation of the driver motor for about **6 seconds**. Check: (a) the driver motor's connection cable is connected correctly; (b) driver board or driver motor failure - replace.
- *Scenario 2:* the console displays E1 about 6 seconds after the driver motor operates. Check: (a) the speed sensor cable is connected correctly; (b) whether the speed sensor is faulty; (c) whether the distance between the speed sensor and the magnet is within **3~6 mm**.

**Cause II - current limit protection.**

- *Scenario 3:* after operating for some time the console displays E1 and shuts down; after being shut down for some time the treadmill can be used again. Check: (a) add lubricant between the running deck and running belt; (b) motor failure - replace.

The owner's manual says 7 seconds and the service manual about 6; both are printed. The sensor gap here is 3~6 mm where the Dyaco books say under 3 mm. The driver board's *current limit indicator light* (item 6 on its parts callout) is the hardware side of Cause II; the callout gives it no further meaning.
