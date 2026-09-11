---
id: cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v
title: Console with an LED display and a tension motor working at DC 4 to 6 V on the
  2016 stepper
kind: spec
question: What does the electrical configuration page of the Spirit cs800-2016 stepper
  service manual say, and what voltage does its tension motor work at?
asked_as:
- what voltage is the cs800 tension motor
- xs200-ss003 electrical configuration
- tension motor working voltage spirit climber
- cs800 2016 main controller
keywords:
- electrical configuration
- tension motor
- working voltage
- dc 4-6v
- console
- main controller
- led display
- motor driver
- xs200-ss003
- climber
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
- spirit-crs800s-cs800-2021-specs-electrical-configuration-ecb-brake-with-no-voltage-printed
- spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor
see_also:
- cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable
- cs800-2016-specs-unit-block-diagram-climber-configuration
- spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v
source:
  ref: spirit-stepper-cs800-2016-service-manual
  locator: 3. Electrical Configurations, PDF pp. 11-12 (printed 11-12), text.md lines
    169-194; the E2 test page repeats the range, PDF p. 35, lines 492-528
  extracted_at: '2026-09-11'
---

**DC 4~6 V**, written without decimals - the same range the CE850 ellipticals print as 4.0-6.0 V
(`spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v`) and the 2020-version CS800
book drops altogether
(`spirit-crs800s-cs800-2021-specs-electrical-configuration-ecb-brake-with-no-voltage-printed`).

| Part | Description printed |
|---|---|
| CONSOLE | Interface that controls all functions of the Climber |
| TENSION MOTOR | It can change to increase or decrease resistance level of brake |

**General information**

| Part | Description printed |
|---|---|
| CONSOLE | Contains Key controls and LED Display. Main controller Include power supply and motor driver control circuit |
| TENSION MOTOR | **Work voltage: DC 4 ~ 6V.** Control resistance increases and decreases |

The E2 test page expects the same range across the motor's black and brown wires: **+4.0 to
6.0 V DC on LEVEL UP, -4.0 to 6.0 V DC on LEVEL DOWN** - although the same page's operation table
says "Level UP: +5VDC; Level DOWN: -5VDC" two paragraphs earlier. Both are inside the 4-6 V range.

The motor is an **M-100A** gear motor with a steel rope; its wire colours and plug are on
`cs800-2016-specs-tension-motor-m-100a-wire-colours-and-the-10-pin-computer-cable`.

