---
id: crw800-2021-specs-electrical-configuration-tension-motor-dc-4-0-to-6-0-v
title: Console with an LCD and a tension motor working at DC 4.0 to 6.0 V on the 2020-version
  air rower
kind: spec
question: What does the electrical configuration page of the Spirit crw800-2021 rower
  service manual say, and what voltage does its tension motor work at?
asked_as:
- what voltage is the crw800 tension motor
- crw800 2020 electrical configuration
- gear motor working voltage spirit rower
- what does the main controller do on the crw800
keywords:
- electrical configuration
- tension motor
- gear motor
- working voltage
- dc 4.0-6.0v
- console
- main controller
- lcd display
- motor driver
- '800940'
facets:
  brand:
  - spirit
  product_line: rower
  model: crw800-2021
  applies_to:
  - crw800-2021
  section: specs
  code: '*'
  model_number:
  - '800940'
authority: 3
not_to_be_confused_with:
- spirit-crw800-2016-xrw600-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v
see_also:
- crw800-2021-specs-unit-block-diagram-generator-and-rf-level-control
- crw800-2021-specs-generator-controller-ae0076-connector-definition
- crw800-2024-specs-resistance-system
- spirit-ce850-specs-tension-motor-working-voltage-dc-4-0-to-6-0-v
source:
  ref: spirit-rower-crw800-2021-service-manual
  locator: 3. Electrical Configurations, PDF p. 10 (printed 9), text.md lines 83-103;
    the E2 voltage-measurement page repeats the figure, PDF p. 35, lines 485-505
  extracted_at: '2026-09-11'
---

**This is the 2020-version book (800940); the 2016 book prints DC 4.5-7.5 V for what looks like the
same motor** (`spirit-crw800-2016-xrw600-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v`).

| Part | Description printed |
|---|---|
| Console | Interface that controls all functions of the Rower |
| Tension motor | It can change to increase or decrease resistance level of brake |

**General information**

| Part | Description printed |
|---|---|
| Console | Contain Keys control and LCD Display. Main controller Include power supply and motor driver control circuit |
| Tension motor | **Work voltage: DC 4.0~6.0V.** Control resistance increases and decreases |

The same 4.0-6.0 V range is what the E2 test page expects to read across the motor's blue and
green wires - +4.0 to 6.0 V DC on LEVEL UP, -4.0 to -6.0 V DC on LEVEL DOWN - so the working voltage
and the test reading are one figure in this book. The motor itself is photographed as a gear motor
with a steel cable to the flywheel brake; the book's own word for it is *cable tensioner* in the
error pages.

No power supply, adapter or generator rating is printed on this page. Where the machine's power
comes from is on the block diagram and generator-controller cards.

