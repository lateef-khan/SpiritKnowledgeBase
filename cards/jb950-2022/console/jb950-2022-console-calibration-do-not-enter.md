---
id: jb950-2022-console-calibration-do-not-enter
title: The Calibration entry the manual tells you not to enter, because it holds factory
  resistance settings
kind: fact
question: What does the Calibration entry do on a Spirit jb950-2022 Johnny G Spirit
  Bike console?
asked_as:
- should i calibrate my johnny g bike
- what is calibration on the jb950 menu
- how do i calibrate the resistance on my spin bike
- i changed the calibration on my johnny g bike
keywords:
- calibration
- factory sensitive
- do not enter
- resistance profile
- maintenance mode
- warning
- brake test
- levels
facets:
  brand:
  - spirit
  product_line: bike
  model: jb950-2022
  applies_to:
  - jb950-2022
  section: console
  code: '*'
  model_number:
  - '950348'
authority: 3
not_to_be_confused_with:
- jb950-2022-console-calibration-offset-number-from-the-mounting-bracket
see_also:
- jb950-2022-console-brake-test
- jb950-2022-console-software-version
- jb950-2022-console-maintenance-mode-entry-and-menu
- jb950-2022-console-calibration-offset-number-from-the-mounting-bracket
source:
  ref: spirit-bike-jb950-2022-owners-manual
  locator: JB950-2022 printed p. 61 CALIBRATION
  extracted_at: '2026-09-09'
---

**Do not enter it.** The manual's entire text for this menu item is a warning:

> "Calibration contains factory-sensitive settings for the bike's resistance system. Do not enter and
> make adjustments as they will **negatively affect the bike's resistance profile**."

**There is no procedure.** Unlike every other entry in this fifteen-page menu, Calibration is given no
steps, no values, no defaults and no way back. The manual documents its existence in order to tell you
to leave it alone.

**So there is no owner-facing calibration on this bike.** A rider who thinks the levels feel wrong is
not being asked to recalibrate - they are being told this is a factory setting.

**Test the resistance instead.** Brake Test runs the motor from L-1 to L-20 and back and reads the
encoder and limit sensor, without touching the calibration values -
`jb950-2022-console-brake-test`. Limit Sensor covers the case where a motor error has occurred.

**If someone has already been in here**, the manual offers no reset for it. Removing power will not
restore it - the console is rider-powered and has no batteries to pull - so the route is Spirit
customer service, and the Software Version screen is what they will ask for first.

**The service manual prints the procedure this manual withholds.** It names the calibration offset
number - written on the console mounting bracket, to be carried over to a replacement console - and
walks through adjusting it on a `CaliAdj` screen until the brake calibrates itself:
`jb950-2022-console-calibration-offset-number-from-the-mounting-bracket`. That is a technician's page;
the warning on this card is still what a rider should hear.
