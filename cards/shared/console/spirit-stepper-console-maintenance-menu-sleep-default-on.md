---
id: spirit-stepper-console-maintenance-menu-sleep-default-on
title: The maintenance menu whose Sleep mode entry prints a default of On and whose Service list has no
  Stride test
kind: procedure
question: How do I get into maintenance mode on a Spirit crs800s-2024 or cs800-2024 stepper, and what is
  in it?
asked_as:
- how do i get into engineering mode on the stepper
- how do i switch the stepper console to metric
- how do i reset the odometer on the stepper
- how do i stop the stepper console going to sleep
keywords:
- maintenance mode
- engineering mode
- start stop enter
- five seconds
- units
- pause mode
- odometer reset
- sleep mode
- cab protocol
- motor test
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2024
  - cs800-2024
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce850-console-maintenance-menu-cab-or-csafe
- spirit-ce800-console-maintenance-menu-function-and-service
- ce900-2025-console-engineering-mode-unit-type
see_also:
- spirit-ce850-console-maintenance-menu-cab-or-csafe
- ct900ent-sleep-mode-auto-shutoff
- spirit-stepper-console-led-data-windows-steps-and-vertical-distance
source:
  ref: spirit-climber-cs800-2024-owners-manual
  locator: CS800-2024 p. 33 ENGINEERING MODE MENU; the CRS800S-2024 owner's manual prints the same
    menu on its p. 32
  extracted_at: '2026-09-10'
---

**Pedal the machine, then press and hold Start, Stop and Enter together for about 5 seconds.** The
Message Center displays **Maintenance Mode**. Press **Enter** to open the menu.

**You have to be pedalling.** Both manuals say so in the first sentence - "pedal the Stepper" and
"pedal the Semi-Recumbent Stepper" - and both head the page ENGINEERING MODE MENU while the screen
reads Maintenance Mode.

1. **Key Test** - test all the keys to make sure they are functioning
2. **Display Test** - tests all the display functions
3. **Function**
   - **Units** - Imperial (miles, pounds, feet) or Metric (kilometers, kilograms, meters)
   - **Pause mode** (have five minutes)
   - **Odometer Reset**
   - **Sleep mode (Default On)**
   - **Beep sound** (Control Beep)
   - **CAB Protocol or CSAFE Protocol**
4. **Service**
   - **Motor test**
   - **Csafe test**
   - **Sensor test** (test the speed sensor function)
5. **Exit**

Both printings list these items in this order, word for word.

**These two are the only Spirit machines whose menu states the sleep default.** Both print
**Sleep mode (Default On)**; the CE850 menu carries a bare Sleep mode entry with no default and no
figure. The 30-minute timeout itself is printed in the FEATURES chapter:
`ct900ent-sleep-mode-auto-shutoff`. **The CRS800S manual is the one that tells you where to turn it
off** - its TO TURN STEPPER OFF paragraph ends "follow the instructions in the Engineering section to
turn it off", meaning this entry.

**There is no Stride test.** The CE850's otherwise identical menu has one, because that machine has an
adjustable stride: `spirit-ce850-console-maintenance-menu-cab-or-csafe`. Neither stepper does, and
neither manual prints the entry.

**The CE800-2024, CR800-2024 and CU800-2024 menu is shorter still** - four Function entries, no Sleep
mode, no protocol choice, and a **PWM test** where this one has a Motor test:
`spirit-ce800-console-maintenance-menu-function-and-service`.

**The CSC900-2024 stair climber has no maintenance or engineering menu at all.** The words
engineering mode and maintenance mode appear nowhere in that manual; units are changed by pressing
**1, 2, 3, OK** from the running display instead (`csc900-2024-console-four-display-windows`).
