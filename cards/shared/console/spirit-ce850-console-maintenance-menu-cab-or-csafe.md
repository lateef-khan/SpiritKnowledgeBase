---
id: spirit-ce850-console-maintenance-menu-cab-or-csafe
title: The maintenance menu whose Function list adds Sleep mode and a CAB or CSAFE protocol choice
kind: procedure
question: How do I get into maintenance mode on a Spirit CE850 elliptical, and what is in it?
asked_as:
- how do i get into engineering mode on the ce850
- how do i switch the elliptical console to metric
- how do i change the elliptical to csafe protocol
- how do i stop the elliptical console going to sleep
keywords:
- engineering mode
- maintenance mode
- start stop enter
- units
- pause mode
- sleep mode
- cab protocol
- csafe protocol
- motor test
- stride test
facets:
  brand:
  - spirit
  product_line: elliptical
  model: '*'
  applies_to:
  - ce850-2020
  - ce850-2022
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-ce800-console-maintenance-menu-function-and-service
see_also:
- spirit-ce800-console-maintenance-menu-function-and-service
- ct900ent-sleep-mode-auto-shutoff
- spirit-ce850-console-power-up-self-test
source:
  ref: spirit-elliptical-ce850-2020-owners-manual
  locator: CE850 2020 p. 41 ENGINEERING MODE; CE850 2022 p. 42
  extracted_at: '2026-09-09'
---

**Press and hold Start, Stop and Enter together for about 5 seconds**, then press **Enter** to open
the menu. Neither manual tells you to pedal first.

1. **Key Test** - test all the keys to make sure they are functioning
2. **Display Test** - tests all the display functions
3. **Function**
   - **Units** - Imperial (miles, pounds, feet) or Metric (kilometers, kilograms, meters)
   - **Pause mode** (have five minutes)
   - **Odometer Reset**
   - **Sleep mode**
   - **Beep sound** (Control Beep)
   - **CAB Protocol or CSAFE Protocol**
4. **Service**
   - **Motor test**
   - **Stride test**
   - **Csafe test**
   - **Sensor test**
5. **Exit**

Both printings list these items in this order, word for word.

**Sleep mode is where the 30-minute timeout is turned off**; the behaviour itself is on
`ct900ent-sleep-mode-auto-shutoff`.

**The manual prints no values for the protocol setting beyond the two names**, no default, and no
instruction on which to pick.

**The CE800-2021 and CE800-2023 menu is shorter** - no Sleep mode, no protocol entry, and a PWM
test where this one has a Motor test and a Stride test:
`spirit-ce800-console-maintenance-menu-function-and-service`.
