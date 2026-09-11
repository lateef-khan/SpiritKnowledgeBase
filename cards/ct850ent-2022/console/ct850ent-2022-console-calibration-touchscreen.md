---
id: ct850ent-2022-console-calibration-touchscreen
title: Calibrating a touchscreen console by tapping the centre of the Home icon ten
  times
kind: procedure
question: How do I calibrate a Spirit CT850ENT-2022 treadmill?
asked_as:
- how do i calibrate my treadmill
- how do i get into the settings page on the touchscreen treadmill
- what should the wheel size be set to
- treadmill speed is wrong how do i reset it
keywords:
- calibration
- setting page
- home icon
- touchscreen
- wheel size 2.98
- minimum speed
- maximum speed
- maximum elevation
- metric
- imperial
facets:
  brand:
  - spirit
  product_line: treadmill
  model: ct850ent-2022
  applies_to:
  - ct850ent-2022
  section: console
  code: '*'
  model_number:
  - '850852'
authority: 3
not_to_be_confused_with:
- ct850-2020-console-calibration-minimum-speed-0-3
- ct850-2016-console-calibration-minimum-speed-0-5
- ct900-calibration-procedure
- spirit-ct800-console-calibration-with-grade-return
see_also:
- ct800ent-2022-console-home-screen
- ct800ent-2022-console-layout
- ct850-2020-factory-setting-ranges
- spirit-ct800ent-console-engineering-mode-speed-and-incline-defaults-wheel-2-98
source:
  ref: spirit-treadmill-ct850ent-2022-owners-manual
  locator: CALIBRATION PROCEDURE, p. 46. CT850ENT-2022 service manual section 8-8
    Engineering Mode, PDF p. 43 (printed 43), text.md lines 862-872
  extracted_at: '2026-09-09'
---

**There is no safety key gesture and no button combination on this console.** Every other Spirit
treadmill calibration routine in this repository is entered by holding two or three keys while the
safety key goes in. This one is entered from the screen.

1. **Click the centre of the Home icon 10 times** to enter the setting page.
2. Set the display to show **Metric or Imperial** settings (Meters vs. Miles) with the **Up** or
   **Down** button, then press **Enter**.
3. Make sure the **wheel size diameter is 2.98**, then press **Enter**.
4. Adjust the **minimum speed** (if needed) to **0.3**, then press **Enter**.
5. Adjust the **maximum speed** (if needed) to **15.0**, then press **Enter**.
6. Adjust the **maximum elevation** (if needed) to **15**, then press **Enter**.
7. **Press Start to begin calibration.** The process is automatic; **the speed will start up without
   warning, so do not stand on the belt.**

The manual prints step 1 as "For ENT model is click on the Home icon center 10 times to the enter
setting page", which is damaged English; the gesture and the count are unambiguous. It does not say
where the Up, Down and Enter controls are on a touchscreen, and steps 2 to 7 are the LED console's
words carried over unchanged.

The manual prints no adjustable range for any of these values and does not say what to do when
calibration fails. Ranges are printed for the LED CT850-2020 console at
`ct850-2020-factory-setting-ranges`; they are that machine's figures, not these.

**The CT800ENT-2022 owner's manual, whose console chapter is otherwise the same document, prints no
calibration procedure at all**, so nothing here is claimed for that machine. The CT850 LED consoles
use a Start and Speed Up gesture and different figures:
`ct850-2020-console-calibration-minimum-speed-0-3` and
`ct850-2016-console-calibration-minimum-speed-0-5`.

**The CT850ENT-2022 service manual prints different speeds for the same screen.** Its Engineering Mode
page says the default speed is **Minimum 0.5 (mi/hr) - Maximum 12.0 (mi/hr)**, the default incline 15
level and the wheel size 2.98, with an Incline AD Value group and a calibration button
(`spirit-ct800ent-console-engineering-mode-speed-and-incline-defaults-wheel-2-98`). This owner's
manual says 0.3 and 15.0. Both are reproduced as printed; read the console's own screen before you
overwrite a value.

