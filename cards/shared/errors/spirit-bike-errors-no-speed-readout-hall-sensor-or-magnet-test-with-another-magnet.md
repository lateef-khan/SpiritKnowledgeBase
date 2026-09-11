---
id: spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet
title: 'No speed readout: the sensor cable connection, then the hall or reed sensor
  or its magnet, tested by holding another magnet to it'
kind: troubleshooting
question: Why does the display show no speed or RPM on a Spirit XBR, XBU, CR800, CU800
  or 4.0U bike, and how does the service manual test the speed sensor?
asked_as:
- spirit bike shows no speed while pedalling
- rpm stays at zero on my recumbent
- how do i test the speed sensor on a spirit upright bike
- no speed readout xbr55
keywords:
- no speed
- no rpm
- speed sensor
- hall sensor
- reed switch
- magnet
- computer cable
- bike
- q&a
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - 40u-2025
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
  code: no-speed
authority: 3
not_to_be_confused_with:
- ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm
- cic850-2022-errors-display-blank-or-no-speed-five-checks
see_also:
- spirit-bike-errors-display-wont-come-on-check-computer-cable-then-meter
- spirit-bike-errors-no-pulse-displayed-check-hand-pulse-wiring-then-continuity
- ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: XBR25 2016 service manual Q&A Console, No speed readout, PDF p. 69, text.md
    lines 1047-1076; XBR55 2016 service manual Q&A Console, No speed readout, PDF
    p. 73, text.md lines 1098-1127; XBR95 2016 service manual Q&A Console, No speed
    readout, PDF p. 72, text.md lines 1071-1093; XBR55ENT 2021 service manual Q&A
    Console, No speed readout, PDF p. 64, text.md lines 905-934; XBR55 2023 service
    manual Q&A Console, No speed readout, PDF p. 28, text.md lines 604-636; XBR95
    2023 service manual Q&A Console, No speed readout, PDF p. 26, text.md lines 537-569;
    CR800 2009 (XR898) service manual II. Q&A 1. Console, No speed readout, PDF p.
    16, text.md lines 449-491; CR800 2020-book (cr800-2021) service manual 9-1, No
    speed rate is displayed, PDF p. 31, text.md lines 442-489; XBU55 2016 service
    manual 9-11, the first "No heart rate is displayed" entry, which is the speed
    entry, PDF p. 56, text.md lines 856-883; CU800 2020-book (cu800-2021) service
    manual 9-1, "No heart rate is displayed" steps 1-2, which are the speed entry,
    PDF p. 31, text.md lines 464-485; 4.0U (FU800-SB022-03) service manual 10. Q&A,
    Console and Error Messages Problem, PDF p. 47 (printed 44), text.md lines 633-662,
    "Display won't show RPM"
  extracted_at: '2026-09-11'
---

**Ten service manuals give the same two-step answer, and the test in step 2 is the useful part: hold another magnet to the sensor.**

The recumbent books (XBR25 2016, XBR55 2016, XBR95 2016, XBR55ENT 2021, XBR55 2023, XBR95 2023, CR800 2009 as XR898):

1. If the display is on but without speed readout, disassemble **Front Shroud (29)** and make sure **9P computer cable (44) and Hall Sensor (46)** are properly connected.
2. If there is no problem with the connection, there is problem with either **Hall Sensor (46) or the magnet (56)**. **Use another magnet to test Hall Sensor (46)**, replace it when necessary.

The CR800 2020-book says the same with the sensor called `Sensor W/Cable (46)` and `Magnet (56)`, and adds that *either Sensor W/Cable (46) or Magnet (56) requires replacement*.

The upright books (XBU55 2016, CU800 2020-book) open **Chain Cover (36)** instead and name a **Reed Switch (23)** - the `400mm Sensor W/Cable (23)` - and **Magnet (22)**; the test is the same, another magnet held to the sensor, and *either Sensor W/Cable (23) or Magnet (22) requires replacement*.

**On the two upright books this entry is printed under the wrong heading.** The XBU55 2016 prints `Q: No heart rate is displayed:` twice in a row; the first answer is this speed entry (*The Console is displaying but without speed showing...*) and only the second is about heart rate. The CU800 2020-book merges the two under one `Q: No heart rate is displayed` heading, steps 1-2 being speed and steps 3-4 pulse. Read the answers, not the headings.

**The same fault on the AB900 air bike carries a figure the others do not**: a sensor-to-magnet gap of less than 3 mm (`ab900-2018-errors-no-speed-reading-magnet-gap-under-3-mm`). The CU900 and CU1000ENT parts chapters set their reed switch **1 mm** from the magnet on reassembly; that is a replacement figure, not a Q&A one, and it is not printed in any of the ten books here.

The battery-powered indoor cycles answer the same symptom differently again - batteries, transmitter and its position: `cic850-2022-errors-display-blank-or-no-speed-five-checks`.

**The 4.0U 2025 medical upright prints the same two moves under its own heading, `Display won't show RPM`**: remove the Chain Cover (L) and recheck the *9 PIN Hall Sensor cable* is installed correctly; if that does not fix it, *it should be the sensor or magnet problem, so try to replace these parts*. **It does not print the other-magnet test** (added 2026-09-11).

