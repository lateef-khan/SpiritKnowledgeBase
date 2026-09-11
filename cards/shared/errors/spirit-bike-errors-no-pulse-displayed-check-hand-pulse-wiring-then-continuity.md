---
id: spirit-bike-errors-no-pulse-displayed-check-hand-pulse-wiring-then-continuity
title: 'No pulse displayed: the hand pulse wire at the console, the grip sensors to
  their wires, the join behind the rear shroud, then a continuity test'
kind: troubleshooting
question: Why do the handgrip sensors show no pulse on a Spirit XBR, XBU, CR800, CU800
  or 4.0U bike, and what does the service manual say to check?
asked_as:
- no pulse showing on my spirit bike grips
- hand pulse not reading on the recumbent
- heart rate blank when holding the handlebars
- how do i check the hand pulse wiring on a spirit bike
keywords:
- no pulse
- hand pulse
- handgrip sensor
- hand pulse wire
- continuity
- rear shroud
- console
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
  code: no-pulse
authority: 3
not_to_be_confused_with:
- spirit-hand-pulse-not-working
- spirit-wireless-chest-belt-no-pulse
see_also:
- spirit-hand-pulse-not-working
- spirit-erratic-pulse-display
- spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet
source:
  ref: spirit-bike-xbr55-2023-service-manual
  locator: XBR25 2016 service manual Q&A Console, No pulse displayed, PDF p. 69, text.md
    lines 1047-1076; XBR55 2016 service manual Q&A Console, No pulse displayed, PDF
    p. 73, text.md lines 1098-1127; XBR95 2016 service manual Q&A Console, No pulse
    displayed, PDF p. 72, text.md lines 1071-1093; XBR55ENT 2021 service manual Q&A
    Console, No pulse displayed, PDF p. 64, text.md lines 905-934; XBR55 2023 service
    manual Q&A Console, No pulse displayed, PDF p. 28, text.md lines 604-636; XBR95
    2023 service manual Q&A Console, No pulse displayed, PDF p. 26, text.md lines
    537-569; CR800 2009 (XR898) service manual II. Q&A 1. Console, No pulse displayed,
    PDF p. 16, text.md lines 449-491; CR800 2020-book (cr800-2021) service manual
    9-1, No heart rate is displayed, PDF p. 31, text.md lines 442-489; XBU55 2016
    service manual 9-11, the second "No heart rate is displayed" entry, PDF p. 56,
    text.md lines 856-883; CU800 2020-book (cu800-2021) service manual 9-1, "No heart
    rate is displayed" steps 3-4, PDF p. 31, text.md lines 464-485; 4.0U (FU800-SB022-03)
    service manual 10. Q&A, Console and Error Messages Problem, PDF p. 47 (printed
    44), text.md lines 633-662, "No heart rate is displayed"
  extracted_at: '2026-09-11'
---

**Ten service manuals answer a blank pulse reading by walking the hand pulse wiring from the console to the grips, and end with a continuity test.** The matrix row for the same symptom (`spirit-hand-pulse-not-working`) lists four causes; this is the Q&A procedure that finds which one.

The XBR25 2016, XBR55 2016, XBR55ENT 2021, XBR55 2023 and XBR95 2023:

1. When the console displays but is without heart beat, check if **Hand Pulse Sensor Assembly W/Cable (45)** is properly connected to **Console assembly (19)**, or if **Handpulse W/Cable Assemblies (21, 27)** are properly connected with **Hand Pulse Sensor Assembly W/Cables (26)**.
2. If there is no problem with installation, dismantle **Rear Shroud (L) (35)** and check if Handpulse W/Cable Assemblies (26) are properly installed with Hand Pulse Sensor Assembly W/Cable (45).
3. If all are connected properly, **use multi meter to check cable continuity.**

The XBR95 2016 and the CR800 2009 (XR898) print the same three steps with the parts called **Handpulse Wire (133)** at the console, **Hand pulse Sensor (27)** to **Handpulse Wires (26)**, and the check behind the left rear shroud. The CR800 2020-book uses `(26.42)` for the wire pair and ends *check all connection with instrument with probe and replace if necessary*.

The upright books are shorter. XBU55 2016: *check if handpulse sensor cable is properly connected to the console (34), and if handpulse assemblies cables are properly connected with sensor wires* - one step, no continuity test. CU800 2020-book: the same, then *check Hand pulse Assembly (26)(28). Replace the wire cable if necessary.*

**Both upright books print this under a heading that also covers speed** - the XBU55 2016 prints `No heart rate is displayed` twice and only the second is pulse; the CU800 2020-book puts speed in steps 1-2 and pulse in steps 3-4 of one entry. See `spirit-bike-errors-no-speed-readout-hall-sensor-or-magnet-test-with-another-magnet`.

Every book closes the console Q&A with the same remark: the console and related parts were factory tested and rarely fail. A pulse that reads but jumps is `spirit-erratic-pulse-display`; a chest belt that reads nothing is `spirit-wireless-chest-belt-no-pulse`.

**The 4.0U 2025 medical upright prints the CU800 upright two steps under a heading of its own**, `No heart rate is displayed` - the hand pulse sensor cable at the console and the hand pulse assemblies to their sensor wires, then *check Hand pulse Assembly, replace the wire cable if necessary* - and the same closing remark that the parts were inspected before shipping (added 2026-09-11).

