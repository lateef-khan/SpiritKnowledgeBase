---
id: cs800-2016-console-engineering-mode-with-a-30-minute-sleep-a-da-test-and-a-safety-item
title: The engineering menu whose Functions list holds a 30-minute Sleep mode, a D/A
  test of the brake and a SAFETY item, behind a keypad Security lock
kind: procedure
question: How do I get into engineering mode on a Spirit cs800-2016 stepper, and what
  is in it?
asked_as:
- how do i get into engineering mode on the older cs800 stepper
- how do i switch the cs800 to metric
- how do i lock the keypad on the stepper
- how do i test the brake on the cs800
keywords:
- engineering mode
- maintenance menu
- start stop enter
- five seconds
- sleep mode
- 30 minutes
- pause mode
- odo reset
- d/a test
- security
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: console
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
- xe795-2021-console-engineering-mode-with-a-da-test
- ce850-2016-console-engineering-mode-security-lock
see_also:
- ce850-2016-console-engineering-mode-security-lock
- cs800-2016-console-software-modes-idle-30-minute-sleep-child-lock-quick-start-pause-end-reset
- cs800-2016-console-keys-in-ready-and-run-mode-and-the-display-key-scan-of-seg-time-dist-and-pace
- spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: CS800-2016 (XS200-SS003) service manual Maintenance Menu in console software,
    PDF p. 40 (printed 40); text.md lines 575-597
  extracted_at: '2026-09-11'
---

The console has built-in maintenance/diagnostic software - it can switch the display between English
and Metric and turn off the key beep, among other things. The book notes the mode **"may be called
Engineering mode, depending on version"**.

**Press and hold Start, Stop and Enter together for about 5 seconds.** The message window displays
**`ENGINEERING MODE MENU PRESS ENTER`**. Press **Enter** to open the menu. **No pedalling is asked
for** - the 2020 CS800 book says "pedal the elliptical" first; this one does not.

- **a. Key test** - test all the keys to make sure they are functioning
- **b. Display test** - tests all the display functions
- **c. Functions** (press Enter to access settings)
  1. **Sleep mode** - turn on to have the console power down automatically after **30 minutes of
     inactivity**
  2. **Pause Mode** - turn on to allow **5 minutes** of pause; turn off to have the console pause
     indefinitely
  3. **ODO reset** - reset the odometer
  4. **Units** - English or Metric display readings
  5. **Beep** - turn on or off the beep when a key is pressed
  6. **D/A test** - **tests the brake resistance**
  7. **SAFETY**
- **d. Security** - allows you to lock the keypad so no unauthorized use is allowed

**SAFETY is printed with no explanation**, as on every Dyaco menu that carries it. Do not guess what
it does.

**This is the CE850-2016 elliptical's menu, word for word** - the same 30-minute sleep, the same D/A
test and the same bare SAFETY (`ce850-2016-console-engineering-mode-security-lock`). It is a
stepper, so it takes its own card; nothing in the two lists differs.

**It is not the 2020 CS800's menu.** The CS800 (2020) and CRS800S books open theirs with the same
three-key hold but land on a **Maintenance Mode** with a Function list of Units, Pause mode, Odometer
Reset, Sleep mode, Beep sound and a **CAB or CSAFE protocol** choice, a Service list of Motor test,
Csafe test and Sensor test, and an Exit
(`spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page`).
**There is no protocol choice, no motor test, no sensor test and no Exit on the 2016 machine**, and
no D/A test or Security on the 2020 one.

**Thirty minutes here, and thirty again in the software modes.** This book's Window Display Mode
page also puts sleep at 30 minutes, so for once the two chapters agree
(`cs800-2016-console-software-modes-idle-30-minute-sleep-child-lock-quick-start-pause-end-reset`).
The XE and XS895 menu prints **20** minutes under a Display Mode entry and ends Functions with a
Motor Test instead (`spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item`).

