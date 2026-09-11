---
id: cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable
title: The M-100A tension motor is drawn with black and brown motor wires, red, orange
  and yellow sensor wires, and a 1200 mm 10-pin computer cable splitting to 5, 2 and
  3-pin plugs
kind: spec
question: What are the wire colours of the tension motor and the computer cable on
  a Spirit cs800-2016 stepper?
asked_as:
- cs800 2016 tension motor wire colours
- which wires are the motor on the xs200 stepper
- 10 pin computer cable on the cs800
- m-100a motor drawing with dimensions
keywords:
- tension motor
- m-100a
- wire colours
- black
- brown
- computer cable
- 10-pin
- xhp
- smr
- steel rope
facets:
  brand:
  - spirit
  product_line: climber
  model: cs800-2016
  applies_to:
  - cs800-2016
  section: specs
  code: '*'
  model_number:
  - '800645'
authority: 3
not_to_be_confused_with:
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
see_also:
- cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down
- cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: Tension Motor connector definition function, PDF p. 28 (printed 28), text.md
    lines 402-411 (only 'STEEL ROPE' is native; the motor drawing with wire colours
    and dimensions read from a 110 dpi render, OCR supplement 1263-1267); the computer-cable
    drawing on the E2 test page, PDF p. 36, lines 529-530 (supplement 1323-1365, Chinese
    wire colours and plug codes)
  extracted_at: '2026-09-11'
---

**Unlike the later stepper books, the 2016 CS800 prints no pin numbers for its motor plug.** Its
page shows a photograph of the blue M-100A motor with one callout, **STEEL ROPE**, over an
engineering drawing of the motor that labels the wires:

| Wire | To |
|---|---|
| **black +** and **brown -** | the **DC Motor** (with a 104J 100V capacitor across it) |
| **red, orange, yellow** | the position potentiometer |

The drawing gives the motor body as roughly 30.5 + 22 + 25.5 + 12 mm long and 41.3 mm high with a
12 mm drum bore, and 20 mm wide - the only dimensions in the book. The E2 test uses the same
colours: "red probe in black wire, Black probe in brown wire".

## The computer cable

A second drawing on the E2 test page gives the loom that carries these lines to the console:

- **1200 +20/-0 mm** long, a **2423-10P (XHP)** ten-way plug at the console end with ten wire
  colours - black, brown, red, orange, yellow, green, blue, purple, grey, white - and heat-shrink
  sleeves at 10 +/-3 mm and 30 +/-3 mm.
- It splits into three SMR plugs at the machine end: **2319-5P** (black, brown, red, orange,
  yellow - the motor), **2319-2P** (green, blue) and **2319-3P** (purple, grey, white).

The ten-way plug's pin functions are on
`cs800-2016-specs-console-to-tension-motor-10-pin-definition-up-signal-down`; the book does not say
which colour is which pin, and the two drawings' colour groups do not line up with that list's
names. The 2020-version books replace all of this with a numbered five-pin list
(`spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1`).

