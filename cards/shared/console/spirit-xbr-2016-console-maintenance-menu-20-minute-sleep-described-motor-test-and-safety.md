---
id: spirit-xbr-2016-console-maintenance-menu-20-minute-sleep-described-motor-test-and-safety
title: 'The 2016 service-manual maintenance menu: a 20-minute sleep switched on, a
  Motor Test that runs the resistance motor in a loop, a Safety item and a Security
  lock'
kind: procedure
question: How do I get into the maintenance menu on a Spirit XBR25-2016 or XBU55-2016
  bike, and what is in it?
asked_as:
- how do i get into engineering mode on my 2016 spirit bike
- how do i run the motor test on the xbr25
- how do i switch the xbu55 console to metric
- how do i lock the keypad on the spirit recumbent
keywords:
- maintenance menu
- engineering mode
- start stop enter
- sleep mode
- display mode
- 20 minutes
- motor test
- position sensor
- safety
- security
facets:
  brand:
  - spirit
  product_line: bike
  model: '*'
  applies_to:
  - xbr25-2016
  - xbu55-2016
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
- xe795-2021-console-engineering-mode-with-a-da-test
- xe395-2023-console-engineering-mode-with-a-child-lock
see_also:
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
- spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset
- xe795-2021-console-engineering-mode-with-a-da-test
- spirit-xbr-2016-console-keys-in-ready-and-run-mode-enter-scans-every-four-seconds
source:
  ref: spirit-bike-xbr25-2016-service-manual
  locator: XBR25-2016 MAINTENANCE MENU IN CONSOLE SOFTWARE, PDF p. 40 (printed 40);
    text.md lines 583-609. The XBU55-2016 service manual prints the same page on its
    PDF p. 40, text.md lines 583-608, with the three wording differences named in
    the body. The XBR55-2016 service manual prints no such page
  extracted_at: '2026-09-11'
---

**Press and hold Start, Stop and Enter for about 5 seconds.** The Message Window displays
**"Engineering Mode"**. Press **Enter** to open the menu; the **Level ▲/▼** keys move through it.

| Item | What it does |
|---|---|
| **a. Key Test** | Tests all the keys to make sure they are functioning |
| **b. LCD Test** | Tests all the display functions |
| **c. Functions** | Press Enter for the settings; the Up arrow scrolls them |
| **d. Security** | Allows the keypad to be locked to prevent unauthorized use |

**Inside Functions, in the printed order:**

| # | XBR25-2016 prints | XBU55-2016 prints |
|---|---|---|
| i | **Sleep Mode** - **turn on** to have the console power down automatically after **20 minutes** of inactivity | **Display Mode** - turn on to have the console power down automatically after 20 minutes of inactivity |
| ii | Pause Mode - turn on to allow **5 minutes** of pause, turn off to pause indefinitely | same |
| iii | ODO Reset - resets the odometer | same |
| iv | **Unit Type** - English or Metric | **Units** - English or Metric |
| v | Beep - turns off the speaker so no beeping sound is heard | same |
| vi | **Motor Test** - "Press Enter to run the resistance motor up and down in a continuous loop. Display shows level setting and position sensor reading. Press Stop to end test" | same |
| vii | Safety - no description printed | same |
| viii | **Bike/Bike** - printed exactly so, with no description | not printed |

**The 2019 owner's-manual menu for the successors of these bikes says "turn off".** The XBR25-2019,
XBR55-2019 and XBU55-2019 books print this list with Display Mode **turned off** to power down, an
undescribed Motor Test, and no Unit Type or Bike/Bike line
(`spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item`). These 2016 service books
say **turn on**, and are the only Spirit residential-bike documents that explain what the Motor Test
does. The 20 minutes and the 5 minutes agree.

**The software-spec chapter of the same books prints 30 minutes for the same sleep**, and calls the
setting Display Mode (`spirit-xbr-2016-console-software-modes-idle-30-minute-sleep-child-lock-pause-end-reset`).
Nothing in either book resolves 20 against 30; read the console.

**The XBR55-2016 service manual has no maintenance menu page.** Its software-spec chapter twice says
a setting "could be set by ENGINEERING MODE", but the book goes from the circuit diagram on p. 41
straight to the troubleshooting matrix on p. 42. This was checked in the text layer, with the
letters spaced, and on a render of both pages. The XBR95-2016 book prints the DA Test menu instead
(`xe795-2021-console-engineering-mode-with-a-da-test`).

**Safety is never explained.** The XE395-2010 elliptical, whose menu this is, turns its Safety on by
holding Start and Enter together; nothing in these two books says so.
