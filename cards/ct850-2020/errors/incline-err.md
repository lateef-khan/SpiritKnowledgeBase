---
id: ct850-2020-incline-err
title: 'INCLINE ERR: the incline reading does not change while the incline runs'
kind: troubleshooting
question: What does INCLINE ERR mean on a Spirit CT800 2020, CT800ENT, CT850 2020,
  CT850ENT or 4.0T treadmill?
asked_as:
- incline err on my spirit treadmill
- treadmill display says incline error
- incline does not move and shows an error
keywords:
- incline err
- vr value
- up down keys
- relay
- incline motor
- console cable
- driver board
- recalibrate
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - 40t-2026
  - ct800-2020
  - ct800ent-2022
  - ct850-2020
  - ct850ent-2022
  section: errors
  code: incline-err
authority: 3
not_to_be_confused_with:
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2020-e-52h-incline-motor-fails-during-calibration
- ct900-e33-incline-err
see_also:
- ct850-2020-e3-incline-motor-cannot-work
- ct850-2016-incline-err-during-incline-action
- ct850-2020-inverter-error-code-list
- ct850-2020-incline-motor-replacement
- 40t-2026-errors-eeprom-err-hold-stop-then-start-stop-fan
source:
  ref: spirit-treadmill-ct850-2020-service-manual
  locator: 'Section 8-4 Error Message: INCLINE ERR, pages 42-44 (printed 41-43). Pages
    42 and 43 are flattened images and were read from raw/page-42.png and raw/page-43.png;
    CT800 2020 service manual 8-4 Error Message: INCLINE ERR; page 41 is a picture
    read from the render, PDF p. 40-42 (printed 39-41), text.md lines 533-580; CT800ENT
    2022 service manual 8-4 Error Message: Incline Err, PDF p. 34, text.md lines 644-679;
    CT850ENT 2022 service manual 8-4 Error Message: Incline Err, PDF p. 35, text.md
    lines 663-698; 4.0T 2026 service manual Error Message: INCLINE ERR, PDF p. 29-31,
    text.md lines 412-472; the 4.0T ST8700A-ST026-01 service manual (spirit-treadmill-40t-2026-service-manual-st8700a,
    88% the ST017 book) prints the same page one page later, word for word (compared
    with difflib on 2026-09-11): Error Message: INCLINE ERR at PDF p. 30-32, text.md
    lines 443-502'
  extracted_at: '2026-09-08'
---

**This is the message INCLINE ERR, not the code E3 and not E-52H.** `INCLINE ERR` is not in the
error code table at 8-1 at all; it only has this section.

Definition:

> During incline action, the display board CPU cannot read the VR value, so INCLINE ERR appears.

Cause:

> Press the incline UP/DOWN key. The incline doesn't operate. INCLINE ERR appears on the display.
> Incline motor isn't operation up or down, making the VR value exceed the range.
> Press the incline UP and DOWN key. The driver board UP or DOWN indicator lights. The incline
> operates, moving the VR, which changes the VR value.
> The display board CPU reads the incline VR value. If there is no VR value change, to the CPU, the
> incline is not operating when it should be. INCLINE Err appears on the display.

| Part | Troubleshooting |
|---|---|
| Display board | 1. Press incline UP key. The driver board UP RELAY action. 2. Press incline DOWN key. The driver board DOWN RELAY action. 3. If not as above, inspect the cable and connections. |
| Console cable | 1. Inspect whether the console cable is connected well. 2. Test by replacing the cable with a good one. |
| Driver board | Inspect whether the driver board UP/DOWN REALY is action. 1. Press incline UP or DOWN key again, making the incline motor return to its position. 2. If ERR still appears, re-calibrate the incline set. |
| Incline motor | 1. Inspect whether the incline motor is stuck. 2. Inspect whether the incline gears are cracked. 3. Test whether the incline motor has a broken circuit. 4. Re-calibrate the incline set. |

**The action flow chart's end box does not say what the rest of the page says.** Re-rendered at 600
dpi, the box reads `SHOW INCLINE E33 MESSAGE`, and `E33` is set in a visibly different font from the
rest of the box, as though pasted in from another manual. `E33` appears **nowhere else in this
manual** - not in the 8-1 error code table, not on this page, not anywhere - while the section
heading and every other line here print `INCLINE ERR`. The message a technician will see on the
display is `INCLINE ERR`. Spirit's CT900 does use `E33` for its incline error, on a different
controller, which is the likeliest origin of the pasted box.

The code `E3`, which the 8-1 table does list, is the *reading out of range* rather than the reading
not changing: `ct850-2020-e3-incline-motor-cannot-work`. The CT850 2016 manual prints **both**
definitions under the single name `INCLINE ERR`.

The last part in the troubleshooting table is the incline motor, checked for a seizure, cracked
gears and a broken circuit; its replacement procedure is on
`ct850-2020-incline-motor-replacement`.

**Four more service manuals print this section word for word**: the CT800 2020, CT800ENT 2022, CT850ENT 2022 and 4.0T - the definition, the cause, the same four-row relay table, and on the CT800 2020 and the 4.0T the same action flow chart whose end box reads `SHOW INCLINE E33 MESSAGE`. The two ENT books print the table beside a smaller configuration drawing and no flow chart. So the pasted `E33` box is in three books now and is Dyaco's template, not a CT850 slip. The 4.0T's own code table has one row, `EEPROM ERR` (`40t-2026-errors-eeprom-err-hold-stop-then-start-stop-fan`), so INCLINE ERR is a message on that machine too, not a code.
