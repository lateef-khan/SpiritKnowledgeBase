---
id: spirit-crw800-errors-count-not-shown-or-no-display-check-board-34-and-the-three-cables
title: 'The stroke count does not show, or the console shows nothing: the optical
  coupler board and then the DC cord, gear motor and computer cable'
kind: troubleshooting
question: Why does the console on a Spirit CRW800 or XRW600 rower not show the count,
  or show nothing at all?
asked_as:
- rower console not counting strokes
- crw800 screen shows nothing
- xrw600 console dead what cables to check
- rower display cycles through screens by itself
keywords:
- count times
- no display
- optical coupler board
- board 34
- dc power cord
- gear motor
- computer cable
- sequence of displays
- rower
facets:
  brand:
  - spirit
  product_line: rower
  model: '*'
  applies_to:
  - crw800-2016
  - crw800-2021
  - xrw600-2019
  section: errors
  code: no-display
authority: 3
not_to_be_confused_with: []
see_also:
- crw800-2024-errors-lcd-display-does-not-shine
- crw800-2021-errors-lcd-display-does-not-shine-check-the-battery-and-the-generator
- crw800-2024-errors-light-sensor-problem
- sr550-2023-count-times-not-shown
- sr500-2016-console-display-sequence-fault
- sr500-2016-console-no-display
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: CRW800 2021 service manual 12-1 The Console Display troubleshooting, PDF
    p. 64 (printed 63), text.md lines 964-972; CRW800 2016 (CW800-YR001) service manual
    9-10 Message on Console, PDF p. 65, text.md lines 757-766; XRW600 (DW400-YR002)
    service manual 9-11 Message on Console, PDF p. 64, text.md lines 745-754
  extracted_at: '2026-09-11'
---

Two questions from the Q&A chapter, printed in all three books with the same part numbers.

**Q: Count Times doesn't show in display** (the 2021 book) / **With a sequence of displays** (the 2016 and XRW600 books).
**A:** Please check the connections with optical coupler Board (34) or the connection of all wires. If not, please replace.

**Q: The console doesn't display** / **No displays.**
**A:** Please check the connection with 750m/m DC Power Cord (39), Gear Motor (35), and 500m/m Computer Cable (Upper) (44).

**Board (34) is the optical coupler - the stroke sensor** - and its number is the exploded-view item, so the parts list will find it. The two older books describe the first symptom as the console cycling through a sequence of displays; the 2021 book describes it as the count not appearing. Same board, same answer.

**Three cables for a blank console, one of which is the gear motor's.** The 750 mm DC power cord (39), the gear motor (35) and the upper computer cable (44) are all named because on these rowers the tensioner (gear motor) and its cable are part of the console's supply path - the LCD row says the tensioner should be putting out DC12V (`crw800-2024-errors-lcd-display-does-not-shine`). The 2021 generator-powered book prints the same three part numbers unchanged, DC power cord included.

The four-step check for the optical sensor itself is the quick-lookup table's light sensor row (`crw800-2024-errors-light-sensor-problem`). Sole prints this Q&A for its own rowers: `sr550-2023-count-times-not-shown`, `sr500-2016-console-display-sequence-fault`, `sr500-2016-console-no-display`.
