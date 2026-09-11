---
id: erg700-2022-errors-lcd-does-not-shine-backlight-or-console-power-ac-100-240-v-dc-12-v
title: 'The LCD does not shine or is incomplete: a damaged backlight, or console power
  too low, checked at AC 100-240 V in and DC 12 V out'
kind: troubleshooting
question: Why is the display dim, blank or partly lit on an Xterra erg700-2022 rower?
asked_as:
- xterra rower screen is dim
- erg rower display only half lit
- rowing machine lcd backlight not working
- xterra rower console faint
keywords:
- lcd
- backlight
- dim display
- incomplete display
- ac 100-240v
- dc 12v
- adapter
- tension motor
- console power
- rower
facets:
  brand:
  - xterra
  product_line: rower
  model: erg700-2022
  applies_to:
  - erg700-2022
  section: errors
  code: '*'
  model_number:
  - '170918'
authority: 3
not_to_be_confused_with:
- xterra-rower-errors-monitor-does-not-display-install-batteries-then-computer-wires
- xterra-treadmill-errors-lcd-not-bright-check-110-v-or-230-v
- xterra-trx-errors-lcd-not-bright-check-220-v
see_also:
- erg700-2022-errors-e2-cable-communication-abnormal-8-pin-cable-and-tension-motor
- crw800-2024-errors-lcd-display-does-not-shine
- sr500-2016-lcd-dim-or-incomplete
source:
  ref: xterra-rower-erg700-2022-owners-manual
  locator: ERG700 OM Troubleshooting table, PDF p. 26 (printed 23), text.md lines
    794-856 (also in the OCR supplement for that page)
  extracted_at: '2026-09-11'
---

**This rower runs on an adapter, so the figures here are an adapter's - AC 100 to 240 V in, DC 12 V out - and the battery answer of the other Xterra rowers does not apply** (`xterra-rower-errors-monitor-does-not-display-install-batteries-then-computer-wires`). It is also not the treadmills' 110 V or 220 V check.

The condition is printed as *LCD display does not shine, incomplete or imperfect*:

| Cause | Solution |
|---|---|
| LCD backlight damage | 1. Replace the new LCD module or the control electronics |
| Console power is too low | 2. Check whether the AC power input is **AC100 ~ 240V** and the output is **DC12V**. 3. Check the power of the console. 4. Has the tension motor output **DC12V**? If not, please replace the new tension motor. |

The four solutions are numbered straight through both causes in the book, so read them as one list: a dead backlight is a module or board swap, and low power is traced adapter, console, tension motor, in that order.

**Step 4 is the odd one and the only tension-motor measurement in the book.** It makes the tension motor a source of console power on this machine, not only the resistance unit, which is why the E2 cable fault and a dark display can share a cause (`erg700-2022-errors-e2-cable-communication-abnormal-8-pin-cable-and-tension-motor`). The book says nothing about where to measure.

The Spirit CRW800 and XRW600 print this row with the same three figures, calling the motor a cable tensioner (`crw800-2024-errors-lcd-display-does-not-shine`); Sole's SR500 prints it too (`sr500-2016-lcd-dim-or-incomplete`).
