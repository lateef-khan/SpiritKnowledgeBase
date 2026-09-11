---
id: ct800-2016-errors-incline-calibration-fails-checks-wire-colours
title: What to check when the incline calibration fails, with the motor and sensor
  wires named by colour and pins 10 to 12 by wire
kind: procedure
question: What do I check when incline calibration fails on a Spirit ct800-2016 treadmill?
asked_as:
- incline calibration fails on my spirit treadmill
- calibration will not complete
- incline motor wiring check
keywords:
- calibration fails
- incline motor
- position sensor
- vr connector
- wire harness
- wire colours
- incline board
- neutral
- 120 vac
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct800-2016
  applies_to:
  - ct800-2016
  section: errors
  code: incline-err
  model_number:
  - '800845'
authority: 3
not_to_be_confused_with:
- ct850-2016-incline-calibration-fails-checks
see_also:
- ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12
- ct800-2016-errors-incline-err-during-incline-action
- xt-2015-errors-calibration-does-not-pass
source:
  ref: spirit-treadmill-ct800-2016-service-manual
  locator: CT800 2016 service manual If calibration fails, PDF p. 53-55 (printed 52-54),
    text.md lines 1004-1076
  extracted_at: '2026-09-11'
---

The page headed *If calibration fails*, which follows the calibration procedure in this book. Remove the motor cover and check every wiring connection from the incline motor to the incline board; push all connectors in until they are fully seated. The connectors to be concerned with are:

1. **The 3 power wires for the motor: Red = Up, Black = Down, White = Neutral.**
2. **The position sensor wires, a 3-pin connector with board designation `VR`: Red = 5 Vdc, Black = Ground, White = Position signal (0~5 V depending on incline position).**
3. **The main wire harness at the bottom of the board.**

Then, in the manual's lettering:

- b. Run calibration again.
- c. Does the incline motor move at all?
- d. If no, do the Up/down lights on the incline board light?
- e. If they light, do the relays click on? If the relay clicks but the motor does not move, check the voltage between the neutral (white) wire and the Up (red) or Down (black) wire with the incline light and relay activated - **about the mains voltage, ~120 VAC** - and voltage with no movement means the motor is bad. If the light is on but the relay does not click, replace the incline board (bad relay most likely).
- f. If the motor moves, is there a sensor reading on the console? **The Distance window** displays the computer incline setting after the speed calibration ends, 15 for maximum and 0 for lowest; the Incline window is a counter showing the actual position sensor output. The potentiometer checks are the ones on `ct800-2016-errors-incline-err-test-procedure-110-vac-pins-10-to-12`: it should not be able to rotate, 5 Vdc between black and red, about 4.5 to 4.7 Vdc between red and white at the lowest position.
- iv to vii. The 3-pin connector on the incline board, then the output connector to the console, then the cable, then the console, as on that card.

**This page names the console connector pins by wire colour**, the same at the incline board and at the console:

| Pin | Wire | Signal |
|---|---|---|
| 10 | white | 5 Vdc |
| 11 | light blue | position signal 0~5 Vdc |
| 12 | pink | ground |

**Two figures on this page do not agree with the test procedure earlier in the same book.** The mains voltage here is ~120 VAC where the section 8.2 test says ~110 VAC, and the console reading here is in the *Distance* window where section 8.2 says the *Incline* window. The calibration procedure page itself (a console fact) says the Incline window shows the potentiometer reading, about 235 at the bottom and about 22 at the top.

**The CT850 2016 service manual prints this page with different pin assignments** - power pins 1 Neutral, 2 Up, 3 Down and VR pins 1 Ground, 2 Position, 3 5 Vdc, by number rather than colour (`ct850-2016-incline-calibration-fails-checks`).
