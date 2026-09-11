---
id: spirit-rehab-stepper-console-maintenance-menu-with-a-five-window-sensor-test
title: The maintenance menu whose Sensor test reports five separate signals, one in
  each data window
kind: procedure
question: How do I get into maintenance mode on a Spirit rehabilitation recumbent
  stepper, and what is in it?
asked_as:
- how do i get into engineering mode on my rehab stepper
- how do i switch the rehab stepper to metric
- how do i test the sensors on the spirit stepper
- how do i reset the odometer on the rehab stepper
keywords:
- maintenance mode
- engineering mode
- start stop enter
- five seconds
- key test
- lcd test
- sleep mode
- pause mode
- odometer reset
- sensor test
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - 7-0s-med
  - 7-5s-med
  - 70s-2025
  - 75s-2025
  - ms300-2021
  section: console
  code: '*'
authority: 3
not_to_be_confused_with:
- spirit-stepper-console-maintenance-menu-sleep-default-on
- spirit-stepper-console-maintenance-menu-sleep-mode-default-off-and-a-cross-reference-to-the-wrong-page
- spirit-xe-console-engineering-mode-with-an-lcd-test-and-a-safety-item
see_also:
- spirit-rehab-stepper-console-set-up-key-position-by-height-and-the-track-or-step-graph
- spirit-rehab-stepper-console-power-up-and-the-twenty-minute-auto-power-down
source:
  ref: spirit-climber-ms300-2021-owners-manual
  locator: MS300-2021 printed p. 57-58, Maintenance menu in console software; the
    7.0S-2025 prints the same menu on its printed p. 39 and the 7.5S-2025 on its printed
    p. 41, both under MACHINE CARE / Console Software. 7.5S (RS9600-SS021-01) service
    manual 5.2.1 Maintenance menu in console software, PDF pp. 11-12, text.md lines
    83-124 (no printed folios). 7.0S (RS9500-SS021-02) service manual, spirit-stepper-70s-2025-service-manual,
    5.2.1 Maintenance menu in console software, PDF pp. 11-12, text.md lines 98-143;
    7.5S (RS9600-SS021-03) service manual, spirit-stepper-75s-2025-service-manual,
    PDF pp. 11-12, lines 82-126 - both word for word the RS9600-SS021-01 page
  extracted_at: '2026-09-10'
---

**Press and hold Start, Stop and Enter together for about 5 seconds**, then press **enter**
to open the menu. **You do not have to be pedalling** - none of the five books says so, unlike the
CS800 and CRS800S manuals, which open the same instruction with "pedal the stepper".

**What the screen says is not the same from book to book, and it does not split by generation.**

| Book | The message window will display |
|---|---|
| **MS300-2021** | **"Engineering mode"** |
| **MED 7.5S** (7-5s-med) | **"Engineering mode"** |
| **MED 7.0S** (7-0s-med) | **"Maintenance mode"** |
| **7.0S-2025**, **7.5S-2025** | **"Maintenance mode"** |

**The two MED books disagree with each other**, on otherwise identical pages. All five head the
paragraph "may be called Engineering mode, depending on version", so both words mean this menu and
neither is wrong on a given console.

| Item | What it holds |
|---|---|
| **Key Test** | - |
| **LCD test** | - |
| **Functions** | **Sleep mode - on**; **Pause mode - on** ("If pause mode is off then console will remained Paused indefinitely, unless Stop or Start is pressed again"); **Odometer reset**; **Units - English or Metric** |
| **Service** | **Motor test**, then **Sensor Test** |
| | |

**Motor test** runs the resistance motor **from level 1~20 and then 20~1**, and shows the **position
sensor value in the STEPS data window**.

**Sensor Test puts a different signal in each of the five data windows** - the only test of its shape
in the Spirit range:

| Window | What it shows |
|---|---|
| **SPM** | reflector sensor **#1** signal (1 or 0) |
| **CALORIES** | reflector sensor **#2** signal |
| **TIME** | **left** step position counter |
| **STEPS** | **right** step position counter |
| **PULSE** | speed sensor signal (on or off) |

**There is no Beep entry, no CSAFE or CAB protocol choice, no Csafe test, no Security and no Exit**,
all of which sit on other Spirit menus. **Units is the entry the Set Up key's Position setting refers
to** when it says centimetres are used "if the machine is set to metric measurements"
(`spirit-rehab-stepper-console-set-up-key-position-by-height-and-the-track-or-step-graph`).

**Sleep mode - on is stated as a value, not as a timeout.** The 20-minute automatic power-down is
printed in the console chapter and never connected to this entry
(`spirit-rehab-stepper-console-power-up-and-the-twenty-minute-auto-power-down`).

**The troubleshooting chapters of all five books send technicians here** - "Perform Keypad test in
Maintenance mode", "Perform the Sensor tests in Maintenance mode" - and call the Key Test a
**Keypad test**, which is not what this menu calls it.

**The 7.5S service manual (RS9600-SS021-01) prints this menu with the figures the owner's manuals
leave out**, and its message window reads **"Engineering mode"**, as the MED 7.5S owner's manual does.
Same three-key hold for about 5 seconds, same four groups. What it adds:

- **Key Test** - each key press beeps and shows a number on the display; a key with no beep and no
  number has malfunctioned; when all keys have been pressed the display shows **"Passed"** and the
  test ends by itself.
- **Sleep** - off means the console power is always on; **on means the console sleeps after 30
  minutes of inactivity**.
- **Pause** - **on means the pause lasts 30 minutes**, then the console returns to idle; off means it
  pauses indefinitely.
- **Motor test** - runs the resistance motor **1 to 20 and then 20 to 1**; the **level shows in the
  SPM window** and the motor position sensor value in the **STEPS window**.
- **Sensor Test** - the book names the two sensors: a **Step Sensor** on the front left side pulley
  (two optical sensors reading a silver-and-black encoder wheel) and an **RPM Sensor** (an optical
  sensor that senses the **four bolt heads on the flywheel**). Sensor #1 shows in SPM and #2 in
  CALORIES as 1 or 0; the TIME and STEPS windows are the left and right step position counters and
  **should go from about 0 to about 17** over a full step; the RPM sensor shows ON/OFF in PULSE and the
  **actual flywheel RPM in the message window**.

**Thirty minutes here, twenty in the owner's manuals.** The five owner's manuals put the automatic
power-down at **20 minutes** and never tie it to this entry
(`spirit-rehab-stepper-console-power-up-and-the-twenty-minute-auto-power-down`); the service manual
puts the Sleep entry at **30**. Nothing reconciles them; both are reproduced as printed. The
service manual also prints the two error messages under the menu - EEPROM Error ("the only error
message") and Motor Error - which are held with the error cards.

**The 7.0S-770545 (RS9500-SS021-02) and 7.5S-775545 (RS9600-SS021-03) service manuals print this menu word for word** - the same "Engineering mode" prompt, the same 30-minute Sleep and 30-minute Pause figures, the same Motor test and five-window Sensor Test - on their PDF pp. 11-12. The 7.0S book is the RS9600 book with a 7.0S cover: nothing on its console pages changes for the shorter machine.

