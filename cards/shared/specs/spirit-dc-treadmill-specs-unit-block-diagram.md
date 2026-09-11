---
id: spirit-dc-treadmill-specs-unit-block-diagram
title: 'The DC-drive unit block diagram: display board, amplifier and speakers above,
  driver board, motor and incline motor below'
kind: spec
question: What does the unit block diagram of a Spirit ct800-2016 or a Spirit XT-series
  DC-drive treadmill show, and how do the books differ?
asked_as:
- block diagram of the xt385
- how are the boards connected on the xt485 ent
- treadmill configuration diagram xt
- signal flow between console and driver board on a dc treadmill
keywords:
- block diagram
- treadmill configuration
- display board
- driver board
- amplifier
- line in
- line out
- bluetooth
- current braker
- vr set
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800-2016
  - xt185-2015
  - xt185-2023
  - xt285-2015
  - xt285-2023
  - xt385-2015
  - xt385-2023
  - xt485-2015
  - xt485-2023
  - xt485ent-2023
  - xt685-2023
  - xt685ent-2023
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- ct850-2020-unit-block-diagram
- ct850-2016-unit-block-diagram
- spirit-ct-ent-specs-unit-block-diagram
see_also:
- spirit-xt-specs-circuit-diagram-codes-and-contents
- ct800-2016-specs-circuit-diagram
- spirit-xt-specs-electrical-part-descriptions
source:
  ref: spirit-treadmill-xt385-2015-service-manual
  locator: 'CT800-2016: PDF p. 21 (printed 20), section 5 Treadmill Configuration,
    text.md lines 362-367. XT185-2015 p. 22 (OCR supplement); XT285-2015 p. 23; XT385-2015
    p. 22, line 371 (OCR); XT485-2015 p. 22, line 370; XT185-2023 p. 11, line 233
    (OCR); XT285-2023 p. 11, line 234; XT385-2023 p. 11, line 211; XT485-2023 p. 11;
    XT685-2023 p. 11; XT485ENT p. 20, line 326 (OCR); XT685ENT p. 10, line 218 (OCR).
    Every page is a flat drawing read from its render or OCR supplement'
  extracted_at: '2026-09-11'
---

Twelve books draw the same block diagram with small differences. The common drawing:

**Upper half.** KEY, COOLING FAN, HR HANDLEBAR, WIRELESS HR RECEIVER and SAFETY KEY feed the **DISPLAY
BOARD**. The display board feeds an **AMPLIFIER** with a **LINE IN**, which drives **SPEAKER L** and
**SPEAKER R**.

**Lower half.** POWER goes through the **POWER SWITCH** and a **CURRENT BRAKER** to the **DRIVER BOARD**,
which drives the **MOTOR** and the **INCLINE MOTOR**; an **RPM SENSOR** reports to the driver board and a
**VR SET** hangs on the incline side.

| Book | What its drawing adds or drops |
|---|---|
| CT800-2016 | adds **LINE OUT** on the amplifier |
| XT185-2015, XT285-2015 | adds a **BLUETOOTH** box on the display board and LINE IN on the amplifier |
| XT385-2015, XT485-2015 | LINE IN and **LINE OUT**, no Bluetooth |
| XT185-2023 to XT685-2023 | **BLUETOOTH** box, no LINE OUT |
| XT485ENT | as the common drawing (KEYBOARD, LINE IN, no Bluetooth box) |
| XT685ENT | **BLE / WIRELESS HR RECEIVER** as one box, adds a **CHARGING** box, no KEYBOARD box |

None of these drawings carries a part number or a pin count. The AC-inverter families (CT850, CT900,
40T) use a different drawing with an inverter in place of the driver board.
