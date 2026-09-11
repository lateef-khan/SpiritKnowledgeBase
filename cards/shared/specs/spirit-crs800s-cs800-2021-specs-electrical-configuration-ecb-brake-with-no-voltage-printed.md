---
id: spirit-crs800s-cs800-2021-specs-electrical-configuration-ecb-brake-with-no-voltage-printed
title: Console with an LED display, a main controller and an ECB brake, and no motor
  working voltage printed on the 2020-version steppers
kind: fact
question: What does the electrical configuration page of the Spirit CRS800S or CS800
  (2020 version) stepper service manual say?
asked_as:
- what is the ecb brake on the cs800
- crs800s electrical configuration
- does the cs800 2020 manual give a tension motor voltage
- what does the main controller do on the spirit stepper
keywords:
- electrical configuration
- ecb brake
- main controller
- console
- led display
- ecb driver
- power supply
- tension motor
- no voltage
- stepper
facets:
  brand:
  - spirit
  product_line: climber
  model: '*'
  applies_to:
  - crs800s-2021
  - cs800-2021
  section: specs
  code: '*'
authority: 3
not_to_be_confused_with:
- cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v
- spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor
see_also:
- spirit-crs800s-cs800-2021-specs-unit-block-diagram
- spirit-crs800s-cs800-2021-specs-tension-motor-connector-5-pin-m-minus-on-pin-1
- spirit-climber-2024-specs-resistance-system
source:
  ref: spirit-stepper-crs800s-2021-service-manual
  locator: 'CRS800S: 3. Electrical Configurations, PDF p. 9 (printed 9), text.md lines
    100-117. CS800(2020): PDF p. 11 (printed 10), lines 168-186, the same text in
    a two-column table'
  extracted_at: '2026-09-11'
---

Both 2020-version books print the same three-part page and, unlike the 2016 CS800 and the XS895
books, **no working voltage for the tension motor**.

| Part | Description printed |
|---|---|
| CONSOLE | Interface that controls all functions of the Stepper |
| MAIN CONTROLLER | The circuit board consists of the DC power supply for console |
| ECB BRAKE | It can change to increase or decrease resistance level of brake |

**General information:** CONSOLE - "Contains Key controls and LED Display. Main controller include
power supply, ECB driver control circuit."

**"ECB brake" is the page's name for the gear-motor magnetic brake** the rest of each book calls
the *tension motor* or *gear motor* - a motor winding a steel cable to move a magnet bracket
against the flywheel (`spirit-climber-2024-specs-resistance-system`). It is not a generator and
it is not the eddy-current brake of the 8.5S. The E2/Err pages give the drive voltage as
**Level UP +4~5 V DC, Level DOWN -4~5 V DC** on the console output (the CRS800S test procedure
widens it to +4~5.5 and -4~-5.5 V DC); that is a test reading, and the only voltage in either
book.

The 2016 CS800 book prints **DC 4~6 V** on this page
(`cs800-2016-specs-electrical-configuration-tension-motor-dc-4-to-6-v`); the XS895 prints
**DC 4.5~7.5 V** and adds an AC incline motor
(`spirit-xs895-specs-electrical-configuration-tension-motor-dc-4-5-to-7-5-v-and-ac-incline-motor`).

